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

    # Synonyms
    rsp_sai_def = "\nResource Specialist Program / Specialized Academic Instruction\nServices may or may not be in separate class."
    sc_sdc_def = "\nSeparate Class / Separate Day Class"

    # A dictionary to store the terms and their definitions
    terms = {
        "APE" : "Adapted Physical Education",
        "CSAT" : "Comprehensive Student Assistance Teams\nA general education process for identifying and supporting students",
        "DHH" : "Deaf and Hard of Hearing",
        "HHI" : "Home Hospital Instruction\nA service for students who are unable to attend school in person due to health needs. The student will still have a \"School of Attendance\" that they would normally attend should they be able to attend school physically. Until then, the student receives their services and education in home setting.",
        "OT" : "Occupational Therapy",
        "PDT" : "Preschool Diagnostic Team",
        "SEAS" : "Social Emotional Academic Support",
        "DIS" : "Designated Instruction and Services\nNo SAI services, but also not Speech Only.\nExamples: APE, DHH, OT",
        "RSP" : "- same as SAI" + rsp_sai_def,
        "SAI" : "- same as RSP" + rsp_sai_def,
        "SC" : "- same as SDC" + sc_sdc_def,
        "SDC" : "- same as SDC" + sc_sdc_def,
        "SPEECH ONLY" : "Only has Language and Speech services\nPreschoolers are not in PowerSchool."
    }

    # A list to store the terms
    term_list = []
    for term, result in terms.items():
        term_list.append(term)
        print(term)

    # ALLOCATE A SPACE FOR THE DROPDOWN TO SELECT TERM
    input_frame.pack()

    text = "Type a term, then press ENTER."
    text += "\nTo search, type letter(s) then press the down arrow key."
    l = w.Label(input_frame, text=text, bg=bg_color)
    l.grid(row=0, column=1)

    selected_term = w.StringVar()
    selected_term.set("Select Term")
    
    # TEXTBOX TO DISPLAY RESULTS
    note_frame.pack()
    textbox = w.Text(note_frame, wrap="word", font=("Calibri", 11))
    textbox.config(width=w.textbox_width, height=int(w.textbox_height*1.5))
    textbox.grid(row=0, column=0, columnspan=2)

    """
    FN PURPOSE: When a dropdown option is selected, display the result in the textbox.
    """
    def display_result(event):
        selected_term = combobox.get().upper() # Convert to all uppercase

        # Exact Match
        if selected_term in term_list:
            line = selected_term + "\n" + terms[selected_term] + "\n\n"
            textbox.insert("end", line)

        # No matches
        else:
            line = selected_term + " was not found in the Glossary.\n\n"
            textbox.insert("end", line)


    def edit_combobox_values(event):
        selected_term = combobox.get().upper() # Convert to all uppercase
        similar_terms = []

        for term in term_list:
            if selected_term in term:
                similar_terms.append(term)
        combobox["values"] = similar_terms
    
    # COMBOBOX TO SELECT A TERM
    combobox = w.ttk.Combobox(input_frame, value=term_list, width=50)
    combobox.bind("<<ComboboxSelected>>", display_result)
    combobox.bind("<KeyRelease>", edit_combobox_values)
    combobox.bind("<Return>", display_result)
    combobox.grid(row=1, column=1)

    # BUTTON TO CLEAR WIDGETS FOR THIS TYPE OF REQUEST
    clearFrames_button = w.Button(close_frame)
    w.make_clear_frames_button(clearFrames_button, frame_list, bg_color)

# EOF glossary.py