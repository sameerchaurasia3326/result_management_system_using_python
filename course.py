from tkinter import *
from PIL import Image, ImageTk  # pip install pillow
from tkinter import ttk , messagebox
import sqlite3
class CourseClass:
    def __init__(self, root):
        self.root = root
        self.root.title("Result Management System")
        self.root.geometry("1200x480+80+170")
        self.root.config(bg="white")
        self.root.focus_force()

        # -- Title Label --
        self.title_label = Label(self.root, text="Manage Course Details",  
                                 font=("Goudy Old Style", 20, "bold"), bg="#033054", fg="white")
        self.title_label.place(x=10, y=15, width=1180, height=35)

        # ===== Variables =====
        self.var_course = StringVar()
        self.var_duration = StringVar()
        self.var_charges = StringVar()
        self.var_search = StringVar()

        # === Widgets ===
        Label(self.root, text="Course Name", font=("Goudy Old Style", 15, "bold"), 
              bg='white', fg="#000000").place(x=10, y=60)
        Label(self.root, text="Duration", font=("Goudy Old Style", 15, "bold"), 
              bg='white', fg="#000000").place(x=10, y=100)
        Label(self.root, text="Course Fees", font=("Goudy Old Style", 15, "bold"), 
              bg='white', fg="#000000").place(x=10, y=140)
        Label(self.root, text="Description", font=("Goudy Old Style", 15, "bold"), 
              bg='white', fg="#000000").place(x=10, y=180)

        self.txt_courseName = Entry(self.root, textvariable=self.var_course, font=("Goudy Old Style", 15, "bold"), 
                                    bg='lightyellow', fg="#000000")
        self.txt_courseName.place(x=150, y=60, width=200)

        self.txt_Duration = Entry(self.root, textvariable=self.var_duration, font=("Goudy Old Style", 15, "bold"), 
                                  bg='lightyellow', fg='#000000')
        self.txt_Duration.place(x=150, y=100, width=200)

        self.txt_courseFees = Entry(self.root, textvariable=self.var_charges, font=("Goudy Old Style", 15, "bold"), 
                                    bg='lightyellow', fg='#000000')
        self.txt_courseFees.place(x=150, y=140, width=200)

        self.txt_Discription = Text(self.root, font=("Goudy Old Style", 15, "bold"), 
                                    bg='lightyellow', fg='#000000')
        self.txt_Discription.place(x=150, y=180, width=500, height=130)

        # === Buttons (Below Widgets) ===
        Button(self.root, text="Save", font=("Goudy Old Style", 15, "bold"), bg="#2196f3", 
               fg="black", cursor="hand2", command=self.add).place(x=150, y=400, width=110, height=40)

        Button(self.root, text="Update", font=("Goudy Old Style", 15, "bold"), bg="#0000FF", 
               fg="black", cursor="hand2",command=self.Update).place(x=270, y=400, width=110, height=40)

        Button(self.root, text="Delete", font=("Goudy Old Style", 15, "bold"), bg="#FF0000", 
               fg="black", cursor="hand2",command=self.delete).place(x=390, y=400, width=110, height=40)

        Button(self.root, text="Clear", font=("Goudy Old Style", 15, "bold"), bg="#607d8b", 
               fg="black", cursor="hand2",command=self.clear).place(x=510, y=400, width=110, height=40)

        # === Search Bar (Top-Right Corner) ===
        Label(self.root, text="Search Course:", font=("Arial", 14, "bold"), 
              bg="white", fg="black").place(x=650, y=60)

        txt_search = Entry(self.root, textvariable=self.var_search, font=("Arial", 12), 
                           bg="lightyellow", fg="black")
        txt_search.place(x=800, y=60, width=200, height=25)

        Button(self.root, text="Search", font=("Arial", 12, "bold"), bg="#008000", 
               fg="black", cursor="hand2",command=self.search).place(x=1010, y=60, width=80, height=25)          

        # === Course Table ===
        self.C_Frame = Frame(self.root, bd=2, relief=RIDGE)
        self.C_Frame.place(x=720, y=100, width=470, height=340)

        # **Scrollbars**
        Scrolly = Scrollbar(self.C_Frame, orient=VERTICAL)
        Scrollx = Scrollbar(self.C_Frame, orient=HORIZONTAL)

        self.CourseTable = ttk.Treeview(self.C_Frame, columns=("cid", "name", "duration", "charges", "description"),
                                        xscrollcommand=Scrollx.set, yscrollcommand=Scrolly.set)

        # **Attach Scrollbars to Treeview**
        Scrolly.config(command=self.CourseTable.yview)
        Scrollx.config(command=self.CourseTable.xview)

        Scrolly.pack(side=RIGHT, fill=Y)
        Scrollx.pack(side=BOTTOM, fill=X)

        # **Table Headings**
        self.CourseTable.heading("cid", text="Course ID")
        self.CourseTable.heading("name", text="Name")
        self.CourseTable.heading("duration", text="Duration")
        self.CourseTable.heading("charges", text="Charges")
        self.CourseTable.heading("description", text="Description")
        self.CourseTable["show"] = "headings"

        # **Column Widths**
        self.CourseTable.column("cid", width=80)
        self.CourseTable.column("name", width=120)
        self.CourseTable.column("duration", width=100)
        self.CourseTable.column("charges", width=100)
        self.CourseTable.column("description", width=150)
        self.CourseTable.pack(fill=BOTH, expand=1)
        self.CourseTable.bind("<ButtonRelease-1>",self.get_data)
        self.show()
#==========================================================
#databs code===
#clear=====
    def clear(self):
        self.show()
        self.var_course.set("")
        self.var_duration.set("")
        self.var_charges.set("")
        self.var_search.set("")
        self.txt_Discription.delete("1.0",END)
        self.txt_courseName.config(state= NORMAL)

#=====delete=====
    def delete(self):
        con = sqlite3.connect(database="rms.db")
        cur = con.cursor()
        try:
            if self.var_course.get() == "":
               messagebox.showerror("Error", "Course Name should be required", parent=self.root)
            else:
               cur.execute("SELECT * FROM course WHERE name=?", (self.var_course.get(),))
               row = cur.fetchone()
            if row is None:
                messagebox.showerror("Error", "Please select a course from the list first", parent=self.root)
            else:
                # ✅ Ask user for confirmation before deleting
                op = messagebox.askyesno("Confirm", "Are you sure you want to delete this course?", parent=self.root)
                if op:
                    cur.execute("DELETE FROM course WHERE name=?", (self.var_course.get(),))
                    con.commit()
                    messagebox.showinfo("Success", "Course deleted successfully", parent=self.root)
                    self.show()  # ✅ Refresh table after deletion
                    self.clear()  # ✅ Clear input fields after deletion
        except Exception as ex:
            messagebox.showerror("Error", f"Error due to {str(ex)}", parent=self.root)   

#data fill in box===    
    def get_data(self,ev):
        self.txt_courseName.config(state='readonly')
        self.txt_courseName
        r=self.CourseTable.focus()
        content=self.CourseTable.item(r)
        row=content["values"]
        #print(row)
        self.var_course.set(row[1])
        self.var_duration.set(row[2])
        self.var_charges.set(row[3])
        #self.var_course.set(row[4])
        self.txt_Discription.delete('1.0', END)
        self.txt_Discription.insert(END,row[4])


    def add(self):
        con=sqlite3.connect(database="rms.db" )
        cur=con.cursor()
        try:
            if self.var_course.get()=="":
                messagebox.showerror("error","Course Name should be required",parent=self.root)
            else:
                cur.execute("select * from course where name=?",(self.var_course.get(),))
                row=cur.fetchone()
                if row!=None:
                    messagebox.showerror("error","Course Name already exist",parent=self.root)
                else:
                    cur.execute("insert into course(name,duration,charges,description) values(?,?,?,?)",(
                        self.var_course.get(),
                        self.var_duration.get(),
                        self.var_charges.get(),
                        self.txt_Discription.get("1.0",END)
                    ))
                    con.commit()
                    messagebox.showinfo("Success","Course added Successfully",parent=self.root)
                    self.show()
        except Exception as ex:
            messagebox.showerror("error",f"Error due to{str(ex)}")


    def Update(self):
        con=sqlite3.connect(database="rms.db" )
        cur=con.cursor()
        try:
            if self.var_course.get()=="":
                messagebox.showerror("error","Course Name should be required",parent=self.root)
            else:
                cur.execute("select * from course where name=?",(self.var_course.get(),))
                row=cur.fetchone()
                if row==None:
                    messagebox.showerror("error","select course form list",parent=self.root)
                else:
                    cur.execute("UPDATE course SET duration = ?, charges = ?, description = ? WHERE name = ?", (
                        self.var_duration.get(),
                        self.var_charges.get(),
                        self.txt_Discription.get("1.0",END),
                        self.var_course.get(),
                    ))
                    con.commit()
                    messagebox.showinfo("Success","Course updated Successfully",parent=self.root)
                    self.show()
        except Exception as ex:
            messagebox.showerror("error",f"Error due to{str(ex)}")


    def show(self):
        con=sqlite3.connect(database="rms.db" )
        cur=con.cursor()
        try:
            cur.execute("select * from course")
            rows = cur.fetchall()  
            self.CourseTable.delete(*self.CourseTable.get_children())
            for row in rows: 
                self.CourseTable.insert('',END,values=row)
                
        except Exception as ex:
            messagebox.showerror("error",f"Error due to{str(ex)}")


    def search(self):
        con = sqlite3.connect(database="rms.db")
        cur = con.cursor()
        try:
            if self.var_search.get() == "":
               messagebox.showerror("Error", "Course Name is required for search", parent=self.root)
            else:
               cur.execute("SELECT * FROM course WHERE name LIKE ?", ('%' + self.var_search.get() + '%',))
               rows = cur.fetchall()
            
            if len(rows) == 0:
                messagebox.showerror("Error", "No course found!", parent=self.root)
            else:
                self.CourseTable.delete(*self.CourseTable.get_children())  # Clear previous data
                
                for row in rows:
                    self.CourseTable.insert('', END, values=row)  # Insert new results
                
        except Exception as ex:
            messagebox.showerror("Error", f"Error due to {str(ex)}", parent=self.root)
    

    

if __name__ == "__main__":
    root = Tk()
    obj = CourseClass(root)
    root.mainloop()
