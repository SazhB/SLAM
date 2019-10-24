import cv2
import numpy as np
import sdl2
import sdl2.ext
import os 

os.environ["PYSDL2_DLL_PATH"] = "c:\\directory\of\\sdl2\\library"

w = 1920//2
h = 1080//2
cap = cv2.VideoCapture('INSERT MP4 FILE')

sdl2.ext.init()
window = sdl2.ext.Window('Driving', size=(w,h))
window.show()


def quit_windows():
    sdl2.SDL_QUIT
    #pygame.display.quit()
    cv2.destroyAllWindows()
    

def process_frame(img):
    img = cv2.resize(img, (w, h))
    events = sdl2.ext.get_events()
    for event in events:
        if event.type == sdl2.SDL_QUIT:
            exit(0)
    window.refresh()
    #cv2.imshow('frame', img)
    #print (img.shape)
    #print(img)
    surf = sdl2.ext.pixels3d(window.get_surface())
    surf[:, :, 0:3] = img.swapaxes(0,1)  
    window.refresh()


if __name__ == "__main__":
    while cap.isOpened():
        ret, frame = cap.read()
        #gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        if ret == True:
            process_frame(frame)
        else:
            break
      
    cap.release()
    cv2.destroyAllWindows()

