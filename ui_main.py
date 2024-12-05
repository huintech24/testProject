# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'main.ui'
##
## Created by: Qt User Interface Compiler version 6.8.0
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
from PySide6.QtWidgets import (QApplication, QComboBox, QFrame, QHBoxLayout,
    QLabel, QLayout, QMainWindow, QPushButton,
    QSizePolicy, QStatusBar, QVBoxLayout, QWidget)
import resource_rc

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(790, 431)
        self.centralWidget = QWidget(MainWindow)
        self.centralWidget.setObjectName(u"centralWidget")
        self.verticalLayoutWidget = QWidget(self.centralWidget)
        self.verticalLayoutWidget.setObjectName(u"verticalLayoutWidget")
        self.verticalLayoutWidget.setGeometry(QRect(0, 0, 791, 384))
        self.verticalLayout = QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setSpacing(1)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setSizeConstraint(QLayout.SetMinAndMaxSize)
        self.verticalLayout.setContentsMargins(2, 0, 0, 0)
        self.headerFrame = QFrame(self.verticalLayoutWidget)
        self.headerFrame.setObjectName(u"headerFrame")
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.headerFrame.sizePolicy().hasHeightForWidth())
        self.headerFrame.setSizePolicy(sizePolicy)
        self.headerFrame.setMaximumSize(QSize(16777215, 40))
        self.headerFrame.setStyleSheet(u"background-color: rgb(0, 85, 127); color: #ffffff;")
        self.headerFrame.setFrameShape(QFrame.StyledPanel)
        self.headerFrame.setFrameShadow(QFrame.Plain)
        self.headerLayout = QHBoxLayout(self.headerFrame)
        self.headerLayout.setSpacing(5)
        self.headerLayout.setObjectName(u"headerLayout")
        self.headerLayout.setContentsMargins(5, 5, 5, 5)
        self.title = QLabel(self.headerFrame)
        self.title.setObjectName(u"title")
        sizePolicy1 = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Preferred)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.title.sizePolicy().hasHeightForWidth())
        self.title.setSizePolicy(sizePolicy1)
        self.title.setMaximumSize(QSize(16777215, 60))
        font = QFont()
        font.setPointSize(13)
        font.setBold(True)
        self.title.setFont(font)
        self.title.setFrameShape(QFrame.NoFrame)
        self.title.setFrameShadow(QFrame.Raised)
        self.title.setLineWidth(0)

        self.headerLayout.addWidget(self.title)

        self.current_time = QLabel(self.headerFrame)
        self.current_time.setObjectName(u"current_time")
        sizePolicy1.setHeightForWidth(self.current_time.sizePolicy().hasHeightForWidth())
        self.current_time.setSizePolicy(sizePolicy1)
        self.current_time.setMaximumSize(QSize(16777215, 40))
        self.current_time.setLineWidth(0)
        self.current_time.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.headerLayout.addWidget(self.current_time)


        self.verticalLayout.addWidget(self.headerFrame)

        self.toolbarWidget = QWidget(self.verticalLayoutWidget)
        self.toolbarWidget.setObjectName(u"toolbarWidget")
        sizePolicy.setHeightForWidth(self.toolbarWidget.sizePolicy().hasHeightForWidth())
        self.toolbarWidget.setSizePolicy(sizePolicy)
        self.toolbarWidget.setMinimumSize(QSize(0, 50))
        self.toolbarWidget.setMaximumSize(QSize(16777215, 50))
        self.toolbarWidget.setBaseSize(QSize(0, 50))
        self.toolbarLayout = QHBoxLayout(self.toolbarWidget)
        self.toolbarLayout.setSpacing(20)
        self.toolbarLayout.setObjectName(u"toolbarLayout")
        self.toolbarLayout.setSizeConstraint(QLayout.SetMinAndMaxSize)
        self.toolbarLayout.setContentsMargins(5, 5, 5, 5)
        self.tool_setting = QPushButton(self.toolbarWidget)
        self.tool_setting.setObjectName(u"tool_setting")
        sizePolicy2 = QSizePolicy(QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Fixed)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.tool_setting.sizePolicy().hasHeightForWidth())
        self.tool_setting.setSizePolicy(sizePolicy2)
        self.tool_setting.setMaximumSize(QSize(35, 35))
        self.tool_setting.setBaseSize(QSize(35, 35))
        self.tool_setting.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.tool_setting.setStyleSheet(u"background: none; border: none;")
        icon = QIcon()
        icon.addFile(u":/icon/settings.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.tool_setting.setIcon(icon)
        self.tool_setting.setIconSize(QSize(35, 35))

        self.toolbarLayout.addWidget(self.tool_setting)

        self.tool_info = QPushButton(self.toolbarWidget)
        self.tool_info.setObjectName(u"tool_info")
        sizePolicy2.setHeightForWidth(self.tool_info.sizePolicy().hasHeightForWidth())
        self.tool_info.setSizePolicy(sizePolicy2)
        self.tool_info.setMaximumSize(QSize(35, 35))
        self.tool_info.setBaseSize(QSize(35, 35))
        self.tool_info.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.tool_info.setStyleSheet(u"background: none; border: none;")
        icon1 = QIcon()
        icon1.addFile(u":/icon/info.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.tool_info.setIcon(icon1)
        self.tool_info.setIconSize(QSize(35, 35))

        self.toolbarLayout.addWidget(self.tool_info)

        self.tool_close = QPushButton(self.toolbarWidget)
        self.tool_close.setObjectName(u"tool_close")
        sizePolicy2.setHeightForWidth(self.tool_close.sizePolicy().hasHeightForWidth())
        self.tool_close.setSizePolicy(sizePolicy2)
        self.tool_close.setMinimumSize(QSize(35, 35))
        self.tool_close.setMaximumSize(QSize(35, 35))
        self.tool_close.setBaseSize(QSize(35, 35))
        self.tool_close.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.tool_close.setStyleSheet(u"background: none; border: none;")
        icon2 = QIcon()
        icon2.addFile(u":/icon/exit.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.tool_close.setIcon(icon2)
        self.tool_close.setIconSize(QSize(35, 35))

        self.toolbarLayout.addWidget(self.tool_close)


        self.verticalLayout.addWidget(self.toolbarWidget)

        self.line = QFrame(self.verticalLayoutWidget)
        self.line.setObjectName(u"line")
        self.line.setFrameShape(QFrame.Shape.HLine)
        self.line.setFrameShadow(QFrame.Shadow.Sunken)

        self.verticalLayout.addWidget(self.line)

        self.row1Layout = QHBoxLayout()
        self.row1Layout.setSpacing(10)
        self.row1Layout.setObjectName(u"row1Layout")
        self.row1Layout.setSizeConstraint(QLayout.SetMinAndMaxSize)
        self.row1Layout.setContentsMargins(5, 5, 5, 5)
        self.statusFrame = QFrame(self.verticalLayoutWidget)
        self.statusFrame.setObjectName(u"statusFrame")
        self.statusFrame.setMaximumSize(QSize(16777215, 135))
        self.statusFrame.setStyleSheet(u"background-color: #fff; border-radius: 5px;")
        self.statusFrame.setFrameShape(QFrame.StyledPanel)
        self.statusFrame.setFrameShadow(QFrame.Raised)
        self.statusLayout = QVBoxLayout(self.statusFrame)
        self.statusLayout.setSpacing(5)
        self.statusLayout.setObjectName(u"statusLayout")
        self.statusLayout.setContentsMargins(5, 5, 5, 5)
        self.lbl_status_title = QLabel(self.statusFrame)
        self.lbl_status_title.setObjectName(u"lbl_status_title")
        self.lbl_status_title.setMaximumSize(QSize(16777215, 40))
        self.lbl_status_title.setBaseSize(QSize(50, 40))
        font1 = QFont()
        font1.setPointSize(12)
        font1.setBold(True)
        self.lbl_status_title.setFont(font1)
        self.lbl_status_title.setAlignment(Qt.AlignCenter)

        self.statusLayout.addWidget(self.lbl_status_title)

        self.val_status = QLabel(self.statusFrame)
        self.val_status.setObjectName(u"val_status")
        self.val_status.setMinimumSize(QSize(0, 50))
        self.val_status.setMaximumSize(QSize(16777215, 50))
        self.val_status.setFont(font)
        self.val_status.setStyleSheet(u"color: green;")
        self.val_status.setAlignment(Qt.AlignCenter)

        self.statusLayout.addWidget(self.val_status)


        self.row1Layout.addWidget(self.statusFrame)

        self.manualFrame = QFrame(self.verticalLayoutWidget)
        self.manualFrame.setObjectName(u"manualFrame")
        self.manualFrame.setMaximumSize(QSize(16777215, 135))
        self.manualFrame.setStyleSheet(u"background-color: #fff; border-radius: 5px;")
        self.manualFrame.setFrameShape(QFrame.StyledPanel)
        self.manualFrame.setFrameShadow(QFrame.Raised)
        self.manualLayout = QVBoxLayout(self.manualFrame)
        self.manualLayout.setObjectName(u"manualLayout")
        self.manualLayout.setContentsMargins(10, 10, 10, 10)
        self.lbl_manual_title = QLabel(self.manualFrame)
        self.lbl_manual_title.setObjectName(u"lbl_manual_title")
        self.lbl_manual_title.setMinimumSize(QSize(0, 30))
        self.lbl_manual_title.setMaximumSize(QSize(16777215, 40))
        self.lbl_manual_title.setFont(font1)
        self.lbl_manual_title.setAlignment(Qt.AlignCenter)

        self.manualLayout.addWidget(self.lbl_manual_title)

        self.manualBtnLayout = QHBoxLayout()
        self.manualBtnLayout.setObjectName(u"manualBtnLayout")
        self.btn_on = QPushButton(self.manualFrame)
        self.btn_on.setObjectName(u"btn_on")
        self.btn_on.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.btn_on.setStyleSheet(u"background: none; border: none;")
        icon3 = QIcon()
        icon3.addFile(u":/icon/toggle-on.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.btn_on.setIcon(icon3)
        self.btn_on.setIconSize(QSize(80, 50))
        self.btn_on.setCheckable(False)

        self.manualBtnLayout.addWidget(self.btn_on)

        self.btn_off = QPushButton(self.manualFrame)
        self.btn_off.setObjectName(u"btn_off")
        self.btn_off.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.btn_off.setStyleSheet(u"background: none; border: none;")
        icon4 = QIcon()
        icon4.addFile(u":/icon/toggle-off.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        icon4.addFile(u":/icon/toggle-on.png", QSize(), QIcon.Mode.Normal, QIcon.State.On)
        icon4.addFile(u":/icon/toggle-off.png", QSize(), QIcon.Mode.Disabled, QIcon.State.Off)
        icon4.addFile(u":/icon/toggle-on.png", QSize(), QIcon.Mode.Disabled, QIcon.State.On)
        icon4.addFile(u":/icon/toggle-off.png", QSize(), QIcon.Mode.Active, QIcon.State.Off)
        icon4.addFile(u":/icon/toggle-on.png", QSize(), QIcon.Mode.Active, QIcon.State.On)
        icon4.addFile(u":/icon/toggle-off.png", QSize(), QIcon.Mode.Selected, QIcon.State.Off)
        icon4.addFile(u":/icon/toggle-on.png", QSize(), QIcon.Mode.Selected, QIcon.State.On)
        self.btn_off.setIcon(icon4)
        self.btn_off.setIconSize(QSize(80, 50))
        self.btn_off.setCheckable(False)

        self.manualBtnLayout.addWidget(self.btn_off)


        self.manualLayout.addLayout(self.manualBtnLayout)


        self.row1Layout.addWidget(self.manualFrame)

        self.rs485Frame = QFrame(self.verticalLayoutWidget)
        self.rs485Frame.setObjectName(u"rs485Frame")
        self.rs485Frame.setMaximumSize(QSize(16777215, 135))
        self.rs485Frame.setStyleSheet(u"background-color: #fff; border-radius: 5px;")
        self.rs485Frame.setFrameShape(QFrame.StyledPanel)
        self.rs485Frame.setFrameShadow(QFrame.Raised)
        self.rs485Layout = QVBoxLayout(self.rs485Frame)
        self.rs485Layout.setObjectName(u"rs485Layout")
        self.rs485Layout.setContentsMargins(12, 10, 10, 10)
        self.rs485Layout1 = QHBoxLayout()
        self.rs485Layout1.setObjectName(u"rs485Layout1")
        self.lbl_rs485_title = QLabel(self.rs485Frame)
        self.lbl_rs485_title.setObjectName(u"lbl_rs485_title")
        self.lbl_rs485_title.setFont(font1)

        self.rs485Layout1.addWidget(self.lbl_rs485_title)

        self.val_rs485_status = QLabel(self.rs485Frame)
        self.val_rs485_status.setObjectName(u"val_rs485_status")
        self.val_rs485_status.setMaximumSize(QSize(60, 20))
        font2 = QFont()
        font2.setPointSize(8)
        font2.setBold(False)
        self.val_rs485_status.setFont(font2)
        self.val_rs485_status.setStyleSheet(u"background-color: #aa0000; border-radius: 5px; color: #fff;")
        self.val_rs485_status.setAlignment(Qt.AlignCenter)

        self.rs485Layout1.addWidget(self.val_rs485_status)


        self.rs485Layout.addLayout(self.rs485Layout1)

        self.rs485Layout2 = QHBoxLayout()
        self.rs485Layout2.setObjectName(u"rs485Layout2")
        self.comport_list = QComboBox(self.rs485Frame)
        self.comport_list.setObjectName(u"comport_list")
        sizePolicy3 = QSizePolicy(QSizePolicy.Policy.Maximum, QSizePolicy.Policy.Fixed)
        sizePolicy3.setHorizontalStretch(0)
        sizePolicy3.setVerticalStretch(0)
        sizePolicy3.setHeightForWidth(self.comport_list.sizePolicy().hasHeightForWidth())
        self.comport_list.setSizePolicy(sizePolicy3)
        self.comport_list.setMinimumSize(QSize(100, 30))
        self.comport_list.setMaximumSize(QSize(150, 30))
        self.comport_list.setBaseSize(QSize(100, 30))
        self.comport_list.setStyleSheet(u"border: 1px solid #000;")

        self.rs485Layout2.addWidget(self.comport_list)

        self.connect_btn = QPushButton(self.rs485Frame)
        self.connect_btn.setObjectName(u"connect_btn")
        self.connect_btn.setMinimumSize(QSize(100, 30))
        self.connect_btn.setMaximumSize(QSize(150, 30))
        self.connect_btn.setBaseSize(QSize(100, 30))
        self.connect_btn.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.connect_btn.setStyleSheet(u"background-color: #1f497d; color: #fff; border-radius: 5px;")
        self.connect_btn.setCheckable(True)

        self.rs485Layout2.addWidget(self.connect_btn)

        self.btn_port_refresh = QPushButton(self.rs485Frame)
        self.btn_port_refresh.setObjectName(u"btn_port_refresh")
        self.btn_port_refresh.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))

        self.rs485Layout2.addWidget(self.btn_port_refresh)


        self.rs485Layout.addLayout(self.rs485Layout2)


        self.row1Layout.addWidget(self.rs485Frame)


        self.verticalLayout.addLayout(self.row1Layout)

        self.row2Layout = QHBoxLayout()
        self.row2Layout.setSpacing(10)
        self.row2Layout.setObjectName(u"row2Layout")
        self.row2Layout.setContentsMargins(5, 5, 5, 5)
        self.rsdDataFrame = QFrame(self.verticalLayoutWidget)
        self.rsdDataFrame.setObjectName(u"rsdDataFrame")
        self.rsdDataFrame.setStyleSheet(u"background-color: #fff; border-radius: 5px; ")
        self.rsdDataFrame.setFrameShape(QFrame.StyledPanel)
        self.rsdDataFrame.setFrameShadow(QFrame.Raised)
        self.rsdDataLayout = QVBoxLayout(self.rsdDataFrame)
        self.rsdDataLayout.setObjectName(u"rsdDataLayout")
        self.rsdIDLayout = QHBoxLayout()
        self.rsdIDLayout.setSpacing(10)
        self.rsdIDLayout.setObjectName(u"rsdIDLayout")
        self.rsdIDLayout.setContentsMargins(10, 10, 10, 10)
        self.lbl_rsd_id = QLabel(self.rsdDataFrame)
        self.lbl_rsd_id.setObjectName(u"lbl_rsd_id")
        self.lbl_rsd_id.setFont(font1)
        self.lbl_rsd_id.setStyleSheet(u"")

        self.rsdIDLayout.addWidget(self.lbl_rsd_id)

        self.val_rsd_id = QLabel(self.rsdDataFrame)
        self.val_rsd_id.setObjectName(u"val_rsd_id")
        self.val_rsd_id.setFont(font1)
        self.val_rsd_id.setStyleSheet(u"color: blue;")

        self.rsdIDLayout.addWidget(self.val_rsd_id)


        self.rsdDataLayout.addLayout(self.rsdIDLayout)

        self.currentLayout = QHBoxLayout()
        self.currentLayout.setSpacing(10)
        self.currentLayout.setObjectName(u"currentLayout")
        self.currentLayout.setContentsMargins(10, 10, 10, 10)
        self.lbl_current_title = QLabel(self.rsdDataFrame)
        self.lbl_current_title.setObjectName(u"lbl_current_title")
        font3 = QFont()
        font3.setPointSize(11)
        font3.setBold(True)
        self.lbl_current_title.setFont(font3)

        self.currentLayout.addWidget(self.lbl_current_title)

        self.val_current = QLabel(self.rsdDataFrame)
        self.val_current.setObjectName(u"val_current")
        self.val_current.setFont(font1)
        self.val_current.setStyleSheet(u"color: blue")
        self.val_current.setAlignment(Qt.AlignCenter)

        self.currentLayout.addWidget(self.val_current)

        self.lbl_current_unit = QLabel(self.rsdDataFrame)
        self.lbl_current_unit.setObjectName(u"lbl_current_unit")
        font4 = QFont()
        font4.setPointSize(11)
        self.lbl_current_unit.setFont(font4)

        self.currentLayout.addWidget(self.lbl_current_unit)


        self.rsdDataLayout.addLayout(self.currentLayout)

        self.temperatureLayout = QHBoxLayout()
        self.temperatureLayout.setSpacing(10)
        self.temperatureLayout.setObjectName(u"temperatureLayout")
        self.temperatureLayout.setContentsMargins(10, 10, 10, 10)
        self.lbl_temperature_title = QLabel(self.rsdDataFrame)
        self.lbl_temperature_title.setObjectName(u"lbl_temperature_title")
        self.lbl_temperature_title.setFont(font3)

        self.temperatureLayout.addWidget(self.lbl_temperature_title)

        self.val_temperature = QLabel(self.rsdDataFrame)
        self.val_temperature.setObjectName(u"val_temperature")
        self.val_temperature.setFont(font1)
        self.val_temperature.setStyleSheet(u"color: blue")
        self.val_temperature.setAlignment(Qt.AlignCenter)

        self.temperatureLayout.addWidget(self.val_temperature)

        self.lbl_temperature_unit = QLabel(self.rsdDataFrame)
        self.lbl_temperature_unit.setObjectName(u"lbl_temperature_unit")
        self.lbl_temperature_unit.setFont(font4)

        self.temperatureLayout.addWidget(self.lbl_temperature_unit)


        self.rsdDataLayout.addLayout(self.temperatureLayout)


        self.row2Layout.addWidget(self.rsdDataFrame)

        self.arcFrame = QFrame(self.verticalLayoutWidget)
        self.arcFrame.setObjectName(u"arcFrame")
        self.arcFrame.setStyleSheet(u"background-color: #fff; border-radius: 5px;")
        self.arcFrame.setFrameShape(QFrame.StyledPanel)
        self.arcFrame.setFrameShadow(QFrame.Raised)
        self.arcLayout = QVBoxLayout(self.arcFrame)
        self.arcLayout.setObjectName(u"arcLayout")
        self.arcHeaderLayout = QHBoxLayout()
        self.arcHeaderLayout.setSpacing(10)
        self.arcHeaderLayout.setObjectName(u"arcHeaderLayout")
        self.arcHeaderLayout.setContentsMargins(10, 10, 10, 10)
        self.lbl_arc_title = QLabel(self.arcFrame)
        self.lbl_arc_title.setObjectName(u"lbl_arc_title")
        self.lbl_arc_title.setFont(font1)

        self.arcHeaderLayout.addWidget(self.lbl_arc_title)

        self.val_arc_status = QLabel(self.arcFrame)
        self.val_arc_status.setObjectName(u"val_arc_status")
        sizePolicy4 = QSizePolicy(QSizePolicy.Policy.Maximum, QSizePolicy.Policy.Maximum)
        sizePolicy4.setHorizontalStretch(0)
        sizePolicy4.setVerticalStretch(0)
        sizePolicy4.setHeightForWidth(self.val_arc_status.sizePolicy().hasHeightForWidth())
        self.val_arc_status.setSizePolicy(sizePolicy4)
        self.val_arc_status.setMinimumSize(QSize(41, 20))
        self.val_arc_status.setStyleSheet(u"border-radius: 5px; color: #fff; padding: 3px;")
        self.val_arc_status.setAlignment(Qt.AlignCenter)

        self.arcHeaderLayout.addWidget(self.val_arc_status)


        self.arcLayout.addLayout(self.arcHeaderLayout)

        self.arcLayout1 = QHBoxLayout()
        self.arcLayout1.setSpacing(10)
        self.arcLayout1.setObjectName(u"arcLayout1")
        self.arcLayout1.setContentsMargins(10, 10, 10, 10)
        self.lbl_count = QLabel(self.arcFrame)
        self.lbl_count.setObjectName(u"lbl_count")
        self.lbl_count.setFont(font3)

        self.arcLayout1.addWidget(self.lbl_count)

        self.val_count = QLabel(self.arcFrame)
        self.val_count.setObjectName(u"val_count")
        self.val_count.setFont(font1)
        self.val_count.setStyleSheet(u"color: red;")
        self.val_count.setAlignment(Qt.AlignCenter)

        self.arcLayout1.addWidget(self.val_count)


        self.arcLayout.addLayout(self.arcLayout1)

        self.arcLayout2 = QHBoxLayout()
        self.arcLayout2.setSpacing(10)
        self.arcLayout2.setObjectName(u"arcLayout2")
        self.arcLayout2.setContentsMargins(10, 10, 10, 10)
        self.lbl_frequency = QLabel(self.arcFrame)
        self.lbl_frequency.setObjectName(u"lbl_frequency")
        self.lbl_frequency.setFont(font3)

        self.arcLayout2.addWidget(self.lbl_frequency)

        self.val_frequency = QLabel(self.arcFrame)
        self.val_frequency.setObjectName(u"val_frequency")
        self.val_frequency.setFont(font1)
        self.val_frequency.setStyleSheet(u"color: red;")
        self.val_frequency.setAlignment(Qt.AlignCenter)

        self.arcLayout2.addWidget(self.val_frequency)


        self.arcLayout.addLayout(self.arcLayout2)


        self.row2Layout.addWidget(self.arcFrame)

        self.alarmFrame = QFrame(self.verticalLayoutWidget)
        self.alarmFrame.setObjectName(u"alarmFrame")
        self.alarmFrame.setStyleSheet(u"background-color:#fff")
        self.alarmFrame.setFrameShape(QFrame.StyledPanel)
        self.alarmFrame.setFrameShadow(QFrame.Raised)

        self.row2Layout.addWidget(self.alarmFrame)


        self.verticalLayout.addLayout(self.row2Layout)

        MainWindow.setCentralWidget(self.centralWidget)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"10kW\uae09 RSD System", None))
        self.title.setText(QCoreApplication.translate("MainWindow", u"\ud0dc\uc591\uad11 10kW\uae09 RSD \uc2dc\uc2a4\ud15c", None))
        self.current_time.setText(QCoreApplication.translate("MainWindow", u"00:00", None))
        self.tool_setting.setText("")
        self.tool_info.setText("")
        self.tool_close.setText("")
        self.lbl_status_title.setText(QCoreApplication.translate("MainWindow", u"SYSTEM  \uc0c1\ud0dc", None))
        self.val_status.setText("")
        self.lbl_manual_title.setText(QCoreApplication.translate("MainWindow", u"\uc218\ub3d9 \uc81c\uc5b4", None))
        self.btn_on.setText("")
        self.btn_off.setText("")
        self.lbl_rs485_title.setText(QCoreApplication.translate("MainWindow", u"RS485 \ud1b5\uc2e0", None))
        self.val_rs485_status.setText(QCoreApplication.translate("MainWindow", u"\uc5f0\uacb0\uc548\ub428", None))
        self.comport_list.setPlaceholderText("")
        self.connect_btn.setText(QCoreApplication.translate("MainWindow", u"Connect", None))
        self.btn_port_refresh.setText(QCoreApplication.translate("MainWindow", u"R", None))
        self.lbl_rsd_id.setText(QCoreApplication.translate("MainWindow", u"RSD ID", None))
        self.val_rsd_id.setText("")
        self.lbl_current_title.setText(QCoreApplication.translate("MainWindow", u"\uc804\ub958", None))
        self.val_current.setText(QCoreApplication.translate("MainWindow", u"34 ", None))
        self.lbl_current_unit.setText(QCoreApplication.translate("MainWindow", u"A", None))
        self.lbl_temperature_title.setText(QCoreApplication.translate("MainWindow", u"\uc628\ub3c4", None))
        self.val_temperature.setText(QCoreApplication.translate("MainWindow", u"29", None))
        self.lbl_temperature_unit.setText(QCoreApplication.translate("MainWindow", u"\ub3c4", None))
        self.lbl_arc_title.setText(QCoreApplication.translate("MainWindow", u"\uc544\ud06c", None))
        self.val_arc_status.setText("")
        self.lbl_count.setText(QCoreApplication.translate("MainWindow", u"\ubc1c\uc0dd\ud69f\uc218", None))
        self.val_count.setText("")
        self.lbl_frequency.setText(QCoreApplication.translate("MainWindow", u"\uc8fc\ud30c\uc218 \ub300\uc5ed", None))
        self.val_frequency.setText("")
    # retranslateUi

