import cv2
import depthai as dai


# check to see if the camera has a command to capture a still
daicam = dai.CameraControl()
still = daicam.getCaptureStill()

if still:
    pass
else:
    print(f"There is no command to capture a still: {still}",
          "\nFixing it!")
    #
    daicam_truth = daicam.setCaptureStill(True)
    print(f"This is the daicam_truth:  {daicam_truth}!")
    print(f"This is what we started with:  {still}")
    still = daicam_truth
    print(f"Now this is what we got:  {still}")

daicam.setCaptureStill(True)

if still:
    print("still capture is set.")
