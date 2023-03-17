# FILE add_student.py
"""
Primary function for adding a student.
"""

import window as w

"""
Add a student to SEIS 
"""
def add_student(req_type, bg_color):
    # SET BACKGROUND
    w.f_add_student["bg"] = bg_color

    # CREATE THE FRAMES
    page_frame = w.f_add_student # !! FRAME
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

    # USER INPUT FOR REQUEST DETAILS
    # A label that is initialized and then changes each time a new role is selected
    text = "Requester Role\n" + w.staff_roles[0]
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
        "Request completed.",
        "SIS record: ",
        "SEIS record: ",
        "SSID: ",

        "\nPsych access granted -",
        "IEP Team added -",

        "\nLEA Start Date: ",
        "Grade: ",
        "Middle Name: ",
        "School of Residence: ",
        "School of Attendance: ",

        "\nRE-ACTIVATED SEIS RECORD",
        "Changed Plan Type to 300 - Pending Initial Evaluation. -",
        "Re-activated the SEIS record.",
        "Status changed to Pending.",
        "Informed the requester of fields to update and how to view student history."
    ]

    # BUTTON TO TAKE TEXT ENTRIES AND POPULATE THE TEXTBOX
    write_button = w.Button(input_frame)
    w.make_write_button(write_button, field_list, role_options, role_label, actions,
    frame_list, bg_color)

    # BUTTON TO CLEAR WIDGETS FOR THIS TYPE OF REQUEST
    go_home_button = w.Button(close_frame)
    w.make_go_home_button(go_home_button, frame_list, bg_color)
# END OF FN add_student

# EOF add_student.py