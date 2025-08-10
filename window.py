import tkinter as tk
from weaselMath import wpt

window = tk.Tk()
window.title("Weasel Period Tracker")
window.geometry("300x500")
window.configure(bg="#1A1A27")

label = tk.Label(
    window,
    text="When was the last time you projected your period onto Weaesl? (Ex: 02/15/2025)",
    wraplength=280,
    fg="White")
label.pack(anchor="center", padx=20)
label.configure(bg="#1A1A27")

input_field = tk.Entry(window, justify="center")
input_field.pack()

happyWeasel = tk.PhotoImage(file="happyWeasel.png")
happyWeaselLabel = tk.Label(window, image=happyWeasel)

def get_input_value():
    global user_input
    global input_field
    global label
    global happyWeaselLabel

    user_input = input_field.get()
    print(f"User entered: {user_input}")

    label.pack_forget()
    input_field.pack_forget()
    submit_button.destroy()
    happyWeaselLabel.pack_forget()

    label = tk.Label(
        window,
        text="What about the time before that? ",
        wraplength=280,
        fg="White"
    )
    label.pack()
    label.configure(bg="#1A1A27")

    input_field = tk.Entry(window, justify="center")
    input_field.pack()

    def get_input_value2():
        global user_input2
        global input_field
        global label
        global happyWeaselLabel

        user_input2 = input_field.get()
        print(f"User entered: {user_input2}")

        label.pack_forget()
        input_field.pack_forget()
        submit_button2.destroy()
        happyWeaselLabel.pack_forget()

        label = tk.Label(
            window,
            text="And the time before that? ",
            wraplength=280,
            fg="White"
        )
        label.pack()
        label.configure(bg="#1A1A27")

        input_field = tk.Entry(window, justify="center")
        input_field.pack()

        def get_input_value3():
            global user_input3
            global input_field
            global label
            global happyWeaselLabel

            user_input3 = input_field.get()
            print(f"User entered: {user_input3}")

            label.pack_forget()
            input_field.pack_forget()
            submit_button3.destroy()
            happyWeaselLabel.pack_forget()

            label = tk.Label(
                window,
                text="And finally, the one before that: ",
                wraplength=280,
                fg="White"
            )
            label.pack()
            label.configure(bg="#1A1A27")

            input_field = tk.Entry(window, justify="center")
            input_field.pack()

            def get_input_value4():
                global user_input4
                global input_field
                global label
                global happyWeaselLabel

                user_input4 = input_field.get()
                print(f"User entered: {user_input4}")
                result = wpt(user_input, user_input2, user_input3, user_input4)

                label.pack_forget()
                input_field.pack_forget()
                submit_button4.destroy()
                happyWeaselLabel.pack_forget()

                labelDone = tk.Label(
                    window,
                    text=f"You'll have to project your period onto Weasel on {result}",
                    wraplength=280,
                    fg="White"
                )
                labelDone.pack()
                labelDone.configure(bg="#1A1A27")

                def changeFace():
                    global painWeasel

                    labelDone.pack_forget()
                    project_button.pack_forget()
                    happyWeaselLabel.pack_forget()

                    painWeasel = tk.PhotoImage(file="painWeasel.png")
                    painWeaselLabel = tk.Label(window, image=painWeasel)
                    painWeaselLabel.pack(pady=20)

                global project_button
                project_button = tk.Button(window, text="Early Project", command=changeFace)
                project_button.pack()

                happyWeaselLabel = tk.Label(window, image=happyWeasel)
                happyWeaselLabel.pack(side="bottom",pady=20)

            global submit_button4
            submit_button4 = tk.Button(window, text="Submit", command=get_input_value4)
            submit_button4.pack()

            happyWeaselLabel = tk.Label(window, image=happyWeasel)
            happyWeaselLabel.pack(side="bottom",pady=20)

        global submit_button3
        submit_button3 = tk.Button(window, text="Submit", command=get_input_value3)
        submit_button3.pack()

        happyWeaselLabel = tk.Label(window, image=happyWeasel)
        happyWeaselLabel.pack(side="bottom",pady=20)
    
    global submit_button2
    submit_button2 = tk.Button(window, text="Submit", command=get_input_value2)
    submit_button2.pack()

    happyWeaselLabel = tk.Label(window, image=happyWeasel)
    happyWeaselLabel.pack(side="bottom",pady=20)

submit_button = tk.Button(window, text="Submit", command=get_input_value)
submit_button.pack()

happyWeaselLabel.pack(side="bottom",pady=20)

window.mainloop()