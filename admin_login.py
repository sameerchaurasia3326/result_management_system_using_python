import sqlite3
from tkinter import *
from tkinter import messagebox

class AdminLogin:
    def __init__(self, root):
        self.root = root
        self.root.title("Admin Login")
        self.root.geometry("500x450+500+200")
        self.root.config(bg="white")

        self.success = False  # Track successful login

        # == Gradient Header ==
        self.header_frame = Frame(self.root, bg="#1E3D59", height=100)
        self.header_frame.pack(fill=X)

        Label(self.header_frame, text="Admin Login", font=("Arial", 22, "bold"), 
              fg="white", bg="#1E3D59").place(x=170, y=30)

        # == Login Form ==
        self.form_frame = Frame(self.root, bg="white")
        self.form_frame.place(x=60, y=120, width=380, height=250)

        Label(self.form_frame, text="Username", font=("Arial", 12), fg="black", bg="white").pack(anchor="w", padx=20)
        self.username_entry = Entry(self.form_frame, font=("Arial", 14), bd=2, relief=SOLID)
        self.username_entry.pack(pady=5, padx=20, fill=X)

        Label(self.form_frame, text="Password", font=("Arial", 12), fg="black", bg="white").pack(anchor="w", padx=20)
        self.password_entry = Entry(self.form_frame, font=("Arial", 14), show="*", bd=2, relief=SOLID)
        self.password_entry.pack(pady=5, padx=20, fill=X)

        # == Login Button ==
        self.login_btn = Button(self.form_frame, text="Login", font=("Arial", 14, "bold"), 
                                bg="#1E3D59", fg="black", cursor="hand2", bd=3, relief=SOLID,
                                command=self.login)
        self.login_btn.pack(pady=20, padx=20, fill=X)

    def login(self):
        username = self.username_entry.get().strip()
        password = self.password_entry.get().strip()

        if not username or not password:
            messagebox.showerror("Error", "All fields are required!", parent=self.root)
            return

        con = sqlite3.connect("rms.db")
        cur = con.cursor()

        cur.execute("SELECT * FROM admin WHERE username=? AND password=?", (username, password))
        row = cur.fetchone()
        con.close()

        if row:
            messagebox.showinfo("Success", "Login Successful!", parent=self.root)
            self.root.withdraw()  # ✅ Hide login window instead of destroying

            self.open_dashboard()  # ✅ Open dashboard
        else:
            messagebox.showerror("Error", "Invalid Username or Password", parent=self.root)

    def open_dashboard(self):
        from dashboard import RMS  # ✅ Delayed import (Fixes circular import)
        
        dashboard_root = Toplevel(self.root)  # ✅ Open dashboard in a new window
        RMS(dashboard_root)

# == Function to Open Admin Login Window ==
def open_admin_login():
    login_root = Tk()
    AdminLogin(login_root)
    login_root.mainloop()

if __name__ == "__main__":
    open_admin_login()
