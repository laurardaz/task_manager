import datetime

from enum import Enum

class PlanPeriod(Enum):
    DAY = "День"
    WEEK = "Неделя"
    MONTH = "Месяц"
    YEAR = "Год"
    INFINITY = "Бессрочно"

class Status(str, Enum):
    TODO = "В планах"
    IN_PROGRESS = "В процессе"
    DONE = "Завершено"


# class Date(date):
# CurrentDate = date.datetime.now().strftime("dd/MM/yyyy")
# dat = "07/05/2023"
# DAY = CurrentDate < dat

date_today = datetime.date.today()

def today():
    return date_today

start_week = date_today - datetime.timedelta(days=date_today.weekday())
end_week = start_week + datetime.timedelta(days=6)

def this_week_start():  
    return start_week

def this_week_end():
    return end_week


def this_month_start():
    return date_today.replace(day=1)
        
def this_month_end():
    return (date_today.replace(day=28) + datetime.timedelta(days=4)).replace(day=1) + datetime.timedelta(days=-1)


def this_year_start():
    return date_today.replace(month=1, day=1)  

def this_year_end():
    return date_today.replace(month=12, day=31)

class TaskStatistics:
    def __init__(self, task_manager):
        self.task_manager = task_manager
        # self.project_manager = project_manager
     

    def count_todo(self, period, tasks):
        return self.count(Status.TODO, period, tasks)

    def count_in_progress(self, period, tasks):
        return self.count(Status.IN_PROGRESS, period, tasks)

    def count_done(self, period, tasks):
        return self.count(Status.DONE, period, tasks)
    
    def progress(self, tasks):
        done_count = self.count_done(PlanPeriod.INFINITY, tasks)
        all_count = len(tasks)
        if all_count == 0:
            return "No tasks yet"
        return f'{round((done_count * 100 / all_count), 2)} % [{done_count} / {all_count}]'

    

    def count(self, status, period, tasks):
        # tasks = self.task_manager.get_tasks(project.name)
        def contain_deadline(t, period: PlanPeriod):
            task_deadline = datetime.datetime.strptime(t.end_date, "%d/%m/%Y").date()
            if period is PlanPeriod.DAY:
                return task_deadline == today()
            elif period is PlanPeriod.WEEK:
                return this_week_start() <= task_deadline <= this_week_end()
            elif period is PlanPeriod.MONTH:
                return this_month_start() <= task_deadline < this_month_end()
            elif period is PlanPeriod.YEAR:
                return this_year_start() <= task_deadline < this_year_end()
            elif period is PlanPeriod.INFINITY:
                return True
            else:
                exit("plan period is unknown")

        return len(list(filter(lambda t: t.status == status and contain_deadline(t, period), tasks)))


class ProjectStatistics:
    def __init__(self, project_manager):
        self.project_manager = project_manager

    def count_todo(self, period):
        return self.count(Status.TODO, period)

    def count_in_progress(self, period):
        return self.count(Status.IN_PROGRESS, period)

    def count_done(self, period):
        return self.count(Status.DONE, period)
    

    def count(self, status, period):
        projects = self.project_manager.get_projects()
        def contain_deadline(p, period: PlanPeriod):
            task_deadline = datetime.datetime.strptime(p.end_date, "%d/%m/%Y").date()
            if period is PlanPeriod.DAY:
                return task_deadline == today()
            elif period is PlanPeriod.WEEK:
                return this_week_start() <= task_deadline <= this_week_end()
            elif period is PlanPeriod.MONTH:
                return this_month_start() <= task_deadline < this_month_end()
            elif period is PlanPeriod.YEAR:
                return this_year_start() <= task_deadline < this_year_end()
            else:
                exit("plan period is unknown")

        return len(list(filter(lambda p: p.status == status and contain_deadline(p, period), projects)))
