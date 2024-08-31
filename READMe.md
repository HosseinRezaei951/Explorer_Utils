# Explorer Utils

## Project Overview

The **Explorer Utils** project is a Python-based command-line utility designed to perform various operations on files and directories. This tool provides functionalities such as displaying file or directory information, listing directory contents, searching for files or directories, and renaming files or directories within a directory and its subdirectories. The goal of this project is to create a flexible and easy-to-use utility that works across different operating systems, without relying on platform-specific commands.

## Features

1. **Show File or Directory Information**:
   - Displays detailed information about a specific file or directory provided by the user, including name, path, size, permissions, and last modification date.
   - Example usage:
     ```
     explorerutil.py \usr\home\cs99
     ```
     Output:
     ```
     -rw-rw-rw- 1 cs99 dir 104 Dec 25 19:32 file
     ```

2. **Show Directory Contents**:
   - Lists all files and subdirectories within a specified directory, displaying their respective attributes.
   - Example usage:
     ```
     explorerutil.py \usr\home\cs99exe
     ```
     Output:
     ```
     Ahmad   folder  dir 104 Dec 10 11:39
     SimaAssig1   folder  dir 104 Dec 27 05:15
     Mohammad   folder  dir 104 Dec 28 16:42
     ```

3. **Search File or Directory in Directory**:
   - Searches for a specific file or directory within a given directory and its subdirectories, showing the full path and attributes of the found item.
   - Example usage:
     ```
     explorerutil.py \usr\home\cs99exe Ahmad
     ```
     Output:
     ```
     Ahmad   \cs99exe\assignment1   folder  dir 104 Dec 10 11:39
     ```

4. **Rename File or Directory**:
   - Renames files or directories with a specified name within a given directory and all its subdirectories.
   - Example usage:
     ```
     explorerutil.py \usr\home\cs99 PICS99A1 Assignment1
     ```
     Output:
     ```
     SimaAssig1/PICS99AI   file  dir 104 Dec 27 05:15
     Mohammad/PICS99AI   file  dir 104 Dec 28 16:42
     ```

## Implementation Details

### 1. Cross-Platform Compatibility
To ensure the tool works seamlessly across different operating systems, the implementation avoids using platform-specific commands. The project relies on Python's built-in modules like `os`, `time`, `stat`, and `pathlib` to interact with the file system.

### 2. Switch Class
The **Switch** class is designed to manage the different functionalities of the tool. It includes methods corresponding to each feature, which are called based on user input. The class uses a simple switch-case-like mechanism to navigate between the different options presented in the main menu.

### 3. File Class
The **File** class encapsulates the details of a file or directory. It provides methods to retrieve and display file information, as well as to list the contents of a directory. This class plays a crucial role in executing the core functionalities of the project.

### 4. Rename Function
The `rename` function is responsible for renaming files or directories. It traverses the specified directory and its subdirectories, searching for the target file or directory by name. If found, it renames the item and displays its updated information.

## How to Use

1. Clone the repository or download the script.
2. Run the script using Python 3.x.
3. Follow the on-screen instructions to navigate through the different functionalities.
4. Use the main menu to select the desired operation by entering the corresponding number.
