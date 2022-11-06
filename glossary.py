# FILE glossary.py
"""
Create and display an interactive glossary.
"""

import window as w

"""
- Definitions of terms
- Expansion of abbreviations
"""
def glossary(bg_color):
    # SET BACKGROUND
    w.f_glossary["bg"] = bg_color

    # CREATE THE FRAMES
    page_frame = w.f_glossary # !! FRAME
    close_frame = w.Frame(page_frame)
    input_frame = w.Frame(page_frame)
    note_frame = w.Frame(page_frame)

    frame_list = []
    frame_list.append(close_frame)
    frame_list.append(input_frame)
    frame_list.append(note_frame)
    w.configure_frames(frame_list, bg_color)

    # TERMS
    # A dictionary to store the terms and their definitions
    terms = {
        "CSAT" : "Comprehensive Student Assistance Teams\nA general education process for identifying and supporting students",
        "HHI" : "Home Hospital Instruction\nA service for students who are unable to attend school in person due to health needs. The student will still have a \"School of Attendance\" that they would normally attend should they be able to attend school physically. Until then, the student receives their services and education in home setting.",
        "PDT" : "Preschool Diagnostic Team",
        "SEAS" : "Social Emotional Academic Support"
    }

    # A list to store the terms
    term_list = []
    for term, result in terms.items():
        term_list.append(term)

    # ALLOCATE A SPACE FOR THE DROPDOWN TO SELECT TERM
    input_frame.pack()
    selected_term = w.StringVar()
    selected_term.set("Select Term")
    
    # TEXTBOX TO DISPLAY RESULTS
    note_frame.pack()
    textbox = w.Text(note_frame, wrap="word")
    textbox.config(width=w.textbox_width, height=int(w.textbox_height*1.75))
    textbox.grid(row=0, column=0, columnspan=2)

    """
    FN PURPOSE: When a dropdown option is selected, display the result in the textbox.
    """
    def display_result(event):
        term = selected_term.get()
        line = term + ":" + terms[selected_term.get()] + "\n\n"
        textbox.insert("end", line)
    
    # DROPDOWN TO SELECT A TERM
    dropdown = w.OptionMenu(input_frame, selected_term, *term_list, command=display_result)
    dropdown.grid(row=0, column=0)

    # BUTTON TO CLEAR WIDGETS FOR THIS TYPE OF REQUEST
    clearFrames_button = w.Button(close_frame)
    w.make_clearFrames_button(clearFrames_button, frame_list, bg_color)

# EOF glossary.py