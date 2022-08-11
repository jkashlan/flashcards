import tkinter as tk
import customtkinter

sets = {"set1":1,"set2":2, "set3":3, "set4":4, "set5":5}
class Edit(customtkinter.CTk):
    def __init__(self):
        super().__init__()
        
        self.geometry("500x300")
        self.title("Edit")
        self.minsize(300, 200)

        # create 2x2 grid system
        self.grid_rowconfigure(0, weight=1)
        self.grid_columnconfigure((0, 1), weight=1)

        self.textbox = tk.Text(master=self)
        self.textbox.grid(row=0,
                          column=0,
                          columnspan=2,
                          padx=20,
                          pady=(20, 0),
                          sticky="nsew")

        self.combobox = customtkinter.CTkComboBox(
            master=self, values=["set1.txt","set2.txt","set3.txt","set4.txt","set5.txt"])
        self.combobox.grid(row=1, column=0, padx=20, pady=20, sticky="ew")

        self.open_button = customtkinter.CTkButton(
            master=self, command=self.open_button_callback, text="Open")
        self.open_button.grid(row=1, column=1, padx=20, pady=20, sticky="ew")

        self.save_button = customtkinter.CTkButton(master=self,
                                                   command=self.save_callback,
                                                   text="Save")
        self.save_button.grid(row=2, column=1, padx=20, pady=20, sticky="ew")

        self.back_button = customtkinter.CTkButton(
            master=self, command=self.back_button_callback, text="Back")
        self.back_button.grid(row=2, column=0, padx=20, pady=20, sticky="ew")

    def open_button_callback(self):
        self.textbox.delete("1.0", tk.END)
        with open(self.combobox.get(), 'r') as f:
            lines = f.readlines()
            for line in lines:
                self.textbox.insert(tk.END, line)

    def save_callback(self):
        with open(self.combobox.get(), 'w') as f:
            f.write(self.textbox.get("1.0", tk.END))

    def back_button_callback(self):
        self.destroy()
        app = Prompt()
        app.mainloop()


class Prompt(customtkinter.CTk):
    def __init__(self):
        super().__init__()

        customtkinter.set_appearance_mode("dark")
        self.geometry("500x300")
        self.title('Start!')
        self.minsize(300, 200)
        self.grid_rowconfigure(0, weight=1)
        self.grid_columnconfigure((0, 1), weight=1)

        self.edit_btn = customtkinter.CTkButton(master=self,
                                                command=self.edit_callback,
                                                text='Edit Flashcards')
        self.practice_btn = customtkinter.CTkButton(
            master=self,
            command=self.practice_callback,
            text='Practice Flashcards')
        self.edit_btn.grid(row=0, column=0, padx=20, pady=20, sticky='ew')
        self.practice_btn.grid(row=0, column=1, padx=20, pady=20, sticky='ew')

        self.combobox = customtkinter.CTkComboBox(
            master=self, values=["set2.txt", "set1.txt","set3.txt","set4.txt","set5.txt",])
        self.combobox.grid(row=1, column=1, padx=20, pady=20, sticky="ew")

    def practice_callback(self):
        set = self.combobox.get()
        print(set)
        self.destroy()
        page3 = Practice(set)
        page3.mainloop()

    def edit_callback(self):
        self.destroy()
        page2 = Edit()
        page2.mainloop()


def readFile(file):
    with open(file, mode="r") as f:
        lines = f.readlines()
        print(lines)
        return lines


def retrieveCards(file):
    #retrieves the cards for review
    cards, wrking = [], []
    for line in readFile(file):
        wrking.append(line.rstrip())
    for card in wrking:
        if len(card) != 0:
            cards.append(card.split(':'))
    return (cards)


class Practice(customtkinter.CTk):
    def __init__(self, set):
        super().__init__()

        self.sets = {"set1.txt":1,"set2.txt":2, "set3.txt":3, "set4.txt":4, "set5.txt":5}
        self.geometry("500x300")
        self.title("review flashcards")
        self.minsize(300, 200)

        self.set = set
        self.level = self.sets[self.set]
        self.cardlist = retrieveCards(self.set)
        self.card = 0
        self.side = 0
        # create 2x2 grid system
        self.grid_rowconfigure(0, weight=1)
        self.grid_columnconfigure((0, 1), weight=1)

        self.label = customtkinter.CTkLabel(
            master=self, text=self.cardlist[self.card][self.side])
        self.label.grid(row=0,
                        column=0,
                        columnspan=2,
                        padx=20,
                        pady=(20, 0),
                        sticky="nsew")
        # next button
        self.nxtbutton = customtkinter.CTkButton(
            master=self, command=self.nxtbutton_callback, text="Next Card")
        self.nxtbutton.grid(row=1, column=1, padx=20, pady=20, sticky="ew")

        # back button
        self.backbutton = customtkinter.CTkButton(
            master=self, command=self.backbutton_callback, text="Back")
        self.backbutton.grid(row=3, column=0, columnspan=2, padx=20, pady=20, sticky="ew")

        # flip button
        self.flipbutton = customtkinter.CTkButton(
            master=self, command=self.flipbutton_callback, text="Flip Card")
        self.flipbutton.grid(row=1, column=0, padx=20, pady=20, sticky="ew")

        #correct button
        self.correctbutton = customtkinter.CTkButton(master=self, command=self.correct_callback, text="Correct")
        self.correctbutton.grid(row=2, column=0, padx=20, pady=20, sticky="ew")

        self.wrongbutton = customtkinter.CTkButton(master=self, command=self.wrong_callback, text="Wrong")
        self.wrongbutton.grid(row=2, column=1, padx=20, pady=20, sticky="ew")

    def nxtbutton_callback(self):
        if self.card < len(self.cardlist) - 1:
            self.card += 1
        else:
            self.card = 0
        self.side = 0
        self.label.configure(text=self.cardlist[self.card][self.side])

    def flipbutton_callback(self):
        lis = [1, 0]
        self.side = lis[self.side]
        self.label.configure(text=self.cardlist[self.card][self.side])

    def backbutton_callback(self):
        self.destroy()
        app = Prompt()
        app.mainloop()
    def correct_callback(self):
      keyss = list(self.sets)
      print(keyss)
      with open(keyss[self.level], 'a') as f:
        f.write('\n'+self.cardlist[self.card][0]+':'+self.cardlist[self.card][1])

    def wrong_callback(self):
      #print(self.cardlist[self.card])
      with open("set1.txt", 'a') as f:
        f.write('\n'+self.cardlist[self.card][0]+':'+self.cardlist[self.card][1])
      with open(self.set, "r") as f:
        self.file_input = f.readlines()
        with open(self.set, "w") as output: 
          
          print(self.file_input)
          for line in self.file_input:
            if line.strip("\n") != self.cardlist[self.card][0]+':'+self.cardlist[self.card][1]:
              output.write(line)
            else:
              print(line.strip("\n"))
      self.cardlist = retrieveCards(self.set)

app = Practice("set2.txt")
app.wrong_callback()
#print(app.line.strip("\n") != app.cardlist[app.card][0]+':'+app.cardlist[app.card][1])

