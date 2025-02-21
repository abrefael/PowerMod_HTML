# PowerMod_HTML

 A Python based builder for an HTML based PowerMod

 It is created with the help and guidance of PhD student Yfat Ben Refael and [Dr. Michal Hochhauser](https://www.ariel.ac.il/wp/itr/) at [Ariel University](https://www.ariel.ac.il/wp/en/) in Israel.
 PowerMod is a tool for assisting Occupational Therapists who are treating people with Intellectual and Developmental Disabilities (IDD).
 The `PowerMod_HTML.py` python script is intended to build a standalone webapp for a ["Gamified"](https://doi.org/10.1080/10447318.2024.2381928) intervention AKA "PowerMod".

# Prerequisites
 1. Windows10 or above (for Linux instructions, contact developer).
 2. Python 3.10 up to 3.14 (hiegher virsions will be added in future versions)
 3. Prerecorded videos for the Video Modeling therapy: one problem video and three solution videos for each scenario.
 4. One repesetative image for each video.
 5. One `.txt` file and One audio file for the clue in each scenario.

# Usage
 1. double click `PowerMod_HTML.py`.
 2. Follow the on-screen instructions.
 3. If any issues occur, don't hesitate to open a GitHub issue.
 
 Good luck

# Translate
 In `languages` folder there are translation files for different languages.
 To have the PowerMod_HTML builder in your lageuage, Please do the following:
 1. Create a `.json` file with your language name (in your language) (see `עברית.json` as an example for the Hebrew translation).
 2. Copy the content of the `English.jason_tamplate` and translate each row to your language.

 Note: wherever you want a new line in a long text, there should be a `\n` (represents a new line) and in order to have a `\` in a text (e.g.: "Please enter participant name\\number"), make sure to have a double backslash (i.e.: `\\`).
 

