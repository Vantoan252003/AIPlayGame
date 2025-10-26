"""
Demo script to test individual components
"""

import cv2
from modules.pose_detector import PoseDetector
from modules.game_controls import check_hands_joined, check_left_right, check_jump_crouch


def test_hands_joined():
    """Test hands joined detection"""
    print("Testing Hands Joined Detection...")
    print("Join your hands together to test. Press ESC to exit.")
    
    pose_detector = PoseDetector()
    camera_video = cv2.VideoCapture(0)
    camera_video.set(3, 1280)
    camera_video.set(4, 960)
    
    cv2.namedWindow('Hands Joined Test', cv2.WINDOW_NORMAL)
    
    while camera_video.isOpened():
        ok, frame = camera_video.read()
        if not ok:
            continue
        
        frame = cv2.flip(frame, 1)
        frame, results = pose_detector.detect_pose(frame, pose_detector.pose_video, draw=True)
        
        if results.pose_landmarks:
            frame, _ = check_hands_joined(frame, results, pose_detector.mp_pose, draw=True)
        
        cv2.imshow('Hands Joined Test', frame)
        
        if cv2.waitKey(1) & 0xFF == 27:
            break
    
    camera_video.release()
    cv2.destroyAllWindows()
    pose_detector.close()


def test_left_right():
    """Test horizontal position detection"""
    print("Testing Left/Right Detection...")
    print("Move left and right to test. Press ESC to exit.")
    
    pose_detector = PoseDetector()
    camera_video = cv2.VideoCapture(0)
    camera_video.set(3, 1280)
    camera_video.set(4, 960)
    
    cv2.namedWindow('Left Right Test', cv2.WINDOW_NORMAL)
    
    while camera_video.isOpened():
        ok, frame = camera_video.read()
        if not ok:
            continue
        
        frame = cv2.flip(frame, 1)
        frame, results = pose_detector.detect_pose(frame, pose_detector.pose_video, draw=True)
        
        if results.pose_landmarks:
            frame, _ = check_left_right(frame, results, pose_detector.mp_pose, draw=True)
        
        cv2.imshow('Left Right Test', frame)
        
        if cv2.waitKey(1) & 0xFF == 27:
            break
    
    camera_video.release()
    cv2.destroyAllWindows()
    pose_detector.close()


def test_jump_crouch():
    """Test jump and crouch detection"""
    print("Testing Jump/Crouch Detection...")
    print("Jump and crouch to test. Press ESC to exit.")
    
    pose_detector = PoseDetector()
    camera_video = cv2.VideoCapture(0)
    camera_video.set(3, 1280)
    camera_video.set(4, 960)
    
    cv2.namedWindow('Jump Crouch Test', cv2.WINDOW_NORMAL)
    
    while camera_video.isOpened():
        ok, frame = camera_video.read()
        if not ok:
            continue
        
        frame = cv2.flip(frame, 1)
        frame, results = pose_detector.detect_pose(frame, pose_detector.pose_video, draw=True)
        
        if results.pose_landmarks:
            frame, _ = check_jump_crouch(frame, results, pose_detector.mp_pose, draw=True)
        
        cv2.imshow('Jump Crouch Test', frame)
        
        if cv2.waitKey(1) & 0xFF == 27:
            break
    
    camera_video.release()
    cv2.destroyAllWindows()
    pose_detector.close()


def main():
    """Main demo menu"""
    print("=" * 70)
    print("POSE DETECTION DEMO - Component Testing")
    print("=" * 70)
    print("\nChoose a test:")
    print("1. Test Hands Joined Detection")
    print("2. Test Left/Right Movement Detection")
    print("3. Test Jump/Crouch Detection")
    print("4. Exit")
    print("=" * 70)
    
    choice = input("\nEnter your choice (1-4): ")
    
    if choice == '1':
        test_hands_joined()
    elif choice == '2':
        test_left_right()
    elif choice == '3':
        test_jump_crouch()
    elif choice == '4':
        print("Exiting...")
    else:
        print("Invalid choice!")


if __name__ == "__main__":
    main()
