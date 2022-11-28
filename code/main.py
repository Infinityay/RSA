################################################################################
##
## BY: WANDERSON M.PIMENTA
## PROJECT MADE WITH: Qt Designer and PySide2
## V: 1.0.0
##
## This project can be used freely for all uses, as long as they maintain the
## respective credits only in the Python scripts, any information in the visual
## interface (GUI) can be modified without any implication.
##
## There are limitations on Qt licenses if you want to use your products
## commercially, I recommend reading them on the official website:
## https://doc.qt.io/qtforpython/licenses.html
##
################################################################################
import os
import sys
import platform
from hashlib import md5
import ctypes

from PySide2 import QtCore, QtGui, QtWidgets
from PySide2.QtCore import (QCoreApplication, QPropertyAnimation, QDate, QDateTime, QMetaObject, QObject, QPoint, QRect,
                            QSize, QTime, QUrl, Qt, QEvent, QRegExp)
from PySide2.QtGui import (QBrush, QColor, QConicalGradient, QCursor, QFont, QFontDatabase, QIcon, QKeySequence,
                           QLinearGradient, QPalette, QPainter, QPixmap, QRadialGradient, QIntValidator,
                           QRegExpValidator)
from PySide2.QtWidgets import *
import binascii
import random
import sys
from gmpy2 import gmpy2, mpz

# GUI FILE
from app_modules import *

sys.setrecursionlimit(1000000)


class MainWindow(QMainWindow):
    def __init__(self):
        QMainWindow.__init__(self)

        ############### #####  以下是RSA所需的参数  ############################
        self.p = 0
        self.q = 0
        self.n = 0
        self.varphi = 0
        self.e = 0
        self.d = 0
        self.pubKey = 0
        self.priKey = 0
        self.cipher_text = 0
        # 时间钟 为了生成随机数
        self.rs = gmpy2.random_state(random.randint(0, 100))
        ############################# 以上是RSA所需的参数 ############################
        self.ui = Ui_MainWindow()  ############################
        self.ui.setupUi(self)

        self.ui.lineEdit.setValidator(QRegExpValidator(QRegExp("[0-9]+$")))
        self.ui.lineEdit_2.setValidator(QRegExpValidator(QRegExp("[0-9]+$")))
        # btn
        self.ui.pushButton_20.clicked.connect(self.encodeM)
        self.ui.pushButton_19.clicked.connect(self.generatePrimes)
        self.ui.pushButton_3.clicked.connect(self.computeNAndPhi)
        # self.ui.pushButton_4.clicked.connect(self.computePhi)
        self.ui.pushButton_18.clicked.connect(self.generateE)
        self.ui.pushButton_5.clicked.connect(self.computeD)
        self.ui.pushButton_10.clicked.connect(self.getKey)
        self.ui.pushButton_21.clicked.connect(self.encrypt)
        self.ui.pushButton_22.clicked.connect(self.decrypt)
        self.ui.pushButton_4.clicked.connect(self.decode)
        self.ui.pushButton_23.clicked.connect(self.encrypt_md5)
        self.ui.pushButton_11.clicked.connect(self.get_e_d)
        self.ui.pushButton_26.clicked.connect(self.sinature)
        self.ui.pushButton_28.clicked.connect(self.designature)
        self.ui.pushButton_27.clicked.connect(self.messageDigest)
        self.ui.pushButton_29.clicked.connect(self.verify)
        ########################################################################
        ## START - WINDOW ATTRIBUTES
        ########################################################################

        ## REMOVE ==> STANDARD TITLE BAR
        UIFunctions.removeTitleBar(True)
        ## ==> END ##

        ## SET ==> WINDOW TITLE
        self.setWindowTitle('Cryptography')
        self.setWindowIcon(QIcon("lock.ico"))
        if sys.platform == "win32":
            import ctypes
            ctypes.windll.shell32.SetCurrentProcessExplicitAppUserModelID("6666")

        UIFunctions.labelTitle(self, 'Cryptography')
        UIFunctions.labelDescription(self, 'Welcome to Cryptography')
        ## ==> END ##

        ## WINDOW SIZE ==> DEFAULT SIZE
        desktop = QtWidgets.QApplication.desktop()
        print(desktop.width(), desktop.height(), desktop)
        self.screenWidth = desktop.width() * 0.65
        self.screenHeight = desktop.height() * 0.7

        startSize = QSize(self.screenWidth, self.screenHeight)
        self.resize(startSize)
        self.setMinimumSize(startSize)
        # UIFunctions.enableMaximumSize(self, 500, 720)
        ## ==> END ##

        ## ==> CREATE MENUS
        ########################################################################

        ## ==> TOGGLE MENU SIZE
        self.ui.btn_toggle_menu.clicked.connect(lambda: UIFunctions.toggleMenu(self, 220, True))
        self.ui.btn_toggle_menu.click()
        ## ==> END ##

        ## ==> ADD CUSTOM MENUS
        ## 在这里添加菜单栏按钮
        self.ui.stackedWidget.setMinimumWidth(20)
        UIFunctions.addNewMenu(self, "HOME", "btn_home", "url(:/16x16/icons/16x16/cil-home.png)", True)
        UIFunctions.addNewMenu(self, "RSA", "btn_rsa", "url(:/16x16/icons/16x16/cil-lock-locked.png)", True)
        UIFunctions.addNewMenu(self, "Signature", "btn_new_signature", "url(:/16x16/icons/16x16/cil-user.png)", True)

        ## ==> END ##

        # START MENU => SELECTION
        UIFunctions.selectStandardMenu(self, "btn_home")
        ## ==> END ##

        ## ==> START PAGE
        self.ui.stackedWidget.setCurrentWidget(self.ui.page_home)
        ## ==> END ##

        ## signature ICON ==> SHOW HIDE

        UIFunctions.userIcon(self, "Cypotography", "url(:/16x16/icons/16x16/cil-lock-locked.png)", True)

        ## ==> END ##

        ## ==> MOVE WINDOW / MAXIMIZE / RESTORE
        ########################################################################
        def moveWindow(event):
            # IF MAXIMIZED CHANGE TO NORMAL
            if UIFunctions.returStatus() == 1:
                UIFunctions.maximize_restore(self)

            # MOVE WINDOW
            if event.buttons() == Qt.LeftButton:
                self.move(self.pos() + event.globalPos() - self.dragPos)
                self.dragPos = event.globalPos()
                event.accept()

        # WIDGET TO MOVE
        self.ui.frame_label_top_btns.mouseMoveEvent = moveWindow
        ## ==> END ##

        ## ==> LOAD DEFINITIONS
        ########################################################################
        UIFunctions.uiDefinitions(self)
        ## ==> END ##

        ########################################################################
        ## END - WINDOW ATTRIBUTES
        ############################## ---/--/--- ##############################

        ########################################################################
        #                                                                      #
        ## START -------------- WIDGETS FUNCTIONS/PARAMETERS ---------------- ##
        #                                                                      #
        ## ==> USER CODES BELLOW                                              ##
        ########################################################################

        ## ==> QTableWidget RARAMETERS
        ########################################################################
        # self.ui.tableWidget.horizontalHeader().setSectionResizeMode(QtWidgets.QHeaderView.Stretch)
        ## ==> END ##

        ########################################################################
        #                                                                      #
        ## END --------------- WIDGETS FUNCTIONS/PARAMETERS ----------------- ##
        #                                                                      #
        ############################## ---/--/--- ##############################

        ## SHOW ==> MAIN WINDOW
        ########################################################################
        self.show()
        ## ==> END ##

    ########################################################################
    ## MENUS ==> DYNAMIC MENUS FUNCTIONS
    #### 在这里添加菜单按钮的操作 显示什么界面...
    ########################################################################
    def Button(self):
        # GET BT CLICKED
        btnWidget = self.sender()
        # PAGE HOME
        if btnWidget.objectName() == "btn_home":
            self.ui.stackedWidget.setCurrentWidget(self.ui.page_home)
            UIFunctions.resetStyle(self, "btn_home")
            UIFunctions.labelPage(self, "Home")
            btnWidget.setStyleSheet(UIFunctions.selectMenu(btnWidget.styleSheet()))

        # PAGE NEW USER
        if btnWidget.objectName() == "btn_new_signature":
            self.ui.stackedWidget.setCurrentWidget(self.ui.page_signature)
            UIFunctions.resetStyle(self, "btn_new_signature")
            UIFunctions.labelPage(self, "Signature")
            btnWidget.setStyleSheet(UIFunctions.selectMenu(btnWidget.styleSheet()))

        if btnWidget.objectName() == "btn_rsa":
            # 菜单rsa 点击出现窗口
            self.ui.stackedWidget.setCurrentWidget(self.ui.page_rsa)
            # style
            UIFunctions.resetStyle(self, "btn_rsa")
            # 右上角显示
            UIFunctions.labelPage(self, "RSA")

            btnWidget.setStyleSheet(UIFunctions.selectMenu(btnWidget.styleSheet()))

        # PAGE WIDGETS
        # if btnWidget.objectName() == "btn_widgets":
        #     self.ui.stackedWidget.setCurrentWidget(self.ui.page_signature)
        #     UIFunctions.resetStyle(self, "btn_widgets")
        #     UIFunctions.labelPage(self, "Custom components")
        #     btnWidget.setStyleSheet(UIFunctions.selectMenu(btnWidget.styleSheet()))

    ## ==> END ##

    def exgcd(self, a, b):
        # 扩展欧几里得算法
        if b == 0:
            return 1, 0
        else:
            x, y = self.exgcd(b, a % b)
            x, y = y, (x - (a // b) * y)
        return x, y

    def generatePrimes(self):

        self.p = gmpy2.mpz_urandomb(self.rs, 1024)  # 随机生成一个0到1024位的素数
        self.q = gmpy2.mpz_urandomb(self.rs, 1024)
        while not gmpy2.is_prime(self.p):  # 判断是否为质数
            self.p = gmpy2.mpz_urandomb(self.rs, 1024)  # 若不是则重新生成
        while not gmpy2.is_prime(self.q):  # 判断是否为质数
            if self.p == self.q:
                self.q = 4
            self.q = gmpy2.mpz_urandomb(self.rs, 1024)  # 若不是则重新生成
        self.ui.lineEdit.setText(str(self.p))

        self.ui.lineEdit_2.setText(str(self.q))

    def encodeM(self):
        m = self.ui.plainTextEdit_8.toPlainText()
        if m != "":
            m1 = mpz(binascii.hexlify(m.encode('utf-8')), 16)
        else:
            m1 = m
            msg_box = QMessageBox(QMessageBox.Critical, 'error', 'input plainText!')
            msg_box.exec_()
            # m = mpz(binascii.hexlify(self.ui.plainTextEdit_8.toPlainText().encode('utf-8')), 16)  # 转为16换进制
            # cipher_text = gmpy2.powmod(m, mpz(self.e), mpz(self.n))
        self.ui.plainTextEdit_8.setPlainText(str(m1))

    def computeNAndPhi(self):
        self.p = self.ui.lineEdit.text()
        self.q = self.ui.lineEdit_2.text()

        if self.p == '' or self.q == '':
            self.n = "input primes p and q"
        elif not gmpy2.is_prime(gmpy2.mpz(self.p)) or not gmpy2.is_prime(gmpy2.mpz(self.q)):
            self.p = int(self.p)
            self.q = int(self.q)
            self.n = "p or q is not a prime"
        else:
            self.p = int(self.p)
            self.q = int(self.q)
            self.n = int(self.ui.lineEdit.text()) * int(self.ui.lineEdit_2.text())

            self.varphi = (self.p - 1) * (self.q - 1)
            self.ui.plainTextEdit_11.setPlainText(str(self.varphi))
        self.ui.plainTextEdit_7.setPlainText(str(self.n))

    # def computePhi(self):
    #     self.p = self.ui.lineEdit.text()
    #     self.q = self.ui.lineEdit_2.text()
    #     if self.p == '' or self.q == '':
    #         self.ui.plainTextEdit_11.setPlainText("请输入质数p,q")
    #     elif not gmpy2.is_prime(gmpy2.mpz(self.p)) or not gmpy2.is_prime(gmpy2.mpz(self.q)):
    #         self.p = int(self.p)
    #         self.q = int(self.q)
    #         self.ui.plainTextEdit_11.setPlainText("您输入的p或q不是质数")
    #     else:
    #         self.p = int(self.p)
    #         self.q = int(self.q)
    #         self.varphi = (self.p - 1) * (self.q - 1)
    #         self.ui.plainTextEdit_11.setPlainText(str(self.varphi))

    def generateE(self):
        self.p = self.ui.lineEdit.text()
        self.q = self.ui.lineEdit_2.text()

        if self.p == '' or self.q == '':
            self.ui.plainTextEdit_31.setPlainText("input primes p and q")
        elif not gmpy2.is_prime(gmpy2.mpz(self.p)) or not gmpy2.is_prime(gmpy2.mpz(self.q)):
            self.p = int(self.p)
            self.q = int(self.q)
            self.ui.plainTextEdit_31.setPlainText("p or q is not a prime")
        elif not self.ui.plainTextEdit_11.toPlainText().isdigit():
            self.ui.plainTextEdit_31.setPlainText("generate Euler functions first")
        else:
            self.p = int(self.p)
            self.q = int(self.q)
            self.e = gmpy2.mpz_random(self.rs, self.varphi)  # 随机生成比欧拉函数小的正整数
            while gmpy2.gcd(self.e, self.varphi) != 1:  # 判断两个数是否互质
                self.e = gmpy2.mpz_random(self.rs, self.varphi)  # 随机生成一个1~phi的,与phi互素的数
            self.ui.plainTextEdit_31.setPlainText(str(self.e))

    def computeD(self):
        self.p = self.ui.lineEdit.text()
        self.q = self.ui.lineEdit_2.text()
        if self.p == '' or self.q == '':
            self.ui.plainTextEdit_29.setPlainText("input primes p and q")
        elif not gmpy2.is_prime(gmpy2.mpz(self.p)) or not gmpy2.is_prime(gmpy2.mpz(self.q)):
            self.p = int(self.p)
            self.q = int(self.q)
            self.ui.plainTextEdit_29.setPlainText("p or q is not a prime")
        elif self.ui.plainTextEdit_31.toPlainText().isdigit():
            self.p = int(self.p)
            self.q = int(self.q)
            d = gmpy2.invert(self.e, self.varphi)
            self.d = d
            self.ui.plainTextEdit_29.setPlainText(str(self.d))
        else:
            self.ui.plainTextEdit_29.setPlainText("generate public exponent e first")
        ########################################################################

    def getKey(self):
        self.ui.plainTextEdit_38.setPlainText("{" + str(self.e) + " , " + str(self.varphi) + "}")
        self.ui.plainTextEdit_39.setPlainText("{" + str(self.d) + " , " + str(self.varphi) + "}")

    def encrypt(self):
        m = self.ui.plainTextEdit_8.toPlainText()
        if not m.isdigit():
            self.ui.plainTextEdit_9.setPlainText("encode plainText first")
        else:
            m = mpz(int(m))
            if self.n > m:
                cipher_text = gmpy2.powmod(m, mpz(self.e), mpz(self.n))
                self.ui.plainTextEdit_9.setPlainText(str(cipher_text))
            else:
                self.ui.plainTextEdit_9.setPlainText("ensure n > encode(plainText)!")

    def decrypt(self):
        m = self.ui.plainTextEdit_9.toPlainText()
        if m.isdigit():
            cipher_text = mpz(int(m))
            m = gmpy2.powmod(cipher_text, mpz(self.d), mpz(self.n))
            # plain_text = binascii.unhexlify(format(m, 'x')).decode('utf-8')
            self.ui.plainTextEdit_10.setPlainText(str(m))
        else:
            self.ui.plainTextEdit_10.setPlainText("encode plainText first")

    def decode(self):
        m = self.ui.plainTextEdit_10.toPlainText()
        if m.isdigit():
            m = mpz(int(m))
            plain_text = binascii.unhexlify(format(m, 'x')).decode('utf-8')
            self.ui.plainTextEdit_13.setPlainText(str(plain_text))
        else:
            self.ui.plainTextEdit_13.setPlainText("encode plainText first")

    def gen_prime(self):
        p = gmpy2.mpz_urandomb(self.rs, 1024)  # 随机生成一个0到1024位的素数
        while not gmpy2.is_prime(p):  # 判断是否为质数
            p = gmpy2.mpz_urandomb(self.rs, 1024)  # 若不是则重新生成
        return p

    def get_e_d(self):
        # 时间钟 为了生成随机数
        self.p = self.gen_prime()
        self.q = self.gen_prime()
        self.n = self.p * self.q
        self.varphi = (self.p - 1) * (self.q - 1)
        self.e = gmpy2.mpz_random(self.rs, self.varphi)  # 随机生成比r小的正整数
        while gmpy2.gcd(self.e, self.varphi) != 1:  # 判断两个数是否互质
            self.e = gmpy2.mpz_random(self.rs, self.varphi)  # 随机生成一个0~phi的,与phi互素的数
        self.d = gmpy2.invert(self.e, self.varphi)
        self.ui.plainTextEdit_41.setPlainText(str(self.e))
        self.ui.plainTextEdit_40.setPlainText(str(self.d))

    def encrypt_md5(self):  # 数字摘要加密
        # 创建md5对象
        new_md5 = md5()
        # 这里必须用encode()函数对字符串进行编码，不然会报 TypeError: Unicode-objects must be encoded before hashing
        s = self.ui.plainTextEdit_12.toPlainText()
        new_md5.update(s.encode(encoding='utf-8'))
        # 加密
        self.ui.plainTextEdit_12.setPlainText(new_md5.hexdigest())

    def sinature(self):
        m = mpz(binascii.hexlify(self.ui.plainTextEdit_12.toPlainText().encode('utf-8')), 16)  # 转为16换进制
        self.cipher_text = gmpy2.powmod(m, self.d, self.n)
        self.ui.plainTextEdit_16.setPlainText(str(self.cipher_text))
        ## START ==> APP EVENTS

    def designature(self):
        m = gmpy2.powmod(self.cipher_text, self.e, self.n)
        plain_text = binascii.unhexlify(format(m, 'x')).decode('utf-8')
        self.ui.plainTextEdit_18.setPlainText(str(plain_text))

    def messageDigest(self):
        message = self.ui.plainTextEdit_17.toPlainText()
        # 创建md5对象
        new_md5 = md5()
        # 这里必须用encode()函数对字符串进行编码，不然会报 TypeError: Unicode-objects must be encoded before hashing

        new_md5.update(message.encode(encoding='utf-8'))
        # 加密
        self.ui.plainTextEdit_17.setPlainText(new_md5.hexdigest())

    def verify(self):
        if self.ui.plainTextEdit_18.toPlainText() == self.ui.plainTextEdit_17.toPlainText():
            self.ui.plainTextEdit_19.setPlainText("Validation succeeded！")
        else:
            self.ui.plainTextEdit_19.setPlainText("The message has been tampered with！")

    ########################################################################

    ## EVENT ==> MOUSE DOUBLE CLICK
    ########################################################################
    def eventFilter(self, watched, event):
        if watched == self.le and event.type() == QtCore.QEvent.MouseButtonDblClick:
            print("pos: ", event.pos())

    ## ==> END ##

    ## EVENT ==> MOUSE CLICK
    ########################################################################
    def mousePressEvent(self, event):
        self.dragPos = event.globalPos()
        # if event.buttons() == Qt.LeftButton:
        #     print('Mouse click: LEFT CLICK')
        # if event.buttons() == Qt.RightButton:
        #     print('Mouse click: RIGHT CLICK')
        # if event.buttons() == Qt.MidButton:
        #     print('Mouse click: MIDDLE BUTTON')
    ## ==> END ##

    ## EVENT ==> KEY PRESSED
    ########################################################################
    # def keyPressEvent(self, event):
    #     print('Key: ' + str(event.key()) + ' | Text Press: ' + str(event.text()))
    ## ==> END ##

    ## EVENT ==> RESIZE EVENT
    ########################################################################
    # def resizeEvent(self, event):
    #     self.resizeFunction()
    #     return super(MainWindow, self).resizeEvent(event)

    # def resizeFunction(self):
    #     print('Height: ' + str(self.height()) + ' | Width: ' + str(self.width()))
    ## ==> END ##

    ########################################################################
    ## END ==> APP EVENTS
    ############################## ---/--/--- ##############################


if __name__ == "__main__":
    app = QApplication(sys.argv)
    QtGui.QFontDatabase.addApplicationFont('fonts/segoeui.ttf')
    QtGui.QFontDatabase.addApplicationFont('fonts/segoeuib.ttf')
    window = MainWindow()
    sys.exit(app.exec_())
