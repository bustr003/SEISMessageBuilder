import window as w # Tkinter window
import status # Request Type: Eligibility Change
import add # Request Type: Add Student
import record # Request Type: Record Change
import follow_up # Unaffirmed/Unsigned IEP/Amendment

# Index Page
index_text = "\nWelcome to the Special Education Message Builder!"
index_text += "\nUse this tool to generate messages using templates."
index_text += "\n\nRequest:\nAn admin note for a SEIS request"
index_text += "\n\nFollow Up:\nA message for unaffirmed/unsigned IEPs/amendments"
index_text += "\n\nMeeting Alert:\nA message for upcoming/overdue meetings"

f_index = w.Frame(w.root)
f_index.pack()
l = w.Label(f_index, text=index_text, font=("Calibri", 12))
l.pack()

# Main Menu
main_menu = w.Menu(w.root)
w.root.config(menu=main_menu)

"""
FN PURPOSE: Hide all frames to make the window clean
for a new frame.
To be run each time a menu option is selected.
"""
def hide_all_frames():
    f_index.pack_forget()

    w.f_add.place_forget()
    w.f_make_eligible.place_forget()
    w.f_make_DNQ.place_forget()
    w.f_record_change.place_forget()

    w.f_follow_up.place_forget()
# END OF FN: hide_all_frames

"""
MENU OPTION FUNCTIONS:
Each menu option has an associated function.
Each function does:
- Hide all frames to make the window fresh.
- Place a frame that fills the screen.
- Run the correct function from the correct file.
"""
r_width = r_height = 1
r_y = 0
def click_add():
    hide_all_frames()
    w.f_add.place(relwidth=r_width, relheight=r_height, rely=r_y)
    add.add()

def click_make_eligible():
    hide_all_frames()
    w.f_make_eligible.place(relwidth=r_width, relheight=r_height, rely=r_y)
    status.make_eligible()

def click_make_DNQ():
    hide_all_frames()
    w.f_make_DNQ.place(relwidth=r_width, relheight=r_height, rely=r_y)
    status.make_DNQ()

def click_record_change():
    hide_all_frames()
    w.f_record_change.place(relwidth=r_width, relheight=r_height, rely=r_y)
    record.record_change()

def click_follow_up(followType, followItem):
    hide_all_frames()
    w.f_follow_up.place(relwidth=r_width, relheight=r_height, rely=r_y)
    follow_up.follow_up(followType, followItem)
# END OF FUNCTIONS: Menu options

# Menu: Request
type_menu = w.Menu(main_menu)
main_menu.add_cascade(label="Request", menu=type_menu)

type_menu.add_command(label="Add Student", # green
                      command=click_add)

type_menu.add_separator()

type_menu.add_command(label="Status: Make Eligible", # blue
                      command=click_make_eligible)

type_menu.add_command(label="Status: Make DNQ", # red
                      command=click_make_DNQ)

type_menu.add_separator()

type_menu.add_command(label="Record Change", # grey
                      command=click_record_change)

# Menu: Follow Up
follow_menu = w.Menu(main_menu)
main_menu.add_cascade(label="Follow Up", menu=follow_menu)
follow_menu.add_command(label="Unsigned IEP",
                        command=lambda: click_follow_up("Unsigned", "IEP"))
follow_menu.add_command(label="Unsigned Amendment",
                        command=lambda: click_follow_up("Unsigned", "Amendment"))
follow_menu.add_command(label="Unaffirmed IEP",
                        command=lambda: click_follow_up("Unaffirmed", "IEP"))
follow_menu.add_command(label="Unaffirmed Amendment",
                        command=lambda: click_follow_up("Unaffirmed", "Amendment"))

# Menu: Meeting Alerts
alert_menu = w.Menu(main_menu)
main_menu.add_cascade(label="Meeting Alerts", menu=alert_menu)
alert_menu.add_command(label="Under construction!")

w.root.mainloop()