# before executing this code, check to see if settings are permanent
# or do they reset after code execution, or after disconnection from power

import depthai as dai


pipeline = dai.Pipeline()

mono = pipeline.createMonoCamera()
mono.setBoardSocket(dai.CameraBoardSocket.LEFT)

xout = pipeline.createXLinkOut()
xout.setStreamName("left")
mono.out.link(xout.input)

with dai.Device(pipeline) as device:
    queue = device.getOutputQueue(name="left")
    frame = queue.get()
    
imOut = frame.getCvFrame()
cv2.imshow("Image", imOut)
