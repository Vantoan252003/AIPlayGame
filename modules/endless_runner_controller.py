import cv2
import pyautogui
from time import time
from modules.game_controls import check_hands_joined, check_left_right, check_jump_crouch


class EndlessRunnerController:
    
    def __init__(self, profile):
        self.profile = profile
        self.game_started = False
        self.x_pos_index = 1
        self.y_pos_index = 1
        self.mid_y = None
        self.counter = 0
        self.last_key_pressed = ""
        
    def process_frame(self, frame, results, pose_detector):
        frame_height, frame_width, _ = frame.shape
        
        if results.pose_landmarks:
            
            if self.game_started:
                # Horizontal movement control
                frame, horizontal_position = check_left_right(
                    frame, results, pose_detector.mp_pose, draw=True
                )
                
                if (horizontal_position == 'Left' and self.x_pos_index != 0) or \
                   (horizontal_position == 'Center' and self.x_pos_index == 2):
                    pyautogui.press(self.profile['controls']['left'])
                    self.last_key_pressed = "TRAI"
                    self.x_pos_index -= 1
                
                elif (horizontal_position == 'Right' and self.x_pos_index != 2) or \
                     (horizontal_position == 'Center' and self.x_pos_index == 0):
                    pyautogui.press(self.profile['controls']['right'])
                    self.last_key_pressed = "PHAI"
                    self.x_pos_index += 1
                
                if self.mid_y:
                    frame, posture = check_jump_crouch(
                        frame, results, pose_detector.mp_pose, self.mid_y, draw=True
                    )
                    
                    if posture == 'Jumping' and self.y_pos_index == 1:
                        pyautogui.press(self.profile['controls']['jump'])
                        self.last_key_pressed = "NHAY"
                        self.y_pos_index += 1
                    
                    elif posture == 'Crouching' and self.y_pos_index == 1:
                        pyautogui.press(self.profile['controls']['crouch'])
                        self.last_key_pressed = "CUI"
                        self.y_pos_index -= 1
                    
                    elif posture == 'Standing' and self.y_pos_index != 1:
                        self.y_pos_index = 1
            
            else:
                cv2.putText(
                    frame,
                    'CHAM 2 TAY DE BAT DAU',
                    (5, frame_height - 10),
                    cv2.FONT_HERSHEY_PLAIN,
                    2,
                    (0, 255, 0),
                    3
                )
            
            if check_hands_joined(frame, results, pose_detector.mp_pose)[1] == 'Hands Joined':
                self.counter += 1
                
                if self.counter == self.profile['settings']['num_frames_to_start']:
                    if not self.game_started:
                        self.game_started = True
                        
                        left_y = int(results.pose_landmarks.landmark[
                            pose_detector.mp_pose.PoseLandmark.LEFT_SHOULDER
                        ].y * frame_height)
                        right_y = int(results.pose_landmarks.landmark[
                            pose_detector.mp_pose.PoseLandmark.RIGHT_SHOULDER
                        ].y * frame_height)
                        self.mid_y = abs(right_y + left_y) // 2
                        
                        if self.profile['settings']['game_start_click']:
                            x, y = self.profile['settings']['game_start_click']
                            pyautogui.click(x=x, y=y, button='left')
                        
                        print("\n✓ Bat dau game!")
                    else:
                        pyautogui.press(self.profile['controls']['start'])
                        self.last_key_pressed = "TIEP TUC"
                        print("\n✓ Tiep tuc game!")
                    
                    self.counter = 0
            else:
                self.counter = 0
        else:
            self.counter = 0
        
        if self.last_key_pressed and self.game_started:
            cv2.putText(
                frame,
                f'{self.last_key_pressed}',
                (10, 70),
                cv2.FONT_HERSHEY_PLAIN,
                2,
                (0, 255, 255),
                3
            )
        
        return frame
    
    def reset(self):
        self.game_started = False
        self.x_pos_index = 1
        self.y_pos_index = 1
        self.mid_y = None
        self.counter = 0
        self.last_key_pressed = ""
