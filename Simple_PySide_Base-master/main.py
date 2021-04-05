

from app_modules import *
import sqlite3
import sys
import platform
from PySide2 import QtCore, QtGui, QtWidgets
from PySide2.QtCore import (QCoreApplication, QPropertyAnimation, QDate, QDateTime, QMetaObject, QObject, QPoint, QRect, QSize, QTime, QUrl, Qt, QEvent)
from PySide2.QtGui import (QBrush, QColor, QConicalGradient, QCursor, QFont, QFontDatabase, QIcon, QKeySequence, QLinearGradient, QPalette, QPainter, QPixmap, QRadialGradient)
from PySide2.QtWidgets import *
import itertools
from datetime import datetime
from operator import itemgetter
##db creation

conn_customer = sqlite3.connect("customer_info.db")
c_c = conn_customer.cursor()



#c_c.execute("""CREATE TABLE customer (
#       first_name text,
#       last_name text,
#       dob text,
#       cert text,
#       cert_check integer,
#       no_dives text,
#       last_dive text,
#       liability_form integer,
#       total_cost integer
#       balance integer

#       )""")

conn_staff = sqlite3.connect("staff_info.db")
c_s = conn_staff.cursor()

#c_s.execute("""CREATE TABLE staff(
#                first_name text,
#                last_name text,
#                pro_number text,
#                insurance_number text,
#                insurance_exp text,
#                highest text,
#                dm integer,
#                owi integer,
#                deep integer,
#                wreck integer,
#                advanced_wreck integer,
#                pb integer,
#                eanx integer,
#                boat integer,
#                nav integer,
#                night integer,
#                sod integer,
#                xr integer,
#                sidemount integer
#                )""")

conn_activities = sqlite3.connect("activities_info.db")
c_a =conn_activities.cursor()

#c_a.execute("""CREATE TABLE activity(
#                activity text,
#                inst_qual text,
#                price text,
#                course integer
#                )""")

#c_a.execute("""CREATE TABLE extras(
#                full_equ_dive text,
#                full_equ_day text,
#                full_equ_upgrade text,
#                computer_day text,
#                torch_day text,
#                bcd_dive text,
#                bcd_day text,
#                bcd_upgrade text,
#                reg_dive text,
#                reg_day text,
#                reg_upgrade text,
#                soft_dive text,
#                soft_day text,
#                soft_upgrade text,
#                eanx_upgrade text,
#                t_15l_upgrade text,
#                t_18l_upgrade text,
#               t_3l_air text,
#               t_3l_100 text,
#               t_6l_50 text,
#               t_6l_100 text,
#               t_12l_50 text,
#               t_12L_100 text,
#               twin_air text,
#               twin_eanx text,
#               rebreather text,
#               sorb text,
#               no_tank text,
#               tech_reg text,
#               back_plate text,
#               wing text,
#               o2_reg text,
#               tech_computer text,
#               tech_torch text,
#               wreck_reel text,
#               smb text,
#               reel text,
#               slate text
#                )""")

conn_dives = sqlite3.connect("dives_record.db")
c_d = conn_dives.cursor()

#c_d.execute("""CREATE TABLE dives(
#                date text,
#                diver_id integer,
#                activity text,
#                guide text,
#                site text,
#                time text,
#                full_equ_dive integer,
#                full_equ_day integer,
#                full_equ_upgrade integer,
#                computer_day integer,
#                torch_day integer,
#                bcd_dive integer,
#                bcd_day integer,
#                bcd_upgrade integer,
#                reg_dive integer,
#                reg_day integer,
#                reg_upgrade integer,
#                soft_dive integer,
#                soft_day integer,
#                soft_upgrade integer,
#                eanx_upgrade integer,
#                t_15l_upgrade integer,
#                t_18l_upgrade integer,
#               t_3l_air integer,
#               t_3l_100 integer,
#               t_6l_50 integer,
#               t_6l_100 integer,
#               t_12l_50 integer,
#               t_12L_100 integer,
#               twin_air integer,
#               twin_eanx integer,
#               rebreather integer,
#               sorb integer,
#               no_tank integer,
#               tech_reg integer,
#               back_plate integer,
#               wing integer,
#               o2_reg integer,
#               tech_computer integer,
#               tech_torch integer,
#               wreck_reel integer,
#               smb integer,
#               reel integer,
#               slate integer
#           )""")


conn_tab = sqlite3.connect("tabs_info.db")
c_t = conn_tab.cursor()

#c_t.execute("""CREATE TABLE tabs (
#            diver_id integer,
#            date_paid text,
#            amount_paid text
#            )""")

conn_payment = sqlite3.connect("payment.db")
c_p = conn_payment.cursor()
#c_p.execute("""CREATE TABLE payment (
#               diver_id integer,
#               date text,
#               amount integer
#               )""")
#Lists and variables

currentyear = datetime.now().year
currentmonth = datetime.now().month
currentday= datetime.now().day
oid = ""
date = ""

c_s.execute("SELECT first_name FROM staff")
x1 = c_s.fetchall()
x2 = [list(x) for x in x1]
lists = itertools.chain(*x2)
staff_list = list(lists)

c_a.execute("SELECT activity FROM activity")
a1 = c_a.fetchall()
a2 = [list(x) for x in a1]
lists2 = itertools.chain(*a2)
activity_list = list(lists2)


certification_level = [" ",
                       "none",
                       "Basic Diver",
                       "Open Water Diver",
                       "Advanced Diver",
                       "Rescue Diver",
                       "Divemaster",
                       "Instructor",
                       "Extended Range",
                       "Technical Extended Range",
                       "Advanced Wreck",
                       ]

dive_sites= [" ",
             "Cyclops",
             "Green Bay",
             "Chaple",
             "De Costa Bay",
             "Nissia Caves",
             "Mimosa",
             "Kaliva",
             "Paramount",
             "Konnos Beach",
             "Chapel",
             "Blue Lagoon",
             "Tunnels and Caves",
             "Canyon",
             "Ammos beach",
             "Amphora",
             "Theater",
             "Bat Caves",
             "Sheep Dip",
             "Elphida Wreck",
             "Zenobia",
             "Classroom",
             ]

inst_qual_list = [" ",
                  "DM",
                  "OWI",
                  "DEEP",
                  "WRECK",
                  "ADVANCED WRECK",
                  "PB",
                  "EANX",
                  "BOAT",
                  "NAV",
                  "NIGHT",
                  "SOD",
                  "XR",
                  "SIDEMOUNT"
                  ]

am = "am"
mid = "mid-am"
pm= "pm"
zen = "Zenobia"
co = "courses"
placeholder = " "




class MainWindow(QMainWindow):
    def __init__(self):
        QMainWindow.__init__(self)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        ## PRINT ==> SYSTEM
        print('System: ' + platform.system())
        print('Version: ' +platform.release())

        self.ui.todays_dive_button.clicked.connect(self.todays_date)
#        self.ui.add_new_am_dive_button.clicked.connect(self.open_add_am_diver)
 #       self.ui.add_new_mid_dive_button.clicked.connect(self.open_add_mid_am_diver)
 #       self.ui.add_new_pm_dive_button.clicked.connect(self.open_add_pm_diver)
 #       self.ui.add_new_zenobia_button.clicked.connect(self.open_add_zen_diver)
 #       self.ui.add_new_course_button.clicked.connect(self.open_add_courses_diver)
        self.ui.calendar_widget.clicked[QtCore.QDate].connect(self.get_date)
        self.ui.am_remove_diver_button.clicked.connect(self.delete_am_diver)
        self.ui.mam_remove_diver_button.clicked.connect(self.delete_mam_diver)
        self.ui.pm_remove_diver_button.clicked.connect(self.delete_pm_diver)
        self.ui.z_remove_diver_button.clicked.connect(self.delete_z_diver)
        self.ui.ci_remove_diver_button.clicked.connect(self.delete_co_diver)
        self.refresh_all()
        self.ui.refresh_button.clicked.connect(self.refresh_all)
        self.ui.calendar_widget.clicked.connect(self.refresh_all)
        self.ui.am_das_combo.addItem(" ")
        self.ui.mam_das_combo.addItem(" ")
        self.ui.pm_das_combo.addItem(" ")
        self.ui.z_das_combo.addItem(" ")
        self.ui.co_das_combo.addItem(" ")
        for i in staff_list:
            self.ui.am_das_combo.addItem(i)
            self.ui.mam_das_combo.addItem(i)
            self.ui.pm_das_combo.addItem(i)
            self.ui.z_das_combo.addItem(i)
            self.ui.co_das_combo.addItem(i)

        for i in dive_sites:
            self.ui.am_dive_site_combo.addItem(i)
            self.ui.mam_dive_site_combo.addItem(i)
            self.ui.pm_dive_site_combo.addItem(i)
            self.ui.z_dive_site_combo.addItem(i)
            self.ui.co_dive_site_combo.addItem(i)

        self.ui.update_am_dive_button.clicked.connect(self.update_am_dive_record)
        self.ui.update_mid_am_dive_button.clicked.connect(self.update_mam_dive_record)
        self.ui.update_pm_dive_button.clicked.connect(self.update_pm_dive_record)
        self.ui.update_zenobia_button.clicked.connect(self.update_zen_dive_record)
        self.ui.update_courses_button.clicked.connect(self.update_courses_record)
        self.ui.pushButton.clicked.connect(self.add_customer)
        self.ui.search_customer_button.clicked.connect(self.search_customer)
        self.ui.delete_customer_button.clicked.connect(self.delete_customer)
        self.ui.list_all_button.clicked.connect(self.list_all)
        self.ui.search_customer_id_button_.clicked.connect(self.populate_customer_record)
        self.ui.update_customer_button.clicked.connect(self.update_customer_record)
        self.ui.pushButton_2.clicked.connect(self.add_staff)
        self.ui.add_search_staff_button.clicked.connect(self.populate_boxes)
        self.ui.delete_staff_button.clicked.connect(self.delete_staff)
        self.ui.update_button.clicked.connect(self.update_staff)
        self.ui.clear_staff_button.clicked.connect(self.clear_staff)
        self.ui.add_activity_button.clicked.connect(self.add_activity)
        self.ui.list_activities_button.clicked.connect(self.list_activities)
        self.ui.inst_cert_combo.clear()
        self.ui.pushButton_3.clicked.connect(self.extras)
        for i in inst_qual_list:
            self.ui.inst_cert_combo.addItem(i)
        self.open_extras()
        self.ui.delete_record_button.clicked.connect(self.delete_activity)
        self.ui.delete_staff_button.clicked.connect(self.delete_staff)
        self.list_staff()
        self.ui.search_customer_button.clicked.connect(self.search_customer)
        self.ui.list_all_button.clicked.connect(self.list_all_tabs)
        self.ui.search_button.clicked.connect(self.refresh_tab)
        self.ui.make_payment_button.clicked.connect(self.payment)
        self.ui.add_new_am_dive_button.clicked.connect(self.am_diver_page)
        self.ui.am_add_to_dive_button.clicked.connect(self.add_am_diver)
        self.ui.mam_add_to_dive_button.clicked.connect(self.add_mam_diver)
        self.ui.add_new_pm_dive_button.clicked.connect(self.pm_diver_page)
        self.ui.pm_add_to_dive_button.clicked.connect(self.add_pm_diver)
        self.ui.add_new_mid_dive_button.clicked.connect(self.mam_diver_page)
        self.ui.add_new_zenobia_button.clicked.connect(self.zen_diver_page)
        self.ui.z_add_to_dive_button.clicked.connect(self.add_zen_diver)
        self.ui.add_new_course_button.clicked.connect(self.co_diver_page)
        self.ui.co_add_to_dive_button.clicked.connect(self.add_co_diver)
        self.ui.am_search_customer_button.clicked.connect(self.search_am_customer)
        self.ui.mam_search_customer_button.clicked.connect(self.search_mam_customer)
        self.ui.pm_search_customer_button.clicked.connect(self.search_pm_customer)
        self.ui.z_search_customer_button.clicked.connect(self.search_zen_customer)
        self.ui.co_search_customer_button.clicked.connect(self.search_co_customer)

        self.ui.am_sorb_entry.setText("0")
        self.ui.mam_sorb_entry_2.setText("0")
        self.ui.pm_sorb_entry.setText("0")
        self.ui.z_sorb_entry.setText("0")
        self.ui.co_sorb_entry.setText("0")

        self.ui.cert_combo.clear()
        for i in certification_level:
            self.ui.cert_combo.addItem(i)
        for i in certification_level:
            self.ui.cert_combo_2.addItem(i)
        for i in activity_list:
            self.ui.am_activity_combo.addItem(i)
            self.ui.mam_activity_combo.addItem(i)
            self.ui.pm_activity_combo.addItem(i)
            self.ui.z_activity_combo.addItem(i)
            self.ui.co_activity_combo.addItem(i)

        ########################################################################
        ## START - WINDOW ATTRIBUTES
        ########################################################################

        ## REMOVE ==> STANDARD TITLE BAR
        UIFunctions.removeTitleBar(True)
        ## ==> END ##

        ## SET ==> WINDOW TITLE
        self.setWindowTitle('Get Wet Divers')
        UIFunctions.labelTitle(self, 'Get Wet Divers booking system')
#        UIFunctions.labelDescription(self, '')
        ## ==> END ##

        ## WINDOW SIZE ==> DEFAULT SIZE
        startSize = QSize(1000, 720)
        self.resize(startSize)
        self.setMinimumSize(startSize)

        #UIFunctions.enableMaximumSize(self, 500, 720)
        ## ==> END ##

        ## ==> CREATE MENUS
        ########################################################################

        ## ==> TOGGLE MENU SIZE
        self.ui.btn_toggle_menu.clicked.connect(lambda: UIFunctions.toggleMenu(self, 220, True))
        ## ==> END ##

        ## ==> ADD CUSTOM MENUS
        self.ui.stackedWidget.setMinimumWidth(20)
        UIFunctions.addNewMenu(self, "Dives", "btn_home", "url(icons8-scuba-diving-16.png)", True)
        UIFunctions.addNewMenu(self, "New Customer", "btn_new_customer", "url(cil-user-follow.png)", True)
        UIFunctions.addNewMenu(self, "Find Customer", "btn_find_customer", "url(cil-magnifying-glass.png)", True)
        UIFunctions.addNewMenu(self, "Staff", "btn_staff", "url(icons8-staff-16.png)",True)
        UIFunctions.addNewMenu(self, "Accounts", "btn_accounts", "url(icons8-euro-16.png)",True)
        UIFunctions.addNewMenu(self, "Activities", "btn_activities", "url(icons8-to-do-16.png)",True)
        ## ==> END ##

        # START MENU => SELECTION
        UIFunctions.selectStandardMenu(self, "btn_home")
        ## ==> END ##

        ## ==> START PAGE
        self.ui.stackedWidget.setCurrentWidget(self.ui.page_dives)
        ## ==> END ##

        ## USER ICON ==> SHOW HIDE
        UIFunctions.userIcon(self, "GWD", "url(facebook logo64.png)", True)
        ## ==> END ##


        ## ==> MOVE WINDOW / MAXIMIZE / RESTORE
        ########################################################################
        def moveWindow(event):
            # IF MAXIMIZED CHANGE TO NORMAL
            if UIFunctions.returStatus() == 1:
                UIFunctions.maximize_restore(self)

            # MOVE WINDOW
            if event.buttons() == Qt.LeftButton:
                self.move(self.pos() + event.globalPos() - self.dragPos)
                self.dragPos = event.globalPos()
                event.accept()

        # WIDGET TO MOVE
        self.ui.frame_label_top_btns.mouseMoveEvent = moveWindow

        UIFunctions.uiDefinitions(self)

        self.showFullScreen()


    def todays_date(self):
        self.ui.calendar_widget.setSelectedDate(QDate(currentyear, currentmonth, currentday))
        self.ui.refresh_button.click()

    def Button(self):
        # GET BT CLICKED
        btnWidget = self.sender()

        # PAGE HOME
        if btnWidget.objectName() == "btn_home":
            self.ui.stackedWidget.setCurrentWidget(self.ui.page_dives)
            UIFunctions.resetStyle(self, "btn_home")
            UIFunctions.labelPage(self, "Dives")
            btnWidget.setStyleSheet(UIFunctions.selectMenu(btnWidget.styleSheet()))

        # PAGE NEW USER
        if btnWidget.objectName() == "btn_new_customer":
            self.ui.stackedWidget.setCurrentWidget(self.ui.page_add_new_customer)
            UIFunctions.resetStyle(self, "btn_new_customer")
            UIFunctions.labelPage(self, "New Customer")
            btnWidget.setStyleSheet(UIFunctions.selectMenu(btnWidget.styleSheet()))

        # PAGE WIDGETS
        if btnWidget.objectName() == "btn_find_customer":
            self.ui.stackedWidget.setCurrentWidget(self.ui.page_find_customer)
            UIFunctions.resetStyle(self, "btn_find_customer")
            UIFunctions.labelPage(self, "Find Customer")
            btnWidget.setStyleSheet(UIFunctions.selectMenu(btnWidget.styleSheet()))

        if btnWidget.objectName() == "btn_staff":
            self.ui.stackedWidget.setCurrentWidget(self.ui.page_staff)
            UIFunctions.resetStyle(self, "btn_staff")
            UIFunctions.labelPage(self, "Staff")
            btnWidget.setStyleSheet(UIFunctions.selectMenu(btnWidget.styleSheet()))

        if btnWidget.objectName() == "btn_accounts":
            self.ui.stackedWidget.setCurrentWidget(self.ui.page_accounts)
            UIFunctions.resetStyle(self, "btn_accounts")
            UIFunctions.labelPage(self, "Accounts")
            btnWidget.setStyleSheet(UIFunctions.selectMenu(btnWidget.styleSheet()))

        if btnWidget.objectName() == "btn_activities":
            self.ui.stackedWidget.setCurrentWidget(self.ui.page_activities)
            UIFunctions.resetStyle(self, "btn_activities")
            UIFunctions.labelPage(self, "Activities")
            btnWidget.setStyleSheet(UIFunctions.selectMenu(btnWidget.styleSheet()))

    def refresh_all(self):
        self.get_date()
        self.refresh_am_dive()
        self.refresh_mid_am_dive()
        self.refresh_pm_dive()
        self.refresh_zenobia_dive()
        self.refresh_courses_dive()

    def am_diver_page(self):
        self.ui.stackedWidget.setCurrentWidget(self.ui.page_am_dive_add)
        UIFunctions.resetStyle(self, "btn_am_dive_add")
        UIFunctions.labelPage(self, "Add am Diver")

    def mam_diver_page(self):
        self.ui.stackedWidget.setCurrentWidget(self.ui.page_mam_dive_add)
        UIFunctions.resetStyle(self, "btn_mam_dive_add")
        UIFunctions.labelPage(self, "Add mid -am Diver")

    def pm_diver_page(self):
        self.ui.stackedWidget.setCurrentWidget(self.ui.page_pm_dive_add)
        UIFunctions.resetStyle(self, "btn_pm_dive_add")
        UIFunctions.labelPage(self, "Add pm Diver")

    def zen_diver_page(self):
        self.ui.stackedWidget.setCurrentWidget(self.ui.page_zen_dive_add)
        UIFunctions.resetStyle(self, "btn_zen_dive_add")
        UIFunctions.labelPage(self, "Add Zenobia Diver")

    def co_diver_page(self):
        self.ui.stackedWidget.setCurrentWidget(self.ui.page_co_add)
        UIFunctions.resetStyle(self, "btn_co_add")
        UIFunctions.labelPage(self, "Add courses Diver")

    def get_date(self):
        global date
        self.cal = self.ui.calendar_widget.selectedDate()
        self.date =  self.cal.toString("dd/MM/yyyy")
        date = self.date

    def refresh_am_dive(self):
        global date
        self.ui.am_dive_table.setRowCount(0)

        conn_dives = sqlite3.connect("dives_record.db")
        c_d = conn_dives.cursor()
        conn_customer = sqlite3.connect("customer_info.db")
        c_c = conn_customer.cursor()
        tablerow = 0
        rowcount = 0
        i = 0


        for row in c_d.execute("SELECT diver_id, activity, guide, site FROM dives WHERE date=? AND time=?",(date, am)):
            rowcount +=1
            self.ui.am_dive_table.setRowCount(rowcount)
            self.ui.am_dive_table.setItem(tablerow, 0, QtWidgets.QTableWidgetItem(str(row[0])))
            self.ui.am_dive_table.setItem(tablerow, 1, QtWidgets.QTableWidgetItem(row[1]))
            self.ui.am_dive_table.setItem(tablerow, 5, QtWidgets.QTableWidgetItem(0))
            self.ui.am_dive_table.setItem(tablerow, 6, QtWidgets.QTableWidgetItem(str(row[0])))
            item = QtWidgets.QTableWidgetItem()
            item.setCheckState(QtCore.Qt.Unchecked)
            self.ui.am_dive_table.setItem(tablerow, 3, item)
            item2 = QtWidgets.QTableWidgetItem()
            item2.setCheckState(QtCore.Qt.Unchecked)
            self.ui.am_dive_table.setItem(tablerow, 4, item2)
            self.ui.am_dive_site_combo.setCurrentText(row[3])

            for j in staff_list:
                self.ui.am_dive_table.setItem(i, 2, QtWidgets.QTableWidgetItem(""))
                combobox = staff_list_combobox_table(self)
                self.ui.am_dive_table.setCellWidget(i, 2, combobox)
            self.ui.am_dive_table.cellWidget(i,2).setCurrentText(row[2])

            i += 1
            tablerow += 1


        for row in range(tablerow):
            oid = self.ui.am_dive_table.item(row,0).text()
            c_c.execute("SELECT first_name, cert_check, liability_form, balance FROM customer WHERE oid=" + oid)
            x = c_c.fetchall()

            name = list(map(itemgetter(0), x))
            cert = list(map(itemgetter(1), x))
            liab = list(map(itemgetter(2), x))
            bala = list(map(itemgetter(3), x))
            name1 = name[0]
            cert1 = cert[0]
            liab1 = liab[0]
            bala1 = bala[0]

            if str(cert1) == "1":
                self.ui.am_dive_table.item(row,3).setCheckState(QtCore.Qt.Checked)
#
            if str(liab1) == "1":
                self.ui.am_dive_table.item(row,4).setCheckState(QtCore.Qt.Checked)

            self.ui.am_dive_table.item(row, 0).setText(name1)
            self.ui.am_dive_table.item(row, 5).setText("€" + str(bala1))

            if bala1 > 0:
                item3 = QtWidgets.QTableWidgetItem()
                brush = QtGui.QBrush(QtGui.QColor(255, 161, 46, 202))
                brush.setStyle(QtCore.Qt.SolidPattern)
                self.ui.am_dive_table.item(row, 0).setBackground(brush)

            if not self.ui.am_dive_table.item(row, 3).checkState() or not self.ui.am_dive_table.item(row, 4).checkState():
                item3 = QtWidgets.QTableWidgetItem()
                brush = QtGui.QBrush(QtGui.QColor(255, 0, 0, 173))
                brush.setStyle(QtCore.Qt.SolidPattern)
                self.ui.am_dive_table.item(row, 0).setBackground(brush)



        conn_customer.commit()
        conn_customer.close()
        conn_dives.commit()
        conn_dives.close()

    def update_am_dive_record(self):
        global date
        global am
        conn_customer = sqlite3.connect("customer_info.db")
        conn_dives = sqlite3.connect("dives_record.db")
        c_c = conn_customer.cursor()
        c_d = conn_dives.cursor()

        rowcount = self.ui.am_dive_table.rowCount()
        for i in range(rowcount):
            oid = self.ui.am_dive_table.item(i, 6).text()
            cert = self.ui.am_dive_table.item(i, 3).checkState()
            liab = self.ui.am_dive_table.item(i, 4).checkState()
            cert = int(cert)
            liab = int(liab)
            if cert == 2:
                cert =1
            if liab == 2:
                liab = 1

            c_c.execute("UPDATE customer SET cert_check = ?, liability_form = ? WHERE oid = ?", (cert, liab, oid))
            combo = self.ui.am_dive_table.cellWidget(i,2).currentText()
            combo2 = self.ui.am_dive_site_combo.currentText()
            c_d.execute("UPDATE dives SET guide = ?, site = ? WHERE date = ? AND diver_id = ? AND time = ?",(combo, combo2, date, oid, am))

        conn_customer.commit()
        conn_customer.close()
        conn_dives.commit()
        conn_dives.close()
        self.ui.refresh_button.click()

    def refresh_mid_am_dive(self):
        global date
        self.ui.mid_am_dive_table.setRowCount(0)

        conn_dives = sqlite3.connect("dives_record.db")
        c_d = conn_dives.cursor()
        conn_customer = sqlite3.connect("customer_info.db")
        c_c = conn_customer.cursor()
        tablerow = 0
        rowcount = 0
        i = 0

        for row in c_d.execute("SELECT diver_id, activity, guide, site FROM dives WHERE date=? AND time=?",
                               (date, mid)):
            rowcount += 1
            self.ui.mid_am_dive_table.setRowCount(rowcount)
            self.ui.mid_am_dive_table.setItem(tablerow, 0, QtWidgets.QTableWidgetItem(str(row[0])))
            self.ui.mid_am_dive_table.setItem(tablerow, 1, QtWidgets.QTableWidgetItem(row[1]))
            self.ui.mid_am_dive_table.setItem(tablerow, 5, QtWidgets.QTableWidgetItem(0))
            self.ui.mid_am_dive_table.setItem(tablerow, 6, QtWidgets.QTableWidgetItem(str(row[0])))
            item = QtWidgets.QTableWidgetItem()
            item.setCheckState(QtCore.Qt.Unchecked)
            self.ui.mid_am_dive_table.setItem(tablerow, 3, item)
            item2 = QtWidgets.QTableWidgetItem()
            item2.setCheckState(QtCore.Qt.Unchecked)
            self.ui.mid_am_dive_table.setItem(tablerow, 4, item2)
            self.ui.mam_dive_site_combo.setCurrentText(row[3])
            for j in staff_list:
                self.ui.mid_am_dive_table.setItem(i, 2, QtWidgets.QTableWidgetItem(""))
                combobox = staff_list_combobox_table(self)
                self.ui.mid_am_dive_table.setCellWidget(i, 2, combobox)
            self.ui.mid_am_dive_table.cellWidget(i, 2).setCurrentText(row[2])

            i += 1
            tablerow += 1

        for row in range(tablerow):
            oid = self.ui.mid_am_dive_table.item(row, 0).text()
            c_c.execute("SELECT first_name, cert_check, liability_form, balance FROM customer WHERE oid=" + oid)
            x = c_c.fetchall()

            nmid_ame = list(map(itemgetter(0), x))
            cert = list(map(itemgetter(1), x))
            liab = list(map(itemgetter(2), x))
            bala = list(map(itemgetter(3), x))
            name1 = nmid_ame[0]
            cert1 = cert[0]
            liab1 = liab[0]
            bala1 = bala[0]

            if str(cert1) == "1":
                self.ui.mid_am_dive_table.item(row, 3).setCheckState(QtCore.Qt.Checked)
            #
            if str(liab1) == "1":
                self.ui.mid_am_dive_table.item(row, 4).setCheckState(QtCore.Qt.Checked)

            self.ui.mid_am_dive_table.item(row, 0).setText(name1)
            self.ui.mid_am_dive_table.item(row, 5).setText("€" + str(bala1))

            if bala1 > 0:
                item3 = QtWidgets.QTableWidgetItem()
                brush = QtGui.QBrush(QtGui.QColor(255, 161, 46, 202))
                brush.setStyle(QtCore.Qt.SolidPattern)
                self.ui.mid_am_dive_table.item(row, 0).setBackground(brush)

            if not self.ui.mid_am_dive_table.item(row, 3).checkState() or not self.ui.mid_am_dive_table.item(row,
                                                                                                             4).checkState():
                item3 = QtWidgets.QTableWidgetItem()
                brush = QtGui.QBrush(QtGui.QColor(255, 0, 0, 173))
                brush.setStyle(QtCore.Qt.SolidPattern)
                self.ui.mid_am_dive_table.item(row, 0).setBackground(brush)

        conn_customer.commit()
        conn_customer.close()
        conn_dives.commit()
        conn_dives.close()

    def update_mam_dive_record(self):
        global date
        global mid
        conn_customer = sqlite3.connect("customer_info.db")
        conn_dives = sqlite3.connect("dives_record.db")
        c_c = conn_customer.cursor()
        c_d = conn_dives.cursor()

        rowcount = self.ui.mid_am_dive_table.rowCount()
        for i in range(rowcount):
            oid = self.ui.mid_am_dive_table.item(i, 6).text()
            cert = self.ui.mid_am_dive_table.item(i, 3).checkState()
            liab = self.ui.mid_am_dive_table.item(i, 4).checkState()
            cert = int(cert)
            liab = int(liab)
            if cert == 2:
                cert = 1
            if liab == 2:
                liab = 1
            c_c.execute("UPDATE customer SET cert_check = ?, liability_form = ? WHERE oid = ?", (cert, liab, oid))
            combo = self.ui.mid_am_dive_table.cellWidget(i, 2).currentText()
            combo2 = self.ui.mam_dive_site_combo.currentText()
            c_d.execute("UPDATE dives SET guide = ?, site = ? WHERE date = ? AND diver_id = ? AND time = ?",
                        (combo, combo2, date, oid, mid))

        conn_customer.commit()
        conn_customer.close()
        conn_dives.commit()
        conn_dives.close()
        self.ui.refresh_button.click()

    def update_pm_dive_record(self):
        global date
        global pm
        conn_customer = sqlite3.connect("customer_info.db")
        conn_dives = sqlite3.connect("dives_record.db")
        c_c = conn_customer.cursor()
        c_d = conn_dives.cursor()

        rowcount = self.ui.pm_dive_table.rowCount()
        for i in range(rowcount):
            oid = self.ui.pm_dive_table.item(i, 6).text()
            cert = self.ui.pm_dive_table.item(i, 3).checkState()
            liab = self.ui.pm_dive_table.item(i, 4).checkState()
            cert = int(cert)
            liab = int(liab)
            if cert == 2:
                cert = 1
            if liab == 2:
                liab = 1
            c_c.execute("UPDATE customer SET cert_check = ?, liability_form = ? WHERE oid = ?", (cert, liab, oid))
            combo = self.ui.pm_dive_table.cellWidget(i, 2).currentText()
            combo2 = self.ui.pm_dive_site_combo.currentText()
            c_d.execute("UPDATE dives SET guide = ?, site = ? WHERE date = ? AND diver_id = ? AND time = ?",
                        (combo, combo2, date, oid, pm))

        conn_customer.commit()
        conn_customer.close()
        conn_dives.commit()
        conn_dives.close()
        self.ui.refresh_button.click()

    def refresh_pm_dive(self):
        global date
        self.ui.pm_dive_table.setRowCount(0)

        conn_dives = sqlite3.connect("dives_record.db")
        c_d = conn_dives.cursor()
        conn_customer = sqlite3.connect("customer_info.db")
        c_c = conn_customer.cursor()
        tablerow = 0
        rowcount = 0
        i = 0

        for row in c_d.execute("SELECT diver_id, activity, guide, site FROM dives WHERE date=? AND time=?", (date, pm)):
            rowcount += 1
            self.ui.pm_dive_table.setRowCount(rowcount)
            self.ui.pm_dive_table.setItem(tablerow, 0, QtWidgets.QTableWidgetItem(str(row[0])))
            self.ui.pm_dive_table.setItem(tablerow, 1, QtWidgets.QTableWidgetItem(row[1]))
            self.ui.pm_dive_table.setItem(tablerow, 5, QtWidgets.QTableWidgetItem(0))
            self.ui.pm_dive_table.setItem(tablerow, 6, QtWidgets.QTableWidgetItem(str(row[0])))
            item = QtWidgets.QTableWidgetItem()
            item.setCheckState(QtCore.Qt.Unchecked)
            self.ui.pm_dive_table.setItem(tablerow, 3, item)
            item2 = QtWidgets.QTableWidgetItem()
            item2.setCheckState(QtCore.Qt.Unchecked)
            self.ui.pm_dive_table.setItem(tablerow, 4, item2)
            self.ui.pm_dive_site_combo.setCurrentText(row[3])
            for j in staff_list:
                self.ui.pm_dive_table.setItem(i, 2, QtWidgets.QTableWidgetItem(""))
                combobox = staff_list_combobox_table(self)
                self.ui.pm_dive_table.setCellWidget(i, 2, combobox)
            self.ui.pm_dive_table.cellWidget(i, 2).setCurrentText(row[2])

            i += 1
            tablerow += 1

        for row in range(tablerow):
            oid = self.ui.pm_dive_table.item(row, 0).text()
            c_c.execute("SELECT first_name, cert_check, liability_form, balance FROM customer WHERE oid=" + oid)
            x = c_c.fetchall()

            npme = list(map(itemgetter(0), x))
            cert = list(map(itemgetter(1), x))
            liab = list(map(itemgetter(2), x))
            bala = list(map(itemgetter(3), x))
            name1 = npme[0]
            cert1 = cert[0]
            liab1 = liab[0]
            bala1 = bala[0]

            if str(cert1) == "1":
                self.ui.pm_dive_table.item(row, 3).setCheckState(QtCore.Qt.Checked)
            #
            if str(liab1) == "1":
                self.ui.pm_dive_table.item(row, 4).setCheckState(QtCore.Qt.Checked)

            self.ui.pm_dive_table.item(row, 0).setText(name1)
            self.ui.pm_dive_table.item(row, 5).setText("€" + str(bala1))

            if bala1 > 0:
                item3 = QtWidgets.QTableWidgetItem()
                brush = QtGui.QBrush(QtGui.QColor(255, 161, 46, 202))
                brush.setStyle(QtCore.Qt.SolidPattern)
                self.ui.pm_dive_table.item(row, 0).setBackground(brush)

            if not self.ui.pm_dive_table.item(row, 3).checkState() or not self.ui.pm_dive_table.item(row,
                                                                                                     4).checkState():
                item3 = QtWidgets.QTableWidgetItem()
                brush = QtGui.QBrush(QtGui.QColor(255, 0, 0, 173))
                brush.setStyle(QtCore.Qt.SolidPattern)
                self.ui.pm_dive_table.item(row, 0).setBackground(brush)

        conn_customer.commit()
        conn_customer.close()
        conn_dives.commit()
        conn_dives.close()

    def refresh_zenobia_dive(self):
        global date
        self.ui.zenobia_table.setRowCount(0)

        conns = sqlite3.connect("dives_record.db")
        c_d = conns.cursor()
        conn_customer = sqlite3.connect("customer_info.db")
        c_c = conn_customer.cursor()
        tablerow = 0
        rowcount = 0
        i = 0

        for row in c_d.execute("SELECT diver_id, activity, guide, site FROM dives WHERE date=? AND time=?", (date, zen)):
            rowcount += 1
            self.ui.zenobia_table.setRowCount(rowcount)
            self.ui.zenobia_table.setItem(tablerow, 0, QtWidgets.QTableWidgetItem(str(row[0])))
            self.ui.zenobia_table.setItem(tablerow, 1, QtWidgets.QTableWidgetItem(row[1]))
            self.ui.zenobia_table.setItem(tablerow, 5, QtWidgets.QTableWidgetItem(0))
            self.ui.zenobia_table.setItem(tablerow, 6, QtWidgets.QTableWidgetItem(str(row[0])))
            item = QtWidgets.QTableWidgetItem()
            item.setCheckState(QtCore.Qt.Unchecked)
            self.ui.zenobia_table.setItem(tablerow, 3, item)
            item2 = QtWidgets.QTableWidgetItem()
            item2.setCheckState(QtCore.Qt.Unchecked)
            self.ui.zenobia_table.setItem(tablerow, 4, item2)
            self.ui.z_dive_site_combo.setCurrentText(row[3])
            for j in staff_list:
                self.ui.zenobia_table.setItem(i, 2, QtWidgets.QTableWidgetItem(""))
                combobox = staff_list_combobox_table(self)
                self.ui.zenobia_table.setCellWidget(i, 2, combobox)
            self.ui.zenobia_table.cellWidget(i, 2).setCurrentText(row[2])

            i += 1
            tablerow += 1

        for row in range(tablerow):
            oid = self.ui.zenobia_table.item(row, 0).text()
            c_c.execute("SELECT first_name, cert_check, liability_form, balance FROM customer WHERE oid=" + oid)
            x = c_c.fetchall()

            nzenobiae = list(map(itemgetter(0), x))
            cert = list(map(itemgetter(1), x))
            liab = list(map(itemgetter(2), x))
            bala = list(map(itemgetter(3), x))
            name1 = nzenobiae[0]
            cert1 = cert[0]
            liab1 = liab[0]
            bala1 = bala[0]

            if str(cert1) == "1":
                self.ui.zenobia_table.item(row, 3).setCheckState(QtCore.Qt.Checked)
            #
            if str(liab1) == "1":
                self.ui.zenobia_table.item(row, 4).setCheckState(QtCore.Qt.Checked)

            self.ui.zenobia_table.item(row, 0).setText(name1)
            self.ui.zenobia_table.item(row, 5).setText("€" + str(bala1))

            if bala1 > 0:
                item3 = QtWidgets.QTableWidgetItem()
                brush = QtGui.QBrush(QtGui.QColor(255, 161, 46, 202))
                brush.setStyle(QtCore.Qt.SolidPattern)
                self.ui.zenobia_table.item(row, 0).setBackground(brush)

            if not self.ui.zenobia_table.item(row, 3).checkState() or not self.ui.zenobia_table.item(row,
                                                                                                     4).checkState():
                item3 = QtWidgets.QTableWidgetItem()
                brush = QtGui.QBrush(QtGui.QColor(255, 0, 0, 173))
                brush.setStyle(QtCore.Qt.SolidPattern)
                self.ui.zenobia_table.item(row, 0).setBackground(brush)

        conn_customer.commit()
        conn_customer.close()
        conns.commit()
        conns.close()

    def update_zen_dive_record(self):
        global date
        global zen
        conn_customer = sqlite3.connect("customer_info.db")
        conn_dives = sqlite3.connect("dives_record.db")
        c_c = conn_customer.cursor()
        c_d = conn_dives.cursor()

        rowcount = self.ui.zenobia_table.rowCount()
        for i in range(rowcount):
            oid = self.ui.zenobia_table.item(i, 6).text()
            cert = self.ui.zenobia_table.item(i, 3).checkState()
            liab = self.ui.zenobia_table.item(i, 4).checkState()
            cert = int(cert)
            liab = int(liab)
            if cert == 2:
                cert = 1
            if liab == 2:
                liab = 1
            c_c.execute("UPDATE customer SET cert_check = ?, liability_form = ? WHERE oid = ?", (cert, liab, oid))
            combo = self.ui.zenobia_table.cellWidget(i, 2).currentText()
            combo2 = self.ui.z_dive_site_combo.currentText()
            c_d.execute("UPDATE dives SET guide = ?, site = ? WHERE date = ? AND diver_id = ? AND time = ?",
                        (combo, combo2, date, oid, zen))

        conn_customer.commit()
        conn_customer.close()
        conn_dives.commit()
        conn_dives.close()
        self.ui.refresh_button.click()

    def refresh_courses_dive(self):
        global date
        self.ui.courses_table.setRowCount(0)

        conns = sqlite3.connect("dives_record.db")
        c_d = conns.cursor()
        conn_customer = sqlite3.connect("customer_info.db")
        c_c = conn_customer.cursor()
        tablerow = 0
        rowcount = 0
        i = 0

        for row in c_d.execute("SELECT diver_id, activity, guide, site FROM dives WHERE date=? AND time=?", (date, co)):
            rowcount += 1
            self.ui.courses_table.setRowCount(rowcount)
            self.ui.courses_table.setItem(tablerow, 0, QtWidgets.QTableWidgetItem(str(row[0])))
            self.ui.courses_table.setItem(tablerow, 1, QtWidgets.QTableWidgetItem(row[1]))
            self.ui.courses_table.setItem(tablerow, 5, QtWidgets.QTableWidgetItem(0))
            self.ui.courses_table.setItem(tablerow, 6, QtWidgets.QTableWidgetItem(str(row[0])))
            item = QtWidgets.QTableWidgetItem()
            item.setCheckState(QtCore.Qt.Unchecked)
            self.ui.courses_table.setItem(tablerow, 3, item)
            item2 = QtWidgets.QTableWidgetItem()
            item2.setCheckState(QtCore.Qt.Unchecked)
            self.ui.courses_table.setItem(tablerow, 4, item2)
            self.ui.co_dive_site_combo.setCurrentText(row[3])

            for j in staff_list:
                self.ui.courses_table.setItem(i, 2, QtWidgets.QTableWidgetItem(""))
                combobox = staff_list_combobox_table(self)
                self.ui.courses_table.setCellWidget(i, 2, combobox)
            self.ui.courses_table.cellWidget(i, 2).setCurrentText(row[2])

            i += 1
            tablerow += 1

        for row in range(tablerow):
            oid = self.ui.courses_table.item(row, 0).text()
            c_c.execute("SELECT first_name, cert_check, liability_form, balance FROM customer WHERE oid=" + oid)
            x = c_c.fetchall()

            ncoursese = list(map(itemgetter(0), x))
            cert = list(map(itemgetter(1), x))
            liab = list(map(itemgetter(2), x))
            bala = list(map(itemgetter(3), x))
            name1 = ncoursese[0]
            cert1 = cert[0]
            liab1 = liab[0]
            bala1 = bala[0]

            if str(cert1) == "1":
                self.ui.courses_table.item(row, 3).setCheckState(QtCore.Qt.Checked)
            #
            if str(liab1) == "1":
                self.ui.courses_table.item(row, 4).setCheckState(QtCore.Qt.Checked)

            self.ui.courses_table.item(row, 0).setText(name1)
            self.ui.courses_table.item(row, 5).setText("€" + str(bala1))

            if bala1 > 0:
                item3 = QtWidgets.QTableWidgetItem()
                brush = QtGui.QBrush(QtGui.QColor(255, 161, 46, 202))
                brush.setStyle(QtCore.Qt.SolidPattern)
                self.ui.courses_table.item(row, 0).setBackground(brush)

            if not self.ui.courses_table.item(row, 3).checkState() or not self.ui.courses_table.item(row,
                                                                                                     4).checkState():
                item3 = QtWidgets.QTableWidgetItem()
                brush = QtGui.QBrush(QtGui.QColor(255, 0, 0, 173))
                brush.setStyle(QtCore.Qt.SolidPattern)
                self.ui.courses_table.item(row, 0).setBackground(brush)

        conn_customer.commit()
        conn_customer.close()
        conns.commit()
        conns.close()

    def update_courses_record(self):
        global date
        global co
        conn_customer = sqlite3.connect("customer_info.db")
        conn_dives = sqlite3.connect("dives_record.db")
        c_c = conn_customer.cursor()
        c_d = conn_dives.cursor()

        rowcount = self.ui.courses_table.rowCount()
        for i in range(rowcount):
            oid = self.ui.courses_table.item(i, 6).text()
            cert = self.ui.courses_table.item(i, 3).checkState()
            liab = self.ui.courses_table.item(i, 4).checkState()
            cert = int(cert)
            liab = int(liab)
            if cert == 2:
                cert = 1
            if liab == 2:
                liab = 1
            c_c.execute("UPDATE customer SET cert_check = ?, liability_form = ? WHERE oid = ?", (cert, liab, oid))
            combo = self.ui.courses_table.cellWidget(i, 2).currentText()
            combo2 = self.ui.co_dive_site_combo.currentText()
            c_d.execute("UPDATE dives SET guide = ?, site = ? WHERE date = ? AND diver_id = ? AND time = ?",
                        (combo, combo2, date, oid, co))

        conn_customer.commit()
        conn_customer.close()
        conn_dives.commit()
        conn_dives.close()
        self.ui.refresh_button.click()

    def delete_am_diver(self):
        conn_dives = sqlite3.connect("dives_record.db")
        conn_customer = sqlite3.connect("customer_info.db")
        conn_activities = sqlite3.connect("activities_info.db")
        c_a = conn_activities.cursor()
        c_d = conn_dives.cursor()
        c_c = conn_customer.cursor()
        oid = self.ui.am_delete_diver_entry.text()
        c_c.execute("SELECT total_cost, balance FROM customer WHERE oid =?",(oid))
        c = c_c.fetchone()
        total_cost = c[0]
        balance = c[1]
        running_bal = 0
        c_d.execute("SELECT * FROM dives WHERE diver_id =? AND date = ? AND time = ?",(oid, date, am))
        d = c_d.fetchall()
        c = d[0]

        c_a.execute("SELECT * FROM extras WHERE oid = 1")
        a = c_a.fetchall()
        b= a[0]
        count = len(b)
        sorb = ""
        for i in range(count):
            if c[(i + 6)] == 1:
                running_bal = running_bal + int(b[i])


        if int(c[32]) >0 :
            running_bal = running_bal - int(b[26])
            sorb = int(c[32]) * int(b[26])
            running_bal = running_bal + sorb


        activity = c[2]
        c_a.execute("SELECT price FROM activity WHERE activity =?",([activity]))
        e = c_a.fetchall()
        f = e[0]





        c_a.execute("SELECT price, course FROM activity WHERE activity =?", ([activity]))
        a = c_a.fetchall()
        price = a[0]
        price2 = price[0]
        course = a[0]
        course2 = course[1]
        c_d.execute("SELECT activity FROM dives WHERE diver_id =?", ([oid]))
        x3 = c_d.fetchall()
        list3 = list(map(itemgetter(0), x3))

        count = 0
        for course in list3:
            if course2 == 1:
                if course == activity:
                    count += 1

        if count > 1:
            running_bal = running_bal - int(price2)

        running_bal = running_bal + int(f[0])

        total_cost = total_cost - running_bal
        balance = balance - running_bal


        c_c.execute("UPDATE customer SET total_cost = ?, balance = ? WHERE oid = ?",(total_cost, balance, oid))
        c_d.execute("DELETE FROM dives WHERE diver_id = ? AND date = ? AND time = ?",(oid, date, am))
        self.ui.am_delete_diver_entry.clear()
        self.ui.refresh_button.click()
        conn_customer.commit()
        conn_dives.commit()
        conn_activities.commit()
        conn_customer.close()
        conn_dives.close()
        conn_activities.close()
        self.ui.refresh_button.click()

    def delete_mam_diver(self):
        conn_dives = sqlite3.connect("dives_record.db")
        conn_customer = sqlite3.connect("customer_info.db")
        conn_activities = sqlite3.connect("activities_info.db")
        c_a = conn_activities.cursor()
        c_d = conn_dives.cursor()
        c_c = conn_customer.cursor()
        oid = self.ui.mam_delete_diver_entry.text()
        c_c.execute("SELECT total_cost, balance FROM customer WHERE oid =?",(oid))
        c = c_c.fetchone()
        total_cost = c[0]
        balance = c[1]
        running_bal = 0
        c_d.execute("SELECT * FROM dives WHERE diver_id =? AND date = ? AND time = ?",(oid, date, mid))
        d = c_d.fetchall()
        c = d[0]

        c_a.execute("SELECT * FROM extras WHERE oid = 1")
        a = c_a.fetchall()
        b= a[0]
        count = len(b)
        sorb = ""
        for i in range(count):
            if c[(i + 6)] == 1:
                running_bal = running_bal + int(b[i])


        if int(c[32]) >0 :
            running_bal = running_bal - int(b[26])
            sorb = int(c[32]) * int(b[26])
            running_bal = running_bal + sorb

        activity = c[2]
        c_a.execute("SELECT price FROM activity WHERE activity =?", ([activity]))
        e = c_a.fetchall()
        f = e[0]

        c_a.execute("SELECT price, course FROM activity WHERE activity =?", ([activity]))
        a = c_a.fetchall()
        price = a[0]
        price2 = price[0]
        course = a[0]
        course2 = course[1]
        c_d.execute("SELECT activity FROM dives WHERE diver_id =?", ([oid]))
        x3 = c_d.fetchall()
        list3 = list(map(itemgetter(0), x3))

        count = 0
        for course in list3:
            if course2 == 1:
                if course == activity:
                    count += 1

        if count > 1:
            running_bal = running_bal - int(price2)

        running_bal = running_bal + int(f[0])

        total_cost = total_cost - running_bal
        balance = balance - running_bal

        c_c.execute("UPDATE customer SET total_cost = ?, balance = ? WHERE oid = ?",(total_cost, balance, oid))
        c_d.execute("DELETE FROM dives WHERE diver_id = ? AND date = ? AND time = ?",(oid, date, mid))
        self.ui.mam_delete_diver_entry.clear()
        self.ui.refresh_button.click()
        conn_customer.commit()
        conn_dives.commit()
        conn_activities.commit()
        conn_customer.close()
        conn_dives.close()
        conn_activities.close()
        self.ui.refresh_button.click()

    def delete_pm_diver(self):
        conn_dives = sqlite3.connect("dives_record.db")
        conn_customer = sqlite3.connect("customer_info.db")
        conn_activities = sqlite3.connect("activities_info.db")
        c_a = conn_activities.cursor()
        c_d = conn_dives.cursor()
        c_c = conn_customer.cursor()
        oid = self.ui.pm_delete_diver_entry.text()
        c_c.execute("SELECT total_cost, balance FROM customer WHERE oid =?",(oid))
        c = c_c.fetchone()
        total_cost = c[0]
        balance = c[1]
        running_bal = 0
        c_d.execute("SELECT * FROM dives WHERE diver_id =? AND date = ? AND time = ?",(oid, date, pm))
        d = c_d.fetchall()
        c = d[0]

        c_a.execute("SELECT * FROM extras WHERE oid = 1")
        a = c_a.fetchall()
        b= a[0]
        count = len(b)
        sorb = ""
        for i in range(count):
            if c[(i + 6)] == 1:
                running_bal = running_bal + int(b[i])


        if int(c[32]) >0 :
            running_bal = running_bal - int(b[26])
            sorb = int(c[32]) * int(b[26])
            running_bal = running_bal + sorb

        activity = c[2]
        c_a.execute("SELECT price FROM activity WHERE activity =?", ([activity]))
        e = c_a.fetchall()
        f = e[0]

        c_a.execute("SELECT price, course FROM activity WHERE activity =?", ([activity]))
        a = c_a.fetchall()
        price = a[0]
        price2 = price[0]
        course = a[0]
        course2 = course[1]
        c_d.execute("SELECT activity FROM dives WHERE diver_id =?", ([oid]))
        x3 = c_d.fetchall()
        list3 = list(map(itemgetter(0), x3))

        count = 0
        for course in list3:
            if course2 == 1:
                if course == activity:
                    count += 1

        if count > 1:
            running_bal = running_bal - int(price2)

        running_bal = running_bal + int(f[0])

        total_cost = total_cost - running_bal
        balance = balance - running_bal

        c_c.execute("UPDATE customer SET total_cost = ?, balance = ? WHERE oid = ?",(total_cost, balance, oid))
        c_d.execute("DELETE FROM dives WHERE diver_id = ? AND date = ? AND time = ?",(oid, date, pm))
        self.ui.pm_delete_diver_entry.clear()
        self.ui.refresh_button.click()
        conn_customer.commit()
        conn_dives.commit()
        conn_activities.commit()
        conn_customer.close()
        conn_dives.close()
        conn_activities.close()
        self.ui.refresh_button.click()

    def delete_z_diver(self):
        conn_dives = sqlite3.connect("dives_record.db")
        conn_customer = sqlite3.connect("customer_info.db")
        conn_activities = sqlite3.connect("activities_info.db")
        c_a = conn_activities.cursor()
        c_d = conn_dives.cursor()
        c_c = conn_customer.cursor()
        oid = self.ui.z_delete_diver_entry.text()
        c_c.execute("SELECT total_cost, balance FROM customer WHERE oid =?",(oid))
        c = c_c.fetchone()
        total_cost = c[0]
        balance = c[1]
        running_bal = 0
        c_d.execute("SELECT * FROM dives WHERE diver_id =? AND date = ? AND time = ?",(oid, date, zen))
        d = c_d.fetchall()
        c = d[0]

        c_a.execute("SELECT * FROM extras WHERE oid = 1")
        a = c_a.fetchall()
        b= a[0]
        count = len(b)
        sorb = ""
        for i in range(count):
            if c[(i + 6)] == 1:
                running_bal = running_bal + int(b[i])


        if int(c[32]) >0 :
            running_bal = running_bal - int(b[26])
            sorb = int(c[32]) * int(b[26])
            running_bal = running_bal + sorb

        activity = c[2]
        c_a.execute("SELECT price FROM activity WHERE activity =?", ([activity]))
        e = c_a.fetchall()
        f = e[0]

        c_a.execute("SELECT price, course FROM activity WHERE activity =?", ([activity]))
        a = c_a.fetchall()
        price = a[0]
        price2 = price[0]
        course = a[0]
        course2 = course[1]
        c_d.execute("SELECT activity FROM dives WHERE diver_id =?", ([oid]))
        x3 = c_d.fetchall()
        list3 = list(map(itemgetter(0), x3))

        count = 0
        for course in list3:
            if course2 == 1:
                if course == activity:
                    count += 1

        if count > 1:
            running_bal = running_bal - int(price2)

        running_bal = running_bal + int(f[0])

        total_cost = total_cost - running_bal
        balance = balance - running_bal

        c_c.execute("UPDATE customer SET total_cost = ?, balance = ? WHERE oid = ?",(total_cost, balance, oid))
        c_d.execute("DELETE FROM dives WHERE diver_id = ? AND date = ? AND time = ?",(oid, date, zen))
        self.ui.z_delete_diver_entry.clear()
        self.ui.refresh_button.click()
        conn_customer.commit()
        conn_dives.commit()
        conn_activities.commit()
        conn_customer.close()
        conn_dives.close()
        conn_activities.close()
        self.ui.refresh_button.click()

    def delete_co_diver(self):
        conn_dives = sqlite3.connect("dives_record.db")
        conn_customer = sqlite3.connect("customer_info.db")
        conn_activities = sqlite3.connect("activities_info.db")
        c_a = conn_activities.cursor()
        c_d = conn_dives.cursor()
        c_c = conn_customer.cursor()
        oid = self.ui.co_delete_diver_entry.text()
        c_c.execute("SELECT total_cost, balance FROM customer WHERE oid =?", (oid))
        c = c_c.fetchone()
        total_cost = c[0]
        balance = c[1]
        running_bal = 0
        c_d.execute("SELECT * FROM dives WHERE diver_id =? AND date = ? AND time = ?", (oid, date, co))
        d = c_d.fetchall()
        c = d[0]

        c_a.execute("SELECT * FROM extras WHERE oid = 1")
        a = c_a.fetchall()
        b = a[0]
        count = len(b)
        sorb = ""
        for i in range(count):
            if c[(i + 6)] == 1:
                running_bal = running_bal + int(b[i])

        if int(c[32]) > 0:
            running_bal = running_bal - int(b[26])
            sorb = int(c[32]) * int(b[26])
            running_bal = running_bal + sorb

        activity = c[2]
        c_a.execute("SELECT price FROM activity WHERE activity =?", ([activity]))
        e = c_a.fetchall()
        f = e[0]

        c_a.execute("SELECT price, course FROM activity WHERE activity =?", ([activity]))
        a = c_a.fetchall()
        price = a[0]
        price2 = price[0]
        course = a[0]
        course2 = course[1]
        c_d.execute("SELECT activity FROM dives WHERE diver_id =?", ([oid]))
        x3 = c_d.fetchall()
        list3 = list(map(itemgetter(0), x3))

        count = 0
        for course in list3:
            if course2 == 1:
                if course == activity:
                    count += 1

        if count > 1:
            running_bal = running_bal - int(price2)

        running_bal = running_bal + int(f[0])

        total_cost = total_cost - running_bal
        balance = balance - running_bal

        c_c.execute("UPDATE customer SET total_cost = ?, balance = ? WHERE oid = ?", (total_cost, balance, oid))
        c_d.execute("DELETE FROM dives WHERE diver_id = ? AND date = ? AND time = ?", (oid, date, co))
        self.ui.co_delete_diver_entry.clear()
        self.ui.refresh_button.click()
        conn_customer.commit()
        conn_dives.commit()
        conn_activities.commit()
        conn_customer.close()
        conn_dives.close()
        conn_activities.close()
        self.ui.refresh_button.click()

    def add_customer(self):
        conn_customer = sqlite3.connect("customer_info.db")
        c_c = conn_customer.cursor()
        c_c.execute(
            "INSERT INTO customer VALUES (:f_name, :l_name, :dob, :cert_level, :cert_check, :number_of_dives, :last_dive, :liab_form, :total_cost, :balance)",
            {"f_name": self.ui.f_name_entry.text(),
             "l_name": self.ui.l_name_entry.text(),
             "dob": self.ui.dob_entry.text(),
             "cert_level": self.ui.cert_combo.currentText(),
             "cert_check": self.ui.cert_check.isChecked(),
             "number_of_dives": self.ui.no_dives_entry.text(),
             "last_dive": self.ui.last_dive_entry.text(),
             "liab_form": self.ui.liab_check.isChecked(),
             "total_cost" : 0,
             "balance" : 0
             })
        self.ui.f_name_entry.clear()
        self.ui.l_name_entry.clear()
        self.ui.dob_entry.clear()
        self.ui.cert_combo.setCurrentText(" ")
        self.ui.cert_check.setChecked(False)
        self.ui.no_dives_entry.clear()
        self.ui.last_dive_entry.clear()
        self.ui.liab_check.setChecked(False)
        self.ui.new_customer_added_label.setText("New customer added")
        conn_customer.commit()
        conn_customer.close()

    def delete_customer(self):
        self.oid = self.ui.id_entry.text()

        conn_customer = sqlite3.connect("customer_info.db")
        c_c = conn_customer

        c_c.execute(("DELETE FROM customer WHERE oid = " + self.oid))

        conn_customer.commit()
        conn_customer.close()
        self.list_all()

    def list_all(self):
        conn_customer = sqlite3.connect("customer_info.db")
        c_c = conn_customer.cursor()

        c_c.execute("SELECT *, oid FROM customer")
        x = c_c.fetchall()

        print_oid = ""
        print_f_name = ""
        print_l_name = ""
        print_dob = ""

        for record in x:
            print_oid += str(record[10]) + "\n"
            print_f_name += str(record[0]) + "\n"
            print_l_name += str(record[1]) + "\n"
            print_dob += str(record[2]) + "\n"

        conn_customer.commit()
        conn_customer.close()

        self.ui.oid_search_results_label.setText(print_oid)
        self.ui.f_name_search_results_label.setText(print_f_name)
        self.ui.l_name_search_results_label.setText(print_l_name)
        self.ui.l_name_search_results_label_2.setText(print_dob)
        self.ui.l_name_search_results_label_2.adjustSize()
        self.ui.oid_search_results_label.adjustSize()
        self.ui.f_name_search_results_label.adjustSize()
        self.ui.l_name_search_results_label.adjustSize()

    def search_customer(self):
        conn_customer = sqlite3.connect("customer_info.db")
        c_c = conn_customer.cursor()

        record_id = self.ui.l_name_search_entry.text()

        c_c.execute("SELECT *, oid FROM customer WHERE last_name LIKE? ", [record_id])
        x = c_c.fetchall()

        print_oid = ""
        print_f_name = ""
        print_l_name = ""
        print_dob = ""

        for record in x:
            print_oid += str(record[10]) + "\n"
            print_f_name += str(record[0]) + "\n"
            print_l_name += str(record[1]) + "\n"
            print_dob += str(record[2]) + "\n"

        conn_customer.commit()
        conn_customer.close()


        self.ui.oid_search_results_label.setText(print_oid)
        self.ui.f_name_search_results_label.setText(print_f_name)
        self.ui.l_name_search_results_label.setText(print_l_name)
        self.ui.l_name_search_results_label_2.setText(print_dob)
        self.ui.l_name_search_results_label_2.adjustSize()
        self.ui.oid_search_results_label.adjustSize()
        self.ui.f_name_search_results_label.adjustSize()
        self.ui.l_name_search_results_label.adjustSize()

    def populate_customer_record(self):
        id1 = self.ui.id_entry.text()
        conn_customer = sqlite3.connect("customer_info.db")
        c_c = conn_customer.cursor()

        c_c.execute("SELECT * FROM customer WHERE oid = " + id1)
        to_edit = c_c.fetchall()

        for record in to_edit:
            self.ui.f_name_entry_2.setText(record[0])
            self.ui.l_name_entry_2.setText(record[1])
            self.ui.dob_entry_2.setText(record[2])
            self.ui.cert_combo_2.setCurrentText(record[3])
            self.ui.cert_check_2.setChecked(record[4])
            self.ui.no_dives_entry_2.setText(record[5])
            self.ui.last_dive_entry_2.setText(record[6])
            self.ui.liab_check_2.setChecked(record[7])

        conn_customer.commit()
        conn_customer.close()

    def update_customer_record(self):

        id1 = self.ui.id_entry.text()
        conn_customer = sqlite3.connect("customer_info.db")
        c_c = conn_customer.cursor()
        c_c.execute("""UPDATE customer SET
                                    first_name = :first,
                                    last_name = :last,
                                    dob = :dob,
                                    cert = :cert,
                                    cert_check = :check,
                                    no_dives = :dives,
                                    last_dive = :lastd,
                                    liability_form =:liab
                                    WHERE oid = :oid""",
                    {"first": self.ui.f_name_entry_2.text(),
                     "last": self.ui.l_name_entry_2.text(),
                     "dob": self.ui.dob_entry_2.text(),
                     "cert": self.ui.cert_combo_2.currentText(),
                     "check": self.ui.cert_check_2.isChecked(),
                     "dives": self.ui.no_dives_entry_2.text(),
                     "lastd": self.ui.last_dive_entry_2.text(),
                     "liab": self.ui.liab_check_2.isChecked(),
                     "oid": id1
                     })
        self.ui.record_updated_label.setText("Record Updated")
        conn_customer.commit()
        conn_customer.close()

    def delete_staff(self):
        oid = self.ui.oid_entry.text()

        conn_staff = sqlite3.connect("staff_info.db")
        c_s = conn_staff.cursor()

        c_s.execute("DELETE FROM staff WHERE oid =" + oid)



        conn_staff.commit()
        conn_staff.close()
        self.list_staff()

    def list_staff(self):
        conn_staff = sqlite3.connect("staff_info.db")
        c_s = conn_staff.cursor()
        c_s.execute("SELECT *, oid FROM staff")
        x = c_s.fetchall()
        print_oid = ""
        print_f_name = ""
        print_l_name = ""
        print_pro_no = ""
        print_insurance = ""
        print_ins_exp = ""
        print_highest = ""

        for i in x:
            print_oid += str(i[19]) + "\n"
            print_f_name += str(i[0]) + "\n"
            print_l_name += str(i[1]) + "\n"
            print_pro_no += str(i[2]) + "\n"
            print_insurance += str(i[3]) + "\n"
            print_ins_exp += str(i[4]) + "\n"
            print_highest += str(i[5]) + "\n"

        self.ui.id_results_label.setText(print_oid)
        self.ui.f_name_results_label.setText(print_f_name)
        self.ui.l_name_results_label.setText(print_l_name)
        self.ui.pro_number_results_label.setText(print_pro_no)
        self.ui.insurance_no_results_label.setText(print_insurance)
        self.ui.insurance_exp_results_label.setText(print_ins_exp)
        self.ui.highest_results_label.setText(print_highest)
        self.ui.id_results_label.adjustSize()
        self.ui.f_name_results_label.adjustSize()
        self.ui.l_name_results_label.adjustSize()
        self.ui.pro_number_results_label.adjustSize()
        self.ui.insurance_no_results_label.adjustSize()
        self.ui.insurance_exp_results_label.adjustSize()
        self.ui.highest_results_label.adjustSize()

        conn_staff.commit()
        conn_staff.close()

    def add_staff(self):
        conn_staff = sqlite3.connect("staff_info.db")
        c_s = conn_staff.cursor()
        c_s.execute("""INSERT INTO staff VALUES (
                                     :f_name, 
                                     :l_name, 
                                     :pro_number, 
                                     :insurance_no, 
                                     :insurance_exp,
                                     :highest,
                                     :dm,
                                     :owi,
                                     :deep,
                                     :wreck,
                                     :adv_wreck,
                                     :pb,
                                     :eanx,
                                     :boat,
                                     :nav,
                                     :night,
                                     :sod,
                                     :xr,
                                     :sidemount
                                      )""",
                    {"f_name": self.ui.lineEdit.text(),
                     "l_name": self.ui.lineEdit_2.text(),
                     "pro_number": self.ui.lineEdit_3.text(),
                     "insurance_no": self.ui.lineEdit_4.text(),
                     "insurance_exp": self.ui.lineEdit_5.text(),
                     "highest": self.ui.lineEdit_6.text(),
                     "dm": self.ui.dm_check.isChecked(),
                     "owi": self.ui.owi_check.isChecked(),
                     "deep": self.ui.deep_check.isChecked(),
                     "wreck": self.ui.wreck_check.isChecked(),
                     "adv_wreck": self.ui.adv_wreck_check.isChecked(),
                     "pb": self.ui.pb_check.isChecked(),
                     "eanx": self.ui.eanx_check.isChecked(),
                     "boat": self.ui.boat_check.isChecked(),
                     "nav": self.ui.nav_check.isChecked(),
                     "night": self.ui.night_check.isChecked(),
                     "sod": self.ui.sod_check.isChecked(),
                     "xr": self.ui.xr_check.isChecked(),
                     "sidemount": self.ui.sidemount_check.isChecked(),
                     })

        self.ui.lineEdit.clear()
        self.ui.lineEdit_2.clear()
        self.ui.lineEdit_3.clear()
        self.ui.lineEdit_4.clear()
        self.ui.lineEdit_5.clear()
        self.ui.lineEdit_6.clear()
        self.ui.dm_check.setChecked(False)
        self.ui.owi_check.setChecked(False)
        self.ui.deep_check.setChecked(False)
        self.ui.wreck_check.setChecked(False)
        self.ui.adv_wreck_check.setChecked(False)
        self.ui.pb_check.setChecked(False)
        self.ui.eanx_check.setChecked(False)
        self.ui.boat_check.setChecked(False)
        self.ui.nav_check.setChecked(False)
        self.ui.night_check.setChecked(False)
        self.ui.sod_check.setChecked(False)
        self.ui.xr_check.setChecked(False)
        self.ui.sidemount_check.setChecked(False)
        conn_staff.commit()
        conn_staff.close()
        self.list_staff()

    def populate_boxes(self):
        conn_staff = sqlite3.connect("staff_info.db")
        c_s = conn_staff.cursor()
        record_id = self.ui.oid_entry.text()
        c_s.execute("SELECT * FROM staff WHERE oid = " + record_id)
        to_edit = c_s.fetchall()

        for i in to_edit:
            self.ui.lineEdit_4.setText(i[3])
            self.ui.lineEdit_5.setText(i[4])
            self.ui.lineEdit.setText(i[0])
            self.ui.lineEdit_2.setText(i[1])
            self.ui.lineEdit_6.setText(i[5])
            self.ui.lineEdit_3.setText(i[2])
            self.ui.dm_check.setChecked(i[6])
            self.ui.deep_check.setChecked(i[8])
            self.ui.owi_check.setChecked(i[7])
            self.ui.adv_wreck_check.setChecked(i[10])
            self.ui.wreck_check.setChecked(i[9])
            self.ui.eanx_check.setChecked(i[12])
            self.ui.pb_check.setChecked(i[11])
            self.ui.nav_check.setChecked(i[14])
            self.ui.boat_check.setChecked(i[13])
            self.ui.night_check.setChecked(i[15])
            self.ui.xr_check.setChecked(i[17])
            self.ui.sod_check.setChecked(i[16])
            self.ui.sidemount_check.setChecked(i[18])

        conn_staff.commit()
        conn_staff.close()

    def update_staff(self):
        oid = self.ui.oid_entry.text()
        conn_staff = sqlite3.connect("staff_info.db")
        c_s = conn_staff.cursor()
        c_s.execute("""UPDATE staff SET 
                                                first_name = :f_name, 
                                                last_name = :l_name, 
                                                pro_number = :pro_number, 
                                                insurance_number = :insurance_no, 
                                                insurance_exp = :insurance_exp,
                                                highest = :highest,
                                                dm = :dm,
                                                owi = :owi,
                                                deep = :deep,
                                                wreck = :wreck,
                                                advanced_wreck = :adv_wreck,
                                                pb = :pb,
                                                eanx = :eanx,
                                                boat = :boat,
                                                nav = :nav,
                                                night = :night,
                                                sod = :sod,
                                                xr = :xr,
                                                sidemount = :sidemount

                                                WHERE oid = :oid""",
                    {"f_name": self.ui.lineEdit.text(),
                     "l_name": self.ui.lineEdit_2.text(),
                     "pro_number": self.ui.lineEdit_3.text(),
                     "insurance_no": self.ui.lineEdit_4.text(),
                     "insurance_exp": self.ui.lineEdit_5.text(),
                     "highest": self.ui.lineEdit_6.text(),
                     "dm": self.ui.dm_check.isChecked(),
                     "owi": self.ui.owi_check.isChecked(),
                     "deep": self.ui.deep_check.isChecked(),
                     "wreck": self.ui.wreck_check.isChecked(),
                     "adv_wreck": self.ui.adv_wreck_check.isChecked(),
                     "pb": self.ui.pb_check.isChecked(),
                     "eanx": self.ui.eanx_check.isChecked(),
                     "boat": self.ui.boat_check.isChecked(),
                     "nav": self.ui.nav_check.isChecked(),
                     "night": self.ui.night_check.isChecked(),
                     "sod": self.ui.sod_check.isChecked(),
                     "xr": self.ui.xr_check.isChecked(),
                     "sidemount": self.ui.sidemount_check.isChecked(),
                     "oid": oid
                     })

        conn_staff.commit()
        conn_staff.close()
        self.clear_staff()
        self.list_staff()

    def clear_staff(self):
        self.ui.lineEdit.clear()
        self.ui.lineEdit_2.clear()
        self.ui.lineEdit_3.clear()
        self.ui.lineEdit_4.clear()
        self.ui.lineEdit_5.clear()
        self.ui.lineEdit_6.clear()
        self.ui.dm_check.setChecked(False)
        self.ui.owi_check.setChecked(False)
        self.ui.deep_check.setChecked(False)
        self.ui.wreck_check.setChecked(False)
        self.ui.adv_wreck_check.setChecked(False)
        self.ui.pb_check.setChecked(False)
        self.ui.eanx_check.setChecked(False)
        self.ui.boat_check.setChecked(False)
        self.ui.nav_check.setChecked(False)
        self.ui.night_check.setChecked(False)
        self.ui.sod_check.setChecked(False)
        self.ui.xr_check.setChecked(False)
        self.ui.sidemount_check.setChecked(False)
        self.ui.oid_entry.clear()

    def add_activity(self):
        conn_activities = sqlite3.connect("activities_info.db")
        c_a = conn_activities.cursor()

        c_a.execute("""INSERT INTO activity VALUES(
                            :activities,
                            :inst,
                            :price,
                            :course
                                )""",
                    {"activities" : self.ui.activity_name_entry.text(),
                     "inst"       : self.ui.inst_cert_combo.currentText(),
                     "price"      : self.ui.price_entry.text(),
                     "course"     : self.ui.is_course_check.isChecked()
                    })

        self.ui.activity_name_entry.setText("")
        self.ui.inst_cert_combo.setCurrentIndex(0)
        self.ui.price_entry.setText("")
        self.ui.is_course_check.setChecked(False)
        conn_activities.commit()
        conn_activities.close()

    def list_activities(self):
        conn_activities = sqlite3.connect("activities_info.db")
        c_a = conn_activities.cursor()

        c_a.execute("SELECT *, oid FROM activity")
        x = c_a.fetchall()

        act = ""
        inst = ""
        price = ""
        id = ""
        for i in x:
            act += str(i[0]) + "\n"
            inst += str(i[1]) + "\n"
            price += "€" + str(i[2]) + "\n"
            id += str(i[4]) + "\n"

        self.ui.activity_list_results.setText(act)
        self.ui.inst_cert_list_results.setText(inst)
        self.ui.price_list_results.setText(price)
        self.ui.id_list_results_.setText(id)
        self.ui.activity_list_results.adjustSize()
        self.ui.inst_cert_list_results.adjustSize()
        self.ui.price_list_results.adjustSize()
        self.ui.id_list_results_.adjustSize()

        conn_activities.commit()
        conn_activities.close()

    def extras(self):
        global placeholder
        conn_activities = sqlite3.connect("activities_info.db")
        c_a = conn_activities.cursor()

        c_a.execute("""UPDATE extras SET
                full_equ_dive =  :full_equ_dive,
                full_equ_day = :full_equ_day,
                full_equ_upgrade = :full_equ_upgrade,
                computer_day = :computer_day,
                torch_day = :torch_day,
                bcd_dive = :bcd_dive,
                bcd_day = :bcd_day,
                bcd_upgrade = :bcd_upgrade,
                reg_dive = :reg_dive,
                reg_day = :reg_day,
                reg_upgrade = :reg_upgrade,
                soft_dive = :soft_dive,
                soft_day = :soft_day,
                soft_upgrade = :soft_upgrade,
                eanx_upgrade = :eanx_upgrade,
                t_15l_upgrade = :t_15l_upgrade,
                t_18l_upgrade = :t_18l_upgrade,
                t_3l_air = :t_3l_air,
                t_3l_100 = :t_3l_100,
                t_6l_50 = :t_6l_50,
                t_6l_100 = :t_6l_100,
                t_12l_50 = :t_12l_50,
                t_12L_100 = :t_12L_100,
                twin_air = :twin_air,
                twin_eanx = :twin_eanx,
                rebreather = :rebreather,
                sorb = :sorb,
                no_tank = :no_tank,
                tech_reg = :tech_reg,
                back_plate = :back_plate,
                wing = :wing,
                o2_reg = :o2_reg,
                tech_computer = :tech_computer,
                tech_torch = :tech_torch,
                wreck_reel = :wreck_reel,
                smb = :smb,
                reel = :reel,
                slate = :slate 
                WHERE oid = 1""",
                    { "full_equ_dive" : self.ui.full_equip_dive_entry.text(),
                "full_equ_day" : self.ui.full_equip_day_entry.text(),
                "full_equ_upgrade" :self.ui.full_equip_upgrade_entry.text(),
                "computer_day" :self.ui.computer_entry.text(),
                "torch_day" :self.ui.torch_entry.text(),
                "bcd_dive" :self.ui.bcd_dive_entry.text(),
                "bcd_day" :self.ui.bcd_day_entry.text(),
                "bcd_upgrade" :self.ui.bcd_upgrade_entry.text(),
                "reg_dive" :self.ui.reg_dive_entry.text(),
                "reg_day" :self.ui.reg_day_entry.text(),
                "reg_upgrade" :self.ui.reg_upgrade_entry.text(),
                "soft_dive" :self.ui.soft_dive_entry.text(),
                "soft_day" :self.ui.soft_day_entry.text(),
                "soft_upgrade" :self.ui.soft_upgrade_entry.text(),
                "eanx_upgrade" :self.ui.eanx_upgrade_entry.text(),
                "t_15l_upgrade" :self.ui.t_15l_entry.text(),
                "t_18l_upgrade" :self.ui.t_18__entry.text(),
                "t_3l_air" :self.ui.t_3l_air_entry.text(),
                "t_3l_100" :self.ui.t_3l_100_entry.text(),
                "t_6l_50" :self.ui.t_6_50_entry.text(),
                "t_6l_100" :self.ui.t_6_100_entry.text(),
                "t_12l_50" :self.ui.t_12_50_entry.text(),
                "t_12L_100" :self.ui.t_12l_100_entry.text(),
                "twin_air" :self.ui.twin_air_entry.text(),
                "twin_eanx" :self.ui.twin_eanx_entry.text(),
                "rebreather" :self.ui.rebreather_entry.text(),
                "sorb" :self.ui.sorb_entry.text(),
                "no_tank" :placeholder,
                "tech_reg" :self.ui.tech_reg_entry.text(),
                "back_plate" :self.ui.back_plate_entry.text(),
                "wing" :self.ui.wing_entry.text(),
                "o2_reg" :self.ui.o2_reg_entry.text(),
                "tech_computer" :self.ui.tech_computer_entry.text(),
                "tech_torch" :self.ui.tech_torch_entry.text(),
                "wreck_reel" :self.ui.wreck_reel_entry.text(),
                "smb" :self.ui.smb_entry.text(),
                "reel" :self.ui.reel_entry.text(),
                "slate" :self.ui.slate_entry.text()
                            })

        conn_activities.commit()
        conn_activities.close()

    def open_extras(self):
        oid = "1"
        conn_activities = sqlite3.connect("activities_info.db")
        c_a = conn_activities.cursor()

        c_a.execute("SELECT * FROM extras WHERE oid = " + oid)
        x= c_a.fetchall()

        for i in x:
            self.ui.full_equip_dive_entry.setText(i[0])
            self.ui.full_equip_day_entry.setText(i[1])
            self.ui.full_equip_upgrade_entry.setText(i[2])
            self.ui.computer_entry.setText(i[3])
            self.ui.torch_entry.setText(i[4])
            self.ui.bcd_dive_entry.setText(i[5])
            self.ui.bcd_day_entry.setText(i[6])
            self.ui.bcd_upgrade_entry.setText(i[7])
            self.ui.reg_dive_entry.setText(i[8])
            self.ui.reg_day_entry.setText(i[9])
            self.ui.reg_upgrade_entry.setText(i[10])
            self.ui.soft_dive_entry.setText(i[11])
            self.ui.soft_day_entry.setText(i[12])
            self.ui.soft_upgrade_entry.setText(i[13])
            self.ui.eanx_upgrade_entry.setText(i[14])
            self.ui.t_15l_entry.setText(i[15])
            self.ui.t_18__entry.setText(i[16])
            self.ui.t_3l_air_entry.setText(i[17])
            self.ui.t_3l_100_entry.setText(i[18])
            self.ui.t_6_50_entry.setText(i[19])
            self.ui.t_6_100_entry.setText(i[20])
            self.ui.t_12_50_entry.setText(i[21])
            self.ui.t_12l_100_entry.setText(i[22])
            self.ui.twin_air_entry.setText(i[23])
            self.ui.twin_eanx_entry.setText(i[24])
            self.ui.rebreather_entry.setText(i[25])
            self.ui.sorb_entry.setText(i[26])
            self.ui.tech_reg_entry.setText(i[28])
            self.ui.back_plate_entry.setText(i[29])
            self.ui.wing_entry.setText(i[30])
            self.ui.o2_reg_entry.setText(i[31])
            self.ui.tech_computer_entry.setText(i[32])
            self.ui.tech_torch_entry.setText(i[33])
            self.ui.wreck_reel_entry.setText(i[34])
            self.ui.smb_entry.setText(i[35])
            self.ui.reel_entry.setText(i[36])
            self.ui.slate_entry.setText(i[37])

    def delete_activity(self):
        oid = self.ui.oid_entry_2.text()

        conn_activities = sqlite3.connect("activities_info.db")
        c_a = conn_activities.cursor()

        c_a.execute("DELETE FROM activity WHERE oid =?",([oid]))



        conn_activities.commit()
        conn_activities.close()
        self.list_activities()

    def payment(self):
        oid = int(self.ui.id_search_entry.text())
        amount = int(self.ui.lineEdit_7.text())
        conn_payment = sqlite3.connect("payment.db")
        c_p = conn_payment.cursor()
        c_p.execute("INSERT INTO payment VALUES (:diver_id, :date, :amount) ",
                    {"diver_id": oid, "date": date, "amount": amount})

        conn_payment.commit()
        conn_payment.close()
        self.refresh_tab()
        self.refresh_all()

    def list_all_tabs(self):
        conn_customer = sqlite3.connect("customer_info.db")
        c_c = conn_customer.cursor()

        c_c.execute("SELECT *, oid FROM customer")
        x = c_c.fetchall()

        print_oid = ""
        print_f_name = ""
        print_l_name = ""
        print_dob = ""

        for record in x:
            print_oid += str(record[10]) + "\n"
            print_f_name += str(record[0]) + "\n"
            print_l_name += str(record[1]) + "\n"
            print_dob += str(record[2]) + "\n"

        conn_customer.commit()
        conn_customer.close()

        self.ui.oid_search_results_label_2.setText(print_oid)
        self.ui.f_name_search_results_label_2.setText(print_f_name)
        self.ui.l_name_search_results_label_2.setText(print_l_name)
        self.ui.l_name_search_results_label_3.setText(print_dob)
        self.ui.l_name_search_results_label_4.adjustSize()
        self.ui.oid_search_results_label.adjustSize()
        self.ui.f_name_search_results_label.adjustSize()
        self.ui.l_name_search_results_label.adjustSize()

    def refresh_tab(self):

        conn_customer = sqlite3.connect("customer_info.db")
        c_c = conn_customer.cursor()
        conn_tab = sqlite3.connect("tabs_info.db")
        c_t = conn_tab.cursor()
        conn_dives = sqlite3.connect("dives_record.db")
        c_d = conn_dives.cursor()
        conn_activities = sqlite3.connect("activities_info.db")
        conn_payment = sqlite3.connect("payment.db")
        c_p = conn_payment.cursor()
        c_a = conn_activities.cursor()
        oid1 = self.ui.id_search_entry.text()
        c_c.execute("SELECT oid, first_name, last_name, balance, total_cost FROM customer WHERE oid = ?", (oid1))
        x = c_c.fetchall()
        for i in x:
            self.ui.id_number_label.setText(str(i[0]))
            self.ui.f_l_name_label.setText(i[1] + " " + i[2])
            self.ui.id_number_label.adjustSize()
            self.ui.f_l_name_label.adjustSize()

        c_d.execute("SELECT * FROM dives WHERE diver_id = ?",(oid1))
        d = c_d.fetchall()
        rowcount = 0
        tablerow = 0
        counter = 0
        for i in d:
            rowcount += 1
            self.ui.tab_table.setRowCount(rowcount)
            act = str(i[2])
            price = c_a.execute("SELECT price FROM activity WHERE activity = ?",([act]))
            pr = price.fetchall()
            pr2 = pr[0]
            self.ui.tab_table.setItem(tablerow, 0, QtWidgets.QTableWidgetItem(i[0]))
            self.ui.tab_table.setItem(tablerow, 1, QtWidgets.QTableWidgetItem(i[2]))
            self.ui.tab_table.setItem(tablerow, 2, QtWidgets.QTableWidgetItem(i[4]))
            self.ui.tab_table.setItem(tablerow, 3, QtWidgets.QTableWidgetItem(i[3]))
            self.ui.tab_table.setItem(tablerow, 4, QtWidgets.QTableWidgetItem("€" + str(pr2[0])))

            item = QtWidgets.QTableWidgetItem()
            item.setCheckState(QtCore.Qt.Unchecked)
            self.ui.tab_table.setItem(tablerow, 5, item)
            equ = list(map(itemgetter(6),d))

            equ1 = equ[counter]

            if str(equ1) == "1":
                self.ui.tab_table.item(tablerow,5).setCheckState(QtCore.Qt.Checked)

            item2 = QtWidgets.QTableWidgetItem()
            item2.setCheckState(QtCore.Qt.Unchecked)
            self.ui.tab_table.setItem(tablerow, 6, item2)
            equ = list(map(itemgetter(7), d))
            equ1 = equ[counter]
            if str(equ1) == "1":
                self.ui.tab_table.item(tablerow, 6).setCheckState(QtCore.Qt.Checked)

            item3 = QtWidgets.QTableWidgetItem()
            item3.setCheckState(QtCore.Qt.Unchecked)
            self.ui.tab_table.setItem(tablerow, 7, item3)
            equ = list(map(itemgetter(8), d))
            equ1 = equ[counter]
            if str(equ1) == "1":
                self.ui.tab_table.item(tablerow, 7).setCheckState(QtCore.Qt.Checked)

            item4 = QtWidgets.QTableWidgetItem()
            item4.setCheckState(QtCore.Qt.Unchecked)
            self.ui.tab_table.setItem(tablerow, 8, item4)
            equ = list(map(itemgetter(9), d))
            equ1 = equ[counter]
            if str(equ1) == "1":
                self.ui.tab_table.item(tablerow, 8).setCheckState(QtCore.Qt.Checked)

            item5 = QtWidgets.QTableWidgetItem()
            item5.setCheckState(QtCore.Qt.Unchecked)
            self.ui.tab_table.setItem(tablerow, 9, item5)
            equ = list(map(itemgetter(10), d))
            equ1 = equ[counter]
            if str(equ1) == "1":
                self.ui.tab_table.item(tablerow, 9).setCheckState(QtCore.Qt.Checked)

            item6 = QtWidgets.QTableWidgetItem()
            item6.setCheckState(QtCore.Qt.Unchecked)
            self.ui.tab_table.setItem(tablerow, 10, item6)
            equ = list(map(itemgetter(11), d))
            equ1 = equ[counter]
            if str(equ1) == "1":
                self.ui.tab_table.item(tablerow, 10).setCheckState(QtCore.Qt.Checked)

            item7 = QtWidgets.QTableWidgetItem()
            item7.setCheckState(QtCore.Qt.Unchecked)
            self.ui.tab_table.setItem(tablerow, 11, item7)
            equ = list(map(itemgetter(12), d))
            equ1 = equ[counter]
            if str(equ1) == "1":
                self.ui.tab_table.item(tablerow, 11).setCheckState(QtCore.Qt.Checked)

            item8 = QtWidgets.QTableWidgetItem()
            item8.setCheckState(QtCore.Qt.Unchecked)
            self.ui.tab_table.setItem(tablerow, 12, item8)
            equ = list(map(itemgetter(13), d))
            equ1 = equ[counter]
            if str(equ1) == "1":
                self.ui.tab_table.item(tablerow, 12).setCheckState(QtCore.Qt.Checked)

            item9 = QtWidgets.QTableWidgetItem()
            item9.setCheckState(QtCore.Qt.Unchecked)
            self.ui.tab_table.setItem(tablerow, 13, item9)
            equ = list(map(itemgetter(14), d))
            equ1 = equ[counter]
            if str(equ1) == "1":
                self.ui.tab_table.item(tablerow, 13).setCheckState(QtCore.Qt.Checked)

            item10 = QtWidgets.QTableWidgetItem()
            item10.setCheckState(QtCore.Qt.Unchecked)
            self.ui.tab_table.setItem(tablerow, 14, item10)
            equ = list(map(itemgetter(15), d))
            equ1 = equ[counter]
            if str(equ1) == "1":
                self.ui.tab_table.item(tablerow, 14).setCheckState(QtCore.Qt.Checked)

            item11 = QtWidgets.QTableWidgetItem()
            item11.setCheckState(QtCore.Qt.Unchecked)
            self.ui.tab_table.setItem(tablerow, 15, item11)
            equ = list(map(itemgetter(16), d))
            equ1 = equ[counter]
            if str(equ1) == "1":
                self.ui.tab_table.item(tablerow, 15).setCheckState(QtCore.Qt.Checked)

            item12 = QtWidgets.QTableWidgetItem()
            item12.setCheckState(QtCore.Qt.Unchecked)
            self.ui.tab_table.setItem(tablerow, 16, item12)
            equ = list(map(itemgetter(17), d))
            equ1 = equ[counter]
            if str(equ1) == "1":
                self.ui.tab_table.item(tablerow, 16).setCheckState(QtCore.Qt.Checked)

            item13 = QtWidgets.QTableWidgetItem()
            item13.setCheckState(QtCore.Qt.Unchecked)
            self.ui.tab_table.setItem(tablerow, 17, item13)
            equ = list(map(itemgetter(18), d))
            equ1 = equ[counter]
            if str(equ1) == "1":
                self.ui.tab_table.item(tablerow, 17).setCheckState(QtCore.Qt.Checked)

            item14 = QtWidgets.QTableWidgetItem()
            item14.setCheckState(QtCore.Qt.Unchecked)
            self.ui.tab_table.setItem(tablerow, 18, item14)
            equ = list(map(itemgetter(19), d))
            equ1 = equ[counter]
            if str(equ1) == "1":
                self.ui.tab_table.item(tablerow, 18).setCheckState(QtCore.Qt.Checked)

            item15 = QtWidgets.QTableWidgetItem()
            item15.setCheckState(QtCore.Qt.Unchecked)
            self.ui.tab_table.setItem(tablerow, 19, item15)
            equ = list(map(itemgetter(20), d))
            equ1 = equ[counter]
            if str(equ1) == "1":
                self.ui.tab_table.item(tablerow, 19).setCheckState(QtCore.Qt.Checked)

            item16 = QtWidgets.QTableWidgetItem()
            item16.setCheckState(QtCore.Qt.Unchecked)
            self.ui.tab_table.setItem(tablerow, 20, item16)
            equ = list(map(itemgetter(21), d))
            equ1 = equ[counter]
            if str(equ1) == "1":
                self.ui.tab_table.item(tablerow, 20).setCheckState(QtCore.Qt.Checked)

            item17 = QtWidgets.QTableWidgetItem()
            item17.setCheckState(QtCore.Qt.Unchecked)
            self.ui.tab_table.setItem(tablerow, 21, item17)
            equ = list(map(itemgetter(22), d))
            equ1 = equ[counter]
            if str(equ1) == "1":
                self.ui.tab_table.item(tablerow, 21).setCheckState(QtCore.Qt.Checked)

            item18 = QtWidgets.QTableWidgetItem()
            item18.setCheckState(QtCore.Qt.Unchecked)
            self.ui.tab_table.setItem(tablerow, 22, item18)
            equ = list(map(itemgetter(23), d))
            equ1 = equ[counter]
            if str(equ1) == "1":
                self.ui.tab_table.item(tablerow, 22).setCheckState(QtCore.Qt.Checked)

            item19 = QtWidgets.QTableWidgetItem()
            item19.setCheckState(QtCore.Qt.Unchecked)
            self.ui.tab_table.setItem(tablerow, 23, item19)
            equ = list(map(itemgetter(24), d))
            equ1 = equ[counter]
            if str(equ1) == "1":
                self.ui.tab_table.item(tablerow, 23).setCheckState(QtCore.Qt.Checked)

            item20 = QtWidgets.QTableWidgetItem()
            item20.setCheckState(QtCore.Qt.Unchecked)
            self.ui.tab_table.setItem(tablerow, 24, item20)
            equ = list(map(itemgetter(25), d))
            equ1 = equ[counter]
            if str(equ1) == "1":
                self.ui.tab_table.item(tablerow, 24).setCheckState(QtCore.Qt.Checked)

            item21 = QtWidgets.QTableWidgetItem()
            item21.setCheckState(QtCore.Qt.Unchecked)
            self.ui.tab_table.setItem(tablerow, 25, item21)
            equ = list(map(itemgetter(26), d))
            equ1 = equ[counter]
            if str(equ1) == "1":
                self.ui.tab_table.item(tablerow, 25).setCheckState(QtCore.Qt.Checked)

            item22 = QtWidgets.QTableWidgetItem()
            item22.setCheckState(QtCore.Qt.Unchecked)
            self.ui.tab_table.setItem(tablerow, 26, item22)
            equ = list(map(itemgetter(27), d))
            equ1 = equ[counter]
            if str(equ1) == "1":
                self.ui.tab_table.item(tablerow, 26).setCheckState(QtCore.Qt.Checked)

            item23 = QtWidgets.QTableWidgetItem()
            item23.setCheckState(QtCore.Qt.Unchecked)
            self.ui.tab_table.setItem(tablerow, 27, item23)
            equ = list(map(itemgetter(28), d))
            equ1 = equ[counter]
            if str(equ1) == "1":
                self.ui.tab_table.item(tablerow, 27).setCheckState(QtCore.Qt.Checked)

            item24 = QtWidgets.QTableWidgetItem()
            item24.setCheckState(QtCore.Qt.Unchecked)
            self.ui.tab_table.setItem(tablerow, 28, item24)
            equ = list(map(itemgetter(29), d))
            equ1 = equ[counter]
            if str(equ1) == "1":
                self.ui.tab_table.item(tablerow, 28).setCheckState(QtCore.Qt.Checked)

            item25 = QtWidgets.QTableWidgetItem()
            item25.setCheckState(QtCore.Qt.Unchecked)
            self.ui.tab_table.setItem(tablerow, 29, item25)
            equ = list(map(itemgetter(30), d))
            equ1 = equ[counter]
            if str(equ1) == "1":
                self.ui.tab_table.item(tablerow, 29).setCheckState(QtCore.Qt.Checked)

            item26 = QtWidgets.QTableWidgetItem()
            item26.setCheckState(QtCore.Qt.Unchecked)
            self.ui.tab_table.setItem(tablerow, 30, item26)
            equ = list(map(itemgetter(34), d))
            equ1 = equ[counter]
            if str(equ1) == "1":
                self.ui.tab_table.item(tablerow, 30).setCheckState(QtCore.Qt.Checked)

            item27 = QtWidgets.QTableWidgetItem()
            item27.setCheckState(QtCore.Qt.Unchecked)
            self.ui.tab_table.setItem(tablerow, 31, item27)
            equ = list(map(itemgetter(35), d))
            equ1 = equ[counter]
            if str(equ1) == "1":
                self.ui.tab_table.item(tablerow, 31).setCheckState(QtCore.Qt.Checked)

            item28 = QtWidgets.QTableWidgetItem()
            item28.setCheckState(QtCore.Qt.Unchecked)
            self.ui.tab_table.setItem(tablerow, 32, item28)
            equ = list(map(itemgetter(36), d))
            equ1 = equ[counter]
            if str(equ1) == "1":
                self.ui.tab_table.item(tablerow, 32).setCheckState(QtCore.Qt.Checked)

            item29 = QtWidgets.QTableWidgetItem()
            item29.setCheckState(QtCore.Qt.Unchecked)
            self.ui.tab_table.setItem(tablerow, 33, item29)
            equ = list(map(itemgetter(37), d))
            equ1 = equ[counter]
            if str(equ1) == "1":
                self.ui.tab_table.item(tablerow, 33).setCheckState(QtCore.Qt.Checked)

            item30 = QtWidgets.QTableWidgetItem()
            item30.setCheckState(QtCore.Qt.Unchecked)
            self.ui.tab_table.setItem(tablerow, 34, item30)
            equ = list(map(itemgetter(38), d))
            equ1 = equ[counter]
            if str(equ1) == "1":
                self.ui.tab_table.item(tablerow, 34).setCheckState(QtCore.Qt.Checked)

            item31 = QtWidgets.QTableWidgetItem()
            item31.setCheckState(QtCore.Qt.Unchecked)
            self.ui.tab_table.setItem(tablerow, 35, item31)
            equ = list(map(itemgetter(39), d))
            equ1 = equ[counter]
            if str(equ1) == "1":
                self.ui.tab_table.item(tablerow, 35).setCheckState(QtCore.Qt.Checked)

            item32 = QtWidgets.QTableWidgetItem()
            item32.setCheckState(QtCore.Qt.Unchecked)
            self.ui.tab_table.setItem(tablerow, 36, item32)
            equ = list(map(itemgetter(40), d))
            equ1 = equ[counter]
            if str(equ1) == "1":
                self.ui.tab_table.item(tablerow, 36).setCheckState(QtCore.Qt.Checked)

            item33 = QtWidgets.QTableWidgetItem()
            item33.setCheckState(QtCore.Qt.Unchecked)
            self.ui.tab_table.setItem(tablerow, 37, item33)
            equ = list(map(itemgetter(41), d))
            equ1 = equ[counter]
            if str(equ1) == "1":
                self.ui.tab_table.item(tablerow, 37).setCheckState(QtCore.Qt.Checked)

            item34 = QtWidgets.QTableWidgetItem()
            item34.setCheckState(QtCore.Qt.Unchecked)
            self.ui.tab_table.setItem(tablerow, 38, item34)
            equ = list(map(itemgetter(42), d))
            equ1 = equ[counter]
            if str(equ1) == "1":
                self.ui.tab_table.item(tablerow, 38).setCheckState(QtCore.Qt.Checked)

            item35 = QtWidgets.QTableWidgetItem()
            item35.setCheckState(QtCore.Qt.Unchecked)
            self.ui.tab_table.setItem(tablerow, 39, item35)
            equ = list(map(itemgetter(43), d))
            equ1 = equ[counter]
            if str(equ1) == "1":
                self.ui.tab_table.item(tablerow, 39).setCheckState(QtCore.Qt.Checked)

            item36 = QtWidgets.QTableWidgetItem()
            item36.setCheckState(QtCore.Qt.Unchecked)
            self.ui.tab_table.setItem(tablerow, 40, item36)
            equ = list(map(itemgetter(31), d))
            equ1 = equ[counter]
            if str(equ1) == "1":
                self.ui.tab_table.item(tablerow, 40).setCheckState(QtCore.Qt.Checked)

            self.ui.tab_table.setItem(tablerow, 41, QtWidgets.QTableWidgetItem(str(i[32])))


            tablerow += 1
            counter +=1


        c_p.execute("SELECT amount FROM payment WHERE diver_id = ?",(oid1))
        x3 = c_p.fetchall()
        x4 = list(map(itemgetter(0), x3))
        total_paid = 0


        for i in x4:
            total_paid = total_paid + i

        amount = x[0]
        amount1 = amount[4]
        bal = amount1 - total_paid

        c_c.execute("UPDATE customer SET balance = ? WHERE oid =?", (bal, oid1))

        self.ui.balance_results.setText("€"+str(bal))
        self.ui.amount_paid_results.setText("€"+str(total_paid))
        self.ui.total_mount_results.setText("€"+str(amount1))

        c_p.execute("SELECT * FROM payment WHERE diver_id =?", (oid1))
        x5=c_p.fetchall()
        rowcount2 = 0
        tablerow2 = 0
        for i in x5:
            rowcount2 += 1
            self.ui.tableWidget.setRowCount(rowcount2)
            self.ui.tableWidget.setItem(tablerow2, 0, QtWidgets.QTableWidgetItem(i[1]))
            self.ui.tableWidget.setItem(tablerow2, 1, QtWidgets.QTableWidgetItem(str(i[2])))
            tablerow2 += 1
            print(tablerow2)
            print(rowcount2)

        conn_customer.commit()
        conn_customer.close()
        conn_dives.commit()
        conn_dives.close()
        conn_tab.commit()
        conn_tab.close()
        conn_activities.commit()
        conn_activities.close()
        conn_payment.commit()
        conn_payment.close()

    def search_am_customer(self):
        conn_customer = sqlite3.connect("customer_info.db")
        c_c = conn_customer.cursor()

        record_id = self.ui.am_l_name_search_entry.text()

        c_c.execute("SELECT *, oid FROM customer WHERE last_name LIKE? ", [record_id])
        x = c_c.fetchall()

        print_oid = ""
        print_f_name = ""
        print_l_name = ""
        print_dob = ""

        for record in x:
            print_oid += str(record[10]) + "\n"
            print_f_name += str(record[0]) + "\n"
            print_l_name += str(record[1]) + "\n"
            print_dob += str(record[2]) + "\n"

        conn_customer.commit()
        conn_customer.close()

        self.ui.am_oid_search_results_label.setText(print_oid)
        self.ui.am_f_name_search_results_label.setText(print_f_name)
        self.ui.am_l_name_search_results_label.setText(print_l_name)
        self.ui.am_l_name_search_results_label_2.setText(print_dob)
        self.ui.am_l_name_search_results_label_2.adjustSize()
        self.ui.am_oid_search_results_label.adjustSize()
        self.ui.am_f_name_search_results_label.adjustSize()
        self.ui.am_l_name_search_results_label.adjustSize()

    def add_am_diver(self):

        global date

        conn_dives = sqlite3.connect("dives_record.db")
        c_d = conn_dives.cursor()
        c_d.execute("""INSERT INTO dives VALUES (
                        :date, 
                        :diver_id,
                        :activity, 
                        :guide,
                        :site, 
                        :time, 
                        :full_equ_dive,
                        :full_equ_day,
                        :full_equ_upgrade,
                        :computer_day,
                        :torch_day,
                        :bcd_dive,
                        :bcd_day,
                        :bcd_upgrade,
                        :reg_dive,
                        :reg_day,
                        :reg_upgrade,
                        :soft_dive,
                        :soft_day,
                        :soft_upgrade,
                        :eanx_upgrad,
                        :t_15l_upgrade,
                        :t_18l_upgrade,
                        :t_3l_air,
                        :t_3l_100,
                        :t_6l_50,
                        :t_6l_100,
                        :t_12l_50,
                        :t_12L_100,
                        :twin_air,
                        :twin_eanx,
                        :rebreather,
                        :sorb,
                        :no_tank,
                        :tech_reg,
                        :back_plate,
                        :wing,
                        :o2_reg,
                        :tech_computer,
                        :tech_torch,
                        :wreck_reel,
                        :smb,
                        :reel,
                        :slate
                        )""",
                        {"date" : date,
                        "diver_id" : self.ui.am_id_entry.text(),
                        "activity" : self.ui.am_activity_combo.currentText(),
                        "guide" : placeholder,
                        "site"  : placeholder,
                        "time" : am,
                        "full_equ_dive" : self.ui.am_full_equip_dive_check.isChecked(),
                        "full_equ_day" : self.ui.am_full_equip_day_check.isChecked(),
                        "full_equ_upgrade" : self.ui.am_full_equip_upgrade_check.isChecked(),
                        "computer_day" : self.ui.am_computer_check.isChecked(),
                        "torch_day" : self.ui.am_torch_check_2.isChecked(),
                        "bcd_dive" : self.ui.am_bcd_dive_check_2.isChecked(),
                        "bcd_day" : self.ui.am_bcd_day_check_2.isChecked(),
                        "bcd_upgrade" : self.ui.am_bcd_upgrade_check_2.isChecked(),
                        "reg_dive" : self.ui.am_reg_dive_check_2.isChecked(),
                        "reg_day" : self.ui.am_reg_day_check_2.isChecked(),
                        "reg_upgrade" : self.ui.am_reg_upgrade_check_2.isChecked(),
                        "soft_dive" : self.ui.am_soft_dive_check_2.isChecked(),
                        "soft_day" : self.ui.am_soft_day_check_2.isChecked(),
                        "soft_upgrade" : self.ui.am_soft_upgrade_check_2.isChecked(),
                        "eanx_upgrad" : self.ui.am_eanx_upgrade_check.isChecked(),
                        "t_15l_upgrade" : self.ui.am_15l_upgrade_check.isChecked(),
                        "t_18l_upgrade" : self.ui.am_18l_upgrade_check.isChecked(),
                        "t_3l_air" : self.ui.am_3l_air_check.isChecked(),
                        "t_3l_100" : self.ui.am_3l_100_check.isChecked(),
                        "t_6l_50" : self.ui.am_6l_50_check.isChecked(),
                        "t_6l_100" : self.ui.am_6l_100_check.isChecked(),
                        "t_12l_50" : self.ui.am_12l_50_check.isChecked(),
                        "t_12L_100" : self.ui.am_12l_100_check.isChecked(),
                        "twin_air" : self.ui.am_twin_air_check.isChecked(),
                        "twin_eanx" : self.ui.am_twin_eanx_check.isChecked(),
                        "rebreather" : self.ui.am_rebreather_check.isChecked(),
                        "sorb" : self.ui.am_sorb_entry.text(),
                        "no_tank" : self.ui.am_no_tank_check.isChecked(),
                        "tech_reg" : self.ui.am_tech_reg_check.isChecked(),
                        "back_plate" : self.ui.am_back_plate_check.isChecked(),
                        "wing" : self.ui.am_wing_check.isChecked(),
                        "o2_reg" : self.ui.am_o2_reg_check.isChecked(),
                        "tech_computer" : self.ui.am_tech_computer_check.isChecked(),
                        "tech_torch" : self.ui.am_tech_torch_check.isChecked(),
                        "wreck_reel" : self.ui.am_wreck_reel_check.isChecked(),
                        "smb" : self.ui.am_smb_check.isChecked(),
                        "reel" : self.ui.am_reel_check.isChecked(),
                        "slate" : self.ui.am_slate_check.isChecked()
                        })
        conn_dives.commit()
        conn_dives.close()
        self.update_am_tab()
        self.ui.stackedWidget.setCurrentWidget(self.ui.page_dives)
        self.refresh_all()
        self.ui.am_id_entry.setText("")
        self.ui.am_activity_combo.setCurrentIndex(0)
        self.ui.am_full_equip_dive_check.isChecked()
        self.ui.am_full_equip_day_check.setChecked(False)
        self.ui.am_full_equip_upgrade_check.setChecked(False)
        self.ui.am_computer_check.setChecked(False)
        self.ui.am_torch_check_2.setChecked(False)
        self.ui.am_bcd_dive_check_2.setChecked(False)
        self.ui.am_bcd_day_check_2.setChecked(False)
        self.ui.am_bcd_upgrade_check_2.setChecked(False)
        self.ui.am_reg_dive_check_2.setChecked(False)
        self.ui.am_reg_day_check_2.setChecked(False)
        self.ui.am_reg_upgrade_check_2.setChecked(False)
        self.ui.am_soft_dive_check_2.setChecked(False)
        self.ui.am_soft_day_check_2.setChecked(False)
        self.ui.am_soft_upgrade_check_2.setChecked(False)
        self.ui.am_eanx_upgrade_check.setChecked(False)
        self.ui.am_15l_upgrade_check.setChecked(False)
        self.ui.am_18l_upgrade_check.setChecked(False)
        self.ui.am_3l_air_check.setChecked(False)
        self.ui.am_3l_100_check.setChecked(False)
        self.ui.am_6l_50_check.setChecked(False)
        self.ui.am_6l_100_check.setChecked(False)
        self.ui.am_12l_50_check.setChecked(False)
        self.ui.am_12l_100_check.setChecked(False)
        self.ui.am_twin_air_check.setChecked(False)
        self.ui.am_twin_eanx_check.setChecked(False)
        self.ui.am_rebreather_check.setChecked(False)
        self.ui.am_sorb_entry.setText("0")
        self.ui.am_no_tank_check.setChecked(False)
        self.ui.am_tech_reg_check.setChecked(False)
        self.ui.am_back_plate_check.setChecked(False)
        self.ui.am_wing_check.setChecked(False)
        self.ui.am_o2_reg_check.setChecked(False)
        self.ui.am_tech_computer_check.setChecked(False)
        self.ui.am_tech_torch_check.setChecked(False)
        self.ui.am_wreck_reel_check.setChecked(False)
        self.ui.am_smb_check.setChecked(False)
        self.ui.am_reel_check.setChecked(False)
        self.ui.am_slate_check.setChecked(False)

    def update_am_tab(self):
        bal = ""
        oid = self.ui.am_id_entry.text()
        conn_customer = sqlite3.connect("customer_info.db")
        c_c = conn_customer.cursor()
        conn_dives = sqlite3.connect("dives_record.db")
        c_d = conn_dives.cursor()
        c_c.execute("SELECT total_cost FROM customer WHERE oid =" + oid)
        x = c_c.fetchall()
        ballist = list(map(itemgetter(0), x))
        bal = ballist[0]


        am_full_equip_dive_check =    self.ui.am_full_equip_dive_check
        am_full_equip_day_check =    self.ui.am_full_equip_day_check
        am_full_equip_upgrade_check =    self.ui.am_full_equip_upgrade_check
        am_computer_check =    self.ui.am_computer_check
        am_torch_check =    self.ui.am_torch_check_2
        am_bcd_dive_check =    self.ui.am_bcd_dive_check_2
        am_bcd_day_check =    self.ui.am_bcd_day_check_2
        am_bcd_upgrade_check =    self.ui.am_bcd_upgrade_check_2
        am_reg_dive_check =    self.ui.am_reg_dive_check_2
        am_reg_day_check =    self.ui.am_reg_day_check_2
        am_reg_upgrade_check =    self.ui.am_reg_upgrade_check_2
        am_soft_dive_check =    self.ui.am_soft_dive_check_2
        am_soft_day_check =    self.ui.am_soft_day_check_2
        am_soft_upgrade_check =    self.ui.am_soft_upgrade_check_2
        am_eanx_upgrade_check =    self.ui.am_eanx_upgrade_check
        am_15l_upgrade_check =    self.ui.am_15l_upgrade_check
        am_18l_upgrade_check =    self.ui.am_18l_upgrade_check
        am_3l_air_check =    self.ui.am_3l_air_check
        am_3l_100_check =    self.ui.am_3l_100_check
        am_6l_50_check =    self.ui.am_6l_50_check
        am_6l_100_check =    self.ui.am_6l_100_check
        am_12l_50_check =    self.ui.am_12l_50_check
        am_12l_100_check =    self.ui.am_12l_100_check
        am_twin_air_check =    self.ui.am_twin_air_check
        am_twin_eanx_check =    self.ui.am_twin_eanx_check
        am_rebreather_check =    self.ui.am_rebreather_check
        am_sorb =    self.ui.am_sorb_entry.text()
        am_tech_reg_check =    self.ui.am_tech_reg_check
        am_back_plate_check =    self.ui.am_back_plate_check
        am_wing_check =    self.ui.am_wing_check
        am_o2_reg_check =    self.ui.am_o2_reg_check
        am_tech_computer_check =    self.ui.am_tech_computer_check
        am_tech_torch_check =    self.ui.am_tech_torch_check
        am_wreck_reel_check =    self.ui.am_wreck_reel_check
        am_smb_check =    self.ui.am_smb_check
        am_reel_check =    self.ui.am_reel_check
        am_slate_check =    self.ui.am_slate_check

        oid1 = "1"
        conn_activities = sqlite3.connect("activities_info.db")
        c_a = conn_activities.cursor()
        c_a.execute("SELECT * FROM extras WHERE oid = " + oid1)
        x = c_a.fetchall()

        for i in x:
            if am_full_equip_dive_check.isChecked():
                am_full_equip_dive_ticked = i[0]
                bal = bal + int(am_full_equip_dive_ticked)
            if am_full_equip_day_check.isChecked():
                am_full_equip_day_ticked = i[1]
                bal = bal + int(am_full_equip_day_ticked)
            if am_full_equip_upgrade_check.isChecked():
                am_full_equip_upgrade_ticked = i[2]
                bal = bal + int(am_full_equip_upgrade_ticked)
            if am_computer_check.isChecked():
                am_computer_ticked = i[3]
                bal = bal + int(am_computer_ticked)
            if am_torch_check.isChecked():
                am_torch_ticked = i[4]
                bal = bal + int(am_torch_ticked)
            if am_bcd_dive_check.isChecked():
                am_bcd_dive_ticked = i[5]
                bal = bal + int(am_bcd_dive_ticked)
            if am_bcd_day_check.isChecked():
                am_bcd_day_ticked = i[6]
                bal = bal + int(am_bcd_day_ticked)
            if am_bcd_upgrade_check.isChecked():
                am_bcd_upgrade_ticked = i[7]
                bal = bal + int(am_bcd_upgrade_ticked)
            if am_reg_dive_check.isChecked():
                am_reg_dive_ticked = i[8]
                bal = bal + int(am_reg_dive_ticked)
            if am_reg_day_check.isChecked():
                am_reg_day_ticked = i[9]
                bal = bal+ int(am_reg_day_ticked)
            if am_reg_upgrade_check.isChecked():
                am_reg_upgrade_ticked = i[10]
                bal = bal + int(am_reg_upgrade_ticked)
            if am_soft_dive_check.isChecked():
                am_soft_dive_ticked = i[11]
                bal = bal + int(am_soft_dive_ticked)
            if am_soft_day_check.isChecked():
                am_soft_day_ticked = i[12]
                bal = bal +int(am_soft_day_ticked)
            if am_soft_upgrade_check.isChecked():
                am_soft_upgrade_ticked = i[13]
                bal = bal + int(am_soft_upgrade_ticked)
            if am_eanx_upgrade_check.isChecked():
                am_eanx_upgrade_ticked = i[14]
                bal = bal + int(am_eanx_upgrade_ticked)
            if am_15l_upgrade_check.isChecked():
                am_15l_upgrade_ticked = i[15]
                bal = bal + int(am_15l_upgrade_ticked)
            if am_18l_upgrade_check.isChecked():
                am_18l_upgrade_ticked = i[16]
                bal = bal + int(am_18l_upgrade_ticked)
            if am_3l_air_check.isChecked():
                am_3l_air_ticked = i[17]
                bal = bal + int(am_3l_air_ticked)
            if am_3l_100_check.isChecked():
                am_3l_100_ticked = i[18]
                bal = bal + int(am_3l_100_ticked)
            if am_6l_50_check.isChecked():
                am_6l_50_ticked = i[19]
                bal = bal + int(am_6l_50_ticked)
            if am_6l_100_check.isChecked():
                am_6l_100_ticked = i[20]
                bal = bal + int(am_6l_100_ticked)
            if am_12l_50_check.isChecked():
                am_12l_50_ticked = i[21]
                bal = bal + int(am_12l_50_ticked)
            if am_12l_100_check.isChecked():
                am_12l_100_ticked = i[22]
                bal = bal + int(am_12l_100_ticked)
            if am_twin_air_check.isChecked():
                am_twin_air_ticked = i[23]
                bal = bal + int(am_twin_air_ticked)
            if am_twin_eanx_check.isChecked():
                am_twin_eanx_ticked = i[24]
                bal = bal + int(am_twin_eanx_ticked)
            if am_rebreather_check.isChecked():
                am_rebreather_ticked = i[25]
                bal = bal + int(am_rebreather_ticked)
            if int(am_sorb) != 0:
                am_sorb_ticked = i[26]
                bal = bal + (int(am_sorb_ticked) * int(am_sorb))
            if am_tech_reg_check.isChecked():
                am_tech_reg_ticked = i[28]
                bal = bal + int(am_tech_reg_ticked)
            if am_back_plate_check.isChecked():
                am_back_plate_ticked = i[29]
                bal = bal + int(am_back_plate_ticked)
            if am_wing_check.isChecked():
                am_wing_ticked = i[30]
                bal = bal + int(am_wing_ticked)
            if am_o2_reg_check.isChecked():
                am_o2_reg_ticked = i[31]
                bal = bal + int(am_o2_reg_ticked)
            if am_tech_computer_check.isChecked():
                am_tech_computer_ticked = i[32]
                bal = bal + int(am_tech_computer_ticked)
            if am_tech_torch_check.isChecked():
                am_tech_torch_ticked = i[33]
                bal = bal + int(am_tech_torch_ticked)
            if am_wreck_reel_check.isChecked():
                am_wreck_reel_ticked = i[34]
                bal = bal + int(am_wreck_reel_ticked)
            if am_smb_check.isChecked():
                am_smb_ticked = i[35]
                bal = bal + int(am_smb_ticked)
            if am_reel_check.isChecked():
                am_reel_ticked = i[36]
                bal = bal + int(am_reel_ticked)
            if am_slate_check.isChecked():
                am_slate_ticked = i[37]
                bal = bal + int(am_slate_ticked)


        act = self.ui.am_activity_combo.currentText()

        c_a.execute("SELECT price, course FROM activity WHERE activity =?", ([act]))
        a = c_a.fetchall()
        price = a[0]
        price2 = price[0]
        course = a[0]
        course2 = course[1]

        c_d.execute("SELECT activity FROM dives WHERE diver_id =?", ([oid]))
        x3 = c_d.fetchall()
        list3 = list(map(itemgetter(0), x3))

        count = 0
        for course in list3:
            if course2 == 1:
                if course == act:
                    count += 1


        if count < 2:
            bal = bal + int(price2)


        c_c.execute("UPDATE customer SET total_cost = :total_cost WHERE oid =" + oid, {"total_cost": bal})
        conn_payment = sqlite3.connect("payment.db")
        c_p = conn_payment.cursor()
        c_p.execute("SELECT amount FROM payment WHERE diver_id = ?", (oid))
        x3 = c_p.fetchall()
        x4 = list(map(itemgetter(0), x3))
        total_paid = 0

        for i in x4:
            total_paid = total_paid + i



        bal2 = bal - total_paid

        c_c.execute("UPDATE customer SET balance = ? WHERE oid =?", (bal2, oid))
        conn_payment.commit()
        conn_payment.close()
        conn_activities.commit()
        conn_activities.close()
        conn_customer.commit()
        conn_customer.close()
        conn_dives.commit()
        conn_dives.close()

    def search_mam_customer(self):
        conn_customer = sqlite3.connect("customer_info.db")
        c_c = conn_customer.cursor()

        record_id = self.ui.mam_l_name_search_entry.text()

        c_c.execute("SELECT *, oid FROM customer WHERE last_name LIKE? ", [record_id])
        x = c_c.fetchall()

        print_oid = ""
        print_f_name = ""
        print_l_name = ""
        print_dob = ""

        for record in x:
            print_oid += str(record[10]) + "\n"
            print_f_name += str(record[0]) + "\n"
            print_l_name += str(record[1]) + "\n"
            print_dob += str(record[2]) + "\n"

        conn_customer.commit()
        conn_customer.close()

        self.ui.mam_oid_search_results_label.setText(print_oid)
        self.ui.mam_f_name_search_results_label.setText(print_f_name)
        self.ui.mam_l_name_search_results_label.setText(print_l_name)
        self.ui.mam_l_name_search_results_label_2.setText(print_dob)
        self.ui.mam_l_name_search_results_label_2.adjustSize()
        self.ui.mam_oid_search_results_label.adjustSize()
        self.ui.mam_f_name_search_results_label.adjustSize()
        self.ui.mam_l_name_search_results_label.adjustSize()

    def add_mam_diver(self):

        global date

        conn_dives = sqlite3.connect("dives_record.db")
        c_d = conn_dives.cursor()
        c_d.execute("""INSERT INTO dives VALUES (
                            :date, 
                            :diver_id,
                            :activity, 
                            :guide, 
                            :site,
                            :time, 
                            :full_equ_dive,
                            :full_equ_day,
                            :full_equ_upgrade,
                            :computer_day,
                            :torch_day,
                            :bcd_dive,
                            :bcd_day,
                            :bcd_upgrade,
                            :reg_dive,
                            :reg_day,
                            :reg_upgrade,
                            :soft_dive,
                            :soft_day,
                            :soft_upgrade,
                            :eanx_upgrad,
                            :t_15l_upgrade,
                            :t_18l_upgrade,
                            :t_3l_air,
                            :t_3l_100,
                            :t_6l_50,
                            :t_6l_100,
                            :t_12l_50,
                            :t_12L_100,
                            :twin_air,
                            :twin_eanx,
                            :rebreather,
                            :sorb,
                            :no_tank,
                            :tech_reg,
                            :back_plate,
                            :wing,
                            :o2_reg,
                            :tech_computer,
                            :tech_torch,
                            :wreck_reel,
                            :smb,
                            :reel,
                            :slate
                            )""",
                    {"date": date,
                     "diver_id": self.ui.mam_id_entry.text(),
                     "activity": self.ui.mam_activity_combo.currentText(),
                     "guide": placeholder,
                     "site": placeholder,
                     "time": mid,
                     "full_equ_dive": self.ui.mam_full_equip_dive_check.isChecked(),
                     "full_equ_day": self.ui.mam_full_equip_day_check.isChecked(),
                     "full_equ_upgrade": self.ui.mam_full_equip_upgrade_check.isChecked(),
                     "computer_day": self.ui.mam_computer_check.isChecked(),
                     "torch_day": self.ui.mam_torch_check.isChecked(),
                     "bcd_dive": self.ui.mam_bcd_dive_check.isChecked(),
                     "bcd_day": self.ui.mam_bcd_day_check.isChecked(),
                     "bcd_upgrade": self.ui.mam_bcd_upgrade_check.isChecked(),
                     "reg_dive": self.ui.mam_reg_dive_check.isChecked(),
                     "reg_day": self.ui.mam_reg_day_check.isChecked(),
                     "reg_upgrade": self.ui.mam_reg_upgrade_check.isChecked(),
                     "soft_dive": self.ui.mam_soft_dive_check.isChecked(),
                     "soft_day": self.ui.mam_soft_day_check.isChecked(),
                     "soft_upgrade": self.ui.mam_soft_upgrade_check.isChecked(),
                     "eanx_upgrad": self.ui.mam_eanx_upgrade_check.isChecked(),
                     "t_15l_upgrade": self.ui.mam_15l_upgrade_check.isChecked(),
                     "t_18l_upgrade": self.ui.mam_18l_upgrade_check.isChecked(),
                     "t_3l_air": self.ui.mam_3l_air_check.isChecked(),
                     "t_3l_100": self.ui.mam_3l_100_check.isChecked(),
                     "t_6l_50": self.ui.mam_6l_50_check.isChecked(),
                     "t_6l_100": self.ui.mam_6l_100_check.isChecked(),
                     "t_12l_50": self.ui.mam_12l_50_check.isChecked(),
                     "t_12L_100": self.ui.mam_12l_100_check.isChecked(),
                     "twin_air": self.ui.mam_twin_air_check.isChecked(),
                     "twin_eanx": self.ui.mam_twin_eanx_check.isChecked(),
                     "rebreather": self.ui.mam_rebreather_check_2.isChecked(),
                     "sorb": self.ui.mam_sorb_entry_2.text(),
                     "no_tank": self.ui.mam_no_tank_check.isChecked(),
                     "tech_reg": self.ui.mam_tech_reg_check_2.isChecked(),
                     "back_plate": self.ui.mam_back_plate_check_2.isChecked(),
                     "wing": self.ui.mam_wing_check_2.isChecked(),
                     "o2_reg": self.ui.mam_o2_reg_check_2.isChecked(),
                     "tech_computer": self.ui.mam_tech_computer_check_2.isChecked(),
                     "tech_torch": self.ui.mam_tech_torch_check_2.isChecked(),
                     "wreck_reel": self.ui.mam_wreck_reel_check_2.isChecked(),
                     "smb": self.ui.mam_smb_check_2.isChecked(),
                     "reel": self.ui.mam_reel_check_2.isChecked(),
                     "slate": self.ui.mam_slate_check_2.isChecked()
                     })
        conn_dives.commit()
        conn_dives.close()
        self.update_mam_tab()
        self.ui.stackedWidget.setCurrentWidget(self.ui.page_dives)
        self.refresh_all()
        self.ui.mam_id_entry.setText("")
        self.ui.mam_activity_combo.setCurrentIndex(0)
        self.ui.mam_full_equip_day_check.setChecked(False)
        self.ui.mam_full_equip_upgrade_check.setChecked(False)
        self.ui.mam_computer_check.setChecked(False)
        self.ui.mam_torch_check.setChecked(False)
        self.ui.mam_bcd_dive_check.setChecked(False)
        self.ui.mam_bcd_day_check.setChecked(False)
        self.ui.mam_bcd_upgrade_check.setChecked(False)
        self.ui.mam_reg_dive_check.setChecked(False)
        self.ui.mam_reg_day_check.setChecked(False)
        self.ui.mam_reg_upgrade_check.setChecked(False)
        self.ui.mam_soft_dive_check.setChecked(False)
        self.ui.mam_soft_day_check.setChecked(False)
        self.ui.mam_soft_upgrade_check.setChecked(False)
        self.ui.mam_eanx_upgrade_check.setChecked(False)
        self.ui.mam_15l_upgrade_check.setChecked(False)
        self.ui.mam_18l_upgrade_check.setChecked(False)
        self.ui.mam_3l_air_check.setChecked(False)
        self.ui.mam_3l_100_check.setChecked(False)
        self.ui.mam_6l_50_check.setChecked(False)
        self.ui.mam_6l_100_check.setChecked(False)
        self.ui.mam_12l_50_check.setChecked(False)
        self.ui.mam_12l_100_check.setChecked(False)
        self.ui.mam_twin_air_check.setChecked(False)
        self.ui.mam_twin_eanx_check.setChecked(False)
        self.ui.mam_rebreather_check_2.setChecked(False)
        self.ui.mam_sorb_entry_2.setText("0")
        self.ui.mam_no_tank_check.setChecked(False)
        self.ui.mam_tech_reg_check_2.setChecked(False)
        self.ui.mam_back_plate_check_2.setChecked(False)
        self.ui.mam_wing_check_2.setChecked(False)
        self.ui.mam_o2_reg_check_2.setChecked(False)
        self.ui.mam_tech_computer_check_2.setChecked(False)
        self.ui.mam_tech_torch_check_2.setChecked(False)
        self.ui.mam_wreck_reel_check_2.setChecked(False)
        self.ui.mam_smb_check_2.setChecked(False)
        self.ui.mam_reel_check_2.setChecked(False)
        self.ui.mam_slate_check_2.setChecked(False)

    def update_mam_tab(self):
        bal = ""
        oid = self.ui.mam_id_entry.text()
        conn_customer = sqlite3.connect("customer_info.db")
        c_c = conn_customer.cursor()
        conn_dives = sqlite3.connect("dives_record.db")
        c_d = conn_dives.cursor()
        c_c.execute("SELECT total_cost FROM customer WHERE oid =" + oid)
        x = c_c.fetchall()
        ballist = list(map(itemgetter(0), x))
        bal = ballist[0]


        mam_full_equip_dive_check =    self.ui.mam_full_equip_dive_check
        mam_full_equip_day_check =    self.ui.mam_full_equip_day_check
        mam_full_equip_upgrade_check =    self.ui.mam_full_equip_upgrade_check
        mam_computer_check =    self.ui.mam_computer_check
        mam_torch_check =    self.ui.mam_torch_check
        mam_bcd_dive_check =    self.ui.mam_bcd_dive_check
        mam_bcd_day_check =    self.ui.mam_bcd_day_check
        mam_bcd_upgrade_check =    self.ui.mam_bcd_upgrade_check
        mam_reg_dive_check =    self.ui.mam_reg_dive_check
        mam_reg_day_check =    self.ui.mam_reg_day_check
        mam_reg_upgrade_check =    self.ui.mam_reg_upgrade_check
        mam_soft_dive_check =    self.ui.mam_soft_dive_check
        mam_soft_day_check =    self.ui.mam_soft_day_check
        mam_soft_upgrade_check =    self.ui.mam_soft_upgrade_check
        mam_eanx_upgrade_check =    self.ui.mam_eanx_upgrade_check
        mam_15l_upgrade_check =    self.ui.mam_15l_upgrade_check
        mam_18l_upgrade_check =    self.ui.mam_18l_upgrade_check
        mam_3l_air_check =    self.ui.mam_3l_air_check
        mam_3l_100_check =    self.ui.mam_3l_100_check
        mam_6l_50_check =    self.ui.mam_6l_50_check
        mam_6l_100_check =    self.ui.mam_6l_100_check
        mam_12l_50_check =    self.ui.mam_12l_50_check
        mam_12l_100_check =    self.ui.mam_12l_100_check
        mam_twin_air_check =    self.ui.mam_twin_air_check
        mam_twin_eanx_check =    self.ui.mam_twin_eanx_check
        mam_rebreather_check =    self.ui.mam_rebreather_check_2
        mam_sorb =    self.ui.mam_sorb_entry_2.text()
        mam_tech_reg_check =    self.ui.mam_tech_reg_check_2
        mam_back_plate_check =    self.ui.mam_back_plate_check_2
        mam_wing_check =    self.ui.mam_wing_check_2
        mam_o2_reg_check =    self.ui.mam_o2_reg_check_2
        mam_tech_computer_check =    self.ui.mam_tech_computer_check_2
        mam_tech_torch_check =    self.ui.mam_tech_torch_check_2
        mam_wreck_reel_check =    self.ui.mam_wreck_reel_check_2
        mam_smb_check =    self.ui.mam_smb_check_2
        mam_reel_check =    self.ui.mam_reel_check_2
        mam_slate_check =    self.ui.mam_slate_check_2

        oid1 = "1"
        conn_activities = sqlite3.connect("activities_info.db")
        c_a = conn_activities.cursor()
        c_a.execute("SELECT * FROM extras WHERE oid = " + oid1)
        x = c_a.fetchall()

        for i in x:
            if mam_full_equip_dive_check.isChecked():
                mam_full_equip_dive_ticked = i[0]
                bal = bal + int(mam_full_equip_dive_ticked)
            if mam_full_equip_day_check.isChecked():
                mam_full_equip_day_ticked = i[1]
                bal = bal + int(mam_full_equip_day_ticked)
            if mam_full_equip_upgrade_check.isChecked():
                mam_full_equip_upgrade_ticked = i[2]
                bal = bal + int(mam_full_equip_upgrade_ticked)
            if mam_computer_check.isChecked():
                mam_computer_ticked = i[3]
                bal = bal + int(mam_computer_ticked)
            if mam_torch_check.isChecked():
                mam_torch_ticked = i[4]
                bal = bal + int(mam_torch_ticked)
            if mam_bcd_dive_check.isChecked():
                mam_bcd_dive_ticked = i[5]
                bal = bal + int(mam_bcd_dive_ticked)
            if mam_bcd_day_check.isChecked():
                mam_bcd_day_ticked = i[6]
                bal = bal + int(mam_bcd_day_ticked)
            if mam_bcd_upgrade_check.isChecked():
                mam_bcd_upgrade_ticked = i[7]
                bal = bal + int(mam_bcd_upgrade_ticked)
            if mam_reg_dive_check.isChecked():
                mam_reg_dive_ticked = i[8]
                bal = bal + int(mam_reg_dive_ticked)
            if mam_reg_day_check.isChecked():
                mam_reg_day_ticked = i[9]
                bal = bal+ int(mam_reg_day_ticked)
            if mam_reg_upgrade_check.isChecked():
                mam_reg_upgrade_ticked = i[10]
                bal = bal + int(mam_reg_upgrade_ticked)
            if mam_soft_dive_check.isChecked():
                mam_soft_dive_ticked = i[11]
                bal = bal + int(mam_soft_dive_ticked)
            if mam_soft_day_check.isChecked():
                mam_soft_day_ticked = i[12]
                bal = bal +int(mam_soft_day_ticked)
            if mam_soft_upgrade_check.isChecked():
                mam_soft_upgrade_ticked = i[13]
                bal = bal + int(mam_soft_upgrade_ticked)
            if mam_eanx_upgrade_check.isChecked():
                mam_eanx_upgrade_ticked = i[14]
                bal = bal + int(mam_eanx_upgrade_ticked)
            if mam_15l_upgrade_check.isChecked():
                mam_15l_upgrade_ticked = i[15]
                bal = bal + int(mam_15l_upgrade_ticked)
            if mam_18l_upgrade_check.isChecked():
                mam_18l_upgrade_ticked = i[16]
                bal = bal + int(mam_18l_upgrade_ticked)
            if mam_3l_air_check.isChecked():
                mam_3l_air_ticked = i[17]
                bal = bal + int(mam_3l_air_ticked)
            if mam_3l_100_check.isChecked():
                mam_3l_100_ticked = i[18]
                bal = bal + int(mam_3l_100_ticked)
            if mam_6l_50_check.isChecked():
                mam_6l_50_ticked = i[19]
                bal = bal + int(mam_6l_50_ticked)
            if mam_6l_100_check.isChecked():
                mam_6l_100_ticked = i[20]
                bal = bal + int(mam_6l_100_ticked)
            if mam_12l_50_check.isChecked():
                mam_12l_50_ticked = i[21]
                bal = bal + int(mam_12l_50_ticked)
            if mam_12l_100_check.isChecked():
                mam_12l_100_ticked = i[22]
                bal = bal + int(mam_12l_100_ticked)
            if mam_twin_air_check.isChecked():
                mam_twin_air_ticked = i[23]
                bal = bal + int(mam_twin_air_ticked)
            if mam_twin_eanx_check.isChecked():
                mam_twin_eanx_ticked = i[24]
                bal = bal + int(mam_twin_eanx_ticked)
            if mam_rebreather_check.isChecked():
                mam_rebreather_ticked = i[25]
                bal = bal + int(mam_rebreather_ticked)
            if int(mam_sorb) != 0:
                mam_sorb_ticked = i[26]
                bal = bal + (int(mam_sorb_ticked) * int(mam_sorb))
            if mam_tech_reg_check.isChecked():
                mam_tech_reg_ticked = i[28]
                bal = bal + int(mam_tech_reg_ticked)
            if mam_back_plate_check.isChecked():
                mam_back_plate_ticked = i[29]
                bal = bal + int(mam_back_plate_ticked)
            if mam_wing_check.isChecked():
                mam_wing_ticked = i[30]
                bal = bal + int(mam_wing_ticked)
            if mam_o2_reg_check.isChecked():
                mam_o2_reg_ticked = i[31]
                bal = bal + int(mam_o2_reg_ticked)
            if mam_tech_computer_check.isChecked():
                mam_tech_computer_ticked = i[32]
                bal = bal + int(mam_tech_computer_ticked)
            if mam_tech_torch_check.isChecked():
                mam_tech_torch_ticked = i[33]
                bal = bal + int(mam_tech_torch_ticked)
            if mam_wreck_reel_check.isChecked():
                mam_wreck_reel_ticked = i[34]
                bal = bal + int(mam_wreck_reel_ticked)
            if mam_smb_check.isChecked():
                mam_smb_ticked = i[35]
                bal = bal + int(mam_smb_ticked)
            if mam_reel_check.isChecked():
                mam_reel_ticked = i[36]
                bal = bal + int(mam_reel_ticked)
            if mam_slate_check.isChecked():
                mam_slate_ticked = i[37]
                bal = bal + int(mam_slate_ticked)


        act = self.ui.mam_activity_combo.currentText()

        c_a.execute("SELECT price, course FROM activity WHERE activity =?", ([act]))
        a = c_a.fetchall()
        price = a[0]
        price2 = price[0]
        course = a[0]
        course2 = course[1]

        c_d.execute("SELECT activity FROM dives WHERE diver_id =?", ([oid]))
        x3 = c_d.fetchall()
        list3 = list(map(itemgetter(0), x3))

        count = 0
        for course in list3:
            if course2 == 1:
                if course == act:
                    count += 1


        if count < 2:
            bal = bal + int(price2)


        c_c.execute("UPDATE customer SET total_cost = :total_cost WHERE oid =" + oid, {"total_cost": bal})
        conn_payment = sqlite3.connect("payment.db")
        c_p = conn_payment.cursor()
        c_p.execute("SELECT amount FROM payment WHERE diver_id = ?", (oid))
        x3 = c_p.fetchall()
        x4 = list(map(itemgetter(0), x3))
        total_paid = 0

        for i in x4:
            total_paid = total_paid + i

        bal2 = bal - total_paid

        c_c.execute("UPDATE customer SET balance = ? WHERE oid =?", (bal2, oid))
        conn_payment.commit()
        conn_payment.close()
        conn_activities.commit()
        conn_activities.close()
        conn_customer.commit()
        conn_customer.close()
        conn_dives.commit()
        conn_dives.close()

    def search_pm_customer(self):
        conn_customer = sqlite3.connect("customer_info.db")
        c_c = conn_customer.cursor()

        record_id = self.ui.pm_l_name_search_entry.text()

        c_c.execute("SELECT *, oid FROM customer WHERE last_name LIKE? ", [record_id])
        x = c_c.fetchall()

        print_oid = ""
        print_f_name = ""
        print_l_name = ""
        print_dob = ""

        for record in x:
            print_oid += str(record[10]) + "\n"
            print_f_name += str(record[0]) + "\n"
            print_l_name += str(record[1]) + "\n"
            print_dob += str(record[2]) + "\n"

        conn_customer.commit()
        conn_customer.close()

        self.ui.pm_oid_search_results_label.setText(print_oid)
        self.ui.pm_f_name_search_results_label.setText(print_f_name)
        self.ui.pm_l_name_search_results_label.setText(print_l_name)
        self.ui.pm_l_name_search_results_label_2.setText(print_dob)
        self.ui.pm_l_name_search_results_label_2.adjustSize()
        self.ui.pm_oid_search_results_label.adjustSize()
        self.ui.pm_f_name_search_results_label.adjustSize()
        self.ui.pm_l_name_search_results_label.adjustSize()

    def add_pm_diver(self):

        global date

        conn_dives = sqlite3.connect("dives_record.db")
        c_d = conn_dives.cursor()
        c_d.execute("""INSERT INTO dives VALUES (
                              :date, 
                              :diver_id,
                              :activity, 
                              :guide, 
                              :site,
                              :time, 
                              :full_equ_dive,
                              :full_equ_day,
                              :full_equ_upgrade,
                              :computer_day,
                              :torch_day,
                              :bcd_dive,
                              :bcd_day,
                              :bcd_upgrade,
                              :reg_dive,
                              :reg_day,
                              :reg_upgrade,
                              :soft_dive,
                              :soft_day,
                              :soft_upgrade,
                              :eanx_upgrad,
                              :t_15l_upgrade,
                              :t_18l_upgrade,
                              :t_3l_air,
                              :t_3l_100,
                              :t_6l_50,
                              :t_6l_100,
                              :t_12l_50,
                              :t_12L_100,
                              :twin_air,
                              :twin_eanx,
                              :rebreather,
                              :sorb,
                              :no_tank,
                              :tech_reg,
                              :back_plate,
                              :wing,
                              :o2_reg,
                              :tech_computer,
                              :tech_torch,
                              :wreck_reel,
                              :smb,
                              :reel,
                              :slate
                              )""",
                    {"date": date,
                     "diver_id": self.ui.pm_id_entry.text(),
                     "activity": self.ui.pm_activity_combo.currentText(),
                     "guide": placeholder,
                     "site": placeholder,
                     "time": pm,
                     "full_equ_dive": self.ui.pm_full_equip_dive_check.isChecked(),
                     "full_equ_day": self.ui.pm_full_equip_day_check.isChecked(),
                     "full_equ_upgrade": self.ui.pm_full_equip_upgrade_check.isChecked(),
                     "computer_day": self.ui.pm_computer_check.isChecked(),
                     "torch_day": self.ui.pm_torch_check.isChecked(),
                     "bcd_dive": self.ui.pm_bcd_dive_check.isChecked(),
                     "bcd_day": self.ui.pm_bcd_day_check.isChecked(),
                     "bcd_upgrade": self.ui.pm_bcd_upgrade_check.isChecked(),
                     "reg_dive": self.ui.pm_reg_dive_check.isChecked(),
                     "reg_day": self.ui.pm_reg_day_check.isChecked(),
                     "reg_upgrade": self.ui.pm_reg_upgrade_check.isChecked(),
                     "soft_dive": self.ui.pm_soft_dive_check.isChecked(),
                     "soft_day": self.ui.pm_soft_day_check.isChecked(),
                     "soft_upgrade": self.ui.pm_soft_upgrade_check.isChecked(),
                     "eanx_upgrad": self.ui.pm_eanx_upgrade_check.isChecked(),
                     "t_15l_upgrade": self.ui.pm_15l_upgrade_check.isChecked(),
                     "t_18l_upgrade": self.ui.pm_18l_upgrade_check.isChecked(),
                     "t_3l_air": self.ui.pm_3l_air_check.isChecked(),
                     "t_3l_100": self.ui.pm_3l_100_check.isChecked(),
                     "t_6l_50": self.ui.pm_6l_50_check.isChecked(),
                     "t_6l_100": self.ui.pm_6l_100_check.isChecked(),
                     "t_12l_50": self.ui.pm_12l_50_check.isChecked(),
                     "t_12L_100": self.ui.pm_12l_100_check.isChecked(),
                     "twin_air": self.ui.pm_twin_air_check.isChecked(),
                     "twin_eanx": self.ui.pm_twin_eanx_check.isChecked(),
                     "rebreather": self.ui.pm_rebreather_check.isChecked(),
                     "sorb": self.ui.pm_sorb_entry.text(),
                     "no_tank": self.ui.pm_no_tank_check.isChecked(),
                     "tech_reg": self.ui.pm_tech_reg_check.isChecked(),
                     "back_plate": self.ui.pm_back_plate_check.isChecked(),
                     "wing": self.ui.pm_wing_check.isChecked(),
                     "o2_reg": self.ui.pm_o2_reg_check.isChecked(),
                     "tech_computer": self.ui.pm_tech_computer_check.isChecked(),
                     "tech_torch": self.ui.pm_tech_torch_check.isChecked(),
                     "wreck_reel": self.ui.pm_wreck_reel_check.isChecked(),
                     "smb": self.ui.pm_smb_check.isChecked(),
                     "reel": self.ui.pm_reel_check.isChecked(),
                     "slate": self.ui.pm_slate_check.isChecked()
                     })
        conn_dives.commit()
        conn_dives.close()
        self.update_pm_tab()
        self.ui.stackedWidget.setCurrentWidget(self.ui.page_dives)
        self.refresh_all()
        self.ui.pm_id_entry.setText("")
        self.ui.pm_activity_combo.setCurrentIndex(0)
        self.ui.pm_full_equip_dive_check.isChecked()
        self.ui.pm_full_equip_day_check.setChecked(False)
        self.ui.pm_full_equip_upgrade_check.setChecked(False)
        self.ui.pm_computer_check.setChecked(False)
        self.ui.pm_torch_check.setChecked(False)
        self.ui.pm_bcd_dive_check.setChecked(False)
        self.ui.pm_bcd_day_check.setChecked(False)
        self.ui.pm_bcd_upgrade_check.setChecked(False)
        self.ui.pm_reg_dive_check.setChecked(False)
        self.ui.pm_reg_day_check.setChecked(False)
        self.ui.pm_reg_upgrade_check.setChecked(False)
        self.ui.pm_soft_dive_check.setChecked(False)
        self.ui.pm_soft_day_check.setChecked(False)
        self.ui.pm_soft_upgrade_check.setChecked(False)
        self.ui.pm_eanx_upgrade_check.setChecked(False)
        self.ui.pm_15l_upgrade_check.setChecked(False)
        self.ui.pm_18l_upgrade_check.setChecked(False)
        self.ui.pm_3l_air_check.setChecked(False)
        self.ui.pm_3l_100_check.setChecked(False)
        self.ui.pm_6l_50_check.setChecked(False)
        self.ui.pm_6l_100_check.setChecked(False)
        self.ui.pm_12l_50_check.setChecked(False)
        self.ui.pm_12l_100_check.setChecked(False)
        self.ui.pm_twin_air_check.setChecked(False)
        self.ui.pm_twin_eanx_check.setChecked(False)
        self.ui.pm_rebreather_check.setChecked(False)
        self.ui.pm_sorb_entry.setText("0")
        self.ui.pm_no_tank_check.setChecked(False)
        self.ui.pm_tech_reg_check.setChecked(False)
        self.ui.pm_back_plate_check.setChecked(False)
        self.ui.pm_wing_check.setChecked(False)
        self.ui.pm_o2_reg_check.setChecked(False)
        self.ui.pm_tech_computer_check.setChecked(False)
        self.ui.pm_tech_torch_check.setChecked(False)
        self.ui.pm_wreck_reel_check.setChecked(False)
        self.ui.pm_smb_check.setChecked(False)
        self.ui.pm_reel_check.setChecked(False)
        self.ui.pm_slate_check.setChecked(False)

    def update_pm_tab(self):
        bal = ""
        oid = self.ui.pm_id_entry.text()
        conn_customer = sqlite3.connect("customer_info.db")
        c_c = conn_customer.cursor()
        conn_dives = sqlite3.connect("dives_record.db")
        c_d = conn_dives.cursor()
        c_c.execute("SELECT total_cost FROM customer WHERE oid =" + oid)
        x = c_c.fetchall()
        ballist = list(map(itemgetter(0), x))
        bal = ballist[0]

        pm_full_equip_dive_check = self.ui.pm_full_equip_dive_check
        pm_full_equip_day_check = self.ui.pm_full_equip_day_check
        pm_full_equip_upgrade_check = self.ui.pm_full_equip_upgrade_check
        pm_computer_check = self.ui.pm_computer_check
        pm_torch_check = self.ui.pm_torch_check
        pm_bcd_dive_check = self.ui.pm_bcd_dive_check
        pm_bcd_day_check = self.ui.pm_bcd_day_check
        pm_bcd_upgrade_check = self.ui.pm_bcd_upgrade_check
        pm_reg_dive_check = self.ui.pm_reg_dive_check
        pm_reg_day_check = self.ui.pm_reg_day_check
        pm_reg_upgrade_check = self.ui.pm_reg_upgrade_check
        pm_soft_dive_check = self.ui.pm_soft_dive_check
        pm_soft_day_check = self.ui.pm_soft_day_check
        pm_soft_upgrade_check = self.ui.pm_soft_upgrade_check
        pm_eanx_upgrade_check = self.ui.pm_eanx_upgrade_check
        pm_15l_upgrade_check = self.ui.pm_15l_upgrade_check
        pm_18l_upgrade_check = self.ui.pm_18l_upgrade_check
        pm_3l_air_check = self.ui.pm_3l_air_check
        pm_3l_100_check = self.ui.pm_3l_100_check
        pm_6l_50_check = self.ui.pm_6l_50_check
        pm_6l_100_check = self.ui.pm_6l_100_check
        pm_12l_50_check = self.ui.pm_12l_50_check
        pm_12l_100_check = self.ui.pm_12l_100_check
        pm_twin_air_check = self.ui.pm_twin_air_check
        pm_twin_eanx_check = self.ui.pm_twin_eanx_check
        pm_rebreather_check = self.ui.pm_rebreather_check
        pm_sorb = self.ui.pm_sorb_entry.text()
        pm_tech_reg_check = self.ui.pm_tech_reg_check
        pm_back_plate_check = self.ui.pm_back_plate_check
        pm_wing_check = self.ui.pm_wing_check
        pm_o2_reg_check = self.ui.pm_o2_reg_check
        pm_tech_computer_check = self.ui.pm_tech_computer_check
        pm_tech_torch_check = self.ui.pm_tech_torch_check
        pm_wreck_reel_check = self.ui.pm_wreck_reel_check
        pm_smb_check = self.ui.pm_smb_check
        pm_reel_check = self.ui.pm_reel_check
        pm_slate_check = self.ui.pm_slate_check

        oid1 = "1"
        conn_activities = sqlite3.connect("activities_info.db")
        c_a = conn_activities.cursor()
        c_a.execute("SELECT * FROM extras WHERE oid = " + oid1)
        x = c_a.fetchall()

        for i in x:
            if pm_full_equip_dive_check.isChecked():
                pm_full_equip_dive_ticked = i[0]
                bal = bal + int(pm_full_equip_dive_ticked)
            if pm_full_equip_day_check.isChecked():
                pm_full_equip_day_ticked = i[1]
                bal = bal + int(pm_full_equip_day_ticked)
            if pm_full_equip_upgrade_check.isChecked():
                pm_full_equip_upgrade_ticked = i[2]
                bal = bal + int(pm_full_equip_upgrade_ticked)
            if pm_computer_check.isChecked():
                pm_computer_ticked = i[3]
                bal = bal + int(pm_computer_ticked)
            if pm_torch_check.isChecked():
                pm_torch_ticked = i[4]
                bal = bal + int(pm_torch_ticked)
            if pm_bcd_dive_check.isChecked():
                pm_bcd_dive_ticked = i[5]
                bal = bal + int(pm_bcd_dive_ticked)
            if pm_bcd_day_check.isChecked():
                pm_bcd_day_ticked = i[6]
                bal = bal + int(pm_bcd_day_ticked)
            if pm_bcd_upgrade_check.isChecked():
                pm_bcd_upgrade_ticked = i[7]
                bal = bal + int(pm_bcd_upgrade_ticked)
            if pm_reg_dive_check.isChecked():
                pm_reg_dive_ticked = i[8]
                bal = bal + int(pm_reg_dive_ticked)
            if pm_reg_day_check.isChecked():
                pm_reg_day_ticked = i[9]
                bal = bal + int(pm_reg_day_ticked)
            if pm_reg_upgrade_check.isChecked():
                pm_reg_upgrade_ticked = i[10]
                bal = bal + int(pm_reg_upgrade_ticked)
            if pm_soft_dive_check.isChecked():
                pm_soft_dive_ticked = i[11]
                bal = bal + int(pm_soft_dive_ticked)
            if pm_soft_day_check.isChecked():
                pm_soft_day_ticked = i[12]
                bal = bal + int(pm_soft_day_ticked)
            if pm_soft_upgrade_check.isChecked():
                pm_soft_upgrade_ticked = i[13]
                bal = bal + int(pm_soft_upgrade_ticked)
            if pm_eanx_upgrade_check.isChecked():
                pm_eanx_upgrade_ticked = i[14]
                bal = bal + int(pm_eanx_upgrade_ticked)
            if pm_15l_upgrade_check.isChecked():
                pm_15l_upgrade_ticked = i[15]
                bal = bal + int(pm_15l_upgrade_ticked)
            if pm_18l_upgrade_check.isChecked():
                pm_18l_upgrade_ticked = i[16]
                bal = bal + int(pm_18l_upgrade_ticked)
            if pm_3l_air_check.isChecked():
                pm_3l_air_ticked = i[17]
                bal = bal + int(pm_3l_air_ticked)
            if pm_3l_100_check.isChecked():
                pm_3l_100_ticked = i[18]
                bal = bal + int(pm_3l_100_ticked)
            if pm_6l_50_check.isChecked():
                pm_6l_50_ticked = i[19]
                bal = bal + int(pm_6l_50_ticked)
            if pm_6l_100_check.isChecked():
                pm_6l_100_ticked = i[20]
                bal = bal + int(pm_6l_100_ticked)
            if pm_12l_50_check.isChecked():
                pm_12l_50_ticked = i[21]
                bal = bal + int(pm_12l_50_ticked)
            if pm_12l_100_check.isChecked():
                pm_12l_100_ticked = i[22]
                bal = bal + int(pm_12l_100_ticked)
            if pm_twin_air_check.isChecked():
                pm_twin_air_ticked = i[23]
                bal = bal + int(pm_twin_air_ticked)
            if pm_twin_eanx_check.isChecked():
                pm_twin_eanx_ticked = i[24]
                bal = bal + int(pm_twin_eanx_ticked)
            if pm_rebreather_check.isChecked():
                pm_rebreather_ticked = i[25]
                bal = bal + int(pm_rebreather_ticked)
            if int(pm_sorb) != 0:
                pm_sorb_ticked = i[26]
                bal = bal + (int(pm_sorb_ticked) * int(pm_sorb))
            if pm_tech_reg_check.isChecked():
                pm_tech_reg_ticked = i[28]
                bal = bal + int(pm_tech_reg_ticked)
            if pm_back_plate_check.isChecked():
                pm_back_plate_ticked = i[29]
                bal = bal + int(pm_back_plate_ticked)
            if pm_wing_check.isChecked():
                pm_wing_ticked = i[30]
                bal = bal + int(pm_wing_ticked)
            if pm_o2_reg_check.isChecked():
                pm_o2_reg_ticked = i[31]
                bal = bal + int(pm_o2_reg_ticked)
            if pm_tech_computer_check.isChecked():
                pm_tech_computer_ticked = i[32]
                bal = bal + int(pm_tech_computer_ticked)
            if pm_tech_torch_check.isChecked():
                pm_tech_torch_ticked = i[33]
                bal = bal + int(pm_tech_torch_ticked)
            if pm_wreck_reel_check.isChecked():
                pm_wreck_reel_ticked = i[34]
                bal = bal + int(pm_wreck_reel_ticked)
            if pm_smb_check.isChecked():
                pm_smb_ticked = i[35]
                bal = bal + int(pm_smb_ticked)
            if pm_reel_check.isChecked():
                pm_reel_ticked = i[36]
                bal = bal + int(pm_reel_ticked)
            if pm_slate_check.isChecked():
                pm_slate_ticked = i[37]
                bal = bal + int(pm_slate_ticked)

        act = self.ui.pm_activity_combo.currentText()

        c_a.execute("SELECT price, course FROM activity WHERE activity =?", ([act]))
        a = c_a.fetchall()
        price = a[0]
        price2 = price[0]
        course = a[0]
        course2 = course[1]

        c_d.execute("SELECT activity FROM dives WHERE diver_id =?", ([oid]))
        x3 = c_d.fetchall()
        list3 = list(map(itemgetter(0), x3))

        count = 0
        for course in list3:
            if course2 == 1:
                if course == act:
                    count += 1

        if count < 2:
            bal = bal + int(price2)

        c_c.execute("UPDATE customer SET total_cost = :total_cost WHERE oid =" + oid, {"total_cost": bal})
        conn_payment = sqlite3.connect("payment.db")
        c_p = conn_payment.cursor()
        c_p.execute("SELECT amount FROM payment WHERE diver_id = ?", (oid))
        x3 = c_p.fetchall()
        x4 = list(map(itemgetter(0), x3))
        total_paid = 0

        for i in x4:
            total_paid = total_paid + i

        bal2 = bal - total_paid

        c_c.execute("UPDATE customer SET balance = ? WHERE oid =?", (bal2, oid))
        conn_payment.commit()
        conn_payment.close()
        conn_activities.commit()
        conn_activities.close()
        conn_customer.commit()
        conn_customer.close()
        conn_dives.commit()
        conn_dives.close()

    def search_zen_customer(self):
        conn_customer = sqlite3.connect("customer_info.db")
        c_c = conn_customer.cursor()

        record_id = self.ui.z_l_name_search_entry.text()

        c_c.execute("SELECT *, oid FROM customer WHERE last_name LIKE? ", [record_id])
        x = c_c.fetchall()

        print_oid = ""
        print_f_name = ""
        print_l_name = ""
        print_dob = ""

        for record in x:
            print_oid += str(record[10]) + "\n"
            print_f_name += str(record[0]) + "\n"
            print_l_name += str(record[1]) + "\n"
            print_dob += str(record[2]) + "\n"

        conn_customer.commit()
        conn_customer.close()

        self.ui.z_oid_search_results_label.setText(print_oid)
        self.ui.z_f_name_search_results_label.setText(print_f_name)
        self.ui.z_l_name_search_results_label.setText(print_l_name)
        self.ui.z_l_name_search_results_label_2.setText(print_dob)
        self.ui.z_l_name_search_results_label_2.adjustSize()
        self.ui.z_oid_search_results_label.adjustSize()
        self.ui.z_f_name_search_results_label.adjustSize()
        self.ui.z_l_name_search_results_label.adjustSize()

    def add_zen_diver(self):
        global date

        conn_dives = sqlite3.connect("dives_record.db")
        c_d = conn_dives.cursor()
        c_d.execute("""INSERT INTO dives VALUES (
                                :date, 
                                :diver_id,
                                :activity, 
                                :guide, 
                                :site,
                                :time, 
                                :full_equ_dive,
                                :full_equ_day,
                                :full_equ_upgrade,
                                :computer_day,
                                :torch_day,
                                :bcd_dive,
                                :bcd_day,
                                :bcd_upgrade,
                                :reg_dive,
                                :reg_day,
                                :reg_upgrade,
                                :soft_dive,
                                :soft_day,
                                :soft_upgrade,
                                :eanx_upgrad,
                                :t_15l_upgrade,
                                :t_18l_upgrade,
                                :t_3l_air,
                                :t_3l_100,
                                :t_6l_50,
                                :t_6l_100,
                                :t_12l_50,
                                :t_12L_100,
                                :twin_air,
                                :twin_eanx,
                                :rebreather,
                                :sorb,
                                :no_tank,
                                :tech_reg,
                                :back_plate,
                                :wing,
                                :o2_reg,
                                :tech_computer,
                                :tech_torch,
                                :wreck_reel,
                                :smb,
                                :reel,
                                :slate
                                )""",
                    {"date": date,
                     "diver_id": self.ui.z_id_entry.text(),
                     "activity": self.ui.z_activity_combo.currentText(),
                     "guide": placeholder,
                     "site": placeholder,
                     "time": zen,
                     "full_equ_dive": self.ui.z_full_equip_dive_check.isChecked(),
                     "full_equ_day": self.ui.z_full_equip_day_check.isChecked(),
                     "full_equ_upgrade": self.ui.z_full_equip_upgrade_check.isChecked(),
                     "computer_day": self.ui.z_computer_check.isChecked(),
                     "torch_day": self.ui.z_torch_check.isChecked(),
                     "bcd_dive": self.ui.z_bcd_dive_check.isChecked(),
                     "bcd_day": self.ui.z_bcd_day_check.isChecked(),
                     "bcd_upgrade": self.ui.z_bcd_upgrade_check.isChecked(),
                     "reg_dive": self.ui.z_reg_dive_check.isChecked(),
                     "reg_day": self.ui.z_reg_day_check.isChecked(),
                     "reg_upgrade": self.ui.z_reg_upgrade_check.isChecked(),
                     "soft_dive": self.ui.z_soft_dive_check.isChecked(),
                     "soft_day": self.ui.z_soft_day_check.isChecked(),
                     "soft_upgrade": self.ui.z_soft_upgrade_check.isChecked(),
                     "eanx_upgrad": self.ui.z_eanx_upgrade_check.isChecked(),
                     "t_15l_upgrade": self.ui.z_15l_upgrade_check.isChecked(),
                     "t_18l_upgrade": self.ui.z_18l_upgrade_check.isChecked(),
                     "t_3l_air": self.ui.z_3l_air_check.isChecked(),
                     "t_3l_100": self.ui.z_3l_100_check.isChecked(),
                     "t_6l_50": self.ui.z_6l_50_check.isChecked(),
                     "t_6l_100": self.ui.z_6l_100_check.isChecked(),
                     "t_12l_50": self.ui.z_12l_50_check.isChecked(),
                     "t_12L_100": self.ui.z_12l_100_check.isChecked(),
                     "twin_air": self.ui.z_twin_air_check.isChecked(),
                     "twin_eanx": self.ui.z_twin_eanx_check.isChecked(),
                     "rebreather": self.ui.z_rebreather_check.isChecked(),
                     "sorb": self.ui.z_sorb_entry.text(),
                     "no_tank": self.ui.z_no_tank_check.isChecked(),
                     "tech_reg": self.ui.z_tech_reg_check.isChecked(),
                     "back_plate": self.ui.z_back_plate_check.isChecked(),
                     "wing": self.ui.z_wing_check.isChecked(),
                     "o2_reg": self.ui.z_o2_reg_check.isChecked(),
                     "tech_computer": self.ui.z_tech_computer_check.isChecked(),
                     "tech_torch": self.ui.z_tech_torch_check.isChecked(),
                     "wreck_reel": self.ui.z_wreck_reel_check.isChecked(),
                     "smb": self.ui.z_smb_check.isChecked(),
                     "reel": self.ui.z_reel_check.isChecked(),
                     "slate": self.ui.z_slate_check.isChecked()
                     })
        conn_dives.commit()
        conn_dives.close()
        self.update_zen_tab()
        self.ui.stackedWidget.setCurrentWidget(self.ui.page_dives)
        self.refresh_all()
        self.ui.z_id_entry.setText("")
        self.ui.z_activity_combo.setCurrentIndex(0)
        self.ui.z_full_equip_dive_check.isChecked()
        self.ui.z_full_equip_day_check.setChecked(False)
        self.ui.z_full_equip_upgrade_check.setChecked(False)
        self.ui.z_computer_check.setChecked(False)
        self.ui.z_torch_check.setChecked(False)
        self.ui.z_bcd_dive_check.setChecked(False)
        self.ui.z_bcd_day_check.setChecked(False)
        self.ui.z_bcd_upgrade_check.setChecked(False)
        self.ui.z_reg_dive_check.setChecked(False)
        self.ui.z_reg_day_check.setChecked(False)
        self.ui.z_reg_upgrade_check.setChecked(False)
        self.ui.z_soft_dive_check.setChecked(False)
        self.ui.z_soft_day_check.setChecked(False)
        self.ui.z_soft_upgrade_check.setChecked(False)
        self.ui.z_eanx_upgrade_check.setChecked(False)
        self.ui.z_15l_upgrade_check.setChecked(False)
        self.ui.z_18l_upgrade_check.setChecked(False)
        self.ui.z_3l_air_check.setChecked(False)
        self.ui.z_3l_100_check.setChecked(False)
        self.ui.z_6l_50_check.setChecked(False)
        self.ui.z_6l_100_check.setChecked(False)
        self.ui.z_12l_50_check.setChecked(False)
        self.ui.z_12l_100_check.setChecked(False)
        self.ui.z_twin_air_check.setChecked(False)
        self.ui.z_twin_eanx_check.setChecked(False)
        self.ui.z_rebreather_check.setChecked(False)
        self.ui.z_sorb_entry.setText("0")
        self.ui.z_no_tank_check.setChecked(False)
        self.ui.z_tech_reg_check.setChecked(False)
        self.ui.z_back_plate_check.setChecked(False)
        self.ui.z_wing_check.setChecked(False)
        self.ui.z_o2_reg_check.setChecked(False)
        self.ui.z_tech_computer_check.setChecked(False)
        self.ui.z_tech_torch_check.setChecked(False)
        self.ui.z_wreck_reel_check.setChecked(False)
        self.ui.z_smb_check.setChecked(False)
        self.ui.z_reel_check.setChecked(False)
        self.ui.z_slate_check.setChecked(False)

    def update_zen_tab(self):
        bal = ""
        oid = self.ui.z_id_entry.text()
        conn_customer = sqlite3.connect("customer_info.db")
        c_c = conn_customer.cursor()
        conn_dives = sqlite3.connect("dives_record.db")
        c_d = conn_dives.cursor()
        c_c.execute("SELECT total_cost FROM customer WHERE oid =" + oid)
        x = c_c.fetchall()
        ballist = list(map(itemgetter(0), x))
        bal = ballist[0]

        z_full_equip_dive_check = self.ui.z_full_equip_dive_check
        z_full_equip_day_check = self.ui.z_full_equip_day_check
        z_full_equip_upgrade_check = self.ui.z_full_equip_upgrade_check
        z_computer_check = self.ui.z_computer_check
        z_torch_check = self.ui.z_torch_check
        z_bcd_dive_check = self.ui.z_bcd_dive_check
        z_bcd_day_check = self.ui.z_bcd_day_check
        z_bcd_upgrade_check = self.ui.z_bcd_upgrade_check
        z_reg_dive_check = self.ui.z_reg_dive_check
        z_reg_day_check = self.ui.z_reg_day_check
        z_reg_upgrade_check = self.ui.z_reg_upgrade_check
        z_soft_dive_check = self.ui.z_soft_dive_check
        z_soft_day_check = self.ui.z_soft_day_check
        z_soft_upgrade_check = self.ui.z_soft_upgrade_check
        z_eanx_upgrade_check = self.ui.z_eanx_upgrade_check
        z_15l_upgrade_check = self.ui.z_15l_upgrade_check
        z_18l_upgrade_check = self.ui.z_18l_upgrade_check
        z_3l_air_check = self.ui.z_3l_air_check
        z_3l_100_check = self.ui.z_3l_100_check
        z_6l_50_check = self.ui.z_6l_50_check
        z_6l_100_check = self.ui.z_6l_100_check
        z_12l_50_check = self.ui.z_12l_50_check
        z_12l_100_check = self.ui.z_12l_100_check
        z_twin_air_check = self.ui.z_twin_air_check
        z_twin_eanx_check = self.ui.z_twin_eanx_check
        z_rebreather_check = self.ui.z_rebreather_check
        z_sorb = self.ui.z_sorb_entry.text()
        z_tech_reg_check = self.ui.z_tech_reg_check
        z_back_plate_check = self.ui.z_back_plate_check
        z_wing_check = self.ui.z_wing_check
        z_o2_reg_check = self.ui.z_o2_reg_check
        z_tech_computer_check = self.ui.z_tech_computer_check
        z_tech_torch_check = self.ui.z_tech_torch_check
        z_wreck_reel_check = self.ui.z_wreck_reel_check
        z_smb_check = self.ui.z_smb_check
        z_reel_check = self.ui.z_reel_check
        z_slate_check = self.ui.z_slate_check

        oid1 = "1"
        conn_activities = sqlite3.connect("activities_info.db")
        c_a = conn_activities.cursor()
        c_a.execute("SELECT * FROM extras WHERE oid = " + oid1)
        x = c_a.fetchall()

        for i in x:
            if z_full_equip_dive_check.isChecked():
                z_full_equip_dive_ticked = i[0]
                bal = bal + int(z_full_equip_dive_ticked)
            if z_full_equip_day_check.isChecked():
                z_full_equip_day_ticked = i[1]
                bal = bal + int(z_full_equip_day_ticked)
            if z_full_equip_upgrade_check.isChecked():
                z_full_equip_upgrade_ticked = i[2]
                bal = bal + int(z_full_equip_upgrade_ticked)
            if z_computer_check.isChecked():
                z_computer_ticked = i[3]
                bal = bal + int(z_computer_ticked)
            if z_torch_check.isChecked():
                z_torch_ticked = i[4]
                bal = bal + int(z_torch_ticked)
            if z_bcd_dive_check.isChecked():
                z_bcd_dive_ticked = i[5]
                bal = bal + int(z_bcd_dive_ticked)
            if z_bcd_day_check.isChecked():
                z_bcd_day_ticked = i[6]
                bal = bal + int(z_bcd_day_ticked)
            if z_bcd_upgrade_check.isChecked():
                z_bcd_upgrade_ticked = i[7]
                bal = bal + int(z_bcd_upgrade_ticked)
            if z_reg_dive_check.isChecked():
                z_reg_dive_ticked = i[8]
                bal = bal + int(z_reg_dive_ticked)
            if z_reg_day_check.isChecked():
                z_reg_day_ticked = i[9]
                bal = bal + int(z_reg_day_ticked)
            if z_reg_upgrade_check.isChecked():
                z_reg_upgrade_ticked = i[10]
                bal = bal + int(z_reg_upgrade_ticked)
            if z_soft_dive_check.isChecked():
                z_soft_dive_ticked = i[11]
                bal = bal + int(z_soft_dive_ticked)
            if z_soft_day_check.isChecked():
                z_soft_day_ticked = i[12]
                bal = bal + int(z_soft_day_ticked)
            if z_soft_upgrade_check.isChecked():
                z_soft_upgrade_ticked = i[13]
                bal = bal + int(z_soft_upgrade_ticked)
            if z_eanx_upgrade_check.isChecked():
                z_eanx_upgrade_ticked = i[14]
                bal = bal + int(z_eanx_upgrade_ticked)
            if z_15l_upgrade_check.isChecked():
                z_15l_upgrade_ticked = i[15]
                bal = bal + int(z_15l_upgrade_ticked)
            if z_18l_upgrade_check.isChecked():
                z_18l_upgrade_ticked = i[16]
                bal = bal + int(z_18l_upgrade_ticked)
            if z_3l_air_check.isChecked():
                z_3l_air_ticked = i[17]
                bal = bal + int(z_3l_air_ticked)
            if z_3l_100_check.isChecked():
                z_3l_100_ticked = i[18]
                bal = bal + int(z_3l_100_ticked)
            if z_6l_50_check.isChecked():
                z_6l_50_ticked = i[19]
                bal = bal + int(z_6l_50_ticked)
            if z_6l_100_check.isChecked():
                z_6l_100_ticked = i[20]
                bal = bal + int(z_6l_100_ticked)
            if z_12l_50_check.isChecked():
                z_12l_50_ticked = i[21]
                bal = bal + int(z_12l_50_ticked)
            if z_12l_100_check.isChecked():
                z_12l_100_ticked = i[22]
                bal = bal + int(z_12l_100_ticked)
            if z_twin_air_check.isChecked():
                z_twin_air_ticked = i[23]
                bal = bal + int(z_twin_air_ticked)
            if z_twin_eanx_check.isChecked():
                z_twin_eanx_ticked = i[24]
                bal = bal + int(z_twin_eanx_ticked)
            if z_rebreather_check.isChecked():
                z_rebreather_ticked = i[25]
                bal = bal + int(z_rebreather_ticked)
            if int(z_sorb) != 0:
                z_sorb_ticked = i[26]
                bal = bal + (int(z_sorb_ticked) * int(z_sorb))
            if z_tech_reg_check.isChecked():
                z_tech_reg_ticked = i[28]
                bal = bal + int(z_tech_reg_ticked)
            if z_back_plate_check.isChecked():
                z_back_plate_ticked = i[29]
                bal = bal + int(z_back_plate_ticked)
            if z_wing_check.isChecked():
                z_wing_ticked = i[30]
                bal = bal + int(z_wing_ticked)
            if z_o2_reg_check.isChecked():
                z_o2_reg_ticked = i[31]
                bal = bal + int(z_o2_reg_ticked)
            if z_tech_computer_check.isChecked():
                z_tech_computer_ticked = i[32]
                bal = bal + int(z_tech_computer_ticked)
            if z_tech_torch_check.isChecked():
                z_tech_torch_ticked = i[33]
                bal = bal + int(z_tech_torch_ticked)
            if z_wreck_reel_check.isChecked():
                z_wreck_reel_ticked = i[34]
                bal = bal + int(z_wreck_reel_ticked)
            if z_smb_check.isChecked():
                z_smb_ticked = i[35]
                bal = bal + int(z_smb_ticked)
            if z_reel_check.isChecked():
                z_reel_ticked = i[36]
                bal = bal + int(z_reel_ticked)
            if z_slate_check.isChecked():
                z_slate_ticked = i[37]
                bal = bal + int(z_slate_ticked)

        act = self.ui.z_activity_combo.currentText()

        c_a.execute("SELECT price, course FROM activity WHERE activity =?", ([act]))
        a = c_a.fetchall()
        price = a[0]
        price2 = price[0]
        course = a[0]
        course2 = course[1]

        c_d.execute("SELECT activity FROM dives WHERE diver_id =?", ([oid]))
        x3 = c_d.fetchall()
        list3 = list(map(itemgetter(0), x3))

        count = 0
        for course in list3:
            if course2 == 1:
                if course == act:
                    count += 1

        if count < 2:
            bal = bal + int(price2)

        c_c.execute("UPDATE customer SET total_cost = :total_cost WHERE oid =" + oid, {"total_cost": bal})
        conn_payment = sqlite3.connect("payment.db")
        c_p = conn_payment.cursor()
        c_p.execute("SELECT amount FROM payment WHERE diver_id = ?", (oid))
        x3 = c_p.fetchall()
        x4 = list(map(itemgetter(0), x3))
        total_paid = 0

        for i in x4:
            total_paid = total_paid + i

        bal2 = bal - total_paid

        c_c.execute("UPDATE customer SET balance = ? WHERE oid =?", (bal2, oid))
        conn_payment.commit()
        conn_payment.close()
        conn_activities.commit()
        conn_activities.close()
        conn_customer.commit()
        conn_customer.close()
        conn_dives.commit()
        conn_dives.close()

    def search_co_customer(self):
        conn_customer = sqlite3.connect("customer_info.db")
        c_c = conn_customer.cursor()

        record_id = self.ui.co_l_name_search_entry.text()

        c_c.execute("SELECT *, oid FROM customer WHERE last_name LIKE? ", [record_id])
        x = c_c.fetchall()

        print_oid = ""
        print_f_name = ""
        print_l_name = ""
        print_dob = ""

        for record in x:
            print_oid += str(record[10]) + "\n"
            print_f_name += str(record[0]) + "\n"
            print_l_name += str(record[1]) + "\n"
            print_dob += str(record[2]) + "\n"

        conn_customer.commit()
        conn_customer.close()

        self.ui.co_oid_search_results_label.setText(print_oid)
        self.ui.co_f_name_search_results_label.setText(print_f_name)
        self.ui.co_l_name_search_results_label.setText(print_l_name)
        self.ui.co_l_name_search_results_label_2.setText(print_dob)
        self.ui.co_l_name_search_results_label_2.adjustSize()
        self.ui.co_oid_search_results_label.adjustSize()
        self.ui.co_f_name_search_results_label.adjustSize()
        self.ui.co_l_name_search_results_label.adjustSize()

    def add_co_diver(self):
        global date

        conn_dives = sqlite3.connect("dives_record.db")
        c_d = conn_dives.cursor()
        c_d.execute("""INSERT INTO dives VALUES (
                              :date, 
                              :diver_id,
                              :activity, 
                              :guide, 
                              :site,
                              :time, 
                              :full_equ_dive,
                              :full_equ_day,
                              :full_equ_upgrade,
                              :computer_day,
                              :torch_day,
                              :bcd_dive,
                              :bcd_day,
                              :bcd_upgrade,
                              :reg_dive,
                              :reg_day,
                              :reg_upgrade,
                              :soft_dive,
                              :soft_day,
                              :soft_upgrade,
                              :eanx_upgrad,
                              :t_15l_upgrade,
                              :t_18l_upgrade,
                              :t_3l_air,
                              :t_3l_100,
                              :t_6l_50,
                              :t_6l_100,
                              :t_12l_50,
                              :t_12L_100,
                              :twin_air,
                              :twin_eanx,
                              :rebreather,
                              :sorb,
                              :no_tank,
                              :tech_reg,
                              :back_plate,
                              :wing,
                              :o2_reg,
                              :tech_computer,
                              :tech_torch,
                              :wreck_reel,
                              :smb,
                              :reel,
                              :slate
                              )""",
                    {"date": date,
                     "diver_id": self.ui.co_id_entry.text(),
                     "activity": self.ui.co_activity_combo.currentText(),
                     "guide": placeholder,
                     "site": placeholder,
                     "time": co,
                     "full_equ_dive": self.ui.co_full_equip_dive_check.isChecked(),
                     "full_equ_day": self.ui.co_full_equip_day_check.isChecked(),
                     "full_equ_upgrade": self.ui.co_full_equip_upgrade_check.isChecked(),
                     "computer_day": self.ui.co_computer_check.isChecked(),
                     "torch_day": self.ui.co_torch_check.isChecked(),
                     "bcd_dive": self.ui.co_bcd_dive_check.isChecked(),
                     "bcd_day": self.ui.co_bcd_day_check.isChecked(),
                     "bcd_upgrade": self.ui.co_bcd_upgrade_check.isChecked(),
                     "reg_dive": self.ui.co_reg_dive_check.isChecked(),
                     "reg_day": self.ui.co_reg_day_check.isChecked(),
                     "reg_upgrade": self.ui.co_reg_upgrade_check.isChecked(),
                     "soft_dive": self.ui.co_soft_dive_check.isChecked(),
                     "soft_day": self.ui.co_soft_day_check.isChecked(),
                     "soft_upgrade": self.ui.co_soft_upgrade_check.isChecked(),
                     "eanx_upgrad": self.ui.co_eanx_upgrade_check.isChecked(),
                     "t_15l_upgrade": self.ui.co_15l_upgrade_check.isChecked(),
                     "t_18l_upgrade": self.ui.co_18l_upgrade_check.isChecked(),
                     "t_3l_air": self.ui.co_3l_air_check.isChecked(),
                     "t_3l_100": self.ui.co_3l_100_check.isChecked(),
                     "t_6l_50": self.ui.co_6l_50_check.isChecked(),
                     "t_6l_100": self.ui.co_6l_100_check.isChecked(),
                     "t_12l_50": self.ui.co_12l_50_check.isChecked(),
                     "t_12L_100": self.ui.co_12l_100_check.isChecked(),
                     "twin_air": self.ui.co_twin_air_check.isChecked(),
                     "twin_eanx": self.ui.co_twin_eanx_check.isChecked(),
                     "rebreather": self.ui.co_rebreather_check.isChecked(),
                     "sorb": self.ui.co_sorb_entry.text(),
                     "no_tank": self.ui.co_no_tank_check.isChecked(),
                     "tech_reg": self.ui.co_tech_reg_check.isChecked(),
                     "back_plate": self.ui.co_back_plate_check.isChecked(),
                     "wing": self.ui.co_wing_check.isChecked(),
                     "o2_reg": self.ui.co_o2_reg_check.isChecked(),
                     "tech_computer": self.ui.co_tech_computer_check.isChecked(),
                     "tech_torch": self.ui.co_tech_torch_check.isChecked(),
                     "wreck_reel": self.ui.co_wreck_reel_check.isChecked(),
                     "smb": self.ui.co_smb_check.isChecked(),
                     "reel": self.ui.co_reel_check.isChecked(),
                     "slate": self.ui.co_slate_check.isChecked()
                     })
        conn_dives.commit()
        conn_dives.close()
        self.update_co_tab()
        self.ui.stackedWidget.setCurrentWidget(self.ui.page_dives)
        self.refresh_all()
        self.ui.co_id_entry.setText("")
        self.ui.co_activity_combo.setCurrentIndex(0)
        self.ui.co_full_equip_dive_check.isChecked()
        self.ui.co_full_equip_day_check.setChecked(False)
        self.ui.co_full_equip_upgrade_check.setChecked(False)
        self.ui.co_computer_check.setChecked(False)
        self.ui.co_torch_check.setChecked(False)
        self.ui.co_bcd_dive_check.setChecked(False)
        self.ui.co_bcd_day_check.setChecked(False)
        self.ui.co_bcd_upgrade_check.setChecked(False)
        self.ui.co_reg_dive_check.setChecked(False)
        self.ui.co_reg_day_check.setChecked(False)
        self.ui.co_reg_upgrade_check.setChecked(False)
        self.ui.co_soft_dive_check.setChecked(False)
        self.ui.co_soft_day_check.setChecked(False)
        self.ui.co_soft_upgrade_check.setChecked(False)
        self.ui.co_eanx_upgrade_check.setChecked(False)
        self.ui.co_15l_upgrade_check.setChecked(False)
        self.ui.co_18l_upgrade_check.setChecked(False)
        self.ui.co_3l_air_check.setChecked(False)
        self.ui.co_3l_100_check.setChecked(False)
        self.ui.co_6l_50_check.setChecked(False)
        self.ui.co_6l_100_check.setChecked(False)
        self.ui.co_12l_50_check.setChecked(False)
        self.ui.co_12l_100_check.setChecked(False)
        self.ui.co_twin_air_check.setChecked(False)
        self.ui.co_twin_eanx_check.setChecked(False)
        self.ui.co_rebreather_check.setChecked(False)
        self.ui.co_sorb_entry.setText("0")
        self.ui.co_no_tank_check.setChecked(False)
        self.ui.co_tech_reg_check.setChecked(False)
        self.ui.co_back_plate_check.setChecked(False)
        self.ui.co_wing_check.setChecked(False)
        self.ui.co_o2_reg_check.setChecked(False)
        self.ui.co_tech_computer_check.setChecked(False)
        self.ui.co_tech_torch_check.setChecked(False)
        self.ui.co_wreck_reel_check.setChecked(False)
        self.ui.co_smb_check.setChecked(False)
        self.ui.co_reel_check.setChecked(False)
        self.ui.co_slate_check.setChecked(False)

    def update_co_tab(self):
        bal = ""
        oid = self.ui.co_id_entry.text()
        conn_customer = sqlite3.connect("customer_info.db")
        c_c = conn_customer.cursor()
        conn_dives = sqlite3.connect("dives_record.db")
        c_d = conn_dives.cursor()
        c_c.execute("SELECT total_cost FROM customer WHERE oid =" + oid)
        x = c_c.fetchall()
        ballist = list(map(itemgetter(0), x))
        bal = ballist[0]

        co_full_equip_dive_check = self.ui.co_full_equip_dive_check
        co_full_equip_day_check = self.ui.co_full_equip_day_check
        co_full_equip_upgrade_check = self.ui.co_full_equip_upgrade_check
        co_computer_check = self.ui.co_computer_check
        co_torch_check = self.ui.co_torch_check
        co_bcd_dive_check = self.ui.co_bcd_dive_check
        co_bcd_day_check = self.ui.co_bcd_day_check
        co_bcd_upgrade_check = self.ui.co_bcd_upgrade_check
        co_reg_dive_check = self.ui.co_reg_dive_check
        co_reg_day_check = self.ui.co_reg_day_check
        co_reg_upgrade_check = self.ui.co_reg_upgrade_check
        co_soft_dive_check = self.ui.co_soft_dive_check
        co_soft_day_check = self.ui.co_soft_day_check
        co_soft_upgrade_check = self.ui.co_soft_upgrade_check
        co_eanx_upgrade_check = self.ui.co_eanx_upgrade_check
        co_15l_upgrade_check = self.ui.co_15l_upgrade_check
        co_18l_upgrade_check = self.ui.co_18l_upgrade_check
        co_3l_air_check = self.ui.co_3l_air_check
        co_3l_100_check = self.ui.co_3l_100_check
        co_6l_50_check = self.ui.co_6l_50_check
        co_6l_100_check = self.ui.co_6l_100_check
        co_12l_50_check = self.ui.co_12l_50_check
        co_12l_100_check = self.ui.co_12l_100_check
        co_twin_air_check = self.ui.co_twin_air_check
        co_twin_eanx_check = self.ui.co_twin_eanx_check
        co_rebreather_check = self.ui.co_rebreather_check
        co_sorb = self.ui.co_sorb_entry.text()
        co_tech_reg_check = self.ui.co_tech_reg_check
        co_back_plate_check = self.ui.co_back_plate_check
        co_wing_check = self.ui.co_wing_check
        co_o2_reg_check = self.ui.co_o2_reg_check
        co_tech_computer_check = self.ui.co_tech_computer_check
        co_tech_torch_check = self.ui.co_tech_torch_check
        co_wreck_reel_check = self.ui.co_wreck_reel_check
        co_smb_check = self.ui.co_smb_check
        co_reel_check = self.ui.co_reel_check
        co_slate_check = self.ui.co_slate_check

        oid1 = "1"
        conn_activities = sqlite3.connect("activities_info.db")
        c_a = conn_activities.cursor()
        c_a.execute("SELECT * FROM extras WHERE oid = " + oid1)
        x = c_a.fetchall()

        for i in x:
            if co_full_equip_dive_check.isChecked():
                co_full_equip_dive_ticked = i[0]
                bal = bal + int(co_full_equip_dive_ticked)
            if co_full_equip_day_check.isChecked():
                co_full_equip_day_ticked = i[1]
                bal = bal + int(co_full_equip_day_ticked)
            if co_full_equip_upgrade_check.isChecked():
                co_full_equip_upgrade_ticked = i[2]
                bal = bal + int(co_full_equip_upgrade_ticked)
            if co_computer_check.isChecked():
                co_computer_ticked = i[3]
                bal = bal + int(co_computer_ticked)
            if co_torch_check.isChecked():
                co_torch_ticked = i[4]
                bal = bal + int(co_torch_ticked)
            if co_bcd_dive_check.isChecked():
                co_bcd_dive_ticked = i[5]
                bal = bal + int(co_bcd_dive_ticked)
            if co_bcd_day_check.isChecked():
                co_bcd_day_ticked = i[6]
                bal = bal + int(co_bcd_day_ticked)
            if co_bcd_upgrade_check.isChecked():
                co_bcd_upgrade_ticked = i[7]
                bal = bal + int(co_bcd_upgrade_ticked)
            if co_reg_dive_check.isChecked():
                co_reg_dive_ticked = i[8]
                bal = bal + int(co_reg_dive_ticked)
            if co_reg_day_check.isChecked():
                co_reg_day_ticked = i[9]
                bal = bal + int(co_reg_day_ticked)
            if co_reg_upgrade_check.isChecked():
                co_reg_upgrade_ticked = i[10]
                bal = bal + int(co_reg_upgrade_ticked)
            if co_soft_dive_check.isChecked():
                co_soft_dive_ticked = i[11]
                bal = bal + int(co_soft_dive_ticked)
            if co_soft_day_check.isChecked():
                co_soft_day_ticked = i[12]
                bal = bal + int(co_soft_day_ticked)
            if co_soft_upgrade_check.isChecked():
                co_soft_upgrade_ticked = i[13]
                bal = bal + int(co_soft_upgrade_ticked)
            if co_eanx_upgrade_check.isChecked():
                co_eanx_upgrade_ticked = i[14]
                bal = bal + int(co_eanx_upgrade_ticked)
            if co_15l_upgrade_check.isChecked():
                co_15l_upgrade_ticked = i[15]
                bal = bal + int(co_15l_upgrade_ticked)
            if co_18l_upgrade_check.isChecked():
                co_18l_upgrade_ticked = i[16]
                bal = bal + int(co_18l_upgrade_ticked)
            if co_3l_air_check.isChecked():
                co_3l_air_ticked = i[17]
                bal = bal + int(co_3l_air_ticked)
            if co_3l_100_check.isChecked():
                co_3l_100_ticked = i[18]
                bal = bal + int(co_3l_100_ticked)
            if co_6l_50_check.isChecked():
                co_6l_50_ticked = i[19]
                bal = bal + int(co_6l_50_ticked)
            if co_6l_100_check.isChecked():
                co_6l_100_ticked = i[20]
                bal = bal + int(co_6l_100_ticked)
            if co_12l_50_check.isChecked():
                co_12l_50_ticked = i[21]
                bal = bal + int(co_12l_50_ticked)
            if co_12l_100_check.isChecked():
                co_12l_100_ticked = i[22]
                bal = bal + int(co_12l_100_ticked)
            if co_twin_air_check.isChecked():
                co_twin_air_ticked = i[23]
                bal = bal + int(co_twin_air_ticked)
            if co_twin_eanx_check.isChecked():
                co_twin_eanx_ticked = i[24]
                bal = bal + int(co_twin_eanx_ticked)
            if co_rebreather_check.isChecked():
                co_rebreather_ticked = i[25]
                bal = bal + int(co_rebreather_ticked)
            if int(co_sorb) != 0:
                co_sorb_ticked = i[26]
                bal = bal + (int(co_sorb_ticked) * int(co_sorb))
            if co_tech_reg_check.isChecked():
                co_tech_reg_ticked = i[28]
                bal = bal + int(co_tech_reg_ticked)
            if co_back_plate_check.isChecked():
                co_back_plate_ticked = i[29]
                bal = bal + int(co_back_plate_ticked)
            if co_wing_check.isChecked():
                co_wing_ticked = i[30]
                bal = bal + int(co_wing_ticked)
            if co_o2_reg_check.isChecked():
                co_o2_reg_ticked = i[31]
                bal = bal + int(co_o2_reg_ticked)
            if co_tech_computer_check.isChecked():
                co_tech_computer_ticked = i[32]
                bal = bal + int(co_tech_computer_ticked)
            if co_tech_torch_check.isChecked():
                co_tech_torch_ticked = i[33]
                bal = bal + int(co_tech_torch_ticked)
            if co_wreck_reel_check.isChecked():
                co_wreck_reel_ticked = i[34]
                bal = bal + int(co_wreck_reel_ticked)
            if co_smb_check.isChecked():
                co_smb_ticked = i[35]
                bal = bal + int(co_smb_ticked)
            if co_reel_check.isChecked():
                co_reel_ticked = i[36]
                bal = bal + int(co_reel_ticked)
            if co_slate_check.isChecked():
                co_slate_ticked = i[37]
                bal = bal + int(co_slate_ticked)

        act = self.ui.co_activity_combo.currentText()

        c_a.execute("SELECT price, course FROM activity WHERE activity =?", ([act]))
        a = c_a.fetchall()
        price = a[0]
        price2 = price[0]
        course = a[0]
        course2 = course[1]

        c_d.execute("SELECT activity FROM dives WHERE diver_id =?", ([oid]))
        x3 = c_d.fetchall()
        list3 = list(map(itemgetter(0), x3))

        count = 0
        for course in list3:
            if course2 == 1:
                if course == act:
                    count += 1

        if count < 2:
            bal = bal + int(price2)

        c_c.execute("UPDATE customer SET total_cost = :total_cost WHERE oid =" + oid, {"total_cost": bal})
        conn_payment = sqlite3.connect("payment.db")
        c_p = conn_payment.cursor()
        c_p.execute("SELECT amount FROM payment WHERE diver_id = ?", (oid))
        x3 = c_p.fetchall()
        x4 = list(map(itemgetter(0), x3))
        total_paid = 0

        for i in x4:
            total_paid = total_paid + i

        bal2 = bal - total_paid

        c_c.execute("UPDATE customer SET balance = ? WHERE oid =?", (bal2, oid))
        conn_payment.commit()
        conn_payment.close()
        conn_activities.commit()
        conn_activities.close()
        conn_customer.commit()
        conn_customer.close()
        conn_dives.commit()
        conn_dives.close()



class staff_list_combobox_table(QComboBox):
    def __init__(self, parent):
        super().__init__(parent)
        self.addItem(" ")
        for i in staff_list:
            self.addItem(i)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    QtGui.QFontDatabase.addApplicationFont('fonts/segoeui.ttf')
    QtGui.QFontDatabase.addApplicationFont('fonts/segoeuib.ttf')
    window = MainWindow()
    sys.exit(app.exec_())
