# FILE follow_up.py
"""
Functions used only for following up on IEPs and Amendments
"""
import window as w

"""
FN PURPOSE: Get user input about a follow up.
- unaffirmed/unsigned IEP/amendment
"""
def input_follow_details(fields_list, input_frame, bg_color):
    # FRAME FOR USER INPUT
    input_frame.pack()
    r = 0 # Row placement

    # TITLE
    title_text = fields_list[0] + " " + fields_list[1]
    l = w.Label(input_frame, text=title_text, bg=bg_color, font=("Courier New", 12))
    l.grid(row=r, column=0, columnspan=2)

    # USER INPUT
    text = "Case Manager"
    l = w.Label(input_frame, text=text, bg=bg_color)
    l.grid(row=r+1, column=0)
    fields_list[2].grid(row=r+2,column=0)

    text = "Date"
    l = w.Label(input_frame, text=text, bg=bg_color)
    l.grid(row=r+1, column=1)
    fields_list[3].grid(row=r+2, column=1)

    text = "Student LN"
    l = w.Label(input_frame, text=text, bg=bg_color)
    l.grid(row=r+3, column=0)
    fields_list[4].grid(row=r+4, column=0)

    text = "Student FN"
    l = w.Label(input_frame, text=text, bg=bg_color)
    l.grid(row=r+3, column=1)
    fields_list[5].grid(row=r+4, column=1)

    text = "SEIS ID"
    l = w.Label(input_frame, text=text, bg=bg_color)
    l.grid(row=r+5, column=0)
    fields_list[6].grid(row=r+6, column=0)
# END OF FN input_follow_details

"""
FN PURPOSE: Write a note that describes the follow up.
"""
def write_message(field_list, note_frame, bg_color):
    note_frame.pack()

    header = field_list[0] + " " + field_list[1]
    l = w.Label(note_frame, text=header, bg=bg_color, font=("Courier New", 12))
    l.grid(row=0, column=0, columnspan=2)

    # BUTTON TO CLEAR FIELDS
    def clear_follow_fields(field_list):
        for i in range(2, len(field_list)):
            field_list[i].delete(0,"end")
            field_list[i].insert(0, "")

    clearFields_button = w.Button(note_frame, text="Clear Fields")
    clearFields_button["command"] = lambda: clear_follow_fields(field_list)
    clearFields_button.grid(row=1, column=0, columnspan=2)

    # TEXTBOX
    textbox = w.Text(note_frame)
    textbox.config(width=w.textbox_width, height=w.textbox_height)
    textbox.grid(row=2, column=0, columnspan=2)

    if field_list[0] == "Unaffirmed":
        action = "Is this " + field_list[1] + " ready to be affirmed?"
    elif field_list[0] == "Unsigned":
        action = "Are you still waiting for a signture for this " + field_list[1] + "?"

    line = "Hello, " + field_list[2].get().strip() + ".\n\n"
    textbox.insert("end", line)

    line = "I noticed that you have an " + field_list[0] + " " + field_list [1]
    line += " for " + field_list[5].get().strip() + " " + field_list[4].get().strip()
    line += ", SEIS ID " + field_list[6].get().strip() + "."
    line += "\n\nThe " + field_list[1] + " Date is " + field_list[3].get().strip() + "."
    line += "\n\n" + action + "\n"

    textbox.insert("end", line)
# END OF FN write_message

"""
FN PURPOSE: Make a button for follow up message.
When pressed, put a message template in an editable textbox.
"""
def make_follow_write_button(write_button, field_list,
    frame_list, bg_color):
    write_button["text"] = "Write Note"
    write_button["command"] = lambda: write_message(field_list,
    frame_list[2], bg_color)
    write_button.grid(row=6, column=1)
# END OF FN make_follow_write_button

"""
Follow up on:
- unaffirmed IEP
- unaffirmed amendment
- unsigned IEP
- unsigned amendment 
"""
def follow_up(follow_type, follow_item, bg_color):
    # SET BACKGROUND
    w.f_follow_up["bg"] = bg_color

    # CREATE THE FRAMES
    page_frame = w.f_follow_up # !! FRAME
    close_frame = w.Frame(page_frame)
    input_frame = w.Frame(page_frame)
    note_frame = w.Frame(page_frame)

    frame_list = []
    frame_list.append(close_frame)
    frame_list.append(input_frame)
    frame_list.append(note_frame)
    w.configure_frames(frame_list, bg_color)

    # CREATE THE REQUEST DETAILS
    cm_name = w.Entry(input_frame)
    date = w.Entry(input_frame)
    stu_LN = w.Entry(input_frame)
    stu_FN = w.Entry(input_frame)
    seis_id = w.Entry(input_frame)

    # CREATE THE LIST OF FIELDS
    field_list = []
    field_list.append(follow_type) # 0
    field_list.append(follow_item) # 1
    field_list.append(cm_name) # 2
    field_list.append(date) # 3
    field_list.append(stu_LN) # 4
    field_list.append(stu_FN) # 5
    field_list.append(seis_id) # 6

    entry_list = []
    for i in range(2,7):
        entry_list.append(field_list[i])

    w.configure_entries(entry_list, w.entry_width_size)

    # USER INPUT FOR REQUEST DETAILS
    input_follow_details(field_list, input_frame, bg_color)

    # BUTTON TO TAKE TEXT ENTRIES AND POPULATE THE TEXTBOX
    write_button = w.Button(input_frame)
    make_follow_write_button(write_button, field_list, frame_list, bg_color)

    # BUTTON TO CLEAR WIDGETS FOR THIS TYPE OF REQUEST
    clearFrames_button = w.Button(close_frame)
    w.make_clear_frames_button(clearFrames_button, frame_list, bg_color)
# END OF FN follow_up

# EOF follow_up.py