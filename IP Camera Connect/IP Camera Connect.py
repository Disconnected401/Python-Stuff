import cv2

def connect_to_ip_camera(ip, port, sensitivity, resize_factor):
    rtsp_url = f"rtsp://{ip}:{port}"
    cap = cv2.VideoCapture(rtsp_url)

    if not cap.isOpened():
        print("Error: Unable to connect to the camera.")
        return

    ret, frame1 = cap.read()
    ret, frame2 = cap.read()

    while cap.isOpened():
        diff = cv2.absdiff(frame1, frame2)
        gray = cv2.cvtColor(diff, cv2.COLOR_BGR2GRAY)
        blur = cv2.GaussianBlur(gray, (5, 5), 0)
        _, thresh = cv2.threshold(blur, sensitivity, 255, cv2.THRESH_BINARY)
        dilated = cv2.dilate(thresh, None, iterations=3)
        contours, _ = cv2.findContours(dilated, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

        for contour in contours:
            if cv2.contourArea(contour) < 500:
                continue
            x, y, w, h = cv2.boundingRect(contour)
            cv2.rectangle(frame1, (x, y), (x + w, y + h), (0, 255, 0), 2)

        width = int(frame1.shape[1] * resize_factor / 100)
        height = int(frame1.shape[0] * resize_factor / 100)
        resized_frame = cv2.resize(frame1, (width, height))

        cv2.imshow('IP Camera', resized_frame)
        frame1 = frame2
        ret, frame2 = cap.read()

        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

        if cv2.getWindowProperty('IP Camera', cv2.WND_PROP_VISIBLE) < 1:
            break

    cap.release()
    cv2.destroyAllWindows()

if __name__ == "__main__":
    sensitivity = 100  # Adjust sensitivity as needed
    resize_factor = 50  # Resize window to 50% of the original size
    connect_to_ip_camera("192.168.100.101", 554, sensitivity, resize_factor)