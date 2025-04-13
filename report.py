from tkinter import *
from PIL import Image, ImageTk
from tkinter import ttk, messagebox
import sqlite3

class reportClass:
    def __init__(self, root):
        self.root = root
        self.root.title("View Student Result")
        self.root.geometry("900x500+250+100")
        self.root.config(bg="white")

        # ==== Gradient Header ====
        self.title_label = Label(self.root, text="View Student Result", font=("Goudy Old Style", 22, "bold"),
                                 bg="#001F3F", fg="white", anchor="w", padx=20)
        self.title_label.place(x=0, y=0, relwidth=1, height=50)

        # ==== Variables ====
        self.var_roll = StringVar()

        # ==== Search Area ====
        frame_search = Frame(self.root, bg="white", bd=2, relief=RIDGE)
        frame_search.place(x=50, y=70, width=800, height=60)

        Label(frame_search, text="Enter Roll No:", font=("Goudy Old Style", 15, "bold"), bg="black").place(x=20, y=15)
        self.txt_roll = Entry(frame_search, textvariable=self.var_roll, font=("Goudy Old Style", 15), bg="lightyellow",fg='black', bd=2, relief=SOLID)
        self.txt_roll.place(x=160, y=15, width=200, height=30)
        
        # 🔵 Search Button - Bright Blue for Clear Visibility
        Button(frame_search, text="Search", font=("Arial", 12, "bold"), bg="#007BFF", fg="black", cursor="hand2", 
               activebackground="#0056b3", command=self.search).place(x=400, y=15, width=100, height=30)
        
        # 🔴 Clear Button - Deep Red for High Contrast
        Button(frame_search, text="Clear", font=("Arial", 12, "bold"), bg="#FF4136", fg="black", cursor="hand2", 
               activebackground="#C70000", command=self.clear).place(x=520, y=15, width=100, height=30)

        # ==== Result Display Area ====
        self.result_frame = Frame(self.root, bd=2, relief=RIDGE, bg="white")
        self.result_frame.place(x=50, y=150, width=800, height=300)

        # Create Treeview Table
        columns = ("Name", "Course", "Marks Obtained", "Full Marks", "Percentage")
        self.result_table = ttk.Treeview(self.result_frame, columns=columns, show="headings")

        # Scrollbars
        scroll_x = Scrollbar(self.result_frame, orient=HORIZONTAL, command=self.result_table.xview)
        scroll_y = Scrollbar(self.result_frame, orient=VERTICAL, command=self.result_table.yview)
        self.result_table.configure(xscrollcommand=scroll_x.set, yscrollcommand=scroll_y.set)

        scroll_x.pack(side=BOTTOM, fill=X)
        scroll_y.pack(side=RIGHT, fill=Y)

        # Define Column Headings
        for col in columns:
            self.result_table.heading(col, text=col)
            self.result_table.column(col, width=150)

        self.result_table.pack(fill=BOTH, expand=1)

    # ==== Fetch Result ====
    def search(self):
        con = sqlite3.connect("rms.db")
        cur = con.cursor()
        try:
            if self.var_roll.get() == "":
                messagebox.showerror("Error", "Roll Number is required", parent=self.root)
                return
            
            cur.execute("SELECT name, course, marks_ob, full_marks, per FROM result WHERE roll=?", (self.var_roll.get(),))
            rows = cur.fetchall()
            
            if rows:
                self.result_table.delete(*self.result_table.get_children())  # Clear previous data
                for row in rows:
                    self.result_table.insert("", END, values=row)
            else:
                messagebox.showerror("Error", "No Record Found", parent=self.root)
        except Exception as ex:
            messagebox.showerror("Error", f"Error due to {str(ex)}", parent=self.root)
        finally:
            con.close()

    # ==== Clear Search ====
    def clear(self):
        self.var_roll.set("")
        self.result_table.delete(*self.result_table.get_children())  # Clear Table Data

if __name__ == "__main__":
    root = Tk()
    obj = reportClass(root)
    root.mainloop()
