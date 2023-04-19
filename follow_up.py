# FILE follow_up.py
"""
Functions used only for following up on IEPs and Amendments
"""
import window as w

"""
FN PURPOSE: Get user input about a follow up on
- unaffirmed/unsigned IEP/amendment
"""
def input_follow_details(fields_list, input_frame, bg_color):
    # FRAME FOR USER INPUT
    input_frame.pack()
    r = 0 # Row placement

    # TITLE
    title_text = fields_list[0] + " " + fields_list[1]
    l = w.Label(input_frame, text=title_text, bg=bg_color, font=("Courier New", 12))
    l.grid(row=r, column=0, columnspan=2)

    # USER INPUT
    text = "Case Manager FN"
    l = w.Label(input_frame, text=text, bg=bg_color)
    l.grid(row=r+1, column=0)
    fields_list[2].grid(row=r+2,column=0)

    text = "Date"
    l = w.Label(input_frame, text=text, bg=bg_color)
    l.grid(row=r+1, column=1)
    fields_list[3].grid(row=r+2, column=1)

    text = "SEIS ID"
    l = w.Label(input_frame, text=text, bg=bg_color)
    l.grid(row=r+3, column=0)
    fields_list[4].grid(row=r+4, column=0)

    text = "Student Name"
    l = w.Label(input_frame, text=text, bg=bg_color)
    l.grid(row=r+5, column=0)
    fields_list[6].grid(row=r+6, column=0)
# END OF FN input_follow_details

"""
FN PURPOSE: Write a note that describes the follow up.
"""
def write_message(field_list, note_frame, bg_color):
    note_frame.pack()

    header = field_list[0] + " " + field_list[1]
    l = w.Label(note_frame, text=header, bg=bg_color, font=("Courier New", 12))
    l.grid(row=0, column=0, columnspan=2)

    # BUTTON TO CLEAR FIELDS
    def clear_follow_fields(field_list):
        for i in range(2, len(field_list)):
            field_list[i].delete(0,"end")
            field_list[i].insert(0, "")

    clearFields_button = w.Button(note_frame, text="Clear Fields")
    clearFields_button["command"] = lambda: clear_follow_fields(field_list)
    clearFields_button.grid(row=1, column=0, columnspan=2)

    # TEXTBOX
    textbox = w.Text(note_frame)
    textbox.config(width=w.textbox_width, height=w.textbox_height)
    textbox.grid(row=2, column=0, columnspan=2)

    if field_list[0] == "Unaffirmed":
        action = "Is this " + field_list[1] + " ready to be affirmed?"
    elif field_list[0] == "Unsigned":
        action = "Was the parent signature obtained for this " + field_list[1] + "?"

    line = "Hello, " + field_list[2].get().strip() + ".\n\n"
    textbox.insert("end", line)

    line = "I noticed that there is an " + field_list[0] + " " + field_list [1]
    line += " for this student.\n\n" + field_list[6].get().strip()
    line += "\nSEIS ID: " + field_list[4].get().strip()
    line += "\n" + field_list[1] + " Date: " + field_list[3].get().strip()
    line += "\n\n" + action + "\n"

    textbox.insert("end", line)
# END OF FN write_message

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
# END OF FN make_follow_write_button

"""
Follow up on:
- unaffirmed IEP
- unaffirmed amendment
- unsigned IEP
- unsigned amendment 
"""
def follow_up(follow_type, follow_item, bg_color):
    # SET BACKGROUND
    w.f_follow_up["bg"] = bg_color

    # CREATE THE FRAMES
    page_frame = w.f_follow_up # !! FRAME
    close_frame = w.Frame(page_frame)
    input_frame = w.Frame(page_frame)
    note_frame = w.Frame(page_frame)

    frame_list = []
    frame_list.append(close_frame)
    frame_list.append(input_frame)
    frame_list.append(note_frame)
    w.configure_frames(frame_list, bg_color)

    # CREATE THE REQUEST DETAILS
    cm_FN = w.Entry(input_frame)
    date = w.Entry(input_frame)
    seis_id = w.Entry(input_frame)
    ssid = w.Entry(input_frame)
    stu_name = w.Entry(input_frame)

    # CREATE THE LIST OF FIELDS
    field_list = []
    field_list.append(follow_type) # 0
    field_list.append(follow_item) # 1
    field_list.append(cm_FN) # 2
    field_list.append(date) # 3
    field_list.append(seis_id) # 4
    field_list.append(ssid) # 5
    field_list.append(stu_name) # 6

    entry_list = []
    for i in range(2,7):
        entry_list.append(field_list[i])

    w.configure_entries(entry_list, w.entry_width_size)

    # USER INPUT FOR REQUEST DETAILS
    input_follow_details(field_list, input_frame, bg_color)

    # BUTTON TO TAKE TEXT ENTRIES AND POPULATE THE TEXTBOX
    write_button = w.Button(input_frame)
    make_follow_write_button(write_button, field_list, frame_list, bg_color)

    # BUTTON TO CLEAR WIDGETS FOR THIS TYPE OF REQUEST
    go_home_button = w.Button(close_frame)
    w.make_go_home_button(go_home_button, frame_list, bg_color)
# END OF FN follow_up

"""
FN PURPOSE: Get user input about a follow up on E-Signature package
"""
def input_signature_details(fields_list, input_frame, bg_color):
    # FRAME FOR USER INPUT
    input_frame.pack()
    r = 0 # Row placement

    # TITLE
    title_text = "Signature: " + fields_list[0]
    l = w.Label(input_frame, text=title_text, bg=bg_color, font=("Courier New", 12))
    l.grid(row=r, column=0, columnspan=2)

    # USER INPUT
    text = "E-Signature Creator"
    l = w.Label(input_frame, text=text, bg=bg_color)
    l.grid(row=r+1, column=0)
    fields_list[1].grid(row=r+2,column=0)

    text = "Student Info (SEIS_ID Expire_Date Last_Name, First_Name)"
    l = w.Label(input_frame, text=text, bg=bg_color)
    l.grid(row=r+3, column=0, columnspan=2)
    fields_list[2].grid(row=r+4, column=0, columnspan=2)

    """
    text = "If there is no SSID, put an 'x' between\nthe SEIS ID and the Student Name."
    l = w.Label(input_frame, text=text, bg=bg_color)
    l.grid(row=r+5, column = 0, columnspan=2)
    """
# END OF FN input_signature_details

"""
FN PURPOSE: Write a note that describes the E-Signature package
"""
def write_signature_message(field_list, note_frame, bg_color):
    note_frame.pack()

    header = ""
    l = w.Label(note_frame, text=header, bg=bg_color, font=("Courier New", 12))
    l.grid(row=0, column=0, columnspan=2)

    # BUTTON TO CLEAR FIELDS
    def clear_sig_fields(field_list):
        for i in range(1, len(field_list)):
            field_list[i].delete(0,"end")
            field_list[i].insert(0, "")

    clearFields_button = w.Button(note_frame, text="Clear Fields")
    clearFields_button["command"] = lambda: clear_sig_fields(field_list)
    clearFields_button.grid(row=1, column=0, columnspan=2)

    # TEXTBOX
    textbox = w.Text(note_frame)
    textbox.config(width=w.textbox_width, height=w.textbox_height)
    textbox.grid(row=2, column=0, columnspan=2)
        
    line = "Hello, " + field_list[1].get().strip() + ".\n\n"
    textbox.insert("end", line)

    line = "Your E-Signature package for the following student is " + field_list[0] + ".\n\n"

    student_info = field_list[2].get().split() # Strip whitespaces and separate the parts of the string into a list
    student_name = ""
    for i in range(2, len(student_info)):
        student_name += student_info[i]
        if i < len(student_info):
            student_name += " "

    line += student_name
    line += "\nSEIS ID: " + student_info[0]
    line += "\nE-Signature expired on: " + student_info[1]
    line += "\n"

    if field_list[0] == "Expired":
        line += "\nFor the signatures that were already collected, you can download the PDF of those signatures and attach it."
        line += "\n\nFor any signatures that still haven't been obtained, you can generate a new E-signature package for the missing signatures. However, if you have already sent out two e-signature packages and parents are struggling to sign, please send a paper copy home to the parent for signature."

    textbox.insert("end", line)
# END OF FN write_signature_message

"""
FN PURPOSE: Make a button for E-Sig message
"""
def make_signature_write_button(write_button, field_list,
    frame_list, bg_color):
    write_button["text"] = "Write Note"
    write_button["command"] = lambda: write_signature_message(field_list,
    frame_list[2], bg_color)
    write_button.grid(row=2, column=1)
# END OF FN make_signature_write_button

"""
Follow up on:
- ready signature
- expired signature
"""
def signature(status, bg_color):
    # SET BACKGROUND
    w.f_signature["bg"] = bg_color

    # CREATE THE FRAMES
    page_frame = w.f_signature # !! FRAME
    close_frame = w.Frame(page_frame)
    input_frame = w.Frame(page_frame)
    note_frame = w.Frame(page_frame)

    frame_list = []
    frame_list.append(close_frame)
    frame_list.append(input_frame)
    frame_list.append(note_frame)
    w.configure_frames(frame_list, bg_color)

    # CREATE THE REQUEST DETAILS
    cm_FN = w.Entry(input_frame)
    stu_info = w.Entry(input_frame)

    # CREATE THE LIST OF FIELDS
    field_list = []
    entry_list = []
    field_list.append(status) # 0
    field_list.append(cm_FN) # 1
    field_list.append(stu_info) # 2

    for i in range(1,3):
        entry_list.append(field_list[i])

    stu_info.insert(0, "SEIS_ID Expire_Date Last_Name, First_Name")
    w.configure_entries(entry_list, w.entry_width_size)

    # USER INPUT FOR REQUEST DETAILS
    input_signature_details(field_list, input_frame, bg_color)

    # BUTTON TO TAKE TEXT ENTRIES AND POPULATE THE TEXTBOX
    write_button = w.Button(input_frame)
    make_signature_write_button(write_button, field_list, frame_list, bg_color)

    # BUTTON TO CLEAR WIDGETS FOR THIS TYPE OF REQUEST
    go_home_button = w.Button(close_frame)
    w.make_go_home_button(go_home_button, frame_list, bg_color)
# END OF FN signature

"""
FN PURPOSE: Get user input about sped type
"""
def input_sped_type_details(fields_list, input_frame, bg_color):
    # FRAME FOR USER INPUT
    input_frame.pack()
    r = 0 # Row placement

    # TITLE
    title_text = "SpEd Type update note"
    l = w.Label(input_frame, text=title_text, bg=bg_color, font=("Courier New", 12))
    l.grid(row=r, column=0, columnspan=2)

    # USER INPUT
    text = "SpEd Type & Start Date"
    l = w.Label(input_frame, text=text, bg=bg_color)
    l.grid(row=r+1, column=0)
    fields_list[0].grid(row=r+2,column=0)
# END OF FN input_sped_type_details

"""
FN PURPOSE: Write a note about updating the sped type
"""
def write_sped_type_note(field_list, note_frame, bg_color):
    note_frame.pack()

    header = ""
    l = w.Label(note_frame, text=header, bg=bg_color, font=("Courier New", 12))
    l.grid(row=0, column=0, columnspan=2)

    # BUTTON TO CLEAR FIELDS
    def clear_sped_type_fields(field_list):
        for i in range(len(field_list)):
            field_list[i].delete(0,"end")
            field_list[i].insert(0, "")

    clearFields_button = w.Button(note_frame, text="Clear Fields")
    clearFields_button["command"] = lambda: clear_sped_type_fields(field_list)
    clearFields_button.grid(row=1, column=0, columnspan=2)

    # TEXTBOX
    textbox = w.Text(note_frame)
    textbox.config(width=w.textbox_width, height=w.textbox_height)
    textbox.grid(row=2, column=0, columnspan=2)

    sped_type_data = field_list[0].get().split() # Strip whitespaces and separate the parts of the string into a list
        
    line = "Updated SpEd Type to " + (sped_type_data[0]).upper() + " as of " + sped_type_data[1]
    textbox.insert("end", line)
# END OF FN write_sped_type_note

"""
FN PURPOSE: Make a button for SpEd Type update note
"""
def make_sped_type_write_button(write_button, field_list,
    frame_list, bg_color):
    write_button["text"] = "Write Note"
    write_button["command"] = lambda: write_sped_type_note(field_list,
    frame_list[2], bg_color)
    write_button.grid(row=2, column=1)
# END OF FN make_signature_write_button

"""
note for updating sped type
"""
def sped_type(bg_color):
    # SET BACKGROUND
    w.f_sped_type["bg"] = bg_color

    # CREATE THE FRAMES
    page_frame = w.f_sped_type # !! FRAME
    close_frame = w.Frame(page_frame)
    input_frame = w.Frame(page_frame)
    note_frame = w.Frame(page_frame)

    frame_list = []
    frame_list.append(close_frame)
    frame_list.append(input_frame)
    frame_list.append(note_frame)
    w.configure_frames(frame_list, bg_color)

    # CREATE THE REQUEST DETAILS
    raw_data = w.Entry(input_frame)

    # CREATE THE LIST OF FIELDS
    field_list = []
    entry_list = []
    field_list.append(raw_data) # 0

    raw_data.insert(0, "sped_type date")
    w.configure_entries(field_list, w.entry_width_size)

    # USER INPUT FOR REQUEST DETAILS
    input_sped_type_details(field_list, input_frame, bg_color)

    # BUTTON TO TAKE TEXT ENTRIES AND POPULATE THE TEXTBOX
    write_button = w.Button(input_frame)
    make_sped_type_write_button(write_button, field_list, frame_list, bg_color)

    # BUTTON TO CLEAR WIDGETS FOR THIS TYPE OF REQUEST
    go_home_button = w.Button(close_frame)
    w.make_go_home_button(go_home_button, frame_list, bg_color)
# END OF FN sped_type

# EOF follow_up.py