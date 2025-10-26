#!/bin/bash

# Script to run demo with virtual environment
# Chạy demo với virtual environment

# Kiểm tra xem virtual environment đã được tạo chưa
if [ ! -d "venv" ]; then
    echo "❌ Virtual environment chưa được tạo!"
    echo "Vui lòng chạy: bash setup_venv.sh"
    exit 1
fi

# Kích hoạt virtual environment
source venv/bin/activate

# Chạy demo
echo "🚀 Đang khởi động Demo..."
python demo.py

# Tự động deactivate khi thoát
deactivate
