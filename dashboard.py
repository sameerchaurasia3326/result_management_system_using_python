from tkinter import *
from PIL import Image, ImageTk   # pip install pillow
from admin_login import AdminLogin   
from course import CourseClass  # Import the course module
from student import StudentClass  # Import the course module
from result import resultClass  # Import the course module
from report import reportClass


class RMS:
# ✅ Function to Handle Login Before Showing Dashboard
    def main():
       root = Tk()
       login_window = AdminLogin(root)
       root.mainloop()
    def __init__(self, root):
        self.root = root
        self.root.title("Result Management System")
        self.root.geometry("1350x700+0+0")
        self.root.config(bg="white")

        # === Load Icon/Image ===
        self.logo = Image.open("images/circular_logo.png")  # Open the image file
        self.logo = self.logo.resize((50, 50))  # Resize to (50, 50) pixels
        self.logo_dash = ImageTk.PhotoImage(self.logo)

        # -- Title Label --
        self.title_label = Label(self.root, text="Student Result Management System", padx=15,
                                 image=self.logo_dash, compound=LEFT,  
                                 font=("Goudy Old Style", 20, "bold"), bg="#033054", fg="white")
        self.title_label.place(x=0, y=0, relwidth=1, height=50)

        # == LabelFrame (Items) ==
        M_Frame = LabelFrame(self.root, text="Items", 
                             font=("Times New Roman", 20, "bold"), 
                             bg="white", fg="black", bd=3, relief=RIDGE)  
        M_Frame.place(x=0, y=80, relwidth=1, height=80)  

        # === Buttons ===
        btn_course = Button(M_Frame, text="Course", font=("Arial", 14, "bold"), 
                            bg="#0b5377", fg="black", activebackground="#1287A5", 
                            activeforeground="blue", cursor="hand2", command=self.add_course, bd=2, padx=10)
        btn_course.place(x=140, y=10, width=200, height=40)

        btn_student = Button(M_Frame, text="Student", font=("Arial", 14, "bold"), 
                             bg="#0b5377", fg="black", activebackground="#1287A5", 
                             activeforeground="blue", cursor="hand2",command=self.add_student, bd=2, padx=10)
        btn_student.place(x=440, y=10, width=200, height=40)

        btn_Result = Button(M_Frame, text="Result", font=("Arial", 14, "bold"), 
                            bg="#0b5377", fg="black", activebackground="#1287A5", 
                            activeforeground="blue", cursor="hand2",command=self.add_result, bd=2, padx=10)
        btn_Result.place(x=740, y=10, width=200, height=40)

        btn_Veiw = Button(M_Frame, text="View Student Result", font=("Arial", 14, "bold"), 
                          bg="#0b5377", fg="black", activebackground="#1287A5", 
                          activeforeground="blue", cursor="hand2",command=self.add_report, bd=2, padx=10)
        btn_Veiw.place(x=1040, y=10, width=200, height=40)

        btn_Logout = Button(M_Frame, text="Logout", font=("Arial", 14, "bold"), 
                            bg="#0b5377", fg="black", activebackground="#1287A5", 
                            activeforeground="blue", cursor="hand2", bd=2, padx=10)
        btn_Logout.place(x=1340, y=10, width=200, height=40)

        # == Content Image ==
        self.bg_img = Image.open("images/bg_image.webp")
        self.bg_img = self.bg_img.resize((1700, 700), Image.Resampling.LANCZOS)
        self.bg_img = ImageTk.PhotoImage(self.bg_img)

        self.lbl_bg = Label(self.root, image=self.bg_img)
        self.lbl_bg.place(x=5, y=170, width=1700, height=700)

        # == Update Details ==
        self.lbl_course = Label(self.root, text="Number of Course\n{ 0 }", font=('Goudy Old Style', 20),
                                bd=10, relief=RIDGE, bg="#01579B")
        self.lbl_course.place(x=10, y=880, width=500, height=150)

        self.lbl_Student = Label(self.root, text="Total Students\n{ 0 }", font=('Goudy Old Style', 20),
                                 bd=10, relief=RIDGE, bg="#002244")
        self.lbl_Student.place(x=600, y=880, width=500, height=150)

        self.lbl_Result = Label(self.root, text="Total Results\n{ 0 }", font=('Goudy Old Style', 20),
                                bd=10, relief=RIDGE, bg="#038074")
        self.lbl_Result.place(x=1190, y=880, width=500, height=150)

        # == Footer ==
        self.footer_label = Label(self.root, text="Developed by Sameer | Student Result Management System",
                                  font=("Goudy Old Style", 12), bg="#033054", fg="white")
        self.footer_label.pack(side=BOTTOM, fill=X)

    # ** Move this function outside __init__ **
    def add_course(self):
        if hasattr(self, "new_win") and self.new_win.winfo_exists():
            self.new_win.lift()  # Bring existing window to front
        else:
            self.new_win = Toplevel(self.root)
            self.new_win.grab_set()  # Prevents multiple clicks opening new windows
            self.new_obj = CourseClass(self.new_win)
    
    def add_student(self):
        if hasattr(self, "new_win") and self.new_win.winfo_exists():
            self.new_win.lift()  # Bring existing window to front
        else:
            self.new_win = Toplevel(self.root)
            self.new_win.grab_set()  # Prevents multiple clicks opening new windows
            self.new_obj = StudentClass(self.new_win)


    def add_result(self):
        if hasattr(self, "new_win") and self.new_win.winfo_exists():
            self.new_win.lift()  # Bring existing window to front
        else:
            self.new_win = Toplevel(self.root)
            self.new_win.grab_set()  # Prevents multiple clicks opening new windows
            self.new_obj = resultClass(self.new_win)
    

    def add_report(self):
        if hasattr(self, "new_win") and self.new_win.winfo_exists():
            self.new_win.lift()  # Bring existing window to front
        else:
            self.new_win = Toplevel(self.root)
            self.new_win.grab_set()  # Prevents multiple clicks opening new windows
            self.new_obj = reportClass(self.new_win)  # ✅ Use reportClass instead of resultClass




