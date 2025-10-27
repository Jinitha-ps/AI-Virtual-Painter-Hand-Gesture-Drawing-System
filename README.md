# 🎨 AI Virtual Painter: Hand Gesture Drawing System
This project is an immersive Human-Computer Interaction (HCI) application that allows users to create digital artwork directly on their screen using only real-time hand gestures. By integrating advanced computer vision, the system interprets hand movements to control an on-screen brush, eliminating the need for traditional input devices like a mouse or stylus.


# ✨ Core Functionality & Features


**🖐️ Real-Time Hand Tracking**: Utilizes MediaPipe to accurately detect and track 21 distinct hand landmarks, ensuring precise control.

**✏️ Dual-Mode Operation**: Seamlessly switches between two states:

**Drawing Mode**: Activated by extending the index finger, translating finger movement into brush strokes.

Selection Mode: Activated by extending the index and middle fingers, locking the drawing to interact with the UI palette.

**🌈 Interactive Virtual Palette**: Features an on-screen toolbar for dynamic selection of drawing colors (Red, Green, Blue, Yellow) and an Eraser tool.

**🎥 Dynamic Canvas Integration**: Employs OpenCV's image processing techniques to seamlessly overlay the transparent drawing canvas onto the live webcam feed.



# ⚙️ Technology Stack


Component,Purpose,Python Library
Vision,Hand Landmark Detection & Tracking,MediaPipe
Processing,Camera Feed & Image Manipulation,OpenCV (cv2)
Calculations,Numerical Array Management (The Canvas),NumPy



# 🚀 Setup & Execution


**Prerequisites**

* Python 3.12
* A functional Webcam


**Quick Start**

1. Clone the Repository and install the required dependencies using pip.
2. Execute the main script (python main.py).
3. The application will launch, displaying your live video feed with the virtual palette ready for use.

