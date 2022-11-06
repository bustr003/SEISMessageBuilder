# FILE record_change.py
"""
Primary function for making a change to a student's record.
"""

import window as w

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
    request_frame = w.f_record_change # !! FRAME
    close_frame = w.Frame(request_frame)
    input_frame = w.Frame(request_frame)
    note_frame = w.Frame(request_frame)

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
    field_list[0] = record_change_type.get() # !! FIX THIS !!
    
    # USER INPUT FOR REQUEST DETAILS
    w.input_request_details(field_list, role_options, input_frame, bg_color)

    # LIST OF COMMON ACTIONS FOR THIS REQUEST TYPE
    actions = [
        "Request completed.",
        ""
    ]

    # BUTTON TO TAKE TEXT ENTRIES AND POPULATE THE TEXTBOX
    write_button = w.Button(input_frame)
    w.make_write_button_record_change(write_button, field_list, actions,
    frame_list, bg_color, record_change_type)

    # BUTTON TO CLEAR WIDGETS FOR THIS TYPE OF REQUEST
    clearFrames_button = w.Button(close_frame)
    w.make_clearFrames_button(clearFrames_button, frame_list, bg_color)
# END OF FN record_change

# EOF record_change.py