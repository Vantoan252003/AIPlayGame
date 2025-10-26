"""
Main Game Controller
Controls Subway Surfers game using pose detection
"""

import cv2
import pyautogui
from time import time
from modules.pose_detector import PoseDetector
from modules.game_controls import check_hands_joined, check_left_right, check_jump_crouch


def main():
    """Main function to run the game controller"""
    
    # Initialize pose detector
    pose_detector = PoseDetector()

    camera_video = cv2.VideoCapture(0)
    camera_video.set(3, 1280)  # Width
    camera_video.set(4, 960)   # Height
    
    # Create named window for resizing purposes
    cv2.namedWindow('Subway Surfers with Pose Detection', cv2.WINDOW_NORMAL)
    
    # Initialize variables
    time1 = 0  # Time of previous frame
    game_started = False  # Game state
    x_pos_index = 1  # Horizontal position (0=left, 1=center, 2=right)
    y_pos_index = 1  # Vertical position (0=crouch, 1=stand, 2=jump)
    mid_y = None  # Initial y-coordinate of shoulder midpoint
    counter = 0  # Counter for consecutive frames with hands joined
    num_of_frames = 10  # Required consecutive frames to start game
    last_key_pressed = ""  # Store last key pressed for display
    
    
    # Main game loop
    while camera_video.isOpened():
        # Read a frame
        ok, frame = camera_video.read()
        
        # Check if frame is read properly
        if not ok:
            print("Failed to read frame from camera")
            continue
        
        # Flip frame horizontally for natural (selfie-view) visualization
        frame = cv2.flip(frame, 1)
        
        # Get frame dimensions
        frame_height, frame_width, _ = frame.shape
        
        # Perform pose detection on the frame
        frame, results = pose_detector.detect_pose(
            frame,
            pose_detector.pose_video,
            draw=game_started
        )
        
        # Check if pose landmarks are detected
        if results.pose_landmarks:
            
            # If game has started
            if game_started:
                
                # --- Control Horizontal Movements ---
                frame, horizontal_position = check_left_right(
                    frame, results, pose_detector.mp_pose, draw=True
                )
                
                # Move left (hoặc từ Right về Center)
                if (horizontal_position == 'Left' and x_pos_index != 0) or \
                   (horizontal_position == 'Center' and x_pos_index == 2):
                    pyautogui.press('left')
                    if x_pos_index == 2:
                        last_key_pressed = "← LEFT (Right→Center)"
                    else:
                        last_key_pressed = "← LEFT"
                    x_pos_index -= 1
                
                # Move right (hoặc từ Left về Center)
                elif (horizontal_position == 'Right' and x_pos_index != 2) or \
                     (horizontal_position == 'Center' and x_pos_index == 0):
                    pyautogui.press('right')
                    if x_pos_index == 0:
                        last_key_pressed = "→ RIGHT (Left→Center)"
                    else:
                        last_key_pressed = "→ RIGHT"
                    x_pos_index += 1
                
                # --- Control Vertical Movements ---
                if mid_y:
                    frame, posture = check_jump_crouch(
                        frame, results, pose_detector.mp_pose, mid_y, draw=True
                    )
                    
                    # Jump
                    if posture == 'Jumping' and y_pos_index == 1:
                        pyautogui.press('up')
                        last_key_pressed = "↑ JUMP"
                        y_pos_index += 1
                    
                    # Crouch
                    elif posture == 'Crouching' and y_pos_index == 1:
                        pyautogui.press('down')
                        last_key_pressed = "↓ CROUCH"
                        y_pos_index -= 1
                    
                    # Standing
                    elif posture == 'Standing' and y_pos_index != 1:
                        y_pos_index = 1
            
            # If game has not started yet
            else:
                cv2.putText(
                    frame,
                    'JOIN BOTH HANDS TO START THE GAME.',
                    (5, frame_height - 10),
                    cv2.FONT_HERSHEY_PLAIN,
                    2,
                    (0, 255, 0),
                    3
                )
            
            # --- Check for Game Start/Resume ---
            if check_hands_joined(frame, results, pose_detector.mp_pose)[1] == 'Hands Joined':
                counter += 1
                
                # Check if counter reached required frames
                if counter == num_of_frames:
                    
                    # Start game for first time
                    if not game_started:
                        game_started = True
                        
                        # Calculate initial shoulder midpoint y-coordinate
                        left_y = int(results.pose_landmarks.landmark[
                            pose_detector.mp_pose.PoseLandmark.LEFT_SHOULDER
                        ].y * frame_height)
                        right_y = int(results.pose_landmarks.landmark[
                            pose_detector.mp_pose.PoseLandmark.RIGHT_SHOULDER
                        ].y * frame_height)
                        mid_y = abs(right_y + left_y) // 2
                        
                        # Click to start game (adjust coordinates as needed)
                        pyautogui.click(x=1300, y=800, button='left')
                        
                        print("\n✓ Game Started! Use your body to control the character.")
                    
                    # Resume game after character death
                    else:
                        pyautogui.press('space')
                        last_key_pressed = "SPACE - RESUME"
                        print("\n✓ Game Resumed!")
                    
                    # Reset counter
                    counter = 0
            
            # Hands not joined
            else:
                counter = 0
        
        # No pose landmarks detected
        else:
            counter = 0
        
        # --- Calculate and Display FPS ---
        time2 = time()
        
        if (time2 - time1) > 0:
            frames_per_second = 1.0 / (time2 - time1)
            cv2.putText(
                frame,
                f'FPS: {int(frames_per_second)}',
                (10, 30),
                cv2.FONT_HERSHEY_PLAIN,
                2,
                (0, 255, 0),
                3
            )
        
        # Display last key pressed
        if last_key_pressed and game_started:
            cv2.putText(
                frame,
                f'Key: {last_key_pressed}',
                (10, 70),
                cv2.FONT_HERSHEY_PLAIN,
                2,
                (0, 255, 255),
                3
            )
        
        time1 = time2
        
        # Display the frame
        cv2.imshow('Subway Surfers with Pose Detection', frame)
        
        # Wait for key press
        k = cv2.waitKey(1) & 0xFF
        
        # Check if ESC is pressed and break the loop
        if k == 27:
            print("\n✓ Exiting game controller...")
            break
    
    # Release resources
    camera_video.release()
    cv2.destroyAllWindows()
    pose_detector.close()
    
    print("✓ Game controller closed successfully!")
    print("=" * 70)


if __name__ == "__main__":
    main()
