# FILE exit_student.py
"""
Primary function for exiting a student.
"""

import window as w

"""
Exit a student
"""
def exit_student(req_type, bg_color):
    # SET BACKGROUND
    w.f_exit_student["bg"] = bg_color

    # CREATE THE FRAMES
    page_frame = w.f_exit_student # !! FRAME
    close_frame = w.Frame(page_frame)
    input_frame = w.Frame(page_frame)
    note_frame = w.Frame(page_frame)

    # CONFIGURE THE FRAMES
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
 
    # CREATE THE LIST OF FIELDS
    field_list = []
    field_list.append(req_type) # 0
    field_list.append(stu_LN) # 1
    field_list.append(stu_FN) # 2
    field_list.append(requester_name) # 3
    field_list.append(requester_comment) # 4
    
    selected_role = w.StringVar()
    selected_role.set("Select Role")
    field_list.append(requester_role) # 5

    entry_list = []
    for i in range(1,4):
        entry_list.append(field_list[i])

    w.configure_entries(entry_list, w.entry_width_size)

    # USER INPUT FOR REQUEST DETAILS
    # When a combo box option is selected or entered, update the field value.
    def set_result(event):
        selected_role = role_options.get().strip()
        field_list[5].set(selected_role)

        text = "Requester Role:\n" + selected_role + "\n(for custom, press Enter)"
        l = w.Label(input_frame, text=text, bg=bg_color)
        l.grid(row=3, column=1)
    
    # COMBOBOX TO SELECT A TERM
    role_options = w.ttk.Combobox(input_frame, value=w.staff_roles, width=15)
    role_options.bind("<<ComboboxSelected>>", set_result)
    role_options.bind("<Return>", set_result)
    role_options.grid(row=8, column=0)
    
    w.input_request_details(field_list, role_options, input_frame, bg_color)

    # LIST OF COMMON ACTIONS FOR THIS REQUEST TYPE
    if req_type == "Exit 70\nNo longer eligible":
        actions = [
            "Request completed.",
            "Parent signed \"no longer eligible\" on "
        ]
    
    elif req_type == "Exit 74\nDrop Out/Not known to be continuing":
        actions = [
            "Request completed.",
            ""
        ]

    elif req_type == "Exit 76\nTransfer, known to be continuing":
        actions = [
            "Request completed.",
            "EUSD Exit Date "
        ]

    elif req_type == "Exit 77\nDeceased":
        actions = [
            "Request completed.",
            ""
        ]

    elif req_type == "Exit 78\nParent Withdrawal":
        actions = [
            "Request completed.",

            "\nCURRENT IEP ATTACHMENT",
            "Revocation Letter: ",

            "\nCURRENT IEP COMMENT",
            "Parent would like to withdraw the student from services.",
            "Parent revoked consent on <date>.",
            "The Revocation Letter was sent by <name>, <role>, on <date>.",
            
            "\nSCHOOL AGE",
            "Do Not Report: -"
        ]

    elif req_type == "Exit 84\nPart C to B No parental consent":
        actions = [
            "Request completed.",
            ""
        ]

    elif req_type == "Exit 85\nExited SPED Out-of-State":
        actions = [
            "Request completed.",
            ""
        ]
    
    # BUTTON TO TAKE TEXT ENTRIES AND POPULATE THE TEXTBOX
    write_button = w.Button(input_frame)
    w.make_write_button(write_button, field_list, actions,
    frame_list, bg_color)

    # BUTTON TO CLEAR WIDGETS FOR THIS TYPE OF REQUEST
    clearFrames_button = w.Button(close_frame)
    w.make_clear_frames_button(clearFrames_button, frame_list, bg_color)
# END OF FN exit_student

# EOF exit_student.py