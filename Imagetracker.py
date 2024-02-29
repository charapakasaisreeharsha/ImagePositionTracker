import cv2
import mediapipe as mp
cap = cv2.VideoCapture(0)
draw_util = mp.solutions.drawing_utils #draw the border of the image
m_pose= mp.solutions.pose # predict the position

with m_pose.Pose(min_detection_confidence=0.5 ,min_tracking_confidence=0.5) as pose:
  while cap.isOpened():
    ret,frame =cap.read()

    #convert this bw to rgb
    rgb = cv2.cvtColor(frame,cv2. COLOR_BGR2RGB)

    # perform pose estimation
    out=pose.process(rgb)

    # marking the landmarks
    if out.pose_landmarks:
        draw_util.draw_landmarks(frame,out.pose_landmarks,m_pose.POSE_CONNECTIONS)

    cv2.imshow('pose estimation',frame)
    if cv2.waitKey(10) & 0XFF==ord('q'):
        break


cap.release()