# PowerMod_HTML

 A Python based builder for an HTML based PowerMod

 It is created with the help and guidance of PhD student Yfat Ben Refael and [Dr. Michal Hochhauser](https://www.ariel.ac.il/wp/itr/) at [Ariel University](https://www.ariel.ac.il/wp/en/) in Israel.
 PowerMod is a tool for assisting Occupational Therapists who are treating people with Intellectual and Developmental Disabilities (IDD).
 The `PowerMod_HTML.py` python script is intended to build a standalone webapp for a ["Gamified"](https://doi.org/10.1080/10447318.2024.2381928) intervention AKA "PowerMod".
 The product of the script is an `.html` file (`PowerMod.html`) and all the files and folders needed for PowerMod.
 In order to perform the intervention the content of the folder should be placed on any computer. Double clicking `PowerMod.html` will open a web browser and will allow you to perform the intervention.
 Important: Do not use MS Edge!

# Prerequisites
 1. Windows10 or above (for Linux instructions, contact developer).
 2. Python 3.10 up to 3.14 (hiegher virsions will be added in future versions)
 3. Prerecorded videos for the Video Modeling therapy: one problem video and three solution videos for each scenario. Only `.mp4`, `webm`, `3gp` or `ogg` files are applicable
 4. One repeseting image for each video. Only `png`, `jpg`, `jpeg`, `gif`, `webp`, or `bmp` files are applicable.
 5. One `.txt` file and one audio file for the clue in each scenario. Only `mp3`, `opus`, `ogg`, `aac`, or `flac` audio files are applicable.

# Usage
 1. double click `PowerMod_HTML.py`.
 2. Follow the on-screen instructions.
 3. If any issues occur, don't hesitate to open a GitHub issue.
 
 Good luck

# Translate
 In `languages` folder there are translation files for different languages.
 To have the PowerMod_HTML builder in your lageuage, please do the following:
 1. Create a `.json` file with your language name (in your language) (see `עברית.json` as an example for the Hebrew translation).
 2. Copy the content of the `English.jason_tamplate` and translate each row to your language.


 Note: wherever you want a new line in a long text, there should be a `\n` (represents a new line) and in order to have a `\` in a text (e.g.: "Please enter participant name\\number"), make sure to have a double backslash (i.e.: `\\`).



**Pro tip:**

if you start the script using:
`python PowerMod_HTML.py *YOURLANGUAGE WRITEN IN YOUR LANGUAGE*` (e.g.: `python PowerMod_HTML.py русский`)
You will not need to select a language during runtime. ;-)
