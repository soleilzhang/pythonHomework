# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'register.ui'
#
# Created by: PyQt5 UI code generator 5.15.1
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_registerPeople(object):
    def setupUi(self, registerPeople):
        registerPeople.setObjectName("registerPeople")
        registerPeople.resize(436, 422)
        font = QtGui.QFont()
        font.setPointSize(16)
        registerPeople.setFont(font)
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(registerPeople)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label = QtWidgets.QLabel(registerPeople)
        self.label.setObjectName("label")
        self.horizontalLayout.addWidget(self.label)
        self.line_id = QtWidgets.QLineEdit(registerPeople)
        self.line_id.setObjectName("line_id")
        self.horizontalLayout.addWidget(self.line_id)
        self.verticalLayout.addLayout(self.horizontalLayout)
        spacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.label_2 = QtWidgets.QLabel(registerPeople)
        self.label_2.setObjectName("label_2")
        self.horizontalLayout_2.addWidget(self.label_2)
        self.line_name = QtWidgets.QLineEdit(registerPeople)
        self.line_name.setObjectName("line_name")
        self.horizontalLayout_2.addWidget(self.line_name)
        self.verticalLayout.addLayout(self.horizontalLayout_2)
        spacerItem1 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem1)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.label_3 = QtWidgets.QLabel(registerPeople)
        self.label_3.setObjectName("label_3")
        self.horizontalLayout_3.addWidget(self.label_3)
        self.line_phone = QtWidgets.QLineEdit(registerPeople)
        self.line_phone.setObjectName("line_phone")
        self.horizontalLayout_3.addWidget(self.line_phone)
        self.verticalLayout.addLayout(self.horizontalLayout_3)
        spacerItem2 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem2)
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.label_4 = QtWidgets.QLabel(registerPeople)
        self.label_4.setObjectName("label_4")
        self.horizontalLayout_4.addWidget(self.label_4)
        self.line_password = QtWidgets.QLineEdit(registerPeople)
        self.line_password.setObjectName("line_password")
        self.horizontalLayout_4.addWidget(self.line_password)
        self.verticalLayout.addLayout(self.horizontalLayout_4)
        spacerItem3 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem3)
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        spacerItem4 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_5.addItem(spacerItem4)
        self.btn_register = QtWidgets.QPushButton(registerPeople)
        self.btn_register.setObjectName("btn_register")
        self.horizontalLayout_5.addWidget(self.btn_register)
        spacerItem5 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_5.addItem(spacerItem5)
        self.verticalLayout.addLayout(self.horizontalLayout_5)
        self.verticalLayout.setStretch(0, 1)
        self.verticalLayout.setStretch(2, 1)
        self.verticalLayout.setStretch(4, 1)
        self.verticalLayout.setStretch(6, 1)
        self.verticalLayout.setStretch(8, 1)
        self.verticalLayout_2.addLayout(self.verticalLayout)
        spacerItem6 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_2.addItem(spacerItem6)

        self.retranslateUi(registerPeople)
        QtCore.QMetaObject.connectSlotsByName(registerPeople)

    def retranslateUi(self, registerPeople):
        _translate = QtCore.QCoreApplication.translate
        registerPeople.setWindowTitle(_translate("registerPeople", "注册管理员"))
        self.label.setText(_translate("registerPeople", "工号："))
        self.label_2.setText(_translate("registerPeople", "姓名："))
        self.label_3.setText(_translate("registerPeople", "电话："))
        self.label_4.setText(_translate("registerPeople", "密码："))
        self.btn_register.setText(_translate("registerPeople", "注册"))
