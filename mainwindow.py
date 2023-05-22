# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'mainwindow.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtWidgets import QApplication, QWidget

from Custom_Widgets.Widgets import QCustomSlideMenu
from Custom_Widgets.Widgets import QCustomStackedWidget


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1050, 724)
        MainWindow.setStyleSheet(u"*{\n"
"        border: none;\n"
"        background-color: transparent;\n"
"        background: transparent;\n"
"        padding: 0;\n"
"        margin: 0;\n"
"        color:#fff;\n"
"}\n"
"\n"
"#centralwidget{\n"
"        background-color: #3F8FD2;\n"
"}\n"
"#leftMenuSubContainer{\n"
"        background-color: #043C6B;\n"
"}\n"
"#leftMenuSubContainer QPushButton{\n"
"        text-align: left;\n"
"        padding: 10px 10px;\n"
"        border-top-left-radius: 10px;\n"
"        border-bottom-left-radius: 10px;\n"
"}\n"
"#headerContainer, #footerContainer{\n"
"        background-color: #25547B;\n"
"}\n"
"#profileSubContainer, #tasksTableWidget{\n"
"        background-color: #25547B;\n"
"        border-radius: 10px;\n"
"}\n"
"#frame_7, #popupNotificationSubContainer, #popupAddNewContainer{\n"
"        background-color:#043C6B;\n"
"        border-radius: 10px;\n"
"}\n"
"\n"
"")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.centralwidget.setStyleSheet(u"")
        self.horizontalLayout = QHBoxLayout(self.centralwidget)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.leftMenuContainer = QCustomSlideMenu(self.centralwidget)
        self.leftMenuContainer.setObjectName(u"leftMenuContainer")
        self.leftMenuContainer.setMinimumSize(QSize(0, 0))
        self.leftMenuContainer.setMaximumSize(QSize(16777215, 16777215))
        self.verticalLayout = QVBoxLayout(self.leftMenuContainer)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setSizeConstraint(QLayout.SetDefaultConstraint)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.leftMenuSubContainer = QWidget(self.leftMenuContainer)
        self.leftMenuSubContainer.setObjectName(u"leftMenuSubContainer")
        sizePolicy = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.leftMenuSubContainer.sizePolicy().hasHeightForWidth())
        self.leftMenuSubContainer.setSizePolicy(sizePolicy)
        self.leftMenuSubContainer.setMinimumSize(QSize(140, 0))
        self.leftMenuSubContainer.setMaximumSize(QSize(16777215, 16777215))
        self.verticalLayout_2 = QVBoxLayout(self.leftMenuSubContainer)
        self.verticalLayout_2.setSpacing(20)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.frame = QFrame(self.leftMenuSubContainer)
        self.frame.setObjectName(u"frame")
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_2 = QHBoxLayout(self.frame)
        self.horizontalLayout_2.setSpacing(0)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.menuBtn = QPushButton(self.frame)
        self.menuBtn.setObjectName(u"menuBtn")
        icon = QIcon()
        icon.addFile(u"icons/feather/menu.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.menuBtn.setIcon(icon)
        self.menuBtn.setIconSize(QSize(24, 24))

        self.horizontalLayout_2.addWidget(self.menuBtn)

        self.addBtn = QPushButton(self.frame)
        self.addBtn.setObjectName(u"addBtn")
        icon1 = QIcon()
        icon1.addFile(u"icons/feather/plus.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.addBtn.setIcon(icon1)
        self.addBtn.setIconSize(QSize(24, 24))

        self.horizontalLayout_2.addWidget(self.addBtn, 0, Qt.AlignRight)


        self.verticalLayout_2.addWidget(self.frame, 0, Qt.AlignTop)

        self.frame_3 = QFrame(self.leftMenuSubContainer)
        self.frame_3.setObjectName(u"frame_3")
        sizePolicy1 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Expanding)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.frame_3.sizePolicy().hasHeightForWidth())
        self.frame_3.setSizePolicy(sizePolicy1)
        self.frame_3.setFrameShape(QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QFrame.Raised)
        self.verticalLayout_3 = QVBoxLayout(self.frame_3)
        self.verticalLayout_3.setSpacing(0)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_3.setContentsMargins(0, 10, 0, 10)
        self.projectsBtn = QPushButton(self.frame_3)
        self.projectsBtn.setObjectName(u"projectsBtn")
        self.projectsBtn.setStyleSheet(u"background-color: #25547B;")
        icon2 = QIcon()
        icon2.addFile(u"icons/feather/layers.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.projectsBtn.setIcon(icon2)
        self.projectsBtn.setIconSize(QSize(24, 24))

        self.verticalLayout_3.addWidget(self.projectsBtn)

        self.tasksBtn = QPushButton(self.frame_3)
        self.tasksBtn.setObjectName(u"tasksBtn")
        icon3 = QIcon()
        icon3.addFile(u"icons/feather/file-text.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.tasksBtn.setIcon(icon3)
        self.tasksBtn.setIconSize(QSize(24, 24))

        self.verticalLayout_3.addWidget(self.tasksBtn)

        self.statisticsBtn = QPushButton(self.frame_3)
        self.statisticsBtn.setObjectName(u"statisticsBtn")
        icon4 = QIcon()
        icon4.addFile(u"icons/feather/activity.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.statisticsBtn.setIcon(icon4)
        self.statisticsBtn.setIconSize(QSize(24, 24))

        self.verticalLayout_3.addWidget(self.statisticsBtn)

        self.calendarBtn = QPushButton(self.frame_3)
        self.calendarBtn.setObjectName(u"calendarBtn")
        icon5 = QIcon()
        icon5.addFile(u"icons/feather/calendar.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.calendarBtn.setIcon(icon5)
        self.calendarBtn.setIconSize(QSize(24, 24))

        self.verticalLayout_3.addWidget(self.calendarBtn)


        self.verticalLayout_2.addWidget(self.frame_3, 0, Qt.AlignTop)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_2.addItem(self.verticalSpacer)

        self.frame_4 = QFrame(self.leftMenuSubContainer)
        self.frame_4.setObjectName(u"frame_4")
        self.frame_4.setFrameShape(QFrame.StyledPanel)
        self.frame_4.setFrameShadow(QFrame.Raised)
        self.verticalLayout_4 = QVBoxLayout(self.frame_4)
        self.verticalLayout_4.setSpacing(0)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.verticalLayout_4.setContentsMargins(0, 10, 0, 10)
        self.settingsBtn = QPushButton(self.frame_4)
        self.settingsBtn.setObjectName(u"settingsBtn")
        self.settingsBtn.setIconSize(QSize(24, 24))

        self.verticalLayout_4.addWidget(self.settingsBtn)


        self.verticalLayout_2.addWidget(self.frame_4, 0, Qt.AlignBottom)


        self.verticalLayout.addWidget(self.leftMenuSubContainer)


        self.horizontalLayout.addWidget(self.leftMenuContainer, 0, Qt.AlignLeft)

        self.mainBodyContainer = QWidget(self.centralwidget)
        self.mainBodyContainer.setObjectName(u"mainBodyContainer")
        sizePolicy2 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.mainBodyContainer.sizePolicy().hasHeightForWidth())
        self.mainBodyContainer.setSizePolicy(sizePolicy2)
        self.mainBodyContainer.setStyleSheet(u"")
        self.verticalLayout_5 = QVBoxLayout(self.mainBodyContainer)
        self.verticalLayout_5.setSpacing(0)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.verticalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.headerContainer = QWidget(self.mainBodyContainer)
        self.headerContainer.setObjectName(u"headerContainer")
        sizePolicy2.setHeightForWidth(self.headerContainer.sizePolicy().hasHeightForWidth())
        self.headerContainer.setSizePolicy(sizePolicy2)
        self.horizontalLayout_4 = QHBoxLayout(self.headerContainer)
        self.horizontalLayout_4.setSpacing(0)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.horizontalLayout_4.setContentsMargins(0, 9, 0, 9)
        self.frame_6 = QFrame(self.headerContainer)
        self.frame_6.setObjectName(u"frame_6")
        self.frame_6.setFrameShape(QFrame.StyledPanel)
        self.frame_6.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_6 = QHBoxLayout(self.frame_6)
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.horizontalLayout_6.setContentsMargins(0, 0, 0, 0)
        self.pushButton_5 = QPushButton(self.frame_6)
        self.pushButton_5.setObjectName(u"pushButton_5")
        icon6 = QIcon()
        icon6.addFile(u"icons/feather/search.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.pushButton_5.setIcon(icon6)
        self.pushButton_5.setIconSize(QSize(24, 24))

        self.horizontalLayout_6.addWidget(self.pushButton_5)


        self.horizontalLayout_4.addWidget(self.frame_6, 0, Qt.AlignRight)

        self.frame_5 = QFrame(self.headerContainer)
        self.frame_5.setObjectName(u"frame_5")
        self.frame_5.setFrameShape(QFrame.StyledPanel)
        self.frame_5.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_5 = QHBoxLayout(self.frame_5)
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.horizontalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.notificationBtn = QPushButton(self.frame_5)
        self.notificationBtn.setObjectName(u"notificationBtn")
        icon7 = QIcon()
        icon7.addFile(u"icons/feather/bell.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.notificationBtn.setIcon(icon7)
        self.notificationBtn.setIconSize(QSize(24, 24))

        self.horizontalLayout_5.addWidget(self.notificationBtn)

        self.profileBtn = QPushButton(self.frame_5)
        self.profileBtn.setObjectName(u"profileBtn")
        icon8 = QIcon()
        icon8.addFile(u"icons/feather/user.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.profileBtn.setIcon(icon8)
        self.profileBtn.setIconSize(QSize(24, 24))

        self.horizontalLayout_5.addWidget(self.profileBtn)


        self.horizontalLayout_4.addWidget(self.frame_5, 0, Qt.AlignHCenter)

        self.frame_2 = QFrame(self.headerContainer)
        self.frame_2.setObjectName(u"frame_2")
        self.frame_2.setFrameShape(QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_3 = QHBoxLayout(self.frame_2)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.minimizeBtn = QPushButton(self.frame_2)
        self.minimizeBtn.setObjectName(u"minimizeBtn")
        icon9 = QIcon()
        icon9.addFile(u"icons/feather/minus.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.minimizeBtn.setIcon(icon9)
        self.minimizeBtn.setIconSize(QSize(24, 24))

        self.horizontalLayout_3.addWidget(self.minimizeBtn)

        self.restoreBtn = QPushButton(self.frame_2)
        self.restoreBtn.setObjectName(u"restoreBtn")
        icon10 = QIcon()
        icon10.addFile(u"icons/feather/square.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.restoreBtn.setIcon(icon10)
        self.restoreBtn.setIconSize(QSize(24, 24))

        self.horizontalLayout_3.addWidget(self.restoreBtn)

        self.closeBtn = QPushButton(self.frame_2)
        self.closeBtn.setObjectName(u"closeBtn")
        icon11 = QIcon()
        icon11.addFile(u"icons/feather/x.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.closeBtn.setIcon(icon11)
        self.closeBtn.setIconSize(QSize(24, 24))

        self.horizontalLayout_3.addWidget(self.closeBtn)


        self.horizontalLayout_4.addWidget(self.frame_2, 0, Qt.AlignRight)


        self.verticalLayout_5.addWidget(self.headerContainer, 0, Qt.AlignTop)

        self.mainBodyContent = QWidget(self.mainBodyContainer)
        self.mainBodyContent.setObjectName(u"mainBodyContent")
        sizePolicy1.setHeightForWidth(self.mainBodyContent.sizePolicy().hasHeightForWidth())
        self.mainBodyContent.setSizePolicy(sizePolicy1)
        self.mainBodyContent.setMinimumSize(QSize(910, 466))
        self.horizontalLayout_7 = QHBoxLayout(self.mainBodyContent)
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.mainContentsContainer = QWidget(self.mainBodyContent)
        self.mainContentsContainer.setObjectName(u"mainContentsContainer")
        self.mainContentsContainer.setMinimumSize(QSize(0, 0))
        self.verticalLayout_9 = QVBoxLayout(self.mainContentsContainer)
        self.verticalLayout_9.setObjectName(u"verticalLayout_9")
        self.mainPages = QCustomStackedWidget(self.mainContentsContainer)
        self.mainPages.setObjectName(u"mainPages")
        self.pageProjects = QWidget()
        self.pageProjects.setObjectName(u"pageProjects")
        self.verticalLayout_14 = QVBoxLayout(self.pageProjects)
        self.verticalLayout_14.setObjectName(u"verticalLayout_14")
        self.label_5 = QLabel(self.pageProjects)
        self.label_5.setObjectName(u"label_5")
        sizePolicy3 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        sizePolicy3.setHorizontalStretch(0)
        sizePolicy3.setVerticalStretch(0)
        sizePolicy3.setHeightForWidth(self.label_5.sizePolicy().hasHeightForWidth())
        self.label_5.setSizePolicy(sizePolicy3)
        font = QFont()
        font.setPointSize(13)
        self.label_5.setFont(font)
        self.label_5.setAlignment(Qt.AlignCenter)

        self.verticalLayout_14.addWidget(self.label_5)

        self.mainPages.addWidget(self.pageProjects)
        self.pageTasks = QWidget()
        self.pageTasks.setObjectName(u"pageTasks")
        self.verticalLayout_13 = QVBoxLayout(self.pageTasks)
        self.verticalLayout_13.setObjectName(u"verticalLayout_13")
        self.widget = QWidget(self.pageTasks)
        self.widget.setObjectName(u"widget")
        self.verticalLayout_17 = QVBoxLayout(self.widget)
        self.verticalLayout_17.setObjectName(u"verticalLayout_17")
        self.label_6 = QLabel(self.widget)
        self.label_6.setObjectName(u"label_6")
        sizePolicy3.setHeightForWidth(self.label_6.sizePolicy().hasHeightForWidth())
        self.label_6.setSizePolicy(sizePolicy3)
        self.label_6.setFont(font)
        self.label_6.setAlignment(Qt.AlignCenter)

        self.verticalLayout_17.addWidget(self.label_6)

        self.tasksTableWidget = QTableWidget(self.widget)
        if (self.tasksTableWidget.columnCount() < 8):
            self.tasksTableWidget.setColumnCount(8)
        __qtablewidgetitem = QTableWidgetItem()
        __qtablewidgetitem.setBackground(QColor(4, 60, 107));
        self.tasksTableWidget.setHorizontalHeaderItem(0, __qtablewidgetitem)
        __qtablewidgetitem1 = QTableWidgetItem()
        __qtablewidgetitem1.setBackground(QColor(4, 60, 107));
        self.tasksTableWidget.setHorizontalHeaderItem(1, __qtablewidgetitem1)
        __qtablewidgetitem2 = QTableWidgetItem()
        __qtablewidgetitem2.setBackground(QColor(4, 60, 107));
        self.tasksTableWidget.setHorizontalHeaderItem(2, __qtablewidgetitem2)
        __qtablewidgetitem3 = QTableWidgetItem()
        __qtablewidgetitem3.setBackground(QColor(4, 60, 107));
        self.tasksTableWidget.setHorizontalHeaderItem(3, __qtablewidgetitem3)
        __qtablewidgetitem4 = QTableWidgetItem()
        __qtablewidgetitem4.setBackground(QColor(4, 60, 107));
        self.tasksTableWidget.setHorizontalHeaderItem(4, __qtablewidgetitem4)
        __qtablewidgetitem5 = QTableWidgetItem()
        __qtablewidgetitem5.setBackground(QColor(4, 60, 107));
        self.tasksTableWidget.setHorizontalHeaderItem(5, __qtablewidgetitem5)
        __qtablewidgetitem6 = QTableWidgetItem()
        __qtablewidgetitem6.setBackground(QColor(4, 60, 107));
        self.tasksTableWidget.setHorizontalHeaderItem(6, __qtablewidgetitem6)
        __qtablewidgetitem7 = QTableWidgetItem()
        __qtablewidgetitem7.setBackground(QColor(4, 60, 107));
        self.tasksTableWidget.setHorizontalHeaderItem(7, __qtablewidgetitem7)
        self.tasksTableWidget.setObjectName(u"tasksTableWidget")
        sizePolicy2.setHeightForWidth(self.tasksTableWidget.sizePolicy().hasHeightForWidth())
        self.tasksTableWidget.setSizePolicy(sizePolicy2)
        self.tasksTableWidget.setMinimumSize(QSize(0, 0))
        self.tasksTableWidget.setMaximumSize(QSize(16777212, 16777215))

        self.verticalLayout_17.addWidget(self.tasksTableWidget)


        self.verticalLayout_13.addWidget(self.widget)

        self.mainPages.addWidget(self.pageTasks)
        self.pageStatistics = QWidget()
        self.pageStatistics.setObjectName(u"pageStatistics")
        self.verticalLayout_12 = QVBoxLayout(self.pageStatistics)
        self.verticalLayout_12.setObjectName(u"verticalLayout_12")
        self.label_4 = QLabel(self.pageStatistics)
        self.label_4.setObjectName(u"label_4")
        sizePolicy3.setHeightForWidth(self.label_4.sizePolicy().hasHeightForWidth())
        self.label_4.setSizePolicy(sizePolicy3)
        self.label_4.setFont(font)
        self.label_4.setAlignment(Qt.AlignCenter)

        self.verticalLayout_12.addWidget(self.label_4)

        self.mainPages.addWidget(self.pageStatistics)
        self.pageCalendar = QWidget()
        self.pageCalendar.setObjectName(u"pageCalendar")
        self.verticalLayout_11 = QVBoxLayout(self.pageCalendar)
        self.verticalLayout_11.setObjectName(u"verticalLayout_11")
        self.label_7 = QLabel(self.pageCalendar)
        self.label_7.setObjectName(u"label_7")
        sizePolicy3.setHeightForWidth(self.label_7.sizePolicy().hasHeightForWidth())
        self.label_7.setSizePolicy(sizePolicy3)
        self.label_7.setFont(font)
        self.label_7.setAlignment(Qt.AlignCenter)

        self.verticalLayout_11.addWidget(self.label_7)

        self.mainPages.addWidget(self.pageCalendar)
        self.pageCreateNewProject = QWidget()
        self.pageCreateNewProject.setObjectName(u"pageCreateNewProject")
        self.verticalLayout_10 = QVBoxLayout(self.pageCreateNewProject)
        self.verticalLayout_10.setObjectName(u"verticalLayout_10")
        self.label_3 = QLabel(self.pageCreateNewProject)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setFont(font)
        self.label_3.setAlignment(Qt.AlignCenter)

        self.verticalLayout_10.addWidget(self.label_3)

        self.mainPages.addWidget(self.pageCreateNewProject)
        self.pageCreateNewTask = QWidget()
        self.pageCreateNewTask.setObjectName(u"pageCreateNewTask")
        self.pageCreateNewTask.setStyleSheet(u"")
        self.label_12 = QLabel(self.pageCreateNewTask)
        self.label_12.setObjectName(u"label_12")
        self.label_12.setGeometry(QRect(50, 10, 144, 24))
        self.label_12.setFont(font)
        self.label_12.setAlignment(Qt.AlignCenter)
        self.mainPages.addWidget(self.pageCreateNewTask)

        self.verticalLayout_9.addWidget(self.mainPages)


        self.horizontalLayout_7.addWidget(self.mainContentsContainer)

        self.profileContainer = QCustomSlideMenu(self.mainBodyContent)
        self.profileContainer.setObjectName(u"profileContainer")
        self.profileContainer.setMinimumSize(QSize(230, 0))
        self.profileContainer.setMaximumSize(QSize(230, 440))
        self.verticalLayout_6 = QVBoxLayout(self.profileContainer)
        self.verticalLayout_6.setSpacing(0)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.verticalLayout_6.setContentsMargins(0, 0, 0, 0)
        self.profileSubContainer = QWidget(self.profileContainer)
        self.profileSubContainer.setObjectName(u"profileSubContainer")
        sizePolicy4 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Ignored)
        sizePolicy4.setHorizontalStretch(0)
        sizePolicy4.setVerticalStretch(0)
        sizePolicy4.setHeightForWidth(self.profileSubContainer.sizePolicy().hasHeightForWidth())
        self.profileSubContainer.setSizePolicy(sizePolicy4)
        self.profileSubContainer.setMinimumSize(QSize(230, 454))
        self.profileSubContainer.setMaximumSize(QSize(16777215, 450))
        self.verticalLayout_7 = QVBoxLayout(self.profileSubContainer)
        self.verticalLayout_7.setSpacing(0)
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.verticalLayout_7.setContentsMargins(0, 0, 0, 0)
        self.frame_7 = QFrame(self.profileSubContainer)
        self.frame_7.setObjectName(u"frame_7")
        sizePolicy5 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Fixed)
        sizePolicy5.setHorizontalStretch(0)
        sizePolicy5.setVerticalStretch(0)
        sizePolicy5.setHeightForWidth(self.frame_7.sizePolicy().hasHeightForWidth())
        self.frame_7.setSizePolicy(sizePolicy5)
        self.frame_7.setFrameShape(QFrame.StyledPanel)
        self.frame_7.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_8 = QHBoxLayout(self.frame_7)
        self.horizontalLayout_8.setSpacing(6)
        self.horizontalLayout_8.setObjectName(u"horizontalLayout_8")
        self.horizontalLayout_8.setContentsMargins(6, 6, 6, 6)
        self.label = QLabel(self.frame_7)
        self.label.setObjectName(u"label")
        sizePolicy5.setHeightForWidth(self.label.sizePolicy().hasHeightForWidth())
        self.label.setSizePolicy(sizePolicy5)
        self.label.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_8.addWidget(self.label)

        self.closeProfileBtn = QPushButton(self.frame_7)
        self.closeProfileBtn.setObjectName(u"closeProfileBtn")
        icon12 = QIcon()
        icon12.addFile(u"icons/feather/x-circle.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.closeProfileBtn.setIcon(icon12)
        self.closeProfileBtn.setIconSize(QSize(24, 24))

        self.horizontalLayout_8.addWidget(self.closeProfileBtn, 0, Qt.AlignRight)


        self.verticalLayout_7.addWidget(self.frame_7)

        self.stackedWidget = QStackedWidget(self.profileSubContainer)
        self.stackedWidget.setObjectName(u"stackedWidget")
        self.stackedWidget.setMaximumSize(QSize(16777215, 16777215))
        self.page = QWidget()
        self.page.setObjectName(u"page")
        self.verticalLayout_8 = QVBoxLayout(self.page)
        self.verticalLayout_8.setObjectName(u"verticalLayout_8")
        self.label_2 = QLabel(self.page)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setAlignment(Qt.AlignCenter)

        self.verticalLayout_8.addWidget(self.label_2)

        self.stackedWidget.addWidget(self.page)
        self.page_2 = QWidget()
        self.page_2.setObjectName(u"page_2")
        self.verticalLayout_19 = QVBoxLayout(self.page_2)
        self.verticalLayout_19.setObjectName(u"verticalLayout_19")
        self.label_13 = QLabel(self.page_2)
        self.label_13.setObjectName(u"label_13")
        self.label_13.setAlignment(Qt.AlignCenter)

        self.verticalLayout_19.addWidget(self.label_13)

        self.stackedWidget.addWidget(self.page_2)

        self.verticalLayout_7.addWidget(self.stackedWidget)


        self.verticalLayout_6.addWidget(self.profileSubContainer, 0, Qt.AlignRight)


        self.horizontalLayout_7.addWidget(self.profileContainer, 0, Qt.AlignRight)


        self.verticalLayout_5.addWidget(self.mainBodyContent)

        self.popupNotificationContainer = QCustomSlideMenu(self.mainBodyContainer)
        self.popupNotificationContainer.setObjectName(u"popupNotificationContainer")
        self.popupNotificationContainer.setMinimumSize(QSize(0, 0))
        self.popupNotificationContainer.setMaximumSize(QSize(900, 16777215))
        self.verticalLayout_15 = QVBoxLayout(self.popupNotificationContainer)
        self.verticalLayout_15.setObjectName(u"verticalLayout_15")
        self.popupNotificationSubContainer = QWidget(self.popupNotificationContainer)
        self.popupNotificationSubContainer.setObjectName(u"popupNotificationSubContainer")
        self.verticalLayout_16 = QVBoxLayout(self.popupNotificationSubContainer)
        self.verticalLayout_16.setObjectName(u"verticalLayout_16")
        self.label_9 = QLabel(self.popupNotificationSubContainer)
        self.label_9.setObjectName(u"label_9")
        font1 = QFont()
        font1.setBold(True)
        font1.setWeight(75)
        self.label_9.setFont(font1)

        self.verticalLayout_16.addWidget(self.label_9)

        self.frame_8 = QFrame(self.popupNotificationSubContainer)
        self.frame_8.setObjectName(u"frame_8")
        self.frame_8.setFrameShape(QFrame.StyledPanel)
        self.frame_8.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_9 = QHBoxLayout(self.frame_8)
        self.horizontalLayout_9.setObjectName(u"horizontalLayout_9")
        self.label_8 = QLabel(self.frame_8)
        self.label_8.setObjectName(u"label_8")
        sizePolicy6 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Preferred)
        sizePolicy6.setHorizontalStretch(0)
        sizePolicy6.setVerticalStretch(0)
        sizePolicy6.setHeightForWidth(self.label_8.sizePolicy().hasHeightForWidth())
        self.label_8.setSizePolicy(sizePolicy6)
        self.label_8.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_9.addWidget(self.label_8)

        self.closeNotificationBtn = QPushButton(self.frame_8)
        self.closeNotificationBtn.setObjectName(u"closeNotificationBtn")
        sizePolicy7 = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        sizePolicy7.setHorizontalStretch(0)
        sizePolicy7.setVerticalStretch(0)
        sizePolicy7.setHeightForWidth(self.closeNotificationBtn.sizePolicy().hasHeightForWidth())
        self.closeNotificationBtn.setSizePolicy(sizePolicy7)
        self.closeNotificationBtn.setMinimumSize(QSize(0, 0))
        icon13 = QIcon()
        icon13.addFile(u"icons/feather/x-octagon.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.closeNotificationBtn.setIcon(icon13)
        self.closeNotificationBtn.setIconSize(QSize(24, 24))

        self.horizontalLayout_9.addWidget(self.closeNotificationBtn, 0, Qt.AlignRight)


        self.verticalLayout_16.addWidget(self.frame_8)


        self.verticalLayout_15.addWidget(self.popupNotificationSubContainer)


        self.verticalLayout_5.addWidget(self.popupNotificationContainer)

        self.popupAddNewContainer = QCustomSlideMenu(self.mainBodyContainer)
        self.popupAddNewContainer.setObjectName(u"popupAddNewContainer")
        self.popupAddNewContainer.setMinimumSize(QSize(50, 50))
        self.popupAddNewContainer.setMaximumSize(QSize(400, 16777215))
        self.verticalLayout_18 = QVBoxLayout(self.popupAddNewContainer)
        self.verticalLayout_18.setObjectName(u"verticalLayout_18")
        self.frame_13 = QFrame(self.popupAddNewContainer)
        self.frame_13.setObjectName(u"frame_13")
        self.frame_13.setFrameShape(QFrame.StyledPanel)
        self.frame_13.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_15 = QHBoxLayout(self.frame_13)
        self.horizontalLayout_15.setObjectName(u"horizontalLayout_15")
        self.AddProjectBtn = QPushButton(self.frame_13)
        self.AddProjectBtn.setObjectName(u"AddProjectBtn")
        self.AddProjectBtn.setIcon(icon2)
        self.AddProjectBtn.setIconSize(QSize(24, 24))

        self.horizontalLayout_15.addWidget(self.AddProjectBtn)

        self.AddTaskBtn = QPushButton(self.frame_13)
        self.AddTaskBtn.setObjectName(u"AddTaskBtn")
        sizePolicy8 = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Fixed)
        sizePolicy8.setHorizontalStretch(0)
        sizePolicy8.setVerticalStretch(0)
        sizePolicy8.setHeightForWidth(self.AddTaskBtn.sizePolicy().hasHeightForWidth())
        self.AddTaskBtn.setSizePolicy(sizePolicy8)
        self.AddTaskBtn.setIcon(icon3)
        self.AddTaskBtn.setIconSize(QSize(24, 24))

        self.horizontalLayout_15.addWidget(self.AddTaskBtn)


        self.verticalLayout_18.addWidget(self.frame_13)


        self.verticalLayout_5.addWidget(self.popupAddNewContainer)

        self.footerContainer = QWidget(self.mainBodyContainer)
        self.footerContainer.setObjectName(u"footerContainer")
        self.horizontalLayout_11 = QHBoxLayout(self.footerContainer)
        self.horizontalLayout_11.setObjectName(u"horizontalLayout_11")
        self.frame_9 = QFrame(self.footerContainer)
        self.frame_9.setObjectName(u"frame_9")
        self.frame_9.setMinimumSize(QSize(0, 0))
        self.frame_9.setFrameShape(QFrame.StyledPanel)
        self.frame_9.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_10 = QHBoxLayout(self.frame_9)
        self.horizontalLayout_10.setObjectName(u"horizontalLayout_10")
        self.label_10 = QLabel(self.frame_9)
        self.label_10.setObjectName(u"label_10")

        self.horizontalLayout_10.addWidget(self.label_10)


        self.horizontalLayout_11.addWidget(self.frame_9)

        self.sizeGrip = QFrame(self.footerContainer)
        self.sizeGrip.setObjectName(u"sizeGrip")
        self.sizeGrip.setMinimumSize(QSize(30, 30))
        self.sizeGrip.setMaximumSize(QSize(30, 30))
        self.sizeGrip.setFrameShape(QFrame.StyledPanel)
        self.sizeGrip.setFrameShadow(QFrame.Raised)
        self.label_11 = QLabel(self.sizeGrip)
        self.label_11.setObjectName(u"label_11")
        self.label_11.setGeometry(QRect(20, 0, 58, 18))

        self.horizontalLayout_11.addWidget(self.sizeGrip)


        self.verticalLayout_5.addWidget(self.footerContainer)


        self.horizontalLayout.addWidget(self.mainBodyContainer)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menuBar = QMenuBar(MainWindow)
        self.menuBar.setObjectName(u"menuBar")
        self.menuBar.setGeometry(QRect(0, 0, 1050, 30))
        MainWindow.setMenuBar(self.menuBar)
        self.toolBar = QToolBar(MainWindow)
        self.toolBar.setObjectName(u"toolBar")
        MainWindow.addToolBar(Qt.TopToolBarArea, self.toolBar)

        self.retranslateUi(MainWindow)

        self.mainPages.setCurrentIndex(1)
        self.stackedWidget.setCurrentIndex(1)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"Task-tracker", None))
#if QT_CONFIG(tooltip)
        self.menuBtn.setToolTip(QCoreApplication.translate("MainWindow", u"Menu", None))
#endif // QT_CONFIG(tooltip)
        self.menuBtn.setText("")
        self.addBtn.setText("")
#if QT_CONFIG(tooltip)
        self.projectsBtn.setToolTip(QCoreApplication.translate("MainWindow", u"Projects", None))
#endif // QT_CONFIG(tooltip)
        self.projectsBtn.setText(QCoreApplication.translate("MainWindow", u"\u041f\u0440\u043e\u0435\u043a\u0442\u044b", None))
#if QT_CONFIG(tooltip)
        self.tasksBtn.setToolTip(QCoreApplication.translate("MainWindow", u"Tasks", None))
#endif // QT_CONFIG(tooltip)
        self.tasksBtn.setText(QCoreApplication.translate("MainWindow", u"\u0417\u0430\u0434\u0430\u0447\u0438", None))
#if QT_CONFIG(tooltip)
        self.statisticsBtn.setToolTip(QCoreApplication.translate("MainWindow", u"Statistics", None))
#endif // QT_CONFIG(tooltip)
        self.statisticsBtn.setText(QCoreApplication.translate("MainWindow", u"\u0421\u0442\u0430\u0442\u0438\u0441\u0442\u0438\u043a\u0430", None))
#if QT_CONFIG(tooltip)
        self.calendarBtn.setToolTip(QCoreApplication.translate("MainWindow", u"Calendar", None))
#endif // QT_CONFIG(tooltip)
        self.calendarBtn.setText(QCoreApplication.translate("MainWindow", u"\u041a\u0430\u043b\u0435\u043d\u0434\u0430\u0440\u044c", None))
#if QT_CONFIG(tooltip)
        self.settingsBtn.setToolTip(QCoreApplication.translate("MainWindow", u"Settings", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(tooltip)
        self.pushButton_5.setToolTip(QCoreApplication.translate("MainWindow", u"Search", None))
#endif // QT_CONFIG(tooltip)
        self.pushButton_5.setText("")
#if QT_CONFIG(tooltip)
        self.notificationBtn.setToolTip(QCoreApplication.translate("MainWindow", u"Notification", None))
#endif // QT_CONFIG(tooltip)
        self.notificationBtn.setText("")
#if QT_CONFIG(tooltip)
        self.profileBtn.setToolTip(QCoreApplication.translate("MainWindow", u"Profile", None))
#endif // QT_CONFIG(tooltip)
        self.profileBtn.setText("")
#if QT_CONFIG(tooltip)
        self.minimizeBtn.setToolTip(QCoreApplication.translate("MainWindow", u"Minimise Window", None))
#endif // QT_CONFIG(tooltip)
        self.minimizeBtn.setText("")
#if QT_CONFIG(tooltip)
        self.restoreBtn.setToolTip(QCoreApplication.translate("MainWindow", u"Restore Window", None))
#endif // QT_CONFIG(tooltip)
        self.restoreBtn.setText("")
#if QT_CONFIG(tooltip)
        self.closeBtn.setToolTip(QCoreApplication.translate("MainWindow", u"Close Window", None))
#endif // QT_CONFIG(tooltip)
        self.closeBtn.setText("")
        self.label_5.setText(QCoreApplication.translate("MainWindow", u"\u041f\u0440\u043e\u0435\u043a\u0442\u044b", None))
        self.label_6.setText(QCoreApplication.translate("MainWindow", u"\u0417\u0430\u0434\u0430\u0447\u0438", None))
        ___qtablewidgetitem = self.tasksTableWidget.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(QCoreApplication.translate("MainWindow", u"\u041d\u0430\u0437\u0432\u0430\u043d\u0438\u0435", None));
        ___qtablewidgetitem1 = self.tasksTableWidget.horizontalHeaderItem(1)
        ___qtablewidgetitem1.setText(QCoreApplication.translate("MainWindow", u"\u041e\u043f\u0438\u0441\u0430\u043d\u0438\u0435", None));
        ___qtablewidgetitem2 = self.tasksTableWidget.horizontalHeaderItem(2)
        ___qtablewidgetitem2.setText(QCoreApplication.translate("MainWindow", u"\u041f\u0440\u043e\u0435\u043a\u0442", None));
        ___qtablewidgetitem3 = self.tasksTableWidget.horizontalHeaderItem(3)
        ___qtablewidgetitem3.setText(QCoreApplication.translate("MainWindow", u"\u041f\u0440\u0438\u043e\u0440\u0438\u0442\u0435\u0442", None));
        ___qtablewidgetitem4 = self.tasksTableWidget.horizontalHeaderItem(4)
        ___qtablewidgetitem4.setText(QCoreApplication.translate("MainWindow", u"\u041d\u0430\u0447\u0430\u043b\u043e", None));
        ___qtablewidgetitem5 = self.tasksTableWidget.horizontalHeaderItem(5)
        ___qtablewidgetitem5.setText(QCoreApplication.translate("MainWindow", u"\u041e\u043a\u043e\u043d\u0447\u0430\u043d\u0438\u0435", None));
        ___qtablewidgetitem6 = self.tasksTableWidget.horizontalHeaderItem(6)
        ___qtablewidgetitem6.setText(QCoreApplication.translate("MainWindow", u"\u0421\u0442\u0430\u0442\u0443\u0441", None));
        ___qtablewidgetitem7 = self.tasksTableWidget.horizontalHeaderItem(7)
        ___qtablewidgetitem7.setText(QCoreApplication.translate("MainWindow", u"\u0414\u0435\u0439\u0441\u0442\u0432\u0438\u0435", None));
        self.label_4.setText(QCoreApplication.translate("MainWindow", u"\u0421\u0442\u0430\u0442\u0438\u0441\u0442\u0438\u043a\u0430", None))
        self.label_7.setText(QCoreApplication.translate("MainWindow", u"\u041a\u0430\u043b\u0435\u043d\u0434\u0430\u0440\u044c", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"\u0421\u043e\u0437\u0434\u0430\u043d\u0438\u0435 \u043f\u0440\u043e\u0435\u043a\u0442\u0430", None))
        self.label_12.setText(QCoreApplication.translate("MainWindow", u"\u0421\u043e\u0437\u0434\u0430\u043d\u0438\u0435 \u0437\u0430\u0434\u0430\u0447\u0438", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"\u041f\u043e\u043b\u044c\u0437\u043e\u0432\u0430\u0442\u0435\u043b\u044c", None))
#if QT_CONFIG(tooltip)
        self.closeProfileBtn.setToolTip(QCoreApplication.translate("MainWindow", u"Close User", None))
#endif // QT_CONFIG(tooltip)
        self.closeProfileBtn.setText("")
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"\u041f\u0440\u043e\u0444\u0438\u043b\u044c", None))
        self.label_13.setText(QCoreApplication.translate("MainWindow", u"\u0410\u0432\u0442\u043e\u0440\u0438\u0437\u0430\u0446\u0438\u044f", None))
#if QT_CONFIG(tooltip)
        self.popupNotificationSubContainer.setToolTip(QCoreApplication.translate("MainWindow", u"Notification Message", None))
#endif // QT_CONFIG(tooltip)
        self.label_9.setText(QCoreApplication.translate("MainWindow", u"Notification", None))
        self.label_8.setText(QCoreApplication.translate("MainWindow", u"Notification Message", None))
#if QT_CONFIG(tooltip)
        self.closeNotificationBtn.setToolTip(QCoreApplication.translate("MainWindow", u"Close Notification", None))
#endif // QT_CONFIG(tooltip)
        self.closeNotificationBtn.setText("")
#if QT_CONFIG(tooltip)
        self.frame_13.setToolTip(QCoreApplication.translate("MainWindow", u"add project", None))
#endif // QT_CONFIG(tooltip)
        self.AddProjectBtn.setText(QCoreApplication.translate("MainWindow", u"\u041f\u0440\u043e\u0435\u043a\u0442", None))
#if QT_CONFIG(tooltip)
        self.AddTaskBtn.setToolTip(QCoreApplication.translate("MainWindow", u"add task", None))
#endif // QT_CONFIG(tooltip)
        self.AddTaskBtn.setText(QCoreApplication.translate("MainWindow", u"\u0417\u0430\u0434\u0430\u0447\u0430", None))
        self.label_11.setText("")
        self.toolBar.setWindowTitle(QCoreApplication.translate("MainWindow", u"toolBar", None))
    # retranslateUi

