#!/bin/bash

# Script to setup virtual environment for Subway Surfers Pose Control
# Tạo virtual environment cho project

echo "======================================================================"
echo "SUBWAY SURFERS POSE CONTROL - Virtual Environment Setup"
echo "======================================================================"
echo ""

# Kiểm tra Python đã được cài đặt chưa
if ! command -v python3 &> /dev/null
then
    echo "❌ Python3 chưa được cài đặt. Vui lòng cài đặt Python3 trước."
    exit 1
fi

echo "✓ Python3 đã được cài đặt: $(python3 --version)"
echo ""

# Tạo virtual environment
echo "📦 Đang tạo virtual environment..."
python3 -m venv venv

if [ $? -eq 0 ]; then
    echo "✓ Virtual environment đã được tạo thành công!"
else
    echo "❌ Lỗi khi tạo virtual environment"
    exit 1
fi

echo ""
echo "🔧 Đang kích hoạt virtual environment..."

# Kích hoạt virtual environment
source venv/bin/activate

if [ $? -eq 0 ]; then
    echo "✓ Virtual environment đã được kích hoạt!"
else
    echo "❌ Lỗi khi kích hoạt virtual environment"
    exit 1
fi

echo ""
echo "📥 Đang cài đặt các thư viện cần thiết..."

# Upgrade pip
pip install --upgrade pip

# Cài đặt requirements
pip install -r requirements.txt

if [ $? -eq 0 ]; then
    echo ""
    echo "✓ Tất cả thư viện đã được cài đặt thành công!"
else
    echo ""
    echo "❌ Lỗi khi cài đặt thư viện"
    exit 1
fi

echo ""
echo "======================================================================"
echo "✅ SETUP HOÀN TẤT!"
echo "======================================================================"
echo ""
echo "Để sử dụng project:"
echo "1. Kích hoạt virtual environment:"
echo "   source venv/bin/activate"
echo ""
echo "2. Chạy chương trình:"
echo "   python main.py"
echo ""
echo "3. Hoặc chạy demo:"
echo "   python demo.py"
echo ""
echo "4. Để thoát virtual environment:"
echo "   deactivate"
echo ""
echo "======================================================================"
