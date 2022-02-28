import cv2
import mediapipe as mp

mpPose = mp.solutions.pose
pose = mpPose.Pose()
mpDraw = mp.solutions.drawing_utils

cap = cv2.VideoCapture('DSC_0042.MOV')

joints_dict = {}
while True:
    success, img = cap.read()
    imgRGB = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    results = pose.process(imgRGB)

    if results.pose_landmarks:
        mpDraw.draw_landmarks(img, results.pose_landmarks, mpPose.POSE_CONNECTIONS)
        for id, lm in enumerate(results.pose_landmarks.landmark):
            h, w, c = img.shape
            # print(id, lm)
            cx, cy = int(lm.x * w), int(lm.y * h)

            cv2.circle(img, (cx, cy), 8, (255, 255, 0), cv2.FILLED)
            # if id == 12 or id == 14 or id == 16:
            #     print(id, cx, cy)
            #     joints_dict[id] =

    print(joints_dict)
    img = cv2.resize(img, (960, 540))
    cv2.imshow("Pose Detection Model", img)
    cv2.waitKey(1)

