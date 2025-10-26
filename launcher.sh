#!/bin/bash

# All-in-One Command Reference for Multi-Game Pose Controller

show_menu() {
    clear
    echo "╔══════════════════════════════════════════════════════════════════╗"
    echo "║         🎮 MULTI-GAME POSE CONTROLLER - LAUNCHER 🎮             ║"
    echo "╚══════════════════════════════════════════════════════════════════╝"
    echo ""
    echo "Select an option:"
    echo ""
    echo "  1️⃣  Play Universal Controller (6 game types)"
    echo "  2️⃣  Test Action Detection (Demo)"
    echo "  3️⃣  Play Subway Surfers (Original)"
    echo "  4️⃣  View Gesture Guide (Visual)"
    echo "  5️⃣  Setup/Update Environment"
    echo "  6️⃣  Read Documentation"
    echo "  7️⃣  Check System Status"
    echo "  0️⃣  Exit"
    echo ""
    echo "╔══════════════════════════════════════════════════════════════════╗"
    echo ""
}

play_universal() {
    echo ""
    echo "🎮 Starting Universal Controller..."
    echo "You can choose from 6 game types!"
    echo ""
    bash run_universal.sh
}

test_actions() {
    echo ""
    echo "🥊 Starting Action Detection Demo..."
    echo "Practice your punches, kicks, and blocks!"
    echo ""
    bash run_demo_actions.sh
}

play_subway_surfers() {
    echo ""
    echo "🏃 Starting Subway Surfers Controller..."
    echo ""
    bash run.sh
}

view_gesture_guide() {
    echo ""
    echo "📖 Displaying Gesture Visual Guide..."
    echo ""
    python GESTURE_VISUAL_GUIDE.py | less
}

setup_environment() {
    echo ""
    echo "🔧 Setting up/updating environment..."
    echo ""
    
    if [ ! -d "venv" ]; then
        echo "Creating virtual environment..."
        bash setup_venv.sh
    else
        echo "Virtual environment exists."
        echo "Updating dependencies..."
        source venv/bin/activate
        pip install -r requirements.txt --upgrade
        deactivate
        echo "✅ Dependencies updated!"
    fi
}

read_docs() {
    clear
    echo "╔══════════════════════════════════════════════════════════════════╗"
    echo "║                      📚 DOCUMENTATION                            ║"
    echo "╚══════════════════════════════════════════════════════════════════╝"
    echo ""
    echo "Available documentation files:"
    echo ""
    echo "  1. README_UNIVERSAL.md      - Complete guide (English)"
    echo "  2. HUONG_DAN_VIET.md       - Hướng dẫn đầy đủ (Tiếng Việt)"
    echo "  3. GESTURE_REFERENCE.txt   - Quick gesture reference"
    echo "  4. CHANGELOG.md            - Version history"
    echo "  5. PROJECT_SUMMARY.md      - Project overview"
    echo "  6. QUICKSTART.md           - Quick start (original)"
    echo "  0. Back to main menu"
    echo ""
    read -p "Select document (0-6): " doc_choice
    
    case $doc_choice in
        1)
            less README_UNIVERSAL.md
            ;;
        2)
            less HUONG_DAN_VIET.md
            ;;
        3)
            less GESTURE_REFERENCE.txt
            ;;
        4)
            less CHANGELOG.md
            ;;
        5)
            less PROJECT_SUMMARY.md
            ;;
        6)
            less QUICKSTART.md
            ;;
        0)
            return
            ;;
        *)
            echo "Invalid choice!"
            sleep 2
            ;;
    esac
}

check_status() {
    clear
    echo "╔══════════════════════════════════════════════════════════════════╗"
    echo "║                    🔍 SYSTEM STATUS CHECK                        ║"
    echo "╚══════════════════════════════════════════════════════════════════╝"
    echo ""
    
    # Check virtual environment
    echo "📦 Virtual Environment:"
    if [ -d "venv" ]; then
        echo "   ✅ Virtual environment exists"
    else
        echo "   ❌ Virtual environment NOT found"
        echo "      Run option 5 to setup"
    fi
    echo ""
    
    # Check Python
    echo "🐍 Python Version:"
    if command -v python3 &> /dev/null; then
        python3 --version
        echo "   ✅ Python 3 installed"
    else
        echo "   ❌ Python 3 NOT found"
    fi
    echo ""
    
    # Check dependencies
    echo "📚 Dependencies:"
    if [ -d "venv" ]; then
        source venv/bin/activate
        
        echo -n "   OpenCV: "
        if python -c "import cv2" 2>/dev/null; then
            echo "✅ Installed"
        else
            echo "❌ Not installed"
        fi
        
        echo -n "   MediaPipe: "
        if python -c "import mediapipe" 2>/dev/null; then
            echo "✅ Installed"
        else
            echo "❌ Not installed"
        fi
        
        echo -n "   PyAutoGUI: "
        if python -c "import pyautogui" 2>/dev/null; then
            echo "✅ Installed"
        else
            echo "❌ Not installed"
        fi
        
        deactivate
    else
        echo "   ⚠️  Virtual environment not found"
    fi
    echo ""
    
    # Check camera
    echo "📷 Camera Check:"
    if [ -e /dev/video0 ]; then
        echo "   ✅ Camera device found (/dev/video0)"
    else
        echo "   ⚠️  Camera device not found"
        echo "      Make sure camera is connected"
    fi
    echo ""
    
    # Check files
    echo "📁 Core Files:"
    files=("main_universal.py" "demo_actions.py" "modules/action_detector.py" "modules/game_profiles.py")
    for file in "${files[@]}"; do
        if [ -f "$file" ]; then
            echo "   ✅ $file"
        else
            echo "   ❌ $file (missing)"
        fi
    done
    echo ""
    
    echo "╔══════════════════════════════════════════════════════════════════╗"
    echo ""
    read -p "Press Enter to continue..."
}

# Main loop
while true; do
    show_menu
    read -p "Enter your choice (0-7): " choice
    
    case $choice in
        1)
            play_universal
            ;;
        2)
            test_actions
            ;;
        3)
            play_subway_surfers
            ;;
        4)
            view_gesture_guide
            ;;
        5)
            setup_environment
            read -p "Press Enter to continue..."
            ;;
        6)
            read_docs
            ;;
        7)
            check_status
            ;;
        0)
            echo ""
            echo "👋 Goodbye! Happy gaming!"
            echo ""
            exit 0
            ;;
        *)
            echo ""
            echo "❌ Invalid choice! Please enter a number between 0-7."
            echo ""
            sleep 2
            ;;
    esac
done
