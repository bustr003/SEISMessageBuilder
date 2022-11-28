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
def write_note(field_list, combobox, role_label, actions, note_frame, bg_color):
    note_frame.pack()

    header = "Note for " + field_list[1].get().strip() + ", " + field_list[2].get().strip()
    l = w.Label(note_frame, text=header, bg=bg_color, font=("Courier New", 12))
    l.grid(row=0, column=0, columnspan=2)

    # BUTTON TO CLEAR THE FIELDS
    def clear_fields(field_list, combobox, role_label):
        w.clear_fields(field_list, combobox, role_label)
        field_list[6].set("Record Change")

    clearFields_button = w.Button(note_frame, text="Clear Fields")
    clearFields_button["command"] = lambda: clear_fields(field_list, combobox, role_label)
    clearFields_button.grid(row=1, column=0, columnspan=2)

    # TEXTBOX
    textbox = w.Text(note_frame, wrap="word")
    textbox.config(width=w.textbox_width, height=w.textbox_height)
    textbox.grid(row=2, column=0, columnspan=2)

    line = field_list[3].get().strip() + ", " + field_list[5].get().strip() + " requested: " + field_list[6].get() + "\n"
    textbox.insert("end", line)

    if field_list[4].get().strip() != "":
        line = "\"" + field_list[4].get().strip() + "\"\n\n"
    else:
        line = "\n"
    textbox.insert("end", line)

    for i in range(0, len(actions)):
        textbox.insert("end", actions[i])
        if (i < len(actions)):
            textbox.insert("end", "\n")
# END OF FN write_note

"""
FN PURPOSE: Make a button.
When pressed, put a Note template in an editable textbox.
- For record changes
"""
def make_write_button(write_button, field_list, combobox, role_label, actions,
    frame_list, bg_color):
    write_button["text"] = "Write Note"
    write_button["command"] = lambda: write_note(field_list, combobox, role_label, actions,
    frame_list[2], bg_color)
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
 
    # CREATE THE LIST OF FIELDS
    field_list = []
    field_list.append(req_type) # 0
    field_list.append(stu_LN) # 1
    field_list.append(stu_FN) # 2
    field_list.append(requester_name) # 3
    field_list.append(requester_comment) # 4

    selected_role = w.StringVar()
    selected_role.set("Select Role")
    field_list.append(selected_role) # 5

    entry_list = []
    for i in range(1,4):
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
    record_change_dropdown.config(width=w.dropdown_width, wrap=w.wrap_units)
    w.input_dropdown(record_change_type, record_change_types, record_change_dropdown, 8, 0)
    field_list.append(record_change_type) # 6
    
    # USER INPUT FOR REQUEST DETAILS
    # A label that is initialized and then changes each time a new role is selected
    text = "Requester Role:\n..."
    role_label = w.Label(input_frame, text=text, wraplength=w.wrap_units, bg=bg_color)
    role_label.grid(row=3, column=1)

    # When a combo box option is selected or entered, update the field value.
    def set_result(event, role_label):
        selected_role = role_options.get().strip()
        field_list[5].set(selected_role)

        # Update the label to display the current role
        text = "Requester Role:\n" + selected_role
        role_label.config(text=text)
        role_label.grid(row=3, column=1)
    
    # COMBOBOX TO SELECT A TERM
    role_options = w.ttk.Combobox(input_frame, value=w.staff_roles, width=w.combobox_width)
    role_options.current(0)
    
    event_bind = "<<ComboboxSelected>>"
    role_options.bind(event_bind, lambda _ :set_result(event_bind, role_label))
    
    event_bind = "<KeyRelease>"
    role_options.bind(event_bind, lambda _ :set_result(event_bind, role_label))
    
    role_options.grid(row=8, column=0)

    w.input_request_details(field_list, role_label, role_options, input_frame, bg_color)

    # LIST OF COMMON ACTIONS FOR THIS REQUEST TYPE
    actions = [
        "Request completed."
    ]

    # BUTTON TO TAKE TEXT ENTRIES AND POPULATE THE TEXTBOX
    write_button = w.Button(input_frame)
    make_write_button(write_button, field_list, role_options, role_label, actions,
    frame_list, bg_color)

    # BUTTON TO CLEAR WIDGETS FOR THIS TYPE OF REQUEST
    go_home_button = w.Button(close_frame)
    w.make_go_home_button(go_home_button, frame_list, bg_color)
# END OF FN record_change

# EOF record_change.py