# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Qt_designer_courseDB_copy.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
from back_end import *

class Ui_MainWindow(object):
    db=newDatabase()
    cursor=db.cursor()

    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1172, 553)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.centralwidget)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.textBrowser = QtWidgets.QTextBrowser(self.centralwidget)
        self.textBrowser.setMaximumSize(QtCore.QSize(350, 16777215))
        self.textBrowser.setObjectName("textBrowser")
        self.horizontalLayout.addWidget(self.textBrowser)
        self.verticalScrollBar = QtWidgets.QScrollBar(self.centralwidget)
        self.verticalScrollBar.setOrientation(QtCore.Qt.Vertical)
        self.verticalScrollBar.setObjectName("verticalScrollBar")
        self.horizontalLayout.addWidget(self.verticalScrollBar)
        spacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.horizontalLayout.addItem(spacerItem)
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.personContainerTitle = QtWidgets.QLabel(self.centralwidget)
        self.personContainerTitle.setAlignment(QtCore.Qt.AlignCenter)
        self.personContainerTitle.setObjectName("personContainerTitle")
        self.verticalLayout_2.addWidget(self.personContainerTitle)
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.verticalLayout_2.addItem(spacerItem1)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.studentRadioButton = QtWidgets.QRadioButton(self.centralwidget)
        self.studentRadioButton.setMaximumSize(QtCore.QSize(100, 100))
        self.studentRadioButton.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.studentRadioButton.setObjectName("studentRadioButton")

        self.horizontalLayout_3.addWidget(self.studentRadioButton)
        self.teacherRadioButton = QtWidgets.QRadioButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.teacherRadioButton.sizePolicy().hasHeightForWidth())
        self.teacherRadioButton.setSizePolicy(sizePolicy)
        self.teacherRadioButton.setMaximumSize(QtCore.QSize(100, 100))
        self.teacherRadioButton.setSizeIncrement(QtCore.QSize(0, 0))
        self.teacherRadioButton.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.teacherRadioButton.setObjectName("teacherRadioButton")

        self.horizontalLayout_3.addWidget(self.teacherRadioButton)
        self.verticalLayout_2.addLayout(self.horizontalLayout_3)
        spacerItem2 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.verticalLayout_2.addItem(spacerItem2)
        self.formLayout = QtWidgets.QFormLayout()
        self.formLayout.setLabelAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.formLayout.setObjectName("formLayout")
        self.studentTeacherIDLabel = QtWidgets.QLabel(self.centralwidget)
        self.studentTeacherIDLabel.setObjectName("studentTeacherIDLabel")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.studentTeacherIDLabel)
        self.studentTeacherIDLineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.studentTeacherIDLineEdit.setObjectName("studentTeacherIDLineEdit")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.studentTeacherIDLineEdit)
        self.firstNameLabel = QtWidgets.QLabel(self.centralwidget)
        self.firstNameLabel.setObjectName("firstNameLabel")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.firstNameLabel)
        self.firstNameLineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.firstNameLineEdit.setObjectName("firstNameLineEdit")

        self.formLayout.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.firstNameLineEdit)
        self.lastNameLabel = QtWidgets.QLabel(self.centralwidget)
        self.lastNameLabel.setObjectName("lastNameLabel")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.LabelRole, self.lastNameLabel)
        self.lastNameLineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.lastNameLineEdit.setObjectName("lastNameLineEdit")

        self.formLayout.setWidget(2, QtWidgets.QFormLayout.FieldRole, self.lastNameLineEdit)
        self.genderLabel = QtWidgets.QLabel(self.centralwidget)
        self.genderLabel.setObjectName("genderLabel")
        self.formLayout.setWidget(3, QtWidgets.QFormLayout.LabelRole, self.genderLabel)
        self.genderLineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.genderLineEdit.setObjectName("genderLineEdit")

        self.formLayout.setWidget(3, QtWidgets.QFormLayout.FieldRole, self.genderLineEdit)
        self.addressLabel = QtWidgets.QLabel(self.centralwidget)
        self.addressLabel.setObjectName("addressLabel")
        self.formLayout.setWidget(4, QtWidgets.QFormLayout.LabelRole, self.addressLabel)
        self.addressLineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.addressLineEdit.setObjectName("addressLineEdit")

        self.formLayout.setWidget(4, QtWidgets.QFormLayout.FieldRole, self.addressLineEdit)
        self.cityLabel = QtWidgets.QLabel(self.centralwidget)
        self.cityLabel.setObjectName("cityLabel")
        self.formLayout.setWidget(5, QtWidgets.QFormLayout.LabelRole, self.cityLabel)
        self.cityLineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.cityLineEdit.setObjectName("cityLineEdit")

        self.formLayout.setWidget(5, QtWidgets.QFormLayout.FieldRole, self.cityLineEdit)
        self.regionLabel = QtWidgets.QLabel(self.centralwidget)
        self.regionLabel.setObjectName("regionLabel")
        self.formLayout.setWidget(6, QtWidgets.QFormLayout.LabelRole, self.regionLabel)
        self.regionLineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.regionLineEdit.setObjectName("regionLineEdit")

        self.formLayout.setWidget(6, QtWidgets.QFormLayout.FieldRole, self.regionLineEdit)
        self.countryLabel = QtWidgets.QLabel(self.centralwidget)
        self.countryLabel.setObjectName("countryLabel")
        self.formLayout.setWidget(7, QtWidgets.QFormLayout.LabelRole, self.countryLabel)
        self.countryLineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.countryLineEdit.setObjectName("countryLineEdit")

        self.formLayout.setWidget(7, QtWidgets.QFormLayout.FieldRole, self.countryLineEdit)
        self.zipLabel = QtWidgets.QLabel(self.centralwidget)
        self.zipLabel.setObjectName("zipLabel")
        self.formLayout.setWidget(8, QtWidgets.QFormLayout.LabelRole, self.zipLabel)
        self.zipLineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.zipLineEdit.setObjectName("zipLineEdit")

        self.formLayout.setWidget(8, QtWidgets.QFormLayout.FieldRole, self.zipLineEdit)
        self.phoneNumberLabel = QtWidgets.QLabel(self.centralwidget)
        self.phoneNumberLabel.setObjectName("phoneNumberLabel")
        self.formLayout.setWidget(9, QtWidgets.QFormLayout.LabelRole, self.phoneNumberLabel)
        self.phoneNumberLineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.phoneNumberLineEdit.setObjectName("phoneNumberLineEdit")

        self.formLayout.setWidget(9, QtWidgets.QFormLayout.FieldRole, self.phoneNumberLineEdit)
        self.verticalLayout_2.addLayout(self.formLayout)
        self.horizontalLayout_2.addLayout(self.verticalLayout_2)
        spacerItem3 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.horizontalLayout_2.addItem(spacerItem3)
        self.courseContainer = QtWidgets.QVBoxLayout()
        self.courseContainer.setObjectName("courseContainer")
        self.courseContainerTitle = QtWidgets.QLabel(self.centralwidget)
        self.courseContainerTitle.setMaximumSize(QtCore.QSize(400, 100))
        self.courseContainerTitle.setAlignment(QtCore.Qt.AlignCenter)
        self.courseContainerTitle.setObjectName("courseContainerTitle")
        self.courseContainer.addWidget(self.courseContainerTitle)
        self.courseFormLayout = QtWidgets.QFormLayout()
        self.courseFormLayout.setContentsMargins(0, 0, 0, 0)
        self.courseFormLayout.setHorizontalSpacing(20)
        self.courseFormLayout.setVerticalSpacing(60)
        self.courseFormLayout.setObjectName("courseFormLayout")
        self.nameLabel = QtWidgets.QLabel(self.centralwidget)
        self.nameLabel.setObjectName("nameLabel")
        self.courseFormLayout.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.nameLabel)
        self.nameLineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.nameLineEdit.setObjectName("nameLineEdit")

        self.courseFormLayout.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.nameLineEdit)
        self.descriptionLabel = QtWidgets.QLabel(self.centralwidget)
        self.descriptionLabel.setObjectName("descriptionLabel")
        self.courseFormLayout.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.descriptionLabel)
        self.descriptionLineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.descriptionLineEdit.setObjectName("descriptionLineEdit")

        self.courseFormLayout.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.descriptionLineEdit)
        self.courseIDLabel = QtWidgets.QLabel(self.centralwidget)
        self.courseIDLabel.setObjectName("courseIDLabel")
        self.courseFormLayout.setWidget(2, QtWidgets.QFormLayout.LabelRole, self.courseIDLabel)
        self.courseIDLineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.courseIDLineEdit.setObjectName("courseIDLineEdit")

        self.courseFormLayout.setWidget(2, QtWidgets.QFormLayout.FieldRole, self.courseIDLineEdit)
        self.teacherIDLabel = QtWidgets.QLabel(self.centralwidget)
        self.teacherIDLabel.setObjectName("teacherIDLabel")
        self.courseFormLayout.setWidget(3, QtWidgets.QFormLayout.LabelRole, self.teacherIDLabel)
        self.teacherIDLineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.teacherIDLineEdit.setObjectName("teacherIDLineEdit")

        self.courseFormLayout.setWidget(3, QtWidgets.QFormLayout.FieldRole, self.teacherIDLineEdit)
        self.courseContainer.addLayout(self.courseFormLayout)
        self.horizontalLayout_2.addLayout(self.courseContainer)
        self.verticalLayout.addLayout(self.horizontalLayout_2)
        spacerItem4 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.verticalLayout.addItem(spacerItem4)
        self.sectionTwoFooter = QtWidgets.QHBoxLayout()
        self.sectionTwoFooter.setObjectName("sectionTwoFooter")
        self.addbutton = QtWidgets.QPushButton(self.centralwidget)
        self.addbutton.setObjectName("addbutton")
        self.sectionTwoFooter.addWidget(self.addbutton)
        self.updateButton = QtWidgets.QPushButton(self.centralwidget)
        self.updateButton.setObjectName("updateButton")
        self.sectionTwoFooter.addWidget(self.updateButton)
        self.searchButton = QtWidgets.QPushButton(self.centralwidget)
        self.searchButton.setObjectName("searchButton")
        self.sectionTwoFooter.addWidget(self.searchButton)
        self.deleteButton = QtWidgets.QPushButton(self.centralwidget)
        self.deleteButton.setObjectName("deleteButton")
        self.sectionTwoFooter.addWidget(self.deleteButton)
        self.verticalLayout.addLayout(self.sectionTwoFooter)
        self.horizontalLayout.addLayout(self.verticalLayout)
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Course Database"))
        self.personContainerTitle.setText(_translate("MainWindow", "Student/Teacher"))
        self.studentRadioButton.setText(_translate("MainWindow", "Student"))
        self.teacherRadioButton.setText(_translate("MainWindow", "Teacher"))
        self.studentTeacherIDLabel.setText(_translate("MainWindow", "Student/Teacher ID"))
        self.firstNameLabel.setText(_translate("MainWindow", "First name"))
        self.lastNameLabel.setText(_translate("MainWindow", "Last name"))
        self.genderLabel.setText(_translate("MainWindow", "Gender"))
        self.addressLabel.setText(_translate("MainWindow", "Address"))
        self.cityLabel.setText(_translate("MainWindow", "City"))
        self.regionLabel.setText(_translate("MainWindow", "Region"))
        self.countryLabel.setText(_translate("MainWindow", "Country"))
        self.zipLabel.setText(_translate("MainWindow", "Zip"))
        self.phoneNumberLabel.setText(_translate("MainWindow", "Phone number"))
        self.courseContainerTitle.setText(_translate("MainWindow", "Course"))
        self.nameLabel.setText(_translate("MainWindow", "Name"))
        self.descriptionLabel.setText(_translate("MainWindow", "Description"))
        self.courseIDLabel.setText(_translate("MainWindow", "Course ID"))
        self.teacherIDLabel.setText(_translate("MainWindow", "Teacher ID"))
        self.addbutton.setText(_translate("MainWindow", "Add"))
        self.updateButton.setText(_translate("MainWindow", "Update"))
        self.searchButton.setText(_translate("MainWindow", "Search"))
        self.deleteButton.setText(_translate("MainWindow", "Delete"))

    def add(self):
        if self.studentRadioButton.clicked():
            cursor.execute('USE courseDB')
            cursor.execute("""INSERT INTO student(student_id, first_name, last_name, gender, address, city, region, country, zip phone_number)
                            VALUES (%d, %s, %s, %s, %s, %s, %s, %s, %s, %d, %d)
                            """ % (''.join(self.firstNameLineEdit.text()),
                                   ''.join(self.lastNameLineEdit.text()),
                                   ''.join(self.genderNameLineEdit.text()),
                                   ''.join(self.addressLineEdit.text()),
                                   ''.join(self.cityLineEdit.text()),
                                   ''.join(self.regionLineEdit.text()),
                                   ''.join(self.countryLineEdit.text()),
                                   ''.join(self.zipLineEdit.text()),
                                   ''.join(self.phoneNumberLineEdit.text())
                                   ))

        elif self.teacherRadioButton.clicked():
            cursor.execute('USE courseDB')
            cursor.execute("""INSERT INTO teacher(teacher_id, first_name, last_name, gender, address, city, region, country, zip phone_number)
                            VALUES (%d, %s, %s, %s, %s, %s, %s, %s, %s, %d, %d)
                            """ % (''.join(self.firstNameLineEdit.text()),
                                   ''.join(self.lastNameLineEdit.text()),
                                   ''.join(self.genderNameLineEdit.text()),
                                   ''.join(self.addressLineEdit.text()),
                                   ''.join(self.cityLineEdit.text()),
                                   ''.join(self.regionLineEdit.text()),
                                   ''.join(self.countryLineEdit.text()),
                                   ''.join(self.zipLineEdit.text()),
                                   ''.join(self.phoneNumberLineEdit.text())))



if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

