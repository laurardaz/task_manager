import sys

from ui_mainwindow import *
from Custom_Widgets.Widgets import *

from task_manager import *
from project_manager import *
from statistics_ import *
from user_manager import *

from datetime import datetime

class MainWindow(QMainWindow):
    def __init__(self):
        self.user_manager = UserManager()
        QMainWindow.__init__(self)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self.ui.profileBtn.clicked.connect(lambda: self.ui.profileContainer.expandMenu())
        self.ui.closeProfileBtn.clicked.connect(lambda: self.ui.profileContainer.collapseMenu())
        self.ui.closeNotificationBtn.clicked.connect(lambda: self.ui.popupNotificationContainer.collapseMenu())

        self.ui.btnSignup.clicked.connect(self.signup_function)
        self.ui.btnLogin.clicked.connect(self.login_function)
        self.ui.btn_changePassword.clicked.connect(lambda: self.ui.profileStackedWidget.setCurrentWidget(self.ui.register_page))
        self.ui.btn_logout.clicked.connect(lambda: self.ui.profileStackedWidget.setCurrentWidget(self.ui.login_page))


        self.ui.from_time_pjt.setDateTime(QtCore.QDateTime.currentDateTime())
        self.ui.end_date_project.setDateTime(QtCore.QDateTime.currentDateTime())
        self.ui.from_time_tsk.setDateTime(QtCore.QDateTime.currentDateTime())
        self.ui.to_time_tsk.setDateTime(QtCore.QDateTime.currentDateTime())

        loadJsonStyle(self, self.ui)

        self.show()

      
        self.ui.tasksTableWidget.setColumnWidth(0, 300)
        self.ui.tasksTableWidget.setColumnWidth(1, 100)
        self.ui.tasksTableWidget.setColumnWidth(2, 100)
        self.ui.tasksTableWidget.setColumnWidth(3, 100)
        self.ui.tasksTableWidget.setColumnWidth(4, 90)
        self.ui.tasksTableWidget.setColumnWidth(5, 70)

        self.ui.projectsTableWidget.setColumnWidth(0, 300)
        self.ui.projectsTableWidget.setColumnWidth(1, 80)
        self.ui.projectsTableWidget.setColumnWidth(2, 100)
        self.ui.projectsTableWidget.setColumnWidth(3, 100)
        self.ui.projectsTableWidget.setColumnWidth(4, 100)
        self.ui.projectsTableWidget.setColumnWidth(5, 90)
        self.ui.projectsTableWidget.setColumnWidth(6, 70)

        def on_task_save():
            project_name = self.ui.choose_project_comboBox.currentText()
            project = self.project_manager.get_project_by_name(project_name)
            self.task_manager.add_task(project,
                                       self.ui.task_name_input.text(),
                                       self.ui.descriptionTask.toPlainText(),
                                       self.ui.taskPriorityComboBox.currentText(),
                                       self.ui.from_time_tsk.date().toString("dd/MM/yyyy"),
                                       self.ui.to_time_tsk.date().toString("dd/MM/yyyy"),
                                       self.ui.taskStatusComboBox.currentText(),
                                       )
            project.progress = self.task_statistics.progress(self.task_manager.get_tasks(project_name))
            self.update_tasks()
            self.update_tasks_statistics()
            self.update_projects()
            current_user_id = self.user_manager.get_user_id(self.user_manager.current_user)
            self.project_manager.write_json(current_user_id)
            self.ui.task_name_input.clear()
            self.ui.descriptionTask.clear()

        def on_project_save():
            print("project save called")
            project_name = self.ui.project_name.text()
            progress = self.task_statistics.progress(self.task_manager.get_tasks(project_name))
            self.project_manager.add_project(project_name,
                                             self.ui.descriptionProject.toPlainText(),
                                             self.ui.projectPriorityComboBox.currentText(),
                                             progress,
                                             self.ui.from_time_pjt.date().toString("dd/MM/yyyy"),
                                             self.ui.end_date_project.date().toString("dd/MM/yyyy"),
                                             self.ui.projectStatusComboBox.currentText(),
                                             [])
            self.update_projects()
            self.update_projects_statistics()
            self.ui.choose_project_comboBox.addItem(project_name)
            current_user_id = self.user_manager.get_user_id(self.user_manager.current_user)
            self.project_manager.write_json(current_user_id)
            self.ui.project_name.clear()
            self.ui.descriptionProject.clear()

        self.ui.projectsBtn.clicked.connect(self.update_projects)
        self.ui.save_task_btn.clicked.connect(on_task_save)
        self.ui.save_project_btn.clicked.connect(on_project_save)

        self.user_manager.current_user = ""
        if self.user_manager.current_user != "":
            self.user_manager.current_user = self.login_function()
        else:
            pass
        
    def fill_data(self, user_id):
        print("fill data is called with user_id: ".format(user_id))
        self.task_manager = TaskManager()
        self.project_manager = ProjectManager(user_id)
        self.task_manager.sync_tasks(self.project_manager)
        self.task_statistics = TaskStatistics(self.task_manager)
        self.project_statistics = ProjectStatistics(self.project_manager)
        self.ui.choose_project_comboBox.addItems(self.project_manager.get_project_names())
        self.update_tasks()        
        self.update_projects()
        self.update_tasks_statistics()        
        self.update_projects_statistics()

        
    def update_tasks_statistics(self):
        self.ui.task_day_todo.setText(str(self.task_statistics.count_todo(PlanPeriod.DAY, self.task_manager.get_all_tasks())))
        self.ui.task_day_in_progress.setText(str(self.task_statistics.count_in_progress(PlanPeriod.DAY, self.task_manager.get_all_tasks())))
        self.ui.task_day_done.setText(str(self.task_statistics.count_done(PlanPeriod.DAY, self.task_manager.get_all_tasks())))

        self.ui.task_week_todo.setText(str(self.task_statistics.count_todo(PlanPeriod.WEEK, self.task_manager.get_all_tasks())))
        self.ui.task_week_in_progress.setText(str(self.task_statistics.count_in_progress(PlanPeriod.WEEK, self.task_manager.get_all_tasks())))
        self.ui.task_week_done.setText(str(self.task_statistics.count_done(PlanPeriod.WEEK, self.task_manager.get_all_tasks())))

        self.ui.task_month_todo.setText(str(self.task_statistics.count_todo(PlanPeriod.MONTH, self.task_manager.get_all_tasks())))
        self.ui.task_month_in_progress.setText(str(self.task_statistics.count_in_progress(PlanPeriod.MONTH, self.task_manager.get_all_tasks())))
        self.ui.task_month_done.setText(str(self.task_statistics.count_done(PlanPeriod.MONTH, self.task_manager.get_all_tasks())))

        self.ui.task_year_todo.setText(str(self.task_statistics.count_todo(PlanPeriod.YEAR, self.task_manager.get_all_tasks())))
        self.ui.task_year_in_progress.setText(str(self.task_statistics.count_in_progress(PlanPeriod.YEAR, self.task_manager.get_all_tasks())))
        self.ui.task_year_done.setText(str(self.task_statistics.count_done(PlanPeriod.YEAR, self.task_manager.get_all_tasks())))


    def update_projects_statistics(self):
        self.ui.project_day_todo.setText(str(self.project_statistics.count_todo(PlanPeriod.DAY)))
        self.ui.project_day_in_progress.setText(str(self.project_statistics.count_in_progress(PlanPeriod.DAY)))
        self.ui.project_day_done.setText(str(self.project_statistics.count_done(PlanPeriod.DAY)))

        self.ui.project_week_todo.setText(str(self.project_statistics.count_todo(PlanPeriod.WEEK)))
        self.ui.project_week_in_progress.setText(str(self.project_statistics.count_in_progress(PlanPeriod.WEEK)))
        self.ui.project_week_done.setText(str(self.project_statistics.count_done(PlanPeriod.WEEK)))

        self.ui.project_month_todo.setText(str(self.project_statistics.count_todo(PlanPeriod.MONTH)))
        self.ui.project_month_in_progress.setText(str(self.project_statistics.count_in_progress(PlanPeriod.MONTH)))
        self.ui.project_month_done.setText(str(self.project_statistics.count_done(PlanPeriod.MONTH)))

        self.ui.project_year_todo.setText(str(self.project_statistics.count_todo(PlanPeriod.YEAR)))
        self.ui.project_year_in_progress.setText(str(self.project_statistics.count_in_progress(PlanPeriod.YEAR)))
        self.ui.project_year_done.setText(str(self.project_statistics.count_done(PlanPeriod.YEAR)))
    
     
    def signup_function(self):
        '''
        Signing up
        '''
        user_sign = self.ui.lineEdit_signup_Name.text()
        password_sign = self.ui.lineEdit_pswrd_signup.text()
        confirmpassword = self.ui.lineEdit_conf_pswrd.text()
        
        if len(user_sign)==0 or len(password_sign)==0 or len(confirmpassword)==0:
            self.ui.label_error_registration.setText("Пожалуйста, заполните все поля!")

        elif password_sign!=confirmpassword:
            self.ui.label_error_registration.setText("Пароли не совпадают!")

        else:
            self.ui.profileStackedWidget.setCurrentWidget(self.ui.profile_page)
            self.ui.profile_user_name.setText(user_sign)
            self.ui.lineEdit_signup_Name.clear()
            self.ui.lineEdit_pswrd_signup.clear()
            self.ui.lineEdit_conf_pswrd.clear()

            self.user_manager.add_new_user(user_sign, password_sign, "")
            self.user_manager.write_user_json()
            user_id = self.user_manager.get_user_id(user_sign)
            project_creator = ProjectCreator().create_empty(user_id)
            self.user_manager.set_current_user(user_sign)
            self.fill_data(user_id)
        

    def login_function(self):
        '''
        Login
        '''
        user_login = self.ui.lineEdit_login_Name.text()
        password_login = self.ui.lineEdit_pswrd_login.text()

        if len(user_login)==0 or len(password_login)==0:
            self.ui.label_error_autorization.setText("Пожалуйста, заполните все поля!")

        elif self.user_manager.check_user(user_login, password_login) == True:
            self.ui.profileStackedWidget.setCurrentWidget(self.ui.profile_page)
            self.ui.lineEdit_login_Name.clear()
            self.ui.lineEdit_pswrd_login.clear()
            self.ui.profile_user_name.setText(user_login)
            self.user_manager.set_current_user(user_login)
            self.fill_data(self.user_manager.get_user_id(user_login))
            
        else:
            self.ui.label_error_autorization.setText("Неверный логин или пароль!")
        

    def removeCurrentProjectRow(self):
        messageBox = QMessageBox(self)
        messageBox.setWindowTitle("Подтверждение действия")
        messageBox.setIcon(QMessageBox.Question)
        messageBox.setText("Удалить объект?")
        messageBox.setInformativeText("Вы действительно хотите удалить этот объект?")
        
        buttonoptionYes = messageBox.addButton("Да", QMessageBox.YesRole)    
        buttonoptionNo = messageBox.addButton("Нет", QMessageBox.NoRole)  
        messageBox.setDefaultButton(buttonoptionNo)
        
        messageBox.exec_()
        if messageBox.clickedButton() == buttonoptionYes:
            buttonoptionYes = self.sender()
            if buttonoptionYes:
                row = self.ui.projectsTableWidget.indexAt(buttonoptionYes.parentWidget().pos()).row()
            
                name_of_project = self.ui.projectsTableWidget.item(row, 0).text()
                self.ui.projectsTableWidget.removeRow(row)

                self.project_manager.delete_projects(name_of_project)
                
                    
                self.update_projects()
                self.update_projects_statistics()
                current_user_id = self.user_manager.get_user_id(self.user_manager.current_user)
                self.project_manager.write_json(current_user_id)

                self.task_manager.delete_tasks(name_of_project) 
                self.update_tasks()
                self.ui.choose_project_comboBox.clear()
                self.ui.choose_project_comboBox.addItems(self.project_manager.get_project_names())


    def update_project_and_save(self, project, status, priority, end_date):
        project.status = status
        project.priority = priority
        project.end_date = end_date
        self.update_projects()
        self.update_projects_statistics()
        user_id = self.user_manager.get_user_id(self.user_manager.current_user)
        self.project_manager.write_json(user_id)

        
    def editCurrentProjectRow(self):
        self.ui.TabWidgetProjects.setCurrentWidget(self.ui.tab_edit_project)
        btn_edit = self.sender()
        if btn_edit:
            row = self.ui.projectsTableWidget.indexAt(btn_edit.parentWidget().pos()).row()
            name_of_project = self.ui.projectsTableWidget.item(row, 0).text()
            self.ui.project_name_edit.setText(name_of_project)
            status_of_project = self.ui.projectsTableWidget.item(row, 5).text()
            self.ui.project_status_edit.setCurrentText(status_of_project)
            priority_of_project = self.ui.projectsTableWidget.item(row, 2).text()
            self.ui.project_priority_edit.setCurrentText(priority_of_project)
            end_date_str = self.ui.projectsTableWidget.item(row, 4).text()
            end_date_date = datetime.strptime(end_date_str, '%d/%m/%Y')
            self.ui.project_date_edit.setDate(end_date_date)
            project = self.project_manager.get_project_by_name(name_of_project)
            self.ui.save_project_edit_btn.clicked.connect(lambda: self.update_project_and_save(project,
                                                                                               self.ui.project_status_edit.currentText(),
                                                                                               self.ui.project_priority_edit.currentText(),
                                                                                               self.ui.project_date_edit.date().toString("dd/MM/yyyy")))
                  

    def infoCurrentProjectRow(self):
        self.ui.TabWidgetProjects.setCurrentWidget(self.ui.tab_info_project)
        btn_info = self.sender()
        if btn_info:    
            row = self.ui.projectsTableWidget.indexAt(btn_info.parentWidget().pos()).row()
            name_of_project = self.ui.projectsTableWidget.item(row, 0).text()
            self.ui.lbl_name_prjct.setText(name_of_project)
            description_of_project = self.project_manager.get_project_by_name(name_of_project).description
            self.ui.project_info_description.setText(description_of_project)
            start_date_project = self.project_manager.get_project_by_name(name_of_project).start_date
            self.ui.start_date_project_info.setText(start_date_project)


    def removeCurrentTaskRow(self):
        messageBox = QMessageBox(self)
        messageBox.setWindowTitle("Подтверждение действия")
        messageBox.setIcon(QMessageBox.Question)
        messageBox.setText("Удалить объект?")
        messageBox.setInformativeText("Вы действительно хотите удалить этот объект?")
        
        buttonoptionYes = messageBox.addButton("Да", QMessageBox.YesRole)    
        buttonoptionNo = messageBox.addButton("Нет", QMessageBox.NoRole)  
        messageBox.setDefaultButton(buttonoptionNo)
        
        messageBox.exec_()
        if messageBox.clickedButton() == buttonoptionYes:
            buttonoptionYes = self.sender()
            if buttonoptionYes:
                row = self.ui.tasksTableWidget.indexAt(buttonoptionYes.parentWidget().pos()).row()
            
                name_of_task = self.ui.tasksTableWidget.item(row, 0).text()
                self.ui.tasksTableWidget.removeRow(row)

                task = self.task_manager.get_task_by_name(name_of_task)
                project = self.project_manager.get_project_by_name(task.project_name)
                project.remove_task(name_of_task)
                self.task_manager.delete_tasks(name_of_task)      
                    
                self.update_tasks()
                self.update_tasks_statistics()
                self.update_projects()

                current_user_id = self.user_manager.get_user_id(self.user_manager.current_user)
                self.project_manager.write_json(current_user_id)


    def update_task_and_save(self, task, status, priority, end_date):
        task.status = status
        task.priority = priority
        task.end_date = end_date
        self.update_tasks()
        self.update_tasks_statistics()
        user_id = self.user_manager.get_user_id(self.user_manager.current_user)
        self.project_manager.write_json(user_id)
    
    def editCurrentTaskRow(self):
        self.ui.tabWidgetTasks.setCurrentWidget(self.ui.tab_edit_task)
        btn_edit = self.sender()
        if btn_edit:
            row = self.ui.tasksTableWidget.indexAt(btn_edit.parentWidget().pos()).row()
            name_of_task = self.ui.tasksTableWidget.item(row, 0).text()
            self.ui.task_name_edit.setText(name_of_task)
            status_of_task = self.ui.tasksTableWidget.item(row, 4).text()
            self.ui.task_status_edit.setCurrentText(status_of_task)
            priority_of_task = self.ui.tasksTableWidget.item(row, 2).text()
            self.ui.project_priority_edit.setCurrentText(priority_of_task)
            end_date_str = self.ui.tasksTableWidget.item(row, 3).text()
            end_date_date = datetime.strptime(end_date_str, '%d/%m/%Y')
            self.ui.task_end_date_edit.setDate(end_date_date)
            task = self.task_manager.get_task_by_name(name_of_task)
            self.ui.save_task_edit_btn.clicked.connect(lambda: self.update_task_and_save(task,
                                                                                        self.ui.task_status_edit.currentText(),
                                                                                        self.ui.task_priority_edit.currentText(),
                                                                                        self.ui.task_end_date_edit.date().toString("dd/MM/yyyy")))


    def infoCurrentTaskRow(self):
        self.ui.tabWidgetTasks.setCurrentWidget(self.ui.tab_info_task)
        btn_info = self.sender()
        if btn_info:    
            row = self.ui.tasksTableWidget.indexAt(btn_info.parentWidget().pos()).row()
            name_of_task = self.ui.tasksTableWidget.item(row, 0).text()
            self.ui.lbl_name_tsk.setText(name_of_task)
            description_of_task = self.task_manager.get_task_by_name(name_of_task).description
            self.ui.task_info_description.setText(description_of_task)
            start_date_task = self.task_manager.get_task_by_name(name_of_task).start_date
            self.ui.start_date_task_info.setText(start_date_task)
      

    def update_tasks(self):
        self.ui.tasksTableWidget.setRowCount(self.task_manager.count_tasks())
        for row_number, task in enumerate(self.task_manager.get_all_tasks()):
            self.ui.tasksTableWidget.setItem(row_number, 0, QtWidgets.QTableWidgetItem(task.name))
            self.ui.tasksTableWidget.setItem(row_number, 1, QtWidgets.QTableWidgetItem(task.project_name))
            self.ui.tasksTableWidget.setItem(row_number, 2, QtWidgets.QTableWidgetItem(task.priority))
            self.ui.tasksTableWidget.setItem(row_number, 3, QtWidgets.QTableWidgetItem(str(task.end_date)))
            self.ui.tasksTableWidget.setItem(row_number, 4, QtWidgets.QTableWidgetItem(task.status))

            layout = QHBoxLayout()
            layout.setContentsMargins(0,0,0,0)
            layout.setSpacing(0)
            delete_btn = QtWidgets.QPushButton()
            info_btn = QtWidgets.QPushButton()
            edit_btn = QtWidgets.QPushButton()         
            layout.addWidget(delete_btn)
            layout.addWidget(info_btn)
            layout.addWidget(edit_btn)

            delete_btn.setIcon(QtGui.QIcon('icons/feather/x-square.svg'))
            delete_btn.setIconSize(QtCore.QSize(25,25))
            info_btn.setIcon(QtGui.QIcon('icons/feather/info.svg'))
            info_btn.setIconSize(QtCore.QSize(25,25))
            edit_btn.setIcon(QtGui.QIcon('icons/feather/edit.svg'))
            edit_btn.setIconSize(QtCore.QSize(25,25))
            cellWidget = QWidget()
            cellWidget.setLayout(layout)
            self.ui.tasksTableWidget.setCellWidget(row_number, 5, cellWidget)
            delete_btn.clicked.connect(self.removeCurrentTaskRow)
            info_btn.clicked.connect(self.infoCurrentTaskRow)
            edit_btn.clicked.connect(self.editCurrentTaskRow)
    

    def update_projects(self):
        self.ui.projectsTableWidget.setRowCount(self.project_manager.get_project_count())
        for row_number, project in enumerate(self.project_manager.get_projects()):
            self.ui.projectsTableWidget.setItem(row_number, 0, QtWidgets.QTableWidgetItem(project.name))
            self.ui.projectsTableWidget.setItem(row_number, 1, QtWidgets.QTableWidgetItem(str(project.tasks_count())))
            self.ui.projectsTableWidget.setItem(row_number, 2, QtWidgets.QTableWidgetItem(project.priority))
            self.ui.projectsTableWidget.setItem(row_number, 3, QtWidgets.QTableWidgetItem(str(project.progress)))
            self.ui.projectsTableWidget.setItem(row_number, 4, QtWidgets.QTableWidgetItem(str(project.end_date)))
            self.ui.projectsTableWidget.setItem(row_number, 5, QtWidgets.QTableWidgetItem(project.status))
            
            layout = QHBoxLayout()
            layout.setContentsMargins(0,0,0,0)
            layout.setSpacing(0)
            delete_btn = QtWidgets.QPushButton()
            info_btn = QtWidgets.QPushButton()
            edit_btn = QtWidgets.QPushButton()          
            layout.addWidget(delete_btn)
            layout.addWidget(info_btn)
            layout.addWidget(edit_btn)    

            delete_btn.setIcon(QtGui.QIcon('icons/feather/x-square.svg'))
            delete_btn.setIconSize(QtCore.QSize(25,25))
            info_btn.setIcon(QtGui.QIcon('icons/feather/info.svg'))
            info_btn.setIconSize(QtCore.QSize(25,25))
            edit_btn.setIcon(QtGui.QIcon('icons/feather/edit.svg'))
            edit_btn.setIconSize(QtCore.QSize(25,25))         
            cellWidget = QWidget()
            cellWidget.setLayout(layout)
            self.ui.projectsTableWidget.setCellWidget(row_number, 6, cellWidget)          
            delete_btn.clicked.connect(self.removeCurrentProjectRow)
            info_btn.clicked.connect(self.infoCurrentProjectRow)
            edit_btn.clicked.connect(self.editCurrentProjectRow)
          

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    sys.exit(app.exec_())
