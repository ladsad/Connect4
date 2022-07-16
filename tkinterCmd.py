#importing necessary modules
from tkinter import *
import csv
import random

def clear():
	#simple function to clear program canvas

	for widget in win.winfo_children():	#winfo_children stores all widgets placed on the canvas
		widget.destroy()

def createBoard():
	#simple function to create the base board

  file=csv.writer(open("board.csv","w", newline="\n"))
  for i in range(6):
    file.writerow(['_','_','_','_','_','_'])

def loadBoard():
	#function to give the board in a simplified nested list form

  b=list(csv.reader(open("board.csv","r",newline="\n")))
  nb=[]
  for i in (b):
    nb.append(i)
  
  return nb

def player(n):
	#setting up a system to seperate the 2 Player & Player vs Bot modes

	global pnum
	pnum=n
	createBoard()
	displayBoard()
	return;

def displayBoard():
	#displays the board allowing player to input moves

	clear()
	board=loadBoard()

	#a check to prevent overlapping moves after win
	if winDetector(board) is True:
		winSequence()
		return;

	#setting up the information on the window
	if pnum==1:
		turnText="PLAYER's TURN: "
		winText="PLAYER 1: "+str(winCount[0])+" | BOT: "+str(winCount[1]//2)
	else:
		if moveCount%2==0:
			turnText="PLAYER 1's TURN: "
		else:
			turnText="PLAYER 2's TURN: "
		winText="PLAYER 1: "+str(winCount[0])+" | PLAYER 2: "+str(winCount[1]//2)


	playerDisplay=Label(win, text=turnText, bg="#202020", fg="white", padx=5, font=fontTup)
	playerDisplay.grid(row=0,column=0, columnspan=6)

	#setting up the board on the window
	for i in range(5,-1,-1):
		for j in range(6):
			if i==5 and board[i][j]=="_":
				if j==0:
					moveButton=Button(win, text="_", bg="#202020", fg="white", padx=5, font=fontTup, activebackground="#BEBEBE", highlightcolor="#505050", command=lambda: inputMove(0))
				elif j==1:
					moveButton=Button(win, text="_", bg="#202020", fg="white", padx=5, font=fontTup, activebackground="#BEBEBE", highlightcolor="#505050", command=lambda: inputMove(1))
				elif j==2:
					moveButton=Button(win, text="_", bg="#202020", fg="white", padx=5, font=fontTup, activebackground="#BEBEBE", highlightcolor="#505050", command=lambda: inputMove(2))
				elif j==3:
					moveButton=Button(win, text="_", bg="#202020", fg="white", padx=5, font=fontTup, activebackground="#BEBEBE", highlightcolor="#505050", command=lambda: inputMove(3))
				elif j==4:
					moveButton=Button(win, text="_", bg="#202020", fg="white", padx=5, font=fontTup, activebackground="#BEBEBE", highlightcolor="#505050", command=lambda: inputMove(4))
				else:
					moveButton=Button(win, text="_", bg="#202020", fg="white", padx=5, font=fontTup, activebackground="#BEBEBE", highlightcolor="#505050", command=lambda: inputMove(5))
				moveButton.grid(row=i+1, column=j)
			elif i<5 and board[i][j]=="_":
				if board[i][j]=="_" and board[i+1][j]=="_":
					blankLabel=Label(win, text=" ", bg="#202020", fg="white", padx=5, font=fontTup)
					blankLabel.grid(row=i+1, column=j)
				else:
					if j==0:
						moveButton=Button(win, text="_", bg="#202020", fg="white", padx=5, font=fontTup, activebackground="#BEBEBE", highlightcolor="#505050", command=lambda: inputMove(0))
					elif j==1:
						moveButton=Button(win, text="_", bg="#202020", fg="white", padx=5, font=fontTup, activebackground="#BEBEBE", highlightcolor="#505050", command=lambda: inputMove(1))
					elif j==2:
						moveButton=Button(win, text="_", bg="#202020", fg="white", padx=5, font=fontTup, activebackground="#BEBEBE", highlightcolor="#505050", command=lambda: inputMove(2))
					elif j==3:
						moveButton=Button(win, text="_", bg="#202020", fg="white", padx=5, font=fontTup, activebackground="#BEBEBE", highlightcolor="#505050", command=lambda: inputMove(3))
					elif j==4:
						moveButton=Button(win, text="_", bg="#202020", fg="white", padx=5, font=fontTup, activebackground="#BEBEBE", highlightcolor="#505050", command=lambda: inputMove(4))
					else:
						moveButton=Button(win, text="_", bg="#202020", fg="white", padx=5, font=fontTup, activebackground="#BEBEBE", highlightcolor="#505050", command=lambda: inputMove(5))
					moveButton.grid(row=i+1, column=j)
			else:
				numberLabel=Label(win, text=board[i][j], bg="#202020", fg="white", padx=5, font=fontTup)
				numberLabel.grid(row=i+1, column=j)
	
	#adding space between the board and wins display
	blankLabel=Label(win, text=" ", bg="#202020", fg="white", padx=5)
	blankLabel.grid(row=7, column=0, columnspan=6)

	#displays the current number of wins
	winDisplay=Label(win, text=winText, bg="#202020", fg="white", padx=5, font=("Courier", 16, "bold"))
	winDisplay.grid(row=8, column=0, columnspan=6)
	return;

def startGame():
	#function which sets up all the basics

	global win
	win=Tk()
	win.title("Connect Four")
	win.configure(bg="#202020")
	win.iconbitmap('logo.ico')
	
	global fontTup
	fontTup=("Courier", 20, "bold")

	global moveCount
	moveCount=0

	global winCount	
	winCount=[0, 0]

	runGame()

	win.mainloop()

def runGame():
	#function which starts the game giving basic instructions and allowing picking between the 2 Modes

	welcomeStr="Hello, Welcome to the Connect4 Game. \nYour aim is simple, get 4 of your counters in a connected line or diagonal!\nThis is a 2 player game so please pick the first player('X') and second player('O').\nWould you like to play against a Bot or another Player?"
	startText=Label(win, text=welcomeStr, bg="#202020", fg="white", padx=5, font=fontTup)
	blankLabel=Label(win,text=" ", bg="#202020", fg="white", padx=5, font=fontTup)
	button_Yes=Button(win, text="Bot", bg="#202020", fg="white", padx=5, font=fontTup, activebackground="#BEBEBE", highlightcolor="#505050", command=lambda: player(1))
	button_No=Button(win, text="Player", bg="#202020", fg="white", padx=5, font=fontTup, activebackground="#BEBEBE", highlightcolor="#505050", command=lambda: player(2))

	startText.grid(row=0, column=0, columnspan=5)
	blankLabel.grid(row=1, column=0, columnspan=5)
	button_Yes.grid(row=2, column=0, columnspan=2)
	button_No.grid(row=2, column=3, columnspan=2)
	return;

def inputMove(colNum=1):
	#function which setups up input of moves

	global moveCount
	moveCount+=1
	if moveCount>36:
		winSequence(0)
	p_num=moveCount%2
	if p_num==1:
		moveDecoder(colNum, "X")
	elif p_num==0 and pnum==2:
		moveDecoder(colNum, "O")
	else:
		botMove()
	return;

def isAvailable(colNum):
	#function which checks if the given column has space & returns the row number where a token can be placed

	board=loadBoard()
	
	if board[0][colNum]!="_":
		return 1,0
	else:
		for i in range(5, -1, -1):
			if board[i][colNum]=="_":
				return 0,i

def moveDecoder(colNum, pchar):
	#function which sets up the moves and inputs them into the board

	board=loadBoard()
	rnum=isAvailable(colNum)

	board[int(rnum[1])][colNum]=pchar
	boardFile=open("board.csv","w", newline="\n")
	writer=csv.writer(boardFile)
	for i in range(6):
		writer.writerow(board[i])
	boardFile.close()

	winCheck=winDetector(board)
	if winCheck is True:
		winSequence()
		return;
	else:
		if pnum==1 & moveCount%2==1:	#runs the bot/code's move
			inputMove()
		displayBoard()
		return;


def winDetector(board):
	#function which checks for wins

	for c in range(6):
		for i in range(5,2,-1):
			if board[i][c]==board[i-1][c] and board[i-1][c]==board[i-2][c] and board[i-2][c]==board[i-3][c] and board[i][c]!='_':
				return True

	for c in range(3):
		for i in range(5,2,-1):
			if board[i][c]==board[i-1][c+1] and board[i-1][c+1]==board[i-2][c+2] and board[i-2][c+2]==board[i-3][c+3] and board[i][c]!='_':
				return True

	for c in range(3,6):
		for i in range(5,2,-1):
			if board[i][c]==board[i-1][c-1] and board[i-1][c-1]==board[i-2][c-2] and board[i-2][c-2]==board[i-3][c-3] and board[i][c]!='_':
				return True

	for i in range(5,-1,-1):
		for c in range(0,3):
			if board[i][c]==board[i][c+1] and board[i][c+1]==board[i][c+2] and board[i][c+2]==board[i][c+3] and board[i][c]!='_':
  			 	return True

	return False  			 	


def winSequence(winD=1):
	#function which displays the win sequence

	global moveCount
	clear()

	if winD==1:
		if pnum==1:
			if moveCount%2==1:
				winText="PLAYER WON!"
				winCount[0]+=1
			else:
				winText="BOT WON!"
				winCount[1]+=1
		else:
			if moveCount%2==1:
				winText="PLAYER 1 WON!"
				winCount[0]+=1
			else:
				winText="PLAYER 2 WON!"
				winCount[1]+=1
	else:
		winText="IT IS A DRAW!"

	winLabel=Label(win, text=winText, bg="#202020", fg="white", padx=5, font=fontTup)
	winLabel.grid(row=0, column=0, columnspan=6)
	
	board=loadBoard()
	
	for i in range(6):
		for j in range(6):
			if board[i][j]=="_":
				blankLabel=Label(win, text=" ", bg="#202020", fg="white", padx=5, font=fontTup)
				blankLabel.grid(row=i+1, column=j)				
			else:
				numberLabel=Label(win, text=board[i][j], bg="#202020", fg="white", padx=5, font=fontTup)
				numberLabel.grid(row=i+1, column=j)

	moveCount=0
	continueLabel=Label(win, text="Would you like to continue?", bg="#202020", fg="white", padx=5, font=fontTup)
	button_Yes=Button(win, text="Yes", bg="#202020", fg="white", padx=5, font=fontTup, activebackground="#BEBEBE", highlightcolor="#505050", command=lambda: player(1))
	button_No=Button(win, text="No", bg="#202020", fg="white", padx=5, font=fontTup, activebackground="#BEBEBE", highlightcolor="#505050", command=lambda: win.quit())

	continueLabel.grid(row=7, column=0, columnspan=6)
	button_Yes.grid(row=8, column=1, columnspan=2)
	button_No.grid(row=8, column=3, columnspan=2)

def botMove():
	#function which calculates the bot's move

	board=loadBoard()
	for i in range(6):
		rnum=isAvailable(i)
		if rnum[0]==0:
			board[int(rnum[1])][i]="O"

			if winDetector(board)==True:
				moveDecoder(i, "O")
				return;
			else:
				board=loadBoard()

	for i in range(6):
		rnum=isAvailable(i)
		if rnum[0]==0:
			board[int(rnum[1])][i]="X"

			if winDetector(board)==True:
				moveDecoder(i, "O")
				return;
			else:
				board=loadBoard()
	
	while True:
		colNum=random.randint(0,5)
		rnum=isAvailable(colNum)
		if rnum[0]==0:
			moveDecoder(colNum, "O")
			return;