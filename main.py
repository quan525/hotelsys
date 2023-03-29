from tkinter import*
from PIL import Image,ImageTk
from customer import Cus_win
class HotelManagementSystem:
    def __init__(self,root):
        self.root = root
        self.root.title("Hospital Management System")
        self.root.geometry("1550x800")
    #===============ist img ===============#
        img1 = Image.open(r"C:\Users\chumi\Pictures\Hotel\hotellabel.jpg")
        img1 = img1.resize((1550,800),Image.ANTIALIAS)
        self.photoimg1= ImageTk.PhotoImage(img1)
        lbimg =Label(self.root,image=self.photoimg1,bd = 4,relief=RIDGE)
        lbimg.place(x=0,y=0,width=1550,height=140)

    #==============logo==================#
        img2 =Image.open(r"C:\Users\chumi\Pictures\Hotel\logo.png")
        img2 = img2.resize((230,130),Image.ANTIALIAS)
        self.photoimg2 = ImageTk.PhotoImage(img2)
        lgimg =Label(self.root,image=self.photoimg2,bd =4,relief= RIDGE  )
        lgimg.place(x=0,y=0,width=230,height=130)
    
    #=========title=============#
        lbl_title = Label(self.root,text="HOTEL MANAGEMENT SYSTEM",font = ("times new roman",40,"bold"),bg= "black",fg="white",bd=4,relief=RAISED)
        lbl_title.place(x = 0,y = 140,width = 1550,height=50)


    #==========main Frame=========#
        main_frame = Frame(self.root,bd=4,relief=RIDGE)
        main_frame.place(x=0,y=190,width=1550,height=620)

    #==========label main=========#
        lbl_menu=Label(self.root,text="Menu",font=("times new roman",20,"bold"),bg="black",fg="white",bd=4,relief=RIDGE)
        lbl_menu.place(x=0,y=190,width=230)
    #btn Frame
        btn_frame = Frame(self.root,bd=4,relief=RIDGE)
        btn_frame.place(x=0,y=228,width=228,height=230)
        
        cust_btn = Button(btn_frame,text="Customer",command=self.cust_detail,width=20,font=("times new roman",14,"bold"),bg="black",fg="gold",bd=4,cursor="hand1")
        cust_btn.grid(row=0,column=0,pady=1)

        cust_btn = Button(btn_frame,text="Room",width=20,font=("times new roman",14,"bold"),bg="black",fg="gold",bd=4,cursor="hand1")
        cust_btn.grid(row=1,column=0,pady=1)

        cust_btn = Button(btn_frame,text="Details",width=20,font=("times new roman",14,"bold"),bg="black",fg="gold",bd=4,cursor="hand1")
        cust_btn.grid(row=2,column=0,pady=1)

        cust_btn = Button(btn_frame,text="Report",width=20,font=("times new roman",14,"bold"),bg="black",fg="gold",bd=4,cursor="hand1")
        cust_btn.grid(row=3,column=0,pady=1)

        cust_btn = Button(btn_frame,text="Logout",width=20,font=("times new roman",14,"bold"),bg="black",fg="gold",bd=4,cursor="hand1")
        cust_btn.grid(row=4,column=0,pady=1)
    def cust_detail(self):
        self.new_window = Toplevel(self.root)
        self.app= Cus_win(self.new_window)


if __name__ == "__main__":
    root=Tk()
    object = HotelManagementSystem(root)
    root.mainloop()


