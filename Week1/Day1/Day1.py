class CameraDevice:
    id: str
    name: str
    is_online: bool
    fps: int
    def __init__(self, id: str, name: str, is_online: bool, fps: int) -> None:
        self.id = id
        self.name = name
        self.is_online = is_online
        self.fps = fps
    def get_info(self) -> str:
        status = "Online" if self.is_online else "Offline"
        return (
            f"Camera: {self.id}\n"
            f"Name: {self.name}\n"
            f"FPS: {self.fps}\n"
            f"Status: {status}\n"
        )

cameras = [
    CameraDevice("CAM001", "Front", True, 30),
    CameraDevice("CAM002", "Driver", False, 25),
    CameraDevice("CAM003", "Rear", True, 20),
    CameraDevice("CAM004", "Left", False, 15),
    CameraDevice("CAM005", "Right", False, 30)
]
# Get camera online
def get_online_cameras(listCameras):
    online_cameras = []
    for camera in listCameras:
        if camera.is_online:
            online_cameras.append(camera)
    return online_cameras

# Tính fps trung bình
def get_average_fps(listCameras):
    count = 0
    for camera in listCameras:
        count += camera.fps
    return count/len(listCameras)

online_cameras = get_online_cameras(cameras)
print(f"Online Cameras: {len(online_cameras)}")

average_fps = get_average_fps(online_cameras)
print(f"Average FPS: {average_fps}")

print(f"Total Cameras: {len(cameras)}")
print("-----")
for camera in cameras:
    print(camera.get_info())

