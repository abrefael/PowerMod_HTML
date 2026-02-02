# PowerMod_HTML

 A Python based builder for an HTML based PowerMod

 It is created with the help and guidance of PhD student Yfat Ben Refael and [Dr. Michal Hochhauser](https://www.ariel.ac.il/wp/itr/) at [Ariel University](https://www.ariel.ac.il/wp/en/) in Israel.
 PowerMod is a tool for assisting Occupational Therapists who are treating people with Intellectual and Developmental Disabilities (IDD).
 The `PowerMod_builder.py` python script is intended to build a standalone webapp for a ["Gamified"](https://doi.org/10.1080/10447318.2024.2381928) intervention AKA "PowerMod".
 The product of the script is a folder, containing an `.html` file (`PowerMod.html`) and all the files and folders needed for PowerMod to work.
 In order to perform the intervention, the content of the folder should be placed on any computer. Double clicking `PowerMod.html` will open a web browser and will allow you to perform the intervention.

 Important: Do not use MS Edge for the intervention!

# Prerequisites
 1. Windows10 or above, Linux or Mac.
 2. For Linux\Mac, [Python 3.10](https://www.python.org/) or above.
 3. Prerecorded videos for the Video Modeling therapy: one problem video and three solution videos for each scenario. Only `.mp4`, `webm`, `3gp` or `ogg` files are applicable!
 4. One representing image for each video. Only `png`, `jpg`, `jpeg`, `gif`, `webp`, or `bmp` files are applicable!
 5. One `.txt` file and one audio file for the clue in each scenario. Only `mp3`, `opus`, `ogg`, `aac`, or `flac` audio files are applicable!
 6. All files should be placed in `1.📥Put_Media_Files_in_Here` folder.

# Usage
 1. Under Windows, double click `2.🧩Let's Build`. Under Linux\Mac, make `PowerMod_builder.py` executable (e.g. `chmod +x PowerMod_builder.py`), then run it (e.g. `./PowerMod_builder.py` or double-click it). A "Commad" (Terminal, Console etc.) window will appear in the background and your web browser will start the system.
 2. Select number of scenarios and type of activity (normal or minimal).
 3. Add files according to the list in you web browser. Don't forget to select files from the aforementioned `1.📥Put_Media_Files_in_Here` folder. You will have visual feedback that you selected the right file from the correct path.
 4. Write the text hints into their respected places.
 5. When ready, select whether or not you wish to save data from your sessions, and click the "*Go!*" button.
 6. The process will be done within a few seconds, and you will see the entire PowerMod HTML tree inside newly created `Play` folder. When all is done, the "Command" windows from above will close.
 7. To start a PowerMod session with your clients, just copy the content of `Play` to any computer (e.g.: place on a thumb drive). Thus at your clients, all you need to do is run `PowerMod.html` using any web browsers.
 8. If any issues occur, don't hesitate to open a GitHub issue.
 
 Good luck! 😄️

