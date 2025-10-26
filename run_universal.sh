#!/bin/bash

# Run the Universal Game Controller

echo "========================================="
echo "  Universal Game Controller Launcher"
echo "========================================="
echo ""

# Check if virtual environment exists
if [ ! -d "venv" ]; then
    echo "⚠️  Virtual environment not found!"
    echo "Please run: bash setup_venv.sh"
    exit 1
fi

# Activate virtual environment
echo "🔧 Activating virtual environment..."
source venv/bin/activate

# Check if required packages are installed
echo "📦 Checking dependencies..."
python -c "import cv2, mediapipe, pyautogui" 2>/dev/null
if [ $? -ne 0 ]; then
    echo "⚠️  Some dependencies are missing!"
    echo "Installing requirements..."
    pip install -r requirements.txt
fi

echo ""
echo "🎮 Starting Universal Game Controller..."
echo ""

# Run the universal controller
python main_universal.py

# Deactivate virtual environment
deactivate

echo ""
echo "✓ Controller stopped."

