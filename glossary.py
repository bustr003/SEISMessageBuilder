# FILE glossary.py
"""
Create and display an interactive glossary.
"""

import window as w
import sped_dictionary as d

# TERMS: A dictionary to store the terms and their definitions
terms = {
    "APE" : "Adapted Physical Education",
    "CALPADS" : d.calpads_def,
    "CSAT" : d.csat_def,
    "DHH" : d.dhh_def,
    "DISCRETE TRIAL TEACHING" : d.discrete_trial_def,
    "DOMAINS OF INSTRUCTION" : d.domains_def,
    "DSEA" : d.dsea_def,
    "EPIPHANY PREP" : d.epiphany_def,
    "HERITAGE" : d.heritage_def,
    "HERITAGE FLEX ACADEMY" : d.hfa_def,
    "HHI" : d.hhi_def,
    "LCAP" : d.lcap_def,
    "LCFF" : d.lcff_def,
    "LEA" : d.lea_def,
    "LLA" : d.lla_def,
    "M/M" : d.mm_def,
    "M/S" : d.ms_def,
    "NEWS 2 YOU" : d.news2you_def,
    "OT" : "Occupational Therapy",
    "PDT" : "Preschool Diagnostic Team",
    "PRESCHOOL" : d.preschool_def,
    "PROACT" : d.proACT_def,
    "PROGRAM SUPPORTS" : d.program_supports_def,
    "DIS" : d.dis_def,
    "RSP" : "- same as SAI" + d.rsp_sai_def,
    "SAI" : "- same as RSP" + d.rsp_sai_def,
    "SC" : "- same as SDC" + d.sc_sdc_def,
    "SCSB" : d.scsb_def,
    "SDC" : "- same as SC" + d.sc_sdc_def,
    "SEAS" : d.seas_def,
    "SELPA" : d.selpa_def,
    "SOAR" : "An elective offered to middle schoolers.\n- Set Goals\n- Organize\n- Ask Questions\n- Record Progress",
    "SPEECH ONLY" : "Only has Language and Speech services\nPreschoolers are not in PowerSchool.",
    "ULS" : d.uls_def
}

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

    # A list to store the terms
    term_list = []
    for term, result in terms.items():
        term_list.append(term)

    # ALLOCATE A SPACE FOR THE DROPDOWN TO SELECT TERM
    input_frame.pack()

    text = "Type a term, then press ENTER."
    text += "\nTo search, type letter(s) then press the down arrow key."
    l = w.Label(input_frame, text=text, bg=bg_color)
    l.grid(row=0, column=0, columnspan=2)

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
            textbox.tag_config("error", foreground=w.dark_red)
            textbox.insert("end", line, "error")


    def edit_combobox_values(event):
        selected_term = combobox.get().upper() # Convert to all uppercase
        similar_terms = []

        for term in term_list:
            if selected_term in term:
                similar_terms.append(term)
        combobox["values"] = similar_terms
    
    # COMBOBOX TO SELECT A TERM
    combobox = w.ttk.Combobox(input_frame, value=term_list, width=30)
    combobox.bind("<<ComboboxSelected>>", display_result)
    combobox.bind("<KeyRelease>", edit_combobox_values)
    combobox.bind("<Return>", display_result)
    combobox.grid(row=1, column=0)

    # BUTTON TO RESET THE FIELDS
    def clear_textbox():
        textbox.delete("1.0", "end")

    clear_textbox_button = w.Button(input_frame, text="Clear Results")
    clear_textbox_button["command"] = clear_textbox
    clear_textbox_button.grid(row=1, column=1)

    # BUTTON TO CLEAR WIDGETS FOR THIS TYPE OF REQUEST
    go_home_button = w.Button(close_frame)
    w.make_go_home_button(go_home_button, frame_list, bg_color)

# EOF glossary.py