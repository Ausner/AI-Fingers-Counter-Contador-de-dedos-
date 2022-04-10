import cv2
from cvzone.HandTrackingModule import HandDetector

cap = cv2.VideoCapture(0)
cap.set(cv2.CAP_PROP_FRAME_WIDTH, 1500)
cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 1500)
detector = HandDetector(detectionCon=0.8, maxHands=2)

while (True):
    success, img = cap.read()
    hands, img = detector.findHands(img) #With draw
    #hands = detector.findHands(img, draw=False) #No draw


    if hands:
        hand1 = hands[0]
        lmList1 = hand1["lmList"]
        bbox1 = hand1["bbox"]
        centerPoint1 = hand1["center"]
        handType1 = hand1["type"]

        fingers1= detector.fingersUp(hand1)


        if len(hands)==2:
            hand2 = hands[1]
            lmList2 = hand2["lmList"]
            bbox2 = hand2["bbox"]
            centerPoint2 = hand1["center"]
            handType2 = hand2["type"]

            fingers2= detector.fingersUp(hand2)

            #print(fingers1, fingers2)
            #length, info, img = detector.findDistance(centerPoint1, centerPoint2, img)
            leftFingers = 0
            rigthFingers = 0
            for finger_left in fingers1:
                if finger_left:
                    leftFingers += 1
            


            for finger_rigth in fingers2:
                if finger_rigth:
                    rigthFingers += 1 

            totalFingers = leftFingers + rigthFingers
            text = "TOTAL DEDOS LEVANTADOS: "
            text += str(totalFingers)
            cv2.putText(img, text, (100, 50), cv2.FONT_HERSHEY_TRIPLEX,1,(255,255,255),1)
        else:
            my_fingers = 0
            for finger_hand in fingers1:
                if finger_hand:
                    my_fingers += 1
            
            text = "TOTAL DEDOS LEVANTADOS: "
            text += str(my_fingers)
            cv2.putText(img, text, (100, 50), cv2.FONT_HERSHEY_TRIPLEX,1,(255,255,255),1)

    cv2.imshow("Image", img)
    cv2.waitKey(1)

