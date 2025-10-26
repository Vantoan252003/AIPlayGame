#!/bin/bash

# Script to run the main program with virtual environment
# Chạy chương trình chính với virtual environment

# Kiểm tra xem virtual environment đã được tạo chưa
if [ ! -d "venv" ]; then
    echo "❌ Virtual environment chưa được tạo!"
    echo "Vui lòng chạy: bash setup_venv.sh"
    exit 1
fi

# Kích hoạt virtual environment
source venv/bin/activate

# Chạy chương trình
echo "🚀 Đang khởi động Subway Surfers Pose Control..."
python main.py

# Tự động deactivate khi thoát
deactivate
