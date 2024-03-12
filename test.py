import tkinter as tk

class App:
    def __init__(self, master):
        self.master = master
        self.entries = []
        self.create_widgets()

    def create_widgets(self):
       
        for i in range(30):
            row = []
            for j in range(2):
                entry = tk.Entry(self.master)
                entry.grid(row=i, column=j)
                row.append(entry)
            self.entries.append(row)

        
        ok_button = tk.Button(self.master, text="Ок", command=self.save_data)
        ok_button.grid(row=14, column=0, columnspan=2)

    def save_data(self):
        
        with open("data.txt", "w") as f:
            for row in self.entries:
                print(row[0].get(), row[1].get())
                f.write(f'ORG 0x{row[0].get()} \n')
                f.write(f'WORD 0x{row[1].get()} \n')

root = tk.Tk()
app = App(root)
root.mainloop()
