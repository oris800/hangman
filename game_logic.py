from tkinter import filedialog
import os
import random

class Game:
    
    welcome_message = """     
  _    _                                         
 | |  | |                                        
 | |__| | __ _ _ __   __ _ _ __ ___   __ _ _ __  
 |  __  |/ _` | '_ \ / _` | '_ ` _ \ / _` | '_ \         
 | |  | | (_| | | | | (_| | | | | | | (_| | | | |
 |_|  |_|\__,_|_| |_|\__, |_| |_| |_|\__,_|_| |_|
                      __/ |                      
                     |___/
    by ori sela 2024
    """  


    letter_list = []
    tryies = 7
    word_list_file_path = ""
    
    def __init__(self,secret_word) -> None:
        self.secret_word = secret_word

    def get_user_input(self,input):
        
        if len(input) > 1:
            print("The string you enter is too loooooong")
        elif input.isalpha() == False:
             print("That not a letter!")
        elif input in self.letter_list:
            print("You already guessed that letter")
        else:
            input = input.lower()
            print("Your letter is " + input)
            self.letter_list.append(input)

            if input not in self.secret_word:
                self.tryies -= 1
            if self.tryies > 0:
                self.print_hangman(self.tryies)
    
    def show_hidden_word(self):
        output = ""
        for letter in self.secret_word:
            if letter in self.letter_list:
                 output += letter
            elif letter == "-":
                output += "-"
            else:
                output += "_"
        return output
    
    def chack_for_win(self):
        temp_list = []
        for letter in self.secret_word:
            if letter in self.letter_list:
               temp_list.append(True)
            if letter == "-":
                temp_list.append(True)
        if len(temp_list) == len(self.secret_word):
            return True
        else:
            return False
        
    def print_hangman(self,picture_number):
        hangman_pictures = {
            1: "    x-------x\n",
            2: "    x-------x\n    |\n    |\n    |\n    |\n    |\n",
            3: "    x-------x\n    |       |\n    |       0\n    |\n    |\n    |\n",
            4: "    x-------x\n    |       |\n    |       0\n    |       |\n    |\n    |\n",
            5: "    x-------x\n    |       |\n    |       0\n    |      /|\\\n    |\n    |\n",
            6: "    x-------x\n    |       |\n    |       0\n    |      /|\\\n    |      /\n    |\n",
            7: "    x-------x\n    |       |\n    |       0\n    |      /|\\\n    |      / \\\n    |\n"
        }

        print(hangman_pictures[picture_number])        
    
    def open_filemanager(self):
        user_home = os.path.expanduser("~")
        ask_user = input("Do you want to open filemanager in GUI? [yes - Y] [no - N]: \n")
        if ask_user == "Y" or ask_user == "y":
            file_path =  filedialog.askopenfilename(initialdir=user_home, title="Open text file")
        else:
            file_path = input("Enter a file path: ")
        return file_path


    def choose_word(self,file_path):
        try:
            with open(file_path) as file:
                list_of_words = []
                for line in file:
                    line = line.lower()
                    line = line.replace(" ","-")
                    line = line.rstrip()
                    list_of_words.append(line)
            random_number = random.randint(0,len(list_of_words) -1)
            return list_of_words[random_number]
        except:
            print("(!) Error: You chose an invalid file. You need to choose a .txt file only. Press any key to open anther file ...")
            input()
            self.choose_word(file_path=self.open_filemanager())
    

    def win_prompep(self):
        the_currect_word = self.secret_word.replace("-"," ")
        self.secret_word = ""
        self.letter_list = []
        self.tryies = 7
        print("YOU WON!!!! " + "\n the currect word was: " + the_currect_word)
        self.secret_word = ""
        uinput = input("Would you like to play again?? [yes - Y] [no - N]: \n")
        if uinput == "Y" or uinput == "y":
            input2 = input("Would you like to open new word list? [yes - Y] [no - N]: ")
            if input2 == "Y" or input2 == "y":
                self.secret_word = self.choose_word(file_path=self.open_filemanager())
            elif input2 == "N" or input2 == "n":
                 self.secret_word = self.choose_word(file_path=self.word_list_file_path)

    def lose_prompep(self):
        the_currect_word = self.secret_word.replace("-"," ")
        self.secret_word = ""
        self.letter_list = []
        self.tryies = 7
        print("YOU LOST!!!!" + "\n the currect word was: " + the_currect_word)
        uinput = input("Would you like to play again?? [yes - Y] [no - N]: \n")
        if uinput == "Y" or uinput == "y":
            input2 = input("Would you like to play from new text file? [yes - Y] [no - N]:")
            if input2 == "Y" or input2 == "y":
                self.secret_word = self.choose_word(file_path=self.open_filemanager())
            elif input2 == "N" or input2 == "n":
                 self.secret_word = self.choose_word(file_path=self.word_list_file_path)