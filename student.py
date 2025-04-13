from tkinter import *
from PIL import Image, ImageTk  # pip install pillow
from tkinter import ttk , messagebox
import sqlite3
class StudentClass:
    def __init__(self, root):
        self.root = root
        self.root.title("Result Management System")
        self.root.geometry("1200x480+80+170")
        self.root.config(bg="white")
        self.root.focus_force()

        # -- Title Label --
        self.title_label = Label(self.root, text="Student Details",  
                                 font=("Goudy Old Style", 20, "bold"), bg="#033054", fg="white")
        self.title_label.place(x=10, y=15, width=1180, height=35)

        # ===== Variables =====
        self.var_roll = StringVar()
        self.var_name = StringVar()
        self.var_email = StringVar()
        self.var_gender = StringVar()
        self.var_dob = StringVar()
        self.var_contact = StringVar()
        self.var_course = StringVar()
        self.var_search = StringVar()  # ✅ Define var_search



        # === Widgets ===
        #====coloum-1=====
        Label(self.root, text="Roll No.", font=("Goudy Old Style", 15, "bold"), 
              bg='white', fg="#000000").place(x=10, y=60)
        Label(self.root, text="Name", font=("Goudy Old Style", 15, "bold"), 
              bg='white', fg="#000000").place(x=10, y=100)
        Label(self.root, text="Email", font=("Goudy Old Style", 15, "bold"), 
              bg='white', fg="#000000").place(x=10, y=140)
        Label(self.root, text="Gender", font=("Goudy Old Style", 15, "bold"), 
              bg='white', fg="#000000").place(x=10, y=180)
        Label(self.root, text="address", font=("Goudy Old Style", 15, "bold"), 
              bg='white', fg="#000000").place(x=10, y=280)

        #====entry fields ===========
        self.txt_roll = Entry(self.root, textvariable=self.var_roll, font=("Goudy Old Style", 15, "bold"), 
                                    bg='lightyellow', fg="#000000")
        self.txt_roll.place(x=140, y=60, width=200)

        self.txt_name = Entry(self.root, textvariable=self.var_name, font=("Goudy Old Style", 15, "bold"), 
                                  bg='lightyellow', fg='#000000')
        self.txt_name.place(x=140, y=100, width=200)

        self.txt_email= Entry(self.root, textvariable=self.var_email, font=("Goudy Old Style", 15, "bold"), 
                                    bg='lightyellow', fg='#000000')
        self.txt_email.place(x=140, y=140, width=200)

        self.txt_gender = ttk.Combobox(self.root, textvariable=self.var_gender, 
                               values=["Select","Male", "Female", "Others"], 
                               font=("Goudy Old Style", 15, "bold"))
        self.txt_gender.current(0)
                                     
        self.txt_gender.place(x=140, y=180, width=210)


        #=====coloum-2======
        Label(self.root, text="D.O.B", font=("Goudy Old Style", 15, "bold"), 
              bg='white', fg="#000000").place(x=380, y=60)
        Label(self.root, text="Contact", font=("Goudy Old Style", 15, "bold"), 
              bg='white', fg="#000000").place(x=380, y=100)
        Label(self.root, text="Course", font=("Goudy Old Style", 15, "bold"), 
              bg='white', fg="#000000").place(x=380, y=140)
        

        
        #======entry field-2=========
        #====entry fields ===========
        self.txt_dob = Entry(self.root, textvariable=self.var_dob, font=("Goudy Old Style", 15, "bold"), 
                                    bg='lightyellow', fg="#000000")
        self.txt_dob.place(x=490, y=60, width=200)

        self.txt_contact = Entry(self.root, textvariable=self.var_contact, font=("Goudy Old Style", 15, "bold"), 
                                  bg='lightyellow', fg='#000000')
        self.txt_contact.place(x=490, y=100, width=200)

        self.txt_Course= Entry(self.root, textvariable=self.var_course, font=("Goudy Old Style", 15, "bold"), 
                                    bg='lightyellow', fg='#000000')
        self.txt_Course.place(x=490, y=140, width=200)

        self.txt_course = ttk.Combobox(self.root, textvariable=self.var_course, 
                               values=[],  # ✅ Initially Empty
                               font=("Goudy Old Style", 15, "bold"),
                               state="readonly")  # ✅ Prevents typing
        self.txt_course.set("")  # ✅ Initially Empty
        self.txt_course.place(x=490, y=140, width=200)

    


        #======text address========
        self.txt_address = Text(self.root, font=("Goudy Old Style", 15, "bold"), 
                                    bg='lightyellow', fg='#000000')
        self.txt_address.place(x=150, y=280, width=500, height=100)

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
        Label(self.root, text="Search Roll No.", font=("Arial", 14, "bold"), 
              bg="white", fg="black").place(x=710, y=60)

        txt_search = Entry(self.root,text="roll no.", textvariable=self.var_search, font=("Arial", 12), 
                           bg="lightyellow", fg="black")
        txt_search.place(x=830, y=60, width=200, height=25)

        Button(self.root, text="Search", font=("Arial", 12, "bold"), bg="#008000", 
               fg="black", cursor="hand2",command=self.search).place(x=1040, y=60, width=80, height=25)          

        # === Course Table ===
        self.C_Frame = Frame(self.root, bd=2, relief=RIDGE)
        self.C_Frame.place(x=720, y=100, width=470, height=340)

        # **Scrollbars**
        Scrolly = Scrollbar(self.C_Frame, orient=VERTICAL)
        Scrollx = Scrollbar(self.C_Frame, orient=HORIZONTAL)

        self.CourseTable = ttk.Treeview(self.C_Frame, columns=("roll", "name", "email", "gender","dob","contact","course","address"),
                                        xscrollcommand=Scrollx.set, yscrollcommand=Scrolly.set)

        # **Attach Scrollbars to Treeview**
        Scrolly.config(command=self.CourseTable.yview)
        Scrollx.config(command=self.CourseTable.xview)

        Scrolly.pack(side=RIGHT, fill=Y)
        Scrollx.pack(side=BOTTOM, fill=X)

        # **Table Headings**
        self.CourseTable.heading("roll", text="Roll No.")
        self.CourseTable.heading("name", text="Name")
        self.CourseTable.heading("email", text="Email")
        self.CourseTable.heading("gender", text="Gender")
        self.CourseTable.heading("dob", text="D.O.B")
        self.CourseTable.heading("contact", text="Contact")
        self.CourseTable.heading("course", text="Course")
        self.CourseTable.heading("address", text="Address")
        self.CourseTable["show"] = "headings"

        # **Column Widths**
        self.CourseTable.column("roll", width=100)
        self.CourseTable.column("name", width=100)
        self.CourseTable.column("email", width=100)
        self.CourseTable.column("gender", width=100)
        self.CourseTable.column("dob", width=100)
        self.CourseTable.column("contact", width=100)
        self.CourseTable.column("course", width=100)
        self.CourseTable.column("address", width=100)

        self.CourseTable.pack(fill=BOTH, expand=1)
        self.CourseTable.bind("<ButtonRelease-1>",self.get_data)
        self.show()
        self.fetch_course()
#==========================================================
#databs code===
#clear=====
    def clear(self):
        self.show()
        self.var_roll.set("")
        self.var_name.set("")
        self.var_email.set("")
        self.var_gender.set("select")
        self.var_dob.set("")
        self.var_contact.set("")
        self.var_course.set("select")
        self.txt_address.delete("1.0",END)
        self.txt_roll.config(state= NORMAL)
        self.var_search.set("")

#=====delete=====
    def delete(self):
        con = sqlite3.connect("rms.db")
        cur = con.cursor()
        try:
            if self.var_roll.get() == "":
               messagebox.showerror("Error", "Roll Number is required", parent=self.root)
            else:
               cur.execute("SELECT * FROM student WHERE roll=?", (self.var_roll.get(),))  # ✅ Corrected table name
               row = cur.fetchone()

            if row is None:  # ✅ Moved inside the correct block
                messagebox.showerror("Error", "Please select a student from the list first", parent=self.root)
            else:
                # ✅ Ask for confirmation before deleting
                op = messagebox.askyesno("Confirm", "Are you sure you want to delete this student?", parent=self.root)
                if op:
                    cur.execute("DELETE FROM student WHERE roll=?", (self.var_roll.get(),))  # ✅ Corrected table name
                    con.commit()
                    messagebox.showinfo("Success", "Student deleted successfully", parent=self.root)
                    self.show()  # ✅ Refresh table after deletion
                    self.clear()  # ✅ Clear input fields after deletion

        except Exception as ex:
            messagebox.showerror("Error", f"Error due to {str(ex)}", parent=self.root)
        finally:
            con.close()  # ✅ Close database connection


#data fill in box===    
    def get_data(self,ev):
        self.txt_roll.config(state='readonly')
        self.txt_roll
        r=self.CourseTable.focus()
        content=self.CourseTable.item(r)
        row=content["values"]
        self.var_roll.set(row[0])             
        self.var_name.set(row[1]),
        self.var_email.set(row[2]),
        self.var_gender.set(row[3]),
        self.var_dob.set(row[4]),  # ✅ DOB is correctly placed
        self.var_contact.set(row[5]),  # ✅ Contact is correctly placed
        self.var_course.set(row[6]),
        self.txt_address.delete("1.0", END)        
        self.txt_address.insert(END,row[7])        


    def add(self):
        con=sqlite3.connect(database="rms.db" )
        cur=con.cursor()
        try:
            if self.var_roll.get()=="":
                messagebox.showerror("error","Roll no. should be required",parent=self.root)
            else:
                cur.execute("select * from student where roll=?",(self.var_roll.get(),))
                row=cur.fetchone()
                if row!=None:
                    messagebox.showerror("error","Roll no already present",parent=self.root)
                else:
                    cur.execute("insert into student(roll,name,email,gender,dob,contact,course,address) values(?,?,?,?,?,?,?,?)",(
                        self.var_roll.get(),
                        self.var_name.get(),
                        self.var_email.get(),
                        self.var_gender.get(),
                        self.var_dob.get(),  # ✅ DOB is correctly placed
                        self.var_contact.get(),  # ✅ Contact is correctly placed
                        self.var_course.get(),
                        self.txt_address.get("1.0", END)
                    ))
                    con.commit()
                    messagebox.showinfo("Success","student added Successfully",parent=self.root)
                    self.show()
        except Exception as ex:
            messagebox.showerror("error",f"Error due to{str(ex)}")


    def Update(self):
        con = sqlite3.connect("rms.db")
        cur = con.cursor()
        try:
            if self.var_roll.get() == "":
                messagebox.showerror("Error", "Roll no. should be required", parent=self.root)
            else:
                cur.execute("SELECT * FROM student WHERE roll=?", (self.var_roll.get(),))
                row = cur.fetchone()
            
            if row is None:
                messagebox.showerror("Error", "Select a student from the list", parent=self.root)
            else:
                cur.execute("""UPDATE student 
                               SET name=?, email=?, gender=?, dob=?, contact=?, course=?, address=? 
                               WHERE roll=?""", (
                    self.var_name.get(),
                    self.var_email.get(),
                    self.var_gender.get(),
                    self.var_dob.get(),
                    self.var_contact.get(),
                    self.var_course.get(),
                    self.txt_address.get("1.0", END),  # ✅ Textbox input for address
                    self.var_roll.get()  # ✅ Roll number goes at the END
                ))
                con.commit()
                messagebox.showinfo("Success", "Student updated successfully", parent=self.root)
                self.show()  # ✅ Refresh table after update
        except Exception as ex:
            messagebox.showerror("Error", f"Error due to {str(ex)}", parent=self.root)
        finally:
            con.close()  # ✅ Close the database connection



    def show(self):
        con=sqlite3.connect(database="rms.db" )
        cur=con.cursor()
        try:
            cur.execute("select * from student")
            rows = cur.fetchall()  
            self.CourseTable.delete(*self.CourseTable.get_children())
            for row in rows: 
                self.CourseTable.insert('',END,values=row)
                
        except Exception as ex:
            messagebox.showerror("error",f"Error due to{str(ex)}")


    def fetch_course(self):
        con = sqlite3.connect("rms.db")
        cur = con.cursor()
        try:
            cur.execute("SELECT DISTINCT name FROM course")  # ✅ Fetch course names from 'course' table
            rows = cur.fetchall()
        
            course_list = [row[0] for row in rows]  # ✅ Extract course names into a list
            self.txt_course["values"] = course_list  # ✅ Populate the combobox with course names
        
        except Exception as ex:
            messagebox.showerror("Error", f"Error due to {str(ex)}", parent=self.root)
        finally:
            con.close()  # ✅ Close the database connection



    def search(self):
        con = sqlite3.connect("rms.db")
        cur = con.cursor()
        try:
            if self.var_search.get() == "":
               messagebox.showerror("Error", "Roll Number is required for search", parent=self.root)
            else:
               cur.execute("SELECT roll FROM student WHERE roll=?", (self.var_search.get(),))  
               row = cur.fetchone()  # ✅ Fetch single result
            
            if row is None:  # ✅ Correctly checking if roll number exists
                messagebox.showerror("Error", "No student found!", parent=self.root)
            else:
                roll_no = row[0]  # ✅ Extracting roll number
                messagebox.showinfo("Success", f"Roll Number Found: {roll_no}", parent=self.root)  # ✅ Show roll number
                
                # ✅ Highlight found roll number in Treeview
                self.CourseTable.delete(*self.CourseTable.get_children())  # Clear previous data
                cur.execute("SELECT * FROM student WHERE roll=?", (roll_no,))
                student_data = cur.fetchone()
                if student_data:
                    self.CourseTable.insert('', END, values=student_data)  # ✅ Insert the found student into table

        except Exception as ex:
            messagebox.showerror("Error", f"Error due to {str(ex)}", parent=self.root)
        finally:
            con.close()  # ✅ Close the database connection

    

    

if __name__ == "__main__":
    root = Tk()
    obj = StudentClass(root)
    root.mainloop()
