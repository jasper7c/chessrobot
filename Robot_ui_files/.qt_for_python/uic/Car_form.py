# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'c:\Users\LZC-solo\Desktop\robot\Robot_ui_files\Car_form.ui'
#
# Created by: PyQt5 UI code generator 5.14.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Car_form(object):
    def setupUi(self, Car_form):
        Car_form.setObjectName("Car_form")
        Car_form.resize(600, 365)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(Car_form.sizePolicy().hasHeightForWidth())
        Car_form.setSizePolicy(sizePolicy)
        Car_form.setMinimumSize(QtCore.QSize(600, 365))
        Car_form.setMaximumSize(QtCore.QSize(810, 365))
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
        Car_form.setPalette(palette)
        font = QtGui.QFont()
        font.setFamily("Arial")
        Car_form.setFont(font)
        self.verticalLayout_7 = QtWidgets.QVBoxLayout(Car_form)
        self.verticalLayout_7.setObjectName("verticalLayout_7")
        self.widget_8 = QtWidgets.QWidget(Car_form)
        self.widget_8.setObjectName("widget_8")
        self.horizontalLayout_7 = QtWidgets.QHBoxLayout(self.widget_8)
        self.horizontalLayout_7.setObjectName("horizontalLayout_7")
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_7.addItem(spacerItem)
        self.win_ico = QtWidgets.QLabel(self.widget_8)
        self.win_ico.setText("")
        self.win_ico.setObjectName("win_ico")
        self.horizontalLayout_7.addWidget(self.win_ico)
        self.label = QtWidgets.QLabel(self.widget_8)
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
        self.horizontalLayout_7.addWidget(self.label)
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_7.addItem(spacerItem1)
        self.verticalLayout_7.addWidget(self.widget_8)
        self.widget_12 = QtWidgets.QWidget(Car_form)
        self.widget_12.setObjectName("widget_12")
        self.horizontalLayout_18 = QtWidgets.QHBoxLayout(self.widget_12)
        self.horizontalLayout_18.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_18.setObjectName("horizontalLayout_18")
        self.widget_4 = QtWidgets.QWidget(self.widget_12)
        self.widget_4.setObjectName("widget_4")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.widget_4)
        self.verticalLayout.setContentsMargins(0, -1, 0, 11)
        self.verticalLayout.setObjectName("verticalLayout")
        self.widget_5 = QtWidgets.QWidget(self.widget_4)
        self.widget_5.setObjectName("widget_5")
        self.verticalLayout_8 = QtWidgets.QVBoxLayout(self.widget_5)
        self.verticalLayout_8.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_8.setObjectName("verticalLayout_8")
        self.widget_17 = QtWidgets.QWidget(self.widget_5)
        self.widget_17.setObjectName("widget_17")
        self.horizontalLayout_11 = QtWidgets.QHBoxLayout(self.widget_17)
        self.horizontalLayout_11.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_11.setObjectName("horizontalLayout_11")
        spacerItem2 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_11.addItem(spacerItem2)
        self.widget_16 = QtWidgets.QWidget(self.widget_17)
        self.widget_16.setObjectName("widget_16")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.widget_16)
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.add_x_butt = QtWidgets.QPushButton(self.widget_16)
        self.add_x_butt.setMinimumSize(QtCore.QSize(50, 50))
        self.add_x_butt.setMaximumSize(QtCore.QSize(50, 50))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(16)
        self.add_x_butt.setFont(font)
        self.add_x_butt.setObjectName("add_x_butt")
        self.verticalLayout_2.addWidget(self.add_x_butt)
        self.del_x_butt = QtWidgets.QPushButton(self.widget_16)
        self.del_x_butt.setMinimumSize(QtCore.QSize(50, 50))
        self.del_x_butt.setMaximumSize(QtCore.QSize(50, 50))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(16)
        self.del_x_butt.setFont(font)
        self.del_x_butt.setObjectName("del_x_butt")
        self.verticalLayout_2.addWidget(self.del_x_butt)
        self.horizontalLayout_11.addWidget(self.widget_16)
        spacerItem3 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_11.addItem(spacerItem3)
        self.verticalLayout_8.addWidget(self.widget_17)
        self.widget_13 = QtWidgets.QWidget(self.widget_5)
        self.widget_13.setObjectName("widget_13")
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout(self.widget_13)
        self.horizontalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.label_5 = QtWidgets.QLabel(self.widget_13)
        self.label_5.setObjectName("label_5")
        self.horizontalLayout_5.addWidget(self.label_5)
        self.step_x = QtWidgets.QDoubleSpinBox(self.widget_13)
        self.step_x.setMinimum(-500.0)
        self.step_x.setMaximum(500.0)
        self.step_x.setSingleStep(0.1)
        self.step_x.setProperty("value", 1.0)
        self.step_x.setObjectName("step_x")
        self.horizontalLayout_5.addWidget(self.step_x)
        self.verticalLayout_8.addWidget(self.widget_13)
        self.verticalLayout.addWidget(self.widget_5)
        self.widget = QtWidgets.QWidget(self.widget_4)
        self.widget.setObjectName("widget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.widget)
        self.horizontalLayout.setContentsMargins(-1, 0, -1, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label_2 = QtWidgets.QLabel(self.widget)
        self.label_2.setObjectName("label_2")
        self.horizontalLayout.addWidget(self.label_2)
        self.X_label = QtWidgets.QLabel(self.widget)
        self.X_label.setText("")
        self.X_label.setObjectName("X_label")
        self.horizontalLayout.addWidget(self.X_label)
        self.verticalLayout.addWidget(self.widget)
        self.horizontalLayout_18.addWidget(self.widget_4)
        self.widget_9 = QtWidgets.QWidget(self.widget_12)
        self.widget_9.setObjectName("widget_9")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout(self.widget_9)
        self.verticalLayout_4.setContentsMargins(0, -1, 0, 11)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.widget_6 = QtWidgets.QWidget(self.widget_9)
        self.widget_6.setObjectName("widget_6")
        self.verticalLayout_9 = QtWidgets.QVBoxLayout(self.widget_6)
        self.verticalLayout_9.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_9.setObjectName("verticalLayout_9")
        self.widget_19 = QtWidgets.QWidget(self.widget_6)
        self.widget_19.setObjectName("widget_19")
        self.horizontalLayout_12 = QtWidgets.QHBoxLayout(self.widget_19)
        self.horizontalLayout_12.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_12.setObjectName("horizontalLayout_12")
        spacerItem4 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_12.addItem(spacerItem4)
        self.widget_18 = QtWidgets.QWidget(self.widget_19)
        self.widget_18.setObjectName("widget_18")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.widget_18)
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.add_y_butt = QtWidgets.QPushButton(self.widget_18)
        self.add_y_butt.setMinimumSize(QtCore.QSize(50, 50))
        self.add_y_butt.setMaximumSize(QtCore.QSize(50, 50))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(16)
        self.add_y_butt.setFont(font)
        self.add_y_butt.setObjectName("add_y_butt")
        self.verticalLayout_3.addWidget(self.add_y_butt)
        self.del_y_butt = QtWidgets.QPushButton(self.widget_18)
        self.del_y_butt.setMinimumSize(QtCore.QSize(50, 50))
        self.del_y_butt.setMaximumSize(QtCore.QSize(50, 50))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(16)
        self.del_y_butt.setFont(font)
        self.del_y_butt.setObjectName("del_y_butt")
        self.verticalLayout_3.addWidget(self.del_y_butt)
        self.horizontalLayout_12.addWidget(self.widget_18)
        spacerItem5 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_12.addItem(spacerItem5)
        self.verticalLayout_9.addWidget(self.widget_19)
        self.widget_14 = QtWidgets.QWidget(self.widget_6)
        self.widget_14.setObjectName("widget_14")
        self.horizontalLayout_8 = QtWidgets.QHBoxLayout(self.widget_14)
        self.horizontalLayout_8.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_8.setObjectName("horizontalLayout_8")
        self.label_6 = QtWidgets.QLabel(self.widget_14)
        self.label_6.setObjectName("label_6")
        self.horizontalLayout_8.addWidget(self.label_6)
        self.step_y = QtWidgets.QDoubleSpinBox(self.widget_14)
        self.step_y.setMinimum(-500.0)
        self.step_y.setMaximum(500.0)
        self.step_y.setSingleStep(0.1)
        self.step_y.setProperty("value", 1.0)
        self.step_y.setObjectName("step_y")
        self.horizontalLayout_8.addWidget(self.step_y)
        self.verticalLayout_9.addWidget(self.widget_14)
        self.verticalLayout_4.addWidget(self.widget_6)
        self.widget_2 = QtWidgets.QWidget(self.widget_9)
        self.widget_2.setObjectName("widget_2")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.widget_2)
        self.horizontalLayout_2.setContentsMargins(-1, 0, -1, 0)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.label_3 = QtWidgets.QLabel(self.widget_2)
        self.label_3.setObjectName("label_3")
        self.horizontalLayout_2.addWidget(self.label_3)
        self.Y_label = QtWidgets.QLabel(self.widget_2)
        self.Y_label.setText("")
        self.Y_label.setObjectName("Y_label")
        self.horizontalLayout_2.addWidget(self.Y_label)
        self.verticalLayout_4.addWidget(self.widget_2)
        self.horizontalLayout_18.addWidget(self.widget_9)
        self.widget_11 = QtWidgets.QWidget(self.widget_12)
        self.widget_11.setObjectName("widget_11")
        self.verticalLayout_6 = QtWidgets.QVBoxLayout(self.widget_11)
        self.verticalLayout_6.setContentsMargins(0, -1, 0, 11)
        self.verticalLayout_6.setObjectName("verticalLayout_6")
        self.widget_10 = QtWidgets.QWidget(self.widget_11)
        self.widget_10.setObjectName("widget_10")
        self.verticalLayout_10 = QtWidgets.QVBoxLayout(self.widget_10)
        self.verticalLayout_10.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_10.setObjectName("verticalLayout_10")
        self.widget_20 = QtWidgets.QWidget(self.widget_10)
        self.widget_20.setObjectName("widget_20")
        self.horizontalLayout_13 = QtWidgets.QHBoxLayout(self.widget_20)
        self.horizontalLayout_13.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_13.setObjectName("horizontalLayout_13")
        spacerItem6 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_13.addItem(spacerItem6)
        self.widget_21 = QtWidgets.QWidget(self.widget_20)
        self.widget_21.setObjectName("widget_21")
        self.verticalLayout_5 = QtWidgets.QVBoxLayout(self.widget_21)
        self.verticalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.add_z_butt = QtWidgets.QPushButton(self.widget_21)
        self.add_z_butt.setMinimumSize(QtCore.QSize(50, 50))
        self.add_z_butt.setMaximumSize(QtCore.QSize(50, 50))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(16)
        self.add_z_butt.setFont(font)
        self.add_z_butt.setObjectName("add_z_butt")
        self.verticalLayout_5.addWidget(self.add_z_butt)
        self.del_z_butt = QtWidgets.QPushButton(self.widget_21)
        self.del_z_butt.setMinimumSize(QtCore.QSize(50, 50))
        self.del_z_butt.setMaximumSize(QtCore.QSize(50, 50))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(16)
        self.del_z_butt.setFont(font)
        self.del_z_butt.setObjectName("del_z_butt")
        self.verticalLayout_5.addWidget(self.del_z_butt)
        self.horizontalLayout_13.addWidget(self.widget_21)
        spacerItem7 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_13.addItem(spacerItem7)
        self.verticalLayout_10.addWidget(self.widget_20)
        self.widget_15 = QtWidgets.QWidget(self.widget_10)
        self.widget_15.setObjectName("widget_15")
        self.horizontalLayout_10 = QtWidgets.QHBoxLayout(self.widget_15)
        self.horizontalLayout_10.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_10.setObjectName("horizontalLayout_10")
        self.label_8 = QtWidgets.QLabel(self.widget_15)
        self.label_8.setObjectName("label_8")
        self.horizontalLayout_10.addWidget(self.label_8)
        self.step_z = QtWidgets.QDoubleSpinBox(self.widget_15)
        self.step_z.setMinimum(0.0)
        self.step_z.setMaximum(500.0)
        self.step_z.setSingleStep(0.1)
        self.step_z.setProperty("value", 1.0)
        self.step_z.setObjectName("step_z")
        self.horizontalLayout_10.addWidget(self.step_z)
        self.verticalLayout_10.addWidget(self.widget_15)
        self.widget_3 = QtWidgets.QWidget(self.widget_10)
        self.widget_3.setObjectName("widget_3")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout(self.widget_3)
        self.horizontalLayout_3.setContentsMargins(-1, 0, -1, 0)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.label_4 = QtWidgets.QLabel(self.widget_3)
        self.label_4.setObjectName("label_4")
        self.horizontalLayout_3.addWidget(self.label_4)
        self.Z_label = QtWidgets.QLabel(self.widget_3)
        self.Z_label.setText("")
        self.Z_label.setObjectName("Z_label")
        self.horizontalLayout_3.addWidget(self.Z_label)
        self.verticalLayout_10.addWidget(self.widget_3)
        self.verticalLayout_6.addWidget(self.widget_10)
        self.horizontalLayout_18.addWidget(self.widget_11)
        self.widget_22 = QtWidgets.QWidget(self.widget_12)
        self.widget_22.setObjectName("widget_22")
        self.verticalLayout_11 = QtWidgets.QVBoxLayout(self.widget_22)
        self.verticalLayout_11.setContentsMargins(0, -1, 0, 11)
        self.verticalLayout_11.setObjectName("verticalLayout_11")
        self.widget_23 = QtWidgets.QWidget(self.widget_22)
        self.widget_23.setObjectName("widget_23")
        self.verticalLayout_12 = QtWidgets.QVBoxLayout(self.widget_23)
        self.verticalLayout_12.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_12.setObjectName("verticalLayout_12")
        self.widget_24 = QtWidgets.QWidget(self.widget_23)
        self.widget_24.setObjectName("widget_24")
        self.horizontalLayout_14 = QtWidgets.QHBoxLayout(self.widget_24)
        self.horizontalLayout_14.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_14.setObjectName("horizontalLayout_14")
        spacerItem8 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_14.addItem(spacerItem8)
        self.widget_25 = QtWidgets.QWidget(self.widget_24)
        self.widget_25.setObjectName("widget_25")
        self.verticalLayout_13 = QtWidgets.QVBoxLayout(self.widget_25)
        self.verticalLayout_13.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_13.setObjectName("verticalLayout_13")
        self.add_p_butt = QtWidgets.QPushButton(self.widget_25)
        self.add_p_butt.setMinimumSize(QtCore.QSize(50, 50))
        self.add_p_butt.setMaximumSize(QtCore.QSize(50, 50))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(16)
        self.add_p_butt.setFont(font)
        self.add_p_butt.setObjectName("add_p_butt")
        self.verticalLayout_13.addWidget(self.add_p_butt)
        self.del_p_butt = QtWidgets.QPushButton(self.widget_25)
        self.del_p_butt.setMinimumSize(QtCore.QSize(50, 50))
        self.del_p_butt.setMaximumSize(QtCore.QSize(50, 50))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(16)
        self.del_p_butt.setFont(font)
        self.del_p_butt.setObjectName("del_p_butt")
        self.verticalLayout_13.addWidget(self.del_p_butt)
        self.horizontalLayout_14.addWidget(self.widget_25)
        spacerItem9 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_14.addItem(spacerItem9)
        self.verticalLayout_12.addWidget(self.widget_24)
        self.widget_26 = QtWidgets.QWidget(self.widget_23)
        self.widget_26.setObjectName("widget_26")
        self.horizontalLayout_15 = QtWidgets.QHBoxLayout(self.widget_26)
        self.horizontalLayout_15.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_15.setObjectName("horizontalLayout_15")
        self.label_9 = QtWidgets.QLabel(self.widget_26)
        self.label_9.setObjectName("label_9")
        self.horizontalLayout_15.addWidget(self.label_9)
        self.step_p = QtWidgets.QDoubleSpinBox(self.widget_26)
        self.step_p.setMinimum(0.0)
        self.step_p.setMaximum(500.0)
        self.step_p.setSingleStep(0.1)
        self.step_p.setProperty("value", 1.0)
        self.step_p.setObjectName("step_p")
        self.horizontalLayout_15.addWidget(self.step_p)
        self.verticalLayout_12.addWidget(self.widget_26)
        self.widget_27 = QtWidgets.QWidget(self.widget_23)
        self.widget_27.setObjectName("widget_27")
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout(self.widget_27)
        self.horizontalLayout_4.setContentsMargins(-1, 0, -1, 0)
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.label_7 = QtWidgets.QLabel(self.widget_27)
        self.label_7.setObjectName("label_7")
        self.horizontalLayout_4.addWidget(self.label_7)
        self.P_label = QtWidgets.QLabel(self.widget_27)
        self.P_label.setText("")
        self.P_label.setObjectName("P_label")
        self.horizontalLayout_4.addWidget(self.P_label)
        self.verticalLayout_12.addWidget(self.widget_27)
        self.verticalLayout_11.addWidget(self.widget_23)
        self.horizontalLayout_18.addWidget(self.widget_22)
        self.widget_28 = QtWidgets.QWidget(self.widget_12)
        self.widget_28.setObjectName("widget_28")
        self.verticalLayout_14 = QtWidgets.QVBoxLayout(self.widget_28)
        self.verticalLayout_14.setContentsMargins(0, -1, 0, 11)
        self.verticalLayout_14.setObjectName("verticalLayout_14")
        self.widget_29 = QtWidgets.QWidget(self.widget_28)
        self.widget_29.setObjectName("widget_29")
        self.verticalLayout_15 = QtWidgets.QVBoxLayout(self.widget_29)
        self.verticalLayout_15.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_15.setObjectName("verticalLayout_15")
        self.widget_30 = QtWidgets.QWidget(self.widget_29)
        self.widget_30.setObjectName("widget_30")
        self.horizontalLayout_16 = QtWidgets.QHBoxLayout(self.widget_30)
        self.horizontalLayout_16.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_16.setObjectName("horizontalLayout_16")
        spacerItem10 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_16.addItem(spacerItem10)
        self.widget_31 = QtWidgets.QWidget(self.widget_30)
        self.widget_31.setObjectName("widget_31")
        self.verticalLayout_16 = QtWidgets.QVBoxLayout(self.widget_31)
        self.verticalLayout_16.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_16.setObjectName("verticalLayout_16")
        self.add_r_butt = QtWidgets.QPushButton(self.widget_31)
        self.add_r_butt.setMinimumSize(QtCore.QSize(50, 50))
        self.add_r_butt.setMaximumSize(QtCore.QSize(50, 50))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(16)
        self.add_r_butt.setFont(font)
        self.add_r_butt.setObjectName("add_r_butt")
        self.verticalLayout_16.addWidget(self.add_r_butt)
        self.del_r_butt = QtWidgets.QPushButton(self.widget_31)
        self.del_r_butt.setMinimumSize(QtCore.QSize(50, 50))
        self.del_r_butt.setMaximumSize(QtCore.QSize(50, 50))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(16)
        self.del_r_butt.setFont(font)
        self.del_r_butt.setObjectName("del_r_butt")
        self.verticalLayout_16.addWidget(self.del_r_butt)
        self.horizontalLayout_16.addWidget(self.widget_31)
        spacerItem11 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_16.addItem(spacerItem11)
        self.verticalLayout_15.addWidget(self.widget_30)
        self.widget_32 = QtWidgets.QWidget(self.widget_29)
        self.widget_32.setObjectName("widget_32")
        self.horizontalLayout_17 = QtWidgets.QHBoxLayout(self.widget_32)
        self.horizontalLayout_17.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_17.setObjectName("horizontalLayout_17")
        self.label_10 = QtWidgets.QLabel(self.widget_32)
        self.label_10.setObjectName("label_10")
        self.horizontalLayout_17.addWidget(self.label_10)
        self.step_r = QtWidgets.QDoubleSpinBox(self.widget_32)
        self.step_r.setMinimum(0.0)
        self.step_r.setMaximum(500.0)
        self.step_r.setSingleStep(0.1)
        self.step_r.setProperty("value", 1.0)
        self.step_r.setObjectName("step_r")
        self.horizontalLayout_17.addWidget(self.step_r)
        self.verticalLayout_15.addWidget(self.widget_32)
        self.widget_33 = QtWidgets.QWidget(self.widget_29)
        self.widget_33.setObjectName("widget_33")
        self.horizontalLayout_9 = QtWidgets.QHBoxLayout(self.widget_33)
        self.horizontalLayout_9.setContentsMargins(-1, 0, -1, 0)
        self.horizontalLayout_9.setObjectName("horizontalLayout_9")
        self.label_11 = QtWidgets.QLabel(self.widget_33)
        self.label_11.setObjectName("label_11")
        self.horizontalLayout_9.addWidget(self.label_11)
        self.R_label = QtWidgets.QLabel(self.widget_33)
        self.R_label.setText("")
        self.R_label.setObjectName("R_label")
        self.horizontalLayout_9.addWidget(self.R_label)
        self.verticalLayout_15.addWidget(self.widget_33)
        self.verticalLayout_14.addWidget(self.widget_29)
        self.horizontalLayout_18.addWidget(self.widget_28)
        self.verticalLayout_7.addWidget(self.widget_12)
        self.widget_7 = QtWidgets.QWidget(Car_form)
        self.widget_7.setMinimumSize(QtCore.QSize(0, 50))
        self.widget_7.setMaximumSize(QtCore.QSize(16777215, 50))
        self.widget_7.setObjectName("widget_7")
        self.horizontalLayout_6 = QtWidgets.QHBoxLayout(self.widget_7)
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        spacerItem12 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_6.addItem(spacerItem12)
        self.exit_butt = QtWidgets.QPushButton(self.widget_7)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        font.setStyleStrategy(QtGui.QFont.PreferAntialias)
        self.exit_butt.setFont(font)
        self.exit_butt.setObjectName("exit_butt")
        self.horizontalLayout_6.addWidget(self.exit_butt)
        self.verticalLayout_7.addWidget(self.widget_7)

        self.retranslateUi(Car_form)
        QtCore.QMetaObject.connectSlotsByName(Car_form)

    def retranslateUi(self, Car_form):
        _translate = QtCore.QCoreApplication.translate
        Car_form.setWindowTitle(_translate("Car_form", "笛卡尔空间示教器"))
        self.label.setText(_translate("Car_form", "调节末端位置"))
        self.add_x_butt.setText(_translate("Car_form", "+X"))
        self.del_x_butt.setText(_translate("Car_form", "-X"))
        self.label_5.setText(_translate("Car_form", "步长："))
        self.label_2.setText(_translate("Car_form", "X:"))
        self.add_y_butt.setText(_translate("Car_form", "+Y"))
        self.del_y_butt.setText(_translate("Car_form", "-Y"))
        self.label_6.setText(_translate("Car_form", "步长："))
        self.label_3.setText(_translate("Car_form", "Y:"))
        self.add_z_butt.setText(_translate("Car_form", "+Z"))
        self.del_z_butt.setText(_translate("Car_form", "-Z"))
        self.label_8.setText(_translate("Car_form", "步长："))
        self.label_4.setText(_translate("Car_form", "Z:"))
        self.add_p_butt.setText(_translate("Car_form", "+P"))
        self.del_p_butt.setText(_translate("Car_form", "-P"))
        self.label_9.setText(_translate("Car_form", "步长："))
        self.label_7.setText(_translate("Car_form", "P:"))
        self.add_r_butt.setText(_translate("Car_form", "+R"))
        self.del_r_butt.setText(_translate("Car_form", "-R"))
        self.label_10.setText(_translate("Car_form", "步长："))
        self.label_11.setText(_translate("Car_form", "R:"))
        self.exit_butt.setText(_translate("Car_form", "退出"))
