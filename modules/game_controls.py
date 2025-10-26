"""
Game Control Module
Contains functions to detect game control gestures
"""

import cv2
from math import hypot
import matplotlib.pyplot as plt


def check_hands_joined(image, results, mp_pose, draw=False, display=False):
    """
    Check whether the hands of the person are joined or not.
    
    Args:
        image: Input image with a prominent person
        results: Output of pose landmarks detection
        mp_pose: MediaPipe pose instance
        draw: Boolean to write hands status on output image
        display: Boolean to display the resultant image
        
    Returns:
        output_image: Image with classified hands status (if specified)
        hand_status: Classified status ('Hands Joined' or 'Hands Not Joined')
    """
    # Get the height and width of the input image
    height, width, _ = image.shape
    
    # Create a copy of the input image
    output_image = image.copy()
    
    # Get the left wrist landmark x and y coordinates
    left_wrist_landmark = (
        results.pose_landmarks.landmark[mp_pose.PoseLandmark.LEFT_WRIST].x * width,
        results.pose_landmarks.landmark[mp_pose.PoseLandmark.LEFT_WRIST].y * height
    )
    
    # Get the right wrist landmark x and y coordinates
    right_wrist_landmark = (
        results.pose_landmarks.landmark[mp_pose.PoseLandmark.RIGHT_WRIST].x * width,
        results.pose_landmarks.landmark[mp_pose.PoseLandmark.RIGHT_WRIST].y * height
    )
    
    # Calculate the euclidean distance between the left and right wrist
    euclidean_distance = int(hypot(
        left_wrist_landmark[0] - right_wrist_landmark[0],
        left_wrist_landmark[1] - right_wrist_landmark[1]
    ))
    
    # Compare the distance with threshold to check if hands are joined
    if euclidean_distance < 130:
        # Set the hands status to joined
        hand_status = 'Hands Joined'
        color = (0, 255, 0)
    else:
        # Set the hands status to not joined
        hand_status = 'Hands Not Joined'
        color = (0, 0, 255)
    
    # Write status on image if specified
    if draw:
        cv2.putText(output_image, hand_status, (10, 30),
                    cv2.FONT_HERSHEY_PLAIN, 2, color, 3)
        cv2.putText(output_image, f'Distance: {euclidean_distance}', (10, 70),
                    cv2.FONT_HERSHEY_PLAIN, 2, color, 3)
    
    # Display the output image if specified
    if display:
        plt.figure(figsize=[10, 10])
        plt.imshow(output_image[:, :, ::-1])
        plt.title("Output Image")
        plt.axis('off')
        plt.show()
    else:
        return output_image, hand_status


def check_left_right(image, results, mp_pose, draw=False, display=False):
    """
    Find the horizontal position (left, center, right) of the person in an image.
    
    Args:
        image: Input image with a prominent person
        results: Output of pose landmarks detection
        mp_pose: MediaPipe pose instance
        draw: Boolean to write horizontal position on output image
        display: Boolean to display the resultant image
        
    Returns:
        output_image: Image with horizontal position written (if specified)
        horizontal_position: Position ('Left', 'Center', or 'Right')
    """
    # Variable to store horizontal position
    horizontal_position = None
    
    # Get the height and width of the image
    height, width, _ = image.shape
    
    # Create a copy of the input image
    output_image = image.copy()
    
    # Retrieve the x-coordinate of the left shoulder landmark
    left_x = int(results.pose_landmarks.landmark[mp_pose.PoseLandmark.LEFT_SHOULDER].x * width)
    
    # Retrieve the x-coordinate of the right shoulder landmark
    right_x = int(results.pose_landmarks.landmark[mp_pose.PoseLandmark.RIGHT_SHOULDER].x * width)
    
    # Calculate center with margin for more sensitive detection
    center = width // 2
    margin = int(width * 0.15)  # 15% margin for better sensitivity
    left_threshold = center - margin
    right_threshold = center + margin
    
    # Calculate average shoulder position
    avg_shoulder_x = (left_x + right_x) // 2
    
    # Check if person is at left (average shoulder position is left of threshold)
    if avg_shoulder_x < left_threshold:
        horizontal_position = 'Left'
    
    # Check if person is at right (average shoulder position is right of threshold)
    elif avg_shoulder_x > right_threshold:
        horizontal_position = 'Right'
    
    # Check if person is at center
    else:
        horizontal_position = 'Center'
    
    # Write position on image if specified
    if draw:
        cv2.putText(output_image, horizontal_position, (5, height - 10),
                    cv2.FONT_HERSHEY_PLAIN, 2, (255, 255, 255), 3)
        # Draw a line at the center of the image
        cv2.line(output_image, (width // 2, 0), (width // 2, height),
                 (255, 255, 255), 2)
    
    # Display the output image if specified
    if display:
        plt.figure(figsize=[10, 10])
        plt.imshow(output_image[:, :, ::-1])
        plt.title("Output Image")
        plt.axis('off')
        plt.show()
    else:
        return output_image, horizontal_position


def check_jump_crouch(image, results, mp_pose, mid_y=250, draw=False, display=False):
    """
    Check the posture (Jumping, Crouching or Standing) of the person.
    
    Args:
        image: Input image with a prominent person
        results: Output of pose landmarks detection
        mp_pose: MediaPipe pose instance
        mid_y: Initial center y-coordinate of shoulders when standing
        draw: Boolean to write posture on output image
        display: Boolean to display the resultant image
        
    Returns:
        output_image: Image with person's posture written (if specified)
        posture: Posture ('Jumping', 'Crouching', or 'Standing')
    """
    # Get the height and width of the image
    height, width, _ = image.shape
    
    # Create a copy of the input image
    output_image = image.copy()
    
    # Retrieve the y-coordinate of the left shoulder landmark
    left_y = int(results.pose_landmarks.landmark[mp_pose.PoseLandmark.LEFT_SHOULDER].y * height)
    
    # Retrieve the y-coordinate of the right shoulder landmark
    right_y = int(results.pose_landmarks.landmark[mp_pose.PoseLandmark.RIGHT_SHOULDER].y * height)
    
    # Calculate the y-coordinate of the mid-point of both shoulders
    actual_mid_y = abs(right_y + left_y) // 2
    
    # Calculate the upper and lower bounds of the threshold
    # Jump: 50 pixels above mid_y (less sensitive, need more lift)
    lower_bound = mid_y - 50
    
    # Crouch: Set at 60% of screen height (easier to trigger with slight head tilt)
    # This allows crouch to trigger when head/shoulders are at 60% down the screen
    upper_bound = int(height * 0.60)
    
    # Check if person has jumped (shoulders above lower bound)
    if actual_mid_y < lower_bound:
        posture = 'Jumping'
        color = (0, 255, 0)  # Green for jump
    
    # Check if person has crouched (shoulders below upper bound)
    elif actual_mid_y > upper_bound:
        posture = 'Crouching'
        color = (0, 165, 255)  # Orange for crouch
    
    # Otherwise person is standing
    else:
        posture = 'Standing'
        color = (255, 255, 255)  # White for standing
    
    # Write posture on image if specified
    if draw:
        cv2.putText(output_image, posture, (5, height - 50),
                    cv2.FONT_HERSHEY_PLAIN, 2, color, 3)
        
        # Draw the reference lines for better visualization
        # Center line (mid_y) - White
        cv2.line(output_image, (0, mid_y), (width, mid_y), (255, 255, 255), 2)
        cv2.putText(output_image, 'STANDING', (width - 150, mid_y - 5),
                    cv2.FONT_HERSHEY_PLAIN, 1.5, (255, 255, 255), 2)
        
        # Jump threshold line (lower_bound) - Green
        cv2.line(output_image, (0, lower_bound), (width, lower_bound), (0, 255, 0), 2)
        cv2.putText(output_image, 'JUMP', (width - 150, lower_bound - 5),
                    cv2.FONT_HERSHEY_PLAIN, 1.5, (0, 255, 0), 2)
        
        # Crouch threshold line (upper_bound) - Orange (at 60% screen)
        cv2.line(output_image, (0, upper_bound), (width, upper_bound), (0, 165, 255), 2)
        cv2.putText(output_image, f'CROUCH (60%)', (width - 200, upper_bound + 20),
                    cv2.FONT_HERSHEY_PLAIN, 1.5, (0, 165, 255), 2)
        
        # Show current shoulder position
        cv2.circle(output_image, (50, actual_mid_y), 10, color, -1)
        cv2.putText(output_image, f'Y: {actual_mid_y}', (70, actual_mid_y),
                    cv2.FONT_HERSHEY_PLAIN, 1.5, color, 2)
    
    # Display the output image if specified
    if display:
        plt.figure(figsize=[10, 10])
        plt.imshow(output_image[:, :, ::-1])
        plt.title("Output Image")
        plt.axis('off')
        plt.show()
    else:
        return output_image, posture
