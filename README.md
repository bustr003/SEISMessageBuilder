# SEISMessageBuilder
https://github.com/bustr003/SEISMessageBuilder.git

PROGRAM TITLE: MessageBuilderGUI
ALTERNATE TITLES:
- SEISMessageBuilder
- SpEd Message Builder
AUTHOR: Mhealyssah Bustria
DATE CREATED: September or October 2022 - on personal laptop
DATE FIRST ACCESSED ON WORK COMPUTER: 10/28/2022

Message builder related to managing the Special Education Information System

Uses Tkinter to make a GUI.

Icon image (bunny) created by Neala Mendoza.

---

# Files

Files for setting up the GUI
1) menu.py The main file.
- - Creates the home page and menu options.
- - RUN FROM THIS FILE!!!
2) window.py The GUI window & secondary functions
- - Creates the GUI window.
- - Contains functions that are shared by multiple menu options.

Files for the primary functions and own functions of each menu option
3) add.py For add requests
4) status.py For status change requests.
5) record.py For record change requests.
6) exit_student.py For exit requests.
7) follow_up.py For unaffirmed/unsigned IEPs/Amendments

Files for references
8) glossary.py An interactive glossary
9) duplicates.py Handling duplicate records

# TO DO
- Update "Note for" heading for each request
- Add update log in Resources
- Add "Student transferred from a non-SEIS district" to Adds
- Change Adds to a checkbox + combobox + popup style

## DONE
11/30/2022
- Added a message builder for changing the meeting type of an affirmed IEP.

11/28/2022
- Clear textbox upon clearing fields

11/26/2022
- Add APE and DHH to staff roles
- Make staff roles a combo box (not just dropdown)
- Add the feature that removes all children, instead of needing to press x
- Add instructions for duplicate records
- Add latest update date & location to home page
- Add image on to Home button
