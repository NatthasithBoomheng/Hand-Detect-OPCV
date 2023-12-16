import cv2
import mediapipe as mp

camera = cv2.VideoCapture(0)
mpHands = mp.solutions.hands
hands = mpHands.Hands()
mpDraw = mp.solutions.drawing_utils
number = 0

while True:
    sccuess, img = camera.read()
    imageRBG = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    results = hands.process(imageRBG)
    if results.multi_hand_landmarks:
        for lanmark in results.multi_hand_landmarks:
            mpDraw.draw_landmarks(img,lanmark,mpHands.HAND_CONNECTIONS)

            if lanmark.landmark[mpHands.HandLandmark.INDEX_FINGER_TIP].y > lanmark.landmark[mpHands.HandLandmark.INDEX_FINGER_DIP].y :
                number1 = 0
            else:
                number1 = 1

            if lanmark.landmark[mpHands.HandLandmark.MIDDLE_FINGER_TIP].y > lanmark.landmark[mpHands.HandLandmark.MIDDLE_FINGER_DIP].y :
                number2 = 0
            else:
                number2 = 1

            if lanmark.landmark[mpHands.HandLandmark.RING_FINGER_TIP].y > lanmark.landmark[mpHands.HandLandmark.RING_FINGER_DIP].y :
                number3 = 0
            else:
                number3 = 1
            
            if lanmark.landmark[mpHands.HandLandmark.PINKY_TIP].y > lanmark.landmark[mpHands.HandLandmark.PINKY_DIP].y :
                number4 = 0
            else:
                number4 = 1
            
            if lanmark.landmark[mpHands.HandLandmark.THUMB_TIP].y > lanmark.landmark[mpHands.HandLandmark.RING_FINGER_MCP].y :
                number5 = 0
            else:
                number5 = 1
            
            number = str(number1 + number2 + number3 + number4 + number5)
            cv2.putText(img, ("Number on hand : " + number), (0, 50), cv2.FONT_HERSHEY_TRIPLEX, 1, (23, 32, 42), 2)

    cv2.imshow("Cam", img)
    if cv2.waitKey(1) & 0xFF == ord("e"):
        break