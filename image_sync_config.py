#!/usr/bin/env python3
"""
Configuration file for Image Sync System
Maps labels to folders and handles image processing
"""

# Label to Folder Mapping
LABEL_TO_FOLDER = {
    # Bản Thân
    "Nghiên cứu khoa học": "Ban Than/Nghien cuu",
    "Mentoring": "Ban Than/Mentoring",
    "Sở thích": "Ban Than/So thich",
    "Bảo tàng": "Ban Than/Bao tang HCM",
    
    # Gia Đình
    "Đám cưới anh Trường": "Gia Dinh/Dam Cuoi Anh Truong",
    "Chị Hai": "Gia Dinh/Chi Hai",
    "Chú Linh": "Gia Dinh/Chu Linh",
    "Mẹ": "Gia Dinh/Me",
    "Nha Trang": "Gia Dinh/Nha Trang",
    "Vũng Tàu": "Gia Dinh/Vung Tau",
    "Ngoại": "Gia Dinh/Ngoai",
    "Đi ăn với Hai": "Gia Dinh/Di an voi Hai",
    
    # Bạn Bè
    "Cấp 3": "Ban Be/Cap 3",
    "Sinh viên": "Ban Be/Sinh vien",
    "Tòa án": "Ban Be/Toa An",
    "Bạn nước ngoài": "Ban Be/Ban nuoc ngoai",
    "Đà Lạt": "Ban Be/Da Lat",
    "HRLZ": "Ban Be/HRLZ",
    "Mùa hè xanh": "Ban Be/Mua he xanh",
    "Quân sự": "Ban Be/Quan su",
    "Vinamilk": "Ban Be/Vinamilk",
}

# Modal Configuration (for HTML updates)
MODAL_CONFIG = {
    "Ban Than/Nghien cuu": {
        "modal_id": "research-modal",
        "title": "Chi tiết cột mốc nghiên cứu dữ liệu",
    },
    "Ban Than/Mentoring": {
        "modal_id": "mentoring-modal",
        "title": "Mentoring",
    },
    "Gia Dinh/Nha Trang": {
        "modal_id": "nhatrang-modal",
        "title": "Đi chơi Nha Trang",
    },
    "Gia Dinh/Vung Tau": {
        "modal_id": "vungtau-modal",
        "title": "Đi chơi Vũng Tàu",
    },
    "Ban Be/Da Lat": {
        "modal_id": "dalat-modal",
        "title": "Đi chơi Đà Lạt",
    },
}

# Supported file extensions
SUPPORTED_IMAGE_EXTENSIONS = ('.jpg', '.jpeg', '.png', '.gif', '.bmp', '.webp')
SUPPORTED_VIDEO_EXTENSIONS = ('.mp4', '.webm', '.mov')
SUPPORTED_EXTENSIONS = SUPPORTED_IMAGE_EXTENSIONS + SUPPORTED_VIDEO_EXTENSIONS

# Image processing settings
MAX_FILE_SIZE = 5 * 1024 * 1024  # 5MB
QUALITY = 85  # For JPEG compression
