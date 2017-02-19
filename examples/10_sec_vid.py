from gopro import GoPro
import time
camera = GoPro.GoPro()
camera.video()
time.sleep(5)
camera.hilight()
time.sleep(5)
camera.stop()
