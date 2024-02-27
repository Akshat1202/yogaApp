from calcangle import calculateAngle
import mediapipe as mp
mp_pose = mp.solutions.pose

def evaluate_vakrasana_pose(landmarks):
    suggestions = []
    class Stage:
        one = 1
        two = 2
        three = 3
    
    left_elbow_angle = calculateAngle(landmarks[mp_pose.PoseLandmark.LEFT_SHOULDER.value],
                                    landmarks[mp_pose.PoseLandmark.LEFT_ELBOW.value],
                                    landmarks[mp_pose.PoseLandmark.LEFT_WRIST.value])

    right_elbow_angle = calculateAngle(landmarks[mp_pose.PoseLandmark.RIGHT_SHOULDER.value],
                                     landmarks[mp_pose.PoseLandmark.RIGHT_ELBOW.value],
                                     landmarks[mp_pose.PoseLandmark.RIGHT_WRIST.value])

    left_shoulder_angle = calculateAngle(landmarks[mp_pose.PoseLandmark.LEFT_ELBOW.value],
                                        landmarks[mp_pose.PoseLandmark.LEFT_SHOULDER.value],
                                        landmarks[mp_pose.PoseLandmark.LEFT_HIP.value])

    right_shoulder_angle = calculateAngle(landmarks[mp_pose.PoseLandmark.RIGHT_HIP.value],
                                         landmarks[mp_pose.PoseLandmark.RIGHT_SHOULDER.value],
                                         landmarks[mp_pose.PoseLandmark.RIGHT_ELBOW.value])

    left_knee_angle = calculateAngle(landmarks[mp_pose.PoseLandmark.LEFT_HIP.value],
                                    landmarks[mp_pose.PoseLandmark.LEFT_KNEE.value],
                                    landmarks[mp_pose.PoseLandmark.LEFT_ANKLE.value])

    right_knee_angle = calculateAngle(landmarks[mp_pose.PoseLandmark.RIGHT_HIP.value],
                                     landmarks[mp_pose.PoseLandmark.RIGHT_KNEE.value],
                                     landmarks[mp_pose.PoseLandmark.RIGHT_ANKLE.value])

    left_hip_s_angle = calculateAngle(landmarks[mp_pose.PoseLandmark.LEFT_SHOULDER.value],
                                    landmarks[mp_pose.PoseLandmark.LEFT_HIP.value],
                                    landmarks[mp_pose.PoseLandmark.LEFT_KNEE.value])

    right_hip_s_angle = calculateAngle(landmarks[mp_pose.PoseLandmark.RIGHT_SHOULDER.value],
                                     landmarks[mp_pose.PoseLandmark.RIGHT_HIP.value],
                                     landmarks[mp_pose.PoseLandmark.RIGHT_KNEE.value])
   
    left_hip_angle=calculateAngle(landmarks[mp_pose.PoseLandmark.NOSE.value],
                                          landmarks[mp_pose.PoseLandmark.LEFT_HIP.value],
                                          landmarks[mp_pose.PoseLandmark.LEFT_ANKLE.value])
        
    right_hip_angle=calculateAngle(landmarks[mp_pose.PoseLandmark.NOSE.value],
                                          landmarks[mp_pose.PoseLandmark.RIGHT_HIP.value],
                                          landmarks[mp_pose.PoseLandmark.RIGHT_ANKLE.value])
    
    pose_stage = None

    if(left_shoulder_angle>=30):
      pose_stage=Stage.three
    else:
      if(left_knee_angle<=60):
        pose_stage=Stage.two
      else:
        pose_stage=Stage.one
        
    print("pose_stage------->",pose_stage)
    
    if pose_stage==Stage.one:
        t = 0
        if (left_hip_angle >=85 and right_hip_angle >=85):
          t =t+1
        else:
          print("please be straight and sit straight ")
          suggestions.append("please be straight and sit straight ")
        if (left_elbow_angle >=165):
          t=t+1
        else:
          print("Keep your hands on ground and take its support.")
          suggestions.append("Keep your hands on ground and take its support.")
        if(left_shoulder_angle <=30):
          t=t+1
        else:
          print("Bring hands near to the body")
          suggestions.append("Bring hands near to the body")
        if( (left_knee_angle <=185 and left_knee_angle>=160 and right_knee_angle <=185 and right_knee_angle>=160)):
          t=t+1
        else:
          print("Bring the feet near to the body")
          suggestions.append("Bring the feet near to the body")
        if t==4:
          print("you are doing great")
          suggestions.append("you are doing great")
        else:
          print("Please take a look at photo and get in right position")
          suggestions.append("Please take a look at photo and get in right position")

    elif pose_stage==Stage.two:
        t = 0
        if (left_hip_angle >=85 and right_hip_angle >=85):
          t =t+1
        else:
          print("please be straight and sit straight ")
          suggestions.append("please be straight and sit straight ")
        if (left_elbow_angle >=165):
          t=t+1
        else:
          print("Keep your hands on ground and take its support.")
          suggestions.append("Keep your hands on ground and take its support.")
        if(left_shoulder_angle <=20):
          t=t+1
        else:
          print("Bring hands near to the body")
          suggestions.append("Bring hands near to the body")
        if(left_knee_angle <=60):
          t=t+1
        else:
          print("Bend the knee properly")
          suggestions.append("Bend the knee properly")
        if t==4:
          print("you are doing great")
          suggestions.append("you are doing great")
        else:
          print("Please take a look at photo and get in right position")
          suggestions.append("Please take a look at photo and get in right position")

    elif pose_stage==Stage.three:
        t = 0
        if (left_hip_angle <=135 and right_hip_angle >=85):
          t =t+1
        else:
          print("please be straight and sit straight ")
          suggestions.append("please be straight and sit straight ")
        if (left_elbow_angle >=165):
          t=t+1
        else:
          print("Keep your hands on ground and take its support.")
          suggestions.append("Keep your hands on ground and take its support.")
        if(left_shoulder_angle <=60 and left_shoulder_angle>=20):
          t=t+1
        else:
          print("Bring hands near to the body")
          suggestions.append("Bring hands near to the body")
        if(left_knee_angle <=60):# and (right_knee_angle >=175 and right_knee_angle <=185)):
          t=t+1
        else:
          print("Bend the knee properly")
          suggestions.append("Bend the knee properly")
        if t==4:
          print("you are doing great")
          suggestions.append("you are doing great")
        else:
          print("Please take a look at photo and get in right position")
          suggestions.append("Please take a look at photo and get in right position")
    
    else:
        suggestions.append("Try to attempt the asana correctly it is not matching with any stage")
        
    return(suggestions)