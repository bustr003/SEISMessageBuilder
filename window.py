# FILE window.py
"""
- Set up the Tkinter window
- Options for colors
- Create a frame for each menu option
- Secondary functions used by each menu option's primary function
"""

from tkinter import *
from tkinter import ttk

root = Tk()
root.iconbitmap(r"images\bunny_face.ico") # Icon to display on the title bar
root.title("SpEd Message Builder") # Text to display on the title bar

# Window geometry
window_width = 420
window_height = 610
screen_width = root.winfo_screenwidth() # Get width of the monitor
screen_height = root.winfo_screenheight() # Get width of the monitor
x_pop = screen_width/4 # The x coordinate of the top left corner
y_pop = screen_height/4 # The y coordinate of the top left corner
root.geometry(f"{window_width}x{window_height}+{int(x_pop)}+{int(y_pop)}")

textbox_width = 50
textbox_height = 18

# Values for Clear button
clear_request_button_text = "x"
clear_request_label_text = "Close this builder before opening a new one"

# Index Page
index_text = "\nWelcome to the Special Education Message Builder!"
index_text += "\nUse this tool to generate messages using templates."
index_text += "\n\nRequest:\nAn admin note for a SEIS request"
index_text += "\n\nFollow Up:\nA message for unaffirmed/unsigned IEPs/amendments"
index_text += "\n\nMeeting Alert:\nA message for upcoming/overdue meetings"

f_index = Frame(root)
l = Label(f_index, text=index_text, font=("Calibri", 12))
f_index.pack()
l.pack()

index_image = PhotoImage(file = r"images\bunny_pixel.png")
l = Label(image=index_image)
l.pack(pady=10)

"""
COLORS
- for backgrounds, etc
"""
red = "#f4cccc"
orange = "#fce5cd"
yellow = "#fff2cc"
green = "#d9ead3"
blue = "#c9daf8"
purple = "#d9d2e9"
pink = "#ead1dc"
dark_red = "#a61c00"

"""
FRAMES
"""
f_record_change = Frame(root)
f_add_student = Frame(root)
f_status_change = Frame(root)
f_exit_student = Frame(root)
f_follow_up = Frame(root)
f_signature = Frame(root)
f_glossary = Frame(root)

window_frames = []
window_frames.append(f_record_change)
window_frames.append(f_add_student)
window_frames.append(f_status_change)
window_frames.append(f_exit_student)
window_frames.append(f_follow_up)
window_frames.append(f_signature)
window_frames.append(f_glossary)

"""
FN PURPOSE: Hide all frames to make the window clean
for a new frame.
To be run each time a menu option is selected.
"""
def hide_all_frames():
    f_index.pack_forget()

    for frame in window_frames:
        frame.place_forget()
# END OF FN hide_all_frames

"""
===================
Functions for
- Record Change
- Add Student
- Status Change
- Exit Student
===================
"""

"""
FN PURPOSE: Set up frames.
"""
def configure_frames(frame_list, bg_color):
    for frame in frame_list:
        frame["bg"] = bg_color
    frame_list[0].pack(anchor=W, padx=10, pady=5)
# END OF FN configure_frames

"""
FN PURPOSE: Set up entry boxes.
"""
entry_width_size = 20 # Size of an entry box
def configure_entries(entry_list, width):
    for entry in entry_list:
        if entry.get() == "SEIS_ID SSID LAST_NAME, FIRST NAME":
            entry.config(width=60)
        else:
            entry.config(width=width)
# END OF FN configure_entries

# STAFF ROLE DROPDOWN OPTIONS
staff_roles = [
    "...",
    "Site",
    "Psych",
    "Special Ed. Teacher",
    "Licensed Speech-Language Pathologist",
    "Speech-Language Pathologist with Valid Credential",
    "Occupational Therapist",
    "Behavior Intervention Specialist",
    "Physical Education Teacher",
    "General Education Teacher",
    "Teacher of Deaf/Hard of Hearing"
]

"""
FN PURPOSE: Get user input about the request.
"""
def input_request_details(fields_list, role_options, input_frame, bg_color):
    # FRAME FOR USER INPUT
    input_frame.pack()
    r = 0 # Row placement

    # TITLE
    l = Label(input_frame, text=fields_list[0], bg=bg_color, font=("Courier New", 12))
    l.grid(row=r, column=0, columnspan=2)

    # USER INPUT
    text = "Student Last Name"
    l = Label(input_frame, text=text, bg=bg_color)
    l.grid(row=r+1, column=0)
    fields_list[1].grid(row=r+2,column=0)

    text = "Student First Name"
    l = Label(input_frame, text=text, bg=bg_color)
    l.grid(row=r+1, column=1)
    fields_list[2].grid(row=r+2, column=1)

    text = "Requester Full Name"
    l = Label(input_frame, text=text, bg=bg_color)
    l.grid(row=r+3, column=0)
    fields_list[3].grid(row=r+4, column=0)

    text = "Requester Role"
    l = Label(input_frame, text=text, bg=bg_color)
    l.grid(row=r+3, column=1)
    fields_list[5].set(staff_roles[0])
    role_options.grid(row=r+4, column=1)

    text = "Requester Comment"
    l = Label(input_frame, text=text, bg=bg_color)
    l.grid(row=r+5, column=0)
    fields_list[4].grid(row=r+6, column=0)
# END OF FN input_reqest_details

"""
FN PURPOSE: Dropdown for change requested in a record change request
"""
def input_dropdown(field, option_list, option_dropdown, r, c):
    field.set(option_list[0])
    option_dropdown.grid(row=r, column=c)
# END OF FN input_dropdown

"""
FN PURPOSE: Reset one entry box.
"""
def reset_entry(entry_name):
    entry_name.delete(0,"end")
    entry_name.insert(0, "")
# END OF FN reset_entry

"""
FN PURPOSE: Reset multiple entry boxes.
"""
def clear_fields(fields_list):
    for i in range(1, 4+1):
        reset_entry(fields_list[i])
    fields_list[5].set("...")
# END OF FN clear_fields

"""
FN PURPOSE: Destroy the widgets for this menu option.
"""
def clear_frames(frame_list):
    for frame in frame_list:
        frame.destroy()
    hide_all_frames()
    f_index.pack()
    l.pack()
# END OF FN clear_frames

"""
FN PURPOSE: Make a button.
When pressed, the widgets for this menu option will be destroyed.
"""
def make_clear_frames_button(clear_request_button, frame_list, bg_color):
    clear_request_button["text"] = clear_request_button_text
    clear_request_button["command"] = lambda: clear_frames(frame_list)
    clear_request_button.grid(row=0, column=0, sticky=W)
    l = Label(frame_list[0], bg=bg_color)
    l["text"] = clear_request_label_text
    l.grid(row=0, column=1, sticky=W)
# END OF FN make_clear_frames_button

"""
FN PURPOSE: Write a note that describes the request,
the actions taken to complete the request,
and any other comments or concerns.
- For status changes, adding a student, and exiting a student
"""
def write_note(field_list, actions, note_frame, bg_color):
    note_frame.pack()

    header = "Note for " + field_list[1].get().strip() + ", " + field_list[2].get().strip()
    l = Label(note_frame, text=header, bg=bg_color, font=("Courier New", 12))
    l.grid(row=0, column=0, columnspan=2)

    # BUTTON TO RESET THE FIELDS
    clearFields_button = Button(note_frame, text="Clear Fields")
    clearFields_button["command"] = lambda: clear_fields(field_list)
    clearFields_button.grid(row=1, column=0, columnspan=2)

    # TEXTBOX
    textbox = Text(note_frame, wrap="word")
    textbox.config(width=textbox_width, height=textbox_height)
    textbox.grid(row=2, column=0, columnspan=2)

    line = field_list[3].get().strip() + ", " + field_list[5].get().strip() + " requested: " + field_list[0] + "\n"
    textbox.insert("end", line)

    line = "\"" + field_list[4].get().strip() + "\"\n\n"
    textbox.insert("end", line)

    for i in range(0, len(actions)):
        textbox.insert("end", actions[i])
        if (i < len(actions)-1):
            textbox.insert("end", "\n")
# END OF FN write_note

"""
FN PURPOSE: Make a button.
When pressed, put a Note template in an editable textbox.
- For status changes, adding a student, and exiting a student.
"""
def make_write_button(write_button, field_list, actions,
    frame_list, bg_color):
    write_button["text"] = "Write Note"
    write_button["command"] = lambda: write_note(field_list, actions,
    frame_list[2], bg_color)
    write_button.grid(row=6, column=1)
# END OF FN make_write_button

# EOF window.py