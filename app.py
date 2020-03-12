import cv2
from flask import Flask , Response , render_template

cam = cv2.VideoCapture(0)
app = Flask(__name__)

def stream():
    while 1 :
        __,frame = cam.read()
        imgencode = cv2.imencode('.jpg',frame)[1]
        strinData = imgencode.tostring()
        yield (b'--frame\r\n'b'Content-Type: text/plain\r\n\r\n'+strinData+b'\r\n')

@app.route('/video')
def video():
    return Response(stream(),mimetype='multipart/x-mixed-replace; boundary=frame')

@app.route('/')
def main():
    return render_template('index.html')

if __name__ == "__main__":
    app.run()