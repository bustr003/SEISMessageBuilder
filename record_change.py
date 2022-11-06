# FILE record_change.py
"""
- Functions used only for record change requests.
- Primary function for making a change to a student's record.
"""

import window as w

"""
FN PURPOSE: Write a note that describes the request,
the actions taken to complete the request,
and any other comments or concerns.
- For record changes
"""
def write_note_record_change(field_list, actions, note_frame, bg_color, change_requested):
    note_frame.pack()

    header = "Note for " + field_list[1].get().strip() + ", " + field_list[2].get().strip()
    l = w.Label(note_frame, text=header, bg=bg_color, font=("Courier New", 12))
    l.grid(row=0, column=0, columnspan=2)

    clearFields_button = w.Button(note_frame, text="Clear Fields")
    clearFields_button["command"] = lambda: w.clear_fields(field_list)
    clearFields_button.grid(row=1, column=0, columnspan=2)

    textbox = w.Text(note_frame, wrap="word")
    textbox.config(width=w.textbox_width, height=w.textbox_height)
    textbox.grid(row=2, column=0, columnspan=2)

    line = field_list[3].get().strip() + ", " + field_list[5].get().strip() + " requested: " + change_requested.get() + "\n"
    textbox.insert("end", line)

    line = "\"" + field_list[4].get().strip() + "\"\n\n"
    textbox.insert("end", line)

    for i in range(0, len(actions)):
        textbox.insert("end", actions[i])
        if (i < len(actions)-1):
            textbox.insert("end", "\n")
# END OF FN write_note_record_change

"""
FN PURPOSE: Make a button.
When pressed, put a Note template in an editable textbox.
- For record changes
"""
def make_write_button_record_change(write_button, field_list, actions,
    frame_list, bg_color, change_requested):
    write_button["text"] = "Write Note"
    write_button["command"] = lambda: write_note_record_change(field_list, actions,
    frame_list[2], bg_color, change_requested)
    write_button.grid(row=6, column=1)
# END OF FN make_write_button_record_change

"""
Change a student's IEP Team
Types of changes requested
- add provider
- change case manager
- remove provider/cm
- other
"""
def record_change(req_type, bg_color):
    w.f_record_change["bg"] = bg_color

    # CREATE THE FRAMES
    page_frame = w.f_record_change # !! FRAME
    close_frame = w.Frame(page_frame)
    input_frame = w.Frame(page_frame)
    note_frame = w.Frame(page_frame)

    frame_list = []
    frame_list.append(close_frame)
    frame_list.append(input_frame)
    frame_list.append(note_frame)
    w.configure_frames(frame_list, bg_color)

    # CREATE THE REQUEST DETAILS
    stu_LN = w.Entry(input_frame)
    stu_FN = w.Entry(input_frame)
    requester_name = w.Entry(input_frame)
    requester_comment = w.Entry(input_frame)

    requester_role = w.StringVar()
    role_options = w.OptionMenu(input_frame, requester_role, *w.staff_roles)

    # CREATE THE LIST OF FIELDS
    field_list = []
    field_list.append(req_type) # 0
    field_list.append(stu_LN) # 1
    field_list.append(stu_FN) # 2
    field_list.append(requester_name) # 3
    field_list.append(requester_comment) # 4
    field_list.append(requester_role) # 5

    entry_list = []
    for i in range(1,5):
        entry_list.append(field_list[i])

    w.configure_entries(entry_list, w.entry_width_size)

    text = "Change Requested"
    l = w.Label(input_frame, text=text, bg=bg_color)
    l.grid(row=7, column=0)

    record_change_types = [
        "Record Change",
        "Student should not be on my caseload",
        "Add provider",
        "Change Case Manager"
    ]

    record_change_type = w.StringVar()
    record_change_dropdown = w.OptionMenu(input_frame, record_change_type, *record_change_types)
    w.input_dropdown(record_change_type, record_change_types, record_change_dropdown, 8, 0)
    field_list[0] = record_change_type.get()
    
    # USER INPUT FOR REQUEST DETAILS
    w.input_request_details(field_list, role_options, input_frame, bg_color)

    # LIST OF COMMON ACTIONS FOR THIS REQUEST TYPE
    actions = [
        "Request completed.",
        ""
    ]

    # BUTTON TO TAKE TEXT ENTRIES AND POPULATE THE TEXTBOX
    write_button = w.Button(input_frame)
    make_write_button_record_change(write_button, field_list, actions,
    frame_list, bg_color, record_change_type)

    # BUTTON TO CLEAR WIDGETS FOR THIS TYPE OF REQUEST
    clearFrames_button = w.Button(close_frame)
    w.make_clearFrames_button(clearFrames_button, frame_list, bg_color)
# END OF FN record_change

# EOF record_change.py