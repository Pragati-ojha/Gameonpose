import cv2
import mediapipe as mp
import math
import pyautogui

mp_pose = mp.solutions.pose
mp_draw = mp.solutions.drawing_utils

pose = mp_pose.Pose()
cap = cv2.VideoCapture(0)
enter_key_pressed = False

def calculate_angle(point1, point2):
    angle_radians = math.atan2(point2.y - point1.y, point2.x - point1.x)
    return math.degrees(angle_radians)

def gop():
    while True:
        ret, img = cap.read()
        img = cv2.resize(img, (600, 400))

        results = pose.process(img)
        mp_draw.draw_landmarks(img, results.pose_landmarks, landmark_drawing_spec=mp_draw.DrawingSpec(color=(0, 0, 255), thickness=2, circle_radius=2))

        if results.pose_landmarks:
            right_elbow = results.pose_landmarks.landmark[mp_pose.PoseLandmark.RIGHT_ELBOW]
            right_wrist = results.pose_landmarks.landmark[mp_pose.PoseLandmark.RIGHT_WRIST]
            left_elbow = results.pose_landmarks.landmark[mp_pose.PoseLandmark.LEFT_ELBOW]
            left_wrist = results.pose_landmarks.landmark[mp_pose.PoseLandmark.LEFT_WRIST]
            right_shoulder = results.pose_landmarks.landmark[mp_pose.PoseLandmark.RIGHT_SHOULDER]
            left_shoulder = results.pose_landmarks.landmark[mp_pose.PoseLandmark.LEFT_SHOULDER]

            if right_shoulder and right_elbow and left_shoulder and left_elbow:
                ls = calculate_angle(left_shoulder, left_elbow)
                rs = calculate_angle(right_shoulder, right_elbow)

                if (rs > 140 and rs < 180) and (ls < 50 and ls > 0):
                    exit()

            if right_elbow and right_wrist:
                angle_degrees = calculate_angle(right_elbow, right_wrist)

                if (angle_degrees > 100 and angle_degrees < 180) and (rs > 90 and rs < 120):
                    pyautogui.keyDown('right')
                else:
                    pyautogui.keyUp('right')

                if (rs > 140 and rs < 180) and (-120 < angle_degrees < -84):
                    if not enter_key_pressed:
                        pyautogui.press('enter')
                        enter_key_pressed = True
                else:
                    enter_key_pressed = False

            if left_elbow and left_wrist:
                angle_degrees = calculate_angle(left_elbow, left_wrist)

                if (angle_degrees <= 70 and angle_degrees > 0) and (50 < ls < 90):
                    pyautogui.keyDown('left')
                else:
                    pyautogui.keyUp('left')

        cv2.imshow("Pose", img)

        if cv2.waitKey(1) & 0xFF == 27:  # Press the Esc key to exit
            break

    cap.release()
    cv2.destroyAllWindows()


