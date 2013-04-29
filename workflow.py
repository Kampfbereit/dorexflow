import time
import datetime
import cv2
from PIL import ImageGrab
import winsound

#cam = cv2.VideoCapture(0)
winName = "Movement Indicator"
#cv2.namedWindow(winName, cv2.CV_WINDOW_AUTOSIZE)

bildNr = 0

cam = cv2.VideoCapture(0)


while True:
    #cv2.destroyWindow(winName)
    #cv2.imshow(winName,cam.read()[1])
    key = cv2.waitKey(10)
    if key == 27:
        cv2.destroyWindow(winName)
        break

    time.sleep(2)
    ts = time.time()
    nowTime = datetime.datetime.fromtimestamp(ts).strftime('%Y-%m-%d_%H-%M-%S')
    im = ImageGrab.grab()
    # Tkinter.Tk().bell()
    winsound.PlaySound('koko.wav', winsound.SND_FILENAME)
    im.save('workflow/screenshot_'+str(nowTime)+'.png')
    cv2.imwrite('workflow/'+'you_'+str(nowTime)+'.jpg',cam.read()[1])
    time.sleep(2)
    bildNr += 1
    print 'snap'+str(bildNr)
    time.sleep(60*10)

cam.release()

print "Goodbye"
