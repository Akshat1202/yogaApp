import cv2
import mediapipe as mp
mp_pose = mp.solutions.pose

def get_landmark_coordinates(image_path):
    # Initialize a list to store x and y coordinates
    landmark_coordinates = []

    cap = cv2.VideoCapture(image_path)
    with mp_pose.Pose(min_detection_confidence=0.5, min_tracking_confidence=0.5) as pose:
        ret, frame = cap.read()
        image = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        image.flags.writeable = False
        results = pose.process(image)
        image.flags.writeable = True
        image = cv2.cvtColor(image, cv2.COLOR_RGB2BGR)
        
        # Extract landmarks
        landmarks = results.pose_landmarks.landmark

        # Extract x and y coordinates from the landmark subset
        for landmark in landmarks:
            x, y, z = landmark.x, landmark.y, landmark.z
            landmark_coordinates.append((x, y))

    return landmark_coordinates