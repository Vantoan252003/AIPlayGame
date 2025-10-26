import cv2
from time import time, sleep
from modules.pose_detector import PoseDetector
from modules.game_profiles import GAME_PROFILES, GAME_MENU
from modules.endless_runner_controller import EndlessRunnerController
from modules.action_game_controller import ActionGameController


def select_game():
    print(GAME_MENU)
    
    while True:
        choice = input("Chon game (0-4): ").strip()
        
        if choice == '0':
            print("\n👋 Tam biet!")
            return None
        
        if choice in GAME_PROFILES:
            profile = GAME_PROFILES[choice]
            print(f"\n✓ Da chon: {profile['name']}")
            print(f"  Phim: {profile['controls']}")
            return profile
        else:
            print("❌ Nhap so tu 0-4!")


def create_controller(profile):
    game_type = profile['type']
    
    if game_type == 'endless_runner':
        return EndlessRunnerController(profile)
    elif game_type == 'action':
        return ActionGameController(profile)
    elif game_type in ['platformer', 'racing']:
        return EndlessRunnerController(profile)
    else:
        raise ValueError(f"Unknown game type: {game_type}")


def main():
    """Main function to run the universal game controller"""
    
    print("=" * 70)
    print("🎮 UNIVERSAL POSE-CONTROLLED GAME CONTROLLER 🎮".center(70))
    print("=" * 70)
    
    # Select game type
    profile = select_game()
    if profile is None:
        return
    
    # Create controller for selected game
    controller = create_controller(profile)
    
    # Initialize pose detector
    print("\n🔧 Initializing pose detector...")
    pose_detector = PoseDetector()
    
    print("📷 Bat camera...")
    camera_video = cv2.VideoCapture(0)
    camera_video.set(3, 1280)
    camera_video.set(4, 960)
    
    window_name = f'{profile["name"]} - Dieu khien bang pose'
    cv2.namedWindow(window_name, cv2.WINDOW_NORMAL)
    
    time1 = 0
    target_fps = 30
    frame_time = 1.0 / target_fps
    
    print("\n" + "=" * 70)
    print(f"✓ Dang chay {profile['name']}!".center(70))
    print("Nhan ESC de thoat | Nhan R de reset".center(70))
    print("=" * 70 + "\n")
    
    while camera_video.isOpened():
        ok, frame = camera_video.read()
        
        if not ok:
            print("⚠ Khong doc duoc frame")
            continue
        
        frame = cv2.flip(frame, 1)
        
        frame_height, frame_width, _ = frame.shape
        
        frame, results = pose_detector.detect_pose(
            frame,
            pose_detector.pose_video,
            draw=True
        )
        
        frame = controller.process_frame(frame, results, pose_detector)
        
        time2 = time()
        if (time2 - time1) > 0:
            fps = 1.0 / (time2 - time1)
            cv2.putText(
                frame,
                f'FPS: {int(fps)}',
                (10, 30),
                cv2.FONT_HERSHEY_PLAIN,
                2,
                (0, 255, 0),
                3
            )
        time1 = time2
        
        # Display game name
        cv2.putText(
            frame,
            profile['name'],
            (frame_width - 450, 30),
            cv2.FONT_HERSHEY_PLAIN,
            1.5,
            (255, 255, 255),
            2
        )
        
        # Display the frame
        cv2.imshow(window_name, frame)
        
        # FPS limiter - maintain target 30 FPS
        elapsed = time() - time1
        if elapsed < frame_time:
            sleep(frame_time - elapsed)
        
        k = cv2.waitKey(1) & 0xFF
        
        if k == 27:
            print("\n✓ Dang thoat...")
            break
        
        elif k == ord('r'):
            print("\n🔄 Dang reset...")
            controller.reset()
            print("✓ Da reset!")
    
    camera_video.release()
    cv2.destroyAllWindows()
    pose_detector.close()
    
    print("\n✓ Da dong!")
    print("=" * 70)


if __name__ == "__main__":
    main()

