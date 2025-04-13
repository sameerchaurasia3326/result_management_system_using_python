import sqlite3
from tkinter import *
from tkinter import messagebox
from report import reportClass  # ✅ Import View Result window

class StudentLogin:
    def __init__(self, root):
        self.root = root
        self.root.title("Student Login")
        self.root.geometry("400x400+500+200")
        self.root.config(bg="white")

        frame = Frame(self.root, bg="white", bd=2, relief=SOLID)
        frame.place(relx=0.5, rely=0.5, anchor=CENTER, width=350, height=350)

        Label(frame, text="Student Login", font=("Arial", 18, "bold"), fg="black", bg="white").pack(pady=10)

        Label(frame, text="Username:", font=("Arial", 12), bg="white", fg="black").pack(anchor="w", padx=20)
        self.username_entry = Entry(frame, font=("Arial", 12), bd=2, relief=SOLID)
        self.username_entry.pack(pady=5, padx=20, fill=X)

        Label(frame, text="Password:", font=("Arial", 12), bg="white", fg="black").pack(anchor="w", padx=20)
        self.password_entry = Entry(frame, font=("Arial", 12), show="*", bd=2, relief=SOLID)
        self.password_entry.pack(pady=5, padx=20, fill=X)

        Button(frame, text="Login", font=("Arial", 12, "bold"), bg="#1E3D59", fg="black",
               command=self.login).pack(pady=20, padx=20, fill=X)

    def login(self):
        username = self.username_entry.get().strip()
        password = self.password_entry.get().strip()

        if not username or not password:
            messagebox.showerror("Error", "All fields are required!", parent=self.root)
            return

        con = sqlite3.connect("rms.db")
        cur = con.cursor()

        cur.execute("SELECT * FROM students WHERE username=? AND password=?", (username, password))
        row = cur.fetchone()
        con.close()

        if row:
            messagebox.showinfo("Success", "Login Successful!", parent=self.root)
            self.open_view_result()  # ✅ Open View Result Window
        else:
            messagebox.showerror("Error", "Invalid Username or Password", parent=self.root)

    def open_view_result(self):
        self.root.withdraw()  # ✅ Hide login window instead of destroying
        new_win = Toplevel(self.root)
        obj = reportClass(new_win)  # ✅ Correct Class Name (Matches `report.py`)

if __name__ == "__main__":
    root = Tk()
    obj = StudentLogin(root)
    root.mainloop()
