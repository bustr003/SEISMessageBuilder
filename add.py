import window as w

"""
Add a student to SEIS 
"""
def add():
    bg_color = w.orange # !! BG COLOR

    # CREATE THE TITLE
    reqType = "Add Student" # !! REQUEST CHANGE

    # CREATE THE FRAMES
    request_frame = w.f_add # !! FRAME
    close_frame = w.Frame(request_frame)
    input_frame = w.Frame(request_frame)
    note_frame = w.Frame(request_frame)

    frame_list = []
    frame_list.append(close_frame)
    frame_list.append(input_frame)
    frame_list.append(note_frame)
    w.configure_frames(frame_list, bg_color)

    # CREATE THE REQUEST DETAILS
    stuLN = w.Entry(input_frame)
    stuFN = w.Entry(input_frame)
    reqName = w.Entry(input_frame)
    reqComment = w.Entry(input_frame)

    reqRole = w.StringVar()
    role_options = w.OptionMenu(input_frame, reqRole, *w.staff_roles)

    # CREATE THE LIST OF FIELDS
    field_list = []
    field_list.append(reqType) # 0
    field_list.append(stuLN) # 1
    field_list.append(stuFN) # 2
    field_list.append(reqName) # 3
    field_list.append(reqComment) # 4
    field_list.append(reqRole) # 5

    entry_list = []
    for i in range(1,5):
        entry_list.append(field_list[i])

    w.configure_entries(entry_list, w.entry_width_size)

    # USER INPUT FOR REQUEST DETAILS
    w.input_request_details(field_list, role_options, input_frame, bg_color)

    # LIST OF COMMON ACTIONS FOR THIS REQUEST TYPE
    actions = [
        "Request completed.",
        "\nPowerSchool Record: ",
        "SEIS record: ",
        "SSID: ",
        "EUSD Start Date: ",
        "Grade: ",
        "Middle Name: ",
        "School of Residence: ",
        "School of Attendance: ",

        # For students who were previously Exited (Inactive)
        "\nChanged Plan Type to 300 - Pending Initial Evaluation",
        "Re-activated the SEIS record.",
        "Directed the requester to update fields 26, 27, 28, 29, 14.20, 14.27.",
        "Directed the requester to NOT change Field 14.27 if it is already Populated."
    ]

    # BUTTON TO TAKE TEXT ENTRIES AND POPULATE THE TEXTBOX
    write_button = w.Button(input_frame)
    w.make_write_button(write_button, field_list, actions,
    frame_list, bg_color)

    # BUTTON TO CLEAR WIDGETS FOR THIS TYPE OF REQUEST
    clearFrames_button = w.Button(close_frame)
    w.make_clearFrames_button(clearFrames_button, frame_list, bg_color)
# END OF FN: add