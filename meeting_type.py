# FILE meeting_type.py
"""
- Functions used only for handling a duplicate record.
"""

import window as w

"""
FN PURPOSE: Get user input about the request.
"""
def input_request_details(fields_list, input_frame, bg_color):
    # FRAME FOR USER INPUT
    input_frame.pack()
    r = 0 # Row placement

    # TITLE
    l = w.Label(input_frame, text=fields_list[0], bg=bg_color, font=("Courier New", 12), wraplength=250)
    l.grid(row=r, column=0, columnspan=2)

    # USER INPUT
    text = "Student Last Name"
    l = w.Label(input_frame, text=text, bg=bg_color)
    l.grid(row=r+1, column=0)
    fields_list[1].grid(row=r+2,column=0)

    text = "Student First Name"
    l = w.Label(input_frame, text=text, bg=bg_color)
    l.grid(row=r+1, column=1)
    fields_list[2].grid(row=r+2, column=1)

    text = "SSID"
    l = w.Label(input_frame, text=text, bg=bg_color)
    l.grid(row=r+3, column=0)
    fields_list[3].grid(row=r+4, column=0)

    text = "Case Manager"
    l = w.Label(input_frame, text=text, bg=bg_color)
    l.grid(row=r+3, column=1)
    fields_list[5].grid(row=r+4, column=1)

    text = "Meeting Date"
    l = w.Label(input_frame, text=text, bg=bg_color)
    l.grid(row=r+5, column=0)
    fields_list[4].grid(row=r+6, column=0)

    text = "Old Type"
    l = w.Label(input_frame, text=text, bg=bg_color)
    l.grid(row=r+7, column=0)
    fields_list[6].grid(row=r+8, column=0)

    text = "New Type"
    l = w.Label(input_frame, text=text, bg=bg_color)
    l.grid(row=r+7, column=1)
    fields_list[7].grid(row=r+8, column=1)
# END OF FN input_reqest_details

"""
FN PURPOSE: Write a note that describes the request,
the actions taken to complete the request,
and any other comments or concerns.
- For record changes
"""
def write_note(field_list, note_frame, bg_color):
    note_frame.pack()

    header = "Note for " + field_list[1].get().strip() + ", " + field_list[2].get().strip()
    l = w.Label(note_frame, text=header, bg=bg_color, font=("Courier New", 12))
    l.grid(row=0, column=0, columnspan=2)

    # BUTTON TO CLEAR THE FIELDS
    def clear_fields(field_list):
        w.clear_fields(field_list)

    clearFields_button = w.Button(note_frame, text="Clear Fields")
    clearFields_button["command"] = lambda: clear_fields(field_list)
    clearFields_button.grid(row=1, column=0, columnspan=2)

    # TEXTBOX
    textbox = w.Text(note_frame, wrap="word")
    textbox.config(width=w.textbox_width, height=w.textbox_height)
    textbox.grid(row=2, column=0, columnspan=2)

    lines = [] # The lines of text
    
    line = "Incorrect Meting Type was selected on the " + field_list[4].get().strip() + " IEP.\n\n"
    lines.append(line)

    line = "- Downloaded attachments and Team Meeting Notes from the Current IEP.\n"
    line += "- Added the attachments and Team Meeting Notes to the Future IEP.\n"
    line += "- Changed the Future IEP Meeting Type from " + field_list[6].get().strip()
    line += " to " + field_list[7].get().strip() + ".\n"
    line += "- In the Future IEP, selected all forms that were used during the " + field_list[4].get().strip() + " meeting.\n\n"
    lines.append(line)

    line = "- Affirm Notes:\n"
    line += "Correction: Meeting should have been " + field_list[7].get().strip()
    line += ", not " + field_list[6].get().strip() + ".\n"
    line += "No other changes were made."
    line += " No meeting held."
    line += " Parent signature for the " + field_list[4].get().strip() + " meeting is attached.\n\n"
    lines.append(line)

    line = "- Posted the corrected CALPADS Transaction.\n"
    line += "- Deleted the erroneous CALPADS Transaction.\n\n"
    lines.append(line)

    line = "- Instructed " + field_list[5].get().strip() + "(Case Manager): Please send the parent a new copy of the IEP with a note explaining the clerical error.\n"
    lines.append(line)

    for line in lines:
        textbox.insert("end", line)
# END OF FN write_note

"""
FN PURPOSE: Make a button.
When pressed, put a Note template in an editable textbox.
- For record changes
"""
def make_write_button(write_button, field_list,
    frame_list, bg_color):
    write_button["text"] = "Write Note"
    write_button["command"] = lambda: write_note(field_list,
    frame_list[2], bg_color)
    write_button.grid(row=6, column=1)
# END OF FN make_write_button

"""
Merge two duplicate records.
- Make the invalid record inactive.
- Update and keep the current record.
"""
def meeting_type_correction(bg_color):
    w.f_meeting_type["bg"] = bg_color

    # CREATE THE FRAMES
    page_frame = w.f_meeting_type # !! FRAME
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
    ssid = w.Entry(input_frame)
    meeting_date = w.Entry(input_frame)
    cm = w.Entry(input_frame)
    old_type = w.Entry(input_frame)
    new_type = w.Entry(input_frame)
 
    # CREATE THE LIST OF FIELDS
    field_list = []
    field_list.append("Meeting Type Correction") # 0
    field_list.append(stu_LN) # 1
    field_list.append(stu_FN) # 2
    field_list.append(ssid) # 3
    field_list.append(meeting_date) # 4
    field_list.append(cm) # 5
    field_list.append(old_type) # 6
    field_list.append(new_type) # 7

    entry_list = []
    for i in range(1,8):
        entry_list.append(field_list[i])

    w.configure_entries(entry_list, w.entry_width_size)
    
    # USER INPUT FOR REQUEST DETAILS
    input_request_details(field_list, input_frame, bg_color)

    """
    # LIST OF COMMON ACTIONS FOR THIS REQUEST TYPE
    actions = [
        "Request completed."
    ]
    """

    # BUTTON TO TAKE TEXT ENTRIES AND POPULATE THE TEXTBOX
    write_button = w.Button(input_frame)
    make_write_button(write_button, field_list,
    frame_list, bg_color)

    # BUTTON TO CLEAR WIDGETS FOR THIS TYPE OF REQUEST
    go_home_button = w.Button(close_frame)
    w.make_go_home_button(go_home_button, frame_list, bg_color)
# END OF FN meeting_type_correction

# EOF meeting_type.py