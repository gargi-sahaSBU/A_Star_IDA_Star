import queue as Q
from copy import deepcopy
import sys
import resource

class State:
	def __init__(self, parent, moves, board, n ,goal_state, row, col):
		self.parent = parent
		#sequence of moves made so far to reach this state from initial state
		self.moves = moves
		#position of the blank square
		self.row = row 
		self.col = col
		#position of elements in the board stored in a list of lists
		self.board = board
		#Calculating value of h for this node
		h_n = 0
		for i in range(0,n):
			for j in range(0,n):
				if self.board[i][j] != goal_state[i][j]:
					h_n = h_n + 1
		self.h = h_n
		
		if parent == None:
			self.g = 0
		else:
			self.g = parent.g + 1
		self.f = self.g + self.h

	#defining comparison operator for priority queue insertion
	def __lt__(self, other):
		if (self.f == other.f) :
			return (self.h < other.h)
		else:
			return (self.f < other.f)

def Generate_successors(state1,n,goal_state):
	# obtaining list of all successors
	successors = Return_successors(state1, n, goal_state)
	return successors

def Return_successors(state1, n, goal_state):
	all_succ = list()
	#if moving left is legal,generate new state
	if (state1.col - 1) >= 0:
		new_board = deepcopy(state1.board)
		new_board[state1.row][state1.col] = new_board[state1.row][state1.col - 1]
		new_board[state1.row][state1.col - 1] = 0
		succ_L = State(state1, state1.moves + ',L',new_board,n, goal_state,state1.row, state1.col-1)
		all_succ.append(succ_L)

	#if moving right is legal,generate new state
	if (state1.col + 1) < n:
		new_board = deepcopy(state1.board)
		new_board[state1.row][state1.col] = new_board[state1.row][state1.col + 1]
		new_board[state1.row][state1.col + 1] = 0
		succ_R = State(state1, state1.moves + ',R',new_board,n, goal_state,state1.row, state1.col+1)
		all_succ.append(succ_R)

	#if moving down is legal,generate new state
	if (state1.row + 1) < n:
		new_board = deepcopy(state1.board)
		new_board[state1.row][state1.col] = new_board[state1.row + 1][state1.col]
		new_board[state1.row +1][state1.col] = 0
		succ_D = State(state1, state1.moves + ',D',new_board,n, goal_state,state1.row + 1, state1.col)
		all_succ.append(succ_D)
	
	#if moving up is legal,generate new state
	if (state1.row - 1) >= 0:
		new_board = deepcopy(state1.board)
		new_board[state1.row][state1.col] = new_board[state1.row - 1][state1.col]
		new_board[state1.row - 1][state1.col] = 0
		succ_U = State(state1, state1.moves + ',U',new_board,n, goal_state,state1.row - 1, state1.col)
		all_succ.append(succ_U)

	return all_succ



def A_star_search(init_state,goal_state,n):
	Frontier = Q.PriorityQueue()
	Explored = list()
	Frontier_list = list() 

	Frontier.put(init_state)
	Frontier_list.append(str(init_state.board))

	while Frontier.empty() == False:
		curr = Frontier.get()
		Frontier_list.remove(str(curr.board))

		if str(curr.board) == str(goal_state):
			return (curr, len(Explored))

		if str(curr.board) not in Explored:
			Explored.append(str(curr.board))
			successors = Generate_successors(curr,n,goal_state)
			for s in successors:
				if s not in Explored and str(s.board) not in Frontier_list:
					Frontier.put(s)
					Frontier_list.append(str(s.board))

	return (None,None)

def A_star_mt(n,i_file):
	input_file = open(i_file,'r')
	#generating goal config
	goal_state = list()
	num = 1
	for i in range(0,n):
		row = list()
		for j in range(0,n):
			row.append(num)
			num = num + 1
		goal_state.append(row)

	goal_state[n-1][n-1] = 0
	#goal state configuration done

	#constructing initial state from input 
	init_state = list()
	f = input_file.read().split("\n")
	if len(f) > n:
		f = f[0:len(f) -1]
	
	r = 0
	c = 0
	for i in f:
		s = i.split(",")
		row = list()
		for x in s:
			if(x == ''):
				c = s.index(x)
				r = f.index(i)
				row.append(0)
			else:
				row.append(int(x))
		init_state.append(row)

	initial_state = State(None,'',init_state, n, goal_state, r, c)
	#initial state constructed
	
	#call A* search on initial state
	final, len_explored = A_star_search(initial_state,goal_state,n)

	return final,len_explored 





