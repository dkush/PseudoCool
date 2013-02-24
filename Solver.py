import collections
import re

class Grid:
  
	def __init__(self):
		self.corresp_sqs = dict()
		self.rows = dict()
		self.cols = dict()
		self.possVals = dict()
		self.assVals = dict()
		
		self.corresp_sqs[1] = [(1,1),(1,2),(1,3),(2,1),(2,2),(2,3),(3,1),(3,2),(3,3)]
		self.corresp_sqs[4] = [(4,1),(4,2),(4,3),(5,1),(5,2),(5,3),(6,1),(6,2),(6,3)]
		self.corresp_sqs[7] = [(7,1),(7,2),(7,3),(8,1),(8,2),(8,3),(9,1),(9,2),(9,3)]
		self.corresp_sqs[2] = [(1,4),(1,5),(1,6),(2,4),(2,5),(2,6),(3,4),(3,5),(3,6)]
		self.corresp_sqs[5] = [(4,4),(4,5),(4,6),(5,4),(5,5),(5,6),(6,4),(6,5),(6,6)]
		self.corresp_sqs[8] = [(7,4),(7,5),(7,6),(8,4),(8,5),(8,6),(9,4),(9,5),(9,6)]
		self.corresp_sqs[3] = [(1,7),(1,8),(1,9),(2,7),(2,8),(2,9),(3,7),(3,8),(3,9)]
		self.corresp_sqs[6] = [(4,7),(4,8),(4,9),(5,7),(5,8),(5,9),(6,7),(6,8),(6,9)]
		self.corresp_sqs[9] = [(7,7),(7,8),(7,9),(8,7),(8,8),(8,9),(9,7),(9,8),(9,9)]
		
		for x in self.corresp_sqs.keys():
				for y in self.corresp_sqs[x]:
					self.possVals[y] = list(range(1,10))
					self.assVals[y] = int()
		self.make_cols(self.cols)
		self.make_rows(self.rows)
		
	def make_rows(self,row_dict):
	  for row in range(1,10):
			self.rows[row] = []
			for col in range(1,10):
				self.rows[row].append((row,col))
    
	def make_cols(self,col_dict):
		for col in range(1,10):
			self.cols[col] = []
			for row in range(1,10):
				self.cols[col].append((row,col))
	
	
	def get_square(coord):
		'''
		takes (x,y) coordinates of a cell, returns the square 
		it's a member of. 
		csqs is corresp_sqs dict
		'''
		for x in self.corresp_sqs:
			if coord in self.corresp_sqs[x]:
				return self.corresp_sqs[x]
	
	
	def get_sthg(self,coord,which_dict):
		for x in which_dict:
			if coord in which_dict[x]:
				y = [x for x in which_dict[x]]
				return y
	
	def remove_mates(self,coord,num,which_dict):
		mates = self.get_sthg(coord,which_dict)
		mates.remove(coord)
		for x in mates:
			if num in self.possVals[x]:
				self.possVals[x].remove(num)
				
	
	def assign(self,coord,num):
		'''
		#assigns a value (num) to a cell at given location (coord)
		#subsequently removes num from poss values in row, column
		'''
		self.assVals[coord] = num
		self.possVals[coord] = []
		self.remove_mates(coord,num,self.corresp_sqs)
		self.remove_mates(coord,num,self.rows)
		self.remove_mates(coord,num,self.cols)

	def get_poss(self,coord):
		return self.possVals[coord]
	
	def print_puzzle(self):
		'''
		 prints current state of the puzzle
		 as a 9 x 9 grid
		'''
		print " __________________________________"
		for x in range(1,10):
			print self.get_row_print(x)
		print " ----------------------------------"
		

	def get_row_print(self,num):
		row = "|%s ," % (self.assVals[num,1])
		for x in range(2,10):
			row+=" %s ," % (self.assVals[num,x])
		row = row.rstrip(",")
		row += "|"
		row = re.sub('0'," ",row)
		return row






class Solver:
	
	def __init__(self,grid):
		self.assVals = grid.assVals
		print "Let's do this."
	
	def only_in(self,which_dict,which_item, grid):
		#
		# checks to see whether there's some val V
		# s.t. V can only be assigned to one cell in 
		# some element (be it local square, row, or col - specified
		# by 'which_dict')
		#
		possList = []
		for cell in which_dict[which_item]:
			possList += grid.get_poss(cell)
		dupes = [x for x, y in collections.Counter(possList).items() if y > 1]
		possList = [x for x in possList if x not in dupes]
		for x in possList:
			## find which square val belongs to
			for cell in which_dict[which_item]:
					# assign value to that cell
					if x in grid.possVals[cell]:
						grid.assign(cell,x)
	
	
	def reductive_pass(self,coord,grid):
		# subtracts filled-in values from row, column, and square cell(x,y) 
		# is a member of from possible range of vals for cell(x,y)
		possList = grid.possVals[coord]
		lists = [grid.rows[coord[0]],grid.cols[coord[1]], grid.get_sthg(coord,grid.corresp_sqs)]
		for xs in lists:
			possList = list(set(possList)-set(xs))
		return possList
	
	def update_possVals(self,grid):
		for x in grid.possVals:
			grid.possVals[x] = self.reductive_pass(x,grid)
	
	def look_for_singletons(self,grid):
		for cell in grid.possVals:
			if len(grid.possVals[cell]) == 1:
				grid.assign(cell,grid.possVals[cell].pop())
	
	def run_solver(self,grid):
		xx = 0
		while xx < 10:
			self.update_possVals(grid)
			self.look_for_singletons(grid)
			for x in range(1,10):
				self.only_in(grid.corresp_sqs,x,grid)
				self.only_in(grid.rows,x,grid)
				self.only_in(grid.cols,x,grid)
			xx+=1


if __name__ == '__main__':
	grid = Grid()
	solver = Solver(grid)
	
	grid.assign((1,2),9)
	grid.assign((1,3),3)
	grid.assign((1,4),1)
	grid.assign((1,6),5)
	grid.assign((1,7),6)
	grid.assign((1,8),4)
                       
	grid.assign((9,2),4)
	grid.assign((9,3),7)
	grid.assign((9,4),3)
	grid.assign((9,6),2)
	grid.assign((9,7),8)
	grid.assign((9,8),5)
                       
	grid.assign((2,1),7)
	grid.assign((2,9),5)
                       
	grid.assign((3,1),5)
	grid.assign((3,3),1)
	grid.assign((3,4),2)
	grid.assign((3,6),9)
	grid.assign((3,7),3)
	grid.assign((3,9),7)
                       
	grid.assign((7,1),3)
	grid.assign((7,3),2)
	grid.assign((7,4),4)
	grid.assign((7,6),8)
	grid.assign((7,7),1)
	grid.assign((7,9),9)
                       
	grid.assign((8,1),6)
	grid.assign((8,9),4)
                       
	grid.assign((4,1),2)
	grid.assign((4,9),3)
                       
	grid.assign((6,1),9)
	grid.assign((6,9),1)
                       
	grid.assign((5,2),3)
	grid.assign((5,3),6)
	grid.assign((5,4),9)
	grid.assign((5,6),7)
	grid.assign((5,7),5)
	grid.assign((5,8),2)
	grid.print_puzzle()
	solver.run_solver(grid)
	grid.print_puzzle()
