from tkinter import ttk
from tkinter import *
from tkinter.messagebox import *
from tkinter.scrolledtext import *
from sqlite3 import *
import matplotlib.pyplot as plt
import numpy as np
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import requests
import bs4
from PIL import Image, ImageTk
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from datetime import datetime
from time import strftime


#HOVER_BUTTON
def hover_btn(button):

	def on_entera(e):
		button['background'] = '#ffbf3f' #ffcc66
		button['foreground']= '#429ffd'  #000d33

	def on_leavea(e):
		button['background'] = '#429ffd'
		button['foreground']= '#ffbf3f'

	button.bind("<Enter>", on_entera)
	button.bind("<Leave>", on_leavea)


#----------------------------------- LOG IN SECTION ----------------------------------------------

def login_fn():
	username = login_window_ent_username.get()
	password = login_window_ent_password.get()

	if username == 'admin' and password == 'admin':
		showinfo("LOGIN SUCCESSFUL", "         W E L C O M E        \n                 T O \n              E. M. S.")
		main_window.deiconify()
		login_window.withdraw()
	else:
		showwarning("LOGIN FAILED","        PLEASE TRY AGAIN        ")
	login_window_ent_username.delete(0, END)
	login_window_ent_password.delete(0, END)

#----------------------------------- MAIN WINDOW SECTION --------------------------------------------

def dept_fn():
	dept_main_window.deiconify()
	main_window.withdraw()

def emp_fn():
	#DEPT_ID DATA FOR COMBOBOX
	con = None
	try:
		con = connect('ems.db')
		cursor = con.cursor()
	
		sql = "select dept_id from department"
		cursor.execute(sql)
	
		dept_id_rows = cursor.fetchall()    
		print(dept_id_rows)
	except Exception as e:
		showerror("Failure", e)
	finally:
		if con is not None:
			con.close()
	emp_add_window_combobox_dept_id['values'] = dept_id_rows
	emp_update_window_combobox_dept_id['values'] = dept_id_rows

	emp_main_window.deiconify()
	main_window.withdraw()

def logout_fn():
	login_window.deiconify()
	main_window.withdraw()

#----------------------------------- DEPARTMENT SECTION --------------------------------------------

#DEPARTMENT-ADD BUTTON
def dept_add_fn():
	dept_add_window.deiconify()
	dept_main_window.withdraw()

#DEPARTMENT-VIEW BUTTON
def dept_view_fn():
	dept_view_window.deiconify()
	dept_main_window.withdraw()
	con = None
	try:
		for item in dept_view_window_tree.get_children():
			dept_view_window_tree.delete(item)
		con = connect("ems.db")
		cursor = con.cursor()
		cursor.execute("SELECT * FROM department")
		rows = cursor.fetchall()    
		for row in rows:
			print(row) 
			dept_view_window_tree.insert("", END, values=row)        
	
	except Exception as e:
		showerror("Failure", e)
	finally:
		if con is not None:
			con.close()

#DEPARTMENT-SAVE BUTTON
def dept_save_fn():
	con = None
	try:
		con = connect("ems.db")
		con.execute("PRAGMA foreign_keys = 1")
		cursor = con.cursor()
		dept_id = dept_add_window_ent_dept_id.get()
		dept_name = dept_add_window_ent_dept_name.get()
		dept_location = dept_add_window_ent_dept_location.get()
		
		if((len(dept_id) == 0) and (len(dept_name) == 0) and (len(dept_location) == 0)):
			return showerror("Error","Please Enter All Data Fields!!")
#		elif (((len(rno) == 0) and (len(name) == 0)) or ((len(name) == 0) and (len(marks) == 0)) or  ((len(rno) == 0) and (len(marks) == 0))) :
#			return showerror("Error","Please check Roll No,Name and Marks\n 2 of them left Empty")
#		elif(rno.isalpha() and marks.isalpha()):
#			return showerror("Error","Roll Number and Marks cannot be a string!!")
		#ROLL NO VALIDATION
#		elif(len(rno) == 0):
#			return showerror("Error","Please Enter Roll Number. \nRoll Number cannot be empty!!")
#		elif(rno.isalpha()):
#			return showerror("Error","Roll Number cannot be a string!!")
#		elif(int(rno) <= 0):
#			return showerror("Error","Roll Number cannot be Negative or Zero!!")
		#NAME VALIDATION
#		elif(len(name) == 0):
#			return showerror("Error","Please Enter Name. \nName cannot Empty!!")
#		elif (not name.isalpha()):
#			return showerror("Error","Name cannot contain numbers!!")
#		elif(len(name) < 2):
#			return showerror("Error","Please check Name. \nLength of Name cannot be less than 2!!")
		#MARKS VALIDATION
#		elif(len(marks) == 0):
#			return showerror("Error","Please Enter Marks. \nMarks cannot be Empty!!")
#		elif(marks.isalpha()):
#			return showerror("Error","Marks cannot be a string!!")
#		elif(int(marks) < 0):
#			return showerror("Error","Marks cannot be less than Zero!!")
#		elif(int(marks) > 100):
#			return showerror("Error","Marks cannot be greater than 100!!")
		else:
			dept_id = int(dept_id)
			dept_name = dept_name
			dept_location = dept_location
			sql = "insert into department values('%d', '%s', '%s')"
			cursor.execute(sql % (dept_id, dept_name, dept_location))
			con.commit()
			showinfo("Success", "Record added")
#	except IntegrityError:
#		showerror("Failure","Department already exists!!")
	except Exception as e:
		print (e)
		showerror("Failure", e)
		con.rollback()
	finally:
		if con is not None:
			con.close()
		dept_add_window_ent_dept_id.delete(0, END)
		dept_add_window_ent_dept_name.delete(0, END)
		dept_add_window_ent_dept_location.delete(0, END)

#DEPARTMENT-BACK BUTTON
def dept_back_fn():
	main_window.deiconify()
	dept_main_window.withdraw()

#DEPARTMENT-ADD-BACK BUTTON
def dept_add_back_fn():
	dept_main_window.deiconify()
	dept_add_window.withdraw()

#DEPARTMENT-VIEW-BACK BUTTON
def dept_view_back_fn():
	dept_main_window.deiconify()
	dept_view_window.withdraw()


#----------------------------------- EMPLOYEE SECTION --------------------------------------------

#EMPLOYEE-BACK BUTTON
def emp_back_fn():
	main_window.deiconify()
	emp_main_window.withdraw()

#ADD BUTTON	
def f1():
	emp_add_window.deiconify()
	emp_main_window.withdraw()

#ADD-BACK BUTTON
def f2():
	emp_main_window.deiconify()
	emp_add_window.withdraw()

#UPDATE BUTTON
def f3():
	emp_update_window.deiconify()
	emp_main_window.withdraw()

#DELETE BUTTON
def f4():
	emp_delete_window.deiconify()
	emp_main_window.withdraw()

#CHARTS BUTTON
def f5():
	pass

#VIEW BUTTON
def f6():
	emp_view_window.deiconify()
	emp_main_window.withdraw()
	#emp_view_window_st_data.delete(1.0, END)
	#info= "Emp_ID	Name	Email	Salary	Projects	Dept_ID\n"
	con = None
	try:
		#con = connect('ems.db')
		#cursor = con.cursor()
		#sql = "select * from employee"
		#cursor.execute(sql)
		#data = cursor.fetchall()
		#for d in data:
		#	info = info + " " + str(d[0]) + " " + str(d[1]) + " " + str(d[2]) + " " + str(d[3]) + "	" + str(d[4]) + " " + str(d[5]) + "\n"
		#print(info)
		#emp_view_window_st_data.insert(INSERT, info)
		
		for item in emp_view_window_tree.get_children():
			emp_view_window_tree.delete(item)
		con = connect("ems.db")
		cursor = con.cursor()
		cursor.execute("SELECT * FROM employee")
		rows = cursor.fetchall()    
		for row in rows:
			print(row) 
			emp_view_window_tree.insert("", END, values=row)        
	
	except Exception as e:
		showerror("Failure", e)
	finally:
		if con is not None:
			con.close()

#VIEW-BACK BUTTON
def f7():
	emp_main_window.deiconify()
	emp_view_window.withdraw()

#ADD-SAVE BUTTON
def f8():
	con = None
	try:
		con = connect("ems.db")
		con.execute("PRAGMA foreign_keys = 1")
		cursor = con.cursor()
		emp_id = emp_add_window_ent_emp_id.get()
		emp_name = emp_add_window_ent_emp_name.get()
		emp_salary = emp_add_window_ent_emp_salary.get()
		dept_id = emp_add_window_combobox_dept_id.get()
		no_projects = emp_add_window_ent_no_projects.get()
		emp_email = emp_add_window_ent_emp_email.get()
		
		if((len(emp_id) == 0) and (len(emp_name) == 0) and (len(emp_salary) == 0) and (len(dept_id) == 0) and (len(no_projects) == 0) and (len(emp_email) == 0)):
			return showerror("Error","Please Enter All Data Fields!!")
#		elif (((len(rno) == 0) and (len(name) == 0)) or ((len(name) == 0) and (len(marks) == 0)) or  ((len(rno) == 0) and (len(marks) == 0))) :
#			return showerror("Error","Please check Roll No,Name and Marks\n 2 of them left Empty")
#		elif(rno.isalpha() and marks.isalpha()):
#			return showerror("Error","Roll Number and Marks cannot be a string!!")
		#ROLL NO VALIDATION
#		elif(len(rno) == 0):
#			return showerror("Error","Please Enter Roll Number. \nRoll Number cannot be empty!!")
#		elif(rno.isalpha()):
#			return showerror("Error","Roll Number cannot be a string!!")
#		elif(int(rno) <= 0):
#			return showerror("Error","Roll Number cannot be Negative or Zero!!")
		#NAME VALIDATION
#		elif(len(name) == 0):
#			return showerror("Error","Please Enter Name. \nName cannot Empty!!")
#		elif (not name.isalpha()):
#			return showerror("Error","Name cannot contain numbers!!")
#		elif(len(name) < 2):
#			return showerror("Error","Please check Name. \nLength of Name cannot be less than 2!!")
		#MARKS VALIDATION
#		elif(len(marks) == 0):
#			return showerror("Error","Please Enter Marks. \nMarks cannot be Empty!!")
#		elif(marks.isalpha()):
#			return showerror("Error","Marks cannot be a string!!")
#		elif(int(marks) < 0):
#			return showerror("Error","Marks cannot be less than Zero!!")
#		elif(int(marks) > 100):
#			return showerror("Error","Marks cannot be greater than 100!!")
		else:
			emp_id = int(emp_id)
			emp_name = emp_name
			salary = int(emp_salary)
			dept_id = int(dept_id)
			no_projects = int(no_projects)
			emp_email = emp_email
			sql = "insert into employee values('%d', '%s', '%s', '%d', '%d', '%d')"
			cursor.execute(sql % (emp_id, emp_name, emp_email, salary, no_projects, dept_id))
			con.commit()
			showinfo("Success", "Record added")

			s = smtplib.SMTP('smtp.gmail.com', 587)
			s.starttls()
			s.login("shubhamrawool0711@gmail.com", "Shubham#011")

			email_id = "shubhamsrawool@gmail.com"

			msg = 'Dear Mr/Ms.' +emp_name+ " !\n\nWelcome to Employee Management System\n\n\nYour details has been successfully registered into the company's database\n Please review your details:\n\nEmployee ID: " +str(emp_id)+ "\nEmployee Name: " +emp_name+ "\nEmployee Email: " +emp_email+ "\nSalary: " +str(salary)+ "\nNumber of Projects: " +str(no_projects)+ "\nDepartment ID: " +str(dept_id)+ "\n\n\nThank You!"
			template = msg
			message = MIMEMultipart()
			#template = template.format('Shubham')

			message['From']= 'shubhamrawool0711@gmail.com'
			message['To']= emp_email
			message['Subject']= "Welcome to Employee Management System"

			message.attach(MIMEText(template, 'plain'))

			s.send_message(message)

			s.quit()

#	except IntegrityError:
#		showerror("Failure","Employee already exists!!")
	except Exception as e:
		print (e)
		showerror("Failure", e)
		con.rollback()
	finally:
		if con is not None:
			con.close()
		emp_add_window_ent_emp_id.delete(0, END)
		emp_add_window_ent_emp_name.delete(0, END)
		emp_add_window_ent_emp_salary.delete(0, END)
		emp_add_window_combobox_dept_id.current(0)
		emp_add_window_ent_no_projects.delete(0, END)
		emp_add_window_ent_emp_email.delete(0, END)

#UPDATE-SAVE BUTTON
def f9():
	con = None
	try:
		con = connect("ems.db")
		con.execute("PRAGMA foreign_keys = 1")
		cursor = con.cursor()
		emp_id = emp_update_window_ent_emp_id.get()
		emp_name = emp_update_window_ent_emp_name.get()
		emp_salary = emp_update_window_ent_emp_salary.get()
		dept_id = emp_update_window_combobox_dept_id.get()
		no_projects = emp_update_window_ent_no_projects.get()
		emp_email = emp_update_window_ent_emp_email.get()
		
		if((len(emp_id) == 0) and (len(emp_name) == 0) and (len(emp_salary) == 0) and (len(dept_id) == 0) and (len(no_projects) == 0) and (len(emp_email) == 0)):
			return showerror("Error","Please Enter All Data Fields!!")
#		elif (((len(rno) == 0) and (len(name) == 0)) or ((len(name) == 0) and (len(marks) == 0)) or  ((len(rno) == 0) and (len(marks) == 0))) :
#			return showerror("Error","Please check Roll No,Name and Marks\n 2 of them left Empty")
#		elif(rno.isalpha() and marks.isalpha()):
#			return showerror("Error","Roll Number and Marks cannot be a string!!")
		#ROLL NO VALIDATION
#		elif(len(rno) == 0):
#			return showerror("Error","Please Enter Roll Number. \nRoll Number cannot be empty!!")
#		elif(rno.isalpha()):
#			return showerror("Error","Roll Number cannot be a string!!")
#		elif(int(rno) <= 0):
#			return showerror("Error","Roll Number cannot be Negative or Zero!!")
		#NAME VALIDATION
#		elif(len(name) == 0):
#			return showerror("Error","Please Enter Name. \nName cannot Empty!!")
#		elif (not name.isalpha()):
#			return showerror("Error","Name cannot contain numbers!!")
#		elif(len(name) < 2):
#			return showerror("Error","Please check Name. \nLength of Name cannot be less than 2!!")
		#MARKS VALIDATION
#		elif(len(marks) == 0):
#			return showerror("Error","Please Enter Marks. \nMarks cannot be Empty!!")
#		elif(marks.isalpha()):
#			return showerror("Error","Marks cannot be a string!!")
#		elif(int(marks) < 0):
#			return showerror("Error","Marks cannot be less than Zero!!")
#		elif(int(marks) > 100):
#			return showerror("Error","Marks cannot be greater than 100!!")
		else:
			emp_id = int(emp_id)
			emp_name = emp_name
			salary = int(emp_salary)
			dept_id = int(dept_id)
			no_projects = int(no_projects)
			emp_email = emp_email
			sql = "update employee set emp_name = '%s',emp_email = '%s',salary = '%d',no_projects = '%d',dept_id = '%d' where emp_id = '%d'"
			cursor.execute(sql % (emp_name, emp_email, salary, no_projects, dept_id, emp_id))
						
			if cursor.rowcount > 0:
				showinfo("Success", "Record Updated")
				con.commit()
			else:
				return showerror("Failure", "Employee ID does not exist!!")
				
	except Exception as e:
		showerror("Failure", e)
		con.rollback()
	finally:
		if con is not None:
			con.close()
		emp_update_window_ent_emp_id.delete(0, END)
		emp_update_window_ent_emp_name.delete(0, END)
		emp_update_window_ent_emp_salary.delete(0, END)
		emp_update_window_combobox_dept_id.current(0)
		emp_update_window_ent_no_projects.delete(0, END)
		emp_update_window_ent_emp_email.delete(0, END)

#UPDATE-BACK BUTTON
def f10():
	emp_main_window.deiconify()
	emp_update_window.withdraw()

#DELETE-SAVE BUTTON
def f11():
	con = None
	try:
		con = connect("ems.db")
		con.execute("PRAGMA foreign_keys = 1")
		cursor = con.cursor()
		emp_id = emp_delete_window_ent_emp_id.get()
		
		#ROLL NO VALIDATION
		if(len(emp_id) == 0):
			return showerror("Error","Please Enter Employee ID. \nEmployee ID cannot be empty!!")
		elif(emp_id.isalpha()):
			return showerror("Error","Employee ID cannot be a string!!")
		elif(int(emp_id) <= 0):
			return showerror("Error","Employee ID cannot be Negative or Zero!!")
		
		else:
			emp_id = int(emp_id)
			sql = "delete from employee where emp_id = '%d'"
			cursor.execute(sql % (emp_id))
						
			if cursor.rowcount > 0:
				showinfo("Success", "Record Deleted")
				con.commit()
			else:
				return showerror("Failure", "Employee ID does not exist")
				
	except Exception as e:
		showerror("Failure", e)
		con.rollback()
	finally:
		if con is not None:
			con.close()
		emp_delete_window_ent_emp_id.delete(0, END)
				
#DELETE-BACK BUTTON
def f12():
	emp_main_window.deiconify()
	emp_delete_window.withdraw()

#ANALYTICS BUTTON	
def f13():
	analytics_window.deiconify()
	emp_main_window.withdraw()
	
#ANALYTICS-BACK BUTTON
def f14():
	emp_main_window.deiconify()
	analytics_window.withdraw()

#EMPLOYEE_PIE BUTTON	
def employee_pie_fn():
	#employee_pie_chart_window.deiconify()
	#analytics_window.withdraw()
	con = None
	try:
		list1 = []
		no_emp_list = []
		dept_name_list = []
		con = connect("ems.db")
		con.execute("PRAGMA foreign_keys = 1")
		cursor = con.cursor()
		sql = " SELECT dept_name AS 'Department Name', COUNT(*) AS 'No of Employees' FROM department INNER JOIN employee ON employee.dept_id = department.dept_id GROUP BY department.dept_id, dept_name ORDER BY 'No of Employees'"
		cursor.execute(sql)
		rows = cursor.fetchall()

		for d in rows:
			list1.append(list(d))
		print(list1)
		
		for i in range(len(list1)) :
			dept_name_list.append(list1[i][0])
			no_emp_list.append(list1[i][1])
		print(no_emp_list)
		print(dept_name_list)
		lista = [0.1]
		listb = [0 for i in range(len(dept_name_list)-1)]
		list_explode = lista + listb
		plt.pie(no_emp_list, labels = dept_name_list, autopct = '%0.2f%%', explode = list_explode,shadow = True)

		plt.title("Total Employees")

		plt.savefig("employee_pie.png")
		plt.show()	
		#img1 = ImageTk.PhotoImage(Image.open('employee_pie.png'))
		
		#lab1.configure(image = img1)
		#lab1.image = img1
		#con.commit()
	except DatabaseError as e :
		messagebox.showerror("Galat Kiya",e)
		con.rollback()
	finally:
		if con is not None:
			con.close()

#EMPLOYEE_PIE-BACK BUTTON
#def employee_pie_back_fn():
#	analytics_window.deiconify()
#	employee_pie_chart_window.withdraw()

#SALARY_CHART BUTTON	
def salary_chart_fn():
	#salary_chart_window.deiconify()
	#analytics_window.withdraw()
	con = None
	try:
		list2 = []
		emp_name_list = []
		salary_list = []
		con = connect("ems.db")
		con.execute("PRAGMA foreign_keys = 1")
		cursor = con.cursor()
		sql = "select emp_name, salary from employee"
		cursor.execute(sql)
		rows = cursor.fetchall()

		for d in rows:
			list2.append(list(d))
		print(list2)
		
		for i in range(len(list2)) :
			emp_name_list.append(list2[i][0])
			salary_list.append(list2[i][1])
		print(emp_name_list)
		print(salary_list)

		plt.barh(emp_name_list,salary_list,0.4,color='#FF0F54')		#label = "Employee Salary"
		plt.title("Employee's Salary")
		plt.xlabel("Names")
		plt.ylabel("Salary")
		plt.legend()
		#plt.grid(color = "#A4A4A4", linewidth = "1.4", linestyle = "-.")
		
		plt.savefig("salary_graph.png")
		plt.show()	
		#img2 = ImageTk.PhotoImage(Image.open('salary_graph.png'))
		
		#lab2.configure(image = img2)
		#lab2.image = img2
		#con.commit()
	except DatabaseError as e :
		messagebox.showerror("Galat Kiya",e)
		con.rollback()
	finally:
		if con is not None:
			con.close()

#SALARY_CHART-BACK BUTTON
#def salary_chart_back_fn():
#	analytics_window.deiconify()
#	salary_chart_window.withdraw()

#PERFORMANCE_CHART BUTTON	
def performance_chart_fn():
	#performance_chart_window.deiconify()
	#analytics_window.withdraw()
	con = None
	try:
		list3 = []
		emp_name_list = []
		no_projects_list = []
		con = connect("ems.db")
		con.execute("PRAGMA foreign_keys = 1")
		cursor = con.cursor()
		sql = "select emp_name, no_projects from employee"
		cursor.execute(sql)
		rows = cursor.fetchall()

		for d in rows:
			list3.append(list(d))
		print(list3)
		
		for i in range(len(list3)) :
			emp_name_list.append(list3[i][0])
			no_projects_list.append(list3[i][1])
		print(emp_name_list)
		print(no_projects_list)

		plt.bar(emp_name_list,no_projects_list,0.4)		#label = "Employee Projects"
		plt.title("Employee's Performance")
		plt.xlabel("Names")
		plt.ylabel("Number of Projects")
		plt.legend()
		#plt.grid(color = "#A4A4A4", linewidth = "1.4", linestyle = "-.")
		
		plt.savefig("projects_graph.png")
		plt.show()	
		#img3 = ImageTk.PhotoImage(Image.open('projects_graph.png'))
		
		#lab3.configure(image = img3)
		#lab3.image = img3
		#con.commit()
	except DatabaseError as e :
		messagebox.showerror("Galat Kiya",e)
		con.rollback()
	finally:
		if con is not None:
			con.close()

#PERFORMANCE-BACK BUTTON
#def performance_chart_back_fn():
#	analytics_window.deiconify()
#	performance_chart_window.withdraw()

#Search BUTTON
def emp_search_fn():
	emp_search_window.deiconify()
	emp_main_window.withdraw()

#Search-NAME BUTTON
def search_name_fn():
	#emp_search_window_st_data.delete(1.0, END)
	#info= "Emp_ID	Name	Email	Salary	Projects	Dept_ID\n"
	con = None
	try:
		for item in emp_search_window_tree.get_children():
			emp_search_window_tree.delete(item)

		emp_name = emp_search_window_ent_emp_name.get()
		
		con = connect('ems.db')
		cursor = con.cursor()
		
		if(len(emp_name) == 0):
			return showerror("Error","Please Enter Employee Name. \nEmployee Name cannot be empty!!")

		sql = "select * from employee where emp_name = '%s'"
		cursor.execute(sql % (emp_name))
		#data = cursor.fetchall()
		#for d in data:
		#	info = info + " " + str(d[0]) + " " + str(d[1]) + " " + str(d[2]) + " " + str(d[3]) + "	" + str(d[4]) + " " + str(d[5]) + "\n"
		#print(info)
		#print(data)
		#print(cursor.rowcount)
		
		rows = cursor.fetchall()    
		
		if not rows:
			showerror("Failure", "Employee ID does not exist!")
			
		else:
			#emp_search_window_st_data.insert(INSERT, info)
			for row in rows:
				print(row) 
				emp_search_window_tree.insert("", END, values=row) 

	except Exception as e:
		showerror("Failure", e)
	finally:
		if con is not None:
			con.close()
		emp_search_window_ent_emp_name.delete(0, END)


#Search-BACK BUTTON
def search_back_fn():
	emp_main_window.deiconify()
	emp_search_window.withdraw()
	#emp_search_window_st_data.delete(1.0, END)

#Location with temperature text
try:
	res = requests.get("https://ipinfo.io")
	data = res.json()
	city = data['city']
	
	a1 = "http://api.openweathermap.org/data/2.5/weather?units=metric"
	a2 = "&q=" + city
	a3 = "&appid=c6e315d09197cec231495138183954bd"
	api_address = a1 + a2 + a3
	res1 = requests.get(api_address)
	data = res1.json()
	temp1 = data['main']['temp']
	loc_temp = city,temp1,u"\u2103"
except Exception as e:
		showerror("Issue", e)

#QOTD text
res = requests.get("https://www.brainyquote.com/quotes_of_the_day.html")
soup = bs4.BeautifulSoup(res.text,'html.parser')
quote = soup.find('img',{"class":"p-qotd"})
#print(quote)
qotd = quote['alt']

#Extracting day 
a=datetime.today().strftime('%A')
b=(a.upper())
c=(b[0:2])

def time1():
	a= b + str(" | ")+strftime('%H : %M : %S')  #%H   %M   %S
	l1.config(text=a)
	l1.after(1000,time1)

def time2():
	a= b + str(" | ")+strftime('%H : %M : %S')  #%H   %M   %S
	l2.config(text=a)
	l2.after(1000,time2)

def time3():
	a= b + str(" | ")+strftime('%H : %M : %S')  #%H   %M   %S
	l3.config(text=a)
	l3.after(1000,time3)

#--------------------------------- GUI -------------------------------------

splash = Tk()
splash.after(3000, splash.destroy)
splash.configure(background = "#011f3f")
splash.wm_attributes('-fullscreen', 'true')
msg = Label(splash, text = "\n\n\n\n\nEMPLOYEE MANAGMENT SYSTEM", font = ('Copperplate Gothic Bold', 50, 'italic'), fg = "#429ffd")
msg.configure(background = "#011f3f")
msg.pack()
splash.mainloop()


login_window = Tk()
login_window.title("E. M. S. ")
login_window.geometry("700x650+400+100")
login_window.configure(background = "#011f3f")

l1=Label(login_window, font=('Century Gothic',20), bg='#0e1013', foreground='#d3d3d3')
time1()
login_window_lbl_ems = Label(login_window, text = "\nEMPLOYEE MANAGMENT SYSTEM", font = ('Copperplate Gothic Bold', 25, 'italic'),bg = "#011f3f", fg = "#ffbf3f")
login_window_lbl_username = Label(login_window, text = "Username", font = ('Century Gothic', 20, 'bold'),bg = "#011f3f", fg = "#ffbf3f")
login_window_ent_username = Entry(login_window, bd = 0, font = ('Century Gothic', 20, 'bold'))
login_window_lbl_password = Label(login_window, text = "Password", font = ('Century Gothic', 20, 'bold'),bg = "#011f3f", fg = "#ffbf3f")
login_window_ent_password = Entry(login_window, bd = 0, font = ('Century Gothic', 20, 'bold'), show='*')
login_window_btn_login = Button(login_window, bd = 0, text = "Login", font = ('Century Gothic', 20, 'bold'),bg = "#429ffd", fg = "#ffbf3f", width = 10, command = login_fn)

img_login = ImageTk.PhotoImage(Image.open('log.png'))
lab_login = Label(login_window, image = img_login)

l1.pack(pady=10)
login_window_lbl_ems.pack(pady = 30)
lab_login.pack(pady=10)
login_window_lbl_username.pack()
login_window_ent_username.pack()
login_window_lbl_password.pack()
login_window_ent_password.pack()
login_window_btn_login.pack(pady = 20)

hover_btn(login_window_btn_login)

#login_window_btn_login.place(x=10,y=10)


main_window = Toplevel(login_window)
main_window.title("E. M. S. ")
main_window.geometry("700x650+400+100")
main_window.configure(background = "#011f3f")


l2=Label(main_window, font=('Century Gothic',20), bg='#0e1013', foreground='#d3d3d3')
time2()
main_window_btn_dept = Button(main_window, bd = 0, text = "Department", font = ('Century Gothic', 20, 'bold'),bg = "#429ffd", fg = "#000000", width = 15, height=5,command = dept_fn)
main_window_btn_emp = Button(main_window, bd = 0, text = "Employee", font = ('Century Gothic', 20, 'bold'),bg = "#429ffd", fg = "#000000", width = 15,height=5 ,command = emp_fn)
main_window_lbl_loctemp = Label(main_window, text = loc_temp, font = ('Century Gothic', 20, 'bold'),bg = "#011f3f", fg = "#ffbf3f")
main_window_btn_logout = Button(main_window, bd = 0, text = "Logout", font = ('Century Gothic', 20, 'bold'),bg = "#429ffd", fg = "#000000", width = 10, command = logout_fn)

l2.pack(pady=10)
main_window_btn_dept.pack(pady = 10)
main_window_btn_emp.pack(pady = 10)
main_window_lbl_loctemp.pack(pady = 30)
main_window_btn_logout.pack(pady = 10)

l2.place(x=30,y=40)
main_window_btn_dept.place(x=40,y=250)
main_window_btn_emp.place(x=400,y=250)
main_window_lbl_loctemp.place(x=30,y=100)
main_window_btn_logout.place(x=500,y=540)

hover_btn(main_window_btn_dept)
hover_btn(main_window_btn_emp)
hover_btn(main_window_btn_logout)

main_window.withdraw()


dept_main_window = Toplevel(main_window)
dept_main_window.title("Department")
dept_main_window.geometry("700x650+400+100")
dept_main_window.configure(background = "#011f3f")

l3=Label(dept_main_window, font=('Century Gothic',20), bg='#0e1013', foreground='#d3d3d3')
time3()
dept_main_window_btn_add = Button(dept_main_window, bd = 0, text = "Add", font = ('Century Gothic', 20, 'bold'),bg = "#429ffd", fg = "#000000", width = 15, height=5,command = dept_add_fn)
dept_main_window_btn_view = Button(dept_main_window, bd = 0, text = "View", font = ('Century Gothic', 20, 'bold'),bg = "#429ffd", fg = "#000000", width = 15,height=5, command = dept_view_fn)
dept_main_window_btn_back = Button(dept_main_window, bd = 0, text = "Back", font = ('Century Gothic', 20, 'bold'),bg = "#429ffd", fg = "#000000", width = 10, command = dept_back_fn)

l3.pack(pady=10)
dept_main_window_btn_add.pack(pady = 20)
dept_main_window_btn_view.pack(pady = 20)
dept_main_window_btn_back.pack(pady = 10)

l3.place(x=30,y=40)
dept_main_window_btn_add.place(x=40,y=200)
dept_main_window_btn_view.place(x=400,y=200)
dept_main_window_btn_back.place(x=500,y=500)

hover_btn(dept_main_window_btn_add)
hover_btn(dept_main_window_btn_view)
hover_btn(dept_main_window_btn_back)

dept_main_window.withdraw()


dept_add_window = Toplevel(dept_main_window)
dept_add_window.title("Add Department")
dept_add_window.geometry("700x650+400+100")
dept_add_window.configure(background = "#011f3f")

dept_add_window_lbl_dept_id = Label(dept_add_window, text = "Department ID", font = ('Century Gothic', 20, 'bold'),bg = "#011f3f", fg = "#ffbf3f")
dept_add_window_ent_dept_id = Entry(dept_add_window, bd = 0, font = ('Century Gothic', 20, 'bold'))
dept_add_window_lbl_dept_name = Label(dept_add_window, text = "Department Name", font = ('Century Gothic', 20, 'bold'),bg = "#011f3f", fg = "#ffbf3f")
dept_add_window_ent_dept_name = Entry(dept_add_window, bd = 0, font = ('Century Gothic', 20, 'bold'))
dept_add_window_lbl_dept_location = Label(dept_add_window, text = "Location", font = ('Century Gothic', 20, 'bold'),bg = "#011f3f", fg = "#ffbf3f")
dept_add_window_ent_dept_location = Entry(dept_add_window, bd = 0, font = ('Century Gothic', 20, 'bold'))
dept_add_window_btn_save = Button(dept_add_window, bd = 0, text = "Save", font = ('Century Gothic', 20, 'bold'),bg = "#429ffd", fg = "#000000", command = dept_save_fn)
dept_add_window_btn_back = Button(dept_add_window, bd = 0, text = "Back", font = ('Century Gothic', 20, 'bold'),bg = "#429ffd", fg = "#000000", command = dept_add_back_fn)

dept_add_window_lbl_dept_id.pack(pady = 20)
dept_add_window_ent_dept_id.pack(pady = 10)
dept_add_window_lbl_dept_name.pack(pady = 20)
dept_add_window_ent_dept_name.pack(pady = 10)
dept_add_window_lbl_dept_location.pack(pady = 20)
dept_add_window_ent_dept_location.pack(pady = 10)
dept_add_window_btn_save.pack(pady = 20)
dept_add_window_btn_back.pack(pady = 10)

dept_add_window_btn_save.place(x=200,y=500)
dept_add_window_btn_back.place(x=400,y=500)

hover_btn(dept_add_window_btn_save)
hover_btn(dept_add_window_btn_back)

dept_add_window.withdraw()

dept_view_window = Toplevel(dept_main_window)
dept_view_window.title("View Department")
dept_view_window.geometry("700x650+400+100")
dept_view_window.configure(background = "#011f3f")


dept_view_window_tree = ttk.Treeview(dept_view_window, height = 15, column=("c1", "c2", "c3"), show='headings')

style = ttk.Style()
style.configure("Treeview.Heading", font=('none', 10, 'bold'))

dept_view_window_tree.column("#1", anchor=CENTER)
dept_view_window_tree.heading("#1", text="DEPT_ID")
dept_view_window_tree.column("#2", anchor=CENTER)
dept_view_window_tree.heading("#2", text="NAME")
dept_view_window_tree.column("#3", anchor=CENTER)
dept_view_window_tree.heading("#3", text="LOCATION")

dept_view_window_btn_back = Button(dept_view_window, bd = 0, text = "Back", font = ('Century Gothic', 20, 'bold'),bg = "#429ffd", fg = "#000000", command = dept_view_back_fn)

dept_view_window_tree.pack(pady = 20)
dept_view_window_btn_back.pack(pady = 10)


hover_btn(dept_view_window_btn_back)

dept_view_window.withdraw()

emp_main_window = Toplevel(main_window)
emp_main_window.title("Employee")
emp_main_window.geometry("700x650+400+100")
emp_main_window.configure(background = "#011f3f")

emp_main_window_btn_add = Button(emp_main_window, bd = 0, text = "Add", font = ('Century Gothic', 20, 'bold'),bg = "#429ffd", fg = "#000000", width = 10, command = f1)
emp_main_window_btn_view = Button(emp_main_window, bd = 0, text = "View", font = ('Century Gothic', 20, 'bold'),bg = "#429ffd", fg = "#000000", width = 10, command = f6)
emp_main_window_btn_update = Button(emp_main_window, bd = 0, text = "Update", font = ('Century Gothic', 20, 'bold'),bg = "#429ffd", fg = "#000000", width = 10, command = f3)
emp_main_window_btn_delete = Button(emp_main_window, bd = 0, text = "Delete", font = ('Century Gothic', 20, 'bold'),bg = "#429ffd", fg = "#000000", width = 10, command = f4)
emp_main_window_btn_charts = Button(emp_main_window, bd = 0, text = "Analytics", font = ('Century Gothic', 20, 'bold'),bg = "#429ffd", fg = "#000000", width = 10, command = f13)
emp_main_window_btn_search = Button(emp_main_window, bd = 0, text = "Search", font = ('Century Gothic', 20, 'bold'),bg = "#429ffd", fg = "#000000", width = 10, command = emp_search_fn)
emp_main_window_lbl_qotd = Label(emp_main_window, text = qotd, font = ('Century Gothic', 10, 'italic'),bg = "#011f3f", fg = "#ffbf3f")
emp_main_window_btn_back = Button(emp_main_window, bd = 0, text = "Back", font = ('Century Gothic', 20, 'bold'),bg = "#429ffd", fg = "#000000", width = 10, command = emp_back_fn)

emp_main_window_btn_add.pack(pady = 10)
emp_main_window_btn_view.pack(pady = 10)
emp_main_window_btn_update.pack(pady = 10)
emp_main_window_btn_delete.pack(pady = 10)
emp_main_window_btn_search.pack(pady = 10)
emp_main_window_btn_charts.pack(pady = 10)
emp_main_window_lbl_qotd.pack(pady = 10)
emp_main_window_btn_back.pack(pady = 10)

emp_main_window_btn_add.place(x=100,y=150)
emp_main_window_btn_view.place(x=100,y=250)
emp_main_window_btn_update.place(x=100,y=350)
emp_main_window_btn_delete.place(x=450,y=350)
emp_main_window_btn_search.place(x=450,y=250)
emp_main_window_btn_charts.place(x=450,y=150)
emp_main_window_lbl_qotd.place(x=50,y=450)
emp_main_window_btn_back.place(x=500,y=500)


hover_btn(emp_main_window_btn_add)
hover_btn(emp_main_window_btn_view)
hover_btn(emp_main_window_btn_update)
hover_btn(emp_main_window_btn_delete)
hover_btn(emp_main_window_btn_search)
hover_btn(emp_main_window_btn_charts)
hover_btn(emp_main_window_btn_back)

emp_main_window.withdraw()



emp_add_window = Toplevel(emp_main_window)
emp_add_window.title("Add Employee")
emp_add_window.geometry("700x650+400+100")
emp_add_window.configure(background = "#011f3f")

emp_add_window_lbl_emp_id = Label(emp_add_window, text = "Employee ID", font = ('Century Gothic', 20, 'bold'),bg = "#011f3f", fg = "#ffbf3f")
emp_add_window_ent_emp_id = Entry(emp_add_window, bd = 0, font = ('Century Gothic', 20, 'bold'))
emp_add_window_lbl_emp_name = Label(emp_add_window, text = "Employee Name", font = ('Century Gothic', 20, 'bold'),bg = "#011f3f", fg = "#ffbf3f")
emp_add_window_ent_emp_name = Entry(emp_add_window, bd = 0, font = ('Century Gothic', 20, 'bold'))
emp_add_window_lbl_emp_salary = Label(emp_add_window, text = "Salary", font = ('Century Gothic', 20, 'bold'),bg = "#011f3f", fg = "#ffbf3f")
emp_add_window_ent_emp_salary = Entry(emp_add_window, bd = 0, font = ('Century Gothic', 20, 'bold'))
emp_add_window_lbl_dept_id = Label(emp_add_window, text = "Department ID", font = ('Century Gothic', 20, 'bold'),bg = "#011f3f", fg = "#ffbf3f")
#	emp_add_window_ent_dept_id = Entry(emp_add_window, bd = 0, font = ('Century Gothic', 20, 'bold'))
emp_add_window_combobox_dept_id = ttk.Combobox(emp_add_window, state = 'readonly', font = ('Century Gothic', 19, 'bold'))
emp_add_window_lbl_no_projects = Label(emp_add_window, text = "Number of Projects", font = ('Century Gothic', 20, 'bold'),bg = "#011f3f", fg = "#ffbf3f")
emp_add_window_ent_no_projects = Entry(emp_add_window, bd = 0, font = ('Century Gothic', 20, 'bold'))
emp_add_window_lbl_emp_email = Label(emp_add_window, text = "Email ID", font = ('Century Gothic', 20, 'bold'),bg = "#011f3f", fg = "#ffbf3f")
emp_add_window_ent_emp_email = Entry(emp_add_window, bd = 0, font = ('Century Gothic', 20, 'bold'))
emp_add_window_btn_save = Button(emp_add_window, bd = 0, text = "Save", font = ('Century Gothic', 20, 'bold'),bg = "#429ffd", fg = "#000000", command = f8)
emp_add_window_btn_back = Button(emp_add_window, bd = 0, text = "Back", font = ('Century Gothic', 20, 'bold'),bg = "#429ffd", fg = "#000000", command = f2)

emp_add_window_lbl_emp_id.pack()
emp_add_window_ent_emp_id.pack()
emp_add_window_lbl_emp_name.pack()
emp_add_window_ent_emp_name.pack()
emp_add_window_lbl_emp_salary.pack()
emp_add_window_ent_emp_salary.pack()
emp_add_window_lbl_dept_id.pack()
#	emp_add_window_ent_dept_id.pack()
emp_add_window_combobox_dept_id.pack()
emp_add_window_lbl_no_projects.pack()
emp_add_window_ent_no_projects.pack()
emp_add_window_lbl_emp_email.pack()
emp_add_window_ent_emp_email.pack()
emp_add_window_btn_save.pack(pady = 20)
emp_add_window_btn_back.pack()

#buttons place
emp_add_window_lbl_emp_id.place(x=30,y=100)
emp_add_window_ent_emp_id.place(x=30,y=150)
emp_add_window_lbl_emp_name.place(x=30,y=200)
emp_add_window_ent_emp_name.place(x=30,y=250)
emp_add_window_lbl_emp_salary.place(x=30,y=300)
emp_add_window_ent_emp_salary.place(x=30,y=350)

emp_add_window_lbl_dept_id.place(x=380,y=100)
emp_add_window_combobox_dept_id.place(x=380,y=150)
emp_add_window_lbl_no_projects.place(x=380,y=200)
emp_add_window_ent_no_projects.place(x=380,y=250)
emp_add_window_lbl_emp_email.place(x=380,y=300)
emp_add_window_ent_emp_email.place(x=380,y=350)

emp_add_window_btn_save.place(x=250,y=450)
emp_add_window_btn_back.place(x=400,y=450)

hover_btn(emp_add_window_btn_save)
hover_btn(emp_add_window_btn_back)

emp_add_window.withdraw()

emp_view_window = Toplevel(emp_main_window)
emp_view_window.title("View Employee")
emp_view_window.geometry("700x650+400+100")
emp_view_window.configure(background = "#011f3f")

#	emp_view_window_st_data = ScrolledText(emp_view_window, width = 50, height = 12, font = ('Century Gothic', 16))
emp_view_window_tree = ttk.Treeview(emp_view_window, height = 15, column=("c1", "c2", "c3","c4","c5","c6"), show='headings')

style = ttk.Style()
style.configure("Treeview.Heading", font=('none', 10, 'bold'))
#				Emp_ID	Name	Email	Salary	Projects	Dept_ID
emp_view_window_tree.column("#1", width=60,anchor=CENTER)
emp_view_window_tree.heading("#1", text="EMP_ID")
emp_view_window_tree.column("#2", width=100, anchor=CENTER)
emp_view_window_tree.heading("#2", text="NAME")
emp_view_window_tree.column("#3", width=140, anchor=CENTER)
emp_view_window_tree.heading("#3", text="EMAIL")
emp_view_window_tree.column("#4", width=100, anchor=CENTER)
emp_view_window_tree.heading("#4", text="SALARY")
emp_view_window_tree.column("#5", width=80, anchor=CENTER)
emp_view_window_tree.heading("#5", text="PROJECTS")
emp_view_window_tree.column("#6", width=80, anchor=CENTER)
emp_view_window_tree.heading("#6", text="DEPT_ID")

emp_view_window_btn_back = Button(emp_view_window, bd = 0, text = "Back", font = ('Century Gothic', 20, 'bold'),bg = "#429ffd", fg = "#000000", command = f7)
#	emp_view_window_st_data.pack(pady = 20)

emp_view_window_tree.pack(pady = 20)
emp_view_window_btn_back.pack(pady = 20)

hover_btn(emp_view_window_btn_back)

emp_view_window.withdraw()

emp_update_window = Toplevel(emp_main_window)
emp_update_window.title("Update Employee")
emp_update_window.geometry("700x650+400+100")
emp_update_window.configure(background = "#011f3f")

emp_update_window_lbl_emp_id = Label(emp_update_window, text = "Employee ID", font = ('Century Gothic', 20, 'bold'),bg = "#011f3f", fg = "#ffbf3f")
emp_update_window_ent_emp_id = Entry(emp_update_window, bd = 0, font = ('Century Gothic', 20, 'bold'))
emp_update_window_lbl_emp_name = Label(emp_update_window, text = "Employee Name", font = ('Century Gothic', 20, 'bold'),bg = "#011f3f", fg = "#ffbf3f")
emp_update_window_ent_emp_name = Entry(emp_update_window, bd = 0, font = ('Century Gothic', 20, 'bold'))
emp_update_window_lbl_emp_salary = Label(emp_update_window, text = "Salary", font = ('Century Gothic', 20, 'bold'),bg = "#011f3f", fg = "#ffbf3f")
emp_update_window_ent_emp_salary = Entry(emp_update_window, bd = 0, font = ('Century Gothic', 20, 'bold'))
emp_update_window_lbl_dept_id = Label(emp_update_window, text = "Department ID", font = ('Century Gothic', 20, 'bold'),bg = "#011f3f", fg = "#ffbf3f")
#	emp_update_window_ent_dept_id = Entry(emp_update_window, bd = 0, font = ('Century Gothic', 20, 'bold'))
emp_update_window_combobox_dept_id = ttk.Combobox(emp_update_window, state = 'readonly', font = ('Century Gothic', 19, 'bold'))
emp_update_window_lbl_no_projects = Label(emp_update_window, text = "Number of Projects", font = ('Century Gothic', 20, 'bold'),bg = "#011f3f", fg = "#ffbf3f")
emp_update_window_ent_no_projects = Entry(emp_update_window, bd = 0, font = ('Century Gothic', 20, 'bold'))
emp_update_window_lbl_emp_email = Label(emp_update_window, text = "Email ID", font = ('Century Gothic', 20, 'bold'),bg = "#011f3f", fg = "#ffbf3f")
emp_update_window_ent_emp_email = Entry(emp_update_window, bd = 0, font = ('Century Gothic', 20, 'bold'))
emp_update_window_btn_update = Button(emp_update_window, bd = 0,width=6, text = "Update", font = ('Century Gothic', 20, 'bold'),bg = "#429ffd", fg = "#000000", command = f9)
emp_update_window_btn_back = Button(emp_update_window, bd = 0,width=5, text = "Back", font = ('Century Gothic', 20, 'bold'),bg = "#429ffd", fg = "#000000", command = f10)

emp_update_window_lbl_emp_id.pack()
emp_update_window_ent_emp_id.pack()
emp_update_window_lbl_emp_name.pack()
emp_update_window_ent_emp_name.pack()
emp_update_window_lbl_emp_salary.pack()
emp_update_window_ent_emp_salary.pack()
emp_update_window_lbl_dept_id.pack()
#	emp_update_window_ent_dept_id.pack()
emp_update_window_combobox_dept_id.pack()
emp_update_window_lbl_no_projects.pack()
emp_update_window_ent_no_projects.pack()
emp_update_window_lbl_emp_email.pack()
emp_update_window_ent_emp_email.pack()
emp_update_window_btn_update.pack(pady = 20)
emp_update_window_btn_back.pack()

#button place

emp_update_window_lbl_emp_id.place(x=30,y=100)
emp_update_window_ent_emp_id.place(x=30,y=150)
emp_update_window_lbl_emp_name.place(x=30,y=200)
emp_update_window_ent_emp_name.place(x=30,y=250)
emp_update_window_lbl_emp_salary.place(x=30,y=300)
emp_update_window_ent_emp_salary.place(x=30,y=350)

emp_update_window_lbl_dept_id.place(x=380,y=100)
emp_update_window_combobox_dept_id.place(x=380,y=150)
emp_update_window_lbl_no_projects.place(x=380,y=200)
emp_update_window_ent_no_projects.place(x=380,y=250)
emp_update_window_lbl_emp_email.place(x=380,y=300)
emp_update_window_ent_emp_email.place(x=380,y=350)

emp_update_window_btn_update.place(x=250,y=450)
emp_update_window_btn_back.place(x=400,y=450)

hover_btn(emp_update_window_btn_update)
hover_btn(emp_update_window_btn_back)

emp_update_window.withdraw()

emp_delete_window = Toplevel(emp_main_window)
emp_delete_window.title("Delete Employee")
emp_delete_window.geometry("700x650+400+100")
emp_delete_window.configure(background = "#011f3f")

emp_delete_window_lbl_emp_id = Label(emp_delete_window, text = "Employee ID", font = ('Century Gothic', 20, 'bold'),bg = "#011f3f", fg = "#ffbf3f")
emp_delete_window_ent_emp_id = Entry(emp_delete_window, bd = 0, font = ('Century Gothic', 20, 'bold'))
emp_delete_window_btn_delete = Button(emp_delete_window, bd = 0, text = "Delete", font = ('Century Gothic', 20, 'bold'),bg = "#429ffd", fg = "#000000", command = f11)
emp_delete_window_btn_back = Button(emp_delete_window, bd = 0, text = "Back", font = ('Century Gothic', 20, 'bold'),bg = "#429ffd", fg = "#000000", command = f12)

emp_delete_window_lbl_emp_id.pack(pady = 20)
emp_delete_window_ent_emp_id.pack(pady = 10)
emp_delete_window_btn_delete.pack(pady = 20)
emp_delete_window_btn_back.pack(pady = 10)

hover_btn(emp_delete_window_btn_delete)
hover_btn(emp_delete_window_btn_back)

emp_delete_window.withdraw()


analytics_window = Toplevel(emp_main_window)
analytics_window.title("Employee Analytics")
analytics_window.geometry("700x650+400+100")
analytics_window.configure(background = "#011f3f")

analytics_window_lbl_charts = Label(analytics_window, text = "Charts", font = ('Century Gothic', 20, 'bold'),bg = "#011f3f", fg = "#ffbf3f")
analytics_window_btn_employee_pie = Button(analytics_window, width= 15, bd = 0, text = "Total Employees", font = ('Century Gothic', 20, 'bold'),bg = "#429ffd", fg = "#000000", command = employee_pie_fn)
analytics_window_btn_salary_chart = Button(analytics_window, width= 15, bd = 0, text = "Salary", font = ('Century Gothic', 20, 'bold'),bg = "#429ffd", fg = "#000000", command = salary_chart_fn)
analytics_window_btn_performance_chart = Button(analytics_window, width= 15, bd = 0, text = "Performance", font = ('Century Gothic', 20, 'bold'),bg = "#429ffd", fg = "#000000", command = performance_chart_fn)		
analytics_window_btn_back = Button(analytics_window, width = 10, bd = 0, text = "Back", font = ('Century Gothic', 20, 'bold'),bg = "#429ffd", fg = "#000000", command = f14)

analytics_window_lbl_charts.pack(pady = 10)
analytics_window_btn_employee_pie.pack(pady = 30)
analytics_window_btn_salary_chart.pack(pady = 30)
analytics_window_btn_performance_chart.pack(pady = 30)
analytics_window_btn_back.pack(pady = 10)

analytics_window_btn_back.place(x=500,y=500)

hover_btn(analytics_window_btn_employee_pie)
hover_btn(analytics_window_btn_salary_chart)
hover_btn(analytics_window_btn_performance_chart)
hover_btn(analytics_window_btn_back)

analytics_window.withdraw()


#employee_pie_chart_window = Toplevel(analytics_window)
#employee_pie_chart_window.title("Employee Pie Chart")
#employee_pie_chart_window.geometry("700x650+400+100")
#employee_pie_chart_window.configure(background = "#011f3f")

#img1 = ImageTk.PhotoImage(Image.open('projects_graph.png'))
#lab1 = Label(employee_pie_chart_window, image = img1)
#lab1.pack(pady=10)
		
#employee_pie_chart_window_btn_back = Button(employee_pie_chart_window, bd = 0, text = "Back", font = ('Century Gothic', 20, 'bold'),bg = "#429ffd", fg = "#000000", command = employee_pie_back_fn)

#employee_pie_chart_window_btn_back.pack(pady = 10)
#employee_pie_chart_window.withdraw()


#salary_chart_window = Toplevel(analytics_window)
#salary_chart_window.title("Salary Graph")
#salary_chart_window.geometry("700x650+400+100")
#salary_chart_window.configure(background = "#011f3f")

#img2 = ImageTk.PhotoImage(Image.open('salary_graph.png'))
#lab2 = Label(salary_chart_window, image = img2)
#lab2.pack(pady=10)
		
#salary_chart_window_btn_back = Button(salary_chart_window, bd = 0, text = "Back", font = ('Century Gothic', 20, 'bold'),bg = "#429ffd", fg = "#000000", command = salary_chart_back_fn)

#salary_chart_window_btn_back.pack(pady = 10)
#salary_chart_window.withdraw()

#performance_chart_window = Toplevel(analytics_window)
#performance_chart_window.title("Performance Graph")
#performance_chart_window.geometry("700x650+400+100")
#performance_chart_window.configure(background = "#011f3f")

#img3 = ImageTk.PhotoImage(Image.open('projects_graph.png'))
#lab3 = Label(performance_chart_window, image = img3)
#lab3.pack(pady=10)
		
#performance_chart_window_btn_back = Button(performance_chart_window, bd = 0, text = "Back", font = ('Century Gothic', 20, 'bold'),bg = "#429ffd", fg = "#000000", command = performance_chart_back_fn)

#performance_chart_window_btn_back.pack(pady = 10)
#performance_chart_window.withdraw()

emp_search_window = Toplevel(emp_main_window)
emp_search_window.title("Search Employee")
emp_search_window.geometry("700x650+400+100")
emp_search_window.configure(background = "#011f3f")

#	emp_search_window_st_data = ScrolledText(emp_search_window, width = 50, height = 5, font = ('Century Gothic', 16))

emp_search_window_tree = ttk.Treeview(emp_search_window, height = 10, column=("c1", "c2", "c3","c4","c5","c6"), show='headings')

style = ttk.Style()
style.configure("Treeview.Heading", font=('none', 10, 'bold'))

emp_search_window_tree.column("#1", width=60,anchor=CENTER)
emp_search_window_tree.heading("#1", text="EMP_ID")
emp_search_window_tree.column("#2", width=100, anchor=CENTER)
emp_search_window_tree.heading("#2", text="NAME")
emp_search_window_tree.column("#3", width=140, anchor=CENTER)
emp_search_window_tree.heading("#3", text="EMAIL")
emp_search_window_tree.column("#4", width=100, anchor=CENTER)
emp_search_window_tree.heading("#4", text="SALARY")
emp_search_window_tree.column("#5", width=80, anchor=CENTER)
emp_search_window_tree.heading("#5", text="PROJECTS")
emp_search_window_tree.column("#6", width=80, anchor=CENTER)
emp_search_window_tree.heading("#6", text="DEPT_ID")

emp_search_window_lbl_emp_name = Label(emp_search_window, text = "Employee Name", font = ('Century Gothic', 20, 'bold'),bg = "#011f3f", fg = "#ffbf3f")
emp_search_window_ent_emp_name = Entry(emp_search_window, bd = 0, font = ('Century Gothic', 20, 'bold'))
emp_search_window_btn_search_name = Button(emp_search_window, bd = 0, text = "Search", font = ('Century Gothic', 20, 'bold'),bg = "#429ffd", fg = "#000000", command = search_name_fn)
emp_search_window_btn_back = Button(emp_search_window, bd = 0, text = "Back", font = ('Century Gothic', 20, 'bold'),bg = "#429ffd", fg = "#000000", command = search_back_fn)

#	emp_search_window_st_data.pack(pady = 20)

emp_search_window_tree.pack(pady = 20)
emp_search_window_lbl_emp_name.pack(pady = 20)
emp_search_window_ent_emp_name.pack(pady = 10)
emp_search_window_btn_search_name.pack(pady = 20)
emp_search_window_btn_back.pack(pady = 20)

hover_btn(emp_search_window_btn_search_name)
hover_btn(emp_search_window_btn_back)

emp_search_window.withdraw()




def quit():
	if askyesno("Quit", "Tussi jaa rahe ho? "):
		login_window.destroy()

login_window.protocol("WM_DELETE_WINDOW", quit)
login_window.mainloop()

