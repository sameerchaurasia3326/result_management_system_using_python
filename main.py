from tkinter import Tk, Button, Label, Frame
from student_registration import StudentRegister
from student_login import StudentLogin

# == Open Student Registration Window ==
def open_student_register():
    root = Tk()
    root.title("Student Registration")
    obj = StudentRegister(root)
    root.mainloop()

# == Open Student Login Window ==
def open_student_login():
    root = Tk()
    root.title("Student Login")
    obj = StudentLogin(root)
    root.mainloop()

# == Main Menu Window ==
def main():
    root = Tk()
    root.title("Main Menu")
    root.geometry("450x350+500+250")
    root.config(bg="#F0F0F0")

    # == Header Section ==
    header_frame = Frame(root, bg="#1E3D59", height=80)
    header_frame.pack(fill="x")

    Label(header_frame, text="Welcome to result sytem", font=("Arial", 18, "bold"), fg="white", bg="#1E3D59").place(x=140, y=20)

    # == Button Styling ==
    def on_enter(e, btn):
        btn.config(bg="#4CAF50", fg="white")

    def on_leave(e, btn):
        btn.config(bg="#1E3D59", fg="white")

    # == Student Registration Button ==
    btn_register = Button(root, text="Student Registration", font=("Arial", 14, "bold"), bg="black", fg="white",
                          cursor="hand2", bd=3, relief="solid", command=lambda: [root.destroy(), open_student_register()])
    btn_register.pack(pady=20, padx=50, fill="x")

    btn_register.bind("<Enter>", lambda e: on_enter(e, btn_register))
    btn_register.bind("<Leave>", lambda e: on_leave(e, btn_register))

    # == Student Login Button ==
    btn_login = Button(root, text="Student Login", font=("Arial", 14, "bold"), bg="black", fg="white",
                       cursor="hand2", bd=3, relief="solid", command=lambda: [root.destroy(), open_student_login()])
    btn_login.pack(pady=10, padx=50, fill="x")

    btn_login.bind("<Enter>", lambda e: on_enter(e, btn_login))
    btn_login.bind("<Leave>", lambda e: on_leave(e, btn_login))

    root.mainloop()

if __name__ == "__main__":
    main()
