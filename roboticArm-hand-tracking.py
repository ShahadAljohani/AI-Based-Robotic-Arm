import cv2, mediapipe as mp, serial, time, math

ARDUINO_PORT = 'COM3'
arduino = serial.Serial(ARDUINO_PORT, 115200, timeout=1)
time.sleep(2)

mp_hands = mp.solutions.hands.Hands(max_num_hands=1, min_detection_confidence=0.7)
draw = mp.solutions.drawing_utils
cap = cv2.VideoCapture(0)

last_sent = 0.0

def send(cmd):
    try:
        arduino.write(f"{cmd}\n".encode())
    except serial.SerialException:
        print("Serial write failed — check connection.")

try:
    while cap.isOpened():
        ok, frame = cap.read()
        if not ok:
            continue

        frame = cv2.flip(frame, 1)
        rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        res = mp_hands.process(rgb)

        if res.multi_hand_landmarks:
            hand = res.multi_hand_landmarks[0]
            #1st servo index fing
            idx_angle = int(hand.landmark[8].y * 180)
            idx_angle = max(0, min(idx_angle, 180))

            #2nd servo middle fing
            mid_angle = int(hand.landmark[12].y * 90)
            mid_angle = max(0, min(mid_angle, 90))

            #3rd servo ring fing
            ring_angle = int(hand.landmark[16].y * 90)
            ring_angle = max(0, min(ring_angle, 90))
            #thumb+index  4th servo-gripper
            x1, y1 = hand.landmark[4].x, hand.landmark[4].y
            x2, y2 = hand.landmark[8].x, hand.landmark[8].y
            dist = math.hypot(x2 - x1, y2 - y1)

            grip_state = 1 if dist < 0.05 else 0  
            now = time.time()
            if now - last_sent > 0.1:  #10 Hz
                send(f"S1:{idx_angle}")
                send(f"S2:{mid_angle}")
                send(f"S3:{ring_angle}")
                send(f"S4:{grip_state}")
                last_sent = now

            draw.draw_landmarks(frame, hand, mp.solutions.hands.HAND_CONNECTIONS)
            cv2.putText(frame, f"Index:{idx_angle} Mid:{mid_angle} Ring:{ring_angle} Grip:{grip_state}",
                        (10, 40), cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0,255,0), 2)
        cv2.imshow("Hand → Servo Control", frame)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

finally:
    cap.release()
    cv2.destroyAllWindows()
    arduino.close()
