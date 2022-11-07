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

    # USER INPUT FOR REQUEST DETAILS
    w.input_request_details(field_list, role_options, input_frame, bg_color)

    # LIST OF COMMON ACTIONS FOR THIS REQUEST TYPE
    actions = [
        "Request completed.",
        "PowerSchool Record: ",
        "SEIS record: ",
        "SSID: ",
        "EUSD Start Date: ",
        "Grade: ",
        "Middle Name: ",
        "School of Residence: ",
        "School of Attendance: ",

        "\nRe-activated the SEIS record.",
        "Status changed to Pending.",
        "Directed the requester to update fields 26, 27, 28, 29, 14.20, 14.27.",
        "Directed the requester to NOT change Field 14.27 if it is already populated."
    ]

    # BUTTON TO TAKE TEXT ENTRIES AND POPULATE THE TEXTBOX
    write_button = w.Button(input_frame)
    w.make_write_button(write_button, field_list, actions,
    frame_list, bg_color)

    # BUTTON TO CLEAR WIDGETS FOR THIS TYPE OF REQUEST
    clearFrames_button = w.Button(close_frame)
    w.make_clear_frames_button(clearFrames_button, frame_list, bg_color)
# END OF FN add_student

# EOF add_student.py