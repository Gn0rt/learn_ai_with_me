# Báo cáo ngày 1
Ngày 1: Tôi đã làm quen với python dựa vào nền tàng JS đã có. Theo lịch trình bạn đã đưa ra, ngày 1 tuần 1 tôi cần làm quen Biến, kiểu dữ liệu, list, dict, for, if, function, import.
Dựa vào ví dụ của bạn:

```Python
#Day 1: Kiểu dữ liệu
#khai báo một mảng
cameras = [
    {"id": 1, "name": "Camera 01", "online": True},
    {"id": 2, "name": "Camera 02", "online": True},
    {"id": 3, "name": "Camera 03", "online": False},
    {"id": 4, "name": "Camera 04", "online": True},
    {"id": 5, "name": "Camera 05", "online": False},
]
#function
def get_online_cameras(device):
    result = []
    #loop
    for camera in cameras:
        if(camera["online"]):
            result.append(camera)

    return result

online_cameras = get_online_cameras(cameras)
#print
print("Số camera online: ", len(online_cameras))

for camera in online_cameras:
    print(camera["name"])
```

Tôi đã thực hiện bài tập bạn đưa ra:
### Bài tập thực hành
Viết class `CameraDevice` gồm:
- `id`: mã camera.
- `name`: tên camera.
- `is_online`: trạng thái.
- `fps`: số frame mỗi giây.
- Phương thức `get_info()` trả về thông tin camera.

```python
class CameraDevice:
    def __init__(self,id, name,is_online,fps):
        self.id = id
        self.name = name
        self.is_online = is_online
        self.fps = fps

    def get_info(self):
        isOnline = ""
        if(self.is_online):
            isOnline = "Online"
        else:
            isOnline = "Offline"
        print(f"Camera: {self.name} \nName: {self.is_online} \nFPS: {self.fps} \nStatus: {isOnline}")


cam1 = CameraDevice("CAM001","Driver Camera",True,30)
cam1.get_info()
```

Và tôi có biến đổi một chút, sử dụng random để có thể render ngẫu nhiên ID của Camera
```python
import random
class CameraDevice:
    def __init__(self,id, name,is_online,fps):
        self.id = id
        self.name = name
        self.is_online = is_online
        self.fps = fps

    def get_info(self):
        isOnline = ""
        if(self.is_online):
            isOnline = "Online"
        else:
            isOnline = "Offline"
        print(f"Camera: {self.id} \nName: {self.name} \nFPS: {self.fps} \nStatus: {isOnline}")

def random_number():
    return random.randint(1,100)

idCAM = "CAM" + str(random_number())
cam1 = CameraDevice(idCAM,"Driver Camera",True,30)
cam1.get_info()
```

Và tôi cũng tự rút ra cách viết class theo quy chuẩn giống như bên C# để dễ dàng hình dung cũng như thói quen để áp dụng sau này
```python
class Person:
    # Khai báo trước các thuộc tính (tùy chọn nhưng giúp IDE gợi ý tốt như C#)
    name: str
    age: int

    def __init__(self, name: str, age: int):
        self.name = name  # Tương đương this.name = name trong C#
        self.age = age

    def introduce(self) -> str:
        return f"Hello, my name is {self.name} and I am {self.age} years old."


# Cách sử dụng
p = Person("Nam", 25)
print(p.introduce())
```