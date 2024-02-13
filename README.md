# Smart Parking System

## Table of Contents
- [Introduction](#introduction)
- [Analysis and Design](#analysis-and-design)
- [Integration of YOLOv8](#integration-of-yolov8)
- [Arduino and Servomotor Usage](#arduino-and-servomotor-usage)
- [Technologies Used](#technologies-used)
- [Project Pipeline](#project-pipeline)
- [Features of "SmartParking"](#features-of-smartparking)

## Introduction

In a rapidly evolving world, urban resource management challenges continue to grow. Parking remains a major concern, affecting traffic flow, energy efficiency, and overall citizen experience. Our Smart Parking project integrates advanced technologies such as artificial intelligence (AI), embedded systems (Arduino and Raspberry Pi), and modern development tools like Angular and Django.

Our approach aims to transform parking spaces into intelligent environments capable of making real-time decisions to optimize resource usage. Arduino and Raspberry Pi ensure seamless integration of sensors and actuators, enabling precise data collection and system responsiveness. Additionally, web development technologies like Angular and Django provide a user-friendly interface and efficient data management.

## Demo
https://www.youtube.com/watch?v=kTJxuZgoJz4&t=12s

## Analysis and Design

### Identifications of Actors
- **Administrator**: Manages and communicates within the platform, overseeing clients, subscriptions, and reports.
- **Client**: Proactively contacts the administrator to subscribe to SmartParking.

### Rules of Management and Organization
- The application can have one or more administrators.
- Authentication requires a valid username and password for administrators.
- Only the administrator can manage key system resources such as clients, subscriptions, reports, and emails.
- ...

For more details, refer to the [full analysis and design section](#analysis-and-design) in the project documentation.

## Integration of YOLOv8

### YOLO
YOLO (You Only Look Once) is a revolutionary object detection algorithm in deep learning. It divides the image into a grid, predicting bounding boxes and object classes for each grid cell in a single pass. YOLO's unique approach provides exceptional speed, making it suitable for real-time object detection in images and videos.

For a detailed understanding of YOLO, refer to the [full YOLO integration section](#integration-of-yolov8) in the project documentation.

## Arduino and Servomotor Usage

The Smart Parking system utilizes Arduino and a Servomotor for efficient control of parking barriers. The pipeline of the project involves the following steps:

For more details on the Arduino and Servomotor usage, refer to the [full Arduino and Servomotor section](#arduino-and-servomotor-usage) in the project documentation.

## Technologies Used

- **Django**: Web framework for backend development.
- **Angular**: Frontend framework for building user interfaces.
- **MySQL**: Database management system.
- **Arduino**: Platform for building electronic projects.
- **Raspberry Pi 4**: Single-board computer for embedded systems.
- **Servomotor**: Actuator for controlling parking barriers.

For more details on the technologies used, refer to the [full technologies section](#technologies-used) in the project documentation.

## Project Pipeline

The project pipeline outlines the steps involved in the Smart Parking system development:

1. **Plate License Coordinates Detection:**
    - Fine-tune the Deep Learning Model (YOLO):
      - Collect Dataset
      - Dataset preprocessing
      - Model Development
      - Results Evaluation

2. **Frame Processing:**
    - Organize the frame to obtain license plate coordinates.

3. **Frame Illumination:**
    - Apply filters to illuminate the frame.

4. **License Plate Extraction:**
    - Extract characters from the frame.
    - Validate the license plate format (e.g., UK format: char char int int char char char).
    - Correct errors (e.g., conflict of 0 and O).

5. **Subscription Verification:**
    - Send the obtained license plate to the database to check if it is associated with a car with an active subscription.

6. **Signal Transmission to Arduino:**
    - If the license plate is linked to an active subscription, Raspberry Pi sends a signal to Arduino to open the barrier.

For more details on the project pipeline, refer to the [full project pipeline section](#project-pipeline) in the project documentation.

## Features of "SmartParking"

### Authentication and Administrative Interface
- The administrator authenticates to access the administrative interface.
- The platform provides a comprehensive view, displaying the camera feed and a monitoring table of incoming and outgoing vehicles.

For more details on the features of SmartParking, refer to the [full features section](#features-of-smartparking) in the project documentation.

**Note:** The provided content is a summary, and detailed information can be found in the full project documentation.

**Happy coding!**
