import cv2
import mediapipe as mp
import xlwt

mpPose = mp.solutions.pose
pose = mpPose.Pose()
mpDraw = mp.solutions.drawing_utils

cap = cv2.VideoCapture('DSC_0042.MOV')

style = xlwt.easyxf('font: bold 1')  # Specifying style
wb = xlwt.Workbook()  # Workbook is created
sheet1 = wb.add_sheet('Sheet 1')  # add_sheet is used to create sheet.

sheet1.write(0, 0, 'Right shoulder', style)
sheet1.write(0, 2, 'Right elbow', style)
sheet1.write(0, 4, 'Right wrist', style)
rows12 = 0
rows14 = 0
rows16 = 0

joints_dict = {}
while True:
    success, img = cap.read()
    imgRGB = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    results = pose.process(imgRGB)

    if results.pose_landmarks:
        mpDraw.draw_landmarks(img, results.pose_landmarks, mpPose.POSE_CONNECTIONS)
        for id, lm in enumerate(results.pose_landmarks.landmark):
            h, w, c = img.shape  # get image's width, height and channel
            cx, cy = int(lm.x * w), int(lm.y * h)  # convert normalized values to real pixel values
            cv2.circle(img, (cx, cy), 6, (0, 0, 255), cv2.FILLED)  # print a red filled circle on the detected joint

            if id == 12:  # right shoulder -> insert it at the right column and row in the excl
                sheet1.write(rows12 + 1, 0, cx)
                sheet1.write(rows12 + 1, 1, cy)
                rows12 += 1
            elif id == 14:  # right elbow -> insert it at the right column and row in the excl
                sheet1.write(rows14 + 1, 2, cx)
                sheet1.write(rows14 + 1, 3, cy)
                rows14 += 1
            elif id == 16:  # right wrist -> insert it at the right column and row in the excl
                sheet1.write(rows16 + 1, 4, cx)
                sheet1.write(rows16 + 1, 5, cy)
                rows16 += 1
            print(id, cx, cy)
            wb.save('athletic_performance_optimization_PERFECT_SET.xls')

    img = cv2.resize(img, (960, 540))  # resize at the display window, not at the input video (!)
    cv2.imshow("Pose Detection Result", img)
    cv2.waitKey(1)

