from django.shortcuts import get_object_or_404, render
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from django.http.response import JsonResponse
from BackendApp.serializers import AbonnementSerializer, CarSerializer, EntryTableSerializer, OutTableSerializer, TableCompletSerializer
from BackendApp.models import Abonnement, Car, TableComplet, EntryTable, OutTable

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.parsers import MultiPartParser, FormParser
from django.utils import timezone
from django.http import StreamingHttpResponse
import cv2
from ultralytics import YOLO
from django.http import StreamingHttpResponse
import math
import string
import easyocr
import time
from datetime import datetime,timedelta
import serial

def index(request):
    return render(request, 'base.html')

'''class VideoFeed(APIView):
    parser_classes = (MultiPartParser, FormParser)'''


model = YOLO('detection.pt')
classNames = ["plate_detection"]
arduino_port='COM4' # div/ttyACM0
baud_rate=9600
ser=serial.Serial(arduino_port,baud_rate,timeout=1)

# Initialize the OCR reader
reader = easyocr.Reader(['en'], gpu=False)

# Mapping dictionaries for character conversion
dict_char_to_int = {'O': '0',
                    'I': '1',
                    'J': '3',
                    'B': '3',
                    'A': '4',
                    'G': '6',
                    'S': '5'}

dict_int_to_char = {'0': 'O',
                    '1': 'I',
                    '3': 'J',
                    '4': 'A',
                    '6': 'G',
                    '5': 'S'}

def yolo():
    cap = cv2.VideoCapture(1)
    last_write_time = time.time()
    while True:
        ret, frame = cap.read()
        if not ret:
            print("Error: failed to capture image")
            break
        results = model(frame)[0]
        for r in results:
            boxes=r.boxes
            for box in boxes:
                x1,y1,x2,y2=box.xyxy[0]
                x1,y1,x2,y2=int(x1), int(y1), int(x2), int(y2)
                print(x1,y1,x2,y2)
                cv2.rectangle(frame, (x1,y1), (x2,y2), (255,0,255),3)
                conf=math.ceil((box.conf[0]*100))/100
                cls=int(box.cls[0])
                license_plate_crop = frame[int(y1):int(y2), int(x1): int(x2), :]
                mat,s =matricule(license_plate_crop)
                if mat is not None:
                    current_datetime = timezone.now()
                    if check_abonnement_existence(mat,current_datetime)==True:
                        if checkentrytable(mat)==False:
                            if checksortytable(mat)==True:
                                obj={'matricule':mat,'entry_time':current_datetime}
                                savetableentry(obj)
                                savetablecomplet(obj)
                                delettablesorty(mat)
                                ser.write('1'.encode())
                                last_write_time = time.time()
                                # Check if 10 seconds have passed since the last ser.write
                                if time.time() - last_write_time >= 10:
                                    break  # Exit the loop 
                            else:
                                obj={'matricule':mat,'entry_time':current_datetime}
                                savetableentry(obj)
                                savetablecomplet(obj)
                                ser.write('1'.encode())
                                last_write_time = time.time()
                                if time.time() - last_write_time >= 10:
                                    break  # Exit the loop
                        else:
                            entrytable=EntryTable.objects.get(matricule=mat)
                            savetablsorty({'matricule':mat,'entry_time': entrytable.entry_time,'out_time': current_datetime})
                            savetablecomplet({'matricule':mat,'entry_time': entrytable.entry_time,'out_time': current_datetime})
                            delettableentry(mat)
                            ser.write('1'.encode())
                            last_write_time = time.time()
                            if time.time() - last_write_time >= 10:
                                    break  # Exit the loop

                class_name=classNames[cls]
                label=f'{mat}  {s}'
                t_size = cv2.getTextSize(label, 0, fontScale=1, thickness=2)[0]
                c2 = x1 + t_size[0], y1 - t_size[1] - 3
                cv2.rectangle(frame, (x1,y1), c2, [255,0,255], -1, cv2.LINE_AA)  # filled
                cv2.putText(frame, label, (x1,y1-2),0, 1,[255,255,255], thickness=1,lineType=cv2.LINE_AA)
                # crop license plate
                
        yield frame

# #######################################################
# #######################################################

    
def checkoperation(mat,date):
    if check_abonnement_existence(mat,date)==True:
        if checkentrytable(mat)==False:
            if checksortytable(mat)==True:
                obj={'matricule':mat,'entry_time':date}
                savetableentry(obj)
                savetablecomplet(obj)
                delettablesorty(mat)
                ser.write('1'.encode())
                last_write_time = time.time()
         
            else:
                obj={'matricule':mat,'entry_time':date}
                savetableentry(obj)
                savetablecomplet(obj)
                ser.write('1'.encode())
                last_write_time = time.time()
        else:
            entrytable=EntryTable.objects.get(matricule=mat)
            savetablsorty({'matricule':mat,'entry_time': entrytable.entry_time,'out_time': date})
            savetablecomplet({'matricule':mat,'entry_time': entrytable.entry_time,'out_time': date})
            delettableentry(mat)
            ser.write('1'.encode())
            last_write_time = time.time()

def check_abonnement_existence(mat, date):
     # Get the Car instance based on the matricule
     try:
        print(mat)
        car = Car.objects.get(matricule=mat)
        print(car)
        # Check if the license plate exists in Abonnement
        license_plate_exists_in_abonnement = Abonnement.objects.filter(car__matricule=mat).exists()
        # Check if there is an abonnement for the given car that is active
        abonnement_exists = Abonnement.objects.filter(
            car_id=car.id,
            start_date__lte=date,
            end_date__gte=date
        ).exists()
        # Return True if the license plate exists in Abonnement and has an active abonnement, False otherwise
        if license_plate_exists_in_abonnement and abonnement_exists:
            return True
        else:
            return False
     except Car.DoesNotExist:
    # Handle the case where the Car with the specified matricule is not found
        print(f"Error: Car with matricule {mat} not found.")
        return False  

def savetablecomplet(obj):
    Table_serializer = TableCompletSerializer(data=obj)
    if Table_serializer.is_valid():
        Table_serializer.save()
        print('car save complet')
    
def savetablsorty(obj):
    Table_serializer = OutTableSerializer(data=obj)
    if Table_serializer.is_valid():
        Table_serializer.save()
        print('car save sorty')

def savetableentry(obj):
    Table_serializer = EntryTableSerializer(data=obj)
    if Table_serializer.is_valid():
        Table_serializer.save()
        print('car save entry')
    else:
        # Print validation errors if any
        print(f"Validation Errors: {Table_serializer.errors}")

def delettablesorty(mat):

    cars_to_delete = OutTable.objects.filter(matricule=mat)
    if cars_to_delete.exists():
        cars_to_delete.delete()
        print(f"Records with matricule {mat} deleted successfully from sorty table.")
    else:
        print(f"No records found with matricule {mat}. Nothing deleted from sorty table.")
  
def delettableentry(mat):

    cars_to_delete = EntryTable.objects.filter(matricule=mat)
    if cars_to_delete.exists():
        cars_to_delete.delete()
        print(f"Records with matricule {mat} deleted successfully from Entry table.")
    else:
        print(f"No records found with matricule {mat}. Nothing deleted from Entry table.")
    return True 

def checksortytable(mat):
    sorty = OutTable.objects.filter(matricule=mat)
    if not sorty.exists():
        return False
    return True

def checkentrytable(mat):
    entry = EntryTable.objects.filter(matricule=mat)
    if  not entry.exists():
        return False
    return True
    








#######################################################



def matricule(license_plate_crop):
    license_plate_crop_gray = cv2.cvtColor(license_plate_crop, cv2.COLOR_BGR2GRAY)
    blur = cv2.blur(license_plate_crop_gray,(5,5))
    ret1,th1 = cv2.threshold(blur,0,255,cv2.THRESH_BINARY+cv2.THRESH_OTSU)
    _, license_plate_crop_thresh = cv2.threshold(th1, 64, 255, cv2.THRESH_BINARY_INV)
    #_, license_plate_crop_thresh = cv2.threshold(license_plate_crop_gray, 64, 255, cv2.THRESH_BINARY_INV)

    # read license plate number
    license_plate_text, license_plate_text_score = read_license_plate(license_plate_crop_thresh)
    # if license_plate_text is not None:
    return license_plate_text,'{:.2f}'.format(license_plate_text_score)
    
def license_complies_format(text):
    """
    Check if the license plate text complies with the required format.

    Args:
        text (str): License plate text.

    Returns:
        bool: True if the license plate complies with the format, False otherwise.
    """
    if len(text) != 7:
        return False

    if (text[0] in string.ascii_uppercase or text[0] in dict_int_to_char.keys()) and \
       (text[1] in string.ascii_uppercase or text[1] in dict_int_to_char.keys()) and \
       (text[2] in ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9'] or text[2] in dict_char_to_int.keys()) and \
       (text[3] in ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9'] or text[3] in dict_char_to_int.keys()) and \
       (text[4] in string.ascii_uppercase or text[4] in dict_int_to_char.keys()) and \
       (text[5] in string.ascii_uppercase or text[5] in dict_int_to_char.keys()) and \
       (text[6] in string.ascii_uppercase or text[6] in dict_int_to_char.keys()):
        return True
    else:
        return False


def format_license(text):
    """
    Format the license plate text by converting characters using the mapping dictionaries.

    Args:
        text (str): License plate text.

    Returns:
        str: Formatted license plate text.
    """
    license_plate_ = ''
    mapping = {0: dict_int_to_char, 1: dict_int_to_char, 4: dict_int_to_char, 5: dict_int_to_char, 6: dict_int_to_char,
               2: dict_char_to_int, 3: dict_char_to_int}
    for j in [0, 1, 2, 3, 4, 5, 6]:
        if text[j] in mapping[j].keys():
            license_plate_ += mapping[j][text[j]]
        else:
            license_plate_ += text[j]

    return license_plate_


def read_license_plate(license_plate_crop):
    """
    Read the license plate text from the given cropped image.

    Args:
        license_plate_crop (PIL.Image.Image): Cropped image containing the license plate.

    Returns:
        tuple: Tuple containing the formatted license plate text and its confidence score.
    """
    
    detections = reader.readtext(license_plate_crop)

    for detection in detections:
        bbox, text, score = detection

        text = text.upper().replace(' ', '')

        if license_complies_format(text):
            return format_license(text), score

    return None , 0

#######################################################
def stream():
   
        yolo_output=yolo()
        for detection in yolo_output:
             
        #im0 = annotator.result()    
            image_bytes = cv2.imencode('.jpg', detection)[1].tobytes()
            yield (b'--frame\r\n'
                    b'Content-Type: image/jpeg\r\n\r\n' + image_bytes + b'\r\n')  

def video_feed(request):
    return StreamingHttpResponse(stream(), content_type='multipart/x-mixed-replace; boundary=frame')    


@csrf_exempt
def carApi(request, id=0):
    if request.method == 'GET' and id==0:
        cars = Car.objects.all()
        car_serializer = CarSerializer(cars, many=True)
        return JsonResponse(car_serializer.data, safe=False)
    
    elif request.method == 'GET':
        print(id)
        car = Car.objects.get(id=id)
        car_serializer = CarSerializer(car)
        return JsonResponse(car_serializer.data, safe=False)
    
    elif request.method == 'POST':
        car_data = JSONParser().parse(request)
        car_serializer = CarSerializer(data=car_data)
        if car_serializer.is_valid():
            car_serializer.save()
            return JsonResponse("Added Successfully", safe=False)
        return JsonResponse("Failed to Add", safe=False)
    
    elif request.method == 'PUT':
        car_data = JSONParser().parse(request)
        car = Car.objects.get(id=id)
        car_serializer = CarSerializer(car, data=car_data)
        if car_serializer.is_valid():
            car_serializer.save()
            return JsonResponse("Updated Successfully", safe=False)
        return JsonResponse("Failed to Update")
    
    elif request.method == 'DELETE':
        car = Car.objects.get(id=id)
        car.delete()
        return JsonResponse("Deleted Successfully", safe=False)

@csrf_exempt
def abonnementApi(request, id=0):
    if request.method == 'GET' and id==0:
        abonnements = Abonnement.objects.all()
        abonnement_serializer = AbonnementSerializer(abonnements, many=True)
        return JsonResponse(abonnement_serializer.data, safe=False)
    
    elif request.method == 'GET':
        print(id)
        abonnement = Abonnement.objects.get(id=id)
        abonnement_serializer = AbonnementSerializer(abonnement)
        return JsonResponse(abonnement_serializer.data, safe=False)

    elif request.method == 'POST':
        abonnement_data = JSONParser().parse(request)
        print(abonnement_data)
        abonnement_serializer = AbonnementSerializer(data=abonnement_data)
        if abonnement_serializer.is_valid():
            abonnement_serializer.save()
            return JsonResponse("Added Successfully", safe=False)
        print(abonnement_serializer.errors)
        return JsonResponse("Failed to Add", safe=False)
    
    elif request.method == 'PUT':
        abonnement_data = JSONParser().parse(request)
        abonnement = Abonnement.objects.get(id=id)
        abonnement_serializer = AbonnementSerializer(abonnement, data=abonnement_data)
        if abonnement_serializer.is_valid():
            abonnement_serializer.save()
            return JsonResponse("Updated Successfully", safe=False)
        return JsonResponse("Failed to Update")
    
    elif request.method == 'DELETE':
        abonnement = Abonnement.objects.get(id=id)
        abonnement.delete()
        return JsonResponse("Deleted Successfully", safe=False)

@csrf_exempt
def tableCompletApi(request, matricule=0):
    if request.method == 'GET' and matricule==0:
        tableComplet = TableComplet.objects.all()
        tableComplet_serializer = TableCompletSerializer(tableComplet, many=True)
        return JsonResponse(tableComplet_serializer.data, safe=False)
    
    elif request.method == 'GET':
        try:
            tableComplet = TableComplet.objects.filter(matricule=matricule)
            tableComplet_serializer = TableCompletSerializer(tableComplet, many=True)
            return JsonResponse(tableComplet_serializer.data, safe=False)
        except TableComplet.DoesNotExist:
            return JsonResponse("TableComplet not found", safe=False)
    
    elif request.method == 'POST':
        tableComplet_data = JSONParser().parse(request)
        tableComplet_serializer = TableCompletSerializer(data=tableComplet_data)
        if tableComplet_serializer.is_valid():
            tableComplet_serializer.save()
            return JsonResponse("Added Successfully", safe=False)
        return JsonResponse("Failed to Add", safe=False)
    
@csrf_exempt
def entryTableApi(request, id=0):
    if request.method == 'GET' and id==0:
        entryTable = EntryTable.objects.all()
        entryTable_serializer = EntryTableSerializer(entryTable, many=True)
        return JsonResponse(entryTable_serializer.data, safe=False)
    
    elif request.method == 'GET':
        print(id)
        entryTable = EntryTable.objects.get(id=id)
        entryTable_serializer = EntryTableSerializer(entryTable)
        return JsonResponse(entryTable_serializer.data, safe=False)
    
    elif request.method == 'POST':
        entryTable_data = JSONParser().parse(request)
        entryTable_serializer = EntryTableSerializer(data=entryTable_data)
        if entryTable_serializer.is_valid():
            entryTable_serializer.save()
            return JsonResponse("Added Successfully", safe=False)
        return JsonResponse("Failed to Add", safe=False)
    
    elif request.method == 'DELETE':
        entryTable = EntryTable.objects.get(id=id)
        entryTable.delete()
        return JsonResponse("Deleted Successfully", safe=False)
    
@csrf_exempt
def outTableApi(request, id=0):
    if request.method == 'GET' and id==0:
        outTable = OutTable.objects.all()
        outTable_serializer = OutTableSerializer(outTable, many=True)
        return JsonResponse(outTable_serializer.data, safe=False)
    
    elif request.method == 'GET':
        print(id)
        outTable = OutTable.objects.get(id=id)
        outTable_serializer = OutTableSerializer(outTable)
        return JsonResponse(outTable_serializer.data, safe=False)
    
    elif request.method == 'POST':
        outTable_data = JSONParser().parse(request)
        outTable_serializer = OutTableSerializer(data=outTable_data)
        if outTable_serializer.is_valid():
            outTable_serializer.save()
            return JsonResponse("Added Successfully", safe=False)
        return JsonResponse("Failed to Add", safe=False)
    
    elif request.method == 'DELETE':
        outTable = OutTable.objects.get(id=id)
        outTable.delete()
        return JsonResponse("Deleted Successfully", safe=False)