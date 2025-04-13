from tkinter import *
from PIL import Image, ImageTk  # pip install pillow
from tkinter import ttk , messagebox
import sqlite3
class resultClass:
    def __init__(self, root):
        self.root = root
        self.root.title("Result Management System")
        self.root.geometry("1200x480+80+170")
        self.root.config(bg="white")
        self.root.focus_force()

        # -- Title Label --
        self.title_label = Label(self.root, text="Add Result ",  
                                 font=("Goudy Old Style", 20, "bold"), bg="orange", fg="#262626")
        self.title_label.place(x=10, y=15, width=1180, height=50)

        #====variable=======
        self.var_roll = StringVar()
        self.var_name = StringVar()
        self.var_course = StringVar()
        self.var_marks = StringVar()
        self.var_full_marks = StringVar()
        self.var_semester = StringVar()
        self.roll_list=[]
        self.fetch_roll()
        #===widgets======

        Label(self.root, text="select  student", font=("Goudy Old Style", 15, "bold"), 
              bg='white', fg="#000000").place(x=50, y=110)
        Label(self.root, text="Name", font=("Goudy Old Style", 15, "bold"), 
              bg='white', fg="#000000").place(x=50, y=170)
        Label(self.root, text="course", font=("Goudy Old Style", 15, "bold"), 
              bg='white', fg="#000000").place(x=50, y=230)
        Label(self.root, text="Mark obtained", font=("Goudy Old Style", 15, "bold"), 
              bg='white', fg="#000000").place(x=50, y=290)
        Label(self.root, text="Full Marks", font=("Goudy Old Style", 15, "bold"), 
              bg='white', fg="#000000").place(x=50, y=350)


        self.txt_student = ttk.Combobox(self.root, textvariable=self.var_roll, 
                               values=self.roll_list,  # ✅ Initially Empty
                               font=("Goudy Old Style", 15, "bold"),
                               state="readonly")  # ✅ Prevents typing
        self.txt_student.set("select")  # ✅ Initially Empty
        self.txt_student.place(x=280, y=100, width=200)

        Button(self.root, text="Search", font=("Arial", 12, "bold"), bg="#03a9f4", 
               fg="blue", cursor="hand2",command=self.search).place(x=500, y=100, width=120, height=28)


        self.txt_Name = Entry(self.root, textvariable=self.var_name, font=("Goudy Old Style", 20, "bold"), 
                                    bg='white',state='readonly', fg="white")
        self.txt_Name.place(x=280, y=160, width=340)

        self.txt_course = Entry(self.root, textvariable=self.var_course, font=("Goudy Old Style", 20, "bold"), 
                                    bg='white',state='readonly', fg="white")
        self.txt_course.place(x=280, y=220, width=340)

        self.txt_marks = Entry(self.root, textvariable=self.var_marks, font=("Goudy Old Style", 20, "bold"), 
                                    bg='lightyellow', fg="#000000")
        self.txt_marks.place(x=280, y=280, width=340)

        self.txt_full_marks = Entry(self.root, textvariable=self.var_full_marks, font=("Goudy Old Style", 20, "bold"), 
                                    bg='lightyellow', fg="#000000")
        self.txt_full_marks.place(x=280, y=340, width=340)

        #====button============
        Button(self.root, text="Submit", font=("times new roman", 15), 
         bg="lightgreen", fg="black", cursor="hand2",command=self.add, highlightbackground="lightgreen").place(x=330, y=450, width=110, height=35)

        Button(self.root, text="Clear", font=("times new roman", 15), 
         bg="gray", fg="black", cursor="hand2",command=self.clear, highlightbackground="gray").place(x=460, y=450, width=110, height=35)
        

        # == Content Image ==
        self.bg_img = Image.open("images/all.webp")
        self.bg_img = self.bg_img.resize((500, 300), Image.Resampling.LANCZOS)
        self.bg_img = ImageTk.PhotoImage(self.bg_img)

        self.lbl_bg = Label(self.root, image=self.bg_img)
        self.lbl_bg.place(x=660, y=100)



#=======================================================================
    def fetch_roll(self):
       con=sqlite3. connect(database="rms.db" )
       cur=con. cursor ()
       try:
          cur. execute("select roll from student")
          rows=cur.fetchall()
          if len(rows)>0:
               for row in rows:
                   self.roll_list.append(row[0])
       except Exception as ex:
          messagebox. showerror ("Error", f"Error due to {str(ex)}")

    def search(self):
       con=sqlite3.connect(database="rms.db")
       cur=con.cursor()
       try:
           cur.execute("select name, course from student where roll=?", (self.var_roll.get(),))
           row=cur.fetchone()
           if row!=None:
                self.var_name.set(row[0])
                self.var_course.set(row[1])
           else:
                messagebox.showerror ("Ertor", "No record found", parent=self.root)
       except Exception as ex:
           messagebox. showerror ("Error", f"Error due to {str(ex)}")

    def add(self):
       con = sqlite3.connect("rms.db")
       cur = con.cursor()
       try:
           if self.var_name.get() == "":
               messagebox.showerror("Error", "Please first search student record", parent=self.root)
           else:
               cur.execute("SELECT * FROM result WHERE roll=? AND course=?", (self.var_roll.get(), self.var_course.get()))
               row = cur.fetchone()
               if row is not None:
                    messagebox.showerror("Error", "Result already present", parent=self.root)
               else:
                    per = (int(self.var_marks.get()) * 100) / int(self.var_full_marks.get())  # ✅ Calculate percentage
                
                # ✅ Corrected SQL Query (Removed extra comma)
               cur.execute("INSERT INTO result (roll, name, course, marks_ob, full_marks, per) VALUES (?, ?, ?, ?, ?, ?)", (
                    self.var_roll.get(),
                    self.var_name.get(),
                    self.var_course.get(),
                    self.var_marks.get(),
                    self.var_full_marks.get(),
                    str(per)  # ✅ Store percentage as a string
                ))
                
               con.commit()
               messagebox.showinfo("Success", "Result added Successfully", parent=self.root)
               self.show()

       except Exception as ex:
           messagebox.showerror("Error", f"Error due to {str(ex)}", parent=self.root)
       finally:
           con.close()  # ✅ Ensure connection is closed

    def clear(self):
        self.var_roll.set("select")
        self.var_name.set("")
        self.var_course.set("")
        self.var_marks.set("")
        self.var_full_marks.set("")





if __name__ == "__main__":
    root = Tk()
    obj = resultClass(root)
    root.mainloop()