from Ui_Login import *
from Ui_MainWindow import *
from PyQt5.QtWidgets import QApplication,QMainWindow
import sys
from PyQt5 import QtCore

user_now = '' #保存当前登录用户名

class LoginWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_LoginWindow()
        self.ui.setupUi(self)#设置信号槽
        #将操作框隐藏
        self.setWindowFlag(QtCore.Qt.FramelessWindowHint)
        self.setAttribute(QtCore.Qt.WA_TranslucentBackground)
        #实现点击页面切换
        self.ui.pushButton_Login.clicked.connect(lambda:self.ui.stackedWidget_2.setCurrentIndex(0))
        self.ui.pushButton_Register.clicked.connect(lambda:self.ui.stackedWidget_2.setCurrentIndex(1))
        #登录
        self.ui.pushButton_L_confirm.clicked.connect(self.login_in)
        #注册
        self.ui.pushButton_R_confirm.clicked.connect(self.register)
        self.show()

    #//登录函数，需要连接数据库检查账号密码///需要修改///
    def login_in(self):
        account = self.ui.lineEdit_L_account.text()
        password = self.ui.lineEdit_L_password.text()

        if account == 'july' and password == '123':
            global user_now
            user_now = account
            #print(user_now)
            self.win = MainWindow()#账号密码正确则跳转到主页面
            self.close()
        elif len(account)==0 or len(password)==0:
            self.ui.stackedWidget.setCurrentIndex(1)
        else:
            self.ui.stackedWidget.setCurrentIndex(2)

    #//注册函数，需要将输入数据传入
    def register(self):
        new_account = self.ui.lineEdit_R_account.text()
        new_password = self.ui.lineEdit_R_password.text()

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)#设置信号槽
        #将操作框隐藏
        self.setWindowFlag(QtCore.Qt.FramelessWindowHint)
        self.setAttribute(QtCore.Qt.WA_TranslucentBackground)
        #点击页面响应
        self.ui.pushButton_home.clicked.connect(lambda:self.ui.stackedWidget_body.setCurrentIndex(0))
        self.ui.pushButton_help.clicked.connect(lambda:self.ui.stackedWidget_body.setCurrentIndex(1))
        self.ui.pushButton_chat.clicked.connect(lambda:self.ui.stackedWidget_body.setCurrentIndex(2))
        self.ui.pushButton_news.clicked.connect(lambda:self.ui.stackedWidget_body.setCurrentIndex(3))
        self.show()


if __name__ =='__main__':
    QtCore.QCoreApplication.setAttribute(QtCore.Qt.AA_EnableHighDpiScaling)
    app = QApplication(sys.argv)
    win = LoginWindow()
    sys.exit(app.exec_())