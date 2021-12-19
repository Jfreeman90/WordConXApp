import tkinter as tk
from tkinter import messagebox
import time
import numpy as np
#ACTUAL CODE HERE
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
    player_word_list=[]
    current_string=[]
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

#timer button starter here  
def start_timer():
    global minute, second, user_input, timerCheck
    # setting the default value as 0
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
                messagebox.showinfo(title="TIME UP", message="You have ran out of time")
                minute=2
                second=30
                #user_input = minute*60 + second
                #mins,secs = np.round(divmod(user_input,60), 1)
                mins_box["text"]='2'
                sec_box["text"]='30'
                # decresing the value of time
            user_input = np.round(user_input-0.1,1)
        
#GLOBAL VARIABLES to store strings and word list as well as word path
global player_word_list
player_word_list=[]
global current_string
current_string=[]
global word_path
word_path=[0]
global buttons_pressed
buttons_pressed=[]

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
    lbl_word_list["text"]=', '.join(player_word_list)   #display the players current words they have found
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
    #print(word_path)
    previous_position=word_path[0]
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
        buttons_pressed.append(position0)
        #check the path is valid before reassigning the current position to word_path
        #print(valid_move_check(word_path, position0))
        if valid_move_check(word_path, position0) == True:
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
        buttons_pressed.append(position1)
        #check the path is valid before reassigning the current position to word_path
        #print(valid_move_check(word_path, position1))
        if valid_move_check(word_path, position1) == True:
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
        buttons_pressed.append(position2)
        #check the path is valid before reassigning the current position to word_path
        #print(valid_move_check(word_path, position2))
        if valid_move_check(word_path, position2) == True:
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
        buttons_pressed.append(position3)
        #check the path is valid before reassigning the current position to word_path
        #print(valid_move_check(word_path, position3))
        if valid_move_check(word_path, position3) == True:
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
        buttons_pressed.append(position4)
        #check the path is valid before reassigning the current position to word_path
        #print(valid_move_check(word_path, position4))
        if valid_move_check(word_path, position4) == True:
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
        buttons_pressed.append(position5)
        #check the path is valid before reassigning the current position to word_path
        #print(valid_move_check(word_path, position5))
        if valid_move_check(word_path, position5) == True:
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
        buttons_pressed.append(position6)
        #check the path is valid before reassigning the current position to word_path
        #print(valid_move_check(word_path, position6))
        if valid_move_check(word_path, position6) == True:
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
        buttons_pressed.append(position7)
        #check the path is valid before reassigning the current position to word_path
        #print(valid_move_check(word_path, position7))
        if valid_move_check(word_path, position7) == True:
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
        buttons_pressed.append(position8)
        #check the path is valid before reassigning the current position to word_path
        #print(valid_move_check(word_path, position8))
        if valid_move_check(word_path, position8) == True:
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
        buttons_pressed.append(position9)
        #check the path is valid before reassigning the current position to word_path
        #print(valid_move_check(word_path, position9))
        if valid_move_check(word_path, position9) == True:
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
        buttons_pressed.append(position10)
        #check the path is valid before reassigning the current position to word_path
        #print(valid_move_check(word_path, position10))
        if valid_move_check(word_path, position10) == True:
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
        buttons_pressed.append(position11)
        #check the path is valid before reassigning the current position to word_path
        #print(valid_move_check(word_path, position11))
        if valid_move_check(word_path, position11) == True:
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
        buttons_pressed.append(position12)
        #check the path is valid before reassigning the current position to word_path
        #print(valid_move_check(word_path, position5))
        if valid_move_check(word_path, position12) == True:
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
        buttons_pressed.append(position13)
        #check the path is valid before reassigning the current position to word_path
        #print(valid_move_check(word_path, position13))
        if valid_move_check(word_path, position13) == True:
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
        buttons_pressed.append(position14)
        #check the path is valid before reassigning the current position to word_path
        #print(valid_move_check(word_path, position14))
        if valid_move_check(word_path, position14) == True:
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
        buttons_pressed.append(position15)
        #check the path is valid before reassigning the current position to word_path
        #print(valid_move_check(word_path, position15))
        if valid_move_check(word_path, position15) == True:
            current_string.append(grid15)
            lbl_current_word["text"]='Word: '+''.join(current_string)
            btn_dice15.config(fg=title_colors[0], bg=title_colors[1], relief=tk.SUNKEN, borderwidth=4) 
            word_path=[position15]
        else:
            messagebox.showinfo(title="Input error", message="You can only choose adjacent tiles!") 

#run the scrips and functions to compile a complete list of all words found by the generated grid.
def check_words_found():
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

    def get_game_score(player_word_list, wordset):
      #compare words found by player and words found by script
      global correct_words
      correct_words=0
      #print(player_word_list)
      #print(wordset)
      for word in player_word_list:
        if word in wordset:
          correct_words=correct_words+1
      return correct_words
    
    #from all of the above functions get all of the relevent variables ensuring using the correct grid that was
    #generated by the 'new'game button. Buttons main function is to return a message box with all of the end game infomation.
    neighbours = get_neighbours() #get all grid combinations
    dictionary, stems = get_dictionary()
    paths = []
    words = get_words()
    wordset = set(words)
    #total words found
    totalwords = len(wordset)
    word_answer_list=sorted(list(filter(lambda x: len(x)>2 , wordset)))
    #words that match the dictionary and the players list
    correct_words=get_game_score(player_word_list, word_answer_list)
    #displays the biggest word found by the computer
    biggest_word_found=max(word_answer_list, key=len)
    
    global gridString, dt_string_date, dt_string_time
    #store the list of words found within the grid
    words_found_txt=open('wordconx_found_words.txt',"a")
    words_found_txt.write("\n"+str(gridString)+','+' '.join(word_answer_list))
    words_found_txt.close()
    
    #open a text file to append all of the games data
    raw_data=open('wordconx_raw_data.txt',"a")
    raw_data.write("\n"+dt_string_date+','+dt_string_time+','+str(gridString)+','+' '.join(player_word_list)+','+str(correct_words)+','+str(totalwords)+','+str(biggest_word_found))
    raw_data.close()
    
    #create a message box pop up that displays all the infomation at the end of the game.
    messagebox.showinfo(title="GAME COMPLETE", message="You found "+ str(correct_words)+" correct words!\nThere were a total of "+str(totalwords)+" words. The longest one was "+str(biggest_word_found))
    
#ALL OF THE BELOW IS FORMATING FOR THE GUI AND ITS DISPLAYS
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
                text="    WORD CONX    ",
                font=("Minion Pro Med", 30,  "bold italic"), 
                foreground=title_colors[0],  
                background=title_colors[1]
)
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


#TIMER LAY OUT HERE
# setting the default value as 0
minute=2
second=30

timer_box = tk.Label(master=frm_timer,
    background=frm_pic_colors[1],
	font=("Lucida Sans Typewriter", 12, "bold"),
	text='TIME LEFT:')
timer_box.grid(row=0,column=0, padx=(20,5),pady=(5))

mins_box = tk.Label(master=frm_timer,
	width=3, 
	font=("Arial",18),
	text=minute, relief=tk.SUNKEN, borderwidth=2)
mins_box.grid(row=0,column=1, pady=5)
  
sec_box = tk.Label(master=frm_timer,
	width=3, 
	font=("Arial",18),
	text=second, relief=tk.SUNKEN, borderwidth=2)
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
btn_dice1=tk.Button(frm_grid, text=' ', font=grid_font, relief=tk.RAISED, borderwidth=4, fg=grid_colors[0], bg=grid_colors[1],
                    image=pixelVirtual, height=grid_dim_pix[0], width=grid_dim_pix[1], compound="center", command=dice1_button_click)
btn_dice1.grid(row=0, column=1, padx=2, pady=(10,2))
btn_dice2=tk.Button(frm_grid, text='R', font=grid_font, relief=tk.RAISED, borderwidth=4, fg=grid_colors[0], bg=grid_colors[1], 
                    image=pixelVirtual, height=grid_dim_pix[0], width=grid_dim_pix[1], compound="center", command=dice2_button_click)
btn_dice2.grid(row=0, column=2, padx=2, pady=(10,2))
btn_dice3=tk.Button(frm_grid, text='D', font=grid_font, relief=tk.RAISED, borderwidth=4, fg=grid_colors[0], bg=grid_colors[1], 
                    image=pixelVirtual, height=grid_dim_pix[0], width=grid_dim_pix[1], compound="center", command=dice3_button_click)
btn_dice3.grid(row=0, column=3, padx=(2, 60), pady=(10,2))
btn_dice4=tk.Button(frm_grid, text=' ', font=grid_font, relief=tk.RAISED, borderwidth=4, fg=grid_colors[0], bg=grid_colors[1], 
                    image=pixelVirtual, height=grid_dim_pix[0], width=grid_dim_pix[1], compound="center", command=dice4_button_click)
btn_dice4.grid(row=1, column=0, padx=(60, 2), pady=2)
btn_dice5=tk.Button(frm_grid, text='O', font=grid_font, relief=tk.RAISED, borderwidth=4, fg=grid_colors[0], bg=grid_colors[1], 
                    image=pixelVirtual, height=grid_dim_pix[0], width=grid_dim_pix[1], compound="center", command=dice5_button_click)
btn_dice5.grid(row=1, column=1, padx=2, pady=2)
btn_dice6=tk.Button(frm_grid, text=' ', font=grid_font, relief=tk.RAISED, borderwidth=4, fg=grid_colors[0], bg=grid_colors[1], 
                    image=pixelVirtual, height=grid_dim_pix[0], width=grid_dim_pix[1], compound="center", command=dice6_button_click)
btn_dice6.grid(row=1, column=2, padx=2, pady=2)
btn_dice7=tk.Button(frm_grid, text=' ', font=grid_font, relief=tk.RAISED, borderwidth=4, fg=grid_colors[0], bg=grid_colors[1], 
                    image=pixelVirtual, height=grid_dim_pix[0], width=grid_dim_pix[1], compound="center", command=dice7_button_click)
btn_dice7.grid(row=1, column=3, padx=(2, 60), pady=2)
btn_dice8=tk.Button(frm_grid, text='C', font=grid_font, relief=tk.RAISED, borderwidth=4, fg=grid_colors[0], bg=grid_colors[1], 
                    image=pixelVirtual, height=grid_dim_pix[0], width=grid_dim_pix[1], compound="center", command=dice8_button_click)
btn_dice8.grid(row=2, column=0, padx=(60, 2), pady=2)
btn_dice9=tk.Button(frm_grid, text=' ', font=grid_font, relief=tk.RAISED, borderwidth=4, fg=grid_colors[0], bg=grid_colors[1], 
                    image=pixelVirtual, height=grid_dim_pix[0], width=grid_dim_pix[1], compound="center", command=dice9_button_click)
btn_dice9.grid(row=2, column=1, padx=2, pady=2)
btn_dice10=tk.Button(frm_grid, text='N', font=grid_font, relief=tk.RAISED, borderwidth=4, fg=grid_colors[0], bg=grid_colors[1], 
                    image=pixelVirtual, height=grid_dim_pix[0], width=grid_dim_pix[1], compound="center", command=dice10_button_click)
btn_dice10.grid(row=2, column=2, padx=2, pady=2)
btn_dice11=tk.Button(frm_grid, text=' ', font=grid_font, relief=tk.RAISED, borderwidth=4, fg=grid_colors[0], bg=grid_colors[1], 
                    image=pixelVirtual, height=grid_dim_pix[0], width=grid_dim_pix[1], compound="center", command=dice11_button_click)
btn_dice11.grid(row=2, column=3, padx=(2, 60), pady=2)
btn_dice12=tk.Button(frm_grid, text=' ', font=grid_font, relief=tk.RAISED, borderwidth=4, fg=grid_colors[0], bg=grid_colors[1], 
                    image=pixelVirtual, height=grid_dim_pix[0], width=grid_dim_pix[1], compound="center", command=dice12_button_click)
btn_dice12.grid(row=3, column=0, padx=(60, 2), pady=(2,10))
btn_dice13=tk.Button(frm_grid, text=' ', font=grid_font, relief=tk.RAISED, borderwidth=4, fg=grid_colors[0], bg=grid_colors[1], 
                    image=pixelVirtual, height=grid_dim_pix[0], width=grid_dim_pix[1], compound="center", command=dice13_button_click)
btn_dice13.grid(row=3, column=1, padx=2, pady=(2,10))
btn_dice14=tk.Button(frm_grid, text=' ', font=grid_font, relief=tk.RAISED, borderwidth=4, fg=grid_colors[0], bg=grid_colors[1], 
                    image=pixelVirtual, height=grid_dim_pix[0], width=grid_dim_pix[1], compound="center", command=dice14_button_click)
btn_dice14.grid(row=3, column=2, padx=2, pady=(2,10))
btn_dice15=tk.Button(frm_grid, text='X', font=grid_font, relief=tk.RAISED, borderwidth=4, fg=grid_colors[0], bg=grid_colors[1], 
                    image=pixelVirtual, height=grid_dim_pix[0], width=grid_dim_pix[1], compound="center", command=dice15_button_click)
btn_dice15.grid(row=3, column=3, padx=(2, 60), pady=(2,10))

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

#click to add the word you have found from the grid to the list of words found in total
save_btn=tk.Button(master=frm_words_found, text='SAVE WORD!', font=("Lucida Sans Typewriter", 12), command=save_string_button)
save_btn.grid(row=3, column=0, padx=15, pady=10)

#button that will clear the current string incase of mistake
clear_btn=tk.Button(master=frm_words_found, text='Delete Word', font=("Lucida Sans Typewriter", 10), command=clear_string_button)
clear_btn.grid(row=4, column=0, padx=15, pady=4)

#button that will end the game and check for how many words could be found and how many the user found and display a score
check_btn=tk.Button(master=frm_words_found, text='Check List', font=("Lucida Sans Typewriter", 10), command=check_words_found)
check_btn.grid(row=5, column=0, padx=15, pady=10)

# Run the application
window.mainloop()
