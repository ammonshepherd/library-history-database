#!/usr/bin/env python

# Import the os and BeautifulSoup libraries
import os
from bs4 import BeautifulSoup


# Set the path of the directory files to scan
path = './AlstonLHD'

# Folder to save the extracted text files
save_folder = 'just_text'

# get all of the contents in the directory and store them as a list named
# "files"
with os.scandir(path) as files:

    # Loop through the list of files, store the info about each item in the
    # list in an object named "file"
    for file in files:

        # Check if the file ends with .htm and is actually a file (not a folder)
        if file.name.endswith('.htm') and file.is_file():

            # print out the file name
            print(file.path)

            # open the file for reading, and store the contents of the file in
            # the variable named "file_contents"
            with open(file.path) as file_contents:

                # Use a try..except so that if we get an error on one file the
                # whole script doesn't stop
                try:

                    # Parse the file contents using BeautifulSoup and store in
                    # an object named "parsed_content"
                    parsed_content = BeautifulSoup(file_contents, 'html.parser')

                    # Open a new file in the 'save_folder' directory with the
                    # same name as the original file, but with ".txt" added on
                    # the end. So if save_folder = text_files, then circ1.htm
                    # becomes /text_files/circ1.htm.txt
                    new_file = open("./" + save_folder + "/" + file.name + ".txt", "w")

                    # write just the text (no HTML/CSS/JS) to the new file
                    new_file.write(parsed_content.get_text())

                    # close the new file
                    new_file.close

                except Exception as error:

                    # Print out what file had an issue.
                    print("Error trying to get text out of " + file.path)
                    print(error)
