# There are 8 prison cells in a row, and each cell is either occupied or vacant.
# Each day, whether the cell is occupied or vacant changes according to the 
# following rules:
#     If a cell has two adjacent neighbors that are both occupied or both vacant, 
#      then the cell becomes occupied.
#     Otherwise, it becomes vacant.
# (Note that because the prison is a row, the first and the last cells in the
#  row can't have two adjacent neighbors.)
# We describe the current state of the prison in the following way:
#  cells[i] == 1 if the i-th cell is occupied, else cells[i] == 0.
# Given the initial state of the prison, return the state of the prison 
# after N days (and N such changes described above.)
N = 1000000000
N = N%14
    
    
# The cycle repeats itself after 14 days.
if N == 0:
    N = 14
dict1 = {}
i = 0
cells = [1,0,0,1,0,0,1,0]
while i < N:
    
    for count in range(len(cells)-1):      
        
            
            if cells[count-1] == cells[count+1]:
                dict1[count] = 1
                
            if cells[count-1] != cells[count+1]:
                dict1[count] = 0
                
            
    print(dict1)            
    for count in range(len(cells)): 
            
            if count in dict1:
                cells[count] = dict1[count]
            
            if count == 0 or count == len(cells) - 1:
                cells[count] = 0
            
    dict1 = {}        
    i += 1
    
print(cells)