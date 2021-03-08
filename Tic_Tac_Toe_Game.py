#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import random

"""
Created on 08-03-2021

@author: Anish

"""


""" TIC-TAC-TOE Game """

# funtion to print thr board of tic-tac game

def display_board(board):
    print("\n"*10) #Clears the screen by printing 100 new lines

    # board is a list having 'O' and 'X'

    print('   |   |')
    print(' ' + board[7] + ' | ' + board[8] + ' | ' + board[9])
    print('   |   |')
    print('-----------')
    print('   |   |')
    print(' ' + board[4] + ' | ' + board[5] + ' | ' + board[6])
    print('   |   |')
    print('-----------')
    print('   |   |')
    print(' ' + board[1] + ' | ' + board[2] + ' | ' + board[3])
    print('   |   |')

# test_board = ['#','X','O','X','O','X','O','X','O','X']
# display_board(test_board)
    
# function to get the mark fo P1 and P2
    
def player_input():
    mark = ''       # Stores marker of P1
    
    # to check mark is choosen correctly
    
    while not (mark == 'X' or mark == 'O'):
        mark = input("\n P1 : Do you want X or O ? \n").upper()
    
        # check the mark for X or O
        
        if mark == 'X':
            return 'X', 'O'     # retruns the marks of P1=X and P2=O
        else:
            return 'O', 'X'     # retruns the marks of P1=O and P2=X

# function to display mark on the screen which takes board, mark and position as agrument
            
def mark_placer(board,mark,position):
    board[position] = mark

# funtion to check winner
    
def winner_check(board,mark):
    return ((board[7] == mark and board[8] == mark and board[9] == mark) or # across the top
    (board[4] == mark and board[5] == mark and board[6] == mark) or # across the middle
    (board[1] == mark and board[2] == mark and board[3] == mark) or # across the bottom
    (board[7] == mark and board[4] == mark and board[1] == mark) or # down the middle
    (board[8] == mark and board[5] == mark and board[2] == mark) or # down the middle
    (board[9] == mark and board[6] == mark and board[3] == mark) or # down the right side
    (board[7] == mark and board[5] == mark and board[3] == mark) or # diagonal
    (board[9] == mark and board[5] == mark and board[1] == mark)) # diagonal

# function to choose who goes first P1 or P2

def first():
    if random.randint(0, 1) == 0:
        return 'P2'
    else:
        return 'P1'

# funtion to check the broad has free space or borad is full

def check_space(board,position):
    return board[position] == ' '

def board_full(board):
    for i in range(1,10):
        if check_space(board, i):
            return False
    return True

# function to get the position of the plyaer where they want to mark
    
def player_choice(board):
    position = 0
    place = [1,2,3,4,5,6,7,8,9]
    
    while position not in place or not check_space(board, position):
        position = int(input('\n Chose your next position (1-9)'))
        
    return position

# function to ask player for replay

def replay():
    return input("\n Do you want to play again ? Enter Yes or No : \n").lower().startswith('y')

# the game logic which runs the game

print("\n \t\t <===== \t Welcome to Tic Tac Toe !! \t =====> ")

while True:
    
    theBoard =  [' '] * 10
    P1, P2 = player_input()
    turn = first()
    print(turn + ' will go first ')
    
    play_game = input("\n Are you ready to play the Game ?  Enter Yes OR No : \n")
    
    if play_game.lower()[0] == 'y':
        game_on = True
    else:
        game_on = False
    
    while game_on:
        
        if turn == 'P1':
            # P1 turn
            display_board(theBoard)
            position = player_choice(theBoard)
            mark_placer(theBoard, P1, position)
            
            if winner_check(theBoard, P1):
                display_board(theBoard)
                print("\n Congratulations! P1 has won the game ")
                game_on = False
                
            else:
                if board_full(theBoard):
                    display_board(theBoard)
                    print("\n It's a DRAW!! ")
                    break
                
                else:
                    turn = 'P2'
                    
        else:
            # P2 turn
            display_board(theBoard)
            position = player_choice(theBoard)
            mark_placer(theBoard, P2, position)
            
            if winner_check(theBoard, P2):
                display_board(theBoard)
                print("\n Congratulations! P2 has won the game ")
                game_on = False
                
            else:
                if board_full(theBoard):
                    display_board(theBoard)
                    print("\n It's a DRAW!! ")
                    break
                
                else:
                    turn = 'P1'
        
    if not replay():
        break

print("\n Press any key to exit ")
input()
