# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'd:\wsd\my_code\database\Warning.ui'
#
# Created by: PyQt5 UI code generator 5.14.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_warning_form(object):
    def setupUi(self, warning_form):
        warning_form.setObjectName("warning_form")
        warning_form.resize(300, 150)
        warning_form.setMinimumSize(QtCore.QSize(300, 150))
        warning_form.setMaximumSize(QtCore.QSize(300, 150))
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Window, brush)
        warning_form.setPalette(palette)
        font = QtGui.QFont()
        font.setFamily("Agency FB")
        font.setStyleStrategy(QtGui.QFont.PreferAntialias)
        warning_form.setFont(font)
        warning_form.setAcceptDrops(False)
        self.verticalLayout = QtWidgets.QVBoxLayout(warning_form)
        self.verticalLayout.setObjectName("verticalLayout")
        self.widget = QtWidgets.QWidget(warning_form)
        font = QtGui.QFont()
        font.setFamily("宋体")
        font.setStyleStrategy(QtGui.QFont.PreferAntialias)
        self.widget.setFont(font)
        self.widget.setObjectName("widget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.widget)
        self.horizontalLayout.setContentsMargins(-1, -1, 2, -1)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.waning_ico = QtWidgets.QLabel(self.widget)
        self.waning_ico.setMaximumSize(QtCore.QSize(50, 16777215))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setStyleStrategy(QtGui.QFont.PreferAntialias)
        self.waning_ico.setFont(font)
        self.waning_ico.setText("")
        self.waning_ico.setObjectName("waning_ico")
        self.horizontalLayout.addWidget(self.waning_ico)
        self.warning_tip = QtWidgets.QLabel(self.widget)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setStyleStrategy(QtGui.QFont.PreferAntialias)
        self.warning_tip.setFont(font)
        self.warning_tip.setText("")
        self.warning_tip.setWordWrap(True)
        self.warning_tip.setObjectName("warning_tip")
        self.horizontalLayout.addWidget(self.warning_tip)
        self.verticalLayout.addWidget(self.widget)
        self.widget_2 = QtWidgets.QWidget(warning_form)
        self.widget_2.setMaximumSize(QtCore.QSize(16777215, 40))
        self.widget_2.setObjectName("widget_2")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.widget_2)
        self.horizontalLayout_2.setContentsMargins(-1, 5, -1, 5)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem)
        self.confirm_butt = QtWidgets.QPushButton(self.widget_2)
        self.confirm_butt.setMaximumSize(QtCore.QSize(60, 16777215))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setStyleStrategy(QtGui.QFont.PreferAntialias)
        self.confirm_butt.setFont(font)
        self.confirm_butt.setIconSize(QtCore.QSize(15, 20))
        self.confirm_butt.setObjectName("confirm_butt")
        self.horizontalLayout_2.addWidget(self.confirm_butt)
        self.cancel_butt = QtWidgets.QPushButton(self.widget_2)
        self.cancel_butt.setMinimumSize(QtCore.QSize(60, 0))
        self.cancel_butt.setMaximumSize(QtCore.QSize(60, 16777215))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setStyleStrategy(QtGui.QFont.PreferAntialias)
        self.cancel_butt.setFont(font)
        self.cancel_butt.setObjectName("cancel_butt")
        self.horizontalLayout_2.addWidget(self.cancel_butt)
        self.verticalLayout.addWidget(self.widget_2)

        self.retranslateUi(warning_form)
        QtCore.QMetaObject.connectSlotsByName(warning_form)

    def retranslateUi(self, warning_form):
        _translate = QtCore.QCoreApplication.translate
        warning_form.setWindowTitle(_translate("warning_form", "警告"))
        self.confirm_butt.setText(_translate("warning_form", "确认"))
        self.cancel_butt.setText(_translate("warning_form", "取消"))