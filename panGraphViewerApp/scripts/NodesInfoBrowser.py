# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'NodesInfoBrowser.ui'
#
# Created by: PyQt5 UI code generator 5.15.2
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_NodesInfoCanvas(object):
    def setupUi(self, NodesInfoCanvas):
        NodesInfoCanvas.setObjectName("NodesInfoCanvas")
        NodesInfoCanvas.resize(400, 300)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(NodesInfoCanvas.sizePolicy().hasHeightForWidth())
        NodesInfoCanvas.setSizePolicy(sizePolicy)
        self.verticalLayout = QtWidgets.QVBoxLayout(NodesInfoCanvas)
        self.verticalLayout.setObjectName("verticalLayout")
        self.NodeInfotextBrowser = QtWidgets.QTextBrowser(NodesInfoCanvas)
        self.NodeInfotextBrowser.setObjectName("NodeInfotextBrowser")
        self.verticalLayout.addWidget(self.NodeInfotextBrowser)

        self.retranslateUi(NodesInfoCanvas)
        QtCore.QMetaObject.connectSlotsByName(NodesInfoCanvas)

    def retranslateUi(self, NodesInfoCanvas):
        _translate = QtCore.QCoreApplication.translate
        NodesInfoCanvas.setWindowTitle(_translate("NodesInfoCanvas", "Selected node(s) Information"))
