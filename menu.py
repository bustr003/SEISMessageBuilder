# FILE menu.py
"""
PROGRAM TITLE: MessageBuilderGUI
ALTERNATE TITLES:
- SEISMessageBuilder
- SpEd Message Builder
AUTHOR: Mhealyssah Bustria
DATE CREATED: unknown - on personal laptop
DATE ACCESSED ON WORK COMPUTER: 10/28/2022

=== FILES ===

Files for setting up the GUI
1) menu.py The main file.
- - Creates the home page and menu options.
- - RUN FROM THIS FILE!!!
2) window.py The GUI window & secondary functions
- - Creates the GUI window.
- - Contains functions that are shared by multiple menu options.

Files for the primary functions and own functions of each menu option
3) add.py For add requests
4) status.py For status change requests.
5) record.py For record change requests.
6) exit_student.py For exit requests.
7) follow_up.py For unaffirmed/unsigned IEPs/Amendments

Files for references
8) glossary.py An interactive glossary
"""

import window as w # Tkinter window

import record_change # Request Type: Record Change
import add_student # Request Type: Add Student
import status_change # Request Type: Eligibility Change
import exit_student # Request Type: Exit

import follow_up # Unaffirmed/Unsigned IEP/Amendment

import glossary # Terms and their definitions

# Main Menu
main_menu = w.Menu(w.root)
w.root.config(menu=main_menu)

"""
MENU OPTION FUNCTIONS
Each menu option has an associated function.
Each function does:
- Hide all frames to make the window fresh.
- Place a frame that fills the screen.
- Run the correct function from the correct file.
"""
r_width = r_height = 1
r_y = 0 # Top padding

# Requests
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

# Follow Ups
def click_follow_up(follow_type, follow_item):
    w.hide_all_frames()
    w.f_follow_up.place(relwidth=r_width, relheight=r_height, rely=r_y)
    follow_up.follow_up(follow_type, follow_item, w.pink)

# Resources
def click_glossary(bg_color):
    w.hide_all_frames()
    w.f_glossary.place(relwidth=r_width, relheight=r_height, rely=r_y)
    glossary.glossary(bg_color)
# END OF Menu Option Functions

"""
CREATE THE MENU OPTIONS
- Titles & Dropdowns
"""
# === Menu: Request ===
type_menu = w.Menu(main_menu)
main_menu.add_cascade(label="Request", menu=type_menu)

# --- Request: Record Change
type_menu.add_command(label="Record Change",
                      command=lambda:click_record_change("Record Change", w.blue))

type_menu.add_separator()

# --- Request: Add Student
type_menu.add_command(label="Add Student",
                      command=lambda:click_add_student("Add Student", w.orange))

type_menu.add_separator()

# --- Request: Status Change
type_menu.add_command(label="Status: Make Eligible",
                      command=lambda:click_status_change("Status: Make Eligible", w.green))

type_menu.add_command(label="Status: Make Ineligible",
                      command=lambda:click_status_change("Status: Make DNQ", w.red))

type_menu.add_command(label="Status: AP Declined",
                      command=lambda:click_status_change("Status: Assessment Plan Declined", w.red))

type_menu.add_command(label="Status: Eligible but NotProvSvcs",
                      command=lambda:click_status_change("Status: Eligible but NotProvSvcs", w.red))

type_menu.add_separator()

# --- Request: Exit Student
type_menu.add_command(label="Exit 70",
                      command=lambda:click_exit_student("Exit 70\nNo longer eligible", w.purple))

type_menu.add_command(label="Exit 74",
                      command=lambda:click_exit_student("Exit 74\nDrop Out/Not known to be continuing", w.purple))

type_menu.add_command(label="Exit 76",
                      command=lambda:click_exit_student("Exit 76\nTransfer, known to be continuing", w.purple))

type_menu.add_command(label="Exit 77",
                      command=lambda:click_exit_student("Exit 77\nDeceased", w.purple))

type_menu.add_command(label="Exit 78",
                      command=lambda:click_exit_student("Exit 78\nParent Withdrawal", w.purple))

type_menu.add_command(label="Exit 84",
                      command=lambda:click_exit_student("Exit 84\nPart C to B No parental consent", w.purple))

type_menu.add_command(label="Exit 85",
                      command=lambda:click_exit_student("Exit 85\nExited SPED Out-of-State", w.purple))           

type_menu.add_separator()

# === Menu: Follow Up ===
follow_menu = w.Menu(main_menu)
main_menu.add_cascade(label="Follow Up", menu=follow_menu)

# --- IEPs and Amendments
follow_menu.add_command(label="Unsigned IEP",
                        command=lambda: click_follow_up("Unsigned", "IEP"))
follow_menu.add_command(label="Unsigned Amendment",
                        command=lambda: click_follow_up("Unsigned", "Amendment"))
follow_menu.add_command(label="Unaffirmed IEP",
                        command=lambda: click_follow_up("Unaffirmed", "IEP"))
follow_menu.add_command(label="Unaffirmed Amendment",
                        command=lambda: click_follow_up("Unaffirmed", "Amendment"))

follow_menu.add_separator()

# --- Meeting Alerts
def open_popup():
   top = w.Toplevel(w.root)
   width = 300
   height = 100
   top.geometry(f"{width}x{height}")
   top.title("Oops!")
   l = w.Label(top, text="Meeting Alerts are under construction.", pady=height/2)
   l.pack()

follow_menu.add_command(label="Meeting Alerts",
                        command=open_popup)

# === Menu: Help ===
help_menu = w.Menu(main_menu)
main_menu.add_cascade(label="Help", menu=help_menu)
help_menu.add_command(label="Glossary",
                        command=lambda: click_glossary(w.yellow))

w.root.mainloop()

# EOF menu.py