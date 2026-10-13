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