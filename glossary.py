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

    # Definitions
    calpads_def = "California Longitudinal Pupil Achievement Data System"

    csat_def = "Comprehensive Student Assistance Teams\n- A general education process for identifying and supporting students."

    dhh_def = "Deaf and Hard of Hearing"
    dhh_def += "\n- Program Specialist: Meghan Carlon"
    dhh_def += "\n- AUDITORY ORAL PROGRAM: Students with hearing loss/Cochlear Implant process. Intensive auditory training and instruction to increase listening and speaking skills. Specialized DHH teacher & Speech Therapist."
    dhh_def += "\n- TOTAL COMMUNICATION/SIGNING PROGRAM: Paraeducators who use sign language & certificated ASL interpreters."
    dhh_def += "\n - ITINERANT PROGRAM: Full Time itinerant DHH teacher and audiologist."

    dis_def = "Designated Instruction and Services\n- No SAI services, but also not Speech Only.\n- Examples: APE, DHH, OT"

    discrete_trial_def = "- Educational strategy based on the principles of applied behavior analysis"
    discrete_trial_def += "\n- Break skills down into smaller components"
    discrete_trial_def += "\n- Teach  sub-skills individually"
    discrete_trial_def += "\n- Repeated practice of skills"
    discrete_trial_def += "\n- Prompting procedures"
    discrete_trial_def += "\n- Reinforcement procedures"

    domains_def = "M/S classes teach across the domains."
    domains_def += "\n- ACADEMICS: Whole/small group/individualized instruction for core content and IEP Goals"
    domains_def += "\n- COMMUNICATION: Language development and communication skills with all modes of communication and Augmentative or Alternative Communication in a language-rich environment"
    domains_def += "\n- COMMUNITY SKILLS: Safety skills, transitioning and navigating camps"
    domains_def += "\n- DAILY LIVING SKILLS: Hygiene, feeding, toileting"
    domains_def += "\n- RECREATION/LEISURE: Making choices, individual choice Activities, collaborative games/activities"
    domains_def += "\n- SOCIAL EMOTIONAL: Self regulation, expected behaviors, social interactions"
    domains_def += "\n- VOCATIONAL SKILLS: Classroom jobs, task lists, student store operation, following directions"

    dsea_def = "District of SpEd Accountability"

    epiphany_def = "Epiphany Prep Charter School"
    epiphany_def += "\nhttps://www.cde.ca.gov/schooldirectory/details?cdscode=37680980133991"
    epiphany_def += "\n- closed"

    heritage_def = "American Heritage Charter Schools family of charter schools"
    heritage_def += "\n- Heritage K-8 Charter"
    heritage_def += "\n- SpEd support services offered through EUSD"
    heritage_def += "\n- DSEA is EUSD"

    hfa_def = "Heritage Flex Academy"
    hfa_def += "\nhttps://hfa.amhcs.org/about/welcome/"
    hfa_def += "\n- TK-8"

    hhi_def = "Home Hospital Instruction\n- A service for students who are unable to attend school in person due to health needs."
    hhi_def += "\n- The student will still have a \"School of Attendance\" that they would normally attend should they be able to attend school physically."
    hhi_def += "\n- Until then, the student receives their services and education in home setting."

    lcap_def = "Local Control and Accountability Plan"
    lcap_def += "\n- A critical part of California's new Local Control Funding Formula (LCFF)"
    lcap_def += "\n- A three-year, district-level plan that is updated annually"

    lcff_def = "Local Control Funding Formula"

    lea_def = "Local Education Agency"
    lea_def += "- EUSD"

    lla_def = "Limitless Learning Academy"
    lla_def += "\nhttps://www.eusd.org/o/lla/page/about-us"
    lla_def += "\n- Blended Learning K-8 Option"
    lla_def += "\n- virtual and hybrid learning"
    lla_def += "\n- engaging lessons via Zoom in the morning"
    lla_def += "\n- personalized learning in the afternoon via in-person or virtually"

    mm_def = "Mild/Moderate"
    mm_def += "\n- M/M SAI"
    mm_def += "\n- M/M SAI SC"

    ms_def = "Moderate-Severe"
    ms_def += "\n- Program Specialist: Alice Abalos"
    ms_def += "\n- M/S classrooms have a SAI teacher and paraeducators who work together to actively engage students in the learning process." 
    ms_def += "\n- Classroom staff work collaboratively with related service providers for a comprehensive approach to addressing each student’s unique needs."
    ms_def += "\n- M/S classes teach across the domains of instruction."

    news2you_def = "- Weekly current events stories and related learning activities"

    orton_gillingham_def = "Orton-Gillingham (OG) structured literacy approach"
    orton_gillingham_def += "\n- Provides instruction on phonemic awareness, phonics, spelling, grammar"

    preschool_def = "https://www.eusd.org/o/preschool/page/eusd-state-preschool-about-us"
    preschool_def += "- Program Specialist: Natalie Muldoon"
    preschool_def += "\n- STATE PRESCHOOL SAI INCLUSION: Provides access to the GenEd environment"
    preschool_def += "\n-- Subsidized programs for low income families"
    preschool_def += "\n-- CSPP: California State Preschool Program"
    preschool_def += "\n-- SDQPI: San Diego Quality Preschool Initiative"
    preschool_def += "\n- NON-CATEGORICAL CLASSES: Peer buddies & paraeducators"
    preschool_def += "\n- SCSB PRESCHOOL CLASSES"

    proACT_def = "Pro-ACT"
    proACT_def += "\n- Professional Assault Crisis Training"

    program_supports_def = "- A critical component in all moderate to severe programs"
    program_supports_def += "\n- Embedded supports that enhance a child's education"
    program_supports_def += "\n- Examples: communication device, chewy necklace, compression vest"

    rsp_sai_def = "\n- Resource Specialist Program\n- Specialized Academic Instruction"
    rsp_sai_def += "\n- Program Specialists, Elementary: Meghan Carlon and Carol Fekete"
    rsp_sai_def += "\n- Program Specialist, Middle: Dena Moore"
    rsp_sai_def += "\n- The M/M SAI program teaches grade level common core standards in conjunction with the GenEd teacher either in the GenEd setting or in the SpEd classroom"
    rsp_sai_def += " so that students feel supported, engaged and committed to meeting their individualized goals."
    
    sc_sdc_def = "\nSeparate Class / Separate Day Class"
    sc_sdc_def += "\n- Program Specialist: Giuliana Forte (Elementary)"
    sc_sdc_def += "\n- The M/M separate class program offers classes that address the unique needs of our students with mild to moderate challenges."

    scsb_def = "Structured Communication Social Behavioral classes"
    scsb_def += "\n- Program Specialist: Tracy Lane"
    scsb_def += "\n- Provide some of our most intensive supports to students with Autism or other developmental disabilities"
    scsb_def += "\n- Provide students with intensive supports, predictable, consistent routines and structure throughout the school day to engage the students in learning activities such as functional communication, social skills, academics, and behavior management."
    scsb_def += "\n- Clearly-defined spaces for whole group activities, small group instruction, Discrete Trial Training, independent work, and cool down/break areas"

    seas_def = "Social Emotional Academic Support classes"
    seas_def += "\n- previously: Intensive Behavioral Intervention program"
    seas_def += "\n- Program Specialist: Dena Moore"
    seas_def += "\n- Addresses the needs of students exhibiting significant social, emotional, and behavioral concerns"
    seas_def += "\n- Therapeutic/mental health supports"
    seas_def += "\n- CLINICAL SOCIAL WORKERS: individual counseling, groups, risk assessments, parent trainings and consultations, help case manage with outside providers"
    seas_def += "\n- SCHOOL PSYCHOLOGIST: behavioral programming, risk assessments, educationally related mental health assessments"
    seas_def += "\n- Treatment Team: weekly meetings"

    selpa_def = "SpEd Local Planning Area"
    selpa_def += "\n- EUSD is in the North Inland SELPA"
    selpa_def += "\n- Heritage K-8 Charter is in the North Inland SELPA"

    uls_def = "Unique Learning Systems"
    uls_def += "\n- A standard-aligned curriculum, differentiated materials across all content areas"

    # A dictionary to store the terms and their definitions
    terms = {
        "APE" : "Adapted Physical Education",
        "CALPADS" : calpads_def,
        "CSAT" : csat_def,
        "DHH" : dhh_def,
        "DISCRETE TRIAL TEACHING" : discrete_trial_def,
        "DOMAINS OF INSTRUCTION" : domains_def,
        "DSEA" : dsea_def,
        "EPIPHANY PREP" : epiphany_def,
        "HERITAGE" : heritage_def,
        "HERITAGE FLEX ACADEMY" : hfa_def,
        "HHI" : hhi_def,
        "LCAP" : lcap_def,
        "LCFF" : lcff_def,
        "LEA" : lea_def,
        "LLA" : lla_def,
        "M/M" : mm_def,
        "M/S" : ms_def,
        "NEWS 2 YOU" : news2you_def,
        "OT" : "Occupational Therapy",
        "PDT" : "Preschool Diagnostic Team",
        "PRESCHOOL" : preschool_def,
        "PROACT" : proACT_def,
        "PROGRAM SUPPORTS" : program_supports_def,
        "DIS" : dis_def,
        "RSP" : "- same as SAI" + rsp_sai_def,
        "SAI" : "- same as RSP" + rsp_sai_def,
        "SC" : "- same as SDC" + sc_sdc_def,
        "SCSB" : scsb_def,
        "SDC" : "- same as SDC" + sc_sdc_def,
        "SEAS" : seas_def,
        "SELPA" : selpa_def,
        "SOAR" : "An elective offered to middle schoolers.\n- Set Goals\n- Organize\n- Ask Questions\n- Record Progress",
        "SPEECH ONLY" : "Only has Language and Speech services\nPreschoolers are not in PowerSchool.",
        "ULS" : uls_def
    }

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
    clearFrames_button = w.Button(close_frame)
    w.make_clear_frames_button(clearFrames_button, frame_list, bg_color)

# EOF glossary.py