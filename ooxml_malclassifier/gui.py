# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file
#
# Created by: PyQt5 UI code generator 5.15.7
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.

from PyQt5 import QtCore, QtWidgets
import json
from mal_classifier import main


class Ui_Dialog(object):
    def __init__(self):
        self.scan_result = None

    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.setEnabled(True)
        Dialog.resize(530, 440)
        self.gridLayout = QtWidgets.QGridLayout(Dialog)
        self.gridLayout.setObjectName("gridLayout")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label = QtWidgets.QLabel(Dialog)
        self.label.setObjectName("label")
        self.horizontalLayout.addWidget(self.label)
        self.dirPathLineEdit = QtWidgets.QLineEdit(Dialog)
        self.dirPathLineEdit.setObjectName("filePathLineEdit")
        self.horizontalLayout.addWidget(self.dirPathLineEdit)
        self.browseButton = QtWidgets.QPushButton(Dialog)
        self.browseButton.setEnabled(True)
        self.browseButton.setObjectName("browseButton")
        self.horizontalLayout.addWidget(self.browseButton)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.scanButton = QtWidgets.QPushButton(Dialog)
        self.scanButton.setObjectName("scanButton")
        self.verticalLayout.addWidget(self.scanButton)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.listWidget = QtWidgets.QListWidget(Dialog)
        self.listWidget.setObjectName("listWidget")
        self.horizontalLayout_3.addWidget(self.listWidget)
        self.verticalLayout.addLayout(self.horizontalLayout_3)
        self.gridLayout.addLayout(self.verticalLayout, 0, 0, 1, 1)
        self.retranslateUi(Dialog)

        # Signal handling
        self.scanButton.clicked.connect(lambda: self.scan())  # type: ignore
        self.browseButton.clicked.connect(lambda: self.browse())  # type: ignore
        self.listWidget.itemDoubleClicked['QListWidgetItem*'].connect(
            lambda: self.openResultDialog(self.listWidget.selectedItems(), self.scan_result))  # type: ignore
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "OOXML file scan"))
        self.label.setText(_translate("Dialog", "folder path : "))
        self.browseButton.setText(_translate("Dialog", "browse"))
        self.scanButton.setText(_translate("Dialog", "scan"))

    def scan(self):
        if self.dirPathLineEdit.text() == '':
            print('Missing directory path')
            return
        main(['-d', self.dirPathLineEdit.text()])
        self.scan_result = json.load(open('output.json'))
        self.listWidget.clear()
        for file_info in self.scan_result.values():
            listItem = QtWidgets.QListWidgetItem()
            listItem.setText(file_info['fileName'])
            self.listWidget.addItem(listItem)

    def browse(self):
        dir_ = QtWidgets.QFileDialog.getExistingDirectory(None, 'Open Directory', './')
        if dir_:
            self.dirPathLineEdit.setText(dir_)

    def openResultDialog(self, selected_items, display_content):
        for file_info in display_content.values():
            if file_info['fileName'] == selected_items[0].text():
                display_content = file_info

        self.ResultDialog = QtWidgets.QDialog()
        ui = Ui_ResultDialog()
        ui.setupUi(self.ResultDialog, selected_items, display_content)
        self.ResultDialog.show()


class Ui_ResultDialog(object):
    def setupUi(self, ResultDialog, SelectedItems: [], display_content):
        ResultDialog.setObjectName("ResultDialog")
        ResultDialog.resize(400, 300)
        self.gridLayout = QtWidgets.QGridLayout(ResultDialog)
        self.gridLayout.setObjectName("gridLayout")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.textBrowser = QtWidgets.QTextBrowser(ResultDialog)
        self.textBrowser.setObjectName("textBrowser")
        self.verticalLayout.addWidget(self.textBrowser)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.summaryLabel = QtWidgets.QLabel(ResultDialog)
        self.summaryLabel.setObjectName("summaryLabel")
        self.horizontalLayout.addWidget(self.summaryLabel)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.gridLayout.addLayout(self.verticalLayout, 0, 0, 1, 1)

        self.textBrowser.setText(str(json.dumps(display_content, indent=4)))

        self.retranslateUi(ResultDialog)
        QtCore.QMetaObject.connectSlotsByName(ResultDialog)

    def retranslateUi(self, ResultDialog):
        _translate = QtCore.QCoreApplication.translate
        ResultDialog.setWindowTitle(_translate("ResultDialog", "Result"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = Ui_Dialog()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())
