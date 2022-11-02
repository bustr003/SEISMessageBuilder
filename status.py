import window as w

"""
Change a student's status from Pending to Eligible
"""
def status_change(reqType, bg_color):
    #bg_color = w.blue # !! BG COLOR

    # CREATE THE TITLE
    #reqType = "Status: Make Eligible" # !! REQUEST CHANGE
    w.f_status_change["bg"] = bg_color

    # CREATE THE FRAMES
    request_frame = w.f_status_change # !! FRAME
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
    if reqType == "Status: Make Eligible":
        actions = [
            "Request completed.",
            "\nSpEd Type: - to be added",
            "Parent Consent Date: ",
            "Meeting Type: ",
            "Plan Type: ",
            "Date parent signed \"I agree\": ",
            "Status changed from Pending to Eligible."
        ]
    elif reqType == "Status: Make DNQ":
        actions = [
        "Request completed.\n",
        "Parent Consent Date: ",
        "Plan Type: ",
        "Date parent signed \"not eligible\": ",
        "Status changed from Pending to Ineligible."
        ]
    elif reqType == "Status: Assessment Plan Declined":
        actions = [
        "Request completed.\n",
        "CALPADS \"Pending\" Transaction: ",
        "Parent Consent Date: (removed)",
        "Removed Date District Received Parent Consent.",
        "Parent signed \"I do not agree with the proposed assessment\" on ",
        "Do Not Report: ",
        "Status changed from Pending to Not Providing Services."
        ]
    

    # BUTTON TO TAKE TEXT ENTRIES AND POPULATE THE TEXTBOX
    write_button = w.Button(input_frame)
    w.make_write_button(write_button, field_list, actions,
    frame_list, bg_color)

    # BUTTON TO CLEAR WIDGETS FOR THIS TYPE OF REQUEST
    clearFrames_button = w.Button(close_frame)
    w.make_clearFrames_button(clearFrames_button, frame_list, bg_color)
# END OF FN: make_elig
