# Alston Library History Database - Extraction Project (ALHDEP)

The ALHD is composed of many HTML files. The desire is to get the data out of
the HTML files and into a CSV file.

Data from the CSV file can then be used to better organize and search in an
Excel like program, or used to create a more accessible website.

# Development

How to get the scripts working on your computer

## Requirements
- Python 3+
  - [Installing Python](https://realpython.com/installing-python/)
- Git
  - [Installing Git](https://git-scm.com/downloads)
- Terminal
- Code Editor
  - VS Code is a good one with built in Terminal
  - [Installing VS Code](https://code.visualstudio.com/Download)

## Set up
Download a copy of this repository. Open a terminal, or if using VS Code open
the terminal pane.

If you are in the folder where you want this project, then type in 
`https://github.com/ammonshepherd/library-history-database.git`

This will make a directory called 'library-history-database' in your folder
with all of the contents in this GitHub repo located inside.

Chage directory into that folder:

`cd library-history-database`

Next, create a virtual python environment in the 'library-history-database'
directory.


`python -m venv .venv`

Activate the virtual environment by running the command:

`source .venv/bin/activate`

Install the requirements

`pip install -r requirements.txt`


## Edit the bs.py script
The script uses BeautifulSoup to get rid of the HTML, leaving just the text.

There are two variables to alter, if desired, at the top of the script. 
- 'path' = The path to the HTML files you want to remove HTML from.
- 'save_folder' = The folder where you want the plain text files to be created.

Make the folder, replacing [folder name] with the word you used in the script.

`mkdir [folder name]`

Run the script like so:
`python bs.py`
