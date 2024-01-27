# Import the module 'os' to interact with the operating system
import os
# import pandas for data manipulation
import pandas as pd


# Create a function to hold the process
def files_in_folder(path):
    # define 'files' as a global variable for use outside the function
    global files
    # change the backslashes to forward slashes in the folder path
    path = path.replace('"', '').replace(r"\\", r"/")
    # A 'try:' statement is used to handle exceptions and errors that might occur within
    # its block
    try:
        # Select the files as a list from the folder given by the path
        files = os.listdir(path)

        # Filter out files specifically not other directories using a single line for loop
        files = [file for file in files if os.path.isfile(os.path.join(path, file))]

        # Now count the number of files selected by way of 'len()' to see how long the list is
        num_of_files = len(files)
        # Finding the file names 'if' the list length is greater than 0
        if 15 > num_of_files > 0:
            # Print message with # of files found in the folder based on # of files
            if 5 > num_of_files > 0:
                # Funny message added
                print(f"Files found:{num_of_files} in {path}\nHave You Done Anything Outside of Class?!?!")
            else:
                # Original  message
                print(f"Files found:{num_of_files} in {path}\n")
            # Print files found
            print("Files located:")
            # For loop to iterate over each element in the list
            for name in files:
                # Print the name of the file found
                print(name)
        # Else statement that changes 'files' to a dataframe for folders with more than 15 files
        else:
            # Original  message
            print(f"Files found:{num_of_files} in {path}\n")
            # Turn 'files' into a dataframe with 'num_of_files' as the index column
            files = pd.DataFrame({num_of_files: files})
            # Rename column with file names to 'file_name'
            files.columns = ['file_name']
            # print the 1st five rows of the dataframe 'files'
            print(files.head())
    # Use an 'except' to give a result of an error message that no files were found
    except FileNotFoundError:
        # Print the message
        print(f"No files found in {path}")


# run is set to true to give the while loop a value to decide w
run = True
while run:
    # Run the function using your chose folder path
    files_in_folder(input("Type in or paste your file path! :"))
    # Use an input to determine if the user wants to search another folder or end the program
    run_again = input("Enter 1 if finished\n"
                      "Enter 2 to search another folder\n")
    # if the user types '1' then quit the program
    if run_again == '1':
        # changes run to False
        run = False
        # break means to stop the program at this current point
        break
    # if the user types '2' then run the program again
    elif run_again == '2':
        # run remains true
        run = True
    # Else statement to return an error message if both above conditions are not met.
    else:
        # another way to stop the program, this time with our own created error.
        raise ValueError("Not a valid option!")
