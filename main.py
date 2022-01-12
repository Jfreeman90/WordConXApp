import tkinter as tk
from tkinter import messagebox
import time
import numpy as np
#import a dictionary module that will find the defintions of said words
from PyDictionary import PyDictionary
dictionary=PyDictionary()

#generate the grid from the 16 different dice
def get_grid():
    from random import choice
    #Return a dictionary of grid positions to random letters  (y, x)
    global X,Y
    X, Y=4, 4
    """Return a dictionary of grid positions to random letters"""
    dice = {}
    dice['0'] = ['R','I','F','O','B','X']
    dice['1'] = ['I','F','E','H','P','Y']
    dice['2'] = ['D','E','N','O','W','S']
    dice['3'] = ['U','T','O','K','N','D']
    dice['4'] = ['A','M','S','R','O','W']
    dice['5'] = ['L','U','P','E','T','S']
    dice['6'] = ['P','C','I','T','O','A']
    dice['7'] = ['Y','L','G','K','U','E']
    dice['8'] = ['E','H','I','S','P','N']
    dice['9'] = ['Q','B','M','J','O','A']
    dice['10'] = ['V','E','T','I','G','N']
    dice['11'] = ['B','A','L','E','Y','T']
    dice['12'] = ['E','Z','A','V','N','D']
    dice['13'] = ['T','A','L','Y','S','D']
    dice['14'] = ['U','W','I','L','R','G']
    dice['15'] = ['P','A','C','E','M','D']
    spent_dice = []
    #get a random dice from the list
    def get_die():
        found = 0
        thisdie = 0
        while found < 1:
            thisdie = choice(range(0,16))
            if thisdie not in spent_dice:
                found = 1
                spent_dice.append(thisdie)
        return thisdie
    #return anyletter from the options on each dice    
    def get_face(die_number):
        face_label = choice(dice[str(die_number)])
        return face_label
    return {(x, y): get_face(get_die()) for x in range(X) for y in range(Y)}

def roll_grid():
    #reset the player word list and current string to empty
    global player_word_list
    player_word_list=[]
    global current_string
    current_string=[]
    
    #create a time and datre variable that is created upon making a grid and can be saved to data file
    from datetime import datetime
    global dt_string_date, dt_string_time
    # datetime object containing current date and time
    now = datetime.now()
    # dd/mm/YY H:M:S
    dt_string_date = now.strftime("%Y/%m/%d")  
    dt_string_time = now.strftime("%H:%M")        
    #print(dt_string_date)
    #print(dt_string_time)

    #inital grid
    global grid
    grid = get_grid()
    #print(grid)
    #get each part of the grid assigned to an individual variable that can be diplayed and linked to each button
    global grid0,grid1, grid2, grid3, grid4, grid5, grid6, grid7, grid8, grid9, grid10, grid11, grid11, grid12, grid13, grid14, grid15
    grid0=grid[0,0]
    grid1=grid[1,0]
    grid2=grid[2,0]
    grid3=grid[3,0]
    grid4=grid[0,1]
    grid5=grid[1,1]
    grid6=grid[2,1]
    grid7=grid[3,1]
    grid8=grid[0,2]
    grid9=grid[1,2]
    grid10=grid[2,2]
    grid11=grid[3,2]
    grid12=grid[0,3]
    grid13=grid[1,3]
    grid14=grid[2,3]
    grid15=grid[3,3]

    #Print the grid as a readable string to check formatting if necersarry and can be added to datafile
    global gridString
    gridString = ''
    for y in range(4):
        for x in range(4):
            gridString += grid[x, y] + ''
        gridString += '//'
    #print(gridString)
    
    # edit the new grid
    btn_dice0["text"]=str(grid0)
    btn_dice1["text"]=str(grid1)
    btn_dice2["text"]=str(grid2)
    btn_dice3["text"]=str(grid3)
    btn_dice4["text"]=str(grid4)
    btn_dice5["text"]=str(grid5)
    btn_dice6["text"]=str(grid6)
    btn_dice7["text"]=str(grid7)
    btn_dice8["text"]=str(grid8)
    btn_dice9["text"]=str(grid9)
    btn_dice10["text"]=str(grid10)
    btn_dice11["text"]=str(grid11)
    btn_dice12["text"]=str(grid12)
    btn_dice13["text"]=str(grid13)
    btn_dice14["text"]=str(grid14)
    btn_dice15["text"]=str(grid15)
    
    #reset word list
    lbl_new_game["text"]="Letters must be connected by adjacent tiles!\nGoodluck!"
    btn_start["text"]='START!'
    player_word_list=[]
    current_string=[]
    lbl_word_list_title["text"]='Words found so far'
    lbl_word_list["text"]=' '
    lbl_current_word["text"]=' '
    #reset all clicked buttons
    btn_dice0.config(fg=grid_colors[0], bg=grid_colors[1], relief=tk.RAISED, borderwidth=4)
    btn_dice1.config(fg=grid_colors[0], bg=grid_colors[1], relief=tk.RAISED, borderwidth=4)
    btn_dice2.config(fg=grid_colors[0], bg=grid_colors[1], relief=tk.RAISED, borderwidth=4)
    btn_dice3.config(fg=grid_colors[0], bg=grid_colors[1], relief=tk.RAISED, borderwidth=4)
    btn_dice4.config(fg=grid_colors[0], bg=grid_colors[1], relief=tk.RAISED, borderwidth=4)
    btn_dice5.config(fg=grid_colors[0], bg=grid_colors[1], relief=tk.RAISED, borderwidth=4)
    btn_dice6.config(fg=grid_colors[0], bg=grid_colors[1], relief=tk.RAISED, borderwidth=4)
    btn_dice7.config(fg=grid_colors[0], bg=grid_colors[1], relief=tk.RAISED, borderwidth=4)
    btn_dice8.config(fg=grid_colors[0], bg=grid_colors[1], relief=tk.RAISED, borderwidth=4)
    btn_dice9.config(fg=grid_colors[0], bg=grid_colors[1], relief=tk.RAISED, borderwidth=4)
    btn_dice10.config(fg=grid_colors[0], bg=grid_colors[1], relief=tk.RAISED, borderwidth=4)
    btn_dice11.config(fg=grid_colors[0], bg=grid_colors[1], relief=tk.RAISED, borderwidth=4)
    btn_dice12.config(fg=grid_colors[0], bg=grid_colors[1], relief=tk.RAISED, borderwidth=4)
    btn_dice13.config(fg=grid_colors[0], bg=grid_colors[1], relief=tk.RAISED, borderwidth=4)
    btn_dice14.config(fg=grid_colors[0], bg=grid_colors[1], relief=tk.RAISED, borderwidth=4)
    btn_dice15.config(fg=grid_colors[0], bg=grid_colors[1], relief=tk.RAISED, borderwidth=4)
    #reset word_path and timer
    global word_path
    word_path=[0]
    global minute, second, buttons_pressed, user_input, timerCheck
    buttons_pressed=[]
    #reset timer display
    user_input =np.round(minute*60 + second,1)
    timerCheck=False    #turn timer off
    minute=2
    second=30
    mins_box["text"]=minute
    sec_box["text"]=second
    
    #once the game has been initiated run the below to complete the grid
    def get_neighbours():
      #Return a dictionary with all the neighbours surrounding a particular position on the grid
      neighbours = {}
      #for each grid position (y, x) return all of the niehgbouring tiles that can be entered,
      #for example (0,0)  can move to (1, 0), (1, 1), (0, 1)
      for position in grid:
        x, y = position
        positions = [(x - 1, y - 1), (x, y - 1), (x + 1, y - 1), (x + 1, y),
                         (x + 1, y + 1), (x, y + 1), (x - 1, y + 1), (x - 1, y)]
        neighbours[position] = [p for p in positions if 0 <= p[0] < X and 0 <= p[1] < Y]  #filter out ones not needed
      return neighbours

    def get_dictionary():
      #Return a list of uppercase english words, including word stems
      stems, dictionary = set(), set()
      with open('words_all_filtered.txt') as f:  #open the text file to get each word and add to the dictionary of words
        for word in f:
          word = word.strip().upper()
          dictionary.add(word)

          for i in range(len(word)):  #find the stems of each word which can allow for quick checking of following words
            stems.add(word[:i + 1])   #for example egg -> eggs, eggy can be checked fast for each stem
      #print('dict:', dictionary)
      #print('\nstems:',len(stems))
      return dictionary, stems

    def path_to_word(path):
      #Convert a list of grid positions to a word, for each coidinate in grid return the letter at that place
      #print(path)
      return ''.join([grid[p] for p in path])

    def search(path):
      #Recursively search the grid for words
      word = path_to_word(path)
      #print(word)
      #print(path)
      #logging.debug('%s: %s' % (path, word))
      if word not in stems:   #if the grid path not in stems(start of any word) dont check the entire dictionary and skip path
        return
      if word in dictionary:
        paths.append(path)  #add to paths if word is found in the dictionary
      for next_pos in neighbours[path[-1]]: 
        if next_pos not in path:
            search(path + [next_pos])

    def get_words():
      #Search each grid position and return all the words found
      for position in grid:
        search([position])  
      return [path_to_word(p) for p in paths] #return each path found to contain a word as a word and stored
    
    #from all of the above functions get all of the relevent variables ensuring using the correct grid that was
    #generated by the 'new'game button. Buttons main function is to return a message box with all of the end game infomation.
    
    neighbours = get_neighbours() #get all grid combinations
    dictionary, stems = get_dictionary()
    paths = []
    words = get_words()
    global wordset
    wordset = set(words)

#timer button starter here  
def start_timer():
    import math
    global minute, second, user_input, timerCheck
    # setting the default value as 0
    btn_start["text"]='Reset!'
    minute=2
    second=30
    #get the time left
    user_input =np.round(minute*60 + second,1)
    
    #begin timer by setting gateway to true ao that the timer will run
    timerCheck=True
    if timerCheck==False:   
        return
    else:
        while user_input >-0.1 and timerCheck==True:
            mins,secs = np.round(divmod(user_input,60), 1)
            mins=math.floor(mins)   #ensure minutes is kept as a whole number and not decimal
            # store the value up to two decimal places and change the display
            minute=mins
            second=secs
            mins_box["text"]=mins
            sec_box["text"]=secs
            # updating the GUI window 
            window.update()
            time.sleep(0.1)
      
            # if user_input value = 0, then a messagebox pop's up
            if (user_input == 0):
                #run the end game function once the timer hits 0 which resets all displays and variables as well as displaying the users score.
                end_game()
            user_input = np.round(user_input-0.1,1)

#run the scrips and functions to compile a complete list of all words found by the generated grid.
def end_game():
    def get_game_score(player_word_list, wordset):
      #compare words found by player and words found by script
      #global correct_words
      correct_words=0
      #print(player_word_list)
      #print(wordset)
      for word in player_word_list:
        if word in wordset:
          correct_words=correct_words+1
      return correct_words

    def get_correct_words(player_word_list, wordset):
      #compare words found by player and words found by script to return the list of words that are correct
      #global correct_words
      correct_word_list=[]
      for word in player_word_list:
        if word in wordset:
          correct_word_list.append(word)
      return correct_word_list
    
    global wordset, player_word_list, correct_word_list
    #total words found
    totalwords = len(wordset)
    word_answer_list=sorted(list(filter(lambda x: len(x)>2 , wordset)))
    #words that match the dictionary and the players list
    correct_words=get_game_score(player_word_list, word_answer_list)
    #displays the biggest word found by the computer
    biggest_word_found=max(word_answer_list, key=len)
    #work out a percentage score for the user based on grid to scale difficulty of grid.
    percentage_score=np.round((correct_words/totalwords)*100,2)
    
    #get the players words and find out which ones are correct to change formatting of list
    #player wants to know which of their words were correct so this function will find that and change display.
    correct_word_list= get_correct_words(player_word_list, wordset)    
    #display largest possible word
    #reset current word
    lbl_current_word.config(text='Longest possible word '+str(biggest_word_found), font=("Lucida Sans Typewriter", 13, "bold"))

    #change formatting of the list so players can see which words they got correct
    lbl_word_list_title["text"]='Correct words found last game'
    lbl_word_list["text"]=', '.join(correct_word_list)   
    
    global gridString, dt_string_date, dt_string_time
    #store the list of words found within the grid
    words_found_txt=open('wordconx_found_words.txt',"a")
    words_found_txt.write("\n"+str(gridString)+','+' '.join(word_answer_list))
    words_found_txt.close()
    
    #open a text file to append all of the games data
    raw_data=open('wordconx_raw_data.txt',"a")
    raw_data.write("\n"+dt_string_date+','+dt_string_time+','+str(gridString)+','+' '.join(player_word_list)+','+str(correct_words)+','+str(totalwords)+','+str(percentage_score)+','+str(biggest_word_found))
    raw_data.close()
    
    #create a message box pop up that displays all the infomation at the end of the game.
    messagebox.showinfo(title="GAME COMPLETE", message="You found "+ str(correct_words)+" correct words!\nThere were a total of "+str(totalwords)+'\nYour score was ' +str(percentage_score)+'%')
    global minute, second, buttons_pressed, user_input, timerCheck
    buttons_pressed=[]
    #reset timer display
    user_input =np.round(minute*60 + second,1)
    timerCheck=False    #turn timer off
    minute=0
    second=0
    btn_start["text"]='Reset!'
    mins_box["text"]=minute
    sec_box["text"]=second
    
    #reset all other variables aat the end of the game    # edit the new grid to return to starting
    '''btn_dice0["text"]='W'
    btn_dice1["text"]=' '
    btn_dice2["text"]='O'
    btn_dice3["text"]='D'
    btn_dice4["text"]=' '
    btn_dice5["text"]='O'
    btn_dice6["text"]=''
    btn_dice7["text"]=' '
    btn_dice8["text"]='C'
    btn_dice9["text"]=' '
    btn_dice10["text"]='N'
    btn_dice11["text"]=' '
    btn_dice12["text"]=' '
    btn_dice13["text"]=' '
    btn_dice14["text"]=' '
    btn_dice15["text"]='X'''
    
    #reset word list
    lbl_new_game["text"]="Roll Grid and click Start to begin the game\n Find as many words as possible"
    player_word_list=[]
    current_string=[] 
    
    #reset all clicked buttons
    btn_dice0.config(fg=grid_colors[0], bg=grid_colors[1], relief=tk.RAISED, borderwidth=4)
    btn_dice1.config(fg=grid_colors[0], bg=grid_colors[1], relief=tk.RAISED, borderwidth=4)
    btn_dice2.config(fg=grid_colors[0], bg=grid_colors[1], relief=tk.RAISED, borderwidth=4)
    btn_dice3.config(fg=grid_colors[0], bg=grid_colors[1], relief=tk.RAISED, borderwidth=4)
    btn_dice4.config(fg=grid_colors[0], bg=grid_colors[1], relief=tk.RAISED, borderwidth=4)
    btn_dice5.config(fg=grid_colors[0], bg=grid_colors[1], relief=tk.RAISED, borderwidth=4)
    btn_dice6.config(fg=grid_colors[0], bg=grid_colors[1], relief=tk.RAISED, borderwidth=4)
    btn_dice7.config(fg=grid_colors[0], bg=grid_colors[1], relief=tk.RAISED, borderwidth=4)
    btn_dice8.config(fg=grid_colors[0], bg=grid_colors[1], relief=tk.RAISED, borderwidth=4)
    btn_dice9.config(fg=grid_colors[0], bg=grid_colors[1], relief=tk.RAISED, borderwidth=4)
    btn_dice10.config(fg=grid_colors[0], bg=grid_colors[1], relief=tk.RAISED, borderwidth=4)
    btn_dice11.config(fg=grid_colors[0], bg=grid_colors[1], relief=tk.RAISED, borderwidth=4)
    btn_dice12.config(fg=grid_colors[0], bg=grid_colors[1], relief=tk.RAISED, borderwidth=4)
    btn_dice13.config(fg=grid_colors[0], bg=grid_colors[1], relief=tk.RAISED, borderwidth=4)
    btn_dice14.config(fg=grid_colors[0], bg=grid_colors[1], relief=tk.RAISED, borderwidth=4)
    btn_dice15.config(fg=grid_colors[0], bg=grid_colors[1], relief=tk.RAISED, borderwidth=4)
    
    #reset word_path and timer
    global word_path
    word_path=[0]
    #reset all grid values to prevent inputting any extra words by the player
    global grid0,grid1, grid2, grid3, grid4, grid5, grid6, grid7, grid8, grid9, grid10, grid11, grid12, grid13, grid14, grid15
    del grid0,grid1, grid2, grid3, grid4, grid5, grid6, grid7, grid8, grid9, grid10, grid11, grid12, grid13, grid14, grid15

#save current word to the list and update the display
def save_string_button():
    global current_string, word_path, player_word_list, buttons_pressed
    #print('Current string:',current_string)
    #print('Current string:',player_word_list)
    if len(current_string)>2:
        if ''.join(current_string) in player_word_list:
            #check that the current word trying to be saved hasnt already been saved    
            messagebox.showinfo(title="Input error", message="You have already saved this word")
            #remove the previous istance of the word before adding it again later on in function
            player_word_list.remove(''.join(current_string))
        #add the string to the list of words found by player
        player_word_list.append(''.join(current_string))
    else: 
        messagebox.showinfo(title="Input error", message="Words must be at least 3 letters long.")

    current_string=[]   #reset the current string to empty for a new word
    #print('Player word list:', player_word_list)
    lbl_word_list["text"]=', '.join(sorted(player_word_list))   #display the players current words they have found
    lbl_current_word["text"]=' '                        #display a cleared current word
    #reset all clicked buttons
    btn_dice0.config(fg=grid_colors[0], bg=grid_colors[1], relief=tk.RAISED, borderwidth=4)
    btn_dice1.config(fg=grid_colors[0], bg=grid_colors[1], relief=tk.RAISED, borderwidth=4)
    btn_dice2.config(fg=grid_colors[0], bg=grid_colors[1], relief=tk.RAISED, borderwidth=4)
    btn_dice3.config(fg=grid_colors[0], bg=grid_colors[1], relief=tk.RAISED, borderwidth=4)
    btn_dice4.config(fg=grid_colors[0], bg=grid_colors[1], relief=tk.RAISED, borderwidth=4)
    btn_dice5.config(fg=grid_colors[0], bg=grid_colors[1], relief=tk.RAISED, borderwidth=4)
    btn_dice6.config(fg=grid_colors[0], bg=grid_colors[1], relief=tk.RAISED, borderwidth=4)
    btn_dice7.config(fg=grid_colors[0], bg=grid_colors[1], relief=tk.RAISED, borderwidth=4)
    btn_dice8.config(fg=grid_colors[0], bg=grid_colors[1], relief=tk.RAISED, borderwidth=4)
    btn_dice9.config(fg=grid_colors[0], bg=grid_colors[1], relief=tk.RAISED, borderwidth=4)
    btn_dice10.config(fg=grid_colors[0], bg=grid_colors[1], relief=tk.RAISED, borderwidth=4)
    btn_dice11.config(fg=grid_colors[0], bg=grid_colors[1], relief=tk.RAISED, borderwidth=4)
    btn_dice12.config(fg=grid_colors[0], bg=grid_colors[1], relief=tk.RAISED, borderwidth=4)
    btn_dice13.config(fg=grid_colors[0], bg=grid_colors[1], relief=tk.RAISED, borderwidth=4)
    btn_dice14.config(fg=grid_colors[0], bg=grid_colors[1], relief=tk.RAISED, borderwidth=4)
    btn_dice15.config(fg=grid_colors[0], bg=grid_colors[1], relief=tk.RAISED, borderwidth=4)
    #reset word_path
    word_path=[0]
    buttons_pressed=[]

#reset all of the string variables and reset the grid if player wants to remake the word
def clear_string_button():
    global current_string, word_path, buttons_pressed
    current_string=[]   #reset the current string to empty for a new word
    lbl_current_word["text"]=' '                        #display a cleared current word
    #reset all clicked buttons
    btn_dice0.config(fg=grid_colors[0], bg=grid_colors[1], relief=tk.RAISED, borderwidth=4)
    btn_dice1.config(fg=grid_colors[0], bg=grid_colors[1], relief=tk.RAISED, borderwidth=4)
    btn_dice2.config(fg=grid_colors[0], bg=grid_colors[1], relief=tk.RAISED, borderwidth=4)
    btn_dice3.config(fg=grid_colors[0], bg=grid_colors[1], relief=tk.RAISED, borderwidth=4)
    btn_dice4.config(fg=grid_colors[0], bg=grid_colors[1], relief=tk.RAISED, borderwidth=4)
    btn_dice5.config(fg=grid_colors[0], bg=grid_colors[1], relief=tk.RAISED, borderwidth=4)
    btn_dice6.config(fg=grid_colors[0], bg=grid_colors[1], relief=tk.RAISED, borderwidth=4)
    btn_dice7.config(fg=grid_colors[0], bg=grid_colors[1], relief=tk.RAISED, borderwidth=4)
    btn_dice8.config(fg=grid_colors[0], bg=grid_colors[1], relief=tk.RAISED, borderwidth=4)
    btn_dice9.config(fg=grid_colors[0], bg=grid_colors[1], relief=tk.RAISED, borderwidth=4)
    btn_dice10.config(fg=grid_colors[0], bg=grid_colors[1], relief=tk.RAISED, borderwidth=4)
    btn_dice11.config(fg=grid_colors[0], bg=grid_colors[1], relief=tk.RAISED, borderwidth=4)
    btn_dice12.config(fg=grid_colors[0], bg=grid_colors[1], relief=tk.RAISED, borderwidth=4)
    btn_dice13.config(fg=grid_colors[0], bg=grid_colors[1], relief=tk.RAISED, borderwidth=4)
    btn_dice14.config(fg=grid_colors[0], bg=grid_colors[1], relief=tk.RAISED, borderwidth=4)
    btn_dice15.config(fg=grid_colors[0], bg=grid_colors[1], relief=tk.RAISED, borderwidth=4)
    #reset word_path
    word_path=[0]
    buttons_pressed=[]

#allow string to be saved by oressing enter instead of just the button
def enter_pressed(event):
    save_string_button()

#returns true if the letter pressed is a neighbour to the previous click.
def valid_move_check(word_path, current_position):
    #dictionary of all #all corresponding neighbouring tiles of a given tile
    #functions refers to this list to find if a move is valid or not
    neighbours1={(0, 0): [(1, 0), (1, 1), (0, 1)],
          (0, 1): [(0, 0), (1, 0), (1, 1), (1, 2), (0, 2)],
          (0, 2): [(0, 1), (1, 1), (1, 2), (1, 3), (0, 3)],
          (0, 3): [(0, 2), (1, 2), (1, 3)], 
          (1, 0): [(2, 0), (2, 1), (1, 1), (0, 1), (0, 0)],
          (1, 1): [(0, 0), (1, 0), (2, 0), (2, 1), (2, 2), (1, 2), (0, 2), (0, 1)],
          (1, 2): [(0, 1), (1, 1), (2, 1), (2, 2), (2, 3), (1, 3), (0, 3), (0, 2)],
          (1, 3): [(0, 2), (1, 2), (2, 2), (2, 3), (0, 3)],
          (2, 0): [(3, 0), (3, 1), (2, 1), (1, 1), (1, 0)],
          (2, 1): [(1, 0), (2, 0), (3, 0), (3, 1), (3, 2), (2, 2), (1, 2), (1, 1)],
          (2, 2): [(1, 1), (2, 1), (3, 1), (3, 2), (3, 3), (2, 3), (1, 3), (1, 2)],
          (2, 3): [(1, 2), (2, 2), (3, 2), (3, 3), (1, 3)],
          (3, 0): [(3, 1), (2, 1), (2, 0)],
          (3, 1): [(2, 0), (3, 0), (3, 2), (2, 2), (2, 1)],
          (3, 2): [(2, 1), (3, 1), (3, 3), (2, 3), (2, 2)],
          (3, 3): [(2, 2), (3, 2), (2, 3)]}
    #print(buttons_pressed)
    if bool(buttons_pressed) == False: #if grid dice has been clicked and then removed check  here and allow to be re clicked to start word
        return True
    else:
        previous_position=buttons_pressed[-1]   #last entry of buttons pressed is the last button clicked.
        #print(previous_position)
    #print(previous_position)
    if previous_position != 0:
        #print('not first string')
        #this isnt the first letter of a string and perform check
        #if previous position is 0 then this is the first letter pressed in a string so no constraints
        if previous_position in (neighbours1[current_position]):
            return True
        else:
            return False
    else:
        return True

#define all of the button clicks here, each will add the letter displayed to a string that can be saved
def dice0_button_click():
    global position0, word_path, buttons_pressed
    #position of grid button to look up in neighbours dictionary
    position0=(0,0)
    if position0 in buttons_pressed: #button has already been pressed
        messagebox.showinfo(title="Input error", message="You have already pressed this button")
    else:
        #add the button pressed if a valid move and then follow all steps including adjacent button checks
        #check the path is valid before reassigning the current position to word_path
        if valid_move_check(word_path, position0) == True:
            buttons_pressed.append(position0)
            current_string.append(grid0)
            lbl_current_word["text"]='Word: '+''.join(current_string)
            btn_dice0.config(fg=title_colors[0], bg=title_colors[1], relief=tk.SUNKEN, borderwidth=4) 
            word_path=[position0]
        else:
            messagebox.showinfo(title="Input error", message="You can only choose adjacent tiles!")

def dice1_button_click():
    global position1, word_path, buttons_pressed
    #position of grid button to look up in neighbours dictionary
    position1=(1,0)
    if position1 in buttons_pressed: #button has already been pressed
        messagebox.showinfo(title="Input error", message="You have already pressed this button")
    else:  
        #add the button pressed if a valid move and then follow all steps including adjacent button checks    
        #check the path is valid before reassigning the current position to word_path
        #print(valid_move_check(word_path, position1))
        if valid_move_check(word_path, position1) == True:
            buttons_pressed.append(position1)
            current_string.append(grid1)
            lbl_current_word["text"]='Word: '+''.join(current_string)
            btn_dice1.config(fg=title_colors[0], bg=title_colors[1], relief=tk.SUNKEN, borderwidth=4) 
            word_path=[position1]
        else:
            messagebox.showinfo(title="Input error", message="You can only choose adjacent tiles!")
    
def dice2_button_click():
    global position2, word_path, buttons_pressed
    #position of grid button to look up in neighbours dictionary
    position2=(2,0) 
    if position2 in buttons_pressed: #button has already been pressed
        messagebox.showinfo(title="Input error", message="You have already pressed this button")
    else: 
        #add the button pressed if a valid move and then follow all steps including adjacent button checks
        #check the path is valid before reassigning the current position to word_path
        #print(valid_move_check(word_path, position2))
        if valid_move_check(word_path, position2) == True:
            buttons_pressed.append(position2)
            current_string.append(grid2)
            lbl_current_word["text"]='Word: '+''.join(current_string)
            btn_dice2.config(fg=title_colors[0], bg=title_colors[1], relief=tk.SUNKEN, borderwidth=4) 
            word_path=[position2]
        else:
            messagebox.showinfo(title="Input error", message="You can only choose adjacent tiles!")

def dice3_button_click():
    global position3, word_path, buttons_pressed
    #position of grid button to look up in neighbours dictionary
    position3=(3,0)
    if position3 in buttons_pressed: #button has already been pressed
        messagebox.showinfo(title="Input error", message="You have already pressed this button")
    else: 
        #add the button pressed if a valid move and then follow all steps including adjacent button checks      
        #check the path is valid before reassigning the current position to word_path
        #print(valid_move_check(word_path, position3))
        if valid_move_check(word_path, position3) == True:
            buttons_pressed.append(position3)
            current_string.append(grid3)
            lbl_current_word["text"]='Word: '+''.join(current_string)
            btn_dice3.config(fg=title_colors[0], bg=title_colors[1], relief=tk.SUNKEN, borderwidth=4) 
            word_path=[position3]
        else:
            messagebox.showinfo(title="Input error", message="You can only choose adjacent tiles!")

def dice4_button_click():
    global position4, word_path, buttons_pressed
    #position of grid button to look up in neighbours dictionary
    position4=(0,1)
    if position4 in buttons_pressed: #button has already been pressed
        messagebox.showinfo(title="Input error", message="You have already pressed this button")
    else:     
        #add the button pressed if a valid move and then follow all steps including adjacent button checks
        #check the path is valid before reassigning the current position to word_path
        #print(valid_move_check(word_path, position4))
        if valid_move_check(word_path, position4) == True:
            buttons_pressed.append(position4)
            current_string.append(grid4)
            lbl_current_word["text"]='Word: '+''.join(current_string)
            btn_dice4.config(fg=title_colors[0], bg=title_colors[1], relief=tk.SUNKEN, borderwidth=4) 
            word_path=[position4]
        else:
            messagebox.showinfo(title="Input error", message="You can only choose adjacent tiles!")

def dice5_button_click():
    global position5, word_path, buttons_pressed
    #position of grid button to look up in neighbours dictionary
    position5=(1,1)
    if position5 in buttons_pressed: #button has already been pressed
        messagebox.showinfo(title="Input error", message="You have already pressed this button")
    else:
        #add the button pressed if a valid move and then follow all steps including adjacent button checks
        #check the path is valid before reassigning the current position to word_path
        #print(valid_move_check(word_path, position5))
        if valid_move_check(word_path, position5) == True:
            buttons_pressed.append(position5)
            current_string.append(grid5)
            lbl_current_word["text"]='Word: '+''.join(current_string)
            btn_dice5.config(fg=title_colors[0], bg=title_colors[1], relief=tk.SUNKEN, borderwidth=4) 
            word_path=[position5]
        else:
            messagebox.showinfo(title="Input error", message="You can only choose adjacent tiles!")
    
def dice6_button_click():
    global position6, word_path, buttons_pressed
    #position of grid button to look up in neighbours dictionary
    position6=(2,1)
    if position6 in buttons_pressed: #button has already been pressed
        messagebox.showinfo(title="Input error", message="You have already pressed this button")
    else:
        #add the button pressed if a valid move and then follow all steps including adjacent button checks
        #check the path is valid before reassigning the current position to word_path
        #print(valid_move_check(word_path, position6))
        if valid_move_check(word_path, position6) == True:
            buttons_pressed.append(position6)
            current_string.append(grid6)
            lbl_current_word["text"]='Word: '+''.join(current_string)
            btn_dice6.config(fg=title_colors[0], bg=title_colors[1], relief=tk.SUNKEN, borderwidth=4) 
            word_path=[position6]
        else:
            messagebox.showinfo(title="Input error", message="You can only choose adjacent tiles!")

def dice7_button_click():
    global position7, word_path, buttons_pressed
    #position of grid button to look up in neighbours dictionary
    position7=(3,1)
    if position7 in buttons_pressed: #button has already been pressed
        messagebox.showinfo(title="Input error", message="You have already pressed this button")
    else:
        #add the button pressed if a valid move and then follow all steps including adjacent button checks
        #check the path is valid before reassigning the current position to word_path
        #print(valid_move_check(word_path, position7))
        if valid_move_check(word_path, position7) == True:
            buttons_pressed.append(position7)
            current_string.append(grid7)
            lbl_current_word["text"]='Word: '+''.join(current_string)
            btn_dice7.config(fg=title_colors[0], bg=title_colors[1], relief=tk.SUNKEN, borderwidth=4) 
            word_path=[position7]
        else:
            messagebox.showinfo(title="Input error", message="You can only choose adjacent tiles!")

def dice8_button_click():
    global position8, word_path, buttons_pressed
    #position of grid button to look up in neighbours dictionary
    position8=(0,2)
    if position8 in buttons_pressed: #button has already been pressed
        messagebox.showinfo(title="Input error", message="You have already pressed this button")
    else:
        #add the button pressed if a valid move and then follow all steps including adjacent button checks
        #check the path is valid before reassigning the current position to word_path
        #print(valid_move_check(word_path, position8))
        if valid_move_check(word_path, position8) == True:
            buttons_pressed.append(position8)
            current_string.append(grid8)
            lbl_current_word["text"]='Word: '+''.join(current_string)
            btn_dice8.config(fg=title_colors[0], bg=title_colors[1], relief=tk.SUNKEN, borderwidth=4) 
            word_path=[position8]
        else:
            messagebox.showinfo(title="Input error", message="You can only choose adjacent tiles!")

def dice9_button_click():
    global position9, word_path, buttons_pressed
    #position of grid button to look up in neighbours dictionary
    position9=(1,2)
    if position9 in buttons_pressed: #button has already been pressed
        messagebox.showinfo(title="Input error", message="You have already pressed this button")
    else:
        #add the button pressed if a valid move and then follow all steps including adjacent button checks
        #check the path is valid before reassigning the current position to word_path
        #print(valid_move_check(word_path, position9))
        if valid_move_check(word_path, position9) == True:
            buttons_pressed.append(position9)
            current_string.append(grid9)
            lbl_current_word["text"]='Word: '+''.join(current_string)
            btn_dice9.config(fg=title_colors[0], bg=title_colors[1], relief=tk.SUNKEN, borderwidth=4) 
            word_path=[position9]
        else:
            messagebox.showinfo(title="Input error", message="You can only choose adjacent tiles!")
    
def dice10_button_click():
    global position10, word_path, buttons_pressed
    #position of grid button to look up in neighbours dictionary
    position10=(2,2)
    if position10 in buttons_pressed: #button has already been pressed
        messagebox.showinfo(title="Input error", message="You have already pressed this button")
    else:
        #add the button pressed if a valid move and then follow all steps including adjacent button checks
        #check the path is valid before reassigning the current position to word_path
        #print(valid_move_check(word_path, position10))
        if valid_move_check(word_path, position10) == True:
            buttons_pressed.append(position10)
            current_string.append(grid10)
            lbl_current_word["text"]='Word: '+''.join(current_string)
            btn_dice10.config(fg=title_colors[0], bg=title_colors[1], relief=tk.SUNKEN, borderwidth=4) 
            word_path=[position10]
        else:
            messagebox.showinfo(title="Input error", message="You can only choose adjacent tiles!")

def dice11_button_click():
    global position11, word_path, buttons_pressed
    #position of grid button to look up in neighbours dictionary
    position11=(3,2)
    if position11 in buttons_pressed: #button has already been pressed
        messagebox.showinfo(title="Input error", message="You have already pressed this button")
    else:
        #add the button pressed if a valid move and then follow all steps including adjacent button checks
        #check the path is valid before reassigning the current position to word_path
        #print(valid_move_check(word_path, position11))
        if valid_move_check(word_path, position11) == True:
            buttons_pressed.append(position11)
            current_string.append(grid11)
            lbl_current_word["text"]='Word: '+''.join(current_string)
            btn_dice11.config(fg=title_colors[0], bg=title_colors[1], relief=tk.SUNKEN, borderwidth=4) 
            word_path=[position11]
        else:
            messagebox.showinfo(title="Input error", message="You can only choose adjacent tiles!")

def dice12_button_click():
    global position12, word_path, buttons_pressed
    #position of grid button to look up in neighbours dictionary
    position12=(0,3)
    if position12 in buttons_pressed: #button has already been pressed
        messagebox.showinfo(title="Input error", message="You have already pressed this button")
    else:
        #add the button pressed if a valid move and then follow all steps including adjacent button checks
        #check the path is valid before reassigning the current position to word_path
        #print(valid_move_check(word_path, position5))
        if valid_move_check(word_path, position12) == True:
            buttons_pressed.append(position12)
            current_string.append(grid12)
            lbl_current_word["text"]='Word: '+''.join(current_string)
            btn_dice12.config(fg=title_colors[0], bg=title_colors[1], relief=tk.SUNKEN, borderwidth=4) 
            word_path=[position12]
        else:
            messagebox.showinfo(title="Input error", message="You can only choose adjacent tiles!")

def dice13_button_click():
    global position13, word_path, buttons_pressed
    #position of grid button to look up in neighbours dictionary
    position13=(1,3)
    if position13 in buttons_pressed: #button has already been pressed
        messagebox.showinfo(title="Input error", message="You have already pressed this button")
    else:
        #add the button pressed if a valid move and then follow all steps including adjacent button checks
        #check the path is valid before reassigning the current position to word_path
        #print(valid_move_check(word_path, position13))
        if valid_move_check(word_path, position13) == True:
            buttons_pressed.append(position13)
            current_string.append(grid13)
            lbl_current_word["text"]='Word: '+''.join(current_string)
            btn_dice13.config(fg=title_colors[0], bg=title_colors[1], relief=tk.SUNKEN, borderwidth=4) 
            word_path=[position13]
        else:
            messagebox.showinfo(title="Input error", message="You can only choose adjacent tiles!")
    
def dice14_button_click():
    global position14, word_path, buttons_pressed
    #position of grid button to look up in neighbours dictionary
    position14=(2,3)
    if position14 in buttons_pressed: #button has already been pressed
        messagebox.showinfo(title="Input error", message="You have already pressed this button")
    else:
        #add the button pressed if a valid move and then follow all steps including adjacent button checks
        #check the path is valid before reassigning the current position to word_path
        #print(valid_move_check(word_path, position14))
        if valid_move_check(word_path, position14) == True:
            buttons_pressed.append(position14)
            current_string.append(grid14)
            lbl_current_word["text"]='Word: '+''.join(current_string)
            btn_dice14.config(fg=title_colors[0], bg=title_colors[1], relief=tk.SUNKEN, borderwidth=4) 
            word_path=[position14]
        else:
            messagebox.showinfo(title="Input error", message="You can only choose adjacent tiles!")

def dice15_button_click():
    global position15, word_path, buttons_pressed
    #position of grid button to look up in neighbours dictionary
    position15=(3,3)
    if position15 in buttons_pressed: #button has already been pressed
        messagebox.showinfo(title="Input error", message="You have already pressed this button")
    else:
        #add the button pressed if a valid move and then follow all steps including adjacent button checks
        #check the path is valid before reassigning the current position to word_path
        #print(valid_move_check(word_path, position15))
        if valid_move_check(word_path, position15) == True:
            buttons_pressed.append(position15)
            current_string.append(grid15)
            lbl_current_word["text"]='Word: '+''.join(current_string)
            btn_dice15.config(fg=title_colors[0], bg=title_colors[1], relief=tk.SUNKEN, borderwidth=4) 
            word_path=[position15]
        else:
            messagebox.showinfo(title="Input error", message="You can only choose adjacent tiles!") 

#function for each button that allows the button to be clicked to uncheck it, can only be the last letter of the word input
def right_click_dice0(event):
    #check to only delete letter if it was the last one pressed
    if position0 not in word_path:
        messagebox.showinfo(title="Input error", message="You can only delete the last letter!")
    else:
        buttons_pressed.remove(position0)
        word_path.remove(position0)
        #reset the current string
        current_string.remove(grid0)
        lbl_current_word["text"]='Word: '+''.join(current_string)
        #reset the appearence of the button
        btn_dice0.config(relief=tk.RAISED, borderwidth=4, fg=grid_colors[0], bg=grid_colors[1])

def right_click_dice1(event):
    #check to only delete letter if it was the last one pressed
    if position1 not in word_path:
        messagebox.showinfo(title="Input error", message="You can only delete the last letter!")
    else:
        buttons_pressed.remove(position1)
        word_path.remove(position1)
        #reset the current string
        current_string.remove(grid1)
        lbl_current_word["text"]='Word: '+''.join(current_string)
        #reset the appearence of the button
        btn_dice1.config(relief=tk.RAISED, borderwidth=4, fg=grid_colors[0], bg=grid_colors[1])

def right_click_dice2(event):
    #check to only delete letter if it was the last one pressed
    if position2 not in word_path:
        messagebox.showinfo(title="Input error", message="You can only delete the last letter!")
    else:
        buttons_pressed.remove(position2)
        word_path.remove(position2)
        #reset the current string
        current_string.remove(grid2)
        lbl_current_word["text"]='Word: '+''.join(current_string)
        #reset the appearence of the button
        btn_dice2.config(relief=tk.RAISED, borderwidth=4, fg=grid_colors[0], bg=grid_colors[1])

def right_click_dice3(event):
    #check to only delete letter if it was the last one pressed
    if position3 not in word_path:
        messagebox.showinfo(title="Input error", message="You can only delete the last letter!")
    else:
        buttons_pressed.remove(position3)
        word_path.remove(position3)
        #reset the current string
        current_string.remove(grid3)
        lbl_current_word["text"]='Word: '+''.join(current_string)
        #reset the appearence of the button
        btn_dice3.config(relief=tk.RAISED, borderwidth=4, fg=grid_colors[0], bg=grid_colors[1])
        
def right_click_dice4(event):
    #check to only delete letter if it was the last one pressed
    if position4 not in word_path:
        messagebox.showinfo(title="Input error", message="You can only delete the last letter!")
    else:
        buttons_pressed.remove(position4)
        word_path.remove(position4)
        #reset the current string
        current_string.remove(grid4)
        lbl_current_word["text"]='Word: '+''.join(current_string)
        #reset the appearence of the button
        btn_dice4.config(relief=tk.RAISED, borderwidth=4, fg=grid_colors[0], bg=grid_colors[1])
        
def right_click_dice5(event):
    #check to only delete letter if it was the last one pressed
    if position5 not in word_path:
        messagebox.showinfo(title="Input error", message="You can only delete the last letter!")
    else:
        buttons_pressed.remove(position5)
        word_path.remove(position5)
        #reset the current string
        current_string.remove(grid5)
        lbl_current_word["text"]='Word: '+''.join(current_string)
        #reset the appearence of the button
        btn_dice5.config(relief=tk.RAISED, borderwidth=4, fg=grid_colors[0], bg=grid_colors[1])
        
def right_click_dice6(event):
    #check to only delete letter if it was the last one pressed
    if position6 not in word_path:
        messagebox.showinfo(title="Input error", message="You can only delete the last letter!")
    else:
        buttons_pressed.remove(position6)
        word_path.remove(position6)
        #reset the current string
        current_string.remove(grid6)
        lbl_current_word["text"]='Word: '+''.join(current_string)
        #reset the appearence of the button
        btn_dice6.config(relief=tk.RAISED, borderwidth=4, fg=grid_colors[0], bg=grid_colors[1])
        
def right_click_dice7(event):
    #check to only delete letter if it was the last one pressed
    if position7 not in word_path:
        messagebox.showinfo(title="Input error", message="You can only delete the last letter!")
    else:
        buttons_pressed.remove(position7)
        word_path.remove(position7)
        #reset the current string
        current_string.remove(grid7)
        lbl_current_word["text"]='Word: '+''.join(current_string)
        #reset the appearence of the button
        btn_dice7.config(relief=tk.RAISED, borderwidth=4, fg=grid_colors[0], bg=grid_colors[1])       

def right_click_dice8(event):
    #check to only delete letter if it was the last one pressed
    if position8 not in word_path:
        messagebox.showinfo(title="Input error", message="You can only delete the last letter!")
    else:
        buttons_pressed.remove(position8)
        word_path.remove(position8)
        #reset the current string
        current_string.remove(grid8)
        lbl_current_word["text"]='Word: '+''.join(current_string)
        #reset the appearence of the button
        btn_dice8.config(relief=tk.RAISED, borderwidth=4, fg=grid_colors[0], bg=grid_colors[1])

def right_click_dice9(event):
    #check to only delete letter if it was the last one pressed
    if position9 not in word_path:
        messagebox.showinfo(title="Input error", message="You can only delete the last letter!")
    else:
        buttons_pressed.remove(position9)
        word_path.remove(position9)
        #reset the current string
        current_string.remove(grid9)
        lbl_current_word["text"]='Word: '+''.join(current_string)
        #reset the appearence of the button
        btn_dice9.config(relief=tk.RAISED, borderwidth=4, fg=grid_colors[0], bg=grid_colors[1])

def right_click_dice10(event):
    #check to only delete letter if it was the last one pressed
    if position10 not in word_path:
        messagebox.showinfo(title="Input error", message="You can only delete the last letter!")
    else:
        buttons_pressed.remove(position10)
        word_path.remove(position10)
        #reset the current string
        current_string.remove(grid10)
        lbl_current_word["text"]='Word: '+''.join(current_string)
        #reset the appearence of the button
        btn_dice10.config(relief=tk.RAISED, borderwidth=4, fg=grid_colors[0], bg=grid_colors[1])

def right_click_dice11(event):
    #check to only delete letter if it was the last one pressed
    if position11 not in word_path:
        messagebox.showinfo(title="Input error", message="You can only delete the last letter!")
    else:
        buttons_pressed.remove(position11)
        word_path.remove(position11)
        #reset the current string
        current_string.remove(grid11)
        lbl_current_word["text"]='Word: '+''.join(current_string)
        #reset the appearence of the button
        btn_dice11.config(relief=tk.RAISED, borderwidth=4, fg=grid_colors[0], bg=grid_colors[1])

def right_click_dice12(event):
    #check to only delete letter if it was the last one pressed
    if position12 not in word_path:
        messagebox.showinfo(title="Input error", message="You can only delete the last letter!")
    else:
        buttons_pressed.remove(position12)
        word_path.remove(position12)
        #reset the current string
        current_string.remove(grid12)
        lbl_current_word["text"]='Word: '+''.join(current_string)
        #reset the appearence of the button
        btn_dice12.config(relief=tk.RAISED, borderwidth=4, fg=grid_colors[0], bg=grid_colors[1])

def right_click_dice13(event):
    #check to only delete letter if it was the last one pressed
    if position13 not in word_path:
        messagebox.showinfo(title="Input error", message="You can only delete the last letter!")
    else:
        buttons_pressed.remove(position13)
        word_path.remove(position13)
        #reset the current string
        current_string.remove(grid13)
        lbl_current_word["text"]='Word: '+''.join(current_string)
        #reset the appearence of the button
        btn_dice13.config(relief=tk.RAISED, borderwidth=4, fg=grid_colors[0], bg=grid_colors[1])

def right_click_dice14(event):
    #check to only delete letter if it was the last one pressed
    if position14 not in word_path:
        messagebox.showinfo(title="Input error", message="You can only delete the last letter!")
    else:
        buttons_pressed.remove(position14)
        word_path.remove(position14)
        #reset the current string
        current_string.remove(grid14)
        lbl_current_word["text"]='Word: '+''.join(current_string)
        #reset the appearence of the button
        btn_dice14.config(relief=tk.RAISED, borderwidth=4, fg=grid_colors[0], bg=grid_colors[1])

def right_click_dice15(event):
    #check to only delete letter if it was the last one pressed
    if position15 not in word_path:
        messagebox.showinfo(title="Input error", message="You can only delete the last letter!")
    else:
        buttons_pressed.remove(position15)
        word_path.remove(position15)
        #reset the current string
        current_string.remove(grid15)
        lbl_current_word["text"]='Word: '+''.join(current_string)
        #reset the appearence of the button
        btn_dice15.config(relief=tk.RAISED, borderwidth=4, fg=grid_colors[0], bg=grid_colors[1])

#function to reveal the full list of words found to user only if the timer is at 0 so once the game has finished
#this function opens a new window
def check_full_list():
    global minute, second
    #ony run the command if timer =0
        
    def get_definition():
        user_word=(ent_word.get()).upper()
        #print(user_word)
        #clear entry for next guess
        ent_word.delete(0, "end")
        ent_word.insert(0, "")
        #check that a guess word has been input and not mis clicked.
        if user_word not in wordset:
            messagebox.showinfo(title="Input error", message=str(user_word)+" is not in the list of words found." )
        else: 
            #find the definitions and meaning of the word
            definition_user_word=dictionary.meaning(user_word)
            
            #if a definition was found using dictionary display a new window else an error message box
            if bool(definition_user_word)==True:
                #Iterate over key/value pairs in dict and append to corresponding lists to be itterated over and format correctly
                keys=[]
                definitions=[]
                for key, value in definition_user_word.items():
                    keys.append(key)
                    definitions.append(value)
                
                #create a new window pop up with the word definition here
                newWindow2=tk.Toplevel(newWindow)
                newWindow2.title('Definition')
                #create frame to hold new list with correct formatting
                #frame to hold definitions
                frm_new_window_definition=tk.Frame(master=newWindow2, bg=frm_pic_colors[1])
                frm_new_window_definition.grid(row=0, column=0, sticky="ew")
                frm_new_window_definition.grid_rowconfigure(0, weight=1)
                frm_new_window_definition.grid_columnconfigure(0, weight=1)
                
                #label word
                lbl_user_word=tk.Label(frm_new_window_definition, text=user_word, font=("Lucida Sans Typewriter", 14, "bold underline"),
                            fg=frm_pic_colors[0], bg=frm_pic_colors[1])
                lbl_user_word.grid(row=0, column=0)            
                #label word type
                lbl_user_word_type=tk.Label(frm_new_window_definition, text=' ', font=("Lucida Sans Typewriter", 10, "bold"),
                            fg=frm_pic_colors[0], bg=frm_pic_colors[1])
                lbl_user_word_type.grid(row=1, column=0)
                #label definition
                lbl_user_word_definition=tk.Label(frm_new_window_definition, text=' ', font=("Lucida Sans Typewriter", 12),wraplength=350, justify="center",
                            fg=frm_pic_colors[0], bg=frm_pic_colors[1])
                lbl_user_word_definition.grid(row=2, column=0)
                
                #pair each definitons with the type of word it is
                lbl_user_word_type["text"]=keys[0]
                lbl_user_word_definition["text"]=definitions[0][0].upper()
            else:
                #display a message to tell user no message was found
                messagebox.showinfo(title="INPUT ERROR", message="There was no definition found for this word")
            
    #run the same commands as if the button is pressed to get the definition if enter is pressed as well.
    def enter_pressed_get_definition(event):
        get_definition()
        
    if minute==0 and second==0:
        newWindow=tk.Toplevel(window)
        newWindow.title('List of words')
        
        #create frame to hold new list with correct formatting
        #frame to hold buttons to end game/view full list(only if timer is ==0)
        frm_new_window=tk.Frame(master=newWindow, bg=frm_pic_colors[1])
        frm_new_window.grid(row=0, column=0, sticky="ew")
        frm_new_window.grid_rowconfigure(0, weight=1)
        frm_new_window.grid_columnconfigure(0, weight=1)
        
        #label to hold full list of words avaiable
        lbl_title_newwindow=tk.Label(frm_new_window, text ="List of words found inside the grid", font=("Lucida Sans Typewriter", 14, "bold underline"),
                        fg=frm_pic_colors[0], bg=frm_pic_colors[1])
        lbl_title_newwindow.grid(row=0,column=0, padx=(5),pady=(5))
        lbl_word_stats=tk.Label(master=frm_new_window, text='There were a total of  '+str(len(wordset))+' words found.', font=("Lucida Sans Typewriter", 11, "bold")
                        ,fg=frm_pic_colors[0], bg=frm_pic_colors[1])
        lbl_word_stats.grid(row=1, column=0)
        lbl_full_list=tk.Label(master=frm_new_window, text=', '.join(sorted(wordset)), font=("Lucida Sans Typewriter", 11, "bold"),wraplength=350, justify="center"
                        ,fg=frm_pic_colors[0], bg=frm_pic_colors[1])
        lbl_full_list.grid(row=2, column=0)
        lbl_search=tk.Label(master=frm_new_window, text='Search for a word to find definition', font=("Lucida Sans Typewriter", 11, "bold underline"),
                        fg=frm_pic_colors[0], bg=frm_pic_colors[1])
        lbl_search.grid(row=3, column=0)
        #frame to hold the entry box and look up meaning button
        frm_search_meanings=tk.Frame(master=newWindow, bg=frm_pic_colors[1])
        frm_search_meanings.grid(row=1, column=0, sticky="ew")
        frm_search_meanings.grid_rowconfigure(0, weight=1)
        frm_search_meanings.grid_columnconfigure([0,1], weight=1)
        
        #entry for the word to look up that can be typed
        ent_word=tk.Entry(master=frm_search_meanings)
        ent_word.grid(row=0, column=0, pady=(5,5))
        ent_word.bind("<Return>", enter_pressed_get_definition)        #bind ENTER to the entry that will run the same as button pressed
        
        #button to search for the word that is in the entry box
        btn_search_meaning=tk.Button(master=frm_search_meanings, text='Get Definition', font=("Lucida Sans Typewriter", 11), command=get_definition)
        btn_search_meaning.grid(row=0, column=1, pady=(5,5))
    else:
        #create a message box pop up that displays all the infomation at the end of the game.
        messagebox.showinfo(title="INPUT ERROR", message="Can only reveal list once game has ended and timer hits 0.")



#GLOBAL VARIABLES to store strings and word list as well as word path
global player_word_list
player_word_list=[]
global current_string
current_string=[]
global word_path
word_path=[0]
global buttons_pressed
buttons_pressed=[]
    
    

#------------------ALL OF THE BELOW IS FORMATING FOR THE GUI AND ITS DISPLAYS---------------------------
# Create instance
window = tk.Tk()
# Disable resizing the GUI
window.resizable(0,1)  #(x,y)
# Add a title
title_colors=["#FFA500","#006400"]
frm_pic_colors=["#191970", "#8FBC8B"]   #TEXT AND BACKGROUND COLOURS
grid_colors=["#F8F8FF", "#3CB371"]      #text and background for grid of letters
btn_colors=["#F8F8FF", "#4169E1"]       #text and background for buttons
window.title("BOGGLE - APP (jlf)")

#LABEL - Choose the words difficulty
lbl_title=tk.Label(master=window, 
                text="    WORD CONX    ", font=("Minion Pro Med", 30,  "bold italic"), foreground=title_colors[0], background=title_colors[1])
lbl_title.grid(row=0, column=0, sticky="ew")

#FRAME TO HOLD NEW GAME BUTTONS
frm_new_game_button=tk.Frame(background=frm_pic_colors[1])
frm_new_game_button.grid(row=1, column=0, sticky="ew")
frm_new_game_button.grid_rowconfigure(0, weight=1)
frm_new_game_button.grid_columnconfigure(0, weight=1)

#NEW GAME BUTTON
lbl_new_game=tk.Label(master=frm_new_game_button, text='Roll Grid and click Start to begin the game\n Find as many words as possible',
                        font=("Minion Pro Med", 11, "bold"),background=frm_pic_colors[1])
lbl_new_game.grid(row=0, column=0)

#NEW GAME BUTTON
btn_new_game=tk.Button(master=frm_new_game_button, text='Roll Grid!', font=("Lucida Sans Typewriter", 12), command=roll_grid)
btn_new_game.grid(row=1, column=0, padx=15, pady=10)

#FRAME TO HOLD TIMER
frm_timer=tk.Frame(background=frm_pic_colors[1])
frm_timer.grid(row=2, column=0, sticky="ew")
frm_timer.grid_rowconfigure(0, weight=1)

#TIMER DISPLAY
minute=2
second=30
timer_box = tk.Label(master=frm_timer,background=frm_pic_colors[1],font=("Lucida Sans Typewriter", 12, "bold"),	text='TIME LEFT:')
timer_box.grid(row=0,column=0, padx=(20,5),pady=(5))

mins_box = tk.Label(master=frm_timer,width=2, font=("Arial",18),text=minute, relief=tk.SUNKEN, borderwidth=2)
mins_box.grid(row=0,column=1, pady=5)
  
sec_box = tk.Label(master=frm_timer, width=4, font=("Arial",18),text=second, relief=tk.SUNKEN, borderwidth=2)
sec_box.grid(row=0,column=2, pady=5)

btn_start = tk.Button(master=frm_timer,	text='START!', font=("Lucida Sans Typewriter", 12), command=start_timer)
btn_start.grid(row=0,column=3, padx=15, pady=5)

#frame to display some space between the tiemr and the grid
frm_buffer=tk.Frame(master=window, bg=frm_pic_colors[1])
frm_buffer.grid(row=3, column=0, sticky="ew")
#lbl_buffer=tk.Label(master=frm_buffer, text=' ', font=("Lucida Sans Typewriter", 12), background=frm_pic_colors[1])
#lbl_buffer.grid(row=0, column=0)

#frame to display the current grid as a group of buttons
frm_grid=tk.Frame(master=window, bg=frm_pic_colors[1])
frm_grid.grid(row=4, column=0, sticky="ew")
frm_grid.grid_rowconfigure(0, weight=1)
frm_grid.grid_columnconfigure([0,1,2,3],weight=1)

#16 buttons inside of this frame.
pixelVirtual = tk.PhotoImage(width=1, height=1) #one pixel image that the button wil resize based off of instead of text
grid_dim_pix=[40, 40]   #[y, x] pixel dimensions for each grid button
grid_font=("Minion Pro Med", 20,  "bold")
btn_dice0=tk.Button(frm_grid, text='W', font=grid_font, relief=tk.RAISED, borderwidth=4, fg=grid_colors[0], bg=grid_colors[1],
                    image=pixelVirtual, height=grid_dim_pix[0], width=grid_dim_pix[1], compound="center", command=dice0_button_click)
btn_dice0.grid(row=0, column=0, padx=(60, 2), pady=(10,2))
btn_dice0.bind("<Button-3>", right_click_dice0)        #bind right click to the dice

btn_dice1=tk.Button(frm_grid, text=' ', font=grid_font, relief=tk.RAISED, borderwidth=4, fg=grid_colors[0], bg=grid_colors[1],
                    image=pixelVirtual, height=grid_dim_pix[0], width=grid_dim_pix[1], compound="center", command=dice1_button_click)
btn_dice1.grid(row=0, column=1, padx=2, pady=(10,2))
btn_dice1.bind("<Button-3>", right_click_dice1)        #bind right click to the dice

btn_dice2=tk.Button(frm_grid, text='R', font=grid_font, relief=tk.RAISED, borderwidth=4, fg=grid_colors[0], bg=grid_colors[1], 
                    image=pixelVirtual, height=grid_dim_pix[0], width=grid_dim_pix[1], compound="center", command=dice2_button_click)
btn_dice2.grid(row=0, column=2, padx=2, pady=(10,2))
btn_dice2.bind("<Button-3>", right_click_dice2)        #bind right click to the dice

btn_dice3=tk.Button(frm_grid, text='D', font=grid_font, relief=tk.RAISED, borderwidth=4, fg=grid_colors[0], bg=grid_colors[1], 
                    image=pixelVirtual, height=grid_dim_pix[0], width=grid_dim_pix[1], compound="center", command=dice3_button_click)
btn_dice3.grid(row=0, column=3, padx=(2, 60), pady=(10,2))
btn_dice3.bind("<Button-3>", right_click_dice3)        #bind right click to the dice

btn_dice4=tk.Button(frm_grid, text=' ', font=grid_font, relief=tk.RAISED, borderwidth=4, fg=grid_colors[0], bg=grid_colors[1], 
                    image=pixelVirtual, height=grid_dim_pix[0], width=grid_dim_pix[1], compound="center", command=dice4_button_click)
btn_dice4.grid(row=1, column=0, padx=(60, 2), pady=2)
btn_dice4.bind("<Button-3>", right_click_dice4)        #bind right click to the dice

btn_dice5=tk.Button(frm_grid, text='O', font=grid_font, relief=tk.RAISED, borderwidth=4, fg=grid_colors[0], bg=grid_colors[1], 
                    image=pixelVirtual, height=grid_dim_pix[0], width=grid_dim_pix[1], compound="center", command=dice5_button_click)
btn_dice5.grid(row=1, column=1, padx=2, pady=2)
btn_dice5.bind("<Button-3>", right_click_dice5)        #bind right click to the dice

btn_dice6=tk.Button(frm_grid, text=' ', font=grid_font, relief=tk.RAISED, borderwidth=4, fg=grid_colors[0], bg=grid_colors[1], 
                    image=pixelVirtual, height=grid_dim_pix[0], width=grid_dim_pix[1], compound="center", command=dice6_button_click)
btn_dice6.grid(row=1, column=2, padx=2, pady=2)
btn_dice6.bind("<Button-3>", right_click_dice6)        #bind right click to the dice

btn_dice7=tk.Button(frm_grid, text=' ', font=grid_font, relief=tk.RAISED, borderwidth=4, fg=grid_colors[0], bg=grid_colors[1], 
                    image=pixelVirtual, height=grid_dim_pix[0], width=grid_dim_pix[1], compound="center", command=dice7_button_click)
btn_dice7.grid(row=1, column=3, padx=(2, 60), pady=2)
btn_dice7.bind("<Button-3>", right_click_dice7)        #bind right click to the dice

btn_dice8=tk.Button(frm_grid, text='C', font=grid_font, relief=tk.RAISED, borderwidth=4, fg=grid_colors[0], bg=grid_colors[1], 
                    image=pixelVirtual, height=grid_dim_pix[0], width=grid_dim_pix[1], compound="center", command=dice8_button_click)
btn_dice8.grid(row=2, column=0, padx=(60, 2), pady=2)
btn_dice8.bind("<Button-3>", right_click_dice8)        #bind right click to the dice

btn_dice9=tk.Button(frm_grid, text=' ', font=grid_font, relief=tk.RAISED, borderwidth=4, fg=grid_colors[0], bg=grid_colors[1], 
                    image=pixelVirtual, height=grid_dim_pix[0], width=grid_dim_pix[1], compound="center", command=dice9_button_click)
btn_dice9.grid(row=2, column=1, padx=2, pady=2)
btn_dice9.bind("<Button-3>", right_click_dice9)        #bind right click to the dice

btn_dice10=tk.Button(frm_grid, text='N', font=grid_font, relief=tk.RAISED, borderwidth=4, fg=grid_colors[0], bg=grid_colors[1], 
                    image=pixelVirtual, height=grid_dim_pix[0], width=grid_dim_pix[1], compound="center", command=dice10_button_click)
btn_dice10.grid(row=2, column=2, padx=2, pady=2)
btn_dice10.bind("<Button-3>", right_click_dice10)        #bind right click to the dice

btn_dice11=tk.Button(frm_grid, text=' ', font=grid_font, relief=tk.RAISED, borderwidth=4, fg=grid_colors[0], bg=grid_colors[1], 
                    image=pixelVirtual, height=grid_dim_pix[0], width=grid_dim_pix[1], compound="center", command=dice11_button_click)
btn_dice11.grid(row=2, column=3, padx=(2, 60), pady=2)
btn_dice11.bind("<Button-3>", right_click_dice11)        #bind right click to the dice

btn_dice12=tk.Button(frm_grid, text=' ', font=grid_font, relief=tk.RAISED, borderwidth=4, fg=grid_colors[0], bg=grid_colors[1], 
                    image=pixelVirtual, height=grid_dim_pix[0], width=grid_dim_pix[1], compound="center", command=dice12_button_click)
btn_dice12.grid(row=3, column=0, padx=(60, 2), pady=(2,10))
btn_dice12.bind("<Button-3>", right_click_dice12)        #bind right click to the dice

btn_dice13=tk.Button(frm_grid, text=' ', font=grid_font, relief=tk.RAISED, borderwidth=4, fg=grid_colors[0], bg=grid_colors[1], 
                    image=pixelVirtual, height=grid_dim_pix[0], width=grid_dim_pix[1], compound="center", command=dice13_button_click)
btn_dice13.grid(row=3, column=1, padx=2, pady=(2,10))
btn_dice13.bind("<Button-3>", right_click_dice13)        #bind right click to the dice

btn_dice14=tk.Button(frm_grid, text=' ', font=grid_font, relief=tk.RAISED, borderwidth=4, fg=grid_colors[0], bg=grid_colors[1], 
                    image=pixelVirtual, height=grid_dim_pix[0], width=grid_dim_pix[1], compound="center", command=dice14_button_click)
btn_dice14.grid(row=3, column=2, padx=2, pady=(2,10))
btn_dice14.bind("<Button-3>", right_click_dice14)        #bind right click to the dice

btn_dice15=tk.Button(frm_grid, text='X', font=grid_font, relief=tk.RAISED, borderwidth=4, fg=grid_colors[0], bg=grid_colors[1], 
                    image=pixelVirtual, height=grid_dim_pix[0], width=grid_dim_pix[1], compound="center", command=dice15_button_click)
btn_dice15.grid(row=3, column=3, padx=(2, 60), pady=(2,10))
btn_dice15.bind("<Button-3>", right_click_dice15)        #bind right click to the dice

frm_grid.bind("<Return>", enter_pressed)        #bind a key which will be numbers to the canvas with a command to draw the number on the canvas
frm_grid.focus_set() #set focus of canvas here so when a key is pressed it can be used

#frame to hold all of the words found by the player so far.
frm_words_found=tk.Frame(master=window, bg=frm_pic_colors[1])
frm_words_found.grid(row=5, column=0, sticky="ew")
frm_words_found.grid_rowconfigure(0, weight=1)
frm_words_found.grid_columnconfigure(0, weight=1)

#label to hold the words found by user so far
lbl_current_word=tk.Label(master=frm_words_found,text='', font=("Lucida Sans Typewriter", 18, "bold"),
                        fg=frm_pic_colors[0], bg=frm_pic_colors[1])
lbl_current_word.grid(row=0, column=0)

lbl_word_list_title=tk.Label(master=frm_words_found,text='Words found so far', font=("Lucida Sans Typewriter", 14, "bold underline"),
                        fg=frm_pic_colors[0], bg=frm_pic_colors[1])
lbl_word_list_title.grid(row=1, column=0)

lbl_word_list=tk.Label(master=frm_words_found,text='WORD \nCONX \nDRONX', font=("Lucida Sans Typewriter", 11, "bold"),wraplength=320, justify="center"
                        ,fg=frm_pic_colors[0], bg=frm_pic_colors[1])
lbl_word_list.grid(row=2, column=0)

#frame to hold buttons to save/clear word
frm_save_words=tk.Frame(master=window, bg=frm_pic_colors[1])
frm_save_words.grid(row=6, column=0, sticky="ew")
frm_save_words.grid_rowconfigure(0, weight=1)
frm_save_words.grid_columnconfigure([0,1], weight=1)

#click to add the word you have found from the grid to the list of words found in total
save_btn=tk.Button(master=frm_save_words, text='SAVE WORD!', font=("Lucida Sans Typewriter", 12), command=save_string_button)
save_btn.grid(row=0, column=0, padx=5, pady=5)

#button that will clear the current string incase of mistake
clear_btn=tk.Button(master=frm_save_words, text='Clear Word', font=("Lucida Sans Typewriter", 10), command=clear_string_button)
clear_btn.grid(row=0, column=1, padx=(5,17), pady=5)

#frame to hold buttons to end game/view full list(only if timer is ==0)
frm_end_game=tk.Frame(master=window, bg=frm_pic_colors[1])
frm_end_game.grid(row=7, column=0, sticky="ew")
frm_end_game.grid_rowconfigure(0, weight=1)
frm_end_game.grid_columnconfigure([0,1], weight=1)

#button that will end the game and check for how many words could be found and how many the user found and display a score
check_btn=tk.Button(master=frm_end_game, text='End Game', font=("Lucida Sans Typewriter", 10), command=end_game)
check_btn.grid(row=5, column=0, padx=(14,5), pady=5)

#button that will end the game and check for how many words could be found and how many the user found and display a score
check_list_btn=tk.Button(master=frm_end_game, text='Check List', font=("Lucida Sans Typewriter", 10), command=check_full_list)
check_list_btn.grid(row=5, column=1, padx=5, pady=5)

# Run the application
window.mainloop()
