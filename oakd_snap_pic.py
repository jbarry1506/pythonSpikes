from sys import maxsize
import time
from pathlib import Path
import cv2
import depthai as dai


# create pipeline
pipeline = dai.Pipeline()

# define sources and outputs
camRgb = pipeline.create(dai.node.ColorCamera)


xoutRgb = pipeline.create(dai.node.XLinkOut)
controlIn = pipeline.create(dai.node.XLinkIn)

xoutRgb.setStreamName("rgb")
controlIn.setStreamName("control")

#properties
# cam preview settings
camRgb.setPreviewSize(300,300)
camRgb.setInterleaved(False)

camRgb.setBoardSocket(dai.CameraBoardSocket.RGB)
camRgb.setResolution(dai.ColorCameraProperties.SensorResolution.THE_1080_P)

# Linking
camRgb.still.link(xoutRgb.input)
controlIn.out.link(camRgb.inputControl)

# connect to device and start pipeline
with dai.Device(pipeline) as device:
    # check camera
    print(f"Connected cameras {device.getConnectedCameras()}")
    # check USB speed
    print(F"USB SPEED: {device.getUsbSpeed().name}")

    # Output queue will be used to get the rgb frames from the output defined above
    qRgb = device.getOutputQueue(name="rgb", maxSize=4, blocking=False)
    controlQueue = device.getInputQueue("control")

    # make sure the destination path is present before starting to store the pictures
    dirname = "/home/jbarry1506/Pictures/oak-d/astronomy"
    # Path(dirname).mkdir(parents=True, exist_ok=True)

    start_time = time.time()

    while True:
        inRgb = qRgb.get() # non-blocking call, will return new data or None otherwise
        cv2.imshow("rgb", inRgb.getCvFrame())

        pressedkey = cv2.waitKey(1) & 0xFF
        if pressedkey == ord("q"):
            break
        elif pressedkey == ord("p"):
            ctrl = dai.CameraControl()
            ctrl.setCaptureStill(True)
            print(f"The capture mode is {ctrl.getCaptureStill()}")
            cv2.imwrite(f"{dirname}/{int(time.time() * 1000)}.png", inRgb.getCvFrame())

            controlQueue.send(ctrl)

        # else:

        #     time.sleep(10)
            
