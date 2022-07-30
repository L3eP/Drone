"""
Simple controller mini drone by dji call tello
basic keyboard control
takeoff using space
move w(forward), a(left), s(back), d(right),r(up), f(down)
rotaion: q(left), e(right)
flip: i(forward), j(to left), k(backward), l(to right)
"""


from cv2 import batchDistance
from djitellopy import Tello
import cv2

tello = Tello()
tello.connect()

tello.streamon()
frame_read = tello.get_frame_read()
battry_read = tello.get_battery()

while True:
    img = frame_read.frame
    img = cv2.resize(img, (720, 480))
    img = battry_read.as_integer_ratio
    cv2.imshow("Dji Tello", img)

    key = cv2.waitKey(1) & 0xff
    if key == 32: #Space
        tello.takeoff() #terbang
    elif key == ord('w'):
        tello.move_forward(20)  #maju
    elif key == ord('a'):
        tello.move_left(20) #kiri
    elif key == ord('s'):
        tello.move_back(20) #mundur
    elif key == ord('d'):
        tello.move_right(20) #kanan
    elif key == ord('e'):
        tello.rotate_clockwise(20) #rotasi_searah_jarum_jam
    elif key == ord('q'):
        tello.rotate_counter_clockwise(20) #rotasi_berlawanan_jarum_jam
    elif key == ord('r'):
        tello.move_up(20) #naik
    elif key == ord('f'):
        tello.move_down(20) #turun
    elif key == ord('i'):
        tello.flip_forward #flip_depan
    elif key == ord('k'):
        tello.flip_back #flip_belakang
    elif key == ord('l'):
        tello.flip_right #flip_kanan
    elif key == ord('j'):
        tello.flip_left #flip_kiri
    elif key == 27: #ESC 
        tello.land() #landing
        cv2.destroyAllWindows() 
        break