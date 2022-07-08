import cv2
def cam():
    key = cv2.waitKey(1)
    webcam= cv2.VideoCapture(0)
    while True:
        try:
            check, frame= webcam.read()
            print(check)
            print(frame)
            cv2.imshow("capturing", frame)
            key= cv2.waitKey(1)
            if key == ord('s'):
                cv2.imwrite(filename="saved_img.jpg", img=frame)
                webcam.release()
                img_new= cv2.imread('saved_img.jpg', cv2.IMREAD_GRAYSCALE)
                img_new= cv2.imshow("Captured Image", img_new)
                cv2.waitKey(1650)
                cv2.destroyAllWindows()
                print("processing image")
                img_=cv2.imread('saved_img.jpg', cv2.IMREAD_ANYCOLOR)
                gray=cv2.cvtColor(img_, cv2.COLOR_BGR2GRAY)
                img_=cv2.resize(gray,(28,29))
                img_resized=cv2.imwrite(filename='saved_img_final.jpg', img=img_)
                print("image saved! ")
                break
            elif key == ord('q'):
                print("turning off camera")
                webcam.release()
                print("program ended")
                cv2.destroyAllWindows()
                break
        except(KeyboardInterrupt):
            print("turning off camera")
            webcam.release()
            print("camera is off")
            cv2.destroyAllWindows()
            break
if __name__==("__main__"):
    cam()
