from tkinter import *
from PIL import Image,ImageTk
from tkinter import ttk
from tkcalendar import Calendar,DateEntry
from tkinter import messagebox
from tkinter import filedialog
from pathlib import Path
import random
import mysql.connector


class Cus_win:
    def __init__(self,root):
        self.root = root
        self.root.title("Hospital Management System")
        self.root.geometry("1295x500+230+220")
    
        lbl_title =Label(self.root,text="Add customer details", font=("times new roman",40,"bold"),bg = "black",fg = "white",bd = 4, relief= RIDGE)
        lbl_title.place(x = 0,y = 0,width = 1295,height=50)


        labelframeleft = LabelFrame(self.root,bd = 2,relief= RIDGE,text= "Customer Details",font=("times new roman",12,"bold"),padx= 2)
        labelframeleft.place(x=5, y= 50,width= 425,height=490)

        #============variable==============#
        self.var_Ref = StringVar()
        x = random.randint(100,999)
        self.var_Ref.set(str(x))

        self.var_name = StringVar()
        self.var_Dob = StringVar()
        self.var_Mobile = StringVar()
        self.var_Gender = StringVar()
        self.var_ID_number = StringVar()
        self.var_Nationality = StringVar()
        #"Name","Dob","Mobile","Gender","ID number","Nationality"
        
        #============label and entry================#
        lbl_Ref = Label(labelframeleft,text= "Customer ref",font=("times new roman",12,"bold"),padx= 2,pady= 6)
        lbl_Ref.grid(row = 0, column= 0, sticky= W)

        enty_ref = Entry(labelframeleft,textvariable= self.var_Ref,width= 30,font=("times new roman",12,"bold"),state= "readonly")
        enty_ref.grid(row= 0,column= 1,sticky= W)


        lbl_cust_name = Label(labelframeleft,text = "Customer Name",font=("times new roman",12,"bold"),padx= 2,pady= 6)
        lbl_cust_name.grid(row= 1, column= 0,sticky=W)

        enty_ref = ttk.Entry(labelframeleft,textvariable=self.var_name,width = 29,font=("times new roman",13,"bold"))
        enty_ref.grid(row = 1,column= 1,sticky= W)

        lbl_Dob = Label(labelframeleft,text = "Day of birth",font=("times new roman",12,"bold"),padx= 2,pady= 4)
        lbl_Dob.grid(row=2,column= 0,sticky=W)        

        cal_Dob = DateEntry(labelframeleft,textvariable=self.var_Dob,width=30,bg="darkblue",fg="white",year=2023)
        cal_Dob.grid(row = 2,column = 1)
        
       

        lbl_cust_mobile = Label(labelframeleft,text = "Mobile",font=("times new roman",12,"bold"),padx= 2,pady= 6)
        lbl_cust_mobile.grid(row= 3, column= 0,sticky=W)

        enty_mobile = ttk.Entry(labelframeleft,textvariable= self.var_Mobile,width= 29,font=("times new roman",13,"bold"))
        enty_mobile.grid(row = 3,column= 1,sticky= W)

        lbl_gender = Label(labelframeleft,text = "Gender", font=("times new roman",12,"bold"),padx= 2,pady= 6)
        lbl_gender.grid(row= 4,column= 0,sticky=W)
        combo_gender = ttk.Combobox(labelframeleft,textvariable=self.var_Gender,font=("arial",12,"bold"),width=12,state = "readonly")
        combo_gender["value"] = ("Male","Female","Other")
        combo_gender.current(0)
        combo_gender.grid(row= 4,column= 1,sticky=W)


        lbl_idnum = Label(labelframeleft,text = "ID Number", font=("times new roman",12,"bold"),padx= 2,pady= 6)
        lbl_idnum.grid(row= 5,column= 0,sticky= W)

        enty_idnum = ttk.Entry(labelframeleft,textvariable=self.var_ID_number,font=("times new roman",12,"bold"),width= 32)
        enty_idnum.grid(row= 5,column=1,sticky=W)



        lbl_nationality = Label(labelframeleft, text= "Nationality",font=("times new roman",12,"bold"),padx= 2,pady= 6)
        lbl_nationality.grid(row= 6,column=0,sticky= W)

        enty_nationality = ttk.Entry(labelframeleft,textvariable=self.var_Nationality,font=("times new roman ",12,"bold"),width= 29)
        enty_nationality.grid(row=6,column= 1,sticky= W)


        #==========Button==============#
        btn_frm = Frame(labelframeleft,bd= 2, relief = FLAT)
        btn_frm.place(x = 0, y= 300 , width= 412,height= 40)


        btn_add = Button(btn_frm,text="Add",command=self.add_data,font=("arial",12,"bold"),bg="black",fg="white",width=7)
        btn_add.grid(column= 0, row= 0, padx= 6)
        
        btn_update = Button(btn_frm,text="Update", command = self.update,font=("arial",12,"bold"),bg="black",fg="white",width=7)
        btn_update.grid(column= 2, row= 0, padx= 6)
        
        btn_delete = Button(btn_frm,text="Delete",command = self.delete,font=("arial",12,"bold"),bg="black",fg="white",width=7)
        btn_delete.grid(column= 4, row= 0,padx= 6)
        
        btn_reset = Button(btn_frm,text= "Reset",command = self.reset,font=("Arial",12,"bold"),bg="black",fg = "white",width=7)
        btn_reset.grid(column= 5 , row = 0 ,padx = 6)


        #table frame search system#

        tabelframe = LabelFrame(self.root,bd = 2,relief= RIDGE,text= "Search",font=("times new roman",12,"bold"),padx= 2)
        tabelframe.place(x=435, y= 50,width= 860,height=490)

        
        lblsearchby = Label(tabelframe,font= ("arial",12,"bold"),text="Search by",bg= "black",fg= "white")
        lblsearchby.grid(row=0,column= 0,sticky=W, padx= 10)

        self.search_var = StringVar()
        combo_search = ttk.Combobox(tabelframe,textvariable= self.search_var,font=("arial",12,"bold"),width=12,state = "readonly")
        combo_search["value"] = ("ID_NUM","MOBILE","CUS_NAME")
        combo_search.current(0)
        combo_search.grid(row= 0,column= 1,sticky=W)

        self.text_search = StringVar()
        txtSearch = ttk.Entry(tabelframe,textvariable= self.text_search,font=("arial",12,"bold"),width=24)
        txtSearch.grid(row= 0,column= 2,padx= 10)

        btn_search = Button(tabelframe,text="Search",command= self.search,font=("arial",13,"bold"),bg="blue",fg="white")
        btn_search.grid(row= 0 , column= 3, padx= 10)

        bt_showall = Button(tabelframe,text="Show all",command= self.fetch_data,font=("arial",13,"bold"),bg="white",fg="blue")
        bt_showall.grid(row= 0,column= 4,padx= 5)

        #customer data table
        detail_table = Frame(tabelframe,bd= 2, relief = RIDGE)
        detail_table.place(x = 0, y= 50 , width= 860,height= 350)

        scroll_x =  ttk.Scrollbar(detail_table, orient= HORIZONTAL)
        scroll_y = ttk.Scrollbar(detail_table,orient = VERTICAL)

        self.Cust_Detail_Table = ttk.Treeview(detail_table, columns = ("Ref","Name","Dob","Mobile","Gender","ID number","Nationality"),xscrollcommand=scroll_x.set,yscrollcommand=scroll_y.set)
        scroll_x.pack(side = BOTTOM,fill= X)
        scroll_y.pack(side = RIGHT, fill= Y)        

        scroll_x.config(command=self.Cust_Detail_Table.xview)
        scroll_y.config(command=self.Cust_Detail_Table.yview)

        self.Cust_Detail_Table.heading("Ref",text = "Ref")
        self.Cust_Detail_Table.heading("Name",text= "Name")
        self.Cust_Detail_Table.heading("Dob",text= "Dob")
        self.Cust_Detail_Table.heading("Mobile",text= "Mobile")
        self.Cust_Detail_Table.heading("Gender",text= "Gender")
        self.Cust_Detail_Table.heading("ID number",text= "ID number")
        self.Cust_Detail_Table.heading("Nationality",text= "Nationality")

        self.Cust_Detail_Table["show"] = "headings"


        self.Cust_Detail_Table.column("Ref",width= 100)
        self.Cust_Detail_Table.column("Name",width= 100)
        self.Cust_Detail_Table.column("Dob",width= 100)
        self.Cust_Detail_Table.column("Mobile",width= 100)
        self.Cust_Detail_Table.column("Gender",width= 100)
        self.Cust_Detail_Table.column("ID number",width= 100)
        self.Cust_Detail_Table.column("Nationality",width= 100)
        
        self.Cust_Detail_Table.pack(fill= BOTH,expand=1)
        self.Cust_Detail_Table.bind("<ButtonRelease-1>",self.get_cursor)
        self.fetch_data()
    

    #add data to sql database
    def add_data(self):
        if self.var_ID_number.get() == "" or self.var_Nationality.get() == "":
            messagebox.showerror("Required","All fields are required",parent = self.root)   
        else:
            try:
                Ref = self.var_Ref.get()
                name = self.var_name.get()
                Dob = self.var_Dob.get()
                Mobile = self.var_Mobile.get() 
                Gender = self.var_Gender.get()
                ID_num = self.var_ID_number.get()
                Nationality = self.var_Nationality.get()         
                conn = mysql.connector.connect(host = "localhost",user="root",password = "Quan.1210",database ="hotel")
                my_cursor = conn.cursor()
                my_cursor.execute("insert into customer value(%s,%s,%s,%s,%s,%s,%s)",(
                                                                                    Ref,
                                                                                    name,
                                                                                    Dob,
                                                                                    Mobile,
                                                                                    Gender,
                                                                                    ID_num,
                                                                                    Nationality
                                                                                    ))
                
                conn.commit()
                self.fetch_data()
                conn.close()
                messagebox.showinfo("success","informations have been added ")
            except Exception as es:
                messagebox.showwarning("Warning",f"Something went wrong:{str(es)}",parent = self.root)
        Customer_data = Path(r"C:\Users\chumi\Documents\hotel-management-system\customerdata.dat")
        Customer_data.touch(exist_ok=True)  # will create file, if it exists will do nothing
        f = open(Customer_data, 'a')  # open file in write mode
        f.write("\nREF {0} : name: {1}  Dob: {2} Mobile: {3} Gender: {4} ID: {5} Nationality: {6}".format(Ref,name,Dob,Mobile,Gender,ID_num,Nationality))
        f.close()

    #fetching data to table
    def fetch_data(self):
        conn = mysql.connector.connect(host = "localhost",user="root",password = "Quan.1210",database ="hotel")
        my_cursor = conn.cursor()
        my_cursor.execute("select * from customer")
        rows = my_cursor.fetchall()
        if len(rows)!= 0:
            self.Cust_Detail_Table.delete(*self.Cust_Detail_Table.get_children())
            for i in rows:
                self.Cust_Detail_Table.insert("",END,value=i)
                conn.commit()
        conn.close()

    def get_cursor(self,event=""):
        cursor_row= self.Cust_Detail_Table.focus(),
        content =self.Cust_Detail_Table.item(cursor_row)
        row = content["values"]


        self.var_Ref.set(row[0]),
        self.var_name.set(row[1]),
        self.var_Dob.set(row[2]),
        self.var_Mobile.set(row[3]),
        self.var_Gender.set(row[4]),
        self.var_ID_number.set(row[5]),
        self.var_Nationality.set(row[6])


    def update(self):
        if self.var_Mobile.get() =="":
            messagebox.showerror("Error","Please enter mobile number",parent = self.root)
        else:
            conn = mysql.connector.connect(host = "localhost",user="root",password = "Quan.1210",database ="hotel" )
            my_cursor = conn.cursor()
            #execute command: write the variable name as the name in sql ex: customer name as CUS_NAME 
            my_cursor.execute("update customer set CUS_NAME =%s, DOB = %s, MOBILE = %s, GENDER = %s, ID_NUM = %s, NATIONALITY = %s where REF = %s",(
                self.var_name.get(),
                self.var_Dob.get(),
                self.var_Mobile.get(), 
                self.var_Gender.get(),
                self.var_ID_number.get(),
                self.var_Nationality.get(),
                self.var_Ref.get()))
        conn.commit()
        self.fetch_data()
        conn.close()
        messagebox.showinfo("Update","Customer details has be en updated successfully",parent = self.root)

    def delete(self):
        delete= messagebox.askyesno("Hotel Management System","Do you want to delete this customer",parent = self.root)
        if delete > 0: 
            conn = mysql.connector.connect(host = "localhost",user="root",password = "Quan.1210",database ="hotel" )
            my_cursor = conn.cursor()
            query = "delete from customer where REF= %s"
            value = (self.var_Ref.get(),)
            my_cursor.execute(query,value)
        else:
            if not delete:
                return
        conn.commit()
        self.fetch_data()
        conn.close()
    def reset(self):
        x = random.randint(100,999)
        self.var_Ref.set(x),
        self.var_name.set(""),
        self.var_Dob.set(""),
        self.var_Mobile.set(""),
        self.var_Gender.set(""),
        self.var_ID_number.set(""),
        self.var_Nationality.set("")


    def search(self):
            conn = mysql.connector.connect(host = "localhost",user="root",password = "Quan.1210",database ="hotel" )
            my_cursor = conn.cursor()
            #execute command: write the variable name as the name in sql ex: customer name as CUS_NAME 
            my_cursor.execute("select * from customer where "+str(self.search_var.get()) + " LIKE'%"+str(self.text_search.get()) + "%'")
            rows = my_cursor.fetchall()
            if len(rows) !=0:
                self.Cust_Detail_Table.delete(*self.Cust_Detail_Table.get_children())
                for i in rows:
                    self.Cust_Detail_Table.insert("",END,value = i) 
                conn.commit()   
            conn.close()
        


if __name__ == "__main__":
    root=Tk()
    object = Cus_win(root)
    root.mainloop()