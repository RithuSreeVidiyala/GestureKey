import cv2
from cvzone.HandTrackingModule import HandDetector
from pynput.keyboard import Key, Controller

cap = cv2.VideoCapture(0)
cap.set(3, 720)
cap.set(4, 420)

detector = HandDetector(detectionCon=0.7, maxHands=1)

keyboard = Controller()
while True:
    _, img = cap.read()
    hands, img = detector.findHands(img)
    if hands:
        fingers = detector.fingersUp(hands[0])
        if all(fingers): 
            keyboard.press(Key.right)
            keyboard.release(Key.left)
            keyboard.release(Key.up)
        elif not any(fingers):  
            keyboard.press(Key.left)
            keyboard.release(Key.right)
            keyboard.release(Key.up)
        elif fingers[0] and fingers[4]:  
            keyboard.press(Key.up)
            keyboard.release(Key.left)
            keyboard.release(Key.right)
        else:
            keyboard.release(Key.left)
            keyboard.release(Key.right)
            keyboard.release(Key.up)
    else:
        keyboard.release(Key.left)
        keyboard.release(Key.right)
        keyboard.release(Key.up)
    cv2.imshow("GestureKey", img)
    if cv2.waitKey(1) == ord("q"):
        break
