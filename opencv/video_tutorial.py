import cv2
import sys
import numpy as np

func = sys.argv[1]
###############################
if func == "webcam":
    video = cv2.VideoCapture(0)
    fourcc = cv2.VideoWriter_fourcc(*'MJPG')
    out = cv2.VideoWriter('movedlikejagger.avi', fourcc, 20.0, (640, 480))

    i = 0
    while(True):
        ret, frame = video.read()
        if ret == True:
            gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

            out.write(gray)

            cv2.imshow('video', gray)
            if cv2.waitKey(1) & 0xFF == ord('q'):
                break
            k = cv2.waitKey(1)
            if k == ord('q'):
                print("Exiting , {} pressed".format(k))
                break
            if k == ord('s'):
                print("Saving Image, {} pressed".format(k))
                filename = "frame{}.png".format(i)
                cv2.imwrite(filename, gray)
                i += 1
        else:
            break

    video.release()
    out.release()
    cv2.destroyAllWindows()

###############################
elif func == "videofile":
    cap = cv2.VideoCapture("movelikejagger.mp4")

    fourcc = cv2.VideoWriter_fourcc('M', 'J', 'P', 'G')
    size = (int(cap.get(3)), int(cap.get(4)))
    video = cv2.VideoWriter('movedlikejagger.avi', fourcc, 30.0, size, True)

    while cap.isOpened():
        ret, frame = cap.read()
        if not ret:
            break
        # gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        frame = cv2.flip(frame, 0)

        video.write(frame)

        cv2.imshow('moveslikejagger', frame)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
    cap.release()
    video.release()
    cv2.destroyAllWindows()


###############################
elif func == "savevideo":
    cap = cv2.VideoCapture(0)

    # Define the codec and create VideoWriter object
    fourcc = cv2.VideoWriter_fourcc('X', '2', '6', '4')
    fps = 30
    size = (1280, 720)
    print(fps, size)
    out = cv2.VideoWriter('output.avi', fourcc, fps, size, True)

    while(cap.isOpened()):
        ret, frame = cap.read()
        if ret == True:
            frame = cv2.flip(frame, 0)

            # write the flipped frame
            out.write(frame)

            cv2.imshow('frame', frame)
            if cv2.waitKey(1) & 0xFF == ord('q'):
                break
        else:
            break

    # Release everything if job is finished
    cap.release()
    out.release()
    cv2.destroyAllWindows()
