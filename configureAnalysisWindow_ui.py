# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'configureAnalysisWindow.ui'
##
## Created by: Qt User Interface Compiler version 6.9.1
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QComboBox, QDialog, QGridLayout,
    QHBoxLayout, QLabel, QLineEdit, QPushButton,
    QSizePolicy, QTabWidget, QWidget)
from Icons import Icons_rc

class Ui_Configure(object):
    def setupUi(self, Configure):
        if not Configure.objectName():
            Configure.setObjectName(u"Configure")
        Configure.setEnabled(True)
        Configure.resize(403, 300)
        icon = QIcon()
        icon.addFile(u":/Main2/Screenshot 2025-06-19 122917.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        Configure.setWindowIcon(icon)
        self.gridLayout = QGridLayout(Configure)
        self.gridLayout.setObjectName(u"gridLayout")
        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.l_configAnalysis = QLabel(Configure)
        self.l_configAnalysis.setObjectName(u"l_configAnalysis")

        self.horizontalLayout.addWidget(self.l_configAnalysis)

        self.b_chooseFile = QPushButton(Configure)
        self.b_chooseFile.setObjectName(u"b_chooseFile")

        self.horizontalLayout.addWidget(self.b_chooseFile)


        self.gridLayout.addLayout(self.horizontalLayout, 0, 0, 1, 1)

        self.tab_SetUp = QTabWidget(Configure)
        self.tab_SetUp.setObjectName(u"tab_SetUp")
        self.tab_General_2 = QWidget()
        self.tab_General_2.setObjectName(u"tab_General_2")
        self.layoutWidget = QWidget(self.tab_General_2)
        self.layoutWidget.setObjectName(u"layoutWidget")
        self.layoutWidget.setGeometry(QRect(10, 20, 351, 111))
        self.gridLayout_2 = QGridLayout(self.layoutWidget)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.gridLayout_2.setContentsMargins(0, 0, 0, 0)
        self.b_instrucSetArchi = QLineEdit(self.layoutWidget)
        self.b_instrucSetArchi.setObjectName(u"b_instrucSetArchi")
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.b_instrucSetArchi.sizePolicy().hasHeightForWidth())
        self.b_instrucSetArchi.setSizePolicy(sizePolicy)
        self.b_instrucSetArchi.setMinimumSize(QSize(0, 0))

        self.gridLayout_2.addWidget(self.b_instrucSetArchi, 0, 0, 1, 1)

        self.b_optionsInstruc = QComboBox(self.layoutWidget)
        self.b_optionsInstruc.addItem("")
        self.b_optionsInstruc.setObjectName(u"b_optionsInstruc")
        sizePolicy1 = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Expanding)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.b_optionsInstruc.sizePolicy().hasHeightForWidth())
        self.b_optionsInstruc.setSizePolicy(sizePolicy1)
        self.b_optionsInstruc.setMouseTracking(True)
        self.b_optionsInstruc.setTabletTracking(True)
        self.b_optionsInstruc.setAcceptDrops(True)

        self.gridLayout_2.addWidget(self.b_optionsInstruc, 0, 1, 1, 1)

        self.b_timeout = QLineEdit(self.layoutWidget)
        self.b_timeout.setObjectName(u"b_timeout")
        self.b_timeout.setEnabled(True)
        sizePolicy.setHeightForWidth(self.b_timeout.sizePolicy().hasHeightForWidth())
        self.b_timeout.setSizePolicy(sizePolicy)
        self.b_timeout.setTabletTracking(True)

        self.gridLayout_2.addWidget(self.b_timeout, 1, 0, 1, 1)

        self.b_optionsTimeout = QComboBox(self.layoutWidget)
        self.b_optionsTimeout.addItem("")
        self.b_optionsTimeout.addItem("")
        self.b_optionsTimeout.addItem("")
        self.b_optionsTimeout.addItem("")
        self.b_optionsTimeout.addItem("")
        self.b_optionsTimeout.setObjectName(u"b_optionsTimeout")
        self.b_optionsTimeout.setEnabled(True)
        sizePolicy1.setHeightForWidth(self.b_optionsTimeout.sizePolicy().hasHeightForWidth())
        self.b_optionsTimeout.setSizePolicy(sizePolicy1)
        self.b_optionsTimeout.setMouseTracking(True)
        self.b_optionsTimeout.setTabletTracking(True)
        self.b_optionsTimeout.setAcceptDrops(True)

        self.gridLayout_2.addWidget(self.b_optionsTimeout, 1, 1, 1, 1)

        self.b_maxMemory = QLineEdit(self.layoutWidget)
        self.b_maxMemory.setObjectName(u"b_maxMemory")
        sizePolicy.setHeightForWidth(self.b_maxMemory.sizePolicy().hasHeightForWidth())
        self.b_maxMemory.setSizePolicy(sizePolicy)

        self.gridLayout_2.addWidget(self.b_maxMemory, 2, 0, 1, 1)

        self.b_optionsMaxMemory = QComboBox(self.layoutWidget)
        self.b_optionsMaxMemory.addItem("")
        self.b_optionsMaxMemory.setObjectName(u"b_optionsMaxMemory")
        sizePolicy1.setHeightForWidth(self.b_optionsMaxMemory.sizePolicy().hasHeightForWidth())
        self.b_optionsMaxMemory.setSizePolicy(sizePolicy1)
        self.b_optionsMaxMemory.setMouseTracking(True)
        self.b_optionsMaxMemory.setTabletTracking(True)
        self.b_optionsMaxMemory.setAcceptDrops(True)

        self.gridLayout_2.addWidget(self.b_optionsMaxMemory, 2, 1, 1, 1)

        self.tab_SetUp.addTab(self.tab_General_2, "")
        self.tab_Entrypoints = QWidget()
        self.tab_Entrypoints.setObjectName(u"tab_Entrypoints")
        self.tab_SetUp.addTab(self.tab_Entrypoints, "")
        self.tab_Extra = QWidget()
        self.tab_Extra.setObjectName(u"tab_Extra")
        self.tab_SetUp.addTab(self.tab_Extra, "")

        self.gridLayout.addWidget(self.tab_SetUp, 1, 0, 1, 1)

        self.b_StartAnalysis = QPushButton(Configure)
        self.b_StartAnalysis.setObjectName(u"b_StartAnalysis")
        sizePolicy2 = QSizePolicy(QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Preferred)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.b_StartAnalysis.sizePolicy().hasHeightForWidth())
        self.b_StartAnalysis.setSizePolicy(sizePolicy2)

        self.gridLayout.addWidget(self.b_StartAnalysis, 2, 0, 1, 1, Qt.AlignmentFlag.AlignRight)


        self.retranslateUi(Configure)

        self.tab_SetUp.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(Configure)
    # setupUi

    def retranslateUi(self, Configure):
        Configure.setWindowTitle(QCoreApplication.translate("Configure", u"Configure Analysis", None))
        self.l_configAnalysis.setText(QCoreApplication.translate("Configure", u"Configure Analysis on", None))
        self.b_chooseFile.setText(QCoreApplication.translate("Configure", u"Choose a file", None))
        self.b_instrucSetArchi.setText(QCoreApplication.translate("Configure", u"Instruction Set Architecture", None))
        self.b_optionsInstruc.setItemText(0, QCoreApplication.translate("Configure", u"x86", None))

        self.b_timeout.setText(QCoreApplication.translate("Configure", u"Timeout (mins)", None))
        self.b_optionsTimeout.setItemText(0, QCoreApplication.translate("Configure", u"30", None))
        self.b_optionsTimeout.setItemText(1, QCoreApplication.translate("Configure", u"60", None))
        self.b_optionsTimeout.setItemText(2, QCoreApplication.translate("Configure", u"90", None))
        self.b_optionsTimeout.setItemText(3, QCoreApplication.translate("Configure", u"120", None))
        self.b_optionsTimeout.setItemText(4, QCoreApplication.translate("Configure", u"180", None))

        self.b_maxMemory.setText(QCoreApplication.translate("Configure", u"Max Memory", None))
        self.b_optionsMaxMemory.setItemText(0, QCoreApplication.translate("Configure", u"16 Gb", None))

        self.tab_SetUp.setTabText(self.tab_SetUp.indexOf(self.tab_General_2), QCoreApplication.translate("Configure", u"General", None))
        self.tab_SetUp.setTabText(self.tab_SetUp.indexOf(self.tab_Entrypoints), QCoreApplication.translate("Configure", u"Entrypoints", None))
        self.tab_SetUp.setTabText(self.tab_SetUp.indexOf(self.tab_Extra), QCoreApplication.translate("Configure", u"...", None))
        self.b_StartAnalysis.setText(QCoreApplication.translate("Configure", u"Start Analysis", None))
    # retranslateUi

