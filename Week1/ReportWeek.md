# Báo cáo tuần 1

## Ngày 1 — Làm quen Python

### Nội dung đã học

- Làm quen với biến, kiểu dữ liệu, `list`, `dict`, vòng lặp `for`, điều kiện `if`, hàm và `import`.
- Áp dụng nền tảng C#/JavaScript để đọc và viết class Python: `__init__`, thuộc tính đối tượng, `self`, kiểu gợi ý (`str`, `int`, `bool`) và f-string.
- Tự tra cứu cú pháp từ Google và W3Schools trong lúc làm bài; phần code được tự viết.

### Bài đã làm

- Viết class `CameraDevice` có các thuộc tính `id`, `name`, `is_online`, `fps`.
- Viết phiên bản `get_info()` cho camera và thử hiển thị thông tin một đối tượng.
- Tự mở rộng ví dụ bằng `random.randint()` để sinh phần số của mã camera.
- Làm mini challenge với danh sách 5 camera và các hàm `get_online_cameras()`, `get_average_fps()` và `get_info()`; có in tổng số camera, số camera online và FPS trung bình.
- Thử cách khai báo thuộc tính kiểu C# trong class `Person` để IDE gợi ý kiểu tốt hơn.

### Điểm mạnh

- Chủ động chuyển kiến thức OOP từ C#/JavaScript sang Python thay vì chỉ chép ví dụ.
- Có tinh thần tự mở rộng bài (`random`, type hint, class `Person`) và chia bài thành các hàm riêng.
- Đã bám đúng chủ đề Ngày 1 và hoàn thành được phần lớn khung bài camera.

### Lỗi/phần cần sửa cụ thể

| Vị trí | Hiện trạng | Cần sửa/hiểu lại |
| --- | --- | --- |
| Tham số hàm | `get_online_cameras(listCameras)` và các hàm tương tự nhận tham số nhưng cách đặt tên chưa theo Python; ở ví dụ ban đầu có tham số `device` nhưng lại duyệt biến toàn cục `cameras`. | Luôn dùng đúng tham số truyền vào; đặt tên theo `snake_case`, ví dụ `camera_list`. |
| `print` và `return` | `CameraDevice.get_info()` đang `print` trực tiếp trong khi yêu cầu là trả về chuỗi. | Hàm nên `return` chuỗi; việc `print(...)` để ở nơi gọi hàm. |
| Tên biến | Có `listCameras`, `isOnline`, `idCAM`. | Đổi sang `camera_list`, `is_online`, `camera_id` theo quy ước `snake_case` của Python. |
| ID ngẫu nhiên | `random.randint(1, 100)` có thể sinh trùng ID. | Chưa có cơ chế bảo đảm duy nhất; cần kiểm tra ID đã dùng hoặc chọn chiến lược sinh ID khác. |
| Lọc camera online | `get_online_cameras()` hiện trả về biến đếm/số lượng, không phải danh sách camera online như tên hàm và yêu cầu “lọc” gợi ra. | Tạo danh sách các camera online rồi trả về danh sách; dùng `len(...)` khi cần đếm. |
| FPS trung bình | `get_average_fps()` cộng FPS của tất cả camera, gồm cả camera offline. | Chỉ tính FPS của camera online theo yêu cầu. |
| `return` trong vòng lặp | `get_info(listCameras)` `return` ngay trong lần lặp đầu tiên. | Hàm hiện chỉ tạo thông tin cho camera đầu tiên; cần xác định rõ muốn lấy một camera hay ghép/trả về thông tin của tất cả camera. |
| Không có camera online | Chưa xử lý trường hợp tính FPS trung bình khi không có camera online; phép chia có thể bằng 0. | Thêm nhánh kiểm tra trước khi chia và trả về giá trị/thông báo phù hợp. |

### Trạng thái cần sửa

Mini challenge đã hoàn thành ở mức bản đầu tiên nhưng **chưa hoàn tất yêu cầu đúng nghĩa**: cần chỉnh lại việc lọc danh sách online, tính FPS chỉ cho camera online, cách trả dữ liệu từ `get_info()` và trường hợp không có camera online. Các lỗi trên mới được ghi nhận, chưa được sửa trong bài hiện tại.

### Bước tiếp theo

1. Sửa lại mini challenge theo từng lỗi trong bảng, ưu tiên dữ liệu trả về của mỗi hàm.
2. Chạy thử ít nhất hai tình huống: có camera online và toàn bộ camera offline.
3. Kiểm tra `get_info()` trả về chuỗi trước, sau đó mới in chuỗi đó ở bên ngoài.
4. Sau khi sửa, ghi kết quả test và các lỗi mới (nếu có) vào báo cáo Ngày 1.
