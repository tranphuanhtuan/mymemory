# 🖼️ Automated Image Sync System - My Memory

## 📋 Giới thiệu

Hệ thống tự động đồng bộ ảnh từ **GitHub Issues** lên **code & website** dựa vào **label**.

Khi bạn upload ảnh vào issue và gắn label tương ứng, workflow sẽ:
1. ✅ Tự động tải ảnh xuống
2. ✅ Lưu vào thư mục đúng dựa vào label
3. ✅ Commit lên main branch
4. ✅ Cập nhật website

---

## 🚀 Cách sử dụng

### Bước 1: Tạo Issue mới
1. Vào tab **Issues** → Click **New Issue**
2. Viết tiêu đề và mô tả

### Bước 2: Upload ảnh
- Dán ảnh vào **Issue body** hoặc **Comments**
- GitHub sẽ tự động upload ảnh lên

### Bước 3: Gắn Label
Chọn một label dưới đây tương ứng với khu vực:

#### 🎓 Bản Thân (Ban Than/)
- `Nghiên cứu khoa học` → `Ban Than/Nghien cuu/`
- `Mentoring` → `Ban Than/Mentoring/`
- `Sở thích` → `Ban Than/So thich/`
- `Bảo tàng` → `Ban Than/Bao tang HCM/`

#### 👨‍👩‍👧‍👦 Gia Đình (Gia Dinh/)
- `Đám cưới anh Trường` → `Gia Dinh/Dam Cuoi Anh Truong/`
- `Chị Hai` → `Gia Dinh/Chi Hai/`
- `Chú Linh` → `Gia Dinh/Chu Linh/`
- `Mẹ` → `Gia Dinh/Me/`
- `Nha Trang` → `Gia Dinh/Nha Trang/`
- `Vũng Tàu` → `Gia Dinh/Vung Tau/`
- `Ngoại` → `Gia Dinh/Ngoai/`

#### 👯 Bạn Bè (Ban Be/)
- `Cấp 3` → `Ban Be/Cap 3/`
- `Sinh viên` → `Ban Be/Sinh vien/`
- `Tòa án` → `Ban Be/Toa An/`
- `Bạn nước ngoài` → `Ban Be/Ban nuoc ngoai/`
- `Đà Lạt` → `Ban Be/Da Lat/`
- `HRLZ` → `Ban Be/HRLZ/`
- `Mùa hè xanh` → `Ban Be/Mua he xanh/`
- `Quân sự` → `Ban Be/Quan su/`
- `Vinamilk` → `Ban Be/Vinamilk/`

### Bước 4: Chạy Workflow
1. Vào tab **Actions**
2. Click workflow **"Sync Images from Issue to Code"**
3. Click **"Run workflow"**
4. Nhập **Issue number** (ví dụ: `2` cho issue #2)
5. Click **"Run workflow"** để bắt đầu

---

## ✨ Kết quả

Sau khi workflow chạy xong:

✅ **Ảnh được lưu** vào thư mục tương ứng theo label  
✅ **Commit tự động** lên main branch  
✅ **Website cập nhật** với ảnh mới  
✅ **Comment tự động** trong issue với danh sách ảnh đã tải

Ví dụ:
```
✅ Image Sync Complete!

Images Downloaded: 3

Files added to code:
- Ban Than/Nghien cuu/image_1.jpg
- Ban Than/Nghien cuu/image_2.jpg
- Ban Than/Nghien cuu/screenshot_1.png

Label Detected: ["Nghiên cứu khoa học"]
```

---

## 🔧 Cấu hình (Nếu cần thêm label mới)

Chỉnh sửa file `.github/workflows/sync-images-from-issue.yml`:

```python
label_to_folder = {
    "Tên Label Mới": "Đường dẫn/Thư mục",
}
```

---

## 📝 Lưu ý quan trọng

- **Chỉ upload ảnh:** JPG, PNG, GIF
- **Video:** MP4 (tùy chọn)
- **Kích thước:** Tối ưu dưới 5MB/ảnh
- **Label:** Phải chính xác (kiểm tra cách viết)
- **Permissions:** Workflow cần quyền `write` để commit

---

## 🐛 Troubleshooting

**❓ Workflow không tìm thấy ảnh?**
- Kiểm tra label có chính xác không
- Đảm bảo ảnh được upload vào issue body hoặc comments

**❓ Label không khớp?**
- Kiểm tra danh sách label trong file workflow
- Thêm label mới nếu cần

**❓ Ảnh không hiển thị trên website?**
- Chờ vài giây GitHub Pages cập nhật
- Refresh trình duyệt (Ctrl+F5)

---

## 📞 Liên hệ

Nếu có vấn đề, tạo issue mới với tag `bug` hoặc `question`.

Happy memories! 🎉
