from tkinter import *

root = Tk()
root.title("SpEd Message Builder")

# Window
window_width = 400
window_height = 500
geo = str(window_width) + "x" + str(window_height)
root.geometry(geo)

# Values for Clear button
clearRequest_button_text = "x"
clearRequest_label_text = "Close this request builder"

"""
REQUESTS MENU
"""
blue = "#c9daf8"
f_status_change = Frame(root)

red = "#f4cccc"
#f_make_DNQ = Frame(root)

purple = "#d9d2e9"
f_record_change = Frame(root, bg=purple)

orange = "#fce5cd"
f_add = Frame(root, bg=orange)

# STAFF ROLE DROPDOWN OPTIONS
staff_roles = ["...",
    "Site",
    "Psych",
    "Special Ed. Teacher",
    "Licensed Speech-Language Pathologist",
    "Speech-Language Pathologist with Valid Credential",
    "Occupational Therapist",
    "Behavior Intervention Specialist",
    "Physical Education Teacher",
    "General Education Teacher"]

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
# END OF FN: input_reqest_details

"""
FN PURPOSE: Set up frames.
"""
def configure_frames(frame_list, bg_color):
    for frame in frame_list:
        frame["bg"] = bg_color
    frame_list[0].pack(anchor=W, padx=10, pady=5)
# END OF FN: configure_frames

"""
FN PURPOSE: Set up entry boxes.
"""
entry_width_size = 20 # Size of an entry box
def configure_entries(entry_list, width):
    """
    for i in range(1, len(entry_list)-1):
        entry_list[i].config(width=width)
    """
    for entry in entry_list:
        entry.config(width=width)
# END OF FN: configure_entries

"""
FN PURPOSE: Reset one entry box.
"""
def reset_entry(entry_name):
    entry_name.delete(0,"end")
    entry_name.insert(0, "")
# END OF FN: reset_entry

"""
FN PURPOSE: Reset multiple entry boxes.
"""
def clear_fields(fields_list):
    for i in range(1, 4+1):
        reset_entry(fields_list[i])
    fields_list[5].set("...")
# END OF FN: clear_fields

"""
FN PURPOSE: Destroy the widgets for this menu option.
"""
def clear_frames(frame_list):
    for frame in frame_list:
        frame.destroy()
# END OF FN: clear_frames

"""
FN PURPOSE: Write a note that describes the request,
the actions taken to complete the request,
and any other comments or concerns.
"""
def write_note(field_list, actions, note_frame, bg_color):
    note_frame.pack()

    header = "Note for " + field_list[1].get().strip() + ", " + field_list[2].get().strip()
    l = Label(note_frame, text=header, bg=bg_color, font=("Courier New", 12))
    l.grid(row=0, column=0, columnspan=2)

    clearFields_button = Button(note_frame, text="Clear Fields")
    clearFields_button["command"] = lambda: clear_fields(field_list)
    clearFields_button.grid(row=1, column=0, columnspan=2)

    textbox = Text(note_frame)
    textbox.config(width=50, height=50)
    textbox.grid(row=2, column=0, columnspan=2)

    line = field_list[3].get().strip() + ", " + field_list[5].get().strip() + " requested: " + field_list[0] + "\n"
    textbox.insert("end", line)

    line = "\"" + field_list[4].get().strip() + "\"\n\n"
    textbox.insert("end", line)

    for i in range(0, len(actions)):
        textbox.insert("end", actions[i])
        if (i > 0 and i < len(actions)-1):
            textbox.insert("end", "\n")
# END OF FN: write_note

"""
FN PURPOSE: Make a button.
When pressed, put a Note template in an editable textbox.
"""
def make_write_button(write_button, field_list, actions,
    frame_list, bg_color):
    write_button["text"] = "Write Note"
    write_button["command"] = lambda: write_note(field_list, actions,
    frame_list[2], bg_color)
    write_button.grid(row=6, column=1)
# END OF FN: make_write_button

"""
FN PURPOSE: Make a button.
When pressed, the widgets for this menu option will be destroyed.
"""
def make_clearFrames_button(clearRequest_button, frame_list, bg_color):
    clearRequest_button["text"] = clearRequest_button_text
    clearRequest_button["command"] = lambda: clear_frames(frame_list)
    clearRequest_button.grid(row=0, column=0, sticky=W)
    l = Label(frame_list[0], bg=bg_color)
    l["text"] = clearRequest_label_text
    l.grid(row=0, column=1, sticky=W)
# END OF FN: make_clearFrames_button

"""
FOLLOW UP MENU
"""
# Follow Up
pink = "#ead1dc"
f_follow_up = Frame(root, bg=pink)

"""
FN PURPOSE: Get user input about a follow up.
- unaffirmed/unsigned IEP/amendment
"""
def input_follow_details(fields_list, input_frame, bg_color):
    # FRAME FOR USER INPUT
    input_frame.pack()
    r = 0 # Row placement

    # TITLE
    title_text = fields_list[0] + " " + fields_list[1]
    l = Label(input_frame, text=title_text, bg=bg_color, font=("Courier New", 12))
    l.grid(row=r, column=0, columnspan=2)

    # USER INPUT
    text = "Case Manager"
    l = Label(input_frame, text=text, bg=bg_color)
    l.grid(row=r+1, column=0)
    fields_list[2].grid(row=r+2,column=0)

    text = "Date"
    l = Label(input_frame, text=text, bg=bg_color)
    l.grid(row=r+1, column=1)
    fields_list[3].grid(row=r+2, column=1)

    text = "Student LN"
    l = Label(input_frame, text=text, bg=bg_color)
    l.grid(row=r+3, column=0)
    fields_list[4].grid(row=r+4, column=0)

    text = "Student FN"
    l = Label(input_frame, text=text, bg=bg_color)
    l.grid(row=r+3, column=1)
    fields_list[5].grid(row=r+4, column=1)

    text = "SEIS ID"
    l = Label(input_frame, text=text, bg=bg_color)
    l.grid(row=r+5, column=0)
    fields_list[6].grid(row=r+6, column=0)
# END OF FN: input_follow_details

"""
FN PURPOSE: Write a note that describes the follow up.
"""
def write_message(field_list, note_frame, bg_color):
    note_frame.pack()

    header = field_list[0] + " " + field_list[1]
    l = Label(note_frame, text=header, bg=bg_color, font=("Courier New", 12))
    l.grid(row=0, column=0, columnspan=2)

    clearFields_button = Button(note_frame, text="Clear Fields")
    clearFields_button["command"] = lambda: clear_fields(field_list)
    clearFields_button.grid(row=1, column=0, columnspan=2)

    textbox = Text(note_frame)
    textbox.config(width=50, height=50)
    textbox.grid(row=2, column=0, columnspan=2)

    if field_list[0] == "Unaffirmed":
        action = "Is this " + field_list[1] + " ready to be affirmed?"
    elif field_list[0] == "Unsigned":
        action = "Are you still waiting for a signture for this " + field_list[1] + "?"

    line = "Hello, " + field_list[2].get().strip() + ".\n\n"
    textbox.insert("end", line)

    line = "I noticed that you have an " + field_list[0] + " " + field_list [1]
    line += " for " + field_list[5].get().strip() + " " + field_list[4].get().strip()
    line += ", SEIS ID " + field_list[6].get().strip() + "."
    line += "\n\nThe " + field_list[1] + " Date is " + field_list[3].get().strip() + "."
    line += "\n\n" + action + "\n"

    textbox.insert("end", line)

# END OF FN: write_message

"""
FN PURPOSE: Make a button for follow up message.
When pressed, put a message template in an editable textbox.
"""
def make_follow_write_button(write_button, field_list,
    frame_list, bg_color):
    write_button["text"] = "Write Note"
    write_button["command"] = lambda: write_message(field_list,
    frame_list[2], bg_color)
    write_button.grid(row=6, column=1)
# END OF FN: make_follow_write_button