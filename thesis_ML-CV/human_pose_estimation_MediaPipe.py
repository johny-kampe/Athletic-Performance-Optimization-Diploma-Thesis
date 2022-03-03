import mediapipe as mp
import xlwt
import cv2
import os


mpPose = mp.solutions.pose
pose = mpPose.Pose()
mpDraw = mp.solutions.drawing_utils

def single_video_find_landmarks_human_pose_estimation(sheet_set_csv, set_csv, folder, name_csv):
    ''' This function is getting a single video from a specific folder and then it detects the human pose.
        Then the pixel values are stored in a specific .csv file '''

    print('Detecting and extracting landmarks values..\n.\n.\n.')
    rows12 = 0
    rows14 = 0
    rows16 = 0

    path = folder + 'DSC_0079_Trim.mp4'  # use any video that you like from any set
    cap = cv2.VideoCapture(path)
    print(f"Video's path: {path}")
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
                cv2.circle(img, (cx, cy), 6, (0, 0, 255),
                           cv2.FILLED)  # print a red filled circle on the detected joint

                if id == 12:  # right shoulder -> insert it at the right column and row in the .csv
                    sheet_set_csv.write(rows12 + 1, 0, cx)
                    sheet_set_csv.write(rows12 + 1, 1, cy)
                    rows12 += 1
                elif id == 14:  # right elbow -> insert it at the right column and row in the .csv
                    sheet_set_csv.write(rows14 + 1, 2, cx)
                    sheet_set_csv.write(rows14 + 1, 3, cy)
                    rows14 += 1
                elif id == 16:  # right wrist -> insert it at the right column and row in the .csv
                    sheet_set_csv.write(rows16 + 1, 4, cx)
                    sheet_set_csv.write(rows16 + 1, 5, cy)
                    rows16 += 1
                set_csv.save(name_csv)

        img = cv2.resize(img, (960, 540))  # resize at the display window, not at the input video (!)
        cv2.imshow("Pose Detection Result", img)
        cv2.waitKey(1)

def multiple_videos_find_landmarks_human_pose_estimation(sheet_set_csv, set_csv, folder, name_csv):
    ''' This function is getting every video from a folder, then it detects the human pose
    and finally the pixel values of right wrist, elbow and shoulder are stored in a specific .csv file '''

    print('Detecting and extracting landmarks values..\n.\n.\n.')
    rows12 = 0
    rows14 = 0
    rows16 = 0

    for filename in os.listdir(folder):
        cap = cv2.VideoCapture(folder+filename)
        print(f"Video's path: {folder + filename}")
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

                    if id == 12:  # right shoulder -> insert it at the right column and row in the .csv
                        sheet_set_csv.write(rows12 + 1, 0, cx)
                        sheet_set_csv.write(rows12 + 1, 1, cy)
                        rows12 += 1
                    elif id == 14:  # right elbow -> insert it at the right column and row in the .csv
                        sheet_set_csv.write(rows14 + 1, 2, cx)
                        sheet_set_csv.write(rows14 + 1, 3, cy)
                        rows14 += 1
                    elif id == 16:  # right wrist -> insert it at the right column and row in the .csv
                        sheet_set_csv.write(rows16 + 1, 4, cx)
                        sheet_set_csv.write(rows16 + 1, 5, cy)
                        rows16 += 1
                    # print(id, cx, cy)
                    set_csv.save(name_csv)

            img = cv2.resize(img, (960, 540))  # resize at the display window, not at the input video (!)
            cv2.imshow("Pose Detection Result", img)
            cv2.waitKey(1)


style = xlwt.easyxf('font: bold 1')  # Specifying style for the .csv files
dataset_xls = xlwt.Workbook()  # Workbook for training set
real_world_set_A_xls = xlwt.Workbook()  # Workbook for test set of athlete A
real_world_set_B_xls = xlwt.Workbook()  # Workbook for test set of athlete B

sheet_dataset = dataset_xls.add_sheet('Sheet 1')  # add_sheet is used to create sheet in .csv
sheet_real_world_set_A = real_world_set_A_xls.add_sheet('Sheet 1')
sheet_real_world_set_B = real_world_set_B_xls.add_sheet('Sheet 1')

sheet_dataset.write(0, 0, 'Right shoulder x', style)  # adding names to the columns of training_set_csv
sheet_dataset.write(0, 1, 'Right shoulder y', style)  # to recognize the data that we have
sheet_dataset.write(0, 2, 'Right elbow x', style)
sheet_dataset.write(0, 3, 'Right elbow y', style)
sheet_dataset.write(0, 4, 'Right wrist x', style)
sheet_dataset.write(0, 5, 'Right wrist y', style)

sheet_real_world_set_A.write(0, 0, 'Right shoulder x', style)  # adding names to the columns of test_set_A_csv
sheet_real_world_set_A.write(0, 1, 'Right shoulder y', style)  # to recognize the data that we have
sheet_real_world_set_A.write(0, 2, 'Right elbow x', style)
sheet_real_world_set_A.write(0, 3, 'Right elbow y', style)
sheet_real_world_set_A.write(0, 4, 'Right wrist x', style)
sheet_real_world_set_A.write(0, 5, 'Right wrist y', style)

sheet_real_world_set_B.write(0, 0, 'Right shoulder x', style)  # adding names to the columns of test_set_B_csv
sheet_real_world_set_B.write(0, 1, 'Right shoulder y', style)  # to recognize the data that we have
sheet_real_world_set_B.write(0, 2, 'Right elbow x', style)
sheet_real_world_set_B.write(0, 3, 'Right elbow y', style)
sheet_real_world_set_B.write(0, 4, 'Right wrist x', style)
sheet_real_world_set_B.write(0, 5, 'Right wrist y', style)

training_set_folder = "D:/Diploma-Thesis/thesis_ML-CV/dataset/"
test_set_A_folder = "D:/Diploma-Thesis/thesis_ML-CV/real_world_set_A/"
test_set_B_folder = "D:/Diploma-Thesis/thesis_ML-CV/real_world_set_B/"

xls_name_training = "dataset.xls"
xls_name_test_A = "real_world_set_A.xls"
xls_name_test_B = "real_world_set_B.xls"

multiple_videos_find_landmarks_human_pose_estimation(sheet_dataset, dataset_xls, training_set_folder, xls_name_training)
# single_video_find_landmarks_human_pose_estimation(sheet_real_world_set_A, real_world_set_A_xls, test_set_A_folder, xls_name_test_A)
# single_video_find_landmarks_human_pose_estimation(sheet_real_world_set_B, real_world_set_B_xls, test_set_B_folder, xls_name_test_B)
