"""
Demo script to test action detection gestures
Shows how punch detection works
"""

import cv2
from modules.pose_detector import PoseDetector
from modules.action_detector import check_punch


def main():
    """Demo action detection"""
    
    print("=" * 70)
    print("🥊 ACTION GESTURE DETECTION DEMO 🥊".center(70))
    print("=" * 70)
    print("\nTest this gesture:")
    print("  • Punch: Extend your arm straight forward (left or right)")
    print("\nPress ESC to exit\n")
    print("=" * 70)
    
    # Initialize pose detector
    pose_detector = PoseDetector()
    
    # Initialize camera
    camera_video = cv2.VideoCapture(0)
    camera_video.set(3, 1280)
    camera_video.set(4, 960)
    
    # Create window
    cv2.namedWindow('Action Gesture Demo', cv2.WINDOW_NORMAL)
    
    while camera_video.isOpened():
        ok, frame = camera_video.read()
        
        if not ok:
            print("Failed to read frame")
            continue
        
        # Flip frame for natural visualization
        frame = cv2.flip(frame, 1)
        
        # Detect pose
        frame, results = pose_detector.detect_pose(
            frame,
            pose_detector.pose_video,
            draw=True
        )
        
        # Check punch gesture
        if results.pose_landmarks:
            frame, punch_status = check_punch(
                frame, results, pose_detector.mp_pose, 
                threshold=0.08,  # Lower threshold = more sensitive
                draw=True
            )
            
            # Display active gesture prominently
            height, width, _ = frame.shape
            active_gesture = "READY"
            color = (255, 255, 255)
            
            if punch_status == 'Punching':
                active_gesture = "� PUNCHING!"
                color = (0, 255, 255)
            
            cv2.putText(
                frame,
                active_gesture,
                (width // 2 - 200, height - 50),
                cv2.FONT_HERSHEY_PLAIN,
                4,
                color,
                5
            )
        
        # Display frame
        cv2.imshow('Action Gesture Demo', frame)
        
        # Exit on ESC
        if cv2.waitKey(1) & 0xFF == 27:
            break
    
    # Cleanup
    camera_video.release()
    cv2.destroyAllWindows()
    pose_detector.close()
    
    print("\n✓ Demo closed!")


if __name__ == "__main__":
    main()

