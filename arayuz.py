import sys
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
import cv2
import serial
from PyQt5 import QtCore, QtGui, QtWidgets
import numpy as np
class MainWindow(QWidget):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.otonom = 1

        self.timer = QTimer(self)
        self.timer.setSingleShot(False)
        self.timer.setInterval(10) # in milliseconds, so 5000 = 5 seconds
        self.timer.timeout.connect(self.loop)
        self.timer.start()
        self.resize(1000, 700)
        self.VBL = QVBoxLayout()

        self.FeedLabel = QLabel()
        self.VBL.addWidget(self.FeedLabel)

        self.CancelBTN = QPushButton("Kapat")
        self.CancelBTN.clicked.connect(self.CancelFeed)
        self.VBL.addWidget(self.CancelBTN)

        self.Worker1 = Worker1()

        self.Worker1.start()
        self.Worker1.ImageUpdate.connect(self.ImageUpdateSlot)
        self.setLayout(self.VBL)
        self.port_secim_label = QtWidgets.QLabel(self)
        self.port_secim_label.setGeometry(QtCore.QRect(815, 50, 31, 20))
        self.port_secim_label.setObjectName("port_secim_label")
        self.Baudrate_label = QtWidgets.QLabel(self)
        self.Baudrate_label.setGeometry(QtCore.QRect(815, 80, 101, 20))
        self.Baudrate_label.setObjectName("Baudrate_label")
        self.port_secim_ComboBox = QtWidgets.QComboBox(self)
        self.port_secim_ComboBox.setGeometry(QtCore.QRect(875, 80, 69, 22))
        self.port_secim_ComboBox.setObjectName("port_secim_ComboBox")
        self.port_secim_ComboBox.addItem("")
        self.port_secim_ComboBox.addItem("")
        self.port_secim_ComboBox.addItem("")
        self.port_secim_ComboBox.addItem("")
        self.port_secim_ComboBox.addItem("")
        self.port_secim_ComboBox.addItem("")
        self.port_secim_ComboBox.addItem("")
        self.port_secim_ComboBox.addItem("")
        self.port_secim_ComboBox.addItem("")
        self.Baudrate_ComboBox = QtWidgets.QComboBox(self)
        self.Baudrate_ComboBox.setGeometry(QtCore.QRect(875, 50, 69, 22))
        self.Baudrate_ComboBox.setObjectName("Baudrate_ComboBox")
        self.Baudrate_ComboBox.addItem("")
        self.Baudrate_ComboBox.addItem("")
        self.Baudrate_ComboBox.addItem("")
        self.Baudrate_ComboBox.addItem("")
        self.Baudrate_ComboBox.addItem("")
        self.Baudrate_ComboBox.addItem("")
        self.Baudrate_ComboBox.addItem("")
        self.Baudrate_ComboBox.addItem("")
        self.Baudrate_ComboBox.addItem("")
        self.Baudrate_ComboBox.addItem("")
        self.Baudrate_ComboBox.addItem("")
        self.Baudrate_ComboBox.addItem("")
        self.Baudrate_ComboBox.addItem("")
        self.Baudrate_ComboBox.addItem("")
        self.Baudrate_ComboBox.addItem("")
        self.baglan_buton = QtWidgets.QPushButton(self)
        self.baglan_buton.setGeometry(QtCore.QRect(875, 120, 75, 23))
        self.baglan_buton.setObjectName("baglan_buton")
        self.baglan_buton.clicked.connect(self.baglan)

        self.label = QtWidgets.QLabel(self)
        self.label.setGeometry(QtCore.QRect(749, 230, 251, 251))
        self.label.setText("")
        self.label.setPixmap(QtGui.QPixmap("pashala logo tasarım 1 (5).png"))
        self.baglan_label = QtWidgets.QLabel(self)
        self.baglan_label.setGeometry(QtCore.QRect(875, 140, 91, 20))
        self.baglan_label.setObjectName("baglan_label")
        self.baglan_label.setText("Bağlantı Bekleniyor")
        self.baglan_label2 = QtWidgets.QLabel(self)
        self.baglan_label2.setGeometry(QtCore.QRect(875, 140, 91, 20))
        self.baglan_label2.setObjectName("baglan_label2")
        self.baglan_label2.setText("Bağlantı Başarılı")
        self.baglan_label2.setHidden(True)
        self.baglan_label3 = QtWidgets.QLabel(self)
        self.baglan_label3.setGeometry(QtCore.QRect(875, 140, 91, 20))
        self.baglan_label3.setObjectName("baglan_label3")
        self.baglan_label3.setText("Bağlantı Başarısız")
        self.baglan_label3.setHidden(True)
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self)
        self.label_2.setGeometry(QtCore.QRect(150, 70, 231, 271))
        self.retranslateUi(self)
    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.port_secim_label.setText(_translate("Dialog", "Port/"))
        self.Baudrate_label.setText(_translate("Dialog", "BaudRate/"))
        self.Baudrate_ComboBox.setCurrentText(_translate("Dialog", "9600"))
        self.Baudrate_ComboBox.setItemText(0, _translate("Dialog", "4800"))
        self.Baudrate_ComboBox.setItemText(1, _translate("Dialog", "9600"))
        self.Baudrate_ComboBox.setItemText(2, _translate("Dialog", "14400"))
        self.Baudrate_ComboBox.setItemText(3, _translate("Dialog", "19200"))
        self.Baudrate_ComboBox.setItemText(4, _translate("Dialog", "28800"))
        self.Baudrate_ComboBox.setItemText(5, _translate("Dialog", "31250"))
        self.Baudrate_ComboBox.setItemText(6, _translate("Dialog", "38400"))
        self.Baudrate_ComboBox.setItemText(7, _translate("Dialog", "57600"))
        self.Baudrate_ComboBox.setItemText(8, _translate("Dialog", "115200"))
        self.port_secim_ComboBox.setItemText(0, _translate("Dialog", "COM1"))
        self.port_secim_ComboBox.setItemText(1, _translate("Dialog", "COM2"))
        self.port_secim_ComboBox.setItemText(2, _translate("Dialog", "COM3"))
        self.port_secim_ComboBox.setItemText(3, _translate("Dialog", "COM4"))
        self.port_secim_ComboBox.setItemText(4, _translate("Dialog", "COM5"))
        self.port_secim_ComboBox.setItemText(5, _translate("Dialog", "COM6"))
        self.port_secim_ComboBox.setItemText(6, _translate("Dialog", "COM7"))
        self.port_secim_ComboBox.setItemText(7, _translate("Dialog", "COM8"))
        self.port_secim_ComboBox.setItemText(8, _translate("Dialog", "COM9"))
        self.port_secim_ComboBox.setItemText(9, _translate("Dialog", "COM10"))
        self.port_secim_ComboBox.setItemText(10, _translate("Dialog", "COM11"))
        self.port_secim_ComboBox.setItemText(11, _translate("Dialog", "COM12"))
        self.port_secim_ComboBox.setItemText(12, _translate("Dialog", "COM13"))
        self.port_secim_ComboBox.setItemText(13, _translate("Dialog", "COM14"))
        self.port_secim_ComboBox.setItemText(14, _translate("Dialog", "COM15"))
        self.baglan_buton.setText(_translate("Dialog", "Bağlan"))
        
    
    def ImageUpdateSlot(self, Image):
        self.FeedLabel.setPixmap(QPixmap.fromImage(Image))
    def keyPressEvent(self, event):
        if event.key() == Qt.Key_W:
            print("W")
            self.arduino.write(b'1')
        elif event.key() == Qt.Key_S:
            print("S")
            self.arduino.write(b'2')
        elif event.key() == Qt.Key_A:
            print("A")
            self.arduino.write(b'3')
        elif event.key() == Qt.Key_D:
            print("D")
            self.arduino.write(b'4')
        elif event.key() == Qt.Key_Q:
            print("5")
            self.arduino.write(b'5')
        elif event.key() == Qt.Key_E:
            print("6")
            self.arduino.write(b'6')
        elif event.key() == Qt.Key_O:
            self.otonom = True
        elif event.key() == Qt.key_P:
            self.otonom = False
    def CancelFeed(self):
        exit()
    def baglan(self, Dialog):
        try:
            self.arduino = serial.Serial(port=str(self.port_secim_ComboBox.currentText()),baudrate = int(self.Baudrate_ComboBox.currentText()))
            self.baglan_label.setHidden(True)
            self.baglan_label2.setHidden(False)
            self.baglan_label3.setHidden(True)
        except:
            self.baglan_label.setHidden(True)
            self.baglan_label2.setHidden(True)
            self.baglan_label3.setHidden(False)
    def loop(self):
        if self.otonom == True:
            cap = cv2.VideoCapture(0,cv2.CAP_DSHOW)
            _, frame = cap.read()
            hsv = cv2.cvtColor(frame,cv2.COLOR_BGR2HSV)
            lowb = np.array([50,50,50])
            lowy = np.array([40, 50, 50]) 
            highb = np.array([130,255,255])

            maskb = cv2.inRange(hsv,lowb,highb)
            image = cv2.cvtColor(maskb, cv2.COLOR_BGR2RGB)
            gray = cv2.cvtColor(image, cv2.COLOR_RGB2GRAY)
            _, binary = cv2.threshold(gray, 225, 255, cv2.THRESH_BINARY_INV)
            contours, hierarchy = cv2.findContours(binary, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
            image = cv2.drawContours(image, contours, -1, (0, 255, 0), 2)
            cv2.imshow("contours",image)
        else:
            cv2.destroyAllWindows()
class Worker1(QThread):
    def __init__(self):
        super(Worker1,self).__init__()
    def on_change(self,data):
        self.otonom = data
    ImageUpdate = pyqtSignal(QImage)
    def run(self):
        self.ThreadActive = True
        Capture = cv2.VideoCapture(0,cv2.CAP_DSHOW)
        while self.ThreadActive:
            ret, frame = Capture.read()
            if ret:
                frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
                FlippedImage = cv2.flip(frame, 1)
                ConvertToQtFormat = QImage(FlippedImage.data, FlippedImage.shape[1], FlippedImage.shape[0], QImage.Format_RGB888)
                Pic = ConvertToQtFormat.scaled(700, 700, Qt.KeepAspectRatio)
                self.ImageUpdate.emit(Pic)
    def stop(self):
        self.ThreadActive = False
        self.quit()
    
if __name__ == "__main__":
    App = QApplication(sys.argv)
    Root = MainWindow()
    Root.show()
    sys.exit(App.exec())
