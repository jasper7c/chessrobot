# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'c:\Users\LZC-solo\Desktop\qt_view\Robot_ui_files\Robot_sim_par.ui'
#
# Created by: PyQt5 UI code generator 5.14.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_par_form(object):
    def setupUi(self, par_form):
        par_form.setObjectName("par_form")
        par_form.resize(550, 365)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(par_form.sizePolicy().hasHeightForWidth())
        par_form.setSizePolicy(sizePolicy)
        par_form.setMinimumSize(QtCore.QSize(550, 365))
        par_form.setMaximumSize(QtCore.QSize(550, 365))
        par_form.setSizeIncrement(QtCore.QSize(560, 365))
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
        par_form.setPalette(palette)
        font = QtGui.QFont()
        font.setStyleStrategy(QtGui.QFont.PreferAntialias)
        par_form.setFont(font)
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(par_form)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.label = QtWidgets.QLabel(par_form)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(15)
        font.setBold(True)
        font.setItalic(False)
        font.setUnderline(False)
        font.setWeight(75)
        font.setStyleStrategy(QtGui.QFont.PreferAntialias)
        self.label.setFont(font)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.verticalLayout_2.addWidget(self.label)
        self.widget_4 = QtWidgets.QWidget(par_form)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setStyleStrategy(QtGui.QFont.PreferAntialias)
        self.widget_4.setFont(font)
        self.widget_4.setObjectName("widget_4")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.widget_4)
        self.verticalLayout.setContentsMargins(-1, 0, -1, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.widget_2 = QtWidgets.QWidget(self.widget_4)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setStyleStrategy(QtGui.QFont.PreferAntialias)
        self.widget_2.setFont(font)
        self.widget_2.setObjectName("widget_2")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.widget_2)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label_2 = QtWidgets.QLabel(self.widget_2)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        font.setStyleStrategy(QtGui.QFont.PreferAntialias)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.horizontalLayout.addWidget(self.label_2)
        self.slide_1 = QtWidgets.QSlider(self.widget_2)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setStyleStrategy(QtGui.QFont.PreferAntialias)
        self.slide_1.setFont(font)
        self.slide_1.setMinimum(-1800)
        self.slide_1.setMaximum(1800)
        self.slide_1.setPageStep(1)
        self.slide_1.setOrientation(QtCore.Qt.Horizontal)
        self.slide_1.setObjectName("slide_1")
        self.horizontalLayout.addWidget(self.slide_1)
        self.slide_v_1 = QtWidgets.QDoubleSpinBox(self.widget_2)
        self.slide_v_1.setDecimals(1)
        self.slide_v_1.setMinimum(-180.0)
        self.slide_v_1.setMaximum(180.0)
        self.slide_v_1.setSingleStep(0.1)
        self.slide_v_1.setStepType(QtWidgets.QAbstractSpinBox.DefaultStepType)
        self.slide_v_1.setObjectName("slide_v_1")
        self.horizontalLayout.addWidget(self.slide_v_1)
        self.verticalLayout.addWidget(self.widget_2)
        self.widget_3 = QtWidgets.QWidget(self.widget_4)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setStyleStrategy(QtGui.QFont.PreferAntialias)
        self.widget_3.setFont(font)
        self.widget_3.setObjectName("widget_3")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.widget_3)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.label_3 = QtWidgets.QLabel(self.widget_3)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        font.setStyleStrategy(QtGui.QFont.PreferAntialias)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.horizontalLayout_2.addWidget(self.label_3)
        self.slide_2 = QtWidgets.QSlider(self.widget_3)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setStyleStrategy(QtGui.QFont.PreferAntialias)
        self.slide_2.setFont(font)
        self.slide_2.setMinimum(-1350)
        self.slide_2.setMaximum(1350)
        self.slide_2.setOrientation(QtCore.Qt.Horizontal)
        self.slide_2.setObjectName("slide_2")
        self.horizontalLayout_2.addWidget(self.slide_2)
        self.slide_v_2 = QtWidgets.QDoubleSpinBox(self.widget_3)
        self.slide_v_2.setDecimals(1)
        self.slide_v_2.setMinimum(-135.0)
        self.slide_v_2.setMaximum(135.0)
        self.slide_v_2.setSingleStep(0.1)
        self.slide_v_2.setObjectName("slide_v_2")
        self.horizontalLayout_2.addWidget(self.slide_v_2)
        self.verticalLayout.addWidget(self.widget_3)
        self.widget_5 = QtWidgets.QWidget(self.widget_4)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setStyleStrategy(QtGui.QFont.PreferAntialias)
        self.widget_5.setFont(font)
        self.widget_5.setObjectName("widget_5")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout(self.widget_5)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.label_4 = QtWidgets.QLabel(self.widget_5)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        font.setStyleStrategy(QtGui.QFont.PreferAntialias)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")
        self.horizontalLayout_3.addWidget(self.label_4)
        self.slide_3 = QtWidgets.QSlider(self.widget_5)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setStyleStrategy(QtGui.QFont.PreferAntialias)
        self.slide_3.setFont(font)
        self.slide_3.setMinimum(-1350)
        self.slide_3.setMaximum(1350)
        self.slide_3.setOrientation(QtCore.Qt.Horizontal)
        self.slide_3.setObjectName("slide_3")
        self.horizontalLayout_3.addWidget(self.slide_3)
        self.slide_v_3 = QtWidgets.QDoubleSpinBox(self.widget_5)
        self.slide_v_3.setDecimals(1)
        self.slide_v_3.setMinimum(-135.0)
        self.slide_v_3.setMaximum(135.0)
        self.slide_v_3.setSingleStep(0.1)
        self.slide_v_3.setObjectName("slide_v_3")
        self.horizontalLayout_3.addWidget(self.slide_v_3)
        self.verticalLayout.addWidget(self.widget_5)
        self.widget_6 = QtWidgets.QWidget(self.widget_4)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setStyleStrategy(QtGui.QFont.PreferAntialias)
        self.widget_6.setFont(font)
        self.widget_6.setObjectName("widget_6")
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout(self.widget_6)
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.label_5 = QtWidgets.QLabel(self.widget_6)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        font.setStyleStrategy(QtGui.QFont.PreferAntialias)
        self.label_5.setFont(font)
        self.label_5.setObjectName("label_5")
        self.horizontalLayout_4.addWidget(self.label_5)
        self.slide_4 = QtWidgets.QSlider(self.widget_6)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setStyleStrategy(QtGui.QFont.PreferAntialias)
        self.slide_4.setFont(font)
        self.slide_4.setMinimum(-1350)
        self.slide_4.setMaximum(1350)
        self.slide_4.setOrientation(QtCore.Qt.Horizontal)
        self.slide_4.setObjectName("slide_4")
        self.horizontalLayout_4.addWidget(self.slide_4)
        self.slide_v_4 = QtWidgets.QDoubleSpinBox(self.widget_6)
        self.slide_v_4.setDecimals(1)
        self.slide_v_4.setMinimum(-135.0)
        self.slide_v_4.setMaximum(135.0)
        self.slide_v_4.setSingleStep(0.1)
        self.slide_v_4.setObjectName("slide_v_4")
        self.horizontalLayout_4.addWidget(self.slide_v_4)
        self.verticalLayout.addWidget(self.widget_6)
        self.widget = QtWidgets.QWidget(self.widget_4)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setStyleStrategy(QtGui.QFont.PreferAntialias)
        self.widget.setFont(font)
        self.widget.setObjectName("widget")
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout(self.widget)
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.label_6 = QtWidgets.QLabel(self.widget)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        font.setStyleStrategy(QtGui.QFont.PreferAntialias)
        self.label_6.setFont(font)
        self.label_6.setObjectName("label_6")
        self.horizontalLayout_5.addWidget(self.label_6)
        self.slide_5 = QtWidgets.QSlider(self.widget)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setStyleStrategy(QtGui.QFont.PreferAntialias)
        self.slide_5.setFont(font)
        self.slide_5.setMinimum(-1800)
        self.slide_5.setMaximum(1800)
        self.slide_5.setSingleStep(0)
        self.slide_5.setPageStep(0)
        self.slide_5.setOrientation(QtCore.Qt.Horizontal)
        self.slide_5.setObjectName("slide_5")
        self.horizontalLayout_5.addWidget(self.slide_5)
        self.slide_v_5 = QtWidgets.QDoubleSpinBox(self.widget)
        self.slide_v_5.setDecimals(1)
        self.slide_v_5.setMinimum(-180.0)
        self.slide_v_5.setMaximum(180.0)
        self.slide_v_5.setSingleStep(0.1)
        self.slide_v_5.setObjectName("slide_v_5")
        self.horizontalLayout_5.addWidget(self.slide_v_5)
        self.verticalLayout.addWidget(self.widget)
        self.widget_7 = QtWidgets.QWidget(self.widget_4)
        self.widget_7.setObjectName("widget_7")
        self.horizontalLayout_6 = QtWidgets.QHBoxLayout(self.widget_7)
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_6.addItem(spacerItem)
        self.reset_butt = QtWidgets.QPushButton(self.widget_7)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        font.setStyleStrategy(QtGui.QFont.PreferAntialias)
        self.reset_butt.setFont(font)
        self.reset_butt.setObjectName("reset_butt")
        self.horizontalLayout_6.addWidget(self.reset_butt)
        self.exit_butt = QtWidgets.QPushButton(self.widget_7)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        font.setStyleStrategy(QtGui.QFont.PreferAntialias)
        self.exit_butt.setFont(font)
        self.exit_butt.setObjectName("exit_butt")
        self.horizontalLayout_6.addWidget(self.exit_butt)
        self.verticalLayout.addWidget(self.widget_7)
        self.verticalLayout_2.addWidget(self.widget_4)

        self.retranslateUi(par_form)
        QtCore.QMetaObject.connectSlotsByName(par_form)

    def retranslateUi(self, par_form):
        _translate = QtCore.QCoreApplication.translate
        par_form.setWindowTitle(_translate("par_form", "关节空间示教器"))
        self.label.setText(_translate("par_form", "调节关节角度"))
        self.label_2.setText(_translate("par_form", "关节一："))
        self.label_3.setText(_translate("par_form", "关节二："))
        self.label_4.setText(_translate("par_form", "关节三："))
        self.label_5.setText(_translate("par_form", "关节四："))
        self.label_6.setText(_translate("par_form", "关节五："))
        self.reset_butt.setText(_translate("par_form", "复位"))
        self.exit_butt.setText(_translate("par_form", "退出"))
