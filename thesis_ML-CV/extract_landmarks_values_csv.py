import mediapipe as mp
import xlwt
import cv2
import os

mpPose = mp.solutions.pose
pose = mpPose.Pose()
mpDraw = mp.solutions.drawing_utils


def get_landmarks_pixel_values_excel(sheet_set_csv, set_csv, folder):
    ''' This function is getting every video from a folder, then it makes the detection
    and then the pixel values are stored in a specific .csv file '''

    print('Detecting and extracting landmarks values..\n.\n.\n.')
    rows12 = 0
    rows14 = 0
    rows16 = 0

    # folder = "D:/Diploma-Thesis/thesis_ML-CV/train/"
    # cap = cv2.VideoCapture(folder+'DSC_0018.MOV')
    #
    for filename in os.listdir(folder):
        cap = cv2.VideoCapture(folder+filename)
        print(folder+filename)
        while True:
            success, img = cap.read()
            if not success:
                print('Done!')
                break
            imgRGB = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
            results = pose.process(imgRGB)

            if results.pose_landmarks:
                mpDraw.draw_landmarks(img, results.pose_landmarks, mpPose.POSE_CONNECTIONS)
                for id, lm in enumerate(results.pose_landmarks.landmark):
                    h, w, c = img.shape  # get image's width, height and channel
                    cx, cy = int(lm.x * w), int(lm.y * h)  # convert normalized values to real pixel values
                    cv2.circle(img, (cx, cy), 6, (0, 0, 255), cv2.FILLED)  # print a red filled circle on the detected joint

                    if id == 12:  # right shoulder -> insert it at the right column and row in the excl
                        sheet_set_csv.write(rows12 + 1, 0, cx)
                        sheet_set_csv.write(rows12 + 1, 1, cy)
                        rows12 += 1
                    elif id == 14:  # right elbow -> insert it at the right column and row in the excl
                        sheet_set_csv.write(rows14 + 1, 2, cx)
                        sheet_set_csv.write(rows14 + 1, 3, cy)
                        rows14 += 1
                    elif id == 16:  # right wrist -> insert it at the right column and row in the excl
                        sheet_set_csv.write(rows16 + 1, 4, cx)
                        sheet_set_csv.write(rows16 + 1, 5, cy)
                        rows16 += 1
                    # print(id, cx, cy)
                    set_csv.save('athletic_performance_optimization_PERFECT_SET.xls')

            img = cv2.resize(img, (960, 540))  # resize at the display window, not at the input video (!)
            cv2.imshow("Pose Detection Result", img)
            cv2.waitKey(1)


style = xlwt.easyxf('font: bold 1')  # Specifying style for the excel files
training_set_csv = xlwt.Workbook()  # Workbook for training set
test_set_A_csv = xlwt.Workbook()  # Workbook for test set of athlete A
test_set_B_csv = xlwt.Workbook()  # Workbook for test set of athlete B

sheet_training_set = training_set_csv.add_sheet('Sheet 1')  # add_sheet is used to create sheet in excel
sheet_test_set_A = test_set_A_csv.add_sheet('Sheet 1')
sheet_test_set_B = test_set_B_csv.add_sheet('Sheet 1')

sheet_training_set.write(0, 0, 'Right shoulder x', style)  # adding names to the columns of training_set.csv to recognize
sheet_training_set.write(0, 1, 'Right shoulder y', style)  # the data that we have
sheet_training_set.write(0, 2, 'Right elbow x', style)
sheet_training_set.write(0, 3, 'Right elbow y', style)
sheet_training_set.write(0, 4, 'Right wrist x', style)
sheet_training_set.write(0, 5, 'Right wrist y', style)

sheet_test_set_A.write(0, 0, 'Right shoulder x', style)  # adding names to the columns of test_set_A.csv to recognize
sheet_test_set_A.write(0, 1, 'Right shoulder y', style)  # the data that we have
sheet_test_set_A.write(0, 2, 'Right elbow x', style)
sheet_test_set_A.write(0, 3, 'Right elbow y', style)
sheet_test_set_A.write(0, 4, 'Right wrist x', style)
sheet_test_set_A.write(0, 5, 'Right wrist y', style)

sheet_test_set_B.write(0, 0, 'Right shoulder x', style)  # adding names to the columns of test_set_B.csv to recognize
sheet_test_set_B.write(0, 1, 'Right shoulder y', style)  # the data that we have
sheet_test_set_B.write(0, 2, 'Right elbow x', style)
sheet_test_set_B.write(0, 3, 'Right elbow y', style)
sheet_test_set_B.write(0, 4, 'Right wrist x', style)
sheet_test_set_B.write(0, 5, 'Right wrist y', style)

training_set_folder = "D:/Diploma-Thesis/thesis_ML-CV/training_set/"
test_set_A_folder = "D:/Diploma-Thesis/thesis_ML-CV/test_set_A/"
test_set_B_folder = "D:/Diploma-Thesis/thesis_ML-CV/test_set_B/"


get_landmarks_pixel_values_excel(sheet_training_set, training_set_csv, training_set_folder)
# get_landmarks_pixel_values_excel(sheet_test_set_A, test_set_A_csv, test_set_A_folder)
# get_landmarks_pixel_values_excel(sheet_test_set_B, test_set_B_csv, test_set_B_folder)
