import tkinter as tk
from tkinter import messagebox
from tkinter import ttk

class gradeAverageCalculator:
    def __init__(self):
        self.root = tk.Tk()
        
        #window
        self.root.title("CMSC 437 Calculator")
        self.root.geometry('300x180')
        self.root.resizable(True, True)
        
        #creating the frames
        self.frame1 = tk.Frame(self.root)
        self.frame1.pack(pady = 5)

        self.frame2 = tk.Frame(self.root)
        self.frame2.pack(pady = 5)

        self.frame3 = tk.Frame(self.root)
        self.frame3.pack(pady = 5)

        self.frame4 = tk.Frame(self.root)
        self.frame4.pack(pady = 5)

        self.frame5 = tk.Frame(self.root)
        self.frame5.pack(pady = 5)
        
        #labels and entry box
        self.subject1_label = tk.Label(self.frame1, text="Bio: ")
        self.subject1_label.pack(side=tk.LEFT, padx = 8)

        self.subject1 = tk.Entry(self.frame1, width=10)
        self.subject1.pack(side=tk.LEFT, padx = 5)

        self.subject2_label = tk.Label(self.frame2, text="Math:")
        self.subject2_label.pack(side=tk.LEFT, padx = 5)

        self.subject2 = tk.Entry(self.frame2, width=10)
        self.subject2.pack(side=tk.LEFT, padx = 5)

        #label for output
        self.average_label = tk.Label(self.frame3, text="Average:")
        self.average_label.pack(side=tk.LEFT, padx = 8)

        self.average_result = tk.Label(self.frame3, text="")
        self.average_result.pack(side=tk.LEFT, padx = 5)

        #calculate and quit button
        self.calculate_btn = ttk.Button(self.frame4, text="Calculate", command=self.calculate)
        self.calculate_btn.pack(side=tk.LEFT, padx = 1, pady = 5)

        self.quit_btn = ttk.Button(self.frame4, text="Quit", command=self.root.destroy)
        self.quit_btn.pack(side=tk.LEFT, padx = 1, pady = 5)

        self.root.mainloop()

    #caluculate funtionality
    def calculate(self):
        try:
            bio_grade = float(self.subject1.get())
            math_grade = float(self.subject2.get())

            if not (0 <= bio_grade <= 100) or not (0 <= math_grade <= 100):
                messagebox.showerror("Error", "Grades must be between 0 and 100.")
                return

            average_grade = (bio_grade + math_grade) / 2
            self.average_result.configure(text=f"{average_grade:.2f}")

        except ValueError:
            messagebox.showerror("Error", "Please enter numeric grades. Grades are not correct!")
   

#this is sthe main prohrams
if __name__ == "__main__":
    app = gradeAverageCalculator()
