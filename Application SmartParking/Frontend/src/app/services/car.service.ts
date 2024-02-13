import { Injectable } from '@angular/core';
import { Observable } from 'rxjs';
import { WebRequestService } from './web-request-service';

@Injectable({
  providedIn: 'root'
})
export class CarService {

  constructor(private _webReqService: WebRequestService) { }

  createCar(jsonData: any) : Observable<any>{
    return this._webReqService.post('car', jsonData) 
  }

  getCar(){
    return this._webReqService.get('car')  ;
  }

  getOneCar(id: string){
    return this._webReqService.get(`car/${id}`);
  }

  editCar(id: string, jsonData: any){
    return this._webReqService.put(`car/${id}`, jsonData)  ;
  }

  deleteCar(id: string){
    return this._webReqService.delete(`car/${id}`);
  }

}
