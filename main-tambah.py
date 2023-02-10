from PyQt5.uic import loadUi
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QVBoxLayout
from PyQt5.QtWidgets import QFileDialog, QMessageBox, QAction, QMainWindow, QSlider, QPushButton, QToolTip
from PyQt5.QtGui import QPixmap, QImage
import cv2
import glob
import os
import matplotlib.pyplot as plt
from PIL import Image
import numpy as np
from math import sin, cos

class Ui_MainWindow(QMainWindow):
    def __init__(self):
        QMainWindow.__init__(self)
        loadUi('viscom.ui', self)

        # Declaration
        self.image = ''

        # Function Button
        self.pushButton.clicked.connect(self.openImg)
        self.pushButton_2.clicked.connect(self.negasiIMG)
        self.pushButton_3.clicked.connect(self.flippingHIMG)
        self.pushButton_4.clicked.connect(self.flippingVIMG)
        self.pushButton_5.clicked.connect(self.Grayscale)
        self.pushButton_6.clicked.connect(self.rotasi)
        self.pushButton_7.clicked.connect(self.flippingHVIMG)
        self.pushButton_8.clicked.connect(self.croping)
        self.pushButton_9.clicked.connect(self.scaling)
        

    def openImg(self):
        
        files = glob.glob('*.jpg')
        for file in files:
            os.remove(file)


        plt.close()
        self.listWidget.clear()
        self.label_2.clear()

        self.imgName, imgType = QFileDialog.getOpenFileName(self.centralwidget, "Open Image", "",
                                                              "*.jpg;;All Files(*)")
        jpg = QPixmap(self.imgName)

        pictureBox1 = self.label_2
        pictureBox1.setPixmap(jpg)



        self.filename = os.path.basename(self.imgName)
        self.cv_img = cv2.imread(self.imgName, cv2.IMREAD_UNCHANGED)
        size = self.cv_img.shape
        bit = self.cv_img.dtype
        print(bit)

        # self.bit_print = print(bit)
        self.label_3.setText('Name File    : ' + self.filename +
                             '\nDimension   : ' + str(size) +
                             '\nHeight        : ' + str(size[1]) +
                             '\nWidth         : ' + str(size[0]) +
                             '\nDepth Color : ' + str(size[2]) +
                             '\nBit Depth     : {}'.format(str(bit)[4]) + '-bit')
        
        # Print nilai RGB
        self.listWidget.addItem('RGB per pixel :')
        
        for x in range(size[0]):
            for y in range(size[1]):
                file1 = open("out1.txt", "a")  # write mode
                file1.write(' {},{}\t: {}'.format(x, y, self.cv_img[x, y]))
                file1.close()
                
                self.listWidget.addItem(' {},{}\t: {}'.format(x, y, self.cv_img[x, y]))
        
       
    
    # =========== Negasi =============
    def negasiIMG(self):
        self.label_6.clear()
        # ========== Open Image ===========
        # ============ NEGASI NEW ============
        img = Image.open(self.imgName).convert('RGB')
        for i in range(0, img.size[0]-1):
            for j in range(0, img.size[1]-1):
                pixelColorVals = img.getpixel((i,j))
                #print(pixelColorVals)
                redPixel    = 255 - pixelColorVals[0]
                greenPixel  = 255 - pixelColorVals[1] 
                bluePixel   = 255 - pixelColorVals[2] 

                img.putpixel((i,j),(redPixel, greenPixel, bluePixel))

        img.save('image\OUT-NEGASI.jpg')
        jpg = QPixmap('image\OUT-NEGASI.jpg')
        pictureBox1 = self.label_6
        pictureBox1.setPixmap(jpg)
    
    # ========= Flipping =============
    def flippingHIMG(self):
        self.label_7.clear()

        # ============ Flipping Horizontal ============
        img = Image.open(self.imgName)
        PIXEL = img.load()
        ukuran_horizontal = img.size[0]
        ukuran_vertikal = img.size[1]

        IMG_BARU = Image.new("RGB", (ukuran_horizontal, ukuran_vertikal))
        PIXEL_BARU = IMG_BARU.load()

        for x in range(ukuran_horizontal):
            for y in range(ukuran_vertikal):
                PIXEL_BARU[x, y] = PIXEL[ukuran_horizontal - 1 - x, y]

        IMG_BARU.save('image\OUT-FLIP.jpg')

        OUT_IMG = QPixmap('image\OUT-FLIP.jpg')

        pictureBox1 = self.label_7
        pictureBox1.setPixmap(OUT_IMG)
    
    # ============ Flipping Vertikal ============
    def flippingVIMG(self):
        self.label_7.clear()
        IMG = Image.open(self.imgName)
        PIXEL = IMG.load()
        ukuran_horizontal = IMG.size[0]
        ukuran_vertikal = IMG.size[1]

        IMG_BARU = Image.new("RGB", (ukuran_horizontal, ukuran_vertikal))
        PIXEL_BARU = IMG_BARU.load()

        for x in range(ukuran_horizontal):
            for y in range(ukuran_vertikal):
                PIXEL_BARU[x, y] = PIXEL[x, ukuran_vertikal - 1 - y]

        IMG_BARU.save('image\OUT-FLIP.jpg')

        OUT_IMG = QPixmap('image\OUT-FLIP.jpg')

        pictureBox1 = self.label_7
        pictureBox1.setPixmap(OUT_IMG)

    def flippingHVIMG(self):
        self.label_7.clear()

        # ============ Flipping Horizontal ============
        img = Image.open(self.imgName)
        PIXEL = img.load()
        ukuran_horizontal = img.size[0]
        ukuran_vertikal = img.size[1]

        IMG_BARU = Image.new("RGB", (ukuran_horizontal, ukuran_vertikal))
        PIXEL_BARU = IMG_BARU.load()

        for x in range(ukuran_horizontal):
            for y in range(ukuran_vertikal):
                PIXEL_BARU[x, y] = PIXEL[ukuran_horizontal - 1 - x, ukuran_vertikal - 1 - y]

        IMG_BARU.save('image\OUT-FLIP.jpg')

        OUT_IMG = QPixmap('image\OUT-FLIP.jpg')

        pictureBox1 = self.label_7
        pictureBox1.setPixmap(OUT_IMG)

    
    # fungsi citra biner
    def Grayscale(self):
        self.label_7.clear()
        # konversi gambar RGB ke grayscale
        # https://stackoverflow.com/a/18778280/9157799
        IMG = Image.open(self.imgName).convert('L')
        PIXEL_GRAYSCALE = IMG.load()
        
        nilai_ambang = 150 #150 = nilai ambang untuk menentukan hitam atau putih

        ukuran_horizontal = IMG.size[0]
        ukuran_vertikal = IMG.size[1]

        for x in range(ukuran_horizontal):
            for y in range(ukuran_vertikal):
                if PIXEL_GRAYSCALE[x, y] < nilai_ambang: 
                    PIXEL_GRAYSCALE[x, y] = 0
                else:
                    PIXEL_GRAYSCALE[x, y] = 255
        
        IMG.save('image\OUT-GREY.jpg')
        OUT_IMG = QPixmap('image\OUT-GREY.jpg')
        histogram, bin_edges = np.histogram(self.cv_img, bins=256, range=(0, 1))
        plt.plot(bin_edges[0:-1], histogram)  # <- or here
        plt.show()

        pictureBox1 = self.label_8
        pictureBox1.setPixmap(OUT_IMG)
        
    
    #Rotasi 
    def rotasi(self):
        self.label_9.clear()
        IMG = Image.open(self.imgName)
        derajat = 90
        PIXEL = IMG.load()

        ukuran_horizontal = IMG.size[0]
        ukuran_vertikal = IMG.size[1]

        IMG_BARU = Image.new("RGB", (ukuran_horizontal, ukuran_vertikal))
        PIXEL_BARU = IMG_BARU.load()

        x_tengah = ukuran_horizontal // 2
        y_tengah = ukuran_vertikal // 2

        for x in range(ukuran_horizontal):
            for y in range(ukuran_vertikal):
                # theta == radian
                theta = derajat * 22/7 / 180
                # rumus rotasi dengan pusat rotasi bebas (disini tengah)
                x_baru = (cos(theta) * (x - x_tengah) - sin(theta)
                        * (y - y_tengah) + x_tengah)
                y_baru = (sin(theta) * (x - x_tengah) + cos(theta)
                        * (y - y_tengah) + y_tengah)
                
                # rumus rotasi dengan pusat rotasi (0, 0)
                # dari buku rinaldi munir
                # x_baru = x*cos(theta) - y*sin(theta)
                # y_baru = x*cos(theta) + y*cos(theta)

                if (x_baru >= ukuran_horizontal or y_baru >= ukuran_vertikal
                        or x_baru < 0 or y_baru < 0):
                    PIXEL_BARU[x, y] = (0, 0, 0)
                else:
                    PIXEL_BARU[x, y] = PIXEL[x_baru, y_baru]

        IMG_BARU.save('image\OUT-ROTATE.jpg')
        OUT_IMG = QPixmap('image\OUT-ROTATE.jpg')

        pictureBox1 = self.label_9
        pictureBox1.setPixmap(OUT_IMG)
    
    #Fungsi untuk CROP
    def croping(self):
        self.label_9.clear()
        IMG = Image.open(self.imgName)
        PIXEL = IMG.load()
        ukuran_horizontal = IMG.size[0]
        ukuran_vertikal = IMG.size[1]
        #NILAI posisi x,y akan dimulai dari xL dan yT
        xL= 50
        yT= 50

        IMG_BARU = Image.new("RGB", (ukuran_horizontal-xL, ukuran_vertikal-yT))
        PIXEL_BARU = IMG_BARU.load()
        #Ukuran File Akan Dikurangi nilai xL dan yT agar tidak ada Blank Hitam
        for x in range(ukuran_horizontal-xL):
            for y in range(ukuran_vertikal-yT):
                PIXEL_BARU[x, y] = PIXEL[x+xL, y+yT] #NILAI posisi x0,y0 dimulai dari x+xT,y+yT
                print(' {},{}\t: {}'.format(x, y, PIXEL_BARU[x, y]))
        IMG_BARU.save('image\OUT-CROP.jpg')

        OUT_IMG = QPixmap('image\OUT-CROP.jpg')

        pictureBox1 = self.label_10
        pictureBox1.setPixmap(OUT_IMG)
    
    def scaling(self):
        self.label_11.clear()
        IMG = Image.open(self.imgName)
        PIXEL = IMG.load()
        basewidth = IMG.size[0]*2
        wpercent = (basewidth / float(IMG.size[0]))
        hsize = int((float(IMG.size[1]) * float(wpercent)))
        IMG_BARU = IMG.resize((IMG.size[0], hsize), Image.ANTIALIAS)
        IMG_BARU.save('image\OUT-SCALE.jpg')
        OUT_IMG = QPixmap('image\OUT-SCALE.jpg')
        print(wpercent,hsize)

        pictureBox1 = self.label_11
        pictureBox1.setPixmap(OUT_IMG)
    
app = QApplication([])
window = Ui_MainWindow()
window.show()
app.exec()