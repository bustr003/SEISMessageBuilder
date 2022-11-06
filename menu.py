# FILE: menu.py
"""
PROGRAM TITLE: MessageBuilderGUI
ALTERNATE TITLES:
- SEISMessageBuilder
- SpEd Message Builder
AUTHOR: Mhealyssah Bustria
DATE CREATED: unknown - on personal laptop
DATE ACCESSED ON WORK COMPUTER: 10/28/2022
FILES
1) menu.py: The main file.
- - Creates the home page and menu options.
- - RUN FROM THIS FILE!!!
2) window.py: The GUI window.
- - Creates the GUI window.
- - Contains the more complex functions used by the menu options.
Files for basic functions
3) add.py: for add requests
4) status.py:  for status change requests.
5) record.py: for record change requests.
6) exit_student.py: for exit requests.
7) follow_up.py: for unaffirmed/unsigned IEPs/Amendments
"""

import window as w # Tkinter window
import status_change # Request Type: Eligibility Change
import record_change # Request Type: Record Change
import add_student # Request Type: Add Student
import exit_student # Request Type: Exit
import follow_up # Unaffirmed/Unsigned IEP/Amendment

# Main Menu
main_menu = w.Menu(w.root)
w.root.config(menu=main_menu)

"""
MENU OPTION FUNCTIONS:
Each menu option has an associated function.
Each function does:
- Hide all frames to make the window fresh.
- Place a frame that fills the screen.
- Run the correct function from the correct file.
"""
r_width = r_height = 1
r_y = 0 # Top padding

def click_record_change(req_type, bg_color):
    w.hide_all_frames()
    w.f_record_change.place(relwidth=r_width, relheight=r_height, rely=r_y)
    record_change.record_change(req_type, bg_color)

def click_add_student(req_type, bg_color):
    w.hide_all_frames()
    w.f_add_student.place(relwidth=r_width, relheight=r_height, rely=r_y)
    add_student.add_student(req_type, bg_color)

def click_status_change(req_type, bg_color):
    w.hide_all_frames()
    w.f_status_change.place(relwidth=r_width, relheight=r_height, rely=r_y)
    status_change.status_change(req_type, bg_color)

def click_exit_student(req_type, bg_color):
    w.hide_all_frames()
    w.f_exit_student.place(relwidth=r_width, relheight=r_height, rely=r_y)
    exit_student.exit_student(req_type, bg_color)

def click_follow_up(follow_type, follow_item):
    w.hide_all_frames()
    w.f_follow_up.place(relwidth=r_width, relheight=r_height, rely=r_y)
    follow_up.follow_up(follow_type, follow_item)
# END OF FUNCTIONS: Menu options

# Menu: Request
type_menu = w.Menu(main_menu)
main_menu.add_cascade(label="Request", menu=type_menu)

# --- Request: Record Change
type_menu.add_command(label="Record Change",
                      command=lambda:click_record_change("Record Change", w.blue))

type_menu.add_separator()

# --- Request: Add
type_menu.add_command(label="Add Student",
                      command=lambda:click_add_student("Add Student", w.orange))

type_menu.add_separator()

# --- Request: Status
type_menu.add_command(label="Status: Make Eligible",
                      command=lambda:click_status_change("Status: Make Eligible", w.green))

type_menu.add_command(label="Status: Make DNQ",
                      command=lambda:click_status_change("Status: Make DNQ", w.red))

type_menu.add_command(label="Status: AP Declined",
                      command=lambda:click_status_change("Status: Assessment Plan Declined", w.red))

type_menu.add_command(label="Status: Eligible but NotProvSvcs",
                      command=lambda:click_status_change("Status: Eligible but NotProvSvcs", w.red))

type_menu.add_separator()

# --- Request: Exit
type_menu.add_command(label="Exit 70",
                      command=lambda:click_exit_student("Exit 70", w.purple))


type_menu.add_separator()

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

# EOF menu.py