import os # Import the os module

def organize_files(directory): # Define the function to organize files in a directory

    # Check if the directory exists
    if not os.path.exists(directory): # Check if the directory exists
        return "Directory does not exist!" # Return an error message if the directory does not exist

    # Detect the operating system using os.name
    is_windows = os.name == 'nt' # Check if the operating system is Windows

    # Define file categories and corresponding file extensions
    file_types = { # Define the file categories and corresponding file extensions
        'Videos': ['.mp4', '.mkv', '.avi', '.mov'],
        'Audios': ['.mp3', '.wav', '.aac', '.flac'],
        'Images': ['.jpg', '.jpeg', '.png', '.gif', '.bmp'],
        'Documents': ['.pdf', '.doc', '.docx', '.xls', '.xlsx', '.ppt', '.pptx', '.txt'],
        'Misc': []
    }


    # Create folders for each file category if they don't already exist
    for folder in file_types.keys(): # Iterate over the file categories
        folder_path = os.path.join(directory, folder) # Create the folder path
        if not os.path.exists(folder_path): # Check if the folder does not exist
            os.makedirs(folder_path) # Create the folder if it does not exist


    # Iterate over the files in the directory
    for file_name in os.listdir(directory): # Iterate over the files in the directory
        file_path = os.path.join(directory, file_name) # Create the file path


        # Skip directories
        if os.path.isdir(file_path): # Check if the file is a directory
            continue # Skip the file if it is a directory
        
        # Determine the file extension
        file_extension = os.path.splitext(file_name)[1].lower() # Get the file extension and convert it to lowercase


        # Find the appropriate category for the file
        moved = False # Initialize the moved variable to False
        for folder, extensions in file_types.items(): # Iterate over the file types dictionary items
            if file_extension in extensions: # Check if the file extension belongs to the current category
                # Move the file to the corresponding folder
                destination = os.path.join(directory, folder, file_name) # Create the destination path
                
                # Check if file already exists at the destination
                if not os.path.exists(destination): # Check if the file does not exist at the destination
                    if is_windows: # Check if the operating system is Windows
                        os.system(f'move "{file_path}" "{destination}"') # Move the file to the destination
                    else: # If the operating system is not Windows
                        os.system(f'mv "{file_path}" "{destination}"') # Move the file to the destination
                moved = True # Set the moved variable to True
                break # Break the loop if the file is moved to a category folder
        
        # If no matching category is found, move to the 'Misc' folder
        if not moved: # Check if the file is not moved to a category folder
            misc_destination = os.path.join(directory, 'Misc', file_name) # Create the destination path for the 'Misc' folder
            if not os.path.exists(misc_destination): # Check if the file does not exist at the destination
                if is_windows: # Check if the operating system is Windows
                    os.system(f'move "{file_path}" "{misc_destination}"') # Move the file to the 'Misc' folder
                else: # If the operating system is not Windows
                    os.system(f'mv "{file_path}" "{misc_destination}"') # Move the file to the 'Misc' folder


    return "Files have been organized!" # Return a success message after organizing the files

# Test the function
directory = 'C:/Users/Username/Downloads' # Specify the directory path
print(organize_files(directory)) # Organize the files in the directory and print the result