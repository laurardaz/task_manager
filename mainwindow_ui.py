# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'mainwindow.ui'
##
## Created by: Qt User Interface Compiler version 6.2.4
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
from PySide6.QtWidgets import (QAbstractScrollArea, QApplication, QComboBox, QDateEdit,
    QFormLayout, QFrame, QGridLayout, QHBoxLayout,
    QHeaderView, QLabel, QLayout, QLineEdit,
    QMainWindow, QMenuBar, QPushButton, QScrollArea,
    QSizePolicy, QSpacerItem, QTabWidget, QTableWidget,
    QTableWidgetItem, QTextBrowser, QTextEdit, QToolBar,
    QVBoxLayout, QWidget)

from Custom_Widgets.Widgets import (QCustomSlideMenu, QCustomStackedWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1050, 718)
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
"#leftMenuSubContainer  QPushButton{\n"
"        text-align: left;\n"
"        padding: 10px 10px;\n"
"        border-top-left-radius: 10px;\n"
"        border-bottom-left-radius: 10px;\n"
"}\n"
"#headerContainer, #footerContainer{\n"
"        background-color: #25547B;\n"
"}\n"
"#profileSubContainer, #tasksTableWidget, #projectsTableWidget, QTabWidget{\n"
"        background-color: #25547B;\n"
"        border-radius: 10px;\n"
"}\n"
"#frame_7, #popupNotificationSubContainer, #popupAddNewContainer{\n"
"        background-color:#043C6B;\n"
"        border-radius: 10px;\n"
"}\n"
"QLineEdit, QComboBox, QTextEdit, QListWidget{\n"
"		 background-color: #043C6B;\n"
"		 padding: 5px 3px;\n"
"	"
                        "	 border-radius: 5px;\n"
"}\n"
"#btnAlready, #btnSignup, #btnNoAcc, #btnLogin, #save_task_btn, #save_project_btn, #addTaskToListBtn, #btn_changePassword, #btn_logout, #save_project_edit_btn, #save_task_edit_btn{\n"
"		 background-color: #043C6B;\n"
"		 padding: 10px 5px;\n"
"		 border-radius: 5px;\n"
"}\n"
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


        self.verticalLayout_2.addWidget(self.frame)

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
        icon1 = QIcon()
        icon1.addFile(u"icons/feather/layers.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.projectsBtn.setIcon(icon1)
        self.projectsBtn.setIconSize(QSize(24, 24))

        self.verticalLayout_3.addWidget(self.projectsBtn)

        self.tasksBtn = QPushButton(self.frame_3)
        self.tasksBtn.setObjectName(u"tasksBtn")
        icon2 = QIcon()
        icon2.addFile(u"icons/feather/file-text.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.tasksBtn.setIcon(icon2)
        self.tasksBtn.setIconSize(QSize(24, 24))

        self.verticalLayout_3.addWidget(self.tasksBtn)

        self.statisticsBtn = QPushButton(self.frame_3)
        self.statisticsBtn.setObjectName(u"statisticsBtn")
        icon3 = QIcon()
        icon3.addFile(u"icons/feather/activity.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.statisticsBtn.setIcon(icon3)
        self.statisticsBtn.setIconSize(QSize(24, 24))

        self.verticalLayout_3.addWidget(self.statisticsBtn)


        self.verticalLayout_2.addWidget(self.frame_3)

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


        self.verticalLayout_2.addWidget(self.frame_4)


        self.verticalLayout.addWidget(self.leftMenuSubContainer)


        self.horizontalLayout.addWidget(self.leftMenuContainer)

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
        icon4 = QIcon()
        icon4.addFile(u"icons/feather/search.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.pushButton_5.setIcon(icon4)
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
        icon5 = QIcon()
        icon5.addFile(u"icons/feather/bell.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.notificationBtn.setIcon(icon5)
        self.notificationBtn.setIconSize(QSize(24, 24))

        self.horizontalLayout_5.addWidget(self.notificationBtn)

        self.profileBtn = QPushButton(self.frame_5)
        self.profileBtn.setObjectName(u"profileBtn")
        icon6 = QIcon()
        icon6.addFile(u"icons/feather/user.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.profileBtn.setIcon(icon6)
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
        icon7 = QIcon()
        icon7.addFile(u"icons/feather/minus.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.minimizeBtn.setIcon(icon7)
        self.minimizeBtn.setIconSize(QSize(24, 24))

        self.horizontalLayout_3.addWidget(self.minimizeBtn)

        self.restoreBtn = QPushButton(self.frame_2)
        self.restoreBtn.setObjectName(u"restoreBtn")
        icon8 = QIcon()
        icon8.addFile(u"icons/feather/square.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.restoreBtn.setIcon(icon8)
        self.restoreBtn.setIconSize(QSize(24, 24))

        self.horizontalLayout_3.addWidget(self.restoreBtn)

        self.closeBtn = QPushButton(self.frame_2)
        self.closeBtn.setObjectName(u"closeBtn")
        icon9 = QIcon()
        icon9.addFile(u"icons/feather/x.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.closeBtn.setIcon(icon9)
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

        self.horizontalLayout_7.addWidget(self.mainContentsContainer)

        self.mainPages = QCustomStackedWidget(self.mainBodyContent)
        self.mainPages.setObjectName(u"mainPages")
        self.pageProjects = QWidget()
        self.pageProjects.setObjectName(u"pageProjects")
        self.verticalLayout_14 = QVBoxLayout(self.pageProjects)
        self.verticalLayout_14.setObjectName(u"verticalLayout_14")
        self.widget_2 = QWidget(self.pageProjects)
        self.widget_2.setObjectName(u"widget_2")
        self.verticalLayout_24 = QVBoxLayout(self.widget_2)
        self.verticalLayout_24.setObjectName(u"verticalLayout_24")
        self.tasks_lbl_3 = QLabel(self.widget_2)
        self.tasks_lbl_3.setObjectName(u"tasks_lbl_3")
        sizePolicy3 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        sizePolicy3.setHorizontalStretch(0)
        sizePolicy3.setVerticalStretch(0)
        sizePolicy3.setHeightForWidth(self.tasks_lbl_3.sizePolicy().hasHeightForWidth())
        self.tasks_lbl_3.setSizePolicy(sizePolicy3)
        font = QFont()
        font.setPointSize(13)
        self.tasks_lbl_3.setFont(font)
        self.tasks_lbl_3.setAlignment(Qt.AlignCenter)

        self.verticalLayout_24.addWidget(self.tasks_lbl_3)

        self.projectsTableWidget = QTableWidget(self.widget_2)
        if (self.projectsTableWidget.columnCount() < 7):
            self.projectsTableWidget.setColumnCount(7)
        __qtablewidgetitem = QTableWidgetItem()
        __qtablewidgetitem.setBackground(QColor(4, 60, 107));
        self.projectsTableWidget.setHorizontalHeaderItem(0, __qtablewidgetitem)
        __qtablewidgetitem1 = QTableWidgetItem()
        __qtablewidgetitem1.setBackground(QColor(4, 60, 107));
        self.projectsTableWidget.setHorizontalHeaderItem(1, __qtablewidgetitem1)
        __qtablewidgetitem2 = QTableWidgetItem()
        __qtablewidgetitem2.setBackground(QColor(4, 60, 107));
        self.projectsTableWidget.setHorizontalHeaderItem(2, __qtablewidgetitem2)
        __qtablewidgetitem3 = QTableWidgetItem()
        __qtablewidgetitem3.setBackground(QColor(4, 60, 107));
        self.projectsTableWidget.setHorizontalHeaderItem(3, __qtablewidgetitem3)
        __qtablewidgetitem4 = QTableWidgetItem()
        __qtablewidgetitem4.setBackground(QColor(4, 60, 107));
        self.projectsTableWidget.setHorizontalHeaderItem(4, __qtablewidgetitem4)
        __qtablewidgetitem5 = QTableWidgetItem()
        __qtablewidgetitem5.setBackground(QColor(4, 60, 107));
        self.projectsTableWidget.setHorizontalHeaderItem(5, __qtablewidgetitem5)
        __qtablewidgetitem6 = QTableWidgetItem()
        __qtablewidgetitem6.setBackground(QColor(4, 60, 107));
        self.projectsTableWidget.setHorizontalHeaderItem(6, __qtablewidgetitem6)
        self.projectsTableWidget.setObjectName(u"projectsTableWidget")
        sizePolicy2.setHeightForWidth(self.projectsTableWidget.sizePolicy().hasHeightForWidth())
        self.projectsTableWidget.setSizePolicy(sizePolicy2)
        self.projectsTableWidget.setMinimumSize(QSize(0, 0))
        self.projectsTableWidget.setMaximumSize(QSize(16777212, 16777215))
        self.projectsTableWidget.setAutoFillBackground(False)
        self.projectsTableWidget.setSizeAdjustPolicy(QAbstractScrollArea.AdjustIgnored)
        self.projectsTableWidget.setSortingEnabled(True)
        self.projectsTableWidget.horizontalHeader().setStretchLastSection(True)

        self.verticalLayout_24.addWidget(self.projectsTableWidget)

        self.scrollProjects = QScrollArea(self.widget_2)
        self.scrollProjects.setObjectName(u"scrollProjects")
        self.scrollProjects.setMinimumSize(QSize(0, 0))
        self.scrollProjects.setMaximumSize(QSize(16777215, 700))
        self.scrollProjects.setWidgetResizable(True)
        self.scrollWidgetProjects = QWidget()
        self.scrollWidgetProjects.setObjectName(u"scrollWidgetProjects")
        self.scrollWidgetProjects.setGeometry(QRect(0, 0, 599, 310))
        self.horizontalLayout_14 = QHBoxLayout(self.scrollWidgetProjects)
        self.horizontalLayout_14.setObjectName(u"horizontalLayout_14")
        self.TabWidgetProjects = QTabWidget(self.scrollWidgetProjects)
        self.TabWidgetProjects.setObjectName(u"TabWidgetProjects")
        self.tab_info_project = QWidget()
        self.tab_info_project.setObjectName(u"tab_info_project")
        self.verticalLayout_28 = QVBoxLayout(self.tab_info_project)
        self.verticalLayout_28.setObjectName(u"verticalLayout_28")
        self.lbl_name_prjct = QLabel(self.tab_info_project)
        self.lbl_name_prjct.setObjectName(u"lbl_name_prjct")

        self.verticalLayout_28.addWidget(self.lbl_name_prjct, 0, Qt.AlignHCenter)

        self.project_info_description = QTextBrowser(self.tab_info_project)
        self.project_info_description.setObjectName(u"project_info_description")
        self.project_info_description.setMaximumSize(QSize(16777215, 60))

        self.verticalLayout_28.addWidget(self.project_info_description)

        self.frame_17 = QFrame(self.tab_info_project)
        self.frame_17.setObjectName(u"frame_17")
        self.frame_17.setFrameShape(QFrame.StyledPanel)
        self.frame_17.setFrameShadow(QFrame.Raised)
        self.gridLayout_7 = QGridLayout(self.frame_17)
        self.gridLayout_7.setObjectName(u"gridLayout_7")
        self.start_date_project_info = QLabel(self.frame_17)
        self.start_date_project_info.setObjectName(u"start_date_project_info")

        self.gridLayout_7.addWidget(self.start_date_project_info, 1, 0, 1, 2, Qt.AlignHCenter)

        self.label_71 = QLabel(self.frame_17)
        self.label_71.setObjectName(u"label_71")

        self.gridLayout_7.addWidget(self.label_71, 0, 0, 1, 2, Qt.AlignHCenter|Qt.AlignVCenter)


        self.verticalLayout_28.addWidget(self.frame_17)

        self.verticalSpacer_11 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_28.addItem(self.verticalSpacer_11)

        self.TabWidgetProjects.addTab(self.tab_info_project, "")
        self.tab_add_project = QWidget()
        self.tab_add_project.setObjectName(u"tab_add_project")
        self.gridLayout_3 = QGridLayout(self.tab_add_project)
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.frame_14 = QFrame(self.tab_add_project)
        self.frame_14.setObjectName(u"frame_14")
        self.frame_14.setFrameShape(QFrame.StyledPanel)
        self.frame_14.setFrameShadow(QFrame.Raised)
        self.gridLayout_2 = QGridLayout(self.frame_14)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.end_date_project = QDateEdit(self.frame_14)
        self.end_date_project.setObjectName(u"end_date_project")

        self.gridLayout_2.addWidget(self.end_date_project, 4, 1, 2, 1)

        self.projectPriorityComboBox = QComboBox(self.frame_14)
        self.projectPriorityComboBox.addItem("")
        self.projectPriorityComboBox.addItem("")
        self.projectPriorityComboBox.addItem("")
        self.projectPriorityComboBox.setObjectName(u"projectPriorityComboBox")

        self.gridLayout_2.addWidget(self.projectPriorityComboBox, 4, 5, 1, 1)

        self.label_5 = QLabel(self.frame_14)
        self.label_5.setObjectName(u"label_5")

        self.gridLayout_2.addWidget(self.label_5, 2, 5, 1, 1)

        self.projectStatusComboBox = QComboBox(self.frame_14)
        self.projectStatusComboBox.addItem("")
        self.projectStatusComboBox.addItem("")
        self.projectStatusComboBox.addItem("")
        self.projectStatusComboBox.setObjectName(u"projectStatusComboBox")

        self.gridLayout_2.addWidget(self.projectStatusComboBox, 4, 4, 1, 1)

        self.from_time_pjt = QDateEdit(self.frame_14)
        self.from_time_pjt.setObjectName(u"from_time_pjt")
        self.from_time_pjt.setMaximumDateTime(QDateTime(QDate(9998, 12, 30), QTime(11, 59, 59)))
        self.from_time_pjt.setTimeSpec(Qt.UTC)

        self.gridLayout_2.addWidget(self.from_time_pjt, 4, 0, 2, 1)

        self.label_13 = QLabel(self.frame_14)
        self.label_13.setObjectName(u"label_13")

        self.gridLayout_2.addWidget(self.label_13, 2, 4, 1, 1)

        self.label_27 = QLabel(self.frame_14)
        self.label_27.setObjectName(u"label_27")

        self.gridLayout_2.addWidget(self.label_27, 2, 1, 1, 1)

        self.lbl_project_start = QLabel(self.frame_14)
        self.lbl_project_start.setObjectName(u"lbl_project_start")

        self.gridLayout_2.addWidget(self.lbl_project_start, 2, 0, 1, 1)


        self.gridLayout_3.addWidget(self.frame_14, 8, 0, 3, 5)

        self.project_name = QLineEdit(self.tab_add_project)
        self.project_name.setObjectName(u"project_name")

        self.gridLayout_3.addWidget(self.project_name, 2, 1, 1, 4)

        self.lbl_add_new_project = QLabel(self.tab_add_project)
        self.lbl_add_new_project.setObjectName(u"lbl_add_new_project")
        self.lbl_add_new_project.setAlignment(Qt.AlignCenter)

        self.gridLayout_3.addWidget(self.lbl_add_new_project, 0, 0, 1, 5)

        self.label_25 = QLabel(self.tab_add_project)
        self.label_25.setObjectName(u"label_25")

        self.gridLayout_3.addWidget(self.label_25, 2, 0, 1, 1)

        self.descriptionProject = QTextEdit(self.tab_add_project)
        self.descriptionProject.setObjectName(u"descriptionProject")
        self.descriptionProject.setMaximumSize(QSize(16777215, 50))

        self.gridLayout_3.addWidget(self.descriptionProject, 5, 0, 1, 5)

        self.save_project_btn = QPushButton(self.tab_add_project)
        self.save_project_btn.setObjectName(u"save_project_btn")

        self.gridLayout_3.addWidget(self.save_project_btn, 11, 0, 1, 5, Qt.AlignHCenter)

        self.lbl_description_project = QLabel(self.tab_add_project)
        self.lbl_description_project.setObjectName(u"lbl_description_project")

        self.gridLayout_3.addWidget(self.lbl_description_project, 4, 0, 1, 1)

        self.TabWidgetProjects.addTab(self.tab_add_project, "")
        self.tab_edit_project = QWidget()
        self.tab_edit_project.setObjectName(u"tab_edit_project")
        self.verticalLayout_23 = QVBoxLayout(self.tab_edit_project)
        self.verticalLayout_23.setObjectName(u"verticalLayout_23")
        self.project_name_edit = QLabel(self.tab_edit_project)
        self.project_name_edit.setObjectName(u"project_name_edit")

        self.verticalLayout_23.addWidget(self.project_name_edit, 0, Qt.AlignHCenter)

        self.widget_3 = QWidget(self.tab_edit_project)
        self.widget_3.setObjectName(u"widget_3")
        self.gridLayout_5 = QGridLayout(self.widget_3)
        self.gridLayout_5.setObjectName(u"gridLayout_5")
        self.lbl_project_status_ed = QLabel(self.widget_3)
        self.lbl_project_status_ed.setObjectName(u"lbl_project_status_ed")

        self.gridLayout_5.addWidget(self.lbl_project_status_ed, 0, 0, 1, 1)

        self.lbl_project_priority_ed = QLabel(self.widget_3)
        self.lbl_project_priority_ed.setObjectName(u"lbl_project_priority_ed")

        self.gridLayout_5.addWidget(self.lbl_project_priority_ed, 1, 0, 1, 1)

        self.lbl_project_end_date_ed = QLabel(self.widget_3)
        self.lbl_project_end_date_ed.setObjectName(u"lbl_project_end_date_ed")

        self.gridLayout_5.addWidget(self.lbl_project_end_date_ed, 2, 0, 1, 1)

        self.project_date_edit = QDateEdit(self.widget_3)
        self.project_date_edit.setObjectName(u"project_date_edit")

        self.gridLayout_5.addWidget(self.project_date_edit, 2, 1, 1, 1)

        self.project_status_edit = QComboBox(self.widget_3)
        self.project_status_edit.addItem("")
        self.project_status_edit.addItem("")
        self.project_status_edit.addItem("")
        self.project_status_edit.setObjectName(u"project_status_edit")

        self.gridLayout_5.addWidget(self.project_status_edit, 0, 1, 1, 1)

        self.project_priority_edit = QComboBox(self.widget_3)
        self.project_priority_edit.addItem("")
        self.project_priority_edit.addItem("")
        self.project_priority_edit.addItem("")
        self.project_priority_edit.setObjectName(u"project_priority_edit")

        self.gridLayout_5.addWidget(self.project_priority_edit, 1, 1, 1, 1)


        self.verticalLayout_23.addWidget(self.widget_3)

        self.save_project_edit_btn = QPushButton(self.tab_edit_project)
        self.save_project_edit_btn.setObjectName(u"save_project_edit_btn")

        self.verticalLayout_23.addWidget(self.save_project_edit_btn, 0, Qt.AlignHCenter)

        self.verticalSpacer_10 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_23.addItem(self.verticalSpacer_10)

        self.TabWidgetProjects.addTab(self.tab_edit_project, "")

        self.horizontalLayout_14.addWidget(self.TabWidgetProjects)

        self.scrollProjects.setWidget(self.scrollWidgetProjects)

        self.verticalLayout_24.addWidget(self.scrollProjects)


        self.verticalLayout_14.addWidget(self.widget_2)

        self.mainPages.addWidget(self.pageProjects)
        self.pageTasks = QWidget()
        self.pageTasks.setObjectName(u"pageTasks")
        self.verticalLayout_13 = QVBoxLayout(self.pageTasks)
        self.verticalLayout_13.setObjectName(u"verticalLayout_13")
        self.widget = QWidget(self.pageTasks)
        self.widget.setObjectName(u"widget")
        self.verticalLayout_17 = QVBoxLayout(self.widget)
        self.verticalLayout_17.setObjectName(u"verticalLayout_17")
        self.tasks_lbl = QLabel(self.widget)
        self.tasks_lbl.setObjectName(u"tasks_lbl")
        sizePolicy3.setHeightForWidth(self.tasks_lbl.sizePolicy().hasHeightForWidth())
        self.tasks_lbl.setSizePolicy(sizePolicy3)
        self.tasks_lbl.setFont(font)
        self.tasks_lbl.setAlignment(Qt.AlignCenter)

        self.verticalLayout_17.addWidget(self.tasks_lbl)

        self.tasksTableWidget = QTableWidget(self.widget)
        if (self.tasksTableWidget.columnCount() < 6):
            self.tasksTableWidget.setColumnCount(6)
        __qtablewidgetitem7 = QTableWidgetItem()
        __qtablewidgetitem7.setBackground(QColor(4, 60, 107));
        self.tasksTableWidget.setHorizontalHeaderItem(0, __qtablewidgetitem7)
        __qtablewidgetitem8 = QTableWidgetItem()
        __qtablewidgetitem8.setBackground(QColor(4, 60, 107));
        self.tasksTableWidget.setHorizontalHeaderItem(1, __qtablewidgetitem8)
        __qtablewidgetitem9 = QTableWidgetItem()
        __qtablewidgetitem9.setBackground(QColor(4, 60, 107));
        self.tasksTableWidget.setHorizontalHeaderItem(2, __qtablewidgetitem9)
        __qtablewidgetitem10 = QTableWidgetItem()
        __qtablewidgetitem10.setBackground(QColor(4, 60, 107));
        self.tasksTableWidget.setHorizontalHeaderItem(3, __qtablewidgetitem10)
        __qtablewidgetitem11 = QTableWidgetItem()
        __qtablewidgetitem11.setBackground(QColor(4, 60, 107));
        self.tasksTableWidget.setHorizontalHeaderItem(4, __qtablewidgetitem11)
        __qtablewidgetitem12 = QTableWidgetItem()
        __qtablewidgetitem12.setBackground(QColor(4, 60, 107));
        self.tasksTableWidget.setHorizontalHeaderItem(5, __qtablewidgetitem12)
        self.tasksTableWidget.setObjectName(u"tasksTableWidget")
        sizePolicy2.setHeightForWidth(self.tasksTableWidget.sizePolicy().hasHeightForWidth())
        self.tasksTableWidget.setSizePolicy(sizePolicy2)
        self.tasksTableWidget.setMinimumSize(QSize(0, 0))
        self.tasksTableWidget.setMaximumSize(QSize(16777212, 16777215))
        self.tasksTableWidget.setSizeAdjustPolicy(QAbstractScrollArea.AdjustIgnored)
        self.tasksTableWidget.setSortingEnabled(True)
        self.tasksTableWidget.horizontalHeader().setStretchLastSection(True)

        self.verticalLayout_17.addWidget(self.tasksTableWidget)

        self.scrollTasks = QScrollArea(self.widget)
        self.scrollTasks.setObjectName(u"scrollTasks")
        self.scrollTasks.setMinimumSize(QSize(0, 0))
        self.scrollTasks.setMaximumSize(QSize(16777215, 300))
        self.scrollTasks.setWidgetResizable(True)
        self.scrollWidgetTasks = QWidget()
        self.scrollWidgetTasks.setObjectName(u"scrollWidgetTasks")
        self.scrollWidgetTasks.setGeometry(QRect(0, 0, 599, 352))
        self.horizontalLayout_12 = QHBoxLayout(self.scrollWidgetTasks)
        self.horizontalLayout_12.setObjectName(u"horizontalLayout_12")
        self.tabWidgetTasks = QTabWidget(self.scrollWidgetTasks)
        self.tabWidgetTasks.setObjectName(u"tabWidgetTasks")
        self.tab_info_task = QWidget()
        self.tab_info_task.setObjectName(u"tab_info_task")
        self.verticalLayout_25 = QVBoxLayout(self.tab_info_task)
        self.verticalLayout_25.setObjectName(u"verticalLayout_25")
        self.lbl_name_tsk = QLabel(self.tab_info_task)
        self.lbl_name_tsk.setObjectName(u"lbl_name_tsk")

        self.verticalLayout_25.addWidget(self.lbl_name_tsk, 0, Qt.AlignHCenter)

        self.textBrowser_2 = QTextBrowser(self.tab_info_task)
        self.textBrowser_2.setObjectName(u"textBrowser_2")
        self.textBrowser_2.setMaximumSize(QSize(16777215, 60))

        self.verticalLayout_25.addWidget(self.textBrowser_2)

        self.frame_18 = QFrame(self.tab_info_task)
        self.frame_18.setObjectName(u"frame_18")
        self.frame_18.setFrameShape(QFrame.StyledPanel)
        self.frame_18.setFrameShadow(QFrame.Raised)
        self.gridLayout_6 = QGridLayout(self.frame_18)
        self.gridLayout_6.setObjectName(u"gridLayout_6")
        self.label_68 = QLabel(self.frame_18)
        self.label_68.setObjectName(u"label_68")

        self.gridLayout_6.addWidget(self.label_68, 0, 0, 1, 1, Qt.AlignHCenter)

        self.start_date_task_info = QLabel(self.frame_18)
        self.start_date_task_info.setObjectName(u"start_date_task_info")

        self.gridLayout_6.addWidget(self.start_date_task_info, 1, 0, 1, 1, Qt.AlignHCenter)


        self.verticalLayout_25.addWidget(self.frame_18)

        self.verticalSpacer_12 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_25.addItem(self.verticalSpacer_12)

        self.tabWidgetTasks.addTab(self.tab_info_task, "")
        self.tab_add_task = QWidget()
        self.tab_add_task.setObjectName(u"tab_add_task")
        self.gridLayout = QGridLayout(self.tab_add_task)
        self.gridLayout.setObjectName(u"gridLayout")
        self.label_18 = QLabel(self.tab_add_task)
        self.label_18.setObjectName(u"label_18")

        self.gridLayout.addWidget(self.label_18, 2, 0, 1, 1)

        self.save_task_btn = QPushButton(self.tab_add_task)
        self.save_task_btn.setObjectName(u"save_task_btn")

        self.gridLayout.addWidget(self.save_task_btn, 13, 0, 1, 7, Qt.AlignHCenter)

        self.label_17 = QLabel(self.tab_add_task)
        self.label_17.setObjectName(u"label_17")

        self.gridLayout.addWidget(self.label_17, 5, 0, 1, 1)

        self.label_16 = QLabel(self.tab_add_task)
        self.label_16.setObjectName(u"label_16")
        self.label_16.setAlignment(Qt.AlignCenter)

        self.gridLayout.addWidget(self.label_16, 0, 0, 1, 6)

        self.task_name_input = QLineEdit(self.tab_add_task)
        self.task_name_input.setObjectName(u"task_name_input")

        self.gridLayout.addWidget(self.task_name_input, 2, 1, 1, 6)

        self.descriptionTask = QTextEdit(self.tab_add_task)
        self.descriptionTask.setObjectName(u"descriptionTask")
        self.descriptionTask.setMaximumSize(QSize(16777215, 50))

        self.gridLayout.addWidget(self.descriptionTask, 6, 0, 1, 7)

        self.label_addTo = QLabel(self.tab_add_task)
        self.label_addTo.setObjectName(u"label_addTo")

        self.gridLayout.addWidget(self.label_addTo, 4, 0, 1, 1)

        self.choose_project_comboBox = QComboBox(self.tab_add_task)
        self.choose_project_comboBox.setObjectName(u"choose_project_comboBox")

        self.gridLayout.addWidget(self.choose_project_comboBox, 4, 1, 1, 6)

        self.frame_19 = QFrame(self.tab_add_task)
        self.frame_19.setObjectName(u"frame_19")
        self.frame_19.setFrameShape(QFrame.StyledPanel)
        self.frame_19.setFrameShadow(QFrame.Raised)
        self.gridLayout_8 = QGridLayout(self.frame_19)
        self.gridLayout_8.setObjectName(u"gridLayout_8")
        self.taskPriorityComboBox = QComboBox(self.frame_19)
        self.taskPriorityComboBox.addItem("")
        self.taskPriorityComboBox.addItem("")
        self.taskPriorityComboBox.addItem("")
        self.taskPriorityComboBox.setObjectName(u"taskPriorityComboBox")

        self.gridLayout_8.addWidget(self.taskPriorityComboBox, 6, 4, 1, 1)

        self.from_time_tsk = QDateEdit(self.frame_19)
        self.from_time_tsk.setObjectName(u"from_time_tsk")

        self.gridLayout_8.addWidget(self.from_time_tsk, 6, 0, 1, 1)

        self.taskStatusComboBox = QComboBox(self.frame_19)
        self.taskStatusComboBox.addItem("")
        self.taskStatusComboBox.addItem("")
        self.taskStatusComboBox.addItem("")
        self.taskStatusComboBox.setObjectName(u"taskStatusComboBox")

        self.gridLayout_8.addWidget(self.taskStatusComboBox, 6, 3, 1, 1)

        self.label_2 = QLabel(self.frame_19)
        self.label_2.setObjectName(u"label_2")

        self.gridLayout_8.addWidget(self.label_2, 2, 4, 1, 1)

        self.label_22 = QLabel(self.frame_19)
        self.label_22.setObjectName(u"label_22")

        self.gridLayout_8.addWidget(self.label_22, 2, 3, 1, 1)

        self.to_time_tsk = QDateEdit(self.frame_19)
        self.to_time_tsk.setObjectName(u"to_time_tsk")

        self.gridLayout_8.addWidget(self.to_time_tsk, 6, 1, 1, 1)

        self.label_19 = QLabel(self.frame_19)
        self.label_19.setObjectName(u"label_19")

        self.gridLayout_8.addWidget(self.label_19, 2, 1, 1, 1)

        self.From_lbl = QLabel(self.frame_19)
        self.From_lbl.setObjectName(u"From_lbl")

        self.gridLayout_8.addWidget(self.From_lbl, 2, 0, 1, 1)


        self.gridLayout.addWidget(self.frame_19, 9, 0, 4, 7)

        self.verticalSpacer_13 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.gridLayout.addItem(self.verticalSpacer_13, 14, 0, 1, 1)

        self.tabWidgetTasks.addTab(self.tab_add_task, "")
        self.tab_edit_task = QWidget()
        self.tab_edit_task.setObjectName(u"tab_edit_task")
        self.verticalLayout_21 = QVBoxLayout(self.tab_edit_task)
        self.verticalLayout_21.setObjectName(u"verticalLayout_21")
        self.task_name_edit = QLabel(self.tab_edit_task)
        self.task_name_edit.setObjectName(u"task_name_edit")

        self.verticalLayout_21.addWidget(self.task_name_edit, 0, Qt.AlignHCenter|Qt.AlignTop)

        self.widget_4 = QWidget(self.tab_edit_task)
        self.widget_4.setObjectName(u"widget_4")
        self.gridLayout_4 = QGridLayout(self.widget_4)
        self.gridLayout_4.setObjectName(u"gridLayout_4")
        self.lb_task_status_ed = QLabel(self.widget_4)
        self.lb_task_status_ed.setObjectName(u"lb_task_status_ed")

        self.gridLayout_4.addWidget(self.lb_task_status_ed, 0, 0, 1, 1)

        self.lbl_task_priority_ed = QLabel(self.widget_4)
        self.lbl_task_priority_ed.setObjectName(u"lbl_task_priority_ed")

        self.gridLayout_4.addWidget(self.lbl_task_priority_ed, 1, 0, 1, 1)

        self.lbl_task_end_time_ed = QLabel(self.widget_4)
        self.lbl_task_end_time_ed.setObjectName(u"lbl_task_end_time_ed")

        self.gridLayout_4.addWidget(self.lbl_task_end_time_ed, 2, 0, 1, 1)

        self.task_end_date_edit = QDateEdit(self.widget_4)
        self.task_end_date_edit.setObjectName(u"task_end_date_edit")

        self.gridLayout_4.addWidget(self.task_end_date_edit, 2, 1, 1, 1)

        self.task_status_edit = QComboBox(self.widget_4)
        self.task_status_edit.addItem("")
        self.task_status_edit.addItem("")
        self.task_status_edit.addItem("")
        self.task_status_edit.setObjectName(u"task_status_edit")

        self.gridLayout_4.addWidget(self.task_status_edit, 0, 1, 1, 1)

        self.task_priority_edit = QComboBox(self.widget_4)
        self.task_priority_edit.addItem("")
        self.task_priority_edit.addItem("")
        self.task_priority_edit.addItem("")
        self.task_priority_edit.setObjectName(u"task_priority_edit")

        self.gridLayout_4.addWidget(self.task_priority_edit, 1, 1, 1, 1)


        self.verticalLayout_21.addWidget(self.widget_4, 0, Qt.AlignTop)

        self.save_task_edit_btn = QPushButton(self.tab_edit_task)
        self.save_task_edit_btn.setObjectName(u"save_task_edit_btn")

        self.verticalLayout_21.addWidget(self.save_task_edit_btn, 0, Qt.AlignHCenter)

        self.verticalSpacer_9 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_21.addItem(self.verticalSpacer_9)

        self.tabWidgetTasks.addTab(self.tab_edit_task, "")

        self.horizontalLayout_12.addWidget(self.tabWidgetTasks)

        self.scrollTasks.setWidget(self.scrollWidgetTasks)

        self.verticalLayout_17.addWidget(self.scrollTasks)


        self.verticalLayout_13.addWidget(self.widget)

        self.mainPages.addWidget(self.pageTasks)
        self.pageStatistics = QWidget()
        self.pageStatistics.setObjectName(u"pageStatistics")
        self.verticalLayout_12 = QVBoxLayout(self.pageStatistics)
        self.verticalLayout_12.setObjectName(u"verticalLayout_12")
        self.label_14 = QLabel(self.pageStatistics)
        self.label_14.setObjectName(u"label_14")
        self.label_14.setFont(font)

        self.verticalLayout_12.addWidget(self.label_14, 0, Qt.AlignHCenter|Qt.AlignTop)

        self.label_4 = QLabel(self.pageStatistics)
        self.label_4.setObjectName(u"label_4")

        self.verticalLayout_12.addWidget(self.label_4)

        self.label_62 = QLabel(self.pageStatistics)
        self.label_62.setObjectName(u"label_62")

        self.verticalLayout_12.addWidget(self.label_62)

        self.frame_13 = QFrame(self.pageStatistics)
        self.frame_13.setObjectName(u"frame_13")
        self.frame_13.setFrameShape(QFrame.StyledPanel)
        self.frame_13.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_16 = QHBoxLayout(self.frame_13)
        self.horizontalLayout_16.setObjectName(u"horizontalLayout_16")
        self.tabWidgetTasks_2 = QTabWidget(self.frame_13)
        self.tabWidgetTasks_2.setObjectName(u"tabWidgetTasks_2")
        self.dayProjects = QWidget()
        self.dayProjects.setObjectName(u"dayProjects")
        self.formLayout_8 = QFormLayout(self.dayProjects)
        self.formLayout_8.setObjectName(u"formLayout_8")
        self.label_addTo_6 = QLabel(self.dayProjects)
        self.label_addTo_6.setObjectName(u"label_addTo_6")
        font1 = QFont()
        font1.setPointSize(15)
        self.label_addTo_6.setFont(font1)

        self.formLayout_8.setWidget(0, QFormLayout.LabelRole, self.label_addTo_6)

        self.project_day_todo = QLabel(self.dayProjects)
        self.project_day_todo.setObjectName(u"project_day_todo")
        self.project_day_todo.setFont(font1)

        self.formLayout_8.setWidget(0, QFormLayout.FieldRole, self.project_day_todo)

        self.label_45 = QLabel(self.dayProjects)
        self.label_45.setObjectName(u"label_45")
        self.label_45.setFont(font1)

        self.formLayout_8.setWidget(1, QFormLayout.LabelRole, self.label_45)

        self.project_day_in_progress = QLabel(self.dayProjects)
        self.project_day_in_progress.setObjectName(u"project_day_in_progress")
        self.project_day_in_progress.setFont(font1)

        self.formLayout_8.setWidget(1, QFormLayout.FieldRole, self.project_day_in_progress)

        self.label_43 = QLabel(self.dayProjects)
        self.label_43.setObjectName(u"label_43")
        self.label_43.setFont(font1)

        self.formLayout_8.setWidget(2, QFormLayout.LabelRole, self.label_43)

        self.project_day_done = QLabel(self.dayProjects)
        self.project_day_done.setObjectName(u"project_day_done")
        self.project_day_done.setFont(font1)

        self.formLayout_8.setWidget(2, QFormLayout.FieldRole, self.project_day_done)

        self.tabWidgetTasks_2.addTab(self.dayProjects, "")
        self.weekProjects = QWidget()
        self.weekProjects.setObjectName(u"weekProjects")
        self.formLayout_7 = QFormLayout(self.weekProjects)
        self.formLayout_7.setObjectName(u"formLayout_7")
        self.label_addTo_7 = QLabel(self.weekProjects)
        self.label_addTo_7.setObjectName(u"label_addTo_7")
        self.label_addTo_7.setFont(font1)

        self.formLayout_7.setWidget(0, QFormLayout.LabelRole, self.label_addTo_7)

        self.project_week_todo = QLabel(self.weekProjects)
        self.project_week_todo.setObjectName(u"project_week_todo")
        self.project_week_todo.setFont(font1)

        self.formLayout_7.setWidget(0, QFormLayout.FieldRole, self.project_week_todo)

        self.label_49 = QLabel(self.weekProjects)
        self.label_49.setObjectName(u"label_49")
        self.label_49.setFont(font1)

        self.formLayout_7.setWidget(1, QFormLayout.LabelRole, self.label_49)

        self.project_week_in_progress = QLabel(self.weekProjects)
        self.project_week_in_progress.setObjectName(u"project_week_in_progress")
        self.project_week_in_progress.setFont(font1)

        self.formLayout_7.setWidget(1, QFormLayout.FieldRole, self.project_week_in_progress)

        self.label_47 = QLabel(self.weekProjects)
        self.label_47.setObjectName(u"label_47")
        self.label_47.setFont(font1)

        self.formLayout_7.setWidget(2, QFormLayout.LabelRole, self.label_47)

        self.project_week_done = QLabel(self.weekProjects)
        self.project_week_done.setObjectName(u"project_week_done")
        self.project_week_done.setFont(font1)

        self.formLayout_7.setWidget(2, QFormLayout.FieldRole, self.project_week_done)

        self.tabWidgetTasks_2.addTab(self.weekProjects, "")
        self.monthProjects = QWidget()
        self.monthProjects.setObjectName(u"monthProjects")
        self.formLayout_6 = QFormLayout(self.monthProjects)
        self.formLayout_6.setObjectName(u"formLayout_6")
        self.label_addTo_8 = QLabel(self.monthProjects)
        self.label_addTo_8.setObjectName(u"label_addTo_8")
        self.label_addTo_8.setFont(font1)

        self.formLayout_6.setWidget(0, QFormLayout.LabelRole, self.label_addTo_8)

        self.project_month_todo = QLabel(self.monthProjects)
        self.project_month_todo.setObjectName(u"project_month_todo")
        self.project_month_todo.setFont(font1)

        self.formLayout_6.setWidget(0, QFormLayout.FieldRole, self.project_month_todo)

        self.label_53 = QLabel(self.monthProjects)
        self.label_53.setObjectName(u"label_53")
        self.label_53.setFont(font1)

        self.formLayout_6.setWidget(1, QFormLayout.LabelRole, self.label_53)

        self.project_month_in_progress = QLabel(self.monthProjects)
        self.project_month_in_progress.setObjectName(u"project_month_in_progress")
        self.project_month_in_progress.setFont(font1)

        self.formLayout_6.setWidget(1, QFormLayout.FieldRole, self.project_month_in_progress)

        self.label_51 = QLabel(self.monthProjects)
        self.label_51.setObjectName(u"label_51")
        self.label_51.setFont(font1)

        self.formLayout_6.setWidget(2, QFormLayout.LabelRole, self.label_51)

        self.project_month_done = QLabel(self.monthProjects)
        self.project_month_done.setObjectName(u"project_month_done")
        self.project_month_done.setFont(font1)

        self.formLayout_6.setWidget(2, QFormLayout.FieldRole, self.project_month_done)

        self.tabWidgetTasks_2.addTab(self.monthProjects, "")
        self.yearProjects = QWidget()
        self.yearProjects.setObjectName(u"yearProjects")
        self.formLayout_5 = QFormLayout(self.yearProjects)
        self.formLayout_5.setObjectName(u"formLayout_5")
        self.label_addTo_9 = QLabel(self.yearProjects)
        self.label_addTo_9.setObjectName(u"label_addTo_9")
        self.label_addTo_9.setFont(font1)

        self.formLayout_5.setWidget(0, QFormLayout.LabelRole, self.label_addTo_9)

        self.project_year_todo = QLabel(self.yearProjects)
        self.project_year_todo.setObjectName(u"project_year_todo")
        self.project_year_todo.setFont(font1)

        self.formLayout_5.setWidget(0, QFormLayout.FieldRole, self.project_year_todo)

        self.label_57 = QLabel(self.yearProjects)
        self.label_57.setObjectName(u"label_57")
        self.label_57.setFont(font1)

        self.formLayout_5.setWidget(1, QFormLayout.LabelRole, self.label_57)

        self.project_year_in_progress = QLabel(self.yearProjects)
        self.project_year_in_progress.setObjectName(u"project_year_in_progress")
        self.project_year_in_progress.setFont(font1)

        self.formLayout_5.setWidget(1, QFormLayout.FieldRole, self.project_year_in_progress)

        self.label_55 = QLabel(self.yearProjects)
        self.label_55.setObjectName(u"label_55")
        self.label_55.setFont(font1)

        self.formLayout_5.setWidget(2, QFormLayout.LabelRole, self.label_55)

        self.project_year_done = QLabel(self.yearProjects)
        self.project_year_done.setObjectName(u"project_year_done")
        self.project_year_done.setFont(font1)

        self.formLayout_5.setWidget(2, QFormLayout.FieldRole, self.project_year_done)

        self.tabWidgetTasks_2.addTab(self.yearProjects, "")

        self.horizontalLayout_16.addWidget(self.tabWidgetTasks_2)


        self.verticalLayout_12.addWidget(self.frame_13)

        self.label_15 = QLabel(self.pageStatistics)
        self.label_15.setObjectName(u"label_15")

        self.verticalLayout_12.addWidget(self.label_15)

        self.label_63 = QLabel(self.pageStatistics)
        self.label_63.setObjectName(u"label_63")

        self.verticalLayout_12.addWidget(self.label_63)

        self.frame_10 = QFrame(self.pageStatistics)
        self.frame_10.setObjectName(u"frame_10")
        self.frame_10.setFrameShape(QFrame.StyledPanel)
        self.frame_10.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_15 = QHBoxLayout(self.frame_10)
        self.horizontalLayout_15.setObjectName(u"horizontalLayout_15")
        self.tabWidgetTasks_3 = QTabWidget(self.frame_10)
        self.tabWidgetTasks_3.setObjectName(u"tabWidgetTasks_3")
        font2 = QFont()
        font2.setPointSize(10)
        self.tabWidgetTasks_3.setFont(font2)
        self.dayTasks = QWidget()
        self.dayTasks.setObjectName(u"dayTasks")
        self.formLayout_2 = QFormLayout(self.dayTasks)
        self.formLayout_2.setObjectName(u"formLayout_2")
        self.label_addTo_4 = QLabel(self.dayTasks)
        self.label_addTo_4.setObjectName(u"label_addTo_4")
        self.label_addTo_4.setFont(font1)

        self.formLayout_2.setWidget(0, QFormLayout.LabelRole, self.label_addTo_4)

        self.task_day_todo = QLabel(self.dayTasks)
        self.task_day_todo.setObjectName(u"task_day_todo")
        self.task_day_todo.setFont(font1)

        self.formLayout_2.setWidget(0, QFormLayout.FieldRole, self.task_day_todo)

        self.label_39 = QLabel(self.dayTasks)
        self.label_39.setObjectName(u"label_39")
        self.label_39.setFont(font1)

        self.formLayout_2.setWidget(1, QFormLayout.LabelRole, self.label_39)

        self.task_day_in_progress = QLabel(self.dayTasks)
        self.task_day_in_progress.setObjectName(u"task_day_in_progress")
        self.task_day_in_progress.setFont(font1)

        self.formLayout_2.setWidget(1, QFormLayout.FieldRole, self.task_day_in_progress)

        self.label_37 = QLabel(self.dayTasks)
        self.label_37.setObjectName(u"label_37")
        self.label_37.setFont(font1)

        self.formLayout_2.setWidget(2, QFormLayout.LabelRole, self.label_37)

        self.task_day_done = QLabel(self.dayTasks)
        self.task_day_done.setObjectName(u"task_day_done")
        self.task_day_done.setFont(font1)

        self.formLayout_2.setWidget(2, QFormLayout.FieldRole, self.task_day_done)

        self.tabWidgetTasks_3.addTab(self.dayTasks, "")
        self.weekTasks = QWidget()
        self.weekTasks.setObjectName(u"weekTasks")
        self.formLayout = QFormLayout(self.weekTasks)
        self.formLayout.setObjectName(u"formLayout")
        self.label_addTo_2 = QLabel(self.weekTasks)
        self.label_addTo_2.setObjectName(u"label_addTo_2")
        self.label_addTo_2.setFont(font1)

        self.formLayout.setWidget(0, QFormLayout.LabelRole, self.label_addTo_2)

        self.task_week_todo = QLabel(self.weekTasks)
        self.task_week_todo.setObjectName(u"task_week_todo")
        self.task_week_todo.setFont(font1)

        self.formLayout.setWidget(0, QFormLayout.FieldRole, self.task_week_todo)

        self.label_20 = QLabel(self.weekTasks)
        self.label_20.setObjectName(u"label_20")
        self.label_20.setFont(font1)

        self.formLayout.setWidget(1, QFormLayout.LabelRole, self.label_20)

        self.task_week_in_progress = QLabel(self.weekTasks)
        self.task_week_in_progress.setObjectName(u"task_week_in_progress")
        self.task_week_in_progress.setFont(font1)

        self.formLayout.setWidget(1, QFormLayout.FieldRole, self.task_week_in_progress)

        self.label_21 = QLabel(self.weekTasks)
        self.label_21.setObjectName(u"label_21")
        self.label_21.setFont(font1)

        self.formLayout.setWidget(2, QFormLayout.LabelRole, self.label_21)

        self.task_week_done = QLabel(self.weekTasks)
        self.task_week_done.setObjectName(u"task_week_done")
        self.task_week_done.setFont(font1)

        self.formLayout.setWidget(2, QFormLayout.FieldRole, self.task_week_done)

        self.tabWidgetTasks_3.addTab(self.weekTasks, "")
        self.monthTasks = QWidget()
        self.monthTasks.setObjectName(u"monthTasks")
        self.formLayout_3 = QFormLayout(self.monthTasks)
        self.formLayout_3.setObjectName(u"formLayout_3")
        self.label_addTo_3 = QLabel(self.monthTasks)
        self.label_addTo_3.setObjectName(u"label_addTo_3")
        self.label_addTo_3.setFont(font1)

        self.formLayout_3.setWidget(0, QFormLayout.LabelRole, self.label_addTo_3)

        self.task_month_todo = QLabel(self.monthTasks)
        self.task_month_todo.setObjectName(u"task_month_todo")
        self.task_month_todo.setFont(font1)

        self.formLayout_3.setWidget(0, QFormLayout.FieldRole, self.task_month_todo)

        self.label_29 = QLabel(self.monthTasks)
        self.label_29.setObjectName(u"label_29")
        self.label_29.setFont(font1)

        self.formLayout_3.setWidget(1, QFormLayout.LabelRole, self.label_29)

        self.task_month_in_progress = QLabel(self.monthTasks)
        self.task_month_in_progress.setObjectName(u"task_month_in_progress")
        self.task_month_in_progress.setFont(font1)

        self.formLayout_3.setWidget(1, QFormLayout.FieldRole, self.task_month_in_progress)

        self.label_28 = QLabel(self.monthTasks)
        self.label_28.setObjectName(u"label_28")
        self.label_28.setFont(font1)

        self.formLayout_3.setWidget(2, QFormLayout.LabelRole, self.label_28)

        self.task_month_done = QLabel(self.monthTasks)
        self.task_month_done.setObjectName(u"task_month_done")
        self.task_month_done.setFont(font1)

        self.formLayout_3.setWidget(2, QFormLayout.FieldRole, self.task_month_done)

        self.tabWidgetTasks_3.addTab(self.monthTasks, "")
        self.yearTasks = QWidget()
        self.yearTasks.setObjectName(u"yearTasks")
        self.formLayout_4 = QFormLayout(self.yearTasks)
        self.formLayout_4.setObjectName(u"formLayout_4")
        self.label_addTo_5 = QLabel(self.yearTasks)
        self.label_addTo_5.setObjectName(u"label_addTo_5")
        self.label_addTo_5.setFont(font1)

        self.formLayout_4.setWidget(0, QFormLayout.LabelRole, self.label_addTo_5)

        self.task_year_todo = QLabel(self.yearTasks)
        self.task_year_todo.setObjectName(u"task_year_todo")
        self.task_year_todo.setFont(font1)

        self.formLayout_4.setWidget(0, QFormLayout.FieldRole, self.task_year_todo)

        self.label_42 = QLabel(self.yearTasks)
        self.label_42.setObjectName(u"label_42")
        self.label_42.setFont(font1)

        self.formLayout_4.setWidget(1, QFormLayout.LabelRole, self.label_42)

        self.task_year_in_progress = QLabel(self.yearTasks)
        self.task_year_in_progress.setObjectName(u"task_year_in_progress")
        self.task_year_in_progress.setFont(font1)

        self.formLayout_4.setWidget(1, QFormLayout.FieldRole, self.task_year_in_progress)

        self.label_31 = QLabel(self.yearTasks)
        self.label_31.setObjectName(u"label_31")
        self.label_31.setFont(font1)

        self.formLayout_4.setWidget(2, QFormLayout.LabelRole, self.label_31)

        self.task_year_done = QLabel(self.yearTasks)
        self.task_year_done.setObjectName(u"task_year_done")
        self.task_year_done.setFont(font1)

        self.formLayout_4.setWidget(2, QFormLayout.FieldRole, self.task_year_done)

        self.tabWidgetTasks_3.addTab(self.yearTasks, "")

        self.horizontalLayout_15.addWidget(self.tabWidgetTasks_3)


        self.verticalLayout_12.addWidget(self.frame_10)

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
        self.verticalLayout_22 = QVBoxLayout(self.pageCreateNewTask)
        self.verticalLayout_22.setObjectName(u"verticalLayout_22")
        self.label_12 = QLabel(self.pageCreateNewTask)
        self.label_12.setObjectName(u"label_12")
        self.label_12.setFont(font)
        self.label_12.setAlignment(Qt.AlignCenter)

        self.verticalLayout_22.addWidget(self.label_12)

        self.mainPages.addWidget(self.pageCreateNewTask)

        self.horizontalLayout_7.addWidget(self.mainPages)

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
        icon10 = QIcon()
        icon10.addFile(u"icons/feather/x-circle.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.closeProfileBtn.setIcon(icon10)
        self.closeProfileBtn.setIconSize(QSize(24, 24))

        self.horizontalLayout_8.addWidget(self.closeProfileBtn, 0, Qt.AlignRight)


        self.verticalLayout_7.addWidget(self.frame_7)

        self.profileStackedWidget = QCustomStackedWidget(self.profileSubContainer)
        self.profileStackedWidget.setObjectName(u"profileStackedWidget")
        self.profileStackedWidget.setEnabled(True)
        sizePolicy6 = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Preferred)
        sizePolicy6.setHorizontalStretch(0)
        sizePolicy6.setVerticalStretch(0)
        sizePolicy6.setHeightForWidth(self.profileStackedWidget.sizePolicy().hasHeightForWidth())
        self.profileStackedWidget.setSizePolicy(sizePolicy6)
        self.profileStackedWidget.setMaximumSize(QSize(16777215, 16777215))
        self.profileStackedWidget.setLayoutDirection(Qt.LeftToRight)
        self.register_page = QWidget()
        self.register_page.setObjectName(u"register_page")
        self.verticalLayout_8 = QVBoxLayout(self.register_page)
        self.verticalLayout_8.setObjectName(u"verticalLayout_8")
        self.pic_user_plus = QLabel(self.register_page)
        self.pic_user_plus.setObjectName(u"pic_user_plus")
        sizePolicy7 = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Fixed)
        sizePolicy7.setHorizontalStretch(0)
        sizePolicy7.setVerticalStretch(0)
        sizePolicy7.setHeightForWidth(self.pic_user_plus.sizePolicy().hasHeightForWidth())
        self.pic_user_plus.setSizePolicy(sizePolicy7)
        self.pic_user_plus.setMinimumSize(QSize(50, 50))
        self.pic_user_plus.setMaximumSize(QSize(50, 50))
        self.pic_user_plus.setPixmap(QPixmap(u"icons/feather/user-plus.svg"))
        self.pic_user_plus.setScaledContents(True)
        self.pic_user_plus.setAlignment(Qt.AlignCenter)

        self.verticalLayout_8.addWidget(self.pic_user_plus, 0, Qt.AlignHCenter)

        self.label_signup_reg = QLabel(self.register_page)
        self.label_signup_reg.setObjectName(u"label_signup_reg")
        self.label_signup_reg.setEnabled(False)
        sizePolicy7.setHeightForWidth(self.label_signup_reg.sizePolicy().hasHeightForWidth())
        self.label_signup_reg.setSizePolicy(sizePolicy7)
        font3 = QFont()
        font3.setPointSize(13)
        font3.setBold(True)
        self.label_signup_reg.setFont(font3)
        self.label_signup_reg.setScaledContents(False)
        self.label_signup_reg.setAlignment(Qt.AlignCenter)

        self.verticalLayout_8.addWidget(self.label_signup_reg, 0, Qt.AlignHCenter)

        self.verticalSpacer_2 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_8.addItem(self.verticalSpacer_2)

        self.frame_11 = QFrame(self.register_page)
        self.frame_11.setObjectName(u"frame_11")
        sizePolicy8 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Maximum)
        sizePolicy8.setHorizontalStretch(0)
        sizePolicy8.setVerticalStretch(0)
        sizePolicy8.setHeightForWidth(self.frame_11.sizePolicy().hasHeightForWidth())
        self.frame_11.setSizePolicy(sizePolicy8)
        self.frame_11.setFrameShape(QFrame.StyledPanel)
        self.frame_11.setFrameShadow(QFrame.Raised)
        self.verticalLayout_18 = QVBoxLayout(self.frame_11)
        self.verticalLayout_18.setObjectName(u"verticalLayout_18")
        self.lineEdit_signup_Name = QLineEdit(self.frame_11)
        self.lineEdit_signup_Name.setObjectName(u"lineEdit_signup_Name")

        self.verticalLayout_18.addWidget(self.lineEdit_signup_Name)

        self.lineEdit_pswrd_signup = QLineEdit(self.frame_11)
        self.lineEdit_pswrd_signup.setObjectName(u"lineEdit_pswrd_signup")
        self.lineEdit_pswrd_signup.setFrame(True)
        self.lineEdit_pswrd_signup.setEchoMode(QLineEdit.Normal)

        self.verticalLayout_18.addWidget(self.lineEdit_pswrd_signup)

        self.lineEdit_conf_pswrd = QLineEdit(self.frame_11)
        self.lineEdit_conf_pswrd.setObjectName(u"lineEdit_conf_pswrd")
        self.lineEdit_conf_pswrd.setEchoMode(QLineEdit.Normal)

        self.verticalLayout_18.addWidget(self.lineEdit_conf_pswrd)


        self.verticalLayout_8.addWidget(self.frame_11)

        self.label_error_registration = QLabel(self.register_page)
        self.label_error_registration.setObjectName(u"label_error_registration")
        self.label_error_registration.setAlignment(Qt.AlignCenter)

        self.verticalLayout_8.addWidget(self.label_error_registration)

        self.verticalSpacer_3 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_8.addItem(self.verticalSpacer_3)

        self.btnSignup = QPushButton(self.register_page)
        self.btnSignup.setObjectName(u"btnSignup")

        self.verticalLayout_8.addWidget(self.btnSignup, 0, Qt.AlignHCenter)

        self.btnAlready = QPushButton(self.register_page)
        self.btnAlready.setObjectName(u"btnAlready")
        font4 = QFont()
        font4.setUnderline(True)
        self.btnAlready.setFont(font4)

        self.verticalLayout_8.addWidget(self.btnAlready)

        self.profileStackedWidget.addWidget(self.register_page)
        self.login_page = QWidget()
        self.login_page.setObjectName(u"login_page")
        self.verticalLayout_20 = QVBoxLayout(self.login_page)
        self.verticalLayout_20.setObjectName(u"verticalLayout_20")
        self.label_6 = QLabel(self.login_page)
        self.label_6.setObjectName(u"label_6")
        sizePolicy7.setHeightForWidth(self.label_6.sizePolicy().hasHeightForWidth())
        self.label_6.setSizePolicy(sizePolicy7)
        self.label_6.setMinimumSize(QSize(50, 50))
        self.label_6.setMaximumSize(QSize(50, 50))
        self.label_6.setPixmap(QPixmap(u"icons/feather/user-check.svg"))
        self.label_6.setScaledContents(True)
        self.label_6.setAlignment(Qt.AlignCenter)

        self.verticalLayout_20.addWidget(self.label_6, 0, Qt.AlignHCenter)

        self.label_signup_2 = QLabel(self.login_page)
        self.label_signup_2.setObjectName(u"label_signup_2")
        self.label_signup_2.setEnabled(False)
        sizePolicy7.setHeightForWidth(self.label_signup_2.sizePolicy().hasHeightForWidth())
        self.label_signup_2.setSizePolicy(sizePolicy7)
        self.label_signup_2.setFont(font3)
        self.label_signup_2.setScaledContents(False)
        self.label_signup_2.setAlignment(Qt.AlignCenter)

        self.verticalLayout_20.addWidget(self.label_signup_2, 0, Qt.AlignHCenter)

        self.verticalSpacer_4 = QSpacerItem(20, 68, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_20.addItem(self.verticalSpacer_4)

        self.frame_12 = QFrame(self.login_page)
        self.frame_12.setObjectName(u"frame_12")
        sizePolicy8.setHeightForWidth(self.frame_12.sizePolicy().hasHeightForWidth())
        self.frame_12.setSizePolicy(sizePolicy8)
        self.frame_12.setFrameShape(QFrame.StyledPanel)
        self.frame_12.setFrameShadow(QFrame.Raised)
        self.verticalLayout_19 = QVBoxLayout(self.frame_12)
        self.verticalLayout_19.setObjectName(u"verticalLayout_19")
        self.lineEdit_login_Name = QLineEdit(self.frame_12)
        self.lineEdit_login_Name.setObjectName(u"lineEdit_login_Name")

        self.verticalLayout_19.addWidget(self.lineEdit_login_Name)

        self.lineEdit_pswrd_login = QLineEdit(self.frame_12)
        self.lineEdit_pswrd_login.setObjectName(u"lineEdit_pswrd_login")
        self.lineEdit_pswrd_login.setEchoMode(QLineEdit.Normal)

        self.verticalLayout_19.addWidget(self.lineEdit_pswrd_login)


        self.verticalLayout_20.addWidget(self.frame_12)

        self.label_error_autorization = QLabel(self.login_page)
        self.label_error_autorization.setObjectName(u"label_error_autorization")
        self.label_error_autorization.setAlignment(Qt.AlignCenter)

        self.verticalLayout_20.addWidget(self.label_error_autorization)

        self.verticalSpacer_5 = QSpacerItem(20, 68, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_20.addItem(self.verticalSpacer_5)

        self.btnLogin = QPushButton(self.login_page)
        self.btnLogin.setObjectName(u"btnLogin")

        self.verticalLayout_20.addWidget(self.btnLogin, 0, Qt.AlignHCenter)

        self.btnNoAcc = QPushButton(self.login_page)
        self.btnNoAcc.setObjectName(u"btnNoAcc")
        self.btnNoAcc.setFont(font4)

        self.verticalLayout_20.addWidget(self.btnNoAcc, 0, Qt.AlignHCenter)

        self.profileStackedWidget.addWidget(self.login_page)
        self.profile_page = QWidget()
        self.profile_page.setObjectName(u"profile_page")
        self.verticalLayout_27 = QVBoxLayout(self.profile_page)
        self.verticalLayout_27.setObjectName(u"verticalLayout_27")
        self.label_34 = QLabel(self.profile_page)
        self.label_34.setObjectName(u"label_34")
        self.label_34.setMinimumSize(QSize(50, 50))
        self.label_34.setMaximumSize(QSize(50, 50))
        self.label_34.setMidLineWidth(0)
        self.label_34.setPixmap(QPixmap(u"icons/feather/user.svg"))
        self.label_34.setScaledContents(True)
        self.label_34.setAlignment(Qt.AlignCenter)

        self.verticalLayout_27.addWidget(self.label_34, 0, Qt.AlignHCenter)

        self.label_33 = QLabel(self.profile_page)
        self.label_33.setObjectName(u"label_33")
        sizePolicy7.setHeightForWidth(self.label_33.sizePolicy().hasHeightForWidth())
        self.label_33.setSizePolicy(sizePolicy7)
        self.label_33.setFont(font)
        self.label_33.setAlignment(Qt.AlignCenter)

        self.verticalLayout_27.addWidget(self.label_33, 0, Qt.AlignHCenter)

        self.verticalSpacer_7 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_27.addItem(self.verticalSpacer_7)

        self.frame_15 = QFrame(self.profile_page)
        self.frame_15.setObjectName(u"frame_15")
        self.frame_15.setFrameShape(QFrame.StyledPanel)
        self.frame_15.setFrameShadow(QFrame.Raised)
        self.verticalLayout_26 = QVBoxLayout(self.frame_15)
        self.verticalLayout_26.setObjectName(u"verticalLayout_26")
        self.profile_user_name = QLabel(self.frame_15)
        self.profile_user_name.setObjectName(u"profile_user_name")
        self.profile_user_name.setFont(font1)

        self.verticalLayout_26.addWidget(self.profile_user_name, 0, Qt.AlignHCenter)

        self.frame_16 = QFrame(self.frame_15)
        self.frame_16.setObjectName(u"frame_16")
        self.frame_16.setFrameShape(QFrame.StyledPanel)
        self.frame_16.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_13 = QHBoxLayout(self.frame_16)
        self.horizontalLayout_13.setObjectName(u"horizontalLayout_13")
        self.label_58 = QLabel(self.frame_16)
        self.label_58.setObjectName(u"label_58")

        self.horizontalLayout_13.addWidget(self.label_58)

        self.lineEdit = QLineEdit(self.frame_16)
        self.lineEdit.setObjectName(u"lineEdit")

        self.horizontalLayout_13.addWidget(self.lineEdit)


        self.verticalLayout_26.addWidget(self.frame_16)

        self.verticalSpacer_8 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_26.addItem(self.verticalSpacer_8)

        self.btn_changePassword = QPushButton(self.frame_15)
        self.btn_changePassword.setObjectName(u"btn_changePassword")

        self.verticalLayout_26.addWidget(self.btn_changePassword)

        self.btn_logout = QPushButton(self.frame_15)
        self.btn_logout.setObjectName(u"btn_logout")

        self.verticalLayout_26.addWidget(self.btn_logout)

        self.verticalSpacer_6 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_26.addItem(self.verticalSpacer_6)


        self.verticalLayout_27.addWidget(self.frame_15)

        self.profileStackedWidget.addWidget(self.profile_page)

        self.verticalLayout_7.addWidget(self.profileStackedWidget, 0, Qt.AlignHCenter)


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
        font5 = QFont()
        font5.setBold(True)
        self.label_9.setFont(font5)

        self.verticalLayout_16.addWidget(self.label_9)

        self.frame_8 = QFrame(self.popupNotificationSubContainer)
        self.frame_8.setObjectName(u"frame_8")
        self.frame_8.setFrameShape(QFrame.StyledPanel)
        self.frame_8.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_9 = QHBoxLayout(self.frame_8)
        self.horizontalLayout_9.setObjectName(u"horizontalLayout_9")
        self.label_8 = QLabel(self.frame_8)
        self.label_8.setObjectName(u"label_8")
        sizePolicy9 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Preferred)
        sizePolicy9.setHorizontalStretch(0)
        sizePolicy9.setVerticalStretch(0)
        sizePolicy9.setHeightForWidth(self.label_8.sizePolicy().hasHeightForWidth())
        self.label_8.setSizePolicy(sizePolicy9)
        self.label_8.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_9.addWidget(self.label_8)

        self.closeNotificationBtn = QPushButton(self.frame_8)
        self.closeNotificationBtn.setObjectName(u"closeNotificationBtn")
        sizePolicy10 = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        sizePolicy10.setHorizontalStretch(0)
        sizePolicy10.setVerticalStretch(0)
        sizePolicy10.setHeightForWidth(self.closeNotificationBtn.sizePolicy().hasHeightForWidth())
        self.closeNotificationBtn.setSizePolicy(sizePolicy10)
        self.closeNotificationBtn.setMinimumSize(QSize(0, 0))
        icon11 = QIcon()
        icon11.addFile(u"icons/feather/x-octagon.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.closeNotificationBtn.setIcon(icon11)
        self.closeNotificationBtn.setIconSize(QSize(24, 24))

        self.horizontalLayout_9.addWidget(self.closeNotificationBtn, 0, Qt.AlignRight)


        self.verticalLayout_16.addWidget(self.frame_8)


        self.verticalLayout_15.addWidget(self.popupNotificationSubContainer)


        self.verticalLayout_5.addWidget(self.popupNotificationContainer)

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
        self.toolBar_2 = QToolBar(MainWindow)
        self.toolBar_2.setObjectName(u"toolBar_2")
        MainWindow.addToolBar(Qt.TopToolBarArea, self.toolBar_2)
        self.toolBar_3 = QToolBar(MainWindow)
        self.toolBar_3.setObjectName(u"toolBar_3")
        MainWindow.addToolBar(Qt.TopToolBarArea, self.toolBar_3)

        self.retranslateUi(MainWindow)

        self.mainPages.setCurrentIndex(0)
        self.TabWidgetProjects.setCurrentIndex(1)
        self.tabWidgetTasks.setCurrentIndex(1)
        self.tabWidgetTasks_2.setCurrentIndex(3)
        self.tabWidgetTasks_3.setCurrentIndex(3)
        self.profileStackedWidget.setCurrentIndex(1)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"Task-tracker", None))
#if QT_CONFIG(tooltip)
        self.menuBtn.setToolTip(QCoreApplication.translate("MainWindow", u"Menu", None))
#endif // QT_CONFIG(tooltip)
        self.menuBtn.setText("")
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
        self.tasks_lbl_3.setText(QCoreApplication.translate("MainWindow", u"\u041f\u0440\u043e\u0435\u043a\u0442\u044b", None))
        ___qtablewidgetitem = self.projectsTableWidget.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(QCoreApplication.translate("MainWindow", u"\u041d\u0430\u0437\u0432\u0430\u043d\u0438\u0435", None));
        ___qtablewidgetitem1 = self.projectsTableWidget.horizontalHeaderItem(1)
        ___qtablewidgetitem1.setText(QCoreApplication.translate("MainWindow", u"\u0417\u0430\u0434\u0430\u0447\u0438", None));
        ___qtablewidgetitem2 = self.projectsTableWidget.horizontalHeaderItem(2)
        ___qtablewidgetitem2.setText(QCoreApplication.translate("MainWindow", u"\u041f\u0440\u0438\u043e\u0440\u0438\u0442\u0435\u0442", None));
        ___qtablewidgetitem3 = self.projectsTableWidget.horizontalHeaderItem(3)
        ___qtablewidgetitem3.setText(QCoreApplication.translate("MainWindow", u"\u041f\u0440\u043e\u0433\u0440\u0435\u0441\u0441", None));
        ___qtablewidgetitem4 = self.projectsTableWidget.horizontalHeaderItem(4)
        ___qtablewidgetitem4.setText(QCoreApplication.translate("MainWindow", u"\u041e\u043a\u043e\u043d\u0447\u0430\u043d\u0438\u0435", None));
        ___qtablewidgetitem5 = self.projectsTableWidget.horizontalHeaderItem(5)
        ___qtablewidgetitem5.setText(QCoreApplication.translate("MainWindow", u"\u0421\u0442\u0430\u0442\u0443\u0441", None));
        ___qtablewidgetitem6 = self.projectsTableWidget.horizontalHeaderItem(6)
        ___qtablewidgetitem6.setText(QCoreApplication.translate("MainWindow", u"\u0414\u0435\u0439\u0441\u0442\u0432\u0438\u0435", None));
#if QT_CONFIG(accessibility)
        self.TabWidgetProjects.setAccessibleName("")
#endif // QT_CONFIG(accessibility)
#if QT_CONFIG(accessibility)
        self.tab_info_project.setAccessibleName("")
#endif // QT_CONFIG(accessibility)
        self.lbl_name_prjct.setText(QCoreApplication.translate("MainWindow", u"\u041d\u0430\u0437\u0432\u0430\u043d\u0438\u0435 \u043f\u0440\u043e\u0435\u043a\u0442\u0430", None))
        self.start_date_project_info.setText(QCoreApplication.translate("MainWindow", u"N/A", None))
        self.label_71.setText(QCoreApplication.translate("MainWindow", u"\u0414\u0430\u0442\u0430 \u043d\u0430\u0447\u0430\u043b\u0430", None))
        self.TabWidgetProjects.setTabText(self.TabWidgetProjects.indexOf(self.tab_info_project), QCoreApplication.translate("MainWindow", u"\u0418\u043d\u0444\u043e\u0440\u043c\u0430\u0446\u0438\u044f", None))
        self.projectPriorityComboBox.setItemText(0, QCoreApplication.translate("MainWindow", u"\u0412\u044b\u0441\u043e\u043a\u0438\u0439", None))
        self.projectPriorityComboBox.setItemText(1, QCoreApplication.translate("MainWindow", u"\u0421\u0440\u0435\u0434\u043d\u0438\u0439", None))
        self.projectPriorityComboBox.setItemText(2, QCoreApplication.translate("MainWindow", u"\u041d\u0438\u0437\u043a\u0438\u0439", None))

        self.label_5.setText(QCoreApplication.translate("MainWindow", u"\u041f\u0440\u0438\u043e\u0440\u0438\u0442\u0435\u0442", None))
        self.projectStatusComboBox.setItemText(0, QCoreApplication.translate("MainWindow", u"\u0412 \u043f\u043b\u0430\u043d\u0430\u0445", None))
        self.projectStatusComboBox.setItemText(1, QCoreApplication.translate("MainWindow", u"\u0412 \u043f\u0440\u043e\u0446\u0435\u0441\u0441\u0435", None))
        self.projectStatusComboBox.setItemText(2, QCoreApplication.translate("MainWindow", u"\u0417\u0430\u0432\u0435\u0440\u0448\u0435\u043d\u043e", None))

        self.label_13.setText(QCoreApplication.translate("MainWindow", u"\u0421\u0442\u0430\u0442\u0443\u0441", None))
        self.label_27.setText(QCoreApplication.translate("MainWindow", u"\u0414\u0430\u0442\u0430 \u043e\u043a\u043e\u043d\u0447\u0430\u043d\u0438\u044f", None))
        self.lbl_project_start.setText(QCoreApplication.translate("MainWindow", u"\u0414\u0430\u0442\u0430 \u043d\u0430\u0447\u0430\u043b\u0430", None))
        self.lbl_add_new_project.setText(QCoreApplication.translate("MainWindow", u"\u0414\u043e\u0431\u0430\u0432\u0438\u0442\u044c \u043d\u043e\u0432\u044b\u0439 \u043f\u0440\u043e\u0435\u043a\u0442", None))
        self.label_25.setText(QCoreApplication.translate("MainWindow", u"\u041d\u0430\u0437\u0432\u0430\u043d\u0438\u0435", None))
        self.save_project_btn.setText(QCoreApplication.translate("MainWindow", u"\u0421\u043e\u0445\u0440\u0430\u043d\u0438\u0442\u044c \u043f\u0440\u043e\u0435\u043a\u0442", None))
        self.lbl_description_project.setText(QCoreApplication.translate("MainWindow", u"\u041e\u043f\u0438\u0441\u0430\u043d\u0438\u0435", None))
        self.TabWidgetProjects.setTabText(self.TabWidgetProjects.indexOf(self.tab_add_project), QCoreApplication.translate("MainWindow", u"\u0414\u043e\u0431\u0430\u0432\u0438\u0442\u044c \u043f\u0440\u043e\u0435\u043a\u0442", None))
        self.project_name_edit.setText(QCoreApplication.translate("MainWindow", u"\u041d\u0430\u0437\u0432\u0430\u043d\u0438\u0435 \u043f\u0440\u043e\u0435\u043a\u0442\u0430", None))
        self.lbl_project_status_ed.setText(QCoreApplication.translate("MainWindow", u"\u0421\u0442\u0430\u0442\u0443\u0441", None))
        self.lbl_project_priority_ed.setText(QCoreApplication.translate("MainWindow", u"\u041f\u0440\u0438\u043e\u0440\u0438\u0442\u0435\u0442", None))
        self.lbl_project_end_date_ed.setText(QCoreApplication.translate("MainWindow", u"\u0414\u0430\u0442\u0430 \u043e\u043a\u043e\u043d\u0447\u0430\u043d\u0438\u044f", None))
        self.project_status_edit.setItemText(0, QCoreApplication.translate("MainWindow", u"\u0412 \u043f\u043b\u0430\u043d\u0430\u0445", None))
        self.project_status_edit.setItemText(1, QCoreApplication.translate("MainWindow", u"\u0412 \u043f\u0440\u043e\u0446\u0435\u0441\u0441\u0435", None))
        self.project_status_edit.setItemText(2, QCoreApplication.translate("MainWindow", u"\u0417\u0430\u0432\u0435\u0440\u0448\u0435\u043d\u043e", None))

        self.project_priority_edit.setItemText(0, QCoreApplication.translate("MainWindow", u"\u0412\u044b\u0441\u043e\u043a\u0438\u0439", None))
        self.project_priority_edit.setItemText(1, QCoreApplication.translate("MainWindow", u"\u0421\u0440\u0435\u0434\u043d\u0438\u0439", None))
        self.project_priority_edit.setItemText(2, QCoreApplication.translate("MainWindow", u"\u041d\u0438\u0437\u043a\u0438\u0439", None))

        self.save_project_edit_btn.setText(QCoreApplication.translate("MainWindow", u"\u0421\u043e\u0445\u0440\u0430\u043d\u0438\u0442\u044c \u0438\u0437\u043c\u0435\u043d\u0435\u043d\u0438\u044f", None))
        self.TabWidgetProjects.setTabText(self.TabWidgetProjects.indexOf(self.tab_edit_project), QCoreApplication.translate("MainWindow", u"\u0420\u0435\u0434\u0430\u043a\u0442\u0438\u0440\u043e\u0432\u0430\u043d\u0438\u0435", None))
        self.tasks_lbl.setText(QCoreApplication.translate("MainWindow", u"\u0417\u0430\u0434\u0430\u0447\u0438", None))
        ___qtablewidgetitem7 = self.tasksTableWidget.horizontalHeaderItem(0)
        ___qtablewidgetitem7.setText(QCoreApplication.translate("MainWindow", u"\u041d\u0430\u0437\u0432\u0430\u043d\u0438\u0435", None));
        ___qtablewidgetitem8 = self.tasksTableWidget.horizontalHeaderItem(1)
        ___qtablewidgetitem8.setText(QCoreApplication.translate("MainWindow", u"\u041f\u0440\u043e\u0435\u043a\u0442", None));
        ___qtablewidgetitem9 = self.tasksTableWidget.horizontalHeaderItem(2)
        ___qtablewidgetitem9.setText(QCoreApplication.translate("MainWindow", u"\u041f\u0440\u0438\u043e\u0440\u0438\u0442\u0435\u0442", None));
        ___qtablewidgetitem10 = self.tasksTableWidget.horizontalHeaderItem(3)
        ___qtablewidgetitem10.setText(QCoreApplication.translate("MainWindow", u"\u041e\u043a\u043e\u043d\u0447\u0430\u043d\u0438\u0435", None));
        ___qtablewidgetitem11 = self.tasksTableWidget.horizontalHeaderItem(4)
        ___qtablewidgetitem11.setText(QCoreApplication.translate("MainWindow", u"\u0421\u0442\u0430\u0442\u0443\u0441", None));
        ___qtablewidgetitem12 = self.tasksTableWidget.horizontalHeaderItem(5)
        ___qtablewidgetitem12.setText(QCoreApplication.translate("MainWindow", u"\u0414\u0435\u0439\u0441\u0442\u0432\u0438\u0435", None));
#if QT_CONFIG(accessibility)
        self.tabWidgetTasks.setAccessibleName("")
#endif // QT_CONFIG(accessibility)
#if QT_CONFIG(accessibility)
        self.tab_info_task.setAccessibleName("")
#endif // QT_CONFIG(accessibility)
        self.lbl_name_tsk.setText(QCoreApplication.translate("MainWindow", u"\u041d\u0430\u0437\u0432\u0430\u043d\u0438\u0435 \u0437\u0430\u0434\u0430\u0447\u0438", None))
        self.label_68.setText(QCoreApplication.translate("MainWindow", u"\u0414\u0430\u0442\u0430 \u043d\u0430\u0447\u0430\u043b\u0430", None))
        self.start_date_task_info.setText(QCoreApplication.translate("MainWindow", u"N/A", None))
        self.tabWidgetTasks.setTabText(self.tabWidgetTasks.indexOf(self.tab_info_task), QCoreApplication.translate("MainWindow", u"\u0418\u043d\u0444\u043e\u0440\u043c\u0430\u0446\u0438\u044f", None))
        self.label_18.setText(QCoreApplication.translate("MainWindow", u"\u041d\u0430\u0437\u0432\u0430\u043d\u0438\u0435", None))
        self.save_task_btn.setText(QCoreApplication.translate("MainWindow", u"\u0421\u043e\u0445\u0440\u0430\u043d\u0438\u0442\u044c \u0437\u0430\u0434\u0430\u0447\u0443", None))
        self.label_17.setText(QCoreApplication.translate("MainWindow", u"\u041e\u043f\u0438\u0441\u0430\u043d\u0438\u0435", None))
        self.label_16.setText(QCoreApplication.translate("MainWindow", u"\u0414\u043e\u0431\u0430\u0432\u0438\u0442\u044c \u043d\u043e\u0432\u0443\u044e \u0437\u0430\u0434\u0430\u0447\u0443", None))
        self.label_addTo.setText(QCoreApplication.translate("MainWindow", u"\u041f\u0440\u043e\u0435\u043a\u0442", None))
        self.taskPriorityComboBox.setItemText(0, QCoreApplication.translate("MainWindow", u"\u0412\u044b\u0441\u043e\u043a\u0438\u0439", None))
        self.taskPriorityComboBox.setItemText(1, QCoreApplication.translate("MainWindow", u"\u0421\u0440\u0435\u0434\u043d\u0438\u0439", None))
        self.taskPriorityComboBox.setItemText(2, QCoreApplication.translate("MainWindow", u"\u041d\u0438\u0437\u043a\u0438\u0439", None))

        self.taskStatusComboBox.setItemText(0, QCoreApplication.translate("MainWindow", u"\u0412 \u043f\u043b\u0430\u043d\u0430\u0445", None))
        self.taskStatusComboBox.setItemText(1, QCoreApplication.translate("MainWindow", u"\u0412 \u043f\u0440\u043e\u0446\u0435\u0441\u0441\u0435", None))
        self.taskStatusComboBox.setItemText(2, QCoreApplication.translate("MainWindow", u"\u0417\u0430\u0432\u0435\u0440\u0448\u0435\u043d\u043e", None))

        self.label_2.setText(QCoreApplication.translate("MainWindow", u"\u041f\u0440\u0438\u043e\u0440\u0438\u0442\u0435\u0442", None))
        self.label_22.setText(QCoreApplication.translate("MainWindow", u"\u0421\u0442\u0430\u0442\u0443\u0441", None))
        self.label_19.setText(QCoreApplication.translate("MainWindow", u"\u0414\u0430\u0442\u0430 \u043e\u043a\u043e\u043d\u0447\u0430\u043d\u0438\u044f", None))
        self.From_lbl.setText(QCoreApplication.translate("MainWindow", u"\u0414\u0430\u0442\u0430 \u043d\u0430\u0447\u0430\u043b\u0430", None))
        self.tabWidgetTasks.setTabText(self.tabWidgetTasks.indexOf(self.tab_add_task), QCoreApplication.translate("MainWindow", u"\u0414\u043e\u0431\u0430\u0432\u0438\u0442\u044c \u0437\u0430\u0434\u0430\u0447\u0443", None))
        self.task_name_edit.setText(QCoreApplication.translate("MainWindow", u"\u041d\u0430\u0437\u0432\u0430\u043d\u0438\u0435 \u0437\u0430\u0434\u0430\u0447\u0438", None))
        self.lb_task_status_ed.setText(QCoreApplication.translate("MainWindow", u"\u0421\u0442\u0430\u0442\u0443\u0441", None))
        self.lbl_task_priority_ed.setText(QCoreApplication.translate("MainWindow", u"\u041f\u0440\u0438\u043e\u0440\u0438\u0442\u0435\u0442", None))
        self.lbl_task_end_time_ed.setText(QCoreApplication.translate("MainWindow", u"\u0414\u0430\u0442\u0430 \u043e\u043a\u043e\u043d\u0447\u0430\u043d\u0438\u044f", None))
        self.task_status_edit.setItemText(0, QCoreApplication.translate("MainWindow", u"\u0412 \u043f\u043b\u0430\u043d\u0430\u0445", None))
        self.task_status_edit.setItemText(1, QCoreApplication.translate("MainWindow", u"\u0412 \u043f\u0440\u043e\u0446\u0435\u0441\u0441\u0435", None))
        self.task_status_edit.setItemText(2, QCoreApplication.translate("MainWindow", u"\u0417\u0430\u0432\u0435\u0440\u0448\u0435\u043d\u043e", None))

        self.task_priority_edit.setItemText(0, QCoreApplication.translate("MainWindow", u"\u0412\u044b\u0441\u043e\u043a\u0438\u0439", None))
        self.task_priority_edit.setItemText(1, QCoreApplication.translate("MainWindow", u"\u0421\u0440\u0435\u0434\u043d\u0438\u0439", None))
        self.task_priority_edit.setItemText(2, QCoreApplication.translate("MainWindow", u"\u041d\u0438\u0437\u043a\u0438\u0439", None))

        self.save_task_edit_btn.setText(QCoreApplication.translate("MainWindow", u"\u0421\u043e\u0445\u0440\u0430\u043d\u0438\u0442\u044c \u0438\u0437\u043c\u0435\u043d\u0435\u043d\u0438\u044f", None))
        self.tabWidgetTasks.setTabText(self.tabWidgetTasks.indexOf(self.tab_edit_task), QCoreApplication.translate("MainWindow", u"\u0420\u0435\u0434\u0430\u043a\u0442\u0438\u0440\u043e\u0432\u0430\u043d\u0438\u0435", None))
        self.label_14.setText(QCoreApplication.translate("MainWindow", u"\u0421\u0442\u0430\u0442\u0438\u0441\u0442\u0438\u043a\u0430", None))
        self.label_4.setText(QCoreApplication.translate("MainWindow", u"\u041f\u0440\u043e\u0435\u043a\u0442\u044b", None))
        self.label_62.setText(QCoreApplication.translate("MainWindow", u"\u0412\u0441\u0435 \u043f\u0440\u043e\u0435\u043a\u0442\u044b", None))
#if QT_CONFIG(accessibility)
        self.tabWidgetTasks_2.setAccessibleName("")
#endif // QT_CONFIG(accessibility)
        self.label_addTo_6.setText(QCoreApplication.translate("MainWindow", u"\u0412 \u043f\u043b\u0430\u043d\u0430\u0445", None))
        self.project_day_todo.setText(QCoreApplication.translate("MainWindow", u"N/A", None))
        self.label_45.setText(QCoreApplication.translate("MainWindow", u"\u0412 \u043f\u0440\u043e\u0446\u0435\u0441\u0441\u0435", None))
        self.project_day_in_progress.setText(QCoreApplication.translate("MainWindow", u"N/A", None))
        self.label_43.setText(QCoreApplication.translate("MainWindow", u"\u0417\u0430\u0432\u0435\u0440\u0448\u0435\u043d\u043e", None))
        self.project_day_done.setText(QCoreApplication.translate("MainWindow", u"N/A", None))
        self.tabWidgetTasks_2.setTabText(self.tabWidgetTasks_2.indexOf(self.dayProjects), QCoreApplication.translate("MainWindow", u"\u0414\u0435\u043d\u044c", None))
#if QT_CONFIG(accessibility)
        self.weekProjects.setAccessibleName("")
#endif // QT_CONFIG(accessibility)
        self.label_addTo_7.setText(QCoreApplication.translate("MainWindow", u"\u0412 \u043f\u043b\u0430\u043d\u0430\u0445", None))
        self.project_week_todo.setText(QCoreApplication.translate("MainWindow", u"N/A", None))
        self.label_49.setText(QCoreApplication.translate("MainWindow", u"\u0412 \u043f\u0440\u043e\u0446\u0435\u0441\u0441\u0435", None))
        self.project_week_in_progress.setText(QCoreApplication.translate("MainWindow", u"N/A", None))
        self.label_47.setText(QCoreApplication.translate("MainWindow", u"\u0417\u0430\u0432\u0435\u0440\u0448\u0435\u043d\u043e", None))
        self.project_week_done.setText(QCoreApplication.translate("MainWindow", u"N/A", None))
        self.tabWidgetTasks_2.setTabText(self.tabWidgetTasks_2.indexOf(self.weekProjects), QCoreApplication.translate("MainWindow", u"\u041d\u0435\u0434\u0435\u043b\u044f", None))
        self.label_addTo_8.setText(QCoreApplication.translate("MainWindow", u"\u0412 \u043f\u043b\u0430\u043d\u0430\u0445", None))
        self.project_month_todo.setText(QCoreApplication.translate("MainWindow", u"N/A", None))
        self.label_53.setText(QCoreApplication.translate("MainWindow", u"\u0412 \u043f\u0440\u043e\u0446\u0435\u0441\u0441\u0435", None))
        self.project_month_in_progress.setText(QCoreApplication.translate("MainWindow", u"N/A", None))
        self.label_51.setText(QCoreApplication.translate("MainWindow", u"\u0417\u0430\u0432\u0435\u0440\u0448\u0435\u043d\u043e", None))
        self.project_month_done.setText(QCoreApplication.translate("MainWindow", u"N/A", None))
        self.tabWidgetTasks_2.setTabText(self.tabWidgetTasks_2.indexOf(self.monthProjects), QCoreApplication.translate("MainWindow", u"\u041c\u0435\u0441\u044f\u0446", None))
        self.label_addTo_9.setText(QCoreApplication.translate("MainWindow", u"\u0412 \u043f\u043b\u0430\u043d\u0430\u0445", None))
        self.project_year_todo.setText(QCoreApplication.translate("MainWindow", u"N/A", None))
        self.label_57.setText(QCoreApplication.translate("MainWindow", u"\u0412 \u043f\u0440\u043e\u0446\u0435\u0441\u0441\u0435", None))
        self.project_year_in_progress.setText(QCoreApplication.translate("MainWindow", u"N/A", None))
        self.label_55.setText(QCoreApplication.translate("MainWindow", u"\u0417\u0430\u0432\u0435\u0440\u0448\u0435\u043d\u043e", None))
        self.project_year_done.setText(QCoreApplication.translate("MainWindow", u"N/A", None))
        self.tabWidgetTasks_2.setTabText(self.tabWidgetTasks_2.indexOf(self.yearProjects), QCoreApplication.translate("MainWindow", u"\u0413\u043e\u0434", None))
        self.label_15.setText(QCoreApplication.translate("MainWindow", u"\u0417\u0430\u0434\u0430\u0447\u0438", None))
        self.label_63.setText(QCoreApplication.translate("MainWindow", u"\u0412\u0441\u0435 \u0437\u0430\u0434\u0430\u0447\u0438", None))
#if QT_CONFIG(accessibility)
        self.tabWidgetTasks_3.setAccessibleName("")
#endif // QT_CONFIG(accessibility)
#if QT_CONFIG(accessibility)
        self.dayTasks.setAccessibleName("")
#endif // QT_CONFIG(accessibility)
        self.label_addTo_4.setText(QCoreApplication.translate("MainWindow", u"\u0412 \u043f\u043b\u0430\u043d\u0430\u0445", None))
        self.task_day_todo.setText(QCoreApplication.translate("MainWindow", u"N/A", None))
        self.label_39.setText(QCoreApplication.translate("MainWindow", u"\u0412 \u043f\u0440\u043e\u0446\u0435\u0441\u0441\u0435", None))
        self.task_day_in_progress.setText(QCoreApplication.translate("MainWindow", u"N/A", None))
        self.label_37.setText(QCoreApplication.translate("MainWindow", u"\u0417\u0430\u0432\u0435\u0440\u0448\u0435\u043d\u043e", None))
        self.task_day_done.setText(QCoreApplication.translate("MainWindow", u"N/A", None))
        self.tabWidgetTasks_3.setTabText(self.tabWidgetTasks_3.indexOf(self.dayTasks), QCoreApplication.translate("MainWindow", u"\u0414\u0435\u043d\u044c", None))
        self.label_addTo_2.setText(QCoreApplication.translate("MainWindow", u"\u0412 \u043f\u043b\u0430\u043d\u0430\u0445", None))
        self.task_week_todo.setText(QCoreApplication.translate("MainWindow", u"N/A", None))
        self.label_20.setText(QCoreApplication.translate("MainWindow", u"\u0412 \u043f\u0440\u043e\u0446\u0435\u0441\u0441\u0435", None))
        self.task_week_in_progress.setText(QCoreApplication.translate("MainWindow", u"N/A", None))
        self.label_21.setText(QCoreApplication.translate("MainWindow", u"\u0417\u0430\u0432\u0435\u0440\u0448\u0435\u043d\u043e", None))
        self.task_week_done.setText(QCoreApplication.translate("MainWindow", u"N/A", None))
        self.tabWidgetTasks_3.setTabText(self.tabWidgetTasks_3.indexOf(self.weekTasks), QCoreApplication.translate("MainWindow", u"\u041d\u0435\u0434\u0435\u043b\u044f", None))
        self.label_addTo_3.setText(QCoreApplication.translate("MainWindow", u"\u0412 \u043f\u043b\u0430\u043d\u0430\u0445", None))
        self.task_month_todo.setText(QCoreApplication.translate("MainWindow", u"N/A", None))
        self.label_29.setText(QCoreApplication.translate("MainWindow", u"\u0412 \u043f\u0440\u043e\u0446\u0435\u0441\u0441\u0435", None))
        self.task_month_in_progress.setText(QCoreApplication.translate("MainWindow", u"N/A", None))
        self.label_28.setText(QCoreApplication.translate("MainWindow", u"\u0417\u0430\u0432\u0435\u0440\u0448\u0435\u043d\u043e", None))
        self.task_month_done.setText(QCoreApplication.translate("MainWindow", u"N/A", None))
        self.tabWidgetTasks_3.setTabText(self.tabWidgetTasks_3.indexOf(self.monthTasks), QCoreApplication.translate("MainWindow", u"\u041c\u0435\u0441\u044f\u0446", None))
        self.label_addTo_5.setText(QCoreApplication.translate("MainWindow", u"\u0412 \u043f\u043b\u0430\u043d\u0430\u0445", None))
        self.task_year_todo.setText(QCoreApplication.translate("MainWindow", u"N/A", None))
        self.label_42.setText(QCoreApplication.translate("MainWindow", u"\u0412 \u043f\u0440\u043e\u0446\u0435\u0441\u0441\u0435", None))
        self.task_year_in_progress.setText(QCoreApplication.translate("MainWindow", u"N/A", None))
        self.label_31.setText(QCoreApplication.translate("MainWindow", u"\u0417\u0430\u0432\u0435\u0440\u0448\u0435\u043d\u043e", None))
        self.task_year_done.setText(QCoreApplication.translate("MainWindow", u"N/A", None))
        self.tabWidgetTasks_3.setTabText(self.tabWidgetTasks_3.indexOf(self.yearTasks), QCoreApplication.translate("MainWindow", u"\u0413\u043e\u0434", None))
        self.label_7.setText(QCoreApplication.translate("MainWindow", u"Calendar", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"Creating Progect", None))
        self.label_12.setText(QCoreApplication.translate("MainWindow", u"Creating task", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"\u041f\u043e\u043b\u044c\u0437\u043e\u0432\u0430\u0442\u0435\u043b\u044c", None))
#if QT_CONFIG(tooltip)
        self.closeProfileBtn.setToolTip(QCoreApplication.translate("MainWindow", u"Close User", None))
#endif // QT_CONFIG(tooltip)
        self.closeProfileBtn.setText("")
        self.pic_user_plus.setText("")
        self.label_signup_reg.setText(QCoreApplication.translate("MainWindow", u"\u0420\u0435\u0433\u0438\u0441\u0442\u0440\u0430\u0446\u0438\u044f", None))
        self.lineEdit_signup_Name.setPlaceholderText(QCoreApplication.translate("MainWindow", u"User Name", None))
        self.lineEdit_pswrd_signup.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Password", None))
        self.lineEdit_conf_pswrd.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Confirm password", None))
        self.label_error_registration.setText("")
        self.btnSignup.setText(QCoreApplication.translate("MainWindow", u"\u0417\u0430\u0440\u0435\u0433\u0438\u0441\u0442\u0440\u0438\u0440\u043e\u0432\u0430\u0442\u044c\u0441\u044f", None))
        self.btnAlready.setText(QCoreApplication.translate("MainWindow", u"\u0423\u0436\u0435 \u0435\u0441\u0442\u044c \u0430\u043a\u043a\u0430\u0443\u043d\u0442? \u0410\u0432\u0442\u043e\u0440\u0438\u0437\u0443\u0439\u0442\u0435\u0441\u044c", None))
        self.label_6.setText("")
        self.label_signup_2.setText(QCoreApplication.translate("MainWindow", u"\u0410\u0432\u0442\u043e\u0440\u0438\u0437\u0430\u0446\u0438\u044f", None))
        self.lineEdit_login_Name.setText("")
        self.lineEdit_login_Name.setPlaceholderText(QCoreApplication.translate("MainWindow", u"User Name", None))
        self.lineEdit_pswrd_login.setText("")
        self.lineEdit_pswrd_login.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Password", None))
        self.label_error_autorization.setText("")
        self.btnLogin.setText(QCoreApplication.translate("MainWindow", u"\u0412\u043e\u0439\u0442\u0438", None))
        self.btnNoAcc.setText(QCoreApplication.translate("MainWindow", u"\u041d\u0435\u0442 \u0430\u043a\u043a\u0430\u0443\u043d\u0442\u0430? \u0417\u0430\u0440\u0435\u0433\u0438\u0441\u0442\u0440\u0438\u0440\u0443\u0439\u0442\u0435\u0441\u044c", None))
        self.label_34.setText("")
        self.label_33.setText(QCoreApplication.translate("MainWindow", u"\u0414\u043e\u0431\u0440\u043e \u043f\u043e\u0436\u0430\u043b\u043e\u0432\u0430\u0442\u044c!", None))
        self.profile_user_name.setText(QCoreApplication.translate("MainWindow", u"User name", None))
        self.label_58.setText(QCoreApplication.translate("MainWindow", u"Email", None))
        self.btn_changePassword.setText(QCoreApplication.translate("MainWindow", u"\u0421\u043c\u0435\u043d\u0438\u0442\u044c \u043f\u0430\u0440\u043e\u043b\u044c", None))
        self.btn_logout.setText(QCoreApplication.translate("MainWindow", u"\u0412\u044b\u0439\u0442\u0438", None))
#if QT_CONFIG(tooltip)
        self.popupNotificationSubContainer.setToolTip(QCoreApplication.translate("MainWindow", u"Notification Message", None))
#endif // QT_CONFIG(tooltip)
        self.label_9.setText(QCoreApplication.translate("MainWindow", u"Notification", None))
        self.label_8.setText(QCoreApplication.translate("MainWindow", u"Notification Message", None))
#if QT_CONFIG(tooltip)
        self.closeNotificationBtn.setToolTip(QCoreApplication.translate("MainWindow", u"Close Notification", None))
#endif // QT_CONFIG(tooltip)
        self.closeNotificationBtn.setText("")
        self.label_11.setText("")
        self.toolBar.setWindowTitle(QCoreApplication.translate("MainWindow", u"toolBar", None))
        self.toolBar_2.setWindowTitle(QCoreApplication.translate("MainWindow", u"toolBar_2", None))
        self.toolBar_3.setWindowTitle(QCoreApplication.translate("MainWindow", u"toolBar_3", None))
    # retranslateUi

