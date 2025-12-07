# Robotic-Arm
An AI-based moveable robotic arm that can replicate hand movements in real time using computer vision and servo actuation.

### Implementation

#### Mechanical Design:
Designing an arm joint using OnShape app, a parametric CAD tool, by my experience of designing 3D mechanical models.

<img width="927" height="667" alt="Screenshot (578)" src="https://github.com/user-attachments/assets/c83b4a57-9e7c-4dbf-9bc2-cda81ba19f0a" />

-each joint was carefully modeled to fit servo motors
-in this design i considered torque distribution and motion range for precise control.

Check out my [Robotic Joint Design](https://github.com/ShahadAljohani/Robotic-Joint-Mechanical-Design/tree/main)

#### Electrical Integration:
I integrated the electrical system using an arduino controller.
-4 servo motors were carefully placed to control the base rotation, shoulder, elbow, and the gripper. 
-wires and connections were carefully arranged (each color represent a specific meaning and path) for signal control.
-soldered the servos horn in a specific length suitable for the 3D design models.

#### Assembly of the Robotic Arm 
-collected all 3D components
-servos was poitioned to align each joint
-joints were reinforced with nails and screws for the structural durability
assembling the arm for smooth movements.


#### robotic arm movement:
The motion of the arm is controlled via Arudino IDE, writing a code for reading servo poritions and execute movements.
-each servo's range of motion and speed was specified to provide coorinated movement across all joints.


#### AI integration of the robotic movement:
Using OpenCV and MediaPipe, the code tracks the hand landmarks in real time by mapping finger positions to servo angles, and send commands for the Arduino for precise movements.
-Robotic arm can mimic hans gestures and adjusting joing angles dynamically.



