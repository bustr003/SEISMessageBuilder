# FILE signature.py
"""
Parent signature statements.
"""

import window as w

"""
- List of statements
"""
def signature_statements(bg_color):
    # SET BACKGROUND
    w.f_sig_statement["bg"] = bg_color

    # CREATE THE FRAMES
    page_frame = w.f_sig_statement # !! FRAME
    close_frame = w.Frame(page_frame)
    #input_frame = w.Frame(page_frame)
    note_frame = w.Frame(page_frame)

    frame_list = []
    frame_list.append(close_frame)
    #frame_list.append(input_frame)
    frame_list.append(note_frame)
    w.configure_frames(frame_list, bg_color)

    # ALLOCATE A SPACE FOR THE DROPDOWN TO SELECT TERM
    #input_frame.pack()
    note_frame.pack()

    # HEADING
    text = "Signature Statements"
    l = w.Label(note_frame, text=text, bg=bg_color, font=("Courier New", 12), wraplength=250)
    l.grid(row=0, column=0, columnspan=2)

    # List of cases and statements
    cases = []

    case_0 = ("[ELIGIBLE]\nInitial Evaluation student found eligible for special education.",
        "I agree to all parts of the document.",
        "I agree to all parts of the IEP.")
    cases.append(case_0)

    case_1 = ("[EXCEPTION]\nAn IEP or changes to an IEP have been offered, but parent disagrees with portions of the proposed IEP.",
        "I agree with the document, with the exception of ____.",
        "I agree with the IEP, with the exception of ____.")
    cases.append(case_1)

    case_2 = ("[DECLINE]\nStudent found eligible for special education, but parent does not consent to the proposed services.",
        "I decline the offer of initiation of special education services.",
        "I decline the offer of initiation of special education services.")
    cases.append(case_2)

    case_3 = ("[DNQ]\nInitial Evaluation, student does not qualify for special education.",
        "I understand that my child is not eligible for special education.",
        "I understand that my child is not eligible for special education.")
    cases.append(case_3)

    case_4 = ("[EXIT 70]\nChange from Eligible to Exit/Drop",
        "I understand that my child is no longer eligible for special education.",
        "I understand that my child is no longer eligible for special education.")
    cases.append(case_4)

    case_5 = ("[PATRICIPATION ONLY]\nNo changes/updates/adjustments were made to the IEP, but you participated in an IEP meeting.",
        "Not Applicable - I am a parent/guardian /adult student signing in participation only.",
        "There is no equivalent option on the paper form.")
    cases.append(case_5)

    # TEXTBOX TO DISPLAY RESULTS
    textbox = w.Text(note_frame, wrap="word", font=("Calibri", 11))
    textbox.config(width=w.textbox_width, height=int(w.textbox_height*1.4))
    textbox.grid(row=2, column=0, columnspan=2)

    for case in cases:
        line = case[0] + "\n----------\n"
        line += ("E-Signature\n").upper()
        line += case[1] + "\n"
        line += ("Wet Signature\n").upper()
        line += case[2] + "\n----------\n\n"
        textbox.insert("end", line)

    # BUTTON TO CLEAR WIDGETS FOR THIS TYPE OF REQUEST
    go_home_button = w.Button(close_frame)
    w.make_go_home_button(go_home_button, frame_list, bg_color)

# EOF signature.py