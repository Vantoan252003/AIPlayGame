"""
Pose Detection Module using MediaPipe
Detects body pose landmarks for game control
"""

import cv2
import mediapipe as mp
import matplotlib.pyplot as plt


class PoseDetector:
    """Class to handle pose detection using MediaPipe"""
    
    def __init__(self, use_gpu=True):
        """Initialize MediaPipe pose detection models"""
        # Initialize mediapipe pose class
        self.mp_pose = mp.solutions.pose
        
        # Check if GPU is available
        import os
        if use_gpu:
            # Try to use GPU delegate
            try:
                os.environ['MEDIAPIPE_DISABLE_GPU'] = '0'
                print("✓ GPU mode enabled for MediaPipe")
            except:
                print("⚠ GPU not available, using CPU")
                os.environ['MEDIAPIPE_DISABLE_GPU'] = '1'
        else:
            os.environ['MEDIAPIPE_DISABLE_GPU'] = '1'
            print("✓ CPU mode for MediaPipe")
        
        # Setup the Pose function for images
        self.pose_image = self.mp_pose.Pose(
            static_image_mode=True,
            min_detection_confidence=0.5,
            model_complexity=1
        )
        
        # Setup the Pose function for videos (optimized for game control)
        self.pose_video = self.mp_pose.Pose(
            static_image_mode=False,
            model_complexity=1,  # Use model_complexity=2 for better accuracy if GPU is strong
            min_detection_confidence=0.5,  # Lower for faster detection
            min_tracking_confidence=0.5,   # Lower for faster tracking
            smooth_landmarks=True
        )
        
        # Initialize mediapipe drawing class
        self.mp_drawing = mp.solutions.drawing_utils
    
    def detect_pose(self, image, pose, draw=False, display=False):
        """
        Perform pose detection on the most prominent person in an image.
        
        Args:
            image: The input image with a prominent person
            pose: The pose function (pose_image or pose_video)
            draw: Boolean to draw pose landmarks on output image
            display: Boolean to display the result
            
        Returns:
            output_image: Image with detected pose landmarks drawn (if specified)
            results: Output of pose landmarks detection
        """
        # Create a copy of the input image
        output_image = image.copy()
        
        # Convert the image from BGR to RGB format
        image_rgb = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
        
        # Perform the Pose Detection
        results = pose.process(image_rgb)
        
        # Check if any landmarks are detected and are specified to be drawn
        if results.pose_landmarks and draw:
            # Draw Pose Landmarks on the output image
            self.mp_drawing.draw_landmarks(
                image=output_image,
                landmark_list=results.pose_landmarks,
                connections=self.mp_pose.POSE_CONNECTIONS,
                landmark_drawing_spec=self.mp_drawing.DrawingSpec(
                    color=(255, 255, 255),
                    thickness=3,
                    circle_radius=3
                ),
                connection_drawing_spec=self.mp_drawing.DrawingSpec(
                    color=(49, 125, 237),
                    thickness=2,
                    circle_radius=2
                )
            )
        
        # Check if the images are specified to be displayed
        if display:
            # Display the original input image and the resultant image
            plt.figure(figsize=[22, 22])
            plt.subplot(121)
            plt.imshow(image[:, :, ::-1])
            plt.title("Original Image")
            plt.axis('off')
            plt.subplot(122)
            plt.imshow(output_image[:, :, ::-1])
            plt.title("Output Image")
            plt.axis('off')
            plt.show()
        else:
            # Return the output image and results
            return output_image, results
    
    def close(self):
        """Close pose detection models"""
        self.pose_image.close()
        self.pose_video.close()
