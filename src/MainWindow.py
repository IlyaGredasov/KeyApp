# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '.\design\main_window.ui'
#
# Created by: PyQt5 UI code generator 5.15.11
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1920, 1080)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        MainWindow.setStyleSheet(
            "QWidget, QLabel[widgetStyleClass=\"keyFrame\"], QFrame[widgetStyleClass=\"keyFrame\"] {\n"
            "    background-color: transparent;\n"
            "    color: #fafafc;\n"
            "    font-family: \'SF Pro\';\n"
            "    font-size: 14pt;\n"
            "    text-align: left;\n"
            "    font-weight: 1000;\n"
            "}\n"
            "\n"
            "QFrame[objectName^=\"passwordFrame\"], QFrame#passwordAddFrame {\n"
            "    border: 4px solid #4a4c54;\n"
            "    border-radius: 10px;\n"
            "}\n"
            "\n"
            "QFrame#keyFrame {\n"
            "    border: none;\n"
            "    border-radius: 15px;\n"
            "}\n"
            "\n"
            "QWidget#centralWidget {\n"
            "    background-color: #131726;\n"
            "}\n"
            "\n"
            "QWidget[widgetStyleClass=\"toolBar\"] {\n"
            "    background-color: #262f4d;\n"
            "}\n"
            "\n"
            "\n"
            "QPushButton#submitButton, QPushButton#backButton {\n"
            "    text-align: center;\n"
            "    font-family: \'SF Pro\';\n"
            "    font-size: 14pt;\n"
            "}\n"
            "\n"
            "QPushButton {\n"
            "    background-color: #394573;\n"
            "    border: none;\n"
            "    border-radius: 15px;\n"
            "    padding: 10px 20px;\n"
            "}\n"
            "\n"
            "QPushButton:hover {\n"
            "    background-color: #4a4c54;\n"
            "}\n"
            "\n"
            "QPushButton#addKeyButton {\n"
            "    background-color: transparent;\n"
            "    text-align: center;\n"
            "}\n"
            "\n"
            "QPushButton#addKeyButton:hover {\n"
            "    background-color: #363636\n"
            "}\n"
            "\n"
            "QLineEdit {\n"
            "    background-color: transparent;\n"
            "    border: 1px solid #394573;\n"
            "    border-radius: 15px;\n"
            "    padding: 10px 5px;\n"
            "    padding-left: 30px;\n"
            "}\n"
            "\n"
            "QLabel#saveKeyLabel {\n"
            "    color: #FFFFFF;\n"
            "    font-size: 16px;\n"
            "    font-weight: bold;\n"
            "    qproperty-alignment: \'AlignCenter\';\n"
            "}\n"
            "\n"
            "QLabel#iconLabel {\n"
            "    color: #FFFFFF;\n"
            "    font-size: 24px;\n"
            "    qproperty-alignment: \'AlignCenter\';\n"
            "}\n"
            "\n"
            "QLabel {\n"
            "    background-color: transparent;\n"
            "    color: #fafafc;\n"
            "    font-family: \'SF Pro\';\n"
            "    font-size: 14pt;\n"
            "    text-align: left;\n"
            "    font-weight: 500;\n"
            "}\n"
            "\n"
            "/* QScrollArea {\n"
            "    border: none;\n"
            "} */\n"
            "\n"
            "QCheckBox {\n"
            "    text-align: center;\n"
            "}\n"
            "")
        self.centralWidget = QtWidgets.QWidget(MainWindow)
        self.centralWidget.setObjectName("centralWidget")
        self.centralStackedWidget = QtWidgets.QStackedWidget(self.centralWidget)
        self.centralStackedWidget.setGeometry(QtCore.QRect(0, 0, 1920, 1080))
        self.centralStackedWidget.setStyleSheet("")
        self.centralStackedWidget.setObjectName("centralStackedWidget")
        self.mainPageWidget = QtWidgets.QWidget()
        self.mainPageWidget.setObjectName("mainPageWidget")
        self.toolsBarFrame = QtWidgets.QFrame(self.mainPageWidget)
        self.toolsBarFrame.setGeometry(QtCore.QRect(0, 0, 420, 1080))
        self.toolsBarFrame.setFrameShape(QtWidgets.QFrame.Box)
        self.toolsBarFrame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.toolsBarFrame.setObjectName("toolsBarFrame")
        self.toolsBarFrame.setParent(self.centralWidget)
        self.toolsBarFrame.lower()

        MainWindow.resize(1920, 1080)
        MainWindow.setWindowFlags(MainWindow.windowFlags() & ~QtCore.Qt.WindowType.WindowMaximizeButtonHint)

        self.toolsLabel = QtWidgets.QLabel(self.toolsBarFrame)
        self.toolsLabel.setGeometry(QtCore.QRect(0, 0, 421, 101))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Ignored, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.toolsLabel.sizePolicy().hasHeightForWidth())
        self.toolsLabel.setSizePolicy(sizePolicy)
        self.toolsLabel.setAlignment(QtCore.Qt.AlignLeading | QtCore.Qt.AlignLeft | QtCore.Qt.AlignTop)
        self.toolsLabel.setObjectName("toolsLabel")
        self.verticalLayoutWidget = QtWidgets.QWidget(self.mainPageWidget)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(0, 100, 421, 981))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.toolsVerticalLayout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.toolsVerticalLayout.setContentsMargins(30, 0, 30, 0)
        self.toolsVerticalLayout.setSpacing(0)
        self.toolsVerticalLayout.setObjectName("toolsVerticalLayout")
        self.findKeyLineEdit = QtWidgets.QLineEdit(self.verticalLayoutWidget)
        self.findKeyLineEdit.setClearButtonEnabled(False)
        self.findKeyLineEdit.setObjectName("findKeyLineEdit")
        self.toolsVerticalLayout.addWidget(self.findKeyLineEdit)
        self.responseLabel = QtWidgets.QLabel(self.verticalLayoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.responseLabel.sizePolicy().hasHeightForWidth())
        self.responseLabel.setSizePolicy(sizePolicy)
        self.responseLabel.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.responseLabel.setText("")
        self.responseLabel.setObjectName("responseLabel")
        self.toolsVerticalLayout.addWidget(self.responseLabel)
        self.getAllDataButton = QtWidgets.QPushButton(self.verticalLayoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.getAllDataButton.sizePolicy().hasHeightForWidth())
        self.getAllDataButton.setSizePolicy(sizePolicy)
        self.getAllDataButton.setObjectName("getAllDataButton")
        self.toolsVerticalLayout.addWidget(self.getAllDataButton)
        self.refreshMasterKeyButton = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.refreshMasterKeyButton.setObjectName("refreshMasterKeyButton")
        self.toolsVerticalLayout.addWidget(self.refreshMasterKeyButton)
        spacerItem = QtWidgets.QSpacerItem(20, 450, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        self.toolsVerticalLayout.addItem(spacerItem)
        self.exitButton = QtWidgets.QPushButton(self.verticalLayoutWidget)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("C:/Users/Ilya/.designer/backup/OpenPane.png"), QtGui.QIcon.Normal,
                       QtGui.QIcon.Off)
        self.exitButton.setIcon(icon)
        self.exitButton.setIconSize(QtCore.QSize(25, 25))
        self.exitButton.setObjectName("exitButton")
        self.toolsVerticalLayout.addWidget(self.exitButton)
        self.scrollArea = QtWidgets.QScrollArea(self.mainPageWidget)
        self.scrollArea.setGeometry(QtCore.QRect(419, -1, 1501, 1081))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.scrollArea.sizePolicy().hasHeightForWidth())
        self.scrollArea.setSizePolicy(sizePolicy)
        self.scrollArea.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.scrollArea.setFrameShadow(QtWidgets.QFrame.Plain)
        self.scrollArea.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOn)
        self.scrollArea.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOn)
        self.scrollArea.setSizeAdjustPolicy(QtWidgets.QAbstractScrollArea.AdjustToContents)
        self.scrollArea.setWidgetResizable(True)
        self.scrollArea.setAlignment(QtCore.Qt.AlignCenter)
        self.scrollArea.setObjectName("scrollArea")
        self.scrollAreaWidgetContents = QtWidgets.QWidget()
        self.scrollAreaWidgetContents.setGeometry(QtCore.QRect(0, 0, 1480, 1060))
        self.scrollAreaWidgetContents.setObjectName("scrollAreaWidgetContents")
        self.layoutWidget = QtWidgets.QWidget(self.scrollAreaWidgetContents)
        self.layoutWidget.setGeometry(QtCore.QRect(10, 10, 1481, 261))
        self.layoutWidget.setObjectName("layoutWidget")
        self.passwordsGridLayout = QtWidgets.QGridLayout(self.layoutWidget)
        self.passwordsGridLayout.setSizeConstraint(QtWidgets.QLayout.SetMinAndMaxSize)
        self.passwordsGridLayout.setContentsMargins(0, 0, 0, 0)
        self.passwordsGridLayout.setSpacing(6)
        self.passwordsGridLayout.setObjectName("passwordsGridLayout")
        self.passwordAddFrame = QtWidgets.QFrame(self.layoutWidget)
        self.passwordAddFrame.setEnabled(True)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.passwordAddFrame.sizePolicy().hasHeightForWidth())
        self.passwordAddFrame.setSizePolicy(sizePolicy)
        self.passwordAddFrame.setMinimumSize(QtCore.QSize(710, 240))
        self.passwordAddFrame.setMaximumSize(QtCore.QSize(710, 240))
        self.passwordAddFrame.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.passwordAddFrame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.passwordAddFrame.setObjectName("passwordAddFrame")
        self.verticalLayoutWidget_2 = QtWidgets.QWidget(self.passwordAddFrame)
        self.verticalLayoutWidget_2.setGeometry(QtCore.QRect(0, -2, 711, 241))
        self.verticalLayoutWidget_2.setObjectName("verticalLayoutWidget_2")
        self.passwordVerticalLayout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget_2)
        self.passwordVerticalLayout.setContentsMargins(50, 70, 50, 70)
        self.passwordVerticalLayout.setObjectName("passwordVerticalLayout")
        self.saveNewKeyLabel = QtWidgets.QLabel(self.verticalLayoutWidget_2)
        self.saveNewKeyLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.saveNewKeyLabel.setObjectName("saveNewKeyLabel")
        self.passwordVerticalLayout.addWidget(self.saveNewKeyLabel)
        self.addKeyButton = QtWidgets.QPushButton(self.verticalLayoutWidget_2)
        self.addKeyButton.setObjectName("addKeyButton")
        self.passwordVerticalLayout.addWidget(self.addKeyButton)
        self.passwordsGridLayout.addWidget(self.passwordAddFrame, 0, 1, 1, 1)
        self.scrollArea.setWidget(self.scrollAreaWidgetContents)
        self.centralStackedWidget.addWidget(self.mainPageWidget)
        self.keyPageWidget = QtWidgets.QWidget()
        self.keyPageWidget.setObjectName("keyPageWidget")
        self.keyFrame = QtWidgets.QFrame(self.keyPageWidget)
        self.keyFrame.setGeometry(QtCore.QRect(660, 300, 600, 481))
        self.keyFrame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.keyFrame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.keyFrame.setObjectName("keyFrame")
        self.verticalLayoutWidget_3 = QtWidgets.QWidget(self.keyFrame)
        self.verticalLayoutWidget_3.setGeometry(QtCore.QRect(0, 0, 601, 481))
        self.verticalLayoutWidget_3.setObjectName("verticalLayoutWidget_3")
        self.keyActionVerticalLayout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget_3)
        self.keyActionVerticalLayout.setContentsMargins(0, 0, 0, 0)
        self.keyActionVerticalLayout.setObjectName("keyActionVerticalLayout")
        self.domainLabel = QtWidgets.QLabel(self.verticalLayoutWidget_3)
        self.domainLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.domainLabel.setObjectName("domainLabel")
        self.keyActionVerticalLayout.addWidget(self.domainLabel)
        self.domainLineEdit = QtWidgets.QLineEdit(self.verticalLayoutWidget_3)
        self.domainLineEdit.setObjectName("domainLineEdit")
        self.keyActionVerticalLayout.addWidget(self.domainLineEdit)
        self.usernameLabel = QtWidgets.QLabel(self.verticalLayoutWidget_3)
        self.usernameLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.usernameLabel.setObjectName("usernameLabel")
        self.keyActionVerticalLayout.addWidget(self.usernameLabel)
        self.usernameLineEdit = QtWidgets.QLineEdit(self.verticalLayoutWidget_3)
        self.usernameLineEdit.setObjectName("usernameLineEdit")
        self.keyActionVerticalLayout.addWidget(self.usernameLineEdit)
        self.passwordLabel = QtWidgets.QLabel(self.verticalLayoutWidget_3)
        self.passwordLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.passwordLabel.setObjectName("passwordLabel")
        self.keyActionVerticalLayout.addWidget(self.passwordLabel)
        self.passwordLineEdit = QtWidgets.QLineEdit(self.verticalLayoutWidget_3)
        self.passwordLineEdit.setObjectName("passwordLineEdit")
        self.keyActionVerticalLayout.addWidget(self.passwordLineEdit)
        self.requiredAdminRightsCheckBox = QtWidgets.QCheckBox(self.verticalLayoutWidget_3)
        self.requiredAdminRightsCheckBox.setObjectName("requiredAdminRightsCheckBox")
        self.keyActionVerticalLayout.addWidget(self.requiredAdminRightsCheckBox)
        self.submitButton = QtWidgets.QPushButton(self.verticalLayoutWidget_3)
        self.submitButton.setObjectName("submitButton")
        self.keyActionVerticalLayout.addWidget(self.submitButton)
        self.backButton = QtWidgets.QPushButton(self.verticalLayoutWidget_3)
        self.backButton.setObjectName("backButton")
        self.keyActionVerticalLayout.addWidget(self.backButton)
        self.errorLabel = QtWidgets.QLabel(self.verticalLayoutWidget_3)
        self.errorLabel.setText("")
        self.errorLabel.setObjectName("errorLabel")
        self.keyActionVerticalLayout.addWidget(self.errorLabel)
        self.centralStackedWidget.addWidget(self.keyPageWidget)
        MainWindow.setCentralWidget(self.centralWidget)

        self.retranslateUi(MainWindow)
        self.centralStackedWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
        """
        Logic implementation
        """

        from PasswordQuery import Ui_passwordQueryWidget
        from DeleteDialog import Ui_deletePasswordDialog
        from Alert import Ui_alertWidget
        from WebApi import PasswordQuery, refreshMasterKey, getAll, \
            addQuery, deleteQuery, changeQuery, fuzzySearch, checkAdminPassword, checkToken, preventiveCheckToken
        from typing import List
        self.deleteDialog = QtWidgets.QDialog()
        self.chosenPasswordWidget: QtWidgets.QWidget | None = None
        self.alertWidget = QtWidgets.QWidget()
        Ui_alertWidget().setupUi(self.alertWidget)

        def showMainWindowSetup():
            self.alertWidget.hide()
            MainWindow.show()

        def showAlertWindowSetup():
            self.alertWidget.show()
            MainWindow.hide()

        def checkInterrupt():
            if checkToken():
                showMainWindowSetup()
            else:
                showAlertWindowSetup()

        def deletePasswordQuery():
            self.chosenPasswordWidget.deleteLater()
            self.passwordsGridLayout.removeWidget(self.chosenPasswordWidget)
            deleteQuery(self.chosenPasswordWidget.findChild(QtWidgets.QLineEdit, "domainLineEdit").text())
            self.chosenPasswordWidget = None
            updatePasswordWidgetsList(getAll())

        def approveDeletion():
            if self.chosenPasswordWidget.findChild(QtWidgets.QLabel,
                                                   "adminLabel").text() != "" and not checkAdminPassword(
                self.deleteDialog.findChild(
                    QtWidgets.QLineEdit, "passwordLineEdit").text()):
                self.deleteDialog.findChild(QtWidgets.QLabel, "errorLabel").setText("Wrong password")
            else:
                deletePasswordQuery()
                self.deleteDialog.accept()

        def addPasswordQuery():
            self.chosenPasswordWidget = None
            self.domainLineEdit.setText("")
            self.usernameLineEdit.setText("")
            self.passwordLineEdit.setText("")
            editPasswordWidget()

        @preventiveCheckToken(onFailure=showAlertWindowSetup)
        def updateMasterKeyResponse():
            refreshMasterKey()
            self.responseLabel.setText("Master key has been refreshed")

        @preventiveCheckToken(onFailure=showAlertWindowSetup)
        def submitPasswordChanges():
            domain = self.domainLineEdit.text().replace("\n", "")
            username = self.usernameLineEdit.text().replace("\n", "")
            password = self.passwordLineEdit.text().replace("\n", "")
            requiredAdminRights = self.requiredAdminRightsCheckBox.isChecked()
            if self.chosenPasswordWidget is None:
                addQuery(domain, username, password, requiredAdminRights)
                self.errorLabel.setText("Data has been added")
            else:
                changeQuery(domain, username, password, requiredAdminRights)
                self.errorLabel.setText("Data has been saved")
                self.chosenPasswordWidget = None
            updatePasswordWidgetsList(getAll())
            self.domainLineEdit.setReadOnly(False)
            backToMainWindow()

        def backToMainWindow():
            self.centralStackedWidget.setCurrentIndex(0)
            self.responseLabel.setText("")
            self.toolsBarFrame.show()

        def changePasswordVisibility(lineEdit: QtWidgets.QLineEdit):
            if lineEdit.echoMode() == QtWidgets.QLineEdit.Normal:
                lineEdit.setEchoMode(QtWidgets.QLineEdit.Password)
            else:
                lineEdit.setEchoMode(QtWidgets.QLineEdit.Normal)

        def editPasswordWidget(chosenWidget: QtWidgets.QWidget | None = None):
            self.domainLineEdit.setReadOnly(chosenWidget is not None)
            self.errorLabel.setText("")
            self.toolsBarFrame.hide()
            self.centralStackedWidget.setCurrentIndex(1)
            if chosenWidget is not None:
                self.chosenPasswordWidget = chosenWidget
                self.domainLineEdit.setText(chosenWidget.findChild(QtWidgets.QLineEdit, "domainLineEdit").text())
                self.usernameLineEdit.setText(chosenWidget.findChild(QtWidgets.QLineEdit, "usernameLineEdit").text())
                self.passwordLineEdit.setText(chosenWidget.findChild(QtWidgets.QLineEdit, "passwordLineEdit").text())
                self.requiredAdminRightsCheckBox.setChecked(
                    chosenWidget.findChild(QtWidgets.QLabel, "adminLabel").text() != "")

        @preventiveCheckToken(onFailure=showAlertWindowSetup)
        def deletePasswordWidget(chosenWidget: QtWidgets.QWidget):
            self.chosenPasswordWidget = chosenWidget
            self.deleteDialog = QtWidgets.QDialog()
            Ui_deletePasswordDialog().setupUi(self.deleteDialog)
            if self.chosenPasswordWidget.findChild(QtWidgets.QLabel, "adminLabel").text() == "":
                self.deleteDialog.findChild(QtWidgets.QLabel, "adminLabel").hide()
                self.deleteDialog.findChild(QtWidgets.QLineEdit, "passwordLineEdit").hide()
            self.deleteDialog.findChild(QtWidgets.QDialogButtonBox, "buttonBox").button(
                QtWidgets.QDialogButtonBox.Ok).clicked.connect(
                approveDeletion)
            okButton = self.deleteDialog.findChild(QtWidgets.QDialogButtonBox, "buttonBox").button(
                QtWidgets.QDialogButtonBox.Ok)

            if okButton:
                okButton.clicked.disconnect()
                okButton.clicked.connect(approveDeletion)
            self.deleteDialog.exec_()

        self.interruptTimer = QtCore.QTimer()
        self.interruptTimer.timeout.connect(checkInterrupt)
        self.interruptTimer.start(5000)

        @preventiveCheckToken(onFailure=showAlertWindowSetup)
        def deletePasswordWidgetsList():
            count = self.passwordsGridLayout.count()
            if count <= 1:
                self.scrollAreaWidgetContents.resize(self.scrollAreaWidgetContents.sizeHint())
                return

            for i in reversed(range(1, count)):
                self.passwordsGridLayout.itemAt(i).widget().deleteLater()
                self.passwordsGridLayout.removeWidget(self.passwordsGridLayout.itemAt(i).widget())

        @preventiveCheckToken(onFailure=showAlertWindowSetup)
        def updatePasswordWidgetsList(queryList: List[PasswordQuery]):
            deletePasswordWidgetsList()
            self.scrollAreaWidgetContents.resize(self.scrollAreaWidgetContents.sizeHint())
            self.responseLabel.setText("")
            self.scrollAreaWidgetContents.setMinimumHeight(240)
            QtWidgets.QApplication.processEvents()
            for i, query in enumerate(queryList):
                passwordQueryWidget: QtWidgets.QWidget = QtWidgets.QWidget()
                passwordQueryWidget.setSizePolicy(
                    QtWidgets.QSizePolicy.Preferred,
                    QtWidgets.QSizePolicy.Preferred
                )

                passwordQueryWidget.setFixedSize(710, 240)
                passwordQueryWidgetUi = Ui_passwordQueryWidget()
                passwordQueryWidgetUi.setupUi(passwordQueryWidget)
                self.passwordsGridLayout.addWidget(passwordQueryWidget, (1 + i) // 2,
                                                   1 + (1 + i) % 2, 1, 1)
                self.scrollAreaWidgetContents.setMinimumHeight(
                    (1 + (i + 1) // 2) * (passwordQueryWidget.height() + 20))
                QtWidgets.QApplication.processEvents()
                self.scrollAreaWidgetContents.adjustSize()
                passwordQueryWidget.findChild(QtWidgets.QLineEdit, "domainLineEdit").setText(query.domain)
                passwordQueryWidget.findChild(QtWidgets.QLineEdit, "usernameLineEdit").setText(
                    query.username)
                passwordQueryWidget.findChild(QtWidgets.QLineEdit, "passwordLineEdit").setText(
                    query.password)
                passwordQueryWidget.findChild(QtWidgets.QLabel, "adminLabel").setText(
                    "Protected With Admin Rights" if query.isAdminProtected else "")
                passwordQueryWidget.findChild(QtWidgets.QPushButton, "showPasswordButton").clicked.connect(
                    lambda checked,
                           lineEdit=passwordQueryWidget.findChild(QtWidgets.QLineEdit, "passwordLineEdit"):
                    changePasswordVisibility(lineEdit))
                passwordQueryWidget.findChild(QtWidgets.QPushButton, "editQueryButton").clicked.connect(
                    lambda checked,
                           widget=passwordQueryWidget: editPasswordWidget(widget))
                passwordQueryWidget.findChild(QtWidgets.QPushButton, "deleteQueryButton").clicked.connect(
                    lambda checked,
                           widget=passwordQueryWidget: deletePasswordWidget(widget))

        @preventiveCheckToken(onFailure=showAlertWindowSetup)
        def getAllWidgets():
            updatePasswordWidgetsList(getAll())

        @preventiveCheckToken(onFailure=showAlertWindowSetup)
        def getAllFuzzyWidgets():
            updatePasswordWidgetsList(fuzzySearch(self.findKeyLineEdit.text()))

        self.getAllDataButton.clicked.connect(lambda: getAllWidgets())
        self.findKeyLineEdit.returnPressed.connect(lambda: getAllFuzzyWidgets())
        self.refreshMasterKeyButton.clicked.connect(lambda: updateMasterKeyResponse())
        self.addKeyButton.clicked.connect(lambda: addPasswordQuery())
        self.submitButton.clicked.connect(lambda: submitPasswordChanges())
        self.backButton.clicked.connect(lambda: backToMainWindow())
        self.exitButton.clicked.connect(sys.exit)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.toolsBarFrame.setProperty("widgetStyleClass", _translate("MainWindow", "toolBar"))
        self.toolsLabel.setText(_translate("MainWindow", "TOOLS"))
        self.toolsLabel.setProperty("widgetStyleClass", _translate("MainWindow", "toolBar"))
        self.findKeyLineEdit.setPlaceholderText(_translate("MainWindow", "FIND KEY"))
        self.getAllDataButton.setText(_translate("MainWindow", "GET ALL DATA"))
        self.refreshMasterKeyButton.setText(_translate("MainWindow", "REFRESH MASTER KEY"))
        self.exitButton.setText(_translate("MainWindow", "EXIT"))
        self.passwordAddFrame.setProperty("widgetStyleClass", _translate("MainWindow", "passwordRectangle"))
        self.saveNewKeyLabel.setText(_translate("MainWindow", "SAVE NEW KEY"))
        self.addKeyButton.setText(_translate("MainWindow", "+"))
        self.keyFrame.setProperty("widgetStyleClass", _translate("MainWindow", "toolBar"))
        self.domainLabel.setText(_translate("MainWindow", "Domain"))
        self.domainLabel.setProperty("widgetStyleClass", _translate("MainWindow", "keyFrame"))
        self.usernameLabel.setText(_translate("MainWindow", "Username"))
        self.passwordLabel.setText(_translate("MainWindow", "Password"))
        self.requiredAdminRightsCheckBox.setText(_translate("MainWindow", "Required Admin Rights"))
        self.submitButton.setText(_translate("MainWindow", "Submit"))
        self.backButton.setText(_translate("MainWindow", "Back"))


if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
