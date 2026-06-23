# Robotic-Arm
An AI-based moveable robotic arm that can replicate hand movements in real time using computer vision and servo actuation.

<img width="960" height="1280" alt="RoboticArm_finalHead" src="https://github.com/user-attachments/assets/dde1fd85-8be8-42d7-8abc-2c0dd8de0b75" />



### Implementation:


#### Mechanical Design:
Designed an arm joint using OnShape app, a parametric CAD tool, by my experience of designing 3D mechanical models.

<img width="927" height="667" alt="Screenshot (578)" src="https://github.com/user-attachments/assets/c83b4a57-9e7c-4dbf-9bc2-cda81ba19f0a" />

-each joint was carefully modeled to fit servo motors

-in this design i considered torque distribution and motion range for precise control.

Check out my [Robotic Joint Design](https://github.com/ShahadAljohani/Robotic-Joint-Mechanical-Design/tree/main)


#### Electrical Integration:
Integrated the electrical system using an arduino controller.
-4 servo motors were carefully placed to control the base rotation, shoulder, elbow, and the gripper. 

-Wires and connections were carefully arranged (each color represent a specific meaning and path) for signal control.

-Soldered the servos horn in a specific length suitable for the 3D design models.

<img width="839" height="1186" alt="RoboticArm_preFinal" src="https://github.com/user-attachments/assets/1c64e846-49ab-4e10-a692-834c18ae257a" />


#### Web Page Controller:
Designed and developed a web-based control system for the robotic arm using HTML, CSS, JavaScript, and PHP, with MySQL (phpMyAdmin) for data storage and management. 
The interface provides a modern, simple, and user-friendly UI/UX that allows users to control the robotic arm in real time and save movement configurations for later use.

-Built the frontend using HTML, CSS, and JavaScript to create an interactive control dashboard.

-Developed backend logic using PHP to handle user inputs and system communication.

-Integrated MySQL database (via phpMyAdmin) to store and retrieve saved arm positions and movement patterns.

-Enabled saving and loading of predefined control settings for repeated and efficient operation.

<img width="1849" height="863" alt="WebPage" src="https://github.com/user-attachments/assets/c447925d-70f8-4d5e-8d59-9afc1de5250a" />


[View and Try Web Controller](https://github.com/ShahadAljohani/SuT_Web_Task3)



#### AI for hand gesture:
Implemented a hand gesture recognition system using OpenCV and MediaPipe, the code tracks the hand landmarks in real time by mapping finger positions to servo angles, and send commands for the Arduino to enable real-time, contactless control of the robotic arm. 


-Captured live video feed using a camera for real-time processing.

-Detected and tracked hand landmarks using computer vision techniques.

-Mapped specific gestures to predefined robotic arm movements.

-Enabled real-time translation of human hand gestures into robotic control signals.

-Robotic arm can mimic hans gestures and adjusting joing angles dynamically.

<img width="1143" height="403" alt="hand-landmark" src="https://github.com/user-attachments/assets/85fb8690-67a2-4b37-8c87-dbcb505e9d6f" />

* Find out the code in the `roboticArm-hand-tracking.py` file 


#### Assembly of the Robotic Arm:
-collected all 3D components

-servos was positioned to align each joint

-joints were reinforced with nails and screws for the structural durability
assembling the arm for smooth movements.

-different parts connected together via **soldering**:

https://github.com/user-attachments/assets/5a83c4cc-7c8b-4fc3-aaaa-7a5b76bfdb84





#### robotic arm movement:
The motion of the arm is controlled via Arudino IDE, writing a code for reading servo poritions and execute movements.
-each servo's range of motion and speed was specified to provide coorinated movement across all joints.



https://github.com/user-attachments/assets/965cd0fb-dc11-4661-93c7-1129840395cf






