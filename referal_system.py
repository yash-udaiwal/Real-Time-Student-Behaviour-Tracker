import tkinter as tk
from tkinter import font  as tkfont
from tkinter import *
from tkinter import messagebox
from PIL import ImageTk
from tkinter import ttk
import cx_Oracle
import sys
u_p=[]
s_p=[]
def main():
    class SampleApp(tk.Tk):

        def __init__(self, *args, **kwargs):
            tk.Tk.__init__(self, *args, **kwargs)

            self.title_font = tkfont.Font(family='Helvetica', size=18, weight="bold", slant="italic")

            # the container is where we'll stack a bunch of frames
            # on top of each other, then the one we want visible
            # will be raised above the others
            container = tk.Frame(self)
            container.pack(side="top", fill="both", expand=True)
            container.grid_rowconfigure(0, weight=1)
            container.grid_columnconfigure(0, weight=1)

            self.frames = {}
            for F in (LoginPage,StartPage, Admin_LoginPage, Admin, Student_Details, Admin_Report, StuPar_Report, Uniform, Teacher_Details, Create_User, Teacher_LoginPage, StuPar_LoginPage, Attendence, Options, Attentive, Behaviour, Ethics, English, Curriculam):
                page_name = F.__name__
                frame = F(parent=container, controller=self)
                self.frames[page_name] = frame

                # put all of the pages in the same location;
                # the one on the top of the stacking order
                # will be the one that is visible.
                frame.grid(row=0, column=0, sticky="nsew")

            self.show_frame("LoginPage")

        def show_frame(self, page_name):
            '''Show a frame for the given page name'''
            frame = self.frames[page_name]
            frame.tkraise()
        


 ##############################################################################################################
            
    class LoginPage(tk.Frame):

        def __init__(self, parent, controller):
            tk.Frame.__init__(self, parent)
            self.controller = controller
            
            #self.title("login system")

            ##############ALL IMAGES########
            self.bg_icon=ImageTk.PhotoImage(file="bckg.jpg")
            self.user_icon=PhotoImage(file="user.png")
            self.pass_icon=PhotoImage(file="pass.png")
            self.logo_icon=PhotoImage(file="logo.png")
            ######### variables############
            self.uname=StringVar()
            self.passw=StringVar()

            bg_lbl=tk.Label(self,image=self.bg_icon).pack()
            title=tk.Label(self,text="Login System",font=("times new roman",40,"bold"),bg="light coral",fg="white",bd=10,relief=GROOVE)
            title.place(x=0,y=0,relwidth=1)

            Login_Frame=tk.Frame(self,bg="white")
            Login_Frame.place(x=750,y=150)

            logolbl=tk.Label(Login_Frame,image=self.logo_icon,bd=0).grid(row=0,columnspan=2,pady=20)

            lbluser=tk.Label(Login_Frame,text="Username",image=self.user_icon,compound=LEFT,font=("times new roman",20,"bold"),bg="white").grid(rows=1,column=0,padx=20,pady=10)
            txtuser=tk.Entry(Login_Frame,bd=5,textvariable=self.uname,relief=GROOVE,font=("",15)).grid(row=1,column=1,padx=20)

            lblpass=tk.Label(Login_Frame,text="Password",image=self.pass_icon,compound=LEFT,font=("times new roman",20,"bold"),bg="white").grid(rows=2,column=0,padx=20,pady=10)
            txtpass=tk.Entry(Login_Frame,bd=5,textvariable=self.passw,relief=GROOVE,font=("",15),show="*").grid(row=2,column=1,padx=20)

            btn_log=tk.Button(Login_Frame,text="Login",width=10,command=self.login,font=("times new roman",14,"bold"),bg="yellow",fg="red").grid(row=3,column=1,pady=10)
            btn_log=tk.Button(Login_Frame,text="Quit",width=10,command=self.logout,font=("times new roman",14,"bold"),bg="yellow",fg="red").grid(row=4,column=1,pady=10)





        def login(self):
            if self.uname.get()=="" or self.passw.get()=="":
                messagebox.showerror("Error","All fields are required!!!")
            elif self.uname.get()=="root" and self.passw.get()=="1234":
                 messagebox.showinfo("Successfull",f"welcome {self.uname.get()}")
                 self.passw.set('')
                 self.uname.set('')
                 self.controller.show_frame("StartPage")
                 
            else:
                messagebox.showerror("Error","Invalid Username or Password!!!")

        def logout(self):
            app.destroy()
    


########################################### Start Page #############################################


    class StartPage(tk.Frame):

        def __init__(self, parent, controller):
            tk.Frame.__init__(self, parent)
            self.controller = controller
            
            self.bg_icon=ImageTk.PhotoImage(file="insrt.jpg")
            bg_lbl=tk.Label(self,image=self.bg_icon).pack()
            title=tk.Label(self,text="MAIN MENU",font=("times new roman",40,"bold"),bg="black",fg="red",bd=10,relief=GROOVE)
            title.place(x=0,y=0,relwidth=1)

            Menu_Frame=tk.Frame(self,bg="gold")
            Menu_Frame.place(x=900,y=100)
            
            button = tk.Button(Menu_Frame, text="Go to Login Page",width=25,command=lambda: controller.show_frame("LoginPage"),font=("times new roman",14,"bold"),bg="black",fg="red").grid(row=0,column=0,pady=10)
            button1 = tk.Button(Menu_Frame, text="ADMIN LOGIN",width=25,command=lambda: controller.show_frame("Admin_LoginPage"),font=("times new roman",14,"bold"),bg="black",fg="red").grid(row=1,column=0,pady=10)
            button2 = tk.Button(Menu_Frame, text="TEACHER LOGIN",width=25, command=lambda: controller.show_frame("Teacher_LoginPage"), font=("times new roman",14,"bold"),bg="black",fg="red").grid(row=2,column=0,pady=10)
            button3 = tk.Button(Menu_Frame, text="STUDENT/PARENT LOGIN",width=25, command=lambda: controller.show_frame("StuPar_LoginPage"), font=("times new roman",14,"bold"),bg="black",fg="red").grid(row=3,column=0,pady=10)




#################################### Admin Login Page ##############################################################



    class Admin_LoginPage(tk.Frame):

        def __init__(self, parent, controller):
            tk.Frame.__init__(self, parent)
            self.controller = controller
            
            ##############ALL IMAGES########
            self.bg_icon=ImageTk.PhotoImage(file="43629.jpg")
            self.user_icon=PhotoImage(file="user.png")
            self.pass_icon=PhotoImage(file="pass.png")
            self.logo_icon=PhotoImage(file="logo.png")
            ######### variables############

            self.uname=StringVar()
            self.passw=StringVar()

            bg_lbl=tk.Label(self,image=self.bg_icon).pack()
            title=tk.Label(self,text="Welcome To Admin System",font=("times new roman",40,"bold"),bg="yellow",fg="red",bd=10,relief=GROOVE)
            title.place(x=0,y=0,relwidth=1)

            Login_Frame=tk.Frame(self,bg="white")
            Login_Frame.place(x=30,y=120)

            logolbl=tk.Label(Login_Frame,image=self.logo_icon,bd=0).grid(row=0,columnspan=2,pady=20)

            lbluser=tk.Label(Login_Frame,text="Username",image=self.user_icon,compound=LEFT,font=("times new roman",20,"bold"),bg="white").grid(rows=1,column=0,padx=20,pady=10)
            txtuser=tk.Entry(Login_Frame,bd=5,textvariable=self.uname,relief=GROOVE,font=("",15)).grid(row=1,column=1,padx=20)

            lblpass=tk.Label(Login_Frame,text="Password",image=self.pass_icon,compound=LEFT,font=("times new roman",20,"bold"),bg="white").grid(rows=2,column=0,padx=20,pady=10)
            txtpass=tk.Entry(Login_Frame,bd=5,textvariable=self.passw,relief=GROOVE,font=("",15),show="*").grid(row=2,column=1,padx=20)
            btn_log=tk.Button(Login_Frame,text="Login",width=10,command=self.login,font=("times new roman",14,"bold"),bg="yellow",fg="red").grid(row=3,column=1,pady=10)
            btn_log=tk.Button(Login_Frame,text="Back",width=10,command=lambda: controller.show_frame("StartPage"),font=("times new roman",14,"bold"),bg="yellow",fg="red").grid(row=4,column=1,pady=10)


        def login(self):
            if self.uname.get()=="" or self.passw.get()=="":
                messagebox.showerror("Error","All fields are required!!!")
            elif self.uname.get()=="admin" and self.passw.get()=="1234":
                 messagebox.showinfo("Successfull",f"welcome {self.uname.get()}")
                 self.passw.set('')
                 self.uname.set('')
                 self.controller.show_frame("Admin")
                 
            else:
                messagebox.showerror("Error","Invalid Username or Password!!!")
                


########################################## Admin Page  ############################################################


    class Admin(tk.Frame):
        def __init__(self, parent, controller):
            tk.Frame.__init__(self, parent)
            self.controller = controller

            
            self.bg_icon=ImageTk.PhotoImage(file="43629.jpg")
            bg_lbl=tk.Label(self,image=self.bg_icon).pack()
            title=tk.Label(self,text="ADMIN MENU",font=("times new roman",40,"bold"),bg="yellow",fg="red",bd=10,relief=GROOVE)
            title.place(x=0,y=0,relwidth=1)

            Admin_Frame=tk.Frame(self,bg="black")
            Admin_Frame.place(x=0,y=83,width=1366,height=60)

            button = tk.Button(Admin_Frame, text="Student",width=10,command=lambda: controller.show_frame("Student_Details"),font=("times new roman",14,"bold"),bg="white",fg="red").grid(row=0,column=0,pady=10)
            button1 = tk.Button(Admin_Frame, text="Teacher",width=10,command=lambda: controller.show_frame("Teacher_Details"),font=("times new roman",14,"bold"),bg="white",fg="red").grid(row=0,column=1,pady=10)
            button3 = tk.Button(Admin_Frame, text="Create User",width=10,command=lambda: controller.show_frame("Create_User"),font=("times new roman",14,"bold"),bg="white",fg="red").grid(row=0,column=3,pady=10)
            button5 = tk.Button(Admin_Frame, text="Report",width=12,command=lambda: controller.show_frame("Admin_Report"),font=("times new roman",14,"bold"),bg="white",fg="red").grid(row=0,column=5,pady=10)
            button6 = tk.Button(Admin_Frame, text="Log Out",width=12,command=lambda: controller.show_frame("LoginPage"),font=("times new roman",14,"bold"),bg="white",fg="red").grid(row=0,column=6,pady=10)



#################################### Student Class ################################################



    class Student_Details(tk.Frame):
        def __init__(self, parent, controller):
            tk.Frame.__init__(self, parent)
            self.controller = controller

            self.bg_icon=ImageTk.PhotoImage(file="43629.jpg")
            bg_lbl=tk.Label(self,image=self.bg_icon).pack()
            title=tk.Label(self,text="Student Details",font=("times new roman",40,"bold"),bg="yellow",fg="red",bd=10,relief=GROOVE)
            title.place(x=0,y=0,relwidth=1)

            Admin_Frame=tk.Frame(self,bg="black")
            Admin_Frame.place(x=0,y=83,width=1366,height=60)

            button = tk.Button(Admin_Frame, text="Student",width=10,command=lambda: controller.show_frame("Student_Details"),font=("times new roman",14,"bold"),bg="white",fg="red").grid(row=0,column=0,pady=10)
            button1 = tk.Button(Admin_Frame, text="Teacher",width=10,command=lambda: controller.show_frame("Teacher_Details"),font=("times new roman",14,"bold"),bg="white",fg="red").grid(row=0,column=1,pady=10)
            button3 = tk.Button(Admin_Frame, text="Create User",width=10,command=lambda: controller.show_frame("Create_User"),font=("times new roman",14,"bold"),bg="white",fg="red").grid(row=0,column=3,pady=10)
            button5 = tk.Button(Admin_Frame, text="Report",width=12,command=lambda: controller.show_frame("Admin_Report"),font=("times new roman",14,"bold"),bg="white",fg="red").grid(row=0,column=5,pady=10)
            button6 = tk.Button(Admin_Frame, text="Log Out",width=12,command=lambda: controller.show_frame("LoginPage"),font=("times new roman",14,"bold"),bg="white",fg="red").grid(row=0,column=6,pady=10)


            self.Roll_No_var=tk.StringVar()
            self.name_var=tk.StringVar()
            self.class_var=tk.StringVar()
            self.gender_var=tk.StringVar()
            self.contact_var=tk.StringVar()
            self.dob_var=tk.StringVar()
            self.guardian_var=tk.StringVar()
            self.guard_cont_var=tk.StringVar()
            self.search_by=tk.StringVar()
            self.search_txt=tk.StringVar()

            Student_Frame=Frame(self,bd=4,relief=GROOVE,bg="white")
            Student_Frame.place(x=190,y=145,width=1000,height=258)
            
            
            lbl_roll=Label(Student_Frame,text="Roll No.",bg="crimson",fg="white",font=("times new roman",20,"bold"))
            lbl_roll.grid(row=1,column=0,pady=7,padx=20,sticky="w")

            txt_Roll=Entry(Student_Frame,textvariable=self.Roll_No_var,font=("times new roman",15,"bold"),bd=5,relief=GROOVE)
            txt_Roll.grid(row=1,column=1,pady=7,padx=20,sticky="w")

            lbl_name=Label(Student_Frame,text="Name",bg="crimson",fg="white",font=("times new roman",20,"bold"))
            lbl_name.grid(row=1,column=4,pady=7,padx=20,sticky="w")

            txt_name=Entry(Student_Frame,textvariable=self.name_var,font=("times new roman",15,"bold"),bd=5,relief=GROOVE)
            txt_name.grid(row=1,column=5,pady=7,padx=20,sticky="w")

            lbl_course=Label(Student_Frame,text="Class",bg="crimson",fg="white",font=("times new roman",20,"bold"))
            lbl_course.grid(row=2,column=0,pady=7,padx=20,sticky="w")

            txt_course=Entry(Student_Frame,textvariable=self.class_var,font=("times new roman",15,"bold"),bd=5,relief=GROOVE)
            txt_course.grid(row=2,column=1,pady=7,padx=20,sticky="w")

            lbl_Gender=Label(Student_Frame,text="Gender",bg="crimson",fg="white",font=("times new roman",20,"bold"))
            lbl_Gender.grid(row=2,column=4,pady=7,padx=20,sticky="w")

            combo_gender=ttk.Combobox(Student_Frame,textvariable=self.gender_var,font=("times new roman",13,"bold"),state='readonly')
            combo_gender['values']=("Male","Female","Other")
            combo_gender.grid(row=2,column=5,pady=7,padx=20)

            lbl_Dob=Label(Student_Frame,text="D.O.B",bg="crimson",fg="white",font=("times new roman",20,"bold"))
            lbl_Dob.grid(row=3,column=0,pady=7,padx=20,sticky="w")

            txt_Dob=Entry(Student_Frame,textvariable=self.dob_var,font=("times new roman",15,"bold"),bd=5,relief=GROOVE)
            txt_Dob.grid(row=3,column=1,pady=7,padx=20,sticky="w")

            lbl_Contact=Label(Student_Frame,text="Contact",bg="crimson",fg="white",font=("times new roman",20,"bold"))
            lbl_Contact.grid(row=3,column=4,pady=7,padx=20,sticky="w")

            txt_Contact=Entry(Student_Frame,textvariable=self.contact_var,font=("times new roman",15,"bold"),bd=5,relief=GROOVE)
            txt_Contact.grid(row=3,column=5,pady=7,padx=20,sticky="w")

            lbl_Guardian=Label(Student_Frame,text="Guardian",bg="crimson",fg="white",font=("times new roman",20,"bold"))
            lbl_Guardian.grid(row=4,column=0,pady=7,padx=20,sticky="w")

            txt_Guardian=Entry(Student_Frame,textvariable=self.guardian_var,font=("times new roman",15,"bold"),bd=5,relief=GROOVE)
            txt_Guardian.grid(row=4,column=1,pady=7,padx=20,sticky="w")

            lbl_Guard_con=Label(Student_Frame,text="Guardian Con.",bg="crimson",fg="white",font=("times new roman",20,"bold"))
            lbl_Guard_con.grid(row=4,column=4,pady=7,padx=20,sticky="w")

            txt_Guard_con=Entry(Student_Frame,textvariable=self.guard_cont_var,font=("times new roman",15,"bold"),bd=5,relief=GROOVE)
            txt_Guard_con.grid(row=4,column=5,pady=7,padx=20,sticky="w")

            #######################button frame##########################
            
            Addbtn=tk.Button(Student_Frame, text="Add",width=10,command=self.add_students,font=("times ne roman",10,"bold"),bg="crimson",fg="white").grid(row=1,column=6,pady=10)
            updatebtn=tk.Button(Student_Frame, text="Update",width=10,command=self.update_data,font=("times ne roman",10,"bold"),bg="crimson",fg="white").grid(row=2,column=6,pady=10)
            deletebtn=tk.Button(Student_Frame, text="Delete",width=10,command=self.delete_data,font=("times ne roman",10,"bold"),bg="crimson",fg="white").grid(row=3,column=6,pady=10)
            Clearbtn =tk.Button(Student_Frame, text="Clear",width=10,command=self.clear,font=("times ne roman",10,"bold"),bg="crimson",fg="white").grid(row=4,column=6,pady=10)

            ##########################detail frame#######################

            Detail_Frame=Frame(self,bd=4,relief=GROOVE,bg="white")
            Detail_Frame.place(x=190,y=405,width=1000,height=295)

            lbl_Search=Label(Detail_Frame,text="Search BY",bg="crimson",fg="white",font=("times new roman",20,"bold"))
            lbl_Search.grid(row=0,column=0,pady=10,padx=20,sticky="w")

            combo_Search=ttk.Combobox(Detail_Frame,textvariable=self.search_by,width=10,font=("times new roman",13,"bold"),state='readonly')
            combo_Search['values']=("Roll_No","Name","Contact")
            combo_Search.grid(row=0,column=1,pady=10,padx=20)

            txt_Search=Entry(Detail_Frame,textvariable=self.search_txt,width=20,font=("times new roman",10,"bold"),bd=5,relief=GROOVE)
            txt_Search.grid(row=0,column=2,pady=10,padx=20,sticky="w")

            Searchbtn=Button(Detail_Frame,text="Search",width=10,command=self.search_data,pady=5).grid(row=0,column=3,padx=10,pady=10)
            Showallbtn=Button(Detail_Frame,text="Show All",width=10,command=self.fetch_data,pady=5).grid(row=0,column=4,padx=10,pady=10)

            #################Table Frame#############################

            Table_Frame=Frame(Detail_Frame,bd=4,relief=RIDGE,bg="crimson")
            Table_Frame.place(x=10,y=60,width=970,height=225)

            scroll_x=Scrollbar(Table_Frame,orient=HORIZONTAL)
            scroll_y=Scrollbar(Table_Frame,orient=VERTICAL)

            self.Student_Table=ttk.Treeview(Table_Frame,columns=("Roll No","Name","Class","Gender","Contact","D.O.B","Guardian","Guardian Cont."),xscrollcommand=scroll_x.set,yscrollcommand=scroll_y.set)
            scroll_x.pack(side=BOTTOM,fill=X)
            scroll_y.pack(side=RIGHT,fill=Y)
            scroll_x.config(command=self.Student_Table.xview)
            scroll_y.config(command=self.Student_Table.yview)
            
            self.Student_Table.heading("Roll No",text="Roll No")
            self.Student_Table.heading("Name",text="Name")
            self.Student_Table.heading("Class",text="Class")
            self.Student_Table.heading("Gender",text="Gender")
            self.Student_Table.heading("Contact",text="Contact")
            self.Student_Table.heading("D.O.B",text="D.O.B")
            self.Student_Table.heading("Guardian",text="Guardian")
            self.Student_Table.heading("Guardian Cont.",text="Guardian Cont.")
       
            self.Student_Table['show']='headings'

            self.Student_Table.column("Roll No",width=100)
            self.Student_Table.column("Name",width=100)
            self.Student_Table.column("Class",width=100)
            self.Student_Table.column("Gender",width=100)
            self.Student_Table.column("Contact",width=100)
            self.Student_Table.column("D.O.B",width=100)
            self.Student_Table.column("Guardian",width=100)
            self.Student_Table.column("Guardian Cont.",width=150)

            self.Student_Table.pack(fill=BOTH,expand=1)
            self.Student_Table.bind("<ButtonRelease-1>",self.get_cursor)
            self.fetch_data()

        def add_students(self):
            try:
                if self.Roll_No_var.get()=="" or\
                   self.name_var.get()=="" or\
                   self.class_var.get()=="" or\
                   self.gender_var.get()=="" or\
                   self.contact_var.get()=="" or\
                   self.dob_var.get()=="" or\
                   self.guardian_var.get()=="" or\
                   self.guard_cont_var.get()=="":
                    messagebox.showerror("Error","All fields are required!!!")
                    self.clear()
                else:
                    con=cx_Oracle.connect('system/yash@localhost:1521/system')
                    cur=con.cursor()
                    if len(self.contact_var.get())!=10:
                        messagebox.showerror("Error","Enter a valid 10 digit contact number")
                        self.contact_var.set('')
                    else:
                        con=cx_Oracle.connect('system/yash@localhost:1521/system')
                        cur=con.cursor()
                        sql="insert into stud(roll_no,name,class,gender,contact,dob,guardian,guardian_cont) values (:1,:2,:3,:4,:5,:6,:7,:8)"
                        cur.execute( sql ,(
                                            self.Roll_No_var.get(),
                                            self.name_var.get(),
                                            self.class_var.get(),
                                            self.gender_var.get(),
                                            self.contact_var.get(),
                                            self.dob_var.get(),
                                            self.guardian_var.get(),
                                            self.guard_cont_var.get()
                                            ))
                        con.commit()
                        con.close()
                        self.clear()
                        self.fetch_data()
                        messagebox.showinfo("Success","Record is inserted successfully")
                    
            except cx_Oracle.IntegrityError:
                messagebox.showerror("Error"," Roll No. is a Unique Variable\n please give a different unique value to it")
                self.Roll_No_var.set('')
            except cx_Oracle.DatabaseError:
                messagebox.showerror("Error",str(sys.exc_info()[0])+"\n"+str(sys.exc_info()[1]))
                self.clear()
            
        def fetch_data(self):
            con=cx_Oracle.connect('system/yash@localhost:1521/system')
            cur=con.cursor()

            cur.execute("select * from stud order by roll_no")
            rows=cur.fetchall()
            self.Student_Table.delete(*self.Student_Table.get_children())
            if len(rows)!=0:
                for row in rows:
                    self.Student_Table.insert('',END,values=row)
                con.commit()
            con.close()

        def clear(self):
            self.Roll_No_var.set('')
            self.name_var.set('')
            self.class_var.set('')
            self.gender_var.set('')
            self.contact_var.set('')
            self.dob_var.set('')
            self.guardian_var.set('')
            self.guard_cont_var.set('')

        def get_cursor(self,ev):
            cursor_row=self.Student_Table.focus()
            contents=self.Student_Table.item(cursor_row)
            row=(contents['values'])
            self.Roll_No_var.set(row[0])
            self.name_var.set(row[1])
            self.class_var.set(row[2])
            self.gender_var.set(row[3])
            self.contact_var.set(row[4])
            self.dob_var.set(row[5])
            self.guardian_var.set(row[6])
            self.guard_cont_var.set(row[7])
            
        def update_data(self):
            try:
                con=cx_Oracle.connect('system/yash@localhost:1521/system')
                cur=con.cursor()


                sql ="update stud set name= :1,class= :2,gender= :5,contact= :6,dob= :7,guardian= :8,guardian_cont= :9 where roll_no= :10"
                cur.execute( sql,(
                                   self.name_var.get(),
                                   self.class_var.get(),
                                   self.gender_var.get(),
                                   self.contact_var.get(),
                                   self.dob_var.get(),
                                   self.guardian_var.get(),
                                   self.guard_cont_var.get(),
                                   self.Roll_No_var.get()
                                   ))
                con.commit()
                con.close()
                self.fetch_data()
                self.clear()
                messagebox.showinfo("Success","Record is updated successfully")
                
            except cx_Oracle.DatabaseError:
                messagebox.showerror("Error",str(sys.exc_info()[0])+"\n"+str(sys.exc_info()[1]))
                self.clear()
            
        def delete_data(self):
            con=cx_Oracle.connect('system/yash@localhost:1521/system')
            cur=con.cursor()

            cur.execute("delete from stud where roll_no= :1",{'1':self.Roll_No_var.get()})

            con.commit()
            con.close()
            self.fetch_data()
            self.clear()
            messagebox.showinfo("Success","Record is deleted successfully")
            
        def search_data(self):
            con=cx_Oracle.connect('system/yash@localhost:1521/system')
            cur=con.cursor()

            cur.execute("select * from stud where "+str(self.search_by.get())+" LIKE '%"+str(self.search_txt.get())+"%'")
            rows=cur.fetchall()
            self.Student_Table.delete(*self.Student_Table.get_children())
            if len(rows)!=0:
                for row in rows:
                    self.Student_Table.insert('',END,values=row)
                con.commit()
            con.close()

        
################################# Teacher class##############################################


    class Teacher_Details(tk.Frame):
        def __init__(self, parent, controller):
            tk.Frame.__init__(self, parent)
            self.controller = controller

            self.bg_icon=ImageTk.PhotoImage(file="43629.jpg")
            bg_lbl=tk.Label(self,image=self.bg_icon).pack()
            title=tk.Label(self,text="Teacher Details",font=("times ne roman",40,"bold"),bg="yellow",fg="red",bd=10,relief=GROOVE)
            title.place(x=0,y=0,relwidth=1)

            Admin_Frame=tk.Frame(self,bg="black")
            Admin_Frame.place(x=0,y=83,width=1366,height=60)

            button = tk.Button(Admin_Frame, text="Student",width=10,command=lambda: controller.show_frame("Student_Details"),font=("times new roman",14,"bold"),bg="white",fg="red").grid(row=0,column=0,pady=10)
            button1 = tk.Button(Admin_Frame, text="Teacher",width=10,command=lambda: controller.show_frame("Teacher_Details"),font=("times new roman",14,"bold"),bg="white",fg="red").grid(row=0,column=1,pady=10)
            button3 = tk.Button(Admin_Frame, text="Create User",width=10,command=lambda: controller.show_frame("Create_User"),font=("times new roman",14,"bold"),bg="white",fg="red").grid(row=0,column=3,pady=10)
            button5 = tk.Button(Admin_Frame, text="Report",width=12,command=lambda: controller.show_frame("Admin_Report"),font=("times new roman",14,"bold"),bg="white",fg="red").grid(row=0,column=5,pady=10)
            button6 = tk.Button(Admin_Frame, text="Log Out",width=12,command=lambda: controller.show_frame("LoginPage"),font=("times new roman",14,"bold"),bg="white",fg="red").grid(row=0,column=6,pady=10)

            self.Id_var=StringVar()
            self.name_var=StringVar()
            self.subject_var=StringVar()
            self.gender_var=StringVar()
            self.contact_var=StringVar()
            self.high_qual_var=StringVar()
            self.search_by=tk.StringVar()
            self.search_txt=tk.StringVar()



            Teacher_Frame=Frame(self,bd=4,relief=GROOVE,bg="white")
            Teacher_Frame.place(x=190,y=145,width=1000,height=255)
            
            
            lbl_id=Label(Teacher_Frame,text="Id",bg="crimson",fg="white",font=("times new roman",20,"bold"))
            lbl_id.grid(row=1,column=0,pady=5,padx=20,sticky="w")

            txt_id=Entry(Teacher_Frame,textvariable=self.Id_var,font=("times new roman",15,"bold"),bd=5,relief=GROOVE)
            txt_id.grid(row=1,column=1,pady=5,padx=20,sticky="w")

            lbl_name=Label(Teacher_Frame,text="Name",bg="crimson",fg="white",font=("times new roman",20,"bold"))
            lbl_name.grid(row=1,column=4,pady=5,padx=20,sticky="w")

            txt_name=Entry(Teacher_Frame,textvariable=self.name_var,font=("times new roman",15,"bold"),bd=5,relief=GROOVE)
            txt_name.grid(row=1,column=5,pady=5,padx=20,sticky="w")

            lbl_course=Label(Teacher_Frame,text="Subject",bg="crimson",fg="white",font=("times new roman",20,"bold"))
            lbl_course.grid(row=2,column=0,pady=5,padx=20,sticky="w")

            txt_course=Entry(Teacher_Frame,textvariable=self.subject_var,font=("times new roman",15,"bold"),bd=5,relief=GROOVE)
            txt_course.grid(row=2,column=1,pady=5,padx=20,sticky="w")

            lbl_Gender=Label(Teacher_Frame,text="Gender",bg="crimson",fg="white",font=("times new roman",20,"bold"))
            lbl_Gender.grid(row=2,column=4,pady=5,padx=20,sticky="w")

            combo_gender=ttk.Combobox(Teacher_Frame,textvariable=self.gender_var,font=("times new roman",13,"bold"),state='readonly')
            combo_gender['values']=("Male","Female","other")
            combo_gender.grid(row=2,column=5,pady=5,padx=20)

            lbl_Contact=Label(Teacher_Frame,text="Contact",bg="crimson",fg="white",font=("times new roman",20,"bold"))
            lbl_Contact.grid(row=3,column=0,pady=5,padx=20,sticky="w")

            txt_Contact=Entry(Teacher_Frame,textvariable=self.contact_var,font=("times new roman",15,"bold"),bd=5,relief=GROOVE)
            txt_Contact.grid(row=3,column=1,pady=5,padx=20,sticky="w")

            lbl_High_qual=Label(Teacher_Frame,text="Highest Qual.",bg="crimson",fg="white",font=("times new roman",20,"bold"))
            lbl_High_qual.grid(row=3,column=4,pady=5,padx=20,sticky="w")

            txt_High_qual=Entry(Teacher_Frame,textvariable=self.high_qual_var,font=("times new roman",15,"bold"),bd=5,relief=GROOVE)
            txt_High_qual.grid(row=3,column=5,pady=5,padx=20,sticky="w")

            #######################button####################

            Addbtn=tk.Button(Teacher_Frame,text="Add",width=10,command=self.add_teachers,font=("times new roman",11,"bold"),bg="crimson",fg="white").grid(row=1,column=6,pady=10)
            updatebtn=Button(Teacher_Frame,text="Update",width=10,command=self.update_data,font=("times new roman",11,"bold"),bg="crimson",fg="white").grid(row=2,column=6,pady=10)
            deletebtn=Button(Teacher_Frame,text="Delete",width=10,command=self.delete_data,font=("times new roman",11,"bold"),bg="crimson",fg="white").grid(row=3,column=6,pady=10)
            Clearbtn =Button(Teacher_Frame,text="Clear",width=10,command=self.clear,font=("times new roman",11,"bold"),bg="crimson",fg="white").grid(row=4,column=6,pady=10)



            ##########################detail frame#######################

            Detail_Frame=Frame(self,bd=4,relief=GROOVE,bg="white")
            Detail_Frame.place(x=190,y=400,width=1000,height=300)

            lbl_Search=Label(Detail_Frame,text="Search BY",bg="crimson",fg="white",font=("times new roman",20,"bold"))
            lbl_Search.grid(row=0,column=0,pady=10,padx=20,sticky="w")

            combo_Search=ttk.Combobox(Detail_Frame,textvariable=self.search_by,width=12,font=("times new roman",13,"bold"),state='readonly')
            combo_Search['values']=("Id","Name","Subject","Contact")
            combo_Search.grid(row=0,column=1,pady=10,padx=20)

            txt_Search=Entry(Detail_Frame,textvariable=self.search_txt,width=20,font=("times new roman",10,"bold"),bd=5,relief=GROOVE)
            txt_Search.grid(row=0,column=2,pady=10,padx=20,sticky="w")

            Searchbtn=Button(Detail_Frame,text="Search",width=10,command=self.search_data,pady=5).grid(row=0,column=3,padx=10,pady=10)
            Showallbtn=Button(Detail_Frame,text="Show All",width=10,command=self.fetch_data,pady=5).grid(row=0,column=4,padx=10,pady=10)

            #################Table Frame#############################

            Table_Frame=Frame(Detail_Frame,bd=4,relief=RIDGE,bg="crimson")
            Table_Frame.place(x=10,y=55,width=870,height=230)

            scroll_x=Scrollbar(Table_Frame,orient=HORIZONTAL)
            scroll_y=Scrollbar(Table_Frame,orient=VERTICAL)

            self.Teacher_Table=ttk.Treeview(Table_Frame,columns=("Id","Name","Subject","Gender","Contact","Highest Qual."),xscrollcommand=scroll_x.set,yscrollcommand=scroll_y.set)
            scroll_x.pack(side=BOTTOM,fill=X)
            scroll_y.pack(side=RIGHT,fill=Y)
            scroll_x.config(command=self.Teacher_Table.xview)
            scroll_y.config(command=self.Teacher_Table.yview)
            self.Teacher_Table.heading("Id",text="Id")
            self.Teacher_Table.heading("Name",text="Name")
            self.Teacher_Table.heading("Subject",text="Subject")
            self.Teacher_Table.heading("Gender",text="Gender")
            self.Teacher_Table.heading("Contact",text="Contact")
            self.Teacher_Table.heading("Highest Qual.",text="Highest Qual.")

            self.Teacher_Table['show']='headings'

            self.Teacher_Table.column("Id",width=100)
            self.Teacher_Table.column("Name",width=100)
            self.Teacher_Table.column("Subject",width=150)
            self.Teacher_Table.column("Gender",width=100)
            self.Teacher_Table.column("Contact",width=100)
            self.Teacher_Table.column("Highest Qual.",width=150)

            self.Teacher_Table.pack(fill=BOTH,expand=1)

            self.Teacher_Table.bind("<ButtonRelease-1>",self.get_cursor)
            self.fetch_data()


        def add_teachers(self):
            try:
                if self.Id_var.get()=="" or \
                   self.name_var.get()=="" or \
                   self.subject_var.get()=="" or \
                   self.gender_var.get()=="" or \
                   self.contact_var.get()=="" or \
                   self.high_qual_var.get()=="":
                    
                    messagebox.showerror("Error","All fields are required!!!")
                else:
                    if len(self.contact_var.get())!=10:
                        messagebox.showerror("Error","Enter a valid 10 digit contact number")
                        self.contact_var.set('')
                    else:
                        con=cx_Oracle.connect('system/yash@localhost:1521/system')
                        cur=con.cursor()
                        sql= "insert into teacher(id,name,subject,gender,contact,highest_qual) values (:1,:2,:3,:4,:5,:6)"
                        cur.execute(sql, (
                                           self.Id_var.get(),
                                           self.name_var.get(),
                                           self.subject_var.get(),
                                           self.gender_var.get(),
                                           self.contact_var.get(),
                                           self.high_qual_var.get()
                                           ))
                        con.commit()
                        con.close()
                        self.fetch_data()
                        self.clear()
                        messagebox.showinfo("Success","Record is inserted successfully")
            except cx_Oracle.IntegrityError:
                messagebox.showerror("Error"," ID is a Unique Variable\n please give a different unique value to it")
                self.Id_var.set('')
            except cx_Oracle.DatabaseError:
                messagebox.showerror("Error",str(sys.exc_info()[0])+"\n"+str(sys.exc_info()[1]))
                self.clear()
            
        def fetch_data(self):
            con=cx_Oracle.connect('system/yash@localhost:1521/system')
            cur=con.cursor()

            cur.execute("select * from teacher order by id")
            rows=cur.fetchall()
            self.Teacher_Table.delete(*self.Teacher_Table.get_children())
            if len(rows)!=0:
                for row in rows:
                    self.Teacher_Table.insert('',END,values=row)
                con.commit()
            con.close()

        def clear(self):
            self.Id_var.set('')
            self.name_var.set('')
            self.subject_var.set('')
            self.gender_var.set('')
            self.contact_var.set('')
            self.high_qual_var.set('')

        def get_cursor(self,ev):
            cursor_row=self.Teacher_Table.focus()
            contents=self.Teacher_Table.item(cursor_row)
            row=(contents['values'])
            self.Id_var.set(row[0])
            self.name_var.set(row[1])
            self.subject_var.set(row[2])
            self.gender_var.set(row[3])
            self.contact_var.set(row[4])
            self.high_qual_var.set(row[5])
            
        def update_data(self):
            try:
                con=cx_Oracle.connect('system/yash@localhost:1521/system')
                cur=con.cursor()

                sql="update teacher set name= :1,subject = :2,gender= :3,contact= :4,highest_qual= :5 where id= :6"
                cur.execute(sql, (
                                   self.name_var.get(),
                                   self.subject_var.get(),
                                   self.gender_var.get(),
                                   self.contact_var.get(),
                                   self.high_qual_var.get(),
                                   self.Id_var.get()
                                  ))
                con.commit()
                self.fetch_data()
                self.clear()
                con.close()
                messagebox.showinfo("Success","Record is updated successfully")

            except cx_Oracle.DatabaseError:
                messagebox.showerror("Error",str(sys.exc_info()[0])+"\n"+str(sys.exc_info()[1]))
                self.clear()
            
        def delete_data(self):
            con=cx_Oracle.connect('system/yash@localhost:1521/system')
            cur=con.cursor()

            cur.execute("delete from teacher where id= :1",{'1':self.Id_var.get()})
            con.commit()
            self.fetch_data()
            self.clear()
            con.close()
            messagebox.showinfo("Success","Record is deleted successfully")

        def search_data(self):
            con=cx_Oracle.connect('system/yash@localhost:1521/system')
            cur=con.cursor()

            cur.execute("select * from teacher where "+str(self.search_by.get())+" LIKE '%"+str(self.search_txt.get())+"%'")
            rows=cur.fetchall()
            self.Teacher_Table.delete(*self.Teacher_Table.get_children())
            if len(rows)!=0:
                for row in rows:
                    self.Teacher_Table.insert('',END,values=row)
                con.commit()
            con.close()


############################################# Create User ###############################################################


    class Create_User(tk.Frame):
        def __init__(self, parent, controller):
            tk.Frame.__init__(self, parent)
            self.controller = controller

            self.bg_icon=ImageTk.PhotoImage(file="43629.jpg")
            bg_lbl=tk.Label(self,image=self.bg_icon).pack()
            title=tk.Label(self,text="Create User",font=("times new roman",38,"bold"),bg="yellow",fg="red",bd=10,relief=GROOVE)
            title.place(x=0,y=0,relwidth=1)

            Admin_Frame=tk.Frame(self,bg="black")
            Admin_Frame.place(x=0,y=83,width=1366,height=60)

            button = tk.Button(Admin_Frame, text="Student",width=10,command=lambda: controller.show_frame("Student_Details"),font=("times new roman",14,"bold"),bg="white",fg="red").grid(row=0,column=0,pady=10)
            button1 = tk.Button(Admin_Frame, text="Teacher",width=10,command=lambda: controller.show_frame("Teacher_Details"),font=("times new roman",14,"bold"),bg="white",fg="red").grid(row=0,column=1,pady=10)
            button3 = tk.Button(Admin_Frame, text="Create User",width=10,command=lambda: controller.show_frame("Create_User"),font=("times new roman",14,"bold"),bg="white",fg="red").grid(row=0,column=3,pady=10)
            button5 = tk.Button(Admin_Frame, text="Report",width=12,command=lambda: controller.show_frame("Admin_Report"),font=("times new roman",14,"bold"),bg="white",fg="red").grid(row=0,column=5,pady=10)
            button6 = tk.Button(Admin_Frame, text="Log Out",width=12,command=lambda: controller.show_frame("LoginPage"),font=("times new roman",14,"bold"),bg="white",fg="red").grid(row=0,column=6,pady=10)


            self.user_var=StringVar()
            self.Id_var=StringVar()
            self.Username_var=StringVar()
            self.Pass_var=StringVar()
            self.search_by=tk.StringVar()
            self.search_txt=tk.StringVar()
            

            User_Frame=Frame(self,bd=4,relief=GROOVE,bg="white")
            User_Frame.place(x=300,y=143,width=800,height=250)

            lbl_User_type=Label(User_Frame,text="User type",bg="crimson",fg="white",font=("times new roman",20,"bold"))
            lbl_User_type.grid(row=1,column=0,pady=10,padx=20,sticky="w")

            combo_User_type=ttk.Combobox(User_Frame,textvariable=self.user_var,width=10,font=("times new roman",13,"bold"),state='readonly')
            combo_User_type['values']=("Teacher","Student")
            combo_User_type.grid(row=1,column=1,pady=10,padx=20,sticky="w")
            
                    
            lbl_Id=Label(User_Frame,text="Id",bg="crimson",fg="white",font=("times new roman",20,"bold"))
            lbl_Id.grid(row=2,column=0,pady=10,padx=20,sticky="w")

            txt_Id=Entry(User_Frame,textvariable=self.Id_var,font=("times new roman",13,"bold"),bd=5,relief=GROOVE)
            txt_Id.grid(row=2,column=1,pady=10,padx=20,sticky="w")

            lbl_Username=Label(User_Frame,text="Username",bg="crimson",fg="white",font=("times new roman",20,"bold"))
            lbl_Username.grid(row=3,column=0,pady=10,padx=20,sticky="w")

            txt_Username=Entry(User_Frame,textvariable=self.Username_var,font=("times new roman",13,"bold"),bd=5,relief=GROOVE)
            txt_Username.grid(row=3,column=1,pady=10,padx=20,sticky="w")

            
            lbl_Password=Label(User_Frame,text="Password",bg="crimson",fg="white",font=("times new roman",20,"bold"))
            lbl_Password.grid(row=4,column=0,pady=10,padx=20,sticky="w")

            txt_Password=Entry(User_Frame,textvariable=self.Pass_var,font=("times new roman",13,"bold"),bd=5,relief=GROOVE)
            txt_Password.grid(row=4,column=1,pady=10,padx=20,sticky="w")
            
            #######################button####################

            Addbtn=tk.Button(User_Frame, text="Add",width=10,command=self.add_user,font=("times new roman",12,"bold"),bg="crimson",fg="white").grid(row=1,column=4,pady=10)
            updatebtn=Button(User_Frame, text="Update",width=10,command=self.update_user,font=("times new roman",12,"bold"),bg="crimson",fg="white").grid(row=2,column=4,pady=10,sticky="w")
            deletebtn=Button(User_Frame, text="Delete",width=10,command=self.delete_user,font=("times new roman",12,"bold"),bg="crimson",fg="white").grid(row=3,column=4,pady=10)
            Clearbtn =Button(User_Frame, text="Clear",width=10,command=self.clear,font=("times new roman",12,"bold"),bg="crimson",fg="white").grid(row=4,column=4,pady=10,sticky="w")

            ##########################detail frame#######################

            Detail_Frame=Frame(self,bd=4,relief=GROOVE,bg="white")
            Detail_Frame.place(x=300,y=393,width=800,height=308)

            lbl_Search=Label(Detail_Frame,text="Search By",bg="crimson",fg="white",font=("times new roman",18,"bold"))
            lbl_Search.grid(row=0,column=0,pady=10,padx=15,sticky="w")

            combo_Search=ttk.Combobox(Detail_Frame,textvariable=self.search_by,width=10,font=("times new roman",13,"bold"),state='readonly')
            combo_Search['values']=("Id","Username")
            combo_Search.grid(row=0,column=1,pady=10,padx=15)

            txt_Search=Entry(Detail_Frame,textvariable=self.search_txt,width=20,font=("times new roman",12,"bold"),bd=5,relief=GROOVE)
            txt_Search.grid(row=0,column=2,pady=10,padx=15,sticky="w")

            Searchbtn=Button(Detail_Frame,text="Search",width=9,command=self.search_user,pady=5).grid(row=0,column=3,padx=10,pady=10)
            Showallbtn=Button(Detail_Frame,text="Show All",width=9,command=self.fetch_data,pady=5).grid(row=0,column=4,padx=10,pady=10)

            #################Table Frame#############################

            Table_Frame=Frame(Detail_Frame,bd=4,relief=RIDGE,bg="crimson")
            Table_Frame.place(x=6,y=55,width=780,height=240)

            scroll_x=Scrollbar(Table_Frame,orient=HORIZONTAL)
            scroll_y=Scrollbar(Table_Frame,orient=VERTICAL)

            self.User_Table=ttk.Treeview(Table_Frame,columns=("User_type","Id","Username","Password"),xscrollcommand=scroll_x.set,yscrollcommand=scroll_y.set)
            scroll_x.pack(side=BOTTOM,fill=X)
            scroll_y.pack(side=RIGHT,fill=Y)
            scroll_x.config(command=self.User_Table.xview)
            scroll_y.config(command=self.User_Table.yview)
            self.User_Table.heading("User_type",text="User_type")
            self.User_Table.heading("Id",text="Id")
            self.User_Table.heading("Username",text="Username")
            self.User_Table.heading("Password",text="Password")
       
            self.User_Table['show']='headings'

            self.User_Table.column("User_type",width=100)
            self.User_Table.column("Id",width=100)
            self.User_Table.column("Username",width=100)
            self.User_Table.column("Password",width=100) 

            self.User_Table.pack(fill=BOTH,expand=1)

            self.User_Table.bind("<ButtonRelease-1>",self.get_cursor)
            self.fetch_data()

        def add_user(self):
            try:
                if self.user_var.get()=="" or self.Id_var.get()=="" or self.Username_var.get()=="" or self.Pass_var.get()=="":
                    messagebox.showerror("Error","All fields are required!!!")
                else:
                    con=cx_Oracle.connect('system/yash@localhost:1521/system')
                    cur=con.cursor()
                    
                    cur.execute("insert into userss(user_type,id,username,password) values (:1,:2,:3,:4)",(
                                                                                                          self.user_var.get(),
                                                                                                          self.Id_var.get(),
                                                                                                          self.Username_var.get(),
                                                                                                          self.Pass_var.get()
                                                                                                          ))
                    

                    con.commit()
                    con.close()
                    self.fetch_data()
                    self.clear()
                    messagebox.showinfo("Success","User created successfully")
            except cx_Oracle.IntegrityError:
                messagebox.showerror("Error"," Id is a Unique Variable\n please give a different unique value to it")
                self.Id_var.set('')
            except cx_Oracle.DatabaseError:
                messagebox.showerror("Error",str(sys.exc_info()[0])+"\n"+str(sys.exc_info()[1]))
                self.clear()
            
        def delete_user(self):
            con=cx_Oracle.connect('system/yash@localhost:1521/system')
            cur=con.cursor()

            cur.execute("delete from userss where id =:1",({'1':self.Id_var.get()}))

            con.commit()
            con.close()
            self.fetch_data()
            self.clear()
            messagebox.showinfo("Success","User deleted successfully")
                    
        def fetch_data(self):
            con=cx_Oracle.connect('system/yash@localhost:1521/system')
            cur=con.cursor()

            cur.execute("select * from userss order by id")
            rows=cur.fetchall()
            self.User_Table.delete(*self.User_Table.get_children())
            if len(rows)!=0:
                for row in rows:
                    self.User_Table.insert('',END,values=row)
                con.commit()
            con.close()

        def clear(self):
            self.user_var.set('')
            self.Id_var.set('')
            self.Username_var.set('')
            self.Pass_var.set('')
            
        def get_cursor(self,ev):
            cursor_row=self.User_Table.focus()
            contents=self.User_Table.item(cursor_row)
            row=(contents['values'])
            self.user_var.set(row[0])
            self.Id_var.set(row[1])
            self.Username_var.set(row[2])
            self.Pass_var.set(row[3])        

        def update_user(self):
            try:
                con=cx_Oracle.connect('system/yash@localhost:1521/system')
                cur=con.cursor()

                cur.execute("update userss set username= :1,password= :2 where id= :3 and user_type =:4",(
                                                                                                         self.Username_var.get(),
                                                                                                         self.Pass_var.get(),
                                                                                                         self.Id_var.get(),
                                                                                                         self.user_var.get()
                                                                                                         ))

                con.commit()
                self.fetch_data()
                self.clear()
                con.close()
                messagebox.showinfo("Success","User updated successfully")

            except cx_Oracle.DatabaseError:
                messagebox.showerror("Error",str(sys.exc_info()[0])+"\n"+str(sys.exc_info()[1]))
                self.clear()

        def search_user(self):
            con=cx_Oracle.connect('system/yash@localhost:1521/system')
            cur=con.cursor()

            cur.execute("select * from userss where "+str(self.search_by.get())+" LIKE '%"+str(self.search_txt.get())+"%'")
            rows=cur.fetchall()
            self.User_Table.delete(*self.User_Table.get_children())
            if len(rows)!=0:
                for row in rows:
                    self.User_Table.insert('',END,values=row)
                con.commit()
            con.close()
############################################ Report#########################
    class Admin_Report(tk.Frame):
        def __init__(self, parent, controller):
            tk.Frame.__init__(self, parent)
            self.controller=controller

            self.bg_icon=ImageTk.PhotoImage(file="bgg1.jpg")
            bg_lbl=tk.Label(self, image=self.bg_icon).pack()
            title=tk.Label(self, text="Result Details", font=("times new roman", 40, "bold"), bg="yellow", fg="red",
                           bd=10, relief=GROOVE)
            title.place(x=0, y=0, relwidth=1)

            self.search_by=tk.StringVar()
            self.search_txt=tk.StringVar()
            Admin_Frame=tk.Frame(self,bg="black")
            Admin_Frame.place(x=0,y=83,width=1366,height=60)

            button = tk.Button(Admin_Frame, text="Student",width=10,command=lambda: controller.show_frame("Student_Details"),font=("times new roman",14,"bold"),bg="white",fg="red").grid(row=0,column=0,pady=10)
            button1 = tk.Button(Admin_Frame, text="Teacher",width=10,command=lambda: controller.show_frame("Teacher_Details"),font=("times new roman",14,"bold"),bg="white",fg="red").grid(row=0,column=1,pady=10)
            button3 = tk.Button(Admin_Frame, text="Create User",width=10,command=lambda: controller.show_frame("Create_User"),font=("times new roman",14,"bold"),bg="white",fg="red").grid(row=0,column=3,pady=10)
            button5 = tk.Button(Admin_Frame, text="Report",width=12,command=lambda: controller.show_frame("Admin_Report"),font=("times new roman",14,"bold"),bg="white",fg="red").grid(row=0,column=5,pady=10)
            button6 = tk.Button(Admin_Frame, text="Log Out",width=12,command=lambda: controller.show_frame("LoginPage"),font=("times new roman",14,"bold"),bg="white",fg="red").grid(row=0,column=6,pady=10)


            ##########################detail frame#######################

            Detail_Frame=Frame(self, bd=4, relief=GROOVE, bg="white")
            Detail_Frame.place(x=230, y=145, width=1000, height=600)

            lbl_Search=Label(Detail_Frame, text="Search BY", bg="crimson", fg="white",
                             font=("times new roman", 20, "bold"))
            lbl_Search.grid(row=0, column=0, pady=10, padx=20, sticky="w")

            combo_Search=ttk.Combobox(Detail_Frame, textvariable=self.search_by, width=10,
                                      font=("times new roman", 13, "bold"), state='readonly')
            combo_Search['values']=("Roll_No")
            combo_Search.grid(row=0, column=1, pady=10, padx=20)

            txt_Search=Entry(Detail_Frame, textvariable=self.search_txt, width=20, font=("times new roman", 10, "bold"),
                             bd=5, relief=GROOVE)
            txt_Search.grid(row=0, column=2, pady=10, padx=20, sticky="w")

            Searchbtn=Button(Detail_Frame, text="Search", width=10, command=self.search_data, pady=5).grid(row=0,
                                                                                                           column=3,
                                                                                                           padx=10,
                                                                                                           pady=10)
            Showallbtn=Button(Detail_Frame, text="Show All", width=10, command=self.fetch_data, pady=5).grid(row=0,
                                                                                                             column=4,
                                                                                                             padx=10,
                                                                                                             pady=10)

            #################Table Frame#############################

            Table_Frame=Frame(Detail_Frame, bd=4, relief=RIDGE, bg="crimson")
            Table_Frame.place(x=10, y=60, width=970, height=495)

            scroll_x=Scrollbar(Table_Frame, orient=HORIZONTAL)
            scroll_y=Scrollbar(Table_Frame, orient=VERTICAL)

            col="Roll_no", "Attendance", "Attentive", "Uniform", "Behaviour", "Ethics", "English", "Extra"
            self.Result_Table=ttk.Treeview(Table_Frame, columns=col, xscrollcommand=scroll_x.set,
                                           yscrollcommand=scroll_y.set)
            scroll_x.pack(side=BOTTOM, fill=X)
            scroll_y.pack(side=RIGHT, fill=Y)
            scroll_x.config(command=self.Result_Table.xview)
            scroll_y.config(command=self.Result_Table.yview)
            #  self.fetch_data()
            # self.Result_Table.heading("Student_name",text="STUDENT NAME")
            self.Result_Table.heading("Roll_no", text="Roll No.")
            self.Result_Table.heading("Attendance", text="Attendance")
            self.Result_Table.heading("Attentive", text="Attentive")
            self.Result_Table.heading("Uniform", text="Uniform")
            self.Result_Table.heading("Behaviour", text="Behaviour")
            self.Result_Table.heading("Ethics", text="Ethics")
            self.Result_Table.heading("English", text="English")
            self.Result_Table.heading("Extra", text="Extra")

            self.Result_Table['show']='headings'

            # self.Result_Table.column("Student_name",width=120)
            self.Result_Table.column("Roll_no", width=120)
            self.Result_Table.column("Attendance", width=120)
            self.Result_Table.column("Attentive", width=120)
            self.Result_Table.column("Uniform", width=120)
            self.Result_Table.column("Behaviour", width=120)
            self.Result_Table.column("Ethics", width=150)
            self.Result_Table.column("English", width=120)
            self.Result_Table.column("Extra", width=120)

            self.Result_Table.pack(fill=BOTH, expand=1)
            # self.Result_Table.bind("<ButtonRelease-1>",self.get_cursor)
            self.fetch_data()

        def fetch_data(self):
            con=cx_Oracle.connect('system/yash@localhost:1521/system')
            cur=con.cursor()
            global s_p
            cur.execute(
                "select roll_no,sum(attendance),sum(attentive),sum(uniform),sum(behaviour),sum(ethics),sum(english),sum(extra) from response group by roll_no")
            rows=cur.fetchall()
            print(rows)
            self.Result_Table.delete(*self.Result_Table.get_children())
            if len(rows) != 0:
                self.Result_Table.delete(*self.Result_Table.get_children())
                for row in rows:
                    self.Result_Table.insert('', END, values=row)
            con.commit()
            con.close()

        def search_data(self):
            con=cx_Oracle.connect('system/yash@localhost:1521/system')
            cur=con.cursor()

            cur.execute("select * from response where " + str(self.search_by.get()) + " LIKE '%" + str(
                self.search_txt.get()) + "%'")
            rows=cur.fetchall()
            self.Result_Table.delete(*self.Result_Table.get_children())
            if len(rows) != 0:
                for row in rows:
                    self.Result_Table.insert('', END, values=row)
                con.commit()
            con.close()

    ################################################ Teacher System #################################################
    ######################################################################################################

    class Teacher_LoginPage(tk.Frame):

        def __init__(self, parent, controller):
            tk.Frame.__init__(self, parent)
            self.controller = controller
            

            ##############ALL IMAGES########
            self.bg_icon=ImageTk.PhotoImage(file="43629.jpg")
            self.user_icon=PhotoImage(file="user.png")
            self.pass_icon=PhotoImage(file="pass.png")
            self.logo_icon=PhotoImage(file="logo.png")
            ######### variables############
            self.uname=StringVar()
            self.passw=StringVar()

            bg_lbl=tk.Label(self,image=self.bg_icon).pack()
            title=tk.Label(self,text="Welcome To Teacher System",font=("times new roman",40,"bold"),bg="yellow",fg="red",bd=10,relief=GROOVE)
            title.place(x=0,y=0,relwidth=1)

            Login_Frame=tk.Frame(self,bg="white")
            Login_Frame.place(x=30,y=120)

            logolbl=tk.Label(Login_Frame,image=self.logo_icon,bd=0).grid(row=0,columnspan=2,pady=20)

            lbluser=tk.Label(Login_Frame,text="Username",image=self.user_icon,compound=LEFT,font=("times new roman",20,"bold"),bg="white").grid(rows=1,column=0,padx=20,pady=10)
            txtuser=tk.Entry(Login_Frame,bd=5,textvariable=self.uname,relief=GROOVE,font=("",15)).grid(row=1,column=1,padx=20)

            lblpass=tk.Label(Login_Frame,text="Password",image=self.pass_icon,compound=LEFT,font=("times new roman",20,"bold"),bg="white").grid(rows=2,column=0,padx=20,pady=10)
            txtpass=tk.Entry(Login_Frame,bd=5,textvariable=self.passw,relief=GROOVE,font=("",15),show="*").grid(row=2,column=1,padx=20)

            btn_log=tk.Button(Login_Frame,text="Login",width=10,command=self.login,font=("times new roman",14,"bold"),bg="yellow",fg="red").grid(row=3,column=1,pady=10)
            btn_log=tk.Button(Login_Frame,text="Back",width=10,command=lambda: controller.show_frame("StartPage"),font=("times new roman",14,"bold"),bg="yellow",fg="red").grid(row=4,column=1,pady=10)





        def login(self):
            con=cx_Oracle.connect('system/yash@localhost:1521/system')
            cur=con.cursor()

            cur.execute("select username,password from userss where user_type = 'Teacher'")
            rows=cur.fetchall()
            print(rows)
            
            if self.uname.get()=="" or self.passw.get()=="":
                messagebox.showerror("Error","All fields are required!!!")
            elif (self.uname.get(),self.passw.get()) in rows:
                 messagebox.showinfo("Successfull",f"welcome {self.uname.get()}")
                 global u_p
                 u_p=[self.uname.get(),self.passw.get()]
                 self.passw.set('')
                 self.uname.set('')
                 con.commit()
                 con.close()
                 self.controller.show_frame("Options")
                 
            else:
                messagebox.showerror("Error","Invalid Username or Password!!!")

################################ OPtions #######################

    class Options(tk.Frame):

        def __init__(self, parent, controller):
            tk.Frame.__init__(self, parent)
            self.controller = controller
            
            self.bg_icon=ImageTk.PhotoImage(file="images.jpg")
            bg_lbl=tk.Label(self,image=self.bg_icon).pack()
            title=tk.Label(self,text="OPTIONS",font=("times new roman",40,"bold"),bg="cadetblue",fg="chartreuse",bd=10,relief=GROOVE)
            title.place(x=0,y=0,relwidth=1)

            Menu_Frame=tk.Frame(self,bg="light coral")
            Menu_Frame.place(x=150,y=150)
            
            button1 = tk.Button(Menu_Frame, text="ATTENDENCE AND ARRIVAL TIME",width=35,command=lambda: controller.show_frame("Attendence"),font=("times new roman",14,"bold"),bg="cadetblue",fg="chartreuse").grid(row=0,column=0,pady=10)
            button2 = tk.Button(Menu_Frame, text="ATTENTIVE",width=35,command=lambda: controller.show_frame("Attentive"),font=("times new roman",14,"bold"),bg="cadetblue",fg="chartreuse").grid(row=1,column=0,pady=10)
            button3 = tk.Button(Menu_Frame, text="UNIFORM",width=35, command=lambda: controller.show_frame("Uniform"), font=("times new roman",14,"bold"),bg="cadetblue",fg="chartreuse").grid(row=2,column=0,pady=10)
            button4 = tk.Button(Menu_Frame, text="BEHAVIOUR WITH CLASS-MATES",width=35,command=lambda: controller.show_frame("Behaviour"),font=("times new roman",14,"bold"),bg="cadetblue",fg="chartreuse").grid(row=3,column=0,pady=10)
            button5 = tk.Button(Menu_Frame, text="GENERAL ETHICS WITH TEACHERS",width=35,command=lambda: controller.show_frame("Ethics"),font=("times new roman",14,"bold"),bg="cadetblue",fg="chartreuse").grid(row=4,column=0,pady=10)
            button6 = tk.Button(Menu_Frame, text="FLUENCY IN ENGLISH",width=35,command=lambda: controller.show_frame("English"),font=("times new roman",14,"bold"),bg="cadetblue",fg="chartreuse").grid(row=5,column=0,pady=10)
            button7 = tk.Button(Menu_Frame, text="EXTRA-CURRICULAM",width=35, command=lambda: controller.show_frame("Curriculam"), font=("times new roman",14,"bold"),bg="cadetblue",fg="chartreuse").grid(row=6,column=0,pady=10)
            

######################################### Attendence and Arrival##################################


    class Attendence(tk.Frame):
        def __init__(self, parent, controller):
            tk.Frame.__init__(self, parent)
            self.controller = controller

            self.bg_icon=ImageTk.PhotoImage(file="images.jpg")
            bg_lbl=tk.Label(self,image=self.bg_icon).pack()
            title=tk.Label(self,text="ATTANDACNE",font=("times new roman",38,"bold"),bg="yellow",fg="red",bd=10,relief=GROOVE)
            title.place(x=0,y=0,relwidth=1)

            
            self.stu_name=StringVar()
            self.stu_roll=StringVar()
            self.attendance= StringVar()
            self.arrival= StringVar()
            self.search_by=tk.StringVar()
            self.search_txt=tk.StringVar()


            User_Frame=Frame(self,bd=4,relief=GROOVE,bg="white")
            User_Frame.place(x=400,y=130,width=530,height=440)

            
            lbl_Name=Label(User_Frame,text="Name",bg="crimson",fg="white",font=("times new roman",20,"bold"))
            lbl_Name.grid(row=0,column=0,pady=10,padx=20,sticky="w")

            txt_Name=Entry(User_Frame,textvariable=self.stu_name,font=("times new roman",13,"bold"),bd=5,relief=GROOVE)
            txt_Name.grid(row=0,column=1,pady=10,padx=20,sticky="w")
            
            lbl_Roll_no=Label(User_Frame,text="Roll No.",bg="crimson",fg="white",font=("times new roman",20,"bold"))
            lbl_Roll_no.grid(row=1,column=0,pady=10,padx=20,sticky="w")

            txt_Roll_no=Entry(User_Frame,textvariable=self.stu_roll,font=("times new roman",13,"bold"),bd=5,relief=GROOVE)
            txt_Roll_no.grid(row=1,column=1,pady=10,padx=20,sticky="w")

            lbl_Attendance=Label(User_Frame,text="Attendance",bg="crimson",fg="white",font=("times new roman",18,"bold"))
            lbl_Attendance.grid(row=2,column=0,pady=10,padx=15,sticky="w")
            
            combo_Attendance=ttk.Combobox(User_Frame,textvariable=self.attendance,width=10,font=("times new roman",13,"bold"),state='readonly')
            combo_Attendance['values']=("Present", "Absent")
            combo_Attendance.grid(row=2,column=1,pady=10,padx=15)

            lbl_Arrival=Label(User_Frame,text="Arrival",bg="crimson",fg="white",font=("times new roman",18,"bold"))
            lbl_Arrival.grid(row=3,column=0,pady=10,padx=15,sticky="w")
            
            combo_Arrival=ttk.Combobox(User_Frame,textvariable=self.arrival,width=10,font=("times new roman",13,"bold"),state='readonly')
            combo_Arrival['values']=("Ontime", "Late")
            combo_Arrival.grid(row=3,column=1,pady=10,padx=15)


            
            #######################button####################

            Addbtn=tk.Button(User_Frame, text="Add",width=10,command=self.add_attendance,font=("times new roman",12,"bold"),bg="crimson",fg="white").grid(row=4,column=1,pady=10,sticky="nsew")
            Clearbtn =Button(User_Frame, text="Clear",width=10,command=self.clear,font=("times new roman",12,"bold"),bg="crimson",fg="white").grid(row=5,column=1,pady=10,sticky="nsew")
            
            ####  search ###########
            
            lbl_Search=Label(User_Frame,text="Search BY",bg="crimson",fg="white",font=("times new roman",18,"bold"))
            lbl_Search.grid(row=6,column=0,pady=10,padx=15,sticky="w")

            combo_Search=ttk.Combobox(User_Frame,textvariable=self.search_by,width=10,font=("times new roman",13,"bold"),state='readonly')
            combo_Search['values']=("Name", "Roll_No")
            combo_Search.grid(row=6,column=1,pady=10,padx=15)

            txt_Search=Entry(User_Frame,textvariable=self.search_txt,width=10,font=("times new roman",12,"bold"),bd=5,relief=GROOVE)
            txt_Search.grid(row=6,column=2,pady=10,padx=15,sticky="w")

            Searchbtn=Button(User_Frame,text="Search",width=8,command=self.search_user,pady=5).grid(row=7,column=0,padx=2,pady=10)
            Showallbtn=Button(User_Frame,text="Show All",width=8,command=self.fetch_data,pady=5).grid(row=7,column=1,padx=2,pady=10)
            button = tk.Button(User_Frame, text="Back",width=10,command=lambda: controller.show_frame("Options"),font=("times new roman",14,"bold"),bg="light coral",fg="white").grid(row=7,column=2,pady=10)

            ##########################detail frame#######################

            # Detail_Frame=Frame(self,bd=4,relief=GROOVE,bg="white")
            # Detail_Frame.place(x=160,y=170,width=300,height=530)



            #################Table Frame#############################

            Table_Frame=Frame(self,bd=4,relief=RIDGE,bg="crimson")
            Table_Frame.place(x=50,y=100,width=300,height=530)

            scroll_x=Scrollbar(Table_Frame,orient=HORIZONTAL)
            scroll_y=Scrollbar(Table_Frame,orient=VERTICAL)

            self.User_Table=ttk.Treeview(Table_Frame,columns=("Name","Roll No"),xscrollcommand=scroll_x.set,yscrollcommand=scroll_y.set)
            scroll_x.pack(side=BOTTOM,fill=X)
            scroll_y.pack(side=RIGHT,fill=Y)
            scroll_x.config(command=self.User_Table.xview)
            scroll_y.config(command=self.User_Table.yview)
            self.User_Table.heading("Name",text="Name")
            self.User_Table.heading("Roll No",text="Roll No")

            self.User_Table['show']='headings'

            self.User_Table.column("Name",width=50)
            self.User_Table.column("Roll No",width=50)
            
            self.User_Table.pack(fill=BOTH,expand=1)

            self.User_Table.bind("<ButtonRelease-1>",self.get_cursor)
            self.fetch_data()


        def add_attendance(self):
            global u_p
            con=cx_Oracle.connect('system/yash@localhost:1521/system')
            cur=con.cursor()
            cur.execute("select roll_no, teacher_name from response")
            stu_data = cur.fetchall()
            print(stu_data)
            if self.attendance.get()=="Present":
                x = 10
                if self.arrival.get()=="Ontime":
                    x+=2
                else:
                    x-=2
            else:
                x = -2
            
            if ((self.stu_roll.get(), u_p[0]) in stu_data):
                cur.execute("update response set attendance=:1 where teacher_name=:2 and roll_no=:3",(
                                                                                                x,
                                                                                                u_p[0],
                                                                                                self.stu_roll.get()
                                                                                                ))
            else:
                cur.execute("insert into response(attendance, student, roll_no, teacher_name) values(:1, :2, :3, :4)",(
                                                                                                x,
                                                                                                self.stu_name.get(),
                                                                                                self.stu_roll.get(),
                                                                                                u_p[0]
                                                                                                ))
            

            con.commit()
            self.fetch_data()
            self.clear()
            con.close()
            messagebox.showinfo("Record","Record Added...!!!")
        
        def fetch_data(self):
            con=cx_Oracle.connect('system/yash@localhost:1521/system')
            cur=con.cursor()

            cur.execute("select name, roll_no from stud order by roll_no")
            rows=cur.fetchall()
            self.User_Table.delete(*self.User_Table.get_children())
            if len(rows)!=0:
                for row in rows:
                    self.User_Table.insert('',END,values=row)
                con.commit()
            con.close()

        def clear(self):
            self.stu_name.set('')
            self.stu_roll.set('')
            self.attendance.set('')
            self.arrival.set('')

            
        def get_cursor(self,ev):
            cursor_row=self.User_Table.focus()
            contents=self.User_Table.item(cursor_row)
            row=(contents['values'])
            self.stu_name.set(row[0])
            self.stu_roll.set(row[1])

        def search_user(self):
            con=cx_Oracle.connect('system/yash@localhost:1521/system')
            cur=con.cursor()

            cur.execute("select * from stud where "+str(self.search_by.get())+" LIKE '%"+str(self.search_txt.get())+"%'")
            rows=cur.fetchall()
            self.User_Table.delete(*self.User_Table.get_children())
            if len(rows)!=0:
                for row in rows:
                    self.User_Table.insert('',END,values=row)
                con.commit()
            con.close()



####################### Attentive ################################

    class Attentive(tk.Frame):
        def __init__(self, parent, controller):
            tk.Frame.__init__(self, parent)
            self.controller = controller

            self.bg_icon=ImageTk.PhotoImage(file="43629.jpg")
            bg_lbl=tk.Label(self,image=self.bg_icon).pack()
            title=tk.Label(self,text="ATTENTIVE IN LECTURES",font=("times new roman",38,"bold"),bg="yellow",fg="red",bd=10,relief=GROOVE)
            title.place(x=0,y=0,relwidth=1)

            self.stu_name=StringVar()
            self.stu_roll=StringVar()
            self.attentive= StringVar()
            self.search_by=tk.StringVar()
            self.search_txt=tk.StringVar()


            User_Frame=Frame(self,bd=4,relief=GROOVE,bg="white")
            User_Frame.place(x=690,y=170,width=580,height=440)

            
            lbl_Name=Label(User_Frame,text="Name",bg="crimson",fg="white",font=("times new roman",20,"bold"))
            lbl_Name.grid(row=0,column=0,pady=10,padx=20,sticky="w")

            txt_Name=Entry(User_Frame,textvariable=self.stu_name,font=("times new roman",13,"bold"),bd=5,relief=GROOVE)
            txt_Name.grid(row=0,column=1,pady=10,padx=20,sticky="w")
            
            lbl_Roll_no=Label(User_Frame,text="Roll No.",bg="crimson",fg="white",font=("times new roman",20,"bold"))
            lbl_Roll_no.grid(row=1,column=0,pady=10,padx=20,sticky="w")

            txt_Roll_no=Entry(User_Frame,textvariable=self.stu_roll,font=("times new roman",13,"bold"),bd=5,relief=GROOVE)
            txt_Roll_no.grid(row=1,column=1,pady=10,padx=20,sticky="w")

            lbl_Attentive=Label(User_Frame,text="Attentive",bg="crimson",fg="white",font=("times new roman",18,"bold"))
            lbl_Attentive.grid(row=2,column=0,pady=10,padx=15,sticky="w")
            
            combo_Attentive=ttk.Combobox(User_Frame,textvariable=self.attentive,width=10,font=("times new roman",13,"bold"),state='readonly')
            combo_Attentive['values']=("Best", "Good", "Average", "Poor")
            combo_Attentive.grid(row=2,column=1,pady=10,padx=15)



            
            #######################button####################

            Addbtn=tk.Button(User_Frame, text="Add",width=10,command=self.add_attentive, font=("times new roman",12,"bold"),bg="crimson",fg="white").grid(row=4,column=1,pady=10,sticky="nsew")
            Clearbtn =Button(User_Frame, text="Clear",width=10,command=self.clear,font=("times new roman",12,"bold"),bg="crimson",fg="white").grid(row=5,column=1,pady=10,sticky="nsew")

            ####  search ###########
            
            lbl_Search=Label(User_Frame,text="Search BY",bg="crimson",fg="white",font=("times new roman",18,"bold"))
            lbl_Search.grid(row=6,column=0,pady=10,padx=15,sticky="w")

            combo_Search=ttk.Combobox(User_Frame,textvariable=self.search_by,width=10,font=("times new roman",13,"bold"),state='readonly')
            combo_Search['values']=("Name", "Roll No")
            combo_Search.grid(row=6,column=1,pady=10,padx=15)

            txt_Search=Entry(User_Frame,textvariable=self.search_txt,width=10,font=("times new roman",12,"bold"),bd=5,relief=GROOVE)
            txt_Search.grid(row=6,column=2,pady=10,padx=15,sticky="w")

            Searchbtn=Button(User_Frame,text="Search",width=8,command=self.search_user,pady=5).grid(row=7,column=0,padx=2,pady=10)
            Showallbtn=Button(User_Frame,text="Show All",width=8,command=self.fetch_data,pady=5).grid(row=7,column=1,padx=2,pady=10)
            button=tk.Button(User_Frame, text="Back", width=10, command=lambda: controller.show_frame("Options"),
                             font=("times new roman", 14, "bold"), bg="light coral", fg="white").grid(row=7, column=2,
                                                                                                      pady=10)

            ##########################detail frame#######################

            # Detail_Frame=Frame(self,bd=4,relief=GROOVE,bg="white")
            # Detail_Frame.place(x=160,y=170,width=300,height=530)



            #################Table Frame#############################

            Table_Frame=Frame(self,bd=4,relief=RIDGE,bg="crimson")
            Table_Frame.place(x=160,y=170,width=300,height=530)

            scroll_x=Scrollbar(Table_Frame,orient=HORIZONTAL)
            scroll_y=Scrollbar(Table_Frame,orient=VERTICAL)

            self.User_Table=ttk.Treeview(Table_Frame,columns=("Name","Roll No"),xscrollcommand=scroll_x.set,yscrollcommand=scroll_y.set)
            scroll_x.pack(side=BOTTOM,fill=X)
            scroll_y.pack(side=RIGHT,fill=Y)
            scroll_x.config(command=self.User_Table.xview)
            scroll_y.config(command=self.User_Table.yview)
            self.User_Table.heading("Name",text="Name")
            self.User_Table.heading("Roll No",text="Roll No")

            self.User_Table['show']='headings'

            self.User_Table.column("Name",width=50)
            self.User_Table.column("Roll No",width=50)
            
            self.User_Table.pack(fill=BOTH,expand=1)

            self.User_Table.bind("<ButtonRelease-1>",self.get_cursor)
            self.fetch_data()


        def add_attentive(self):
            global u_p
            con=cx_Oracle.connect('system/yash@localhost:1521/system')
            cur=con.cursor()
            cur.execute("select roll_no, teacher_name from response")
            stu_data = cur.fetchall()
            print(stu_data)
            if self.attentive.get()=="Best":
                x = 10
            elif self.attentive.get()=="Good":
                x=8
            elif self.attentive.get()=="Average":
                x=6
            else:
                x=4
            
            if ((self.stu_roll.get(), u_p[0]) in stu_data):
                cur.execute("update response set attentive=:1 where teacher_name=:2 and roll_no=:3",(
                                                                                                x,
                                                                                                u_p[0],
                                                                                                self.stu_roll.get()
                                                                                                ))
            else:
                cur.execute("insert into response(attentive, student, roll_no, teacher_name) values(:1, :2, :3, :4)",(
                                                                                                x,
                                                                                                self.stu_name.get(),
                                                                                                self.stu_roll.get(),
                                                                                                u_p[0]
                                                                                                ))
            

            con.commit()
            self.fetch_data()
            self.clear()
            con.close()
            messagebox.showinfo("Record","Record Added...!!!")
            
        def fetch_data(self):
            con=cx_Oracle.connect('system/yash@localhost:1521/system')
            cur=con.cursor()

            cur.execute("select name, roll_no from stud order by roll_no")
            rows=cur.fetchall()
            self.User_Table.delete(*self.User_Table.get_children())
            if len(rows)!=0:
                for row in rows:
                    self.User_Table.insert('',END,values=row)
                con.commit()
            con.close()

        def clear(self):
            self.stu_name.set('')
            self.stu_roll.set('')
            self.attentive.set('')
            
        def get_cursor(self,ev):
            cursor_row=self.User_Table.focus()
            contents=self.User_Table.item(cursor_row)
            row=(contents['values'])
            self.stu_name.set(row[0])
            self.stu_roll.set(row[1])

        def search_user(self):
            con=cx_Oracle.connect('system/yash@localhost:1521/system')
            cur=con.cursor()

            cur.execute("select * from stud where "+str(self.search_by.get())+" LIKE '%"+str(self.search_txt.get())+"%'")
            rows=cur.fetchall()
            self.User_Table.delete(*self.User_Table.get_children())
            if len(rows)!=0:
                for row in rows:
                    self.User_Table.insert('',END,values=row)
                con.commit()
            con.close()


####################### Uniform ################################

    class Uniform(tk.Frame):
        def __init__(self, parent, controller):
            tk.Frame.__init__(self, parent)
            self.controller = controller

            self.bg_icon=ImageTk.PhotoImage(file="43629.jpg")
            bg_lbl=tk.Label(self,image=self.bg_icon).pack()
            title=tk.Label(self,text="UNIFORM",font=("times new roman",38,"bold"),bg="yellow",fg="red",bd=10,relief=GROOVE)
            title.place(x=0,y=0,relwidth=1)

            self.stu_name=StringVar()
            self.stu_roll=StringVar()
            self.Uniform= StringVar()
            self.search_by=tk.StringVar()
            self.search_txt=tk.StringVar()


            User_Frame=Frame(self,bd=4,relief=GROOVE,bg="white")
            User_Frame.place(x=690,y=170,width=580,height=440)

            
            lbl_Name=Label(User_Frame,text="Name",bg="crimson",fg="white",font=("times new roman",20,"bold"))
            lbl_Name.grid(row=0,column=0,pady=10,padx=20,sticky="w")

            txt_Name=Entry(User_Frame,textvariable=self.stu_name,font=("times new roman",13,"bold"),bd=5,relief=GROOVE)
            txt_Name.grid(row=0,column=1,pady=10,padx=20,sticky="w")
            
            lbl_Roll_no=Label(User_Frame,text="Roll No.",bg="crimson",fg="white",font=("times new roman",20,"bold"))
            lbl_Roll_no.grid(row=1,column=0,pady=10,padx=20,sticky="w")

            txt_Roll_no=Entry(User_Frame,textvariable=self.stu_roll,font=("times new roman",13,"bold"),bd=5,relief=GROOVE)
            txt_Roll_no.grid(row=1,column=1,pady=10,padx=20,sticky="w")

            lbl_Uniform=Label(User_Frame,text="Uniform",bg="crimson",fg="white",font=("times new roman",18,"bold"))
            lbl_Uniform.grid(row=2,column=0,pady=10,padx=15,sticky="w")
            
            combo_Uniform=ttk.Combobox(User_Frame,textvariable=self.Uniform,width=10,font=("times new roman",13,"bold"),state='readonly')
            combo_Uniform['values']=("Proper", "Improper")
            combo_Uniform.grid(row=2,column=1,pady=10,padx=15)



            
            #######################button####################

            Addbtn=tk.Button(User_Frame, text="Add",width=10,command=self.add_uniform,font=("times new roman",12,"bold"),bg="crimson",fg="white").grid(row=4,column=1,pady=10,sticky="nsew")
            Clearbtn =Button(User_Frame, text="Clear",width=10,command=self.clear,font=("times new roman",12,"bold"),bg="crimson",fg="white").grid(row=5,column=1,pady=10,sticky="nsew")
            
            ####  search ###########
            
            lbl_Search=Label(User_Frame,text="Search BY",bg="crimson",fg="white",font=("times new roman",18,"bold"))
            lbl_Search.grid(row=6,column=0,pady=10,padx=15,sticky="w")

            combo_Search=ttk.Combobox(User_Frame,textvariable=self.search_by,width=10,font=("times new roman",13,"bold"),state='readonly')
            combo_Search['values']=("Name", "Roll No")
            combo_Search.grid(row=6,column=1,pady=10,padx=15)

            txt_Search=Entry(User_Frame,textvariable=self.search_txt,width=10,font=("times new roman",12,"bold"),bd=5,relief=GROOVE)
            txt_Search.grid(row=6,column=2,pady=10,padx=15,sticky="w")

            Searchbtn=Button(User_Frame,text="Search",width=8,command=self.search_user,pady=5).grid(row=7,column=0,padx=2,pady=10)
            Showallbtn=Button(User_Frame,text="Show All",width=8,command=self.fetch_data,pady=5).grid(row=7,column=1,padx=2,pady=10)
            button=tk.Button(User_Frame, text="Back", width=10, command=lambda: controller.show_frame("Options"),
                             font=("times new roman", 14, "bold"), bg="light coral", fg="white").grid(row=7, column=2,
                                                                                                      pady=10)

            ##########################detail frame#######################

            # Detail_Frame=Frame(self,bd=4,relief=GROOVE,bg="white")
            # Detail_Frame.place(x=160,y=170,width=300,height=530)



            #################Table Frame#############################

            Table_Frame=Frame(self,bd=4,relief=RIDGE,bg="crimson")
            Table_Frame.place(x=160,y=170,width=300,height=530)

            scroll_x=Scrollbar(Table_Frame,orient=HORIZONTAL)
            scroll_y=Scrollbar(Table_Frame,orient=VERTICAL)

            self.User_Table=ttk.Treeview(Table_Frame,columns=("Name","Roll No"),xscrollcommand=scroll_x.set,yscrollcommand=scroll_y.set)
            scroll_x.pack(side=BOTTOM,fill=X)
            scroll_y.pack(side=RIGHT,fill=Y)
            scroll_x.config(command=self.User_Table.xview)
            scroll_y.config(command=self.User_Table.yview)
            self.User_Table.heading("Name",text="Name")
            self.User_Table.heading("Roll No",text="Roll No")

            self.User_Table['show']='headings'

            self.User_Table.column("Name",width=50)
            self.User_Table.column("Roll No",width=50)
            
            self.User_Table.pack(fill=BOTH,expand=1)

            self.User_Table.bind("<ButtonRelease-1>",self.get_cursor)
            self.fetch_data()


        def add_uniform(self):
            global u_p
            con=cx_Oracle.connect('system/yash@localhost:1521/system')
            cur=con.cursor()
            cur.execute("select roll_no, teacher_name from response")
            stu_data = cur.fetchall()
            print(stu_data)
            if self.Uniform.get()=="Proper":
                x = 10
            else:
                x = 5
            
            if ((self.stu_roll.get(), u_p[0]) in stu_data):
                cur.execute("update response set uniform=:1 where teacher_name=:2 and roll_no=:3",(
                                                                                                x,
                                                                                                u_p[0],
                                                                                                self.stu_roll.get()
                                                                                                ))
            else:
                cur.execute("insert into response(uniform, student, roll_no, teacher_name) values(:1, :2, :3, :4)",(
                                                                                                x,
                                                                                                self.stu_name.get(),
                                                                                                self.stu_roll.get(),
                                                                                                u_p[0]
                                                                                                ))
            

            con.commit()
            self.fetch_data()
            self.clear()
            con.close()
            messagebox.showinfo("Record","Record Added...!!!")
        
            
        def fetch_data(self):
            con=cx_Oracle.connect('system/yash@localhost:1521/system')
            cur=con.cursor()

            cur.execute("select name, roll_no from stud order by roll_no")
            rows=cur.fetchall()
            self.User_Table.delete(*self.User_Table.get_children())
            if len(rows)!=0:
                for row in rows:
                    self.User_Table.insert('',END,values=row)
                con.commit()
            con.close()

        def clear(self):
            self.stu_roll.set('')
            self.stu_name.set('')
            self.Uniform.set('')
            
        def get_cursor(self,ev):
            cursor_row=self.User_Table.focus()
            contents=self.User_Table.item(cursor_row)
            row=(contents['values'])
            self.stu_name.set(row[0])
            self.stu_roll.set(row[1])

        def search_user(self):
            con=cx_Oracle.connect('system/yash@localhost:1521/system')
            cur=con.cursor()

            cur.execute("select * from stud where "+str(self.search_by.get())+" LIKE '%"+str(self.search_txt.get())+"%'")
            rows=cur.fetchall()
            self.User_Table.delete(*self.User_Table.get_children())
            if len(rows)!=0:
                for row in rows:
                    self.User_Table.insert('',END,values=row)
                con.commit()
            con.close()

####################### Behaviour ################################

    class Behaviour(tk.Frame):
        def __init__(self, parent, controller):
            tk.Frame.__init__(self, parent)
            self.controller = controller

            self.bg_icon=ImageTk.PhotoImage(file="43629.jpg")
            bg_lbl=tk.Label(self,image=self.bg_icon).pack()
            title=tk.Label(self,text="BEHAVIOUR WITH CLASS-MATES",font=("times new roman",38,"bold"),bg="yellow",fg="red",bd=10,relief=GROOVE)
            title.place(x=0,y=0,relwidth=1)

            self.stu_name=StringVar()
            self.stu_roll=StringVar()
            self.Behaviour= StringVar()
            self.search_by=tk.StringVar()
            self.search_txt=tk.StringVar()


            User_Frame=Frame(self,bd=4,relief=GROOVE,bg="white")
            User_Frame.place(x=690,y=170,width=580,height=440)

            
            lbl_Name=Label(User_Frame,text="Name",bg="crimson",fg="white",font=("times new roman",20,"bold"))
            lbl_Name.grid(row=0,column=0,pady=10,padx=20,sticky="w")

            txt_Name=Entry(User_Frame,textvariable=self.stu_name,font=("times new roman",13,"bold"),bd=5,relief=GROOVE)
            txt_Name.grid(row=0,column=1,pady=10,padx=20,sticky="w")
            
            lbl_Roll_no=Label(User_Frame,text="Roll No.",bg="crimson",fg="white",font=("times new roman",20,"bold"))
            lbl_Roll_no.grid(row=1,column=0,pady=10,padx=20,sticky="w")

            txt_Roll_no=Entry(User_Frame,textvariable=self.stu_roll,font=("times new roman",13,"bold"),bd=5,relief=GROOVE)
            txt_Roll_no.grid(row=1,column=1,pady=10,padx=20,sticky="w")

            lbl_Behaviour=Label(User_Frame,text="Behaviour",bg="crimson",fg="white",font=("times new roman",18,"bold"))
            lbl_Behaviour.grid(row=2,column=0,pady=10,padx=15,sticky="w")
            
            combo_Behaviour=ttk.Combobox(User_Frame,textvariable=self.Behaviour,width=10,font=("times new roman",13,"bold"),state='readonly')
            combo_Behaviour['values']=("Friendly", "Casual", "Introvert", "Aggresive", "Inappropriate")
            combo_Behaviour.grid(row=2,column=1,pady=10,padx=15)



            
            #######################button####################

            Addbtn=tk.Button(User_Frame, text="Add",width=10,command=self.add_behaviour,font=("times new roman",12,"bold"),bg="crimson",fg="white").grid(row=4,column=1,pady=10,sticky="nsew")
            Clearbtn =Button(User_Frame, text="Clear",width=10,command=self.clear,font=("times new roman",12,"bold"),bg="crimson",fg="white").grid(row=5,column=1,pady=10,sticky="nsew")
            
            ####  search ###########
            
            lbl_Search=Label(User_Frame,text="Search BY",bg="crimson",fg="white",font=("times new roman",18,"bold"))
            lbl_Search.grid(row=6,column=0,pady=10,padx=15,sticky="w")

            combo_Search=ttk.Combobox(User_Frame,textvariable=self.search_by,width=10,font=("times new roman",13,"bold"),state='readonly')
            combo_Search['values']=("Name", "Roll No")
            combo_Search.grid(row=6,column=1,pady=10,padx=15)

            txt_Search=Entry(User_Frame,textvariable=self.search_txt,width=10,font=("times new roman",12,"bold"),bd=5,relief=GROOVE)
            txt_Search.grid(row=6,column=2,pady=10,padx=15,sticky="w")

            Searchbtn=Button(User_Frame,text="Search",width=8,command=self.search_user,pady=5).grid(row=7,column=0,padx=2,pady=10)
            Showallbtn=Button(User_Frame,text="Show All",width=8,command=self.fetch_data,pady=5).grid(row=7,column=1,padx=2,pady=10)
            button=tk.Button(User_Frame, text="Back", width=10, command=lambda: controller.show_frame("Options"),
                             font=("times new roman", 14, "bold"), bg="light coral", fg="white").grid(row=7, column=2,
                                                                                                      pady=10)

            ##########################detail frame#######################

            # Detail_Frame=Frame(self,bd=4,relief=GROOVE,bg="white")
            # Detail_Frame.place(x=160,y=170,width=300,height=530)



            #################Table Frame#############################

            Table_Frame=Frame(self,bd=4,relief=RIDGE,bg="crimson")
            Table_Frame.place(x=160,y=170,width=300,height=530)

            scroll_x=Scrollbar(Table_Frame,orient=HORIZONTAL)
            scroll_y=Scrollbar(Table_Frame,orient=VERTICAL)

            self.User_Table=ttk.Treeview(Table_Frame,columns=("Name","Roll No"),xscrollcommand=scroll_x.set,yscrollcommand=scroll_y.set)
            scroll_x.pack(side=BOTTOM,fill=X)
            scroll_y.pack(side=RIGHT,fill=Y)
            scroll_x.config(command=self.User_Table.xview)
            scroll_y.config(command=self.User_Table.yview)
            self.User_Table.heading("Name",text="Name")
            self.User_Table.heading("Roll No",text="Roll No")

            self.User_Table['show']='headings'

            self.User_Table.column("Name",width=50)
            self.User_Table.column("Roll No",width=50)
            
            self.User_Table.pack(fill=BOTH,expand=1)

            self.User_Table.bind("<ButtonRelease-1>",self.get_cursor)
            self.fetch_data()


        def add_behaviour(self):
            global u_p
            con=cx_Oracle.connect('system/yash@localhost:1521/system')
            cur=con.cursor()
            cur.execute("select roll_no, teacher_name from response")
            stu_data = cur.fetchall()
            print(stu_data)
            if self.Behaviour.get()=="Friendly":
                x=10
            elif self.Behaviour.get() == "Casual":
                x = 8
            elif self.Behaviour.get() == "Introvert":
                x = 6
            elif self.Behaviour.get() == "Aggresive":
                x = 2
            else:
                x = -2
            
            if ((self.stu_roll.get(), u_p[0]) in stu_data):
                cur.execute("update response set behaviour=:1 where teacher_name=:2 and roll_no=:3",(
                                                                                                x,
                                                                                                u_p[0],
                                                                                                self.stu_roll.get()
                                                                                                ))
            else:
                cur.execute("insert into response(behaviour, student, roll_no, teacher_name) values(:1, :2, :3, :4)",(
                                                                                                x,
                                                                                                self.stu_name.get(),
                                                                                                self.stu_roll.get(),
                                                                                                u_p[0]
                                                                                                ))
            

            con.commit()
            self.fetch_data()
            self.clear()
            con.close()
            messagebox.showinfo("Record","Record Added...!!!")
        
            
        def fetch_data(self):
            con=cx_Oracle.connect('system/yash@localhost:1521/system')
            cur=con.cursor()

            cur.execute("select name, roll_no from stud order by roll_no")
            rows=cur.fetchall()
            self.User_Table.delete(*self.User_Table.get_children())
            if len(rows)!=0:
                for row in rows:
                    self.User_Table.insert('',END,values=row)
                con.commit()
            con.close()

        def clear(self):
            self.Behaviour.set('')
            self.stu_name.set('')
            self.stu_roll.set('')
            
        def get_cursor(self,ev):
            cursor_row=self.User_Table.focus()
            contents=self.User_Table.item(cursor_row)
            row=(contents['values'])
            self.stu_name.set(row[0])
            self.stu_roll.set(row[1])

        def search_user(self):
            con=cx_Oracle.connect('system/yash@localhost:1521/system')
            cur=con.cursor()

            cur.execute("select * from stud where "+str(self.search_by.get())+" LIKE '%"+str(self.search_txt.get())+"%'")
            rows=cur.fetchall()
            self.User_Table.delete(*self.User_Table.get_children())
            if len(rows)!=0:
                for row in rows:
                    self.User_Table.insert('',END,values=row)
                con.commit()
            con.close()


####################### Ethics ################################

    class Ethics(tk.Frame):
        def __init__(self, parent, controller):
            tk.Frame.__init__(self, parent)
            self.controller = controller

            self.bg_icon=ImageTk.PhotoImage(file="43629.jpg")
            bg_lbl=tk.Label(self,image=self.bg_icon).pack()
            title=tk.Label(self,text="ETHICS TOWARDS TEACHERS",font=("times new roman",38,"bold"),bg="yellow",fg="red",bd=10,relief=GROOVE)
            title.place(x=0,y=0,relwidth=1)

            self.stu_name=StringVar()
            self.stu_roll=StringVar()
            self.Ethics= StringVar()
            self.search_by=tk.StringVar()
            self.search_txt=tk.StringVar()


            User_Frame=Frame(self,bd=4,relief=GROOVE,bg="white")
            User_Frame.place(x=690,y=170,width=580,height=440)

            
            lbl_Name=Label(User_Frame,text="Name",bg="crimson",fg="white",font=("times new roman",20,"bold"))
            lbl_Name.grid(row=0,column=0,pady=10,padx=20,sticky="w")

            txt_Name=Entry(User_Frame,textvariable=self.stu_name,font=("times new roman",13,"bold"),bd=5,relief=GROOVE)
            txt_Name.grid(row=0,column=1,pady=10,padx=20,sticky="w")
            
            lbl_Roll_no=Label(User_Frame,text="Roll No.",bg="crimson",fg="white",font=("times new roman",20,"bold"))
            lbl_Roll_no.grid(row=1,column=0,pady=10,padx=20,sticky="w")

            txt_Roll_no=Entry(User_Frame,textvariable=self.stu_roll,font=("times new roman",13,"bold"),bd=5,relief=GROOVE)
            txt_Roll_no.grid(row=1,column=1,pady=10,padx=20,sticky="w")

            lbl_Ethics=Label(User_Frame,text="Ethics",bg="crimson",fg="white",font=("times new roman",18,"bold"))
            lbl_Ethics.grid(row=2,column=0,pady=10,padx=15,sticky="w")
            
            combo_Ethics=ttk.Combobox(User_Frame,textvariable=self.Ethics,width=10,font=("times new roman",13,"bold"),state='readonly')
            combo_Ethics['values']=("Respectful","Compassionate Nature", "Casual", "Disrespectful")
            combo_Ethics.grid(row=2,column=1,pady=10,padx=15)



            
            #######################button####################

            Addbtn=tk.Button(User_Frame, text="Add",width=10,command=self.add_ethics,font=("times new roman",12,"bold"),bg="crimson",fg="white").grid(row=4,column=1,pady=10,sticky="nsew")
            Clearbtn =Button(User_Frame, text="Clear",width=10,command=self.clear,font=("times new roman",12,"bold"),bg="crimson",fg="white").grid(row=5,column=1,pady=10,sticky="nsew")
            
            ####  search ###########
            
            lbl_Search=Label(User_Frame,text="Search BY",bg="crimson",fg="white",font=("times new roman",18,"bold"))
            lbl_Search.grid(row=6,column=0,pady=10,padx=15,sticky="w")

            combo_Search=ttk.Combobox(User_Frame,textvariable=self.search_by,width=10,font=("times new roman",13,"bold"),state='readonly')
            combo_Search['values']=("Name", "Roll No")
            combo_Search.grid(row=6,column=1,pady=10,padx=15)

            txt_Search=Entry(User_Frame,textvariable=self.search_txt,width=10,font=("times new roman",12,"bold"),bd=5,relief=GROOVE)
            txt_Search.grid(row=6,column=2,pady=10,padx=15,sticky="w")

            Searchbtn=Button(User_Frame,text="Search",width=8,command=self.search_user,pady=5).grid(row=7,column=0,padx=2,pady=10)
            Showallbtn=Button(User_Frame,text="Show All",width=8,command=self.fetch_data,pady=5).grid(row=7,column=1,padx=2,pady=10)
            button=tk.Button(User_Frame, text="Back", width=10, command=lambda: controller.show_frame("Options"),
                             font=("times new roman", 14, "bold"), bg="light coral", fg="white").grid(row=7, column=2,
                                                                                                      pady=10)

            ##########################detail frame#######################

            # Detail_Frame=Frame(self,bd=4,relief=GROOVE,bg="white")
            # Detail_Frame.place(x=160,y=170,width=300,height=530)



            #################Table Frame#############################

            Table_Frame=Frame(self,bd=4,relief=RIDGE,bg="crimson")
            Table_Frame.place(x=160,y=170,width=300,height=530)

            scroll_x=Scrollbar(Table_Frame,orient=HORIZONTAL)
            scroll_y=Scrollbar(Table_Frame,orient=VERTICAL)

            self.User_Table=ttk.Treeview(Table_Frame,columns=("Name","Roll No"),xscrollcommand=scroll_x.set,yscrollcommand=scroll_y.set)
            scroll_x.pack(side=BOTTOM,fill=X)
            scroll_y.pack(side=RIGHT,fill=Y)
            scroll_x.config(command=self.User_Table.xview)
            scroll_y.config(command=self.User_Table.yview)
            self.User_Table.heading("Name",text="Name")
            self.User_Table.heading("Roll No",text="Roll No")

            self.User_Table['show']='headings'

            self.User_Table.column("Name",width=50)
            self.User_Table.column("Roll No",width=50)
            
            self.User_Table.pack(fill=BOTH,expand=1)

            self.User_Table.bind("<ButtonRelease-1>",self.get_cursor)
            self.fetch_data()


        def add_ethics(self):
            global u_p
            con=cx_Oracle.connect('system/yash@localhost:1521/system')
            cur=con.cursor()
            cur.execute("select roll_no, teacher_name from response")
            stu_data = cur.fetchall()
            print(stu_data)

            if self.Ethics.get()=="Respectful":
                x = 10
            elif self.Ethics.get() == "Compassionate Nature":
                x = 8
            elif self.Ethics.get() == "Casual":
                x = 3
            else:
                x = -5
            
            if ((self.stu_roll.get(), u_p[0]) in stu_data):
                cur.execute("update response set ethics=:1 where teacher_name=:2 and roll_no=:3",(
                                                                                                x,
                                                                                                u_p[0],
                                                                                                self.stu_roll.get()
                                                                                                ))
            else:
                cur.execute("insert into response(ethics, student, roll_no, teacher_name) values(:1, :2, :3, :4)",(
                                                                                                x,
                                                                                                self.stu_name.get(),
                                                                                                self.stu_roll.get(),
                                                                                                u_p[0]
                                                                                                ))
            

            con.commit()
            self.fetch_data()
            self.clear()
            con.close()
            messagebox.showinfo("Record","Record Added...!!!")
            
        def fetch_data(self):
            con=cx_Oracle.connect('system/yash@localhost:1521/system')
            cur=con.cursor()

            cur.execute("select name, roll_no from stud order by roll_no")
            rows=cur.fetchall()
            self.User_Table.delete(*self.User_Table.get_children())
            if len(rows)!=0:
                for row in rows:
                    self.User_Table.insert('',END,values=row)
                con.commit()
            con.close()

        def clear(self):
            self.Ethics.set('')
            self.stu_roll.set('')
            self.stu_name.set('')

        def get_cursor(self,ev):
            cursor_row=self.User_Table.focus()
            contents=self.User_Table.item(cursor_row)
            row=(contents['values'])
            self.stu_name.set(row[0])
            self.stu_roll.set(row[1])

        def search_user(self):
            con=cx_Oracle.connect('system/yash@localhost:1521/system')
            cur=con.cursor()

            cur.execute("select * from stud where "+str(self.search_by.get())+" LIKE '%"+str(self.search_txt.get())+"%'")
            rows=cur.fetchall()
            self.User_Table.delete(*self.User_Table.get_children())
            if len(rows)!=0:
                for row in rows:
                    self.User_Table.insert('',END,values=row)
                con.commit()
            con.close()


####################### English ################################

    class English(tk.Frame):
        def __init__(self, parent, controller):
            tk.Frame.__init__(self, parent)
            self.controller = controller

            self.bg_icon=ImageTk.PhotoImage(file="43629.jpg")
            bg_lbl=tk.Label(self,image=self.bg_icon).pack()
            title=tk.Label(self,text="SPOKEN ENGLISH",font=("times new roman",38,"bold"),bg="yellow",fg="red",bd=10,relief=GROOVE)
            title.place(x=0,y=0,relwidth=1)

            self.stu_name=StringVar()
            self.stu_roll=StringVar()
            self.Spoken= StringVar()
            self.search_by=tk.StringVar()
            self.search_txt=tk.StringVar()


            User_Frame=Frame(self,bd=4,relief=GROOVE,bg="white")
            User_Frame.place(x=690,y=170,width=580,height=440)

            
            lbl_Name=Label(User_Frame,text="Name",bg="crimson",fg="white",font=("times new roman",20,"bold"))
            lbl_Name.grid(row=0,column=0,pady=10,padx=20,sticky="w")

            txt_Name=Entry(User_Frame,textvariable=self.stu_name,font=("times new roman",13,"bold"),bd=5,relief=GROOVE)
            txt_Name.grid(row=0,column=1,pady=10,padx=20,sticky="w")
            
            lbl_Roll_no=Label(User_Frame,text="Roll No.",bg="crimson",fg="white",font=("times new roman",20,"bold"))
            lbl_Roll_no.grid(row=1,column=0,pady=10,padx=20,sticky="w")

            txt_Roll_no=Entry(User_Frame,textvariable=self.stu_roll,font=("times new roman",13,"bold"),bd=5,relief=GROOVE)
            txt_Roll_no.grid(row=1,column=1,pady=10,padx=20,sticky="w")

            lbl_Spoken=Label(User_Frame,text="English Spoken",bg="crimson",fg="white",font=("times new roman",18,"bold"))
            lbl_Spoken.grid(row=2,column=0,pady=10,padx=15,sticky="w")
            
            combo_Spoken=ttk.Combobox(User_Frame,textvariable=self.Spoken,width=10,font=("times new roman",13,"bold"),state='readonly')
            combo_Spoken['values']=("Excellent","Good", "Average", "Poor")
            combo_Spoken.grid(row=2,column=1,pady=10,padx=15)



            
            #######################button####################

            Addbtn=tk.Button(User_Frame, text="Add",width=10,command=self.add_course,font=("times new roman",12,"bold"),bg="crimson",fg="white").grid(row=4,column=1,pady=10,sticky="nsew")
            Clearbtn =Button(User_Frame, text="Clear",width=10,command=self.clear,font=("times new roman",12,"bold"),bg="crimson",fg="white").grid(row=5,column=1,pady=10,sticky="nsew")
            
            ####  search ###########
            
            lbl_Search=Label(User_Frame,text="Search BY",bg="crimson",fg="white",font=("times new roman",18,"bold"))
            lbl_Search.grid(row=6,column=0,pady=10,padx=15,sticky="w")

            combo_Search=ttk.Combobox(User_Frame,textvariable=self.search_by,width=10,font=("times new roman",13,"bold"),state='readonly')
            combo_Search['values']=("Name", "Roll No")
            combo_Search.grid(row=6,column=1,pady=10,padx=15)

            txt_Search=Entry(User_Frame,textvariable=self.search_txt,width=10,font=("times new roman",12,"bold"),bd=5,relief=GROOVE)
            txt_Search.grid(row=6,column=2,pady=10,padx=15,sticky="w")

            Searchbtn=Button(User_Frame,text="Search",width=8,command=self.search_user,pady=5).grid(row=7,column=0,padx=2,pady=10)
            Showallbtn=Button(User_Frame,text="Show All",width=8,command=self.fetch_data,pady=5).grid(row=7,column=1,padx=2,pady=10)
            button=tk.Button(User_Frame, text="Back", width=10, command=lambda: controller.show_frame("Options"),
                             font=("times new roman", 14, "bold"), bg="light coral", fg="white").grid(row=7, column=2,
                                                                                                      pady=10)

            ##########################detail frame#######################

            # Detail_Frame=Frame(self,bd=4,relief=GROOVE,bg="white")
            # Detail_Frame.place(x=160,y=170,width=300,height=530)



            #################Table Frame#############################

            Table_Frame=Frame(self,bd=4,relief=RIDGE,bg="crimson")
            Table_Frame.place(x=160,y=170,width=300,height=530)

            scroll_x=Scrollbar(Table_Frame,orient=HORIZONTAL)
            scroll_y=Scrollbar(Table_Frame,orient=VERTICAL)

            self.User_Table=ttk.Treeview(Table_Frame,columns=("Name","Roll No"),xscrollcommand=scroll_x.set,yscrollcommand=scroll_y.set)
            scroll_x.pack(side=BOTTOM,fill=X)
            scroll_y.pack(side=RIGHT,fill=Y)
            scroll_x.config(command=self.User_Table.xview)
            scroll_y.config(command=self.User_Table.yview)
            self.User_Table.heading("Name",text="Name")
            self.User_Table.heading("Roll No",text="Roll No")

            self.User_Table['show']='headings'

            self.User_Table.column("Name",width=50)
            self.User_Table.column("Roll No",width=50)
            
            self.User_Table.pack(fill=BOTH,expand=1)

            self.User_Table.bind("<ButtonRelease-1>",self.get_cursor)
            self.fetch_data()


        def add_course(self):
            global u_p
            con=cx_Oracle.connect('system/yash@localhost:1521/system')
            cur=con.cursor()
            cur.execute("select roll_no, teacher_name from response")
            stu_data = cur.fetchall()
            print(stu_data)

            if self.Spoken.get()=="Excellent":
                x = 10
            elif self.Spoken.get() == "Good":
                x = 8
            elif self.Spoken.get() == "Average":
                x = 5
            else:
                x = 2
            
            if ((self.stu_roll.get(), u_p[0]) in stu_data):
                cur.execute("update response set english=:1 where teacher_name=:2 and roll_no=:3",(
                                                                                                x,
                                                                                                u_p[0],
                                                                                                self.stu_roll.get()
                                                                                                ))
            else:
                cur.execute("insert into response(english, student, roll_no, teacher_name) values(:1, :2, :3, :4)",(
                                                                                                x,
                                                                                                self.stu_name.get(),
                                                                                                self.stu_roll.get(),
                                                                                                u_p[0]
                                                                                                ))
            

            con.commit()
            self.fetch_data()
            self.clear()
            con.close()
            messagebox.showinfo("Record","Record Added...!!!")
            
        def fetch_data(self):
            con=cx_Oracle.connect('system/yash@localhost:1521/system')
            cur=con.cursor()

            cur.execute("select name, roll_no from stud order by roll_no")
            rows=cur.fetchall()
            self.User_Table.delete(*self.User_Table.get_children())
            if len(rows)!=0:
                for row in rows:
                    self.User_Table.insert('',END,values=row)
                con.commit()
            con.close()

        def clear(self):
            self.Spoken.set('')
            self.stu_name.set('')
            self.stu_roll.set('')
            
        def get_cursor(self,ev):
            cursor_row=self.User_Table.focus()
            contents=self.User_Table.item(cursor_row)
            row=(contents['values'])
            self.stu_name.set(row[0])
            self.stu_roll.set(row[1])

        def search_user(self):
            con=cx_Oracle.connect('system/yash@localhost:1521/system')
            cur=con.cursor()

            cur.execute("select * from stud where "+str(self.search_by.get())+" LIKE '%"+str(self.search_txt.get())+"%'")
            rows=cur.fetchall()
            self.User_Table.delete(*self.User_Table.get_children())
            if len(rows)!=0:
                for row in rows:
                    self.User_Table.insert('',END,values=row)
                con.commit()
            con.close()



####################### Curriculam ################################

    class Curriculam(tk.Frame):
        def __init__(self, parent, controller):
            tk.Frame.__init__(self, parent)
            self.controller = controller

            self.bg_icon=ImageTk.PhotoImage(file="43629.jpg")
            bg_lbl=tk.Label(self,image=self.bg_icon).pack()
            title=tk.Label(self,text="EXTRA CURRICULAM",font=("times new roman",38,"bold"),bg="yellow",fg="red",bd=10,relief=GROOVE)
            title.place(x=0,y=0,relwidth=1)

            self.stu_name=StringVar()
            self.stu_roll=StringVar()
            self.sports= StringVar()
            self.cultural= StringVar()
            self.spoken= StringVar()
            self.search_by=tk.StringVar()
            self.search_txt=tk.StringVar()


            User_Frame=Frame(self,bd=4,relief=GROOVE,bg="white")
            User_Frame.place(x=690,y=170,width=580,height=530)

            
            lbl_Name=Label(User_Frame,text="Name",bg="crimson",fg="white",font=("times new roman",20,"bold"))
            lbl_Name.grid(row=0,column=0,pady=10,padx=20,sticky="w")

            txt_Name=Entry(User_Frame,textvariable=self.stu_name,font=("times new roman",13,"bold"),bd=5,relief=GROOVE)
            txt_Name.grid(row=0,column=1,pady=10,padx=20,sticky="w")
            
            lbl_Roll_no=Label(User_Frame,text="Roll No.",bg="crimson",fg="white",font=("times new roman",20,"bold"))
            lbl_Roll_no.grid(row=1,column=0,pady=10,padx=20,sticky="w")

            txt_Roll_no=Entry(User_Frame,textvariable=self.stu_roll,font=("times new roman",13,"bold"),bd=5,relief=GROOVE)
            txt_Roll_no.grid(row=1,column=1,pady=10,padx=20,sticky="w")

            lbl_Sports_Curriculam=Label(User_Frame,text="Sports",bg="crimson",fg="white",font=("times new roman",18,"bold"))
            lbl_Sports_Curriculam.grid(row=2,column=0,pady=10,padx=15,sticky="w")
            
            combo_Sports_Curriculam=ttk.Combobox(User_Frame,textvariable=self.sports,width=10,font=("times new roman",13,"bold"),state='readonly')
            combo_Sports_Curriculam['values']=("Excellent","Good", "Average", "Poor")
            combo_Sports_Curriculam.grid(row=2,column=1,pady=10,padx=15)

            lbl_Drama_Curriculam=Label(User_Frame,text="Cultural",bg="crimson",fg="white",font=("times new roman",18,"bold"))
            lbl_Drama_Curriculam.grid(row=3,column=0,pady=10,padx=15,sticky="w")
            
            combo_Drama_Curriculam=ttk.Combobox(User_Frame,textvariable=self.cultural,width=10,font=("times new roman",13,"bold"),state='readonly')
            combo_Drama_Curriculam['values']=("Excellent","Good", "Average", "Poor")
            combo_Drama_Curriculam.grid(row=3,column=1,pady=10,padx=15)

            lbl_Vocal_Curriculam=Label(User_Frame,text="Public Speaking",bg="crimson",fg="white",font=("times new roman",18,"bold"))
            lbl_Vocal_Curriculam.grid(row=4,column=0,pady=10,padx=15,sticky="w")
            
            combo_Vocal_Curriculam=ttk.Combobox(User_Frame,textvariable=self.spoken,width=10,font=("times new roman",13,"bold"),state='readonly')
            combo_Vocal_Curriculam['values']=("Excellent","Good", "Average", "Poor")
            combo_Vocal_Curriculam.grid(row=4,column=1,pady=10,padx=15)



            
            #######################button####################

            Addbtn=tk.Button(User_Frame, text="Add",width=10,command=self.add_course,font=("times new roman",12,"bold"),bg="crimson",fg="white").grid(row=5,column=1,pady=10,sticky="nsew")
            Clearbtn =Button(User_Frame, text="Clear",width=10,command=self.clear,font=("times new roman",12,"bold"),bg="crimson",fg="white").grid(row=6,column=1,pady=10,sticky="nsew")
            
            ####  search ###########
            
            lbl_Search=Label(User_Frame,text="Search BY",bg="crimson",fg="white",font=("times new roman",18,"bold"))
            lbl_Search.grid(row=7,column=0,pady=10,padx=15,sticky="w")

            combo_Search=ttk.Combobox(User_Frame,textvariable=self.search_by,width=10,font=("times new roman",13,"bold"),state='readonly')
            combo_Search['values']=("Name", "Roll_No")
            combo_Search.grid(row=7,column=1,pady=10,padx=15)

            txt_Search=Entry(User_Frame,textvariable=self.search_txt,width=10,font=("times new roman",12,"bold"),bd=5,relief=GROOVE)
            txt_Search.grid(row=7,column=2,pady=10,padx=15,sticky="w")

            Searchbtn=Button(User_Frame,text="Search",width=8,command=self.search_user,pady=5).grid(row=8,column=0,padx=2,pady=10)
            Showallbtn=Button(User_Frame,text="Show All",width=8,command=self.fetch_data,pady=5).grid(row=8,column=1,padx=2,pady=10)
            button=tk.Button(User_Frame, text="Back", width=10, command=lambda: controller.show_frame("Options"),
                             font=("times new roman", 14, "bold"), bg="light coral", fg="white").grid(row=8, column=2,
                                                                                                      pady=10)

            ##########################detail frame#######################

            # Detail_Frame=Frame(self,bd=4,relief=GROOVE,bg="white")
            # Detail_Frame.place(x=160,y=170,width=300,height=530)



            #################Table Frame#############################

            Table_Frame=Frame(self,bd=4,relief=RIDGE,bg="crimson")
            Table_Frame.place(x=160,y=170,width=300,height=530)

            scroll_x=Scrollbar(Table_Frame,orient=HORIZONTAL)
            scroll_y=Scrollbar(Table_Frame,orient=VERTICAL)

            self.User_Table=ttk.Treeview(Table_Frame,columns=("Name","Roll No"),xscrollcommand=scroll_x.set,yscrollcommand=scroll_y.set)
            scroll_x.pack(side=BOTTOM,fill=X)
            scroll_y.pack(side=RIGHT,fill=Y)
            scroll_x.config(command=self.User_Table.xview)
            scroll_y.config(command=self.User_Table.yview)
            self.User_Table.heading("Name",text="Name")
            self.User_Table.heading("Roll No",text="Roll No")

            self.User_Table['show']='headings'

            self.User_Table.column("Name",width=50)
            self.User_Table.column("Roll No",width=50)
            
            self.User_Table.pack(fill=BOTH,expand=1)

            self.User_Table.bind("<ButtonRelease-1>",self.get_cursor)
            self.fetch_data()


        def add_course(self):
            global u_p
            con=cx_Oracle.connect('system/yash@localhost:1521/system')
            cur=con.cursor()
            cur.execute("select roll_no, teacher_name from response")
            stu_data = cur.fetchall()
            print(stu_data)

            if self.spoken.get()=="Excellent":
                x = 10
            elif self.spoken.get() == "Good":
                x = 8
            elif self.spoken.get() == "Average":
                x = 5
            else:
                x = 2
            
            if self.sports.get()=="Excellent":
                y = 10
            elif self.sports.get() == "Good":
                y = 8
            elif self.sports.get() == "Average":
                y = 5
            else:
                y = 2
            
            if self.cultural.get()=="Excellent":
                z = 10
            elif self.cultural.get() == "Good":
                z = 8
            elif self.cultural.get() == "Average":
                z = 5
            else:
                z = 2
            
            x = x + y + z

            if ((self.stu_roll.get(), u_p[0]) in stu_data):
                cur.execute("update response set extra=:1 where teacher_name=:2 and roll_no=:3",(
                                                                                                x,
                                                                                                u_p[0],
                                                                                                self.stu_roll.get()
                                                                                                ))
            else:
                cur.execute("insert into response(extra, student, roll_no, teacher_name) values(:1, :2, :3, :4)",(
                                                                                                x,
                                                                                                self.stu_name.get(),
                                                                                                self.stu_roll.get(),
                                                                                                u_p[0]
                                                                                                ))
            

            con.commit()
            self.fetch_data()
            self.clear()
            con.close()
            messagebox.showinfo("Record","Record Added...!!!")
            
        def fetch_data(self):
            con=cx_Oracle.connect('system/yash@localhost:1521/system')
            cur=con.cursor()

            cur.execute("select name, roll_no from stud order by roll_no")
            rows=cur.fetchall()
            self.User_Table.delete(*self.User_Table.get_children())
            if len(rows)!=0:
                for row in rows:
                    self.User_Table.insert('',END,values=row)
                con.commit()
            con.close()

        def clear(self):
            self.stu_roll.set('')
            self.stu_name.set('')
            self.sports.set('')
            self.spoken.set('')
            self.cultural.set('')

            
        def get_cursor(self,ev):
            cursor_row=self.User_Table.focus()
            contents=self.User_Table.item(cursor_row)
            row=(contents['values'])
            self.stu_name.set(row[0])
            self.stu_roll.set(row[1])

        def search_user(self):
            con=cx_Oracle.connect('system/yash@localhost:1521/system')
            cur=con.cursor()

            cur.execute("select * from stud where "+str(self.search_by.get())+" LIKE '%"+str(self.search_txt.get())+"%'")
            rows=cur.fetchall()
            self.User_Table.delete(*self.User_Table.get_children())
            if len(rows)!=0:
                for row in rows:
                    self.User_Table.insert('',END,values=row)
                con.commit()
            con.close()


################################### Student Parent Login Page##############################
    class StuPar_LoginPage(tk.Frame):

        def __init__(self, parent, controller):
            tk.Frame.__init__(self, parent)
            self.controller = controller
            

            ##############ALL IMAGES########
            self.bg_icon=ImageTk.PhotoImage(file="43629.jpg")
            self.user_icon=PhotoImage(file="user.png")
            self.pass_icon=PhotoImage(file="pass.png")
            self.logo_icon=PhotoImage(file="logo.png")
            ######### variables############
            self.uname=StringVar()
            self.passw=StringVar()

            bg_lbl=tk.Label(self,image=self.bg_icon).pack()
            title=tk.Label(self,text="Welcome To Student/Parent Login System",font=("times new roman",40,"bold"),bg="yellow",fg="red",bd=10,relief=GROOVE)
            title.place(x=0,y=0,relwidth=1)

            Login_Frame=tk.Frame(self,bg="white")
            Login_Frame.place(x=30,y=120)

            logolbl=tk.Label(Login_Frame,image=self.logo_icon,bd=0).grid(row=0,columnspan=2,pady=20)

            lbluser=tk.Label(Login_Frame,text="Username",image=self.user_icon,compound=LEFT,font=("times new roman",20,"bold"),bg="white").grid(rows=1,column=0,padx=20,pady=10)
            txtuser=tk.Entry(Login_Frame,bd=5,textvariable=self.uname,relief=GROOVE,font=("",15)).grid(row=1,column=1,padx=20)

            lblpass=tk.Label(Login_Frame,text="Password",image=self.pass_icon,compound=LEFT,font=("times new roman",20,"bold"),bg="white").grid(rows=2,column=0,padx=20,pady=10)
            txtpass=tk.Entry(Login_Frame,bd=5,textvariable=self.passw,relief=GROOVE,font=("",15),show="*").grid(row=2,column=1,padx=20)

            btn_log=tk.Button(Login_Frame,text="Login",width=10,command=self.login,font=("times new roman",14,"bold"),bg="yellow",fg="red").grid(row=3,column=1,pady=10)
            btn_log=tk.Button(Login_Frame,text="Back",width=10,command=lambda: controller.show_frame("StartPage"),font=("times new roman",14,"bold"),bg="yellow",fg="red").grid(row=4,column=1,pady=10)





        def login(self):
            con=cx_Oracle.connect('system/yash@localhost:1521/system')
            cur=con.cursor()

            cur.execute("select username,password from userss where user_type = 'Student'")
            rows=cur.fetchall()
            print(rows)
            
            if self.uname.get()=="" or self.passw.get()=="":
                messagebox.showerror("Error","All fields are required!!!")
            elif (self.uname.get(),self.passw.get()) in rows:
                 messagebox.showinfo("Successfull",f"welcome {self.uname.get()}")
                 global s_p
                 s_p=[self.uname.get(),self.passw.get()]
                 self.passw.set('')
                 self.uname.set('')
                 con.commit()
                 con.close()
                 self.controller.show_frame("StuPar_Report")
                 
            else:
                messagebox.showerror("Error","Invalid Username or Password!!!")

###################################### Report ##################################
    class StuPar_Report(tk.Frame):
        def __init__(self, parent, controller):
            tk.Frame.__init__(self, parent)
            self.controller = controller
            

            self.bg_icon=ImageTk.PhotoImage(file="bgg1.jpg")
            bg_lbl=tk.Label(self,image=self.bg_icon).pack()
            title=tk.Label(self,text="Result Details",font=("times new roman",40,"bold"),bg="yellow",fg="red",bd=10,relief=GROOVE)
            title.place(x=0,y=0,relwidth=1)

            self.search_by=tk.StringVar()
            self.search_txt=tk.StringVar()
            
            ##########################detail frame#######################

            Detail_Frame=Frame(self,bd=4,relief=GROOVE,bg="white")
            Detail_Frame.place(x=230,y=145,width=1000,height=600)

            lbl_Search=Label(Detail_Frame,text="Search BY",bg="crimson",fg="white",font=("times new roman",20,"bold"))
            lbl_Search.grid(row=0,column=0,pady=10,padx=20,sticky="w")

            combo_Search=ttk.Combobox(Detail_Frame,textvariable=self.search_by,width=10,font=("times new roman",13,"bold"),state='readonly')
            combo_Search['values']=("Roll_No")
            combo_Search.grid(row=0,column=1,pady=10,padx=20)

            txt_Search=Entry(Detail_Frame,textvariable=self.search_txt,width=20,font=("times new roman",10,"bold"),bd=5,relief=GROOVE)
            txt_Search.grid(row=0,column=2,pady=10,padx=20,sticky="w")

            Searchbtn=Button(Detail_Frame,text="Search",width=10,command=self.search_data,pady=5).grid(row=0,column=3,padx=10,pady=10)
            Showallbtn=Button(Detail_Frame,text="Show All",width=10,command=self.fetch_data,pady=5).grid(row=0,column=4,padx=10,pady=10)



            #################Table Frame#############################


            Table_Frame=Frame(Detail_Frame,bd=4,relief=RIDGE,bg="crimson")
            Table_Frame.place(x=10,y=60,width=970,height=495)

            scroll_x=Scrollbar(Table_Frame,orient=HORIZONTAL)
            scroll_y=Scrollbar(Table_Frame,orient=VERTICAL)

            col ="Roll_no","Attendance","Attentive","Uniform","Behaviour","Ethics","English","Extra"
            self.Result_Table=ttk.Treeview(Table_Frame,columns=col,xscrollcommand=scroll_x.set,yscrollcommand=scroll_y.set)
            scroll_x.pack(side=BOTTOM,fill=X)
            scroll_y.pack(side=RIGHT,fill=Y)
            scroll_x.config(command=self.Result_Table.xview)
            scroll_y.config(command=self.Result_Table.yview)
          #  self.fetch_data()
            #self.Result_Table.heading("Student_name",text="STUDENT NAME")
            self.Result_Table.heading("Roll_no",text="Roll No.")
            self.Result_Table.heading("Attendance",text="Attendance")
            self.Result_Table.heading("Attentive",text="Attentive")
            self.Result_Table.heading("Uniform",text="Uniform")
            self.Result_Table.heading("Behaviour",text="Behaviour")
            self.Result_Table.heading("Ethics",text="Ethics")
            self.Result_Table.heading("English",text="English")
            self.Result_Table.heading("Extra",text="Extra")

            self.Result_Table['show']='headings'

            #self.Result_Table.column("Student_name",width=120)
            self.Result_Table.column("Roll_no",width=120)
            self.Result_Table.column("Attendance",width=120)
            self.Result_Table.column("Attentive",width=120)
            self.Result_Table.column("Uniform",width=120)
            self.Result_Table.column("Behaviour",width=120)
            self.Result_Table.column("Ethics",width=150)
            self.Result_Table.column("English",width=120)
            self.Result_Table.column("Extra",width=120)

            self.Result_Table.pack(fill=BOTH,expand=1)
            #self.Result_Table.bind("<ButtonRelease-1>",self.get_cursor)
            self.fetch_data()

        def fetch_data(self):
            con=cx_Oracle.connect('system/yash@localhost:1521/system')
            cur=con.cursor()
            global s_p
            cur.execute("select roll_no,sum(attendance),sum(attentive),sum(uniform),sum(behaviour),sum(ethics),sum(english),sum(extra) from response group by roll_no")
            rows=cur.fetchall()
            print(rows)
            self.Result_Table.delete(*self.Result_Table.get_children())
            if len(rows)!=0:
                self.Result_Table.delete(*self.Result_Table.get_children())
                for row in rows:
                    self.Result_Table.insert('',END,values=row)
            con.commit()
            con.close()

        
        
        def search_data(self):
            con=cx_Oracle.connect('system/yash@localhost:1521/system')
            cur=con.cursor()

            cur.execute("select * from response where "+str(self.search_by.get())+" LIKE '%"+str(self.search_txt.get())+"%'")
            rows=cur.fetchall()
            self.Result_Table.delete(*self.Result_Table.get_children())
            if len(rows)!=0:
                for row in rows:
                    self.Result_Table.insert('',END,values=row)
                con.commit()
            con.close()

    app = SampleApp()
    app.title("EXAM MANAGEMENT SYSTEM")
    app.geometry("1366x768+0+0")
    app.mainloop()


main()