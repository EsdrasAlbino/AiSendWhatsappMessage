import sys
import cv2
import numpy as np
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QPushButton, QVBoxLayout
from PyQt5.QtCore import QTimer
from PyQt5.QtGui import QImage, QPixmap
from ultralytics import YOLO


class YOLOv8App(QWidget):
    def __init__(self):
        super().__init__()

        self.initUI()

        # Load YOLOv8 model
        # Adjust the model path if necessary
        self.model = YOLO('weights/best.pt')

        # Initialize camera
        self.cap = cv2.VideoCapture(0)
        self.timer = QTimer(self)
        self.timer.timeout.connect(self.update_frame)
        self.timer.start(30)

    def initUI(self):
        self.setWindowTitle('ASUS_A001D')
        self.setGeometry(100, 100, 800, 600)

        self.label = QLabel(self)
        self.label.resize(800, 600)

        self.button = QPushButton('Close', self)
        self.button.clicked.connect(self.close)

        layout = QVBoxLayout()
        layout.addWidget(self.label)
        layout.addWidget(self.button)
        self.setLayout(layout)

    def update_frame(self):
        ret, frame = self.cap.read()
        if ret:
            results = self.model(frame)

            for result in results.xyxy[0]:
                x1, y1, x2, y2, conf, cls = result
                x1, y1, x2, y2 = int(x1), int(y1), int(x2), int(y2)
                label = self.model.names[int(cls)]
                confidence = float(conf)
                color = (0, 255, 0)
                cv2.rectangle(frame, (x1, y1), (x2, y2), color, 2)
                cv2.putText(frame, f'{label} {confidence:.2f}', (x1,
                            y1 - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.5, color, 2)

            image = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
            image = QImage(
                image.data, image.shape[1], image.shape[0], QImage.Format_RGB888)
            self.label.setPixmap(QPixmap.fromImage(image))

    def closeEvent(self, event):
        self.cap.release()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = YOLOv8App()
    ex.show()
    sys.exit(app.exec_())
