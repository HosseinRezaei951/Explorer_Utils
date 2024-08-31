import os, time
import stat
from pathlib import Path 

############################################################
# GLOBAL STRINGS
############################################################

# for main program panel 
PANEL_MESSAGE =             "\t1- Show file or directory information\n"+\
                            "\t2- Show directory contents\n"+\
                            "\t3- Search file or directory in directory\n"+\
                            "\t4- Rename file or directory in directory and it's sub-directories\n"+\
                            "\t0- Exit "
                            
SWITCH_MESSAGE =            "\n Plz select your function: "
EMPTY_INPUT =               "\n Empty input !!!"
INVALID_MESSAGE =           "\n Invalid input !!!"
RETURN_MESSAGE =            "\n Press any key to return panel ..."
TRY_AGAIN_MESSAGE =         "\n Press any key to try again ..."
NUMBER_OF_FUNCTIONS = 4


############################################################
# CEAR SCREEN 
############################################################

def clear_screen():
    '''
    Code to clear running screen
    '''    
    # for mac and linux(here, os.name is 'posix')
    if os.name == 'posix':
        _ = os.system('clear')
    else:
        # for windows platfrom
        _ = os.system('cls')


############################################################
# RENAME 
############################################################

def rename(current_path, source_path, destination_path):
    ''' <note: The word «file» in these sentences means file or directory>
        It renames source_path file to destination_path when source_path file located in current_path.
        Parameters: current_path - type:string - the path that we try to find source_path file in it.
                    source_path - type:string - the path of file that we want to change it name.
                    cadestination_pathnvas - type:string - the name of source_path file we want to finally 
                                                 have after rename.         
    '''
    found_flag = False
    for x in os.walk(current_path , topdown=False) :
       
        source_full_path = os.path.join(os.path.normpath(x[0]), source_path)
        destination_full_path = os.path.join(os.path.normpath(x[0]), destination_path)
        
        if (os.path.isfile(source_full_path) or os.path.isdir(source_full_path)) :
            if found_flag == False :
                found_flag = True
            
            try:
                tmpFile = File(source_full_path)
                os.rename(source_full_path, destination_full_path)
                tmpFile.print_information()
            
            except OSError as error: 
                print("\n ", error)
            

    if found_flag == False:
        print("\n Couldn't find any file or directory with " +\
            "«" + source_path + "» name in «" + current_path + "» and its sub-directories ... ")            


############################################################
# FILE CLASS
############################################################ 
  
class File(object):
    '''
        File class: it represents file or directory.
        Attributes: dir - type:string - real path of file.
    '''

    def __init__(self, dir):
        self.status = os.stat(os.path.normpath(os.path.realpath(dir)))
        self.mode = self.status.st_mode  
        
        self.name = os.path.basename(dir)
        self.path = os.path.normpath(os.path.realpath(dir))
        self.size_in_bytes = self.status.st_size
        self.hard_links = self.status.st_nlink
        self.permissions = stat.filemode(self.mode)
        self.last_modification = time.asctime(time.localtime(os.path.getmtime(dir)))     
            
    
    def get_information(self):
        '''
        Returns all information of the File object.
        '''
        result = {} 
        result['name'] = self.name
        result['path'] = self.path
        result['size_in_bytes'] = self.size_in_bytes
        result['hard_links'] = self.hard_links
        result['permissions'] = self.permissions
        result['last_modification'] = self.last_modification
        return result
    

    def get_directory_contents(self):
        '''
        If the File object is a directory, returns all contents file or directories in it.
        Otherwise return 0.
        '''
        contents = []
        if stat.S_ISDIR(self.mode):
            directory_list = os.listdir(self.path)
            for x in directory_list:
                contents.append(File(os.path.normpath(os.path.realpath(self.path + "/" + x))))
            return contents
        else:
            return 0
    

    def print_information(self):
        '''
        Print all information of the File object.
        '''       
        info = self.get_information()
        print()
        for x in info:
            print(" " + x + ": " , info[x])
    

    def print_directory_contents_information(self):
        '''
        Print all information of directory contents of the File object.
        '''   
        contents = self.get_directory_contents()
        print()
        if contents != 0:
            for i in range(0, len(contents)):
                print(" ======================================== ")
                print(" " , i+1 , ": ")
                contents[i].print_information()
                print(" ======================================== ")
                print() 


############################################################
# FILE CLASS
############################################################ 

class Switch(object):
    ''' 
        Switch class: it represents switching between parts of panel.
    '''

    def select(self, i):
        ''' 
            Get a number and represents part of panel .
            Parameters: i - type: string - a number between 1 and  NUMBER_OF_FUNCTIONS
                                           that used to select one part of the panel.
        ''' 
        method_name = 'number_' + str(i)
        method = getattr(self, method_name, lambda :input(INVALID_MESSAGE + RETURN_MESSAGE))
        return method()


    '''
    <Each method of this class represents one part of panel. And any of them help user 
     to get inputs and doing some thing.>
    '''
    def number_1(self):
        while True:
            clear_screen()
            print("\n\t *** Show file or directory information ***")
            user_input = input("\n plz enter your «Directory» or «File name(with extension)»" + \
                                " <or 0 for exit>: ") 
            if user_input == "0":
                return
            elif user_input == "":
                input(EMPTY_INPUT + TRY_AGAIN_MESSAGE)
            else:
                
                if (os.path.isdir(user_input) or os.path.isfile(user_input)) :
                    File(user_input).print_information()
                else:
                    print("\n «" + user_input + "» not found ...")

                input(TRY_AGAIN_MESSAGE)      


    def number_2(self):
        while True:
            clear_screen()
            print("\n\t *** Show directory contents ***")
            user_input_path = input("\n plz enter your «Directory»" + \
                                " <or 0 for exit>: ") 
            if user_input_path == "0":
                return
            elif user_input_path == "":
                input(EMPTY_INPUT + TRY_AGAIN_MESSAGE)
            else:
                if (os.path.isdir(user_input_path)):
                    File(user_input_path).print_directory_contents_information()    
                else:
                    print("\n «" + user_input_path + "» isn't directory or not found in current directory ...")

                input(TRY_AGAIN_MESSAGE)


    def number_3(self):
        while True:
            clear_screen()
            print("\n\t *** Search file or directory in directory ***")
            user_input_path = input("\n plz enter your «Directory»" + \
                                " <or 0 for exit>: ") 
            if user_input_path == "0":
                return
            elif user_input_path == "":
                input(EMPTY_INPUT + TRY_AGAIN_MESSAGE)
            else:
                if (os.path.isdir(user_input_path)):
                    user_input_file = input("\n plz enter your «Directory» or «File name(with extension)»" + \
                                " <or 0 for exit>: ") 
                    if user_input_file == "0":
                        return
                    elif user_input_file == "":
                        input(EMPTY_INPUT + TRY_AGAIN_MESSAGE)
                    else:
                        tmp_file_path = os.path.join(user_input_path, user_input_file)
                        if (os.path.isfile(tmp_file_path) or os.path.isdir(tmp_file_path)) :
                            File(tmp_file_path).print_information()
                        else:
                            print("\n «" + user_input_file + "» not found in "
                                  "«" + user_input_path +  "» ...")   
                else:
                    print("\n «" + user_input_path + "» isn't directory or not found in current directory ...")

                input(TRY_AGAIN_MESSAGE)                                              
           
            
    def number_4(self): 
        while True:
            clear_screen()
            print("\n\t *** Rename file or directory in directory and it's sub-directories ***")
            user_input_path = input("\n plz enter your «Directory»" + \
                                " <or 0 for exit>: ") 
            if user_input_path == "0":
                return
            elif user_input_path == "":
                input(EMPTY_INPUT + TRY_AGAIN_MESSAGE)
            else:
                if (os.path.isdir(user_input_path)):
                    
                    user_input_source = input("\n plz enter your source «Directory» or «File name(with extension)»" + \
                                " <or 0 for exit>: ") 
                    if user_input_source == "0":
                        return
                    elif user_input_source == "":
                        input(EMPTY_INPUT + TRY_AGAIN_MESSAGE)
                    else:
                        user_input_destination = input("\n plz enter your destination «Directory» or «File name(with extension)»" + \
                            " <or 0 for exit>: ") 
                        if user_input_destination == "0":
                            return
                        elif user_input_destination == "":
                            input(EMPTY_INPUT + TRY_AGAIN_MESSAGE)
                        else:
                            rename(user_input_path, user_input_source, user_input_destination)
                                
                else:
                    print("\n «" + user_input_path + "» isn't directory or not found in current directory ...")

                input(TRY_AGAIN_MESSAGE)


if __name__ == "__main__":
    s = Switch()
    while True :
        clear_screen()
        print()
        print(PANEL_MESSAGE)
        switch_input = ""
        switch_input = input(SWITCH_MESSAGE)
        if switch_input == "0":
            break
        elif switch_input == "":
                input(EMPTY_INPUT + TRY_AGAIN_MESSAGE)
        else:
            s.select(switch_input)