import cv2
import pyautogui
from modules.action_detector import check_punch
from modules.game_controls import check_left_right, check_jump_crouch


class ActionGameController:
    
    def __init__(self, profile):
        self.profile = profile
        self.last_punch_frame = 0
        self.frame_count = 0
        self.last_key_pressed = ""
        self.cooldown = profile['settings'].get('cooldown_frames', 3)
        self.punch_threshold = profile['settings'].get('punch_threshold', 0.08)
        
        self.current_horizontal = 'Center'
        self.is_holding_left = False
        self.is_holding_right = False
        
        self.mid_y = None
        self.y_pos_index = 1
        
    def process_frame(self, frame, results, pose_detector):
        frame_height, frame_width, _ = frame.shape
        self.frame_count += 1
        
        if results.pose_landmarks:
            
            if self.mid_y is None:
                left_y = int(results.pose_landmarks.landmark[
                    pose_detector.mp_pose.PoseLandmark.LEFT_SHOULDER
                ].y * frame_height)
                right_y = int(results.pose_landmarks.landmark[
                    pose_detector.mp_pose.PoseLandmark.RIGHT_SHOULDER
                ].y * frame_height)
                self.mid_y = abs(right_y + left_y) // 2
            
            if self.profile['gestures'].get('punch'):
                frame, punch_status = check_punch(
                    frame, results, pose_detector.mp_pose, 
                    threshold=self.punch_threshold,
                    draw=True
                )
                
                if punch_status == 'Punching':
                    if self._check_cooldown():
                        pyautogui.press(self.profile['controls']['punch'])
                        self.last_key_pressed = f"DAM [{self.profile['controls']['punch'].upper()}]"
                        self._set_cooldown()
            
            if self.profile['gestures'].get('left_right'):
                frame, horizontal_position = check_left_right(
                    frame, results, pose_detector.mp_pose, draw=True
                )
                
                # Update movement state and hold/release keys accordingly
                if horizontal_position != self.current_horizontal:
                    # Release previously held keys
                    if self.is_holding_left:
                        pyautogui.keyUp(self.profile['controls']['left'])
                        self.is_holding_left = False
                    if self.is_holding_right:
                        pyautogui.keyUp(self.profile['controls']['right'])
                        self.is_holding_right = False
                    
                    if horizontal_position == 'Left':
                        pyautogui.keyDown(self.profile['controls']['left'])
                        self.is_holding_left = True
                        self.last_key_pressed = f"TRAI [{self.profile['controls']['left'].upper()}]"
                    elif horizontal_position == 'Right':
                        pyautogui.keyDown(self.profile['controls']['right'])
                        self.is_holding_right = True
                        self.last_key_pressed = f"PHAI [{self.profile['controls']['right'].upper()}]"
                    
                    self.current_horizontal = horizontal_position
            
            if self.profile['gestures'].get('jump_crouch') and self.mid_y:
                frame, posture = check_jump_crouch(
                    frame, results, pose_detector.mp_pose, self.mid_y, draw=True
                )
                
                if posture == 'Jumping' and self.y_pos_index == 1:
                    pyautogui.press(self.profile['controls']['jump'])
                    self.last_key_pressed = f"NHAY [{self.profile['controls']['jump'].upper()}]"
                    self.y_pos_index = 2
                
                elif posture == 'Crouching' and self.y_pos_index == 1:
                    pyautogui.press(self.profile['controls']['crouch'])
                    self.last_key_pressed = f"CUI [{self.profile['controls']['crouch'].upper()}]"
                    self.y_pos_index = 0
                
                elif posture == 'Standing' and self.y_pos_index != 1:
                    self.y_pos_index = 1
        
        
        # Display last action
        if self.last_key_pressed:
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
    
    def _check_cooldown(self):
        return (self.frame_count - self.last_punch_frame) >= self.cooldown
    
    def _set_cooldown(self):
        self.last_punch_frame = self.frame_count
    
    def reset(self):
        if self.is_holding_left:
            pyautogui.keyUp(self.profile['controls']['left'])
        if self.is_holding_right:
            pyautogui.keyUp(self.profile['controls']['right'])
        
        self.last_punch_frame = 0
        self.frame_count = 0
        self.last_key_pressed = ""
        self.current_horizontal = 'Center'
        self.is_holding_left = False
        self.is_holding_right = False
        self.mid_y = None
        self.y_pos_index = 1

