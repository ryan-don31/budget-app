# budget-app

Bit of an interesting experiment with tkinter I was working on a couple months back. Has little actual functionality, but uses some methods I couldn't find elsewhere online.

## Methods used
The program almost entirely relies on csv files, since that's what I'm used to from a previous project I was working on, but I'm planning on switching it to use json if I decide to keep working on this
### File loading
Uses seperate csv files for different instances of entries.
- New button, copies template file and renames it to current pc time
- Load button, opens a window with a dropdown menu to choose from files in the datafiles folder
### File reading
- each file holds different chunks of information that are written to the textboxes seen by the user
### List management
- uses tkinters atrocious textbox widget to append and pop from the list of item entries
