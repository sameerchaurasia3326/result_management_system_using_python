import sqlite3
from tkinter import *
from tkinter import messagebox
from student_login import StudentLogin  # ✅ Import Student Login

class StudentRegister:
    def __init__(self, root):
        self.root = root
        self.root.title("Student Registration")
        self.root.geometry("400x500+300+100")
        self.root.config(bg="white")

        # UI Components
        frame = Frame(self.root, bg="white", bd=2, relief=SOLID)
        frame.place(relx=0.5, rely=0.5, anchor=CENTER, width=350, height=450)

        Label(frame, text="Student Registration", font=("Arial", 18, "bold"), fg="black", bg="white").pack(pady=10)

        Label(frame, text="Name:", font=("Arial", 12), bg="white", fg='black').pack(anchor="w", padx=20)
        self.name_entry = Entry(frame, font=("Arial", 12), bd=2, relief=SOLID)
        self.name_entry.pack(pady=5, padx=20, fill=X)

        Label(frame, text="Username:", font=("Arial", 12), bg="white", fg='black').pack(anchor="w", padx=20)
        self.username_entry = Entry(frame, font=("Arial", 12), bd=2, relief=SOLID)
        self.username_entry.pack(pady=5, padx=20, fill=X)

        Label(frame, text="Password:", font=("Arial", 12), bg="white", fg='black').pack(anchor="w", padx=20)
        self.password_entry = Entry(frame, font=("Arial", 12), show="*", bd=2, relief=SOLID)
        self.password_entry.pack(pady=5, padx=20, fill=X)

        Button(frame, text="Register", font=("Arial", 12, "bold"), bg="#28A745", fg="black",
               command=self.register_student).pack(pady=15, padx=20, fill=X)

    def register_student(self):
        name = self.name_entry.get()
        username = self.username_entry.get()
        password = self.password_entry.get()

        if not name or not username or not password:
            messagebox.showerror("Error", "All fields are required")
            return

        con = sqlite3.connect("rms.db")
        cur = con.cursor()
        
        try:
            cur.execute("INSERT INTO students (name, username, password) VALUES (?, ?, ?)", (name, username, password))
            con.commit()
            messagebox.showinfo("Success", "Registration Successful")

            self.root.destroy()  # ✅ Close registration window
            self.open_student_login()  # ✅ Open login window automatically

        except sqlite3.IntegrityError:
            messagebox.showerror("Error", "Username already exists")
        con.close()

    def open_student_login(self):
        login_root = Tk()
        login_root.title("Student Login")
        obj = StudentLogin(login_root)
        login_root.mainloop()

if __name__ == "__main__":
    root = Tk()
    obj = StudentRegister(root)
    root.mainloop()
