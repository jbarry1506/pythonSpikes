
import cv2
import depthai as dai
import time

# create pipeline
pipeline = dai.Pipeline()

# define sources and outputs
camRgb = pipeline.create(dai.node.ColorCamera)
xoutRgb = pipeline.create(dai.node.XLinkOut)

xoutRgb.setStreamName("rgb")

#properties
# cam preview settings
camRgb.setPreviewSize(1080,720)
camRgb.setInterleaved(False)
camRgb.setColorOrder(dai.ColorCameraProperties.ColorOrder.RGB)
camRgb.setResolution(dai.ColorCameraProperties.SensorResolution.THE_4_K)

# Linking
camRgb.preview.link(xoutRgb.input)

# connect to device and start pipeline
with dai.Device(pipeline) as device:
    # check camera
    print(f"Connected cameras {device.getConnectedCameras()}")
    # check USB speed
    print(F"USB SPEED: {device.getUsbSpeed().name}")

    # Output queue will be used to get the rgb frames from the output defined above
    qRgb = device.getOutputQueue(name="rgb", maxSize=4, blocking=False)

    # make sure the destination path is present before starting to store the pictures
    dirname = "/home/jbarry1506/Pictures/oak-d/astronomy"
    # Path(dirname).mkdir(parents=True, exist_ok=True)

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
