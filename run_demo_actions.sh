#!/bin/bash

# Run the Action Detection Demo

echo "========================================="
echo "  Action Detection Demo Launcher"
echo "========================================="
echo ""

# Check if virtual environment exists
if [ ! -d "venv" ]; then
    echo "Virtual environment not found!"
    echo "Please run setup_venv.sh first"
    exit 1
fi

# Activate virtual environment
echo "Activating virtual environment..."
source venv/bin/activate

echo ""
echo "Starting Action Detection Demo..."
echo ""
echo "Test these gestures:"
echo "  • Punch: Extend your arm forward"
echo "  • Kick: Raise your knee high"
echo "  • Block: Raise both arms to face"
echo "  • Uppercut: Raise fist upward"
echo ""
echo "Press ESC to exit"
echo ""

# Run the demo
python demo_actions.py

# Deactivate virtual environment
deactivate

echo ""
echo "Demo stopped."
