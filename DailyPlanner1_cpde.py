# Coding file for Daily Planner aPP
# This is first version 

from DailyPlanner1_GUI import Ui_MainWindow
from PyQt5 import QtWidgets, QtCore
from PyQt5.QtWidgets import QMainWindow,QApplication, QListWidgetItem, QInputDialog, QMessageBox
from PyQt5.QtGui import QMovie
import sys
import sqlite3


class Main(QMainWindow):
    def __init__(self, parent=None):
        super(Main, self).__init__(parent)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        # set  .gif  file to label
        movie = QMovie('1.gif')
        self.ui.lblImage.setMovie(movie)
        movie.setSpeed(200)
        movie.start()

        self.ui.calendar.selectionChanged.connect(self.dateChanged)
        self.ui.btnAddTask.clicked.connect(self.add_task)
        self.ui.btnUpdateTask.clicked.connect(self.update_task)
        #self.ui.btnDeleteTask.clicked.connect(self.delete_task)
        self.ui.btnDeleteTask.clicked.connect(self.delete_task)



    def dateChanged(self):
        # set a variable to get date from calender widger
        selected_date = self.ui.calendar.selectedDate().toPyDate()
        selected_date_label = self.ui.calendar.selectedDate().toString()
        print(selected_date)
        self.ui.lblDate.setText(selected_date_label)
        self.setTaskList(selected_date)


    def setTaskList(self,date):
        # clear list widget
        self.ui.listTask.clear()
        print(date)

        # connection with database
        con = sqlite3.connect("DailyPlanner.db")
        cur = con.cursor()
        #print("get cursor")

        # get records with select query
        select_query = """ select task, status from task_list where date = ? """
        cur.execute(select_query,(date,))
        records = cur.fetchall()
        #print(records)

        for record in records:
            item = QListWidgetItem(str(record[0]))
            item.setFlags(item.flags() | QtCore.Qt.ItemIsUserCheckable)
            if record[1] == "yes" :
                item.setCheckState(QtCore.Qt.Checked)
            elif record[1] == "no" :
                item.setCheckState(QtCore.Qt.Unchecked)

            self.ui.listTask.addItem(item)

        con.commit()
        con.close()


    def add_task(self):
        new_task, ok  = QInputDialog.getText(self, "New Task", "Enter New Task")
        selected_date = self.ui.calendar.selectedDate().toPyDate()
        status = "no"

        # set connection with database
        con = sqlite3.connect("DailyPlanner.db")
        cur = con.cursor()

        # set insert query
        insert_query = """insert into task_list(task, status, date)
                                    values (?, ?, ?)"""
        #select_query = """ select task, status from task_list where date = ? """
        field_list=(new_task, status, selected_date)
        cur.execute(insert_query,field_list)

        con.commit()
        self.setTaskList(selected_date)
        con.close()


    def delete_task(self):
        con = sqlite3.connect("DailyPlanner.db")
        cur = con.cursor()
        currentRow = self.ui.listTask.currentRow()
        selected_date = self.ui.calendar.selectedDate().toPyDate()
        item = self.ui.listTask.item(currentRow)
        print(item.text())

        if item is None:
            return

        response = QMessageBox.question(self, "Delete Task", "Do You Want to Delete Task - " + item.text() + " ??",
                               QMessageBox.Yes | QMessageBox.No)

        if response == QMessageBox.Yes :

            delete_query = "delete from task_list where task = ? and date = ?"
            field_list=(item.text(),selected_date)
            cur.execute(delete_query,field_list)

            item = self.ui.listTask.takeItem(currentRow)
            del item

        con.commit()
        con.close()

        msgBox = QMessageBox()
        msgBox.setText("Task Deleted...")
        msgBox.exec_()

    def update_task(self):
        selected_date = self.ui.calendar.selectedDate().toPyDate()
        con = sqlite3.connect("DailyPlanner.db")
        cur = con.cursor()

        for i in range(self.ui.listTask.count()):
            #print(i)
            item = self.ui.listTask.item(i)
            task = item.text()
            #print(task)
            if item.checkState() == QtCore.Qt.Checked :
                update_query = "update task_list set status = 'yes' where task=? and date=? "
            else :
                update_query = "update task_list set status = 'no' where task=? and date=? "

            field_list=(task, selected_date)
            cur.execute(update_query,field_list)

        msgBox = QMessageBox()
        msgBox.setText("Task Updated...")
        msgBox.exec_()

        con.commit()
        con.close()


def main():
    app = QApplication(sys.argv)
    window = Main()
    window.show()
    #sys.exit(app.exec_())
    app.exec_()


main()