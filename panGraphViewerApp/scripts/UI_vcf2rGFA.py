# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'vcf2rGFA.ui'
#
# Created by: PyQt5 UI code generator 5.15.2
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_vcf2rGFA(object):
    def setupUi(self, vcf2rGFA):
        vcf2rGFA.setObjectName("vcf2rGFA")
        vcf2rGFA.resize(485, 425)
        vcf2rGFA.setMinimumSize(QtCore.QSize(485, 425))
        vcf2rGFA.setMaximumSize(QtCore.QSize(485, 425))
        self.gridLayout_2 = QtWidgets.QGridLayout(vcf2rGFA)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.label = QtWidgets.QLabel(vcf2rGFA)
        self.label.setMaximumSize(QtCore.QSize(100, 25))
        font = QtGui.QFont()
        font.setBold(False)
        font.setWeight(50)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.gridLayout_2.addWidget(self.label, 4, 0, 1, 1)
        self.outClear = QtWidgets.QPushButton(vcf2rGFA)
        self.outClear.setMaximumSize(QtCore.QSize(60, 25))
        self.outClear.setObjectName("outClear")
        self.gridLayout_2.addWidget(self.outClear, 6, 3, 1, 1)
        self.outDirPath = QtWidgets.QLineEdit(vcf2rGFA)
        self.outDirPath.setMaximumSize(QtCore.QSize(16777215, 25))
        self.outDirPath.setObjectName("outDirPath")
        self.gridLayout_2.addWidget(self.outDirPath, 6, 1, 1, 1)
        self.fastaClear = QtWidgets.QPushButton(vcf2rGFA)
        self.fastaClear.setMaximumSize(QtCore.QSize(60, 25))
        self.fastaClear.setObjectName("fastaClear")
        self.gridLayout_2.addWidget(self.fastaClear, 2, 3, 1, 1)
        self.label_2 = QtWidgets.QLabel(vcf2rGFA)
        self.label_2.setMaximumSize(QtCore.QSize(180, 25))
        font = QtGui.QFont()
        font.setBold(False)
        font.setWeight(50)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.gridLayout_2.addWidget(self.label_2, 2, 0, 1, 1)
        self.vcfClear = QtWidgets.QPushButton(vcf2rGFA)
        self.vcfClear.setMaximumSize(QtCore.QSize(60, 25))
        self.vcfClear.setObjectName("vcfClear")
        self.gridLayout_2.addWidget(self.vcfClear, 4, 3, 1, 1)
        self.fastaPath = QtWidgets.QLineEdit(vcf2rGFA)
        self.fastaPath.setMaximumSize(QtCore.QSize(16777215, 25))
        self.fastaPath.setObjectName("fastaPath")
        self.gridLayout_2.addWidget(self.fastaPath, 2, 1, 1, 1)
        self.outSelect = QtWidgets.QPushButton(vcf2rGFA)
        self.outSelect.setMaximumSize(QtCore.QSize(60, 25))
        self.outSelect.setObjectName("outSelect")
        self.gridLayout_2.addWidget(self.outSelect, 6, 2, 1, 1)
        self.vcfSelect = QtWidgets.QPushButton(vcf2rGFA)
        self.vcfSelect.setMaximumSize(QtCore.QSize(60, 25))
        self.vcfSelect.setObjectName("vcfSelect")
        self.gridLayout_2.addWidget(self.vcfSelect, 4, 2, 1, 1)
        self.label_4 = QtWidgets.QLabel(vcf2rGFA)
        self.label_4.setMaximumSize(QtCore.QSize(120, 25))
        font = QtGui.QFont()
        font.setBold(False)
        font.setWeight(50)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")
        self.gridLayout_2.addWidget(self.label_4, 6, 0, 1, 1)
        self.label_3 = QtWidgets.QLabel(vcf2rGFA)
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.gridLayout_2.addWidget(self.label_3, 0, 0, 1, 2)
        self.fastaSelect = QtWidgets.QPushButton(vcf2rGFA)
        self.fastaSelect.setMaximumSize(QtCore.QSize(60, 25))
        self.fastaSelect.setObjectName("fastaSelect")
        self.gridLayout_2.addWidget(self.fastaSelect, 2, 2, 1, 1)
        self.vcfPath = QtWidgets.QLineEdit(vcf2rGFA)
        self.vcfPath.setMaximumSize(QtCore.QSize(16777215, 25))
        self.vcfPath.setObjectName("vcfPath")
        self.gridLayout_2.addWidget(self.vcfPath, 4, 1, 1, 1)
        self.gridLayout = QtWidgets.QGridLayout()
        self.gridLayout.setObjectName("gridLayout")
        self.convertStatus = QtWidgets.QLabel(vcf2rGFA)
        self.convertStatus.setMaximumSize(QtCore.QSize(16777215, 25))
        self.convertStatus.setObjectName("convertStatus")
        self.gridLayout.addWidget(self.convertStatus, 1, 1, 1, 1)
        self.covert = QtWidgets.QPushButton(vcf2rGFA)
        self.covert.setMaximumSize(QtCore.QSize(125, 25))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.covert.setFont(font)
        self.covert.setObjectName("covert")
        self.gridLayout.addWidget(self.covert, 1, 2, 1, 1)
        self.label_5 = QtWidgets.QLabel(vcf2rGFA)
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_5.setFont(font)
        self.label_5.setObjectName("label_5")
        self.gridLayout.addWidget(self.label_5, 1, 0, 1, 1)
        self.gridLayout_2.addLayout(self.gridLayout, 9, 0, 1, 4)
        self.formLayout = QtWidgets.QFormLayout()
        self.formLayout.setObjectName("formLayout")
        self.label_7 = QtWidgets.QLabel(vcf2rGFA)
        self.label_7.setMinimumSize(QtCore.QSize(332, 0))
        self.label_7.setObjectName("label_7")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.label_7)
        self.bbName = QtWidgets.QLineEdit(vcf2rGFA)
        self.bbName.setMinimumSize(QtCore.QSize(0, 25))
        self.bbName.setObjectName("bbName")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.bbName)
        self.label_6 = QtWidgets.QLabel(vcf2rGFA)
        self.label_6.setObjectName("label_6")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.label_6)
        self.threads = QtWidgets.QLineEdit(vcf2rGFA)
        self.threads.setMinimumSize(QtCore.QSize(0, 25))
        self.threads.setObjectName("threads")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.threads)
        self.label_8 = QtWidgets.QLabel(vcf2rGFA)
        self.label_8.setObjectName("label_8")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.LabelRole, self.label_8)
        self.chrTextEdit = QtWidgets.QPlainTextEdit(vcf2rGFA)
        self.chrTextEdit.setObjectName("chrTextEdit")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.FieldRole, self.chrTextEdit)
        self.gridLayout_2.addLayout(self.formLayout, 7, 0, 1, 4)

        self.retranslateUi(vcf2rGFA)
        QtCore.QMetaObject.connectSlotsByName(vcf2rGFA)

    def retranslateUi(self, vcf2rGFA):
        _translate = QtCore.QCoreApplication.translate
        vcf2rGFA.setWindowTitle(_translate("vcf2rGFA", "VCF2rGFA"))
        self.label.setText(_translate("vcf2rGFA", "The VCF File:"))
        self.outClear.setText(_translate("vcf2rGFA", "Clear"))
        self.fastaClear.setText(_translate("vcf2rGFA", "Clear"))
        self.label_2.setText(_translate("vcf2rGFA", "The Backbone Fasta File:"))
        self.vcfClear.setText(_translate("vcf2rGFA", "Clear"))
        self.outSelect.setText(_translate("vcf2rGFA", "Select"))
        self.vcfSelect.setText(_translate("vcf2rGFA", "Select"))
        self.label_4.setText(_translate("vcf2rGFA", "The Output Directory:"))
        self.label_3.setText(_translate("vcf2rGFA", "Convert a VCF file to an rGFA file"))
        self.fastaSelect.setText(_translate("vcf2rGFA", "Select"))
        self.convertStatus.setText(_translate("vcf2rGFA", "Idle"))
        self.covert.setText(_translate("vcf2rGFA", "Start"))
        self.label_5.setText(_translate("vcf2rGFA", "Convert"))
        self.label_7.setText(_translate("vcf2rGFA", "Name of backbone sample: "))
        self.label_6.setText(_translate("vcf2rGFA", "Threads to use: "))
        self.threads.setText(_translate("vcf2rGFA", "4"))
        self.label_8.setText(_translate("vcf2rGFA", "The chromosome to convert: "))
        self.chrTextEdit.setPlainText(_translate("vcf2rGFA", "All"))