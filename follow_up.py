# FILE follow_up.py
"""
Primary function for following up on IEPs and amendments.
"""

import window as w

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
    w.input_follow_details(field_list, input_frame, bg_color)

    # BUTTON TO TAKE TEXT ENTRIES AND POPULATE THE TEXTBOX
    write_button = w.Button(input_frame)
    w.make_follow_write_button(write_button, field_list, frame_list, bg_color)

    # BUTTON TO CLEAR WIDGETS FOR THIS TYPE OF REQUEST
    clearFrames_button = w.Button(close_frame)
    w.make_clearFrames_button(clearFrames_button, frame_list, bg_color)
# END OF FN follow_up

# EOF follow_up.py