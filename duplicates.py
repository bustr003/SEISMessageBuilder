# FILE duplicates.py
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
    text = "Outdated SEIS ID"
    l = w.Label(input_frame, text=text, bg=bg_color)
    l.grid(row=r+1, column=0)
    fields_list[1].grid(row=r+2,column=0)

    text = "Date created (outdated)"
    l = w.Label(input_frame, text=text, bg=bg_color)
    l.grid(row=r+1, column=1)
    fields_list[2].grid(row=r+2, column=1)

    text = "Current SEIS ID"
    l = w.Label(input_frame, text=text, bg=bg_color)
    l.grid(row=r+3, column=0)
    fields_list[3].grid(row=r+4, column=0)

    text = "Date created (current)"
    l = w.Label(input_frame, text=text, bg=bg_color)
    l.grid(row=r+3, column=1)
    fields_list[5].grid(row=r+4, column=1)

    text = "Student Name (current)"
    l = w.Label(input_frame, text=text, bg=bg_color)
    l.grid(row=r+5, column=0)
    fields_list[4].grid(row=r+6, column=0)

    text = "Providers"
    l = w.Label(input_frame, text=text, bg=bg_color)
    l.grid(row=r+7, column=0, columnspan=2)
    fields_list[6].grid(row=r+8, column=0, columnspan=2)

# END OF FN input_reqest_details

"""
FN PURPOSE: Write a note that describes the request,
the actions taken to complete the request,
and any other comments or concerns.
- For record changes
"""
def write_note(field_list, note_frame, bg_color):
    note_frame.pack()

    header = "Note for " + field_list[4].get().strip()
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
    
    line = "SEIS ID " + field_list[1].get().strip() + " is an outdated record, created on " + field_list[2].get().strip() + ".\n"
    line += "This SEIS record must be deactivated.\n\n"
    lines.append(line)

    line = "The correct record for this student is " + field_list[3].get().strip() + ".\n"
    line += "Name: " + field_list[4].get().strip() + "\n"
    line += "Record added on: " + field_list[5].get().strip() + "\n\n"
    lines.append(line)

    line = "Downloaded the Future IEP forms and attachments. -\n"
    line += "Sent the documents to providers and advised them to work on the correct record (not this one). -\n"
    line += field_list[6].get().strip() + "\n\n"
    lines.append(line)

    line = "PROCESS FOR DE-ACTIVATING A DUPLICATE RECORD\n"
    line += "Do not report: DNR, Current record is " + field_list[3].get().strip() + " -\n"
    line += "Duplicate record: Current record is " + field_list[3].get().strip() + " -\n"
    line += "Changed status to DNQ/Not Providing Services. -\n\n"
    line += "This record will not be pulled into search results.\n"
    line += "This record will not be pulled into the Add Student search.\n"
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
def merge_duplicates(bg_color):
    w.f_duplicate["bg"] = bg_color

    # CREATE THE FRAMES
    page_frame = w.f_duplicate # !! FRAME
    close_frame = w.Frame(page_frame)
    input_frame = w.Frame(page_frame)
    note_frame = w.Frame(page_frame)

    frame_list = []
    frame_list.append(close_frame)
    frame_list.append(input_frame)
    frame_list.append(note_frame)
    w.configure_frames(frame_list, bg_color)

    # CREATE THE REQUEST DETAILS
    invalid_seis_id = w.Entry(input_frame)
    invalid_date = w.Entry(input_frame)
    current_seis_id = w.Entry(input_frame)
    current_name = w.Entry(input_frame)
    current_date = w.Entry(input_frame)
    providers = w.Entry(input_frame)
 
    # CREATE THE LIST OF FIELDS
    field_list = []
    field_list.append("Merge Duplicate Records") # 0
    field_list.append(invalid_seis_id) # 1
    field_list.append(invalid_date) # 2
    field_list.append(current_seis_id) # 3
    field_list.append(current_name) # 4
    field_list.append(current_date) # 5
    field_list.append(providers) # 6

    entry_list = []
    for i in range(1,7):
        entry_list.append(field_list[i])

    current_name.insert(0, "<Name in current SEIS ID>")
    providers.insert(0, "<Names of providers>")
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
# END OF FN merge_duplicates

# EOF duplicates.py