"""
Action Detection Module
Detects fighting/action game gestures
"""

import cv2


def check_punch(image, results, mp_pose, threshold=0.08, draw=False):
    """
    Detect if person is punching (either arm extended straight forward).
    
    Args:
        image: Input image with a prominent person
        results: Output of pose landmarks detection
        mp_pose: MediaPipe pose instance
        threshold: Z-depth threshold for arm extension (lower = more sensitive)
        draw: Boolean to draw punch status on output image
        
    Returns:
        output_image: Image with punch status (if specified)
        punch_status: 'Punching' or 'No Punch'
    """
    height, width, _ = image.shape
    output_image = image.copy()
    punch_status = 'No Punch'
    color = (255, 255, 255)
    
    # Get shoulder, elbow, and wrist landmarks for both arms
    left_shoulder = results.pose_landmarks.landmark[mp_pose.PoseLandmark.LEFT_SHOULDER]
    right_shoulder = results.pose_landmarks.landmark[mp_pose.PoseLandmark.RIGHT_SHOULDER]
    left_elbow = results.pose_landmarks.landmark[mp_pose.PoseLandmark.LEFT_ELBOW]
    right_elbow = results.pose_landmarks.landmark[mp_pose.PoseLandmark.RIGHT_ELBOW]
    left_wrist = results.pose_landmarks.landmark[mp_pose.PoseLandmark.LEFT_WRIST]
    right_wrist = results.pose_landmarks.landmark[mp_pose.PoseLandmark.RIGHT_WRIST]
    
    # Check if either arm is extended forward (z-axis depth)
    # Positive value means wrist is in front of shoulder
    left_extension = left_shoulder.z - left_wrist.z
    right_extension = right_shoulder.z - right_wrist.z
    
    # Calculate arm straightness (distance from shoulder to wrist in x-y plane)
    # This ensures the arm is actually extended, not just bent forward
    left_arm_distance = abs(left_shoulder.x - left_wrist.x) + abs(left_shoulder.y - left_wrist.y)
    right_arm_distance = abs(right_shoulder.x - right_wrist.x) + abs(right_shoulder.y - right_wrist.y)
    
    # Check if elbow is between shoulder and wrist (arm is straight)
    left_elbow_forward = left_shoulder.z > left_elbow.z > left_wrist.z
    right_elbow_forward = right_shoulder.z > right_elbow.z > right_wrist.z
    
    # Detect punch: arm extended forward, at shoulder height, AND arm is extended (not bent)
    # Require minimum arm extension distance to avoid false positives when arm is bent
    left_punch = (left_extension > threshold and 
                  left_wrist.y < left_shoulder.y + 0.25 and
                  left_arm_distance > 0.3 and  # Arm must be extended
                  left_elbow_forward)  # Elbow in front of shoulder
    
    right_punch = (right_extension > threshold and 
                   right_wrist.y < right_shoulder.y + 0.25 and
                   right_arm_distance > 0.3 and  # Arm must be extended
                   right_elbow_forward)  # Elbow in front of shoulder
    
    if left_punch or right_punch:
        punch_status = 'Punching'
        color = (0, 255, 255)  # Yellow
    
    # Draw status on image
    if draw:
        cv2.putText(output_image, punch_status, (10, 110),
                    cv2.FONT_HERSHEY_PLAIN, 2, color, 3)
        # Show extension values and arm distance for debugging
        cv2.putText(output_image, f'L:{left_extension:.2f} R:{right_extension:.2f}', 
                    (10, 140), cv2.FONT_HERSHEY_PLAIN, 1.5, (255, 255, 255), 2)
        cv2.putText(output_image, f'LD:{left_arm_distance:.2f} RD:{right_arm_distance:.2f}', 
                    (10, 170), cv2.FONT_HERSHEY_PLAIN, 1.5, (255, 255, 255), 2)
    
    return output_image, punch_status

