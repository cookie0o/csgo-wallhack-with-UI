from PyQt5 import QtCore, QtGui, QtWidgets
from threading import Thread
import pymem
import pymem.process
import numpy as np
import time

#import offset;
from offsets import *


#main cheat part
def main_cheat(self):
        #get line edit input,

        #T values;
        T_R__ = self.T_Blue_2.text()
        if T_R__ == "0":
                pass
        else:
                try:
                        T_R_ = self.T_Blue_2.text()
                        #convert to float; ?
                        T_R = float(T_R_.replace('','0'))
                except ValueError as err:
                        pass 
        #
        T_G__ = self.T_GREEN_2.text()
        if T_G__ == "0":
                pass
        else:
                try:
                        T_G_ = self.T_GREEN_2.text()
                        #convert to float; ?
                        T_G = float(T_G_.replace('','0'))
                except ValueError as err:
                        pass 
        #
        T_B__ = self.T_Blue.text()
        if T_B__ == "0":
                pass
        else:
                try:
                        T_B_ = self.T_Blue.text()
                        #convert to float; ?
                        T_B = float(T_B_.replace('','0'))
                except ValueError as err:
                        pass 
        

        #CT values;
        CT_R__ = self.CT_RED.text()
        if CT_R__ == "0":
                pass
        else:
                try:
                        CT_R_ = self.CT_RED.text()
                        #convert to float; ?
                        CT_R = float(CT_R_.replace('','0'))
                except ValueError as err:
                        pass 
        #
        CT_G__ = self.CT_GREEN.text()
        if CT_G__ == "0":
                pass
        else:
                try:
                        CT_G_ = self.CT_GREEN.text()
                        #convert to float; ?
                        CT_G = float(CT_G_.replace('','0'))
                except ValueError as err:
                        pass 
        #
        CT_B__ = self.CT_Blue.text()
        if CT_B__  == "0":
                pass
        else:
                try:
                        CT_B_ = self.CT_Blue.text()
                        #convert to float; ?
                        CT_B = float(CT_B_.replace('','0'))
                except ValueError as err:
                        pass 


        #main part ;

        try:
                pm = pymem.Pymem("csgo.exe")
                client = pymem.process.module_from_name(pm.process_handle, "client.dll").lpBaseOfDll
        except pymem.exception.ProcessNotFound:
                print('Launch Game')
        
        pm = pymem.Pymem("csgo.exe")

        while True:
                time.sleep(0.001)

                glow_manager = pm.read_int(client + dwGlowObjectManager)

                for i in range(1, 32):  # Entities 1-32 are reserved for players.
                        entity = pm.read_int(client + dwEntityList + i * 0x10)

                        if entity:
                                entity_team_id = pm.read_int(entity + m_iTeamNum)
                                entity_glow = pm.read_int(entity + m_iGlowIndex)

                                if entity_team_id == 2:  # Terrorist
                                        pm.write_float(glow_manager + entity_glow * 0x38 + 0x8, float(T_R))   # R
                                        pm.write_float(glow_manager + entity_glow * 0x38 + 0xC, float(T_G))   # G
                                        pm.write_float(glow_manager + entity_glow * 0x38 + 0x10, float(T_B))  # B
                                        pm.write_float(glow_manager + entity_glow * 0x38 + 0x14, float(1))    # Alpha
                                        pm.write_int(glow_manager + entity_glow * 0x38 + 0x28, 1)       # Enable glow

                                elif entity_team_id == 3:  # Counter-terrorist
                                        pm.write_float(glow_manager + entity_glow * 0x38 + 0x8, float(CT_R))   # R
                                        pm.write_float(glow_manager + entity_glow * 0x38 + 0xC, float(CT_G))   # G
                                        pm.write_float(glow_manager + entity_glow * 0x38 + 0x10, float(CT_B))  # B
                                        pm.write_float(glow_manager + entity_glow * 0x38 + 0x14, float(1))     # Alpha
                                        pm.write_int(glow_manager + entity_glow * 0x38 + 0x28, 1)         # Enable glow





class Ui_main_window(object):
    def setupUi(self, main_window):
        main_window.setObjectName("main_window")
        main_window.resize(490, 240)
        main_window.setMinimumSize(QtCore.QSize(490, 240))
        main_window.setMaximumSize(QtCore.QSize(490, 240))
        font = QtGui.QFont()
        font.setPointSize(8)
        main_window.setFont(font)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/ico/ico.ico"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        main_window.setWindowIcon(icon)
        self.background = QtWidgets.QLabel(main_window)
        self.background.setGeometry(QtCore.QRect(0, 0, 491, 241))
        self.background.setAutoFillBackground(False)
        self.background.setStyleSheet("background-color: rgb(88, 88, 88);")
        self.background.setText("")
        self.background.setObjectName("background")
        self.title = QtWidgets.QLabel(main_window)
        self.title.setGeometry(QtCore.QRect(0, 0, 491, 61))
        font = QtGui.QFont()
        font.setPointSize(24)
        font.setBold(True)
        font.setWeight(75)
        self.title.setFont(font)
        self.title.setStyleSheet("color: rgb(255, 0, 0);")
        self.title.setAlignment(QtCore.Qt.AlignCenter)
        self.title.setObjectName("title")
        self.link_to_github = QtWidgets.QTextBrowser(main_window)
        self.link_to_github.setGeometry(QtCore.QRect(0, 0, 121, 21))
        self.link_to_github.setStyleSheet("background-color: rgb(52, 52, 52);")
        self.link_to_github.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.link_to_github.setReadOnly(True)
        self.link_to_github.setMarkdown("[cookie0_o on github](https://github.com/cookie0o)\n"
"\n"
"")
        self.link_to_github.setOpenExternalLinks(True)
        self.link_to_github.setObjectName("link_to_github")
        self.CT_title = QtWidgets.QLabel(main_window)
        self.CT_title.setGeometry(QtCore.QRect(0, 60, 241, 51))
        font = QtGui.QFont()
        font.setPointSize(13)
        font.setBold(True)
        font.setWeight(75)
        self.CT_title.setFont(font)
        self.CT_title.setStyleSheet("color: rgb(85, 0, 255);\n"
"background-color: rgb(52, 52, 52);")
        self.CT_title.setAlignment(QtCore.Qt.AlignCenter)
        self.CT_title.setObjectName("CT_title")
        self.T_title = QtWidgets.QLabel(main_window)
        self.T_title.setGeometry(QtCore.QRect(240, 60, 251, 51))
        font = QtGui.QFont()
        font.setPointSize(13)
        font.setBold(True)
        font.setWeight(75)
        self.T_title.setFont(font)
        self.T_title.setStyleSheet("color: rgb(170, 0, 0);\n"
"background-color: rgb(52, 52, 52);")
        self.T_title.setAlignment(QtCore.Qt.AlignCenter)
        self.T_title.setObjectName("T_title")
        self.r_text = QtWidgets.QLabel(main_window)
        self.r_text.setGeometry(QtCore.QRect(0, 110, 71, 41))
        font = QtGui.QFont()
        font.setPointSize(13)
        font.setBold(True)
        font.setWeight(75)
        self.r_text.setFont(font)
        self.r_text.setObjectName("r_text")
        self.g_text = QtWidgets.QLabel(main_window)
        self.g_text.setGeometry(QtCore.QRect(0, 150, 71, 41))
        font = QtGui.QFont()
        font.setPointSize(13)
        font.setBold(True)
        font.setWeight(75)
        self.g_text.setFont(font)
        self.g_text.setObjectName("g_text")
        self.b_text = QtWidgets.QLabel(main_window)
        self.b_text.setGeometry(QtCore.QRect(0, 190, 71, 51))
        font = QtGui.QFont()
        font.setPointSize(13)
        font.setBold(True)
        font.setWeight(75)
        self.b_text.setFont(font)
        self.b_text.setObjectName("b_text")
        self.r_text_T = QtWidgets.QLabel(main_window)
        self.r_text_T.setGeometry(QtCore.QRect(210, 110, 71, 41))
        font = QtGui.QFont()
        font.setPointSize(13)
        font.setBold(True)
        font.setWeight(75)
        self.r_text_T.setFont(font)
        self.r_text_T.setObjectName("r_text_T")
        self.g_text_T = QtWidgets.QLabel(main_window)
        self.g_text_T.setGeometry(QtCore.QRect(210, 160, 71, 21))
        font = QtGui.QFont()
        font.setPointSize(13)
        font.setBold(True)
        font.setWeight(75)
        self.g_text_T.setFont(font)
        self.g_text_T.setObjectName("g_text_T")
        self.b_text_T = QtWidgets.QLabel(main_window)
        self.b_text_T.setGeometry(QtCore.QRect(210, 190, 71, 51))
        font = QtGui.QFont()
        font.setPointSize(13)
        font.setBold(True)
        font.setWeight(75)
        self.b_text_T.setFont(font)
        self.b_text_T.setObjectName("b_text_T")
        self.CT_RED = QtWidgets.QLineEdit(main_window)
        self.CT_RED.setGeometry(QtCore.QRect(70, 120, 91, 31))
        font = QtGui.QFont()
        font.setPointSize(21)
        font.setBold(True)
        font.setWeight(75)
        self.CT_RED.setFont(font)
        self.CT_RED.setStyleSheet("background-color: rgb(52, 52, 52);")
        self.CT_RED.setMaxLength(3)
        self.CT_RED.setAlignment(QtCore.Qt.AlignCenter)
        self.CT_RED.setObjectName("CT_RED")
        self.CT_GREEN = QtWidgets.QLineEdit(main_window)
        self.CT_GREEN.setGeometry(QtCore.QRect(70, 160, 91, 31))
        font = QtGui.QFont()
        font.setPointSize(21)
        font.setBold(True)
        font.setWeight(75)
        self.CT_GREEN.setFont(font)
        self.CT_GREEN.setStyleSheet("background-color: rgb(52, 52, 52);")
        self.CT_GREEN.setMaxLength(3)
        self.CT_GREEN.setAlignment(QtCore.Qt.AlignCenter)
        self.CT_GREEN.setObjectName("CT_GREEN")
        self.CT_Blue = QtWidgets.QLineEdit(main_window)
        self.CT_Blue.setGeometry(QtCore.QRect(70, 200, 91, 31))
        font = QtGui.QFont()
        font.setPointSize(21)
        font.setBold(True)
        font.setWeight(75)
        self.CT_Blue.setFont(font)
        self.CT_Blue.setStyleSheet("background-color: rgb(52, 52, 52);")
        self.CT_Blue.setMaxLength(3)
        self.CT_Blue.setAlignment(QtCore.Qt.AlignCenter)
        self.CT_Blue.setObjectName("CT_Blue")
        self.T_Blue = QtWidgets.QLineEdit(main_window)
        self.T_Blue.setGeometry(QtCore.QRect(280, 200, 91, 31))
        font = QtGui.QFont()
        font.setPointSize(21)
        font.setBold(True)
        font.setWeight(75)
        self.T_Blue.setFont(font)
        self.T_Blue.setStyleSheet("background-color: rgb(52, 52, 52);")
        self.T_Blue.setText("")
        self.T_Blue.setMaxLength(3)
        self.T_Blue.setAlignment(QtCore.Qt.AlignCenter)
        self.T_Blue.setObjectName("T_Blue")
        self.T_Blue_2 = QtWidgets.QLineEdit(main_window)
        self.T_Blue_2.setGeometry(QtCore.QRect(280, 120, 91, 31))
        font = QtGui.QFont()
        font.setPointSize(21)
        font.setBold(True)
        font.setWeight(75)
        self.T_Blue_2.setFont(font)
        self.T_Blue_2.setStyleSheet("background-color: rgb(52, 52, 52);")
        self.T_Blue_2.setMaxLength(3)
        self.T_Blue_2.setAlignment(QtCore.Qt.AlignCenter)
        self.T_Blue_2.setObjectName("T_Blue_2")
        self.T_GREEN_2 = QtWidgets.QLineEdit(main_window)
        self.T_GREEN_2.setGeometry(QtCore.QRect(280, 160, 91, 31))
        font = QtGui.QFont()
        font.setPointSize(21)
        font.setBold(True)
        font.setWeight(75)
        self.T_GREEN_2.setFont(font)
        self.T_GREEN_2.setStyleSheet("background-color: rgb(52, 52, 52);")
        self.T_GREEN_2.setMaxLength(3)
        self.T_GREEN_2.setAlignment(QtCore.Qt.AlignCenter)
        self.T_GREEN_2.setObjectName("T_GREEN_2")
        self.apply_and_inject_button = QtWidgets.QPushButton(main_window)
        self.apply_and_inject_button.setGeometry(QtCore.QRect(380, 200, 101, 31))
        font = QtGui.QFont()
        font.setPointSize(9)
        font.setBold(False)
        font.setWeight(50)
        self.apply_and_inject_button.setFont(font)
        self.apply_and_inject_button.setStyleSheet("background-color: rgb(255, 85, 255);")
        self.apply_and_inject_button.setObjectName("apply_and_inject_button")
        self.background.raise_()
        self.CT_title.raise_()
        self.T_title.raise_()
        self.r_text.raise_()
        self.g_text.raise_()
        self.b_text.raise_()
        self.r_text_T.raise_()
        self.g_text_T.raise_()
        self.b_text_T.raise_()
        self.CT_RED.raise_()
        self.CT_GREEN.raise_()
        self.CT_Blue.raise_()
        self.T_Blue.raise_()
        self.title.raise_()
        self.T_Blue_2.raise_()
        self.T_GREEN_2.raise_()
        self.apply_and_inject_button.raise_()
        self.link_to_github.raise_()

        self.retranslateUi(main_window)
        QtCore.QMetaObject.connectSlotsByName(main_window)

        #button

        #run cheat with settings applied
        self.apply_and_inject_button.clicked.connect(lambda: Thread(target=main_cheat(self)).start())




    def retranslateUi(self, main_window):
        _translate = QtCore.QCoreApplication.translate
        main_window.setWindowTitle(_translate("main_window", "cs:go wall [ by; cookie0_o ]"))
        self.title.setText(_translate("main_window", "cs:go wallhack by; cookie0_o"))
        self.link_to_github.setHtml(_translate("main_window", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:8.25pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><a href=\"https://github.com/cookie0o\"><span style=\" font-size:8pt; text-decoration: underline; color:#00ffff;\">cookie0_o on github</span></a></p></body></html>"))
        self.CT_title.setText(_translate("main_window", "Counter-Terrorists color;"))
        self.T_title.setText(_translate("main_window", "Terrorists color;"))
        self.r_text.setText(_translate("main_window", "R value;"))
        self.g_text.setText(_translate("main_window", "G value;"))
        self.b_text.setText(_translate("main_window", "B value;"))
        self.r_text_T.setText(_translate("main_window", "R value;"))
        self.g_text_T.setText(_translate("main_window", "G value;"))
        self.b_text_T.setText(_translate("main_window", "B value;"))
        self.CT_Blue.setText(_translate("main_window", "1"))
        self.T_Blue_2.setText(_translate("main_window", "1"))
        self.apply_and_inject_button.setText(_translate("main_window", "apply and inject"))
import res.res_rc


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    main_window = QtWidgets.QWidget()
    ui = Ui_main_window()
    ui.setupUi(main_window)
    main_window.show()
    sys.exit(app.exec_())
