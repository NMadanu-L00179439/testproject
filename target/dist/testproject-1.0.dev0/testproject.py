from tkinter import *
from tkinter import ttk
import sys

sys.path.insert(
    0, '../ATU-Studies/githubdemo-Project/project-github/src/main/python/')


# Initializing the window
root_window = Tk()

# Formating the window
root_window.geometry('500x350')
root_window.configure(bg='#75420e', padx=10, pady=10)
root_window.resizable(False, False)
root_window.title('App Count Lines')


def userConfig():
    # tk.Label(text=user_name, bg="#e9e5cd", font=user_info).grid(
    #   row=2, column=1, padx=50, pady=50)
    numberOfWords = len(userFormValues['entry'].get().split())
    final_value = 'Number Of Words : ' + str(numberOfWords)
    userFormValues['user_output'].config(text=final_value)
    return final_value


# Greeting the user with Label and configure
greet_user = Label(root_window,
                   text="Hello, Welcome to word Count!",
                   bg="#e9e5cd",
                   font=('baskerville bold', 30, 'underline')
                   )
greet_user.pack()
# greet_user.pack()

userFormValues = {}

userFormValues['user_info'] = Label(root_window,
                                    text="Enter Text",
                                    bg="#ffffff",
                                    font=('baskerville bold', 20, 'italic')
                                    )

userFormValues['entry'] = Entry(root_window)


# Submit Button
userFormValues['submitButton'] = ttk.Button(root_window, text="SUBMIT",
                                            command=userConfig)
userFormValues['user_output'] = Label(root_window,
                                      bg="#e9e5cd",
                                      font=('baskerville', 25)
                                      )

for formValue in userFormValues:
    userFormValues[formValue].pack(anchor=W, padx=10, pady=5, fill=X)


# waiting for the events
root_window.mainloop()
