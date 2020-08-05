"""Given a 2D board and a list of words from the dictionary, find all words in 
the board. 
Each word must be constructed from letters of sequentially adjacent cell, 
where "adjacent" cells are those horizontally or vertically neighboring. 
The same letter cell may not be used more than once in a word."""

def wordsearch(matrix, words):
    def findwords(matrix, trie, ro,co,path):     

        # Once the word gets completed, that is if there is '#  
        if '#' in trie:
            result.add(path)
        
        if not (0 <= ro < len(matrix)) or not (0 <= co < len(matrix[0])) or matrix[ro][co] not in trie:
            return
        temp = matrix[ro][co]
        matrix[ro][co] = '@'
        for r, c in directions:            
            findwords(matrix, trie[temp], ro + r,co+c,path+temp )

        matrix[ro][co] = temp
         
    
    directions = ((0,1), (0,-1), (1,0), (-1,0))
    row = len(matrix)   # determines the number of rows
    col = len(matrix[0]) #Determines the number of columns

    trie = dict()
    # Building the trie datastructure to populate the mentioned words
    #{'o': {'a': {'t': {'h': {'#': '#'}}}}, 'p': {'e': {'a': {'#': '#'}}},
    #  'e': {'a': {'t': {'#': '#'}}}, 'r': {'a': {'i': {'n': {'#': '#'}}}}}
    for word in words:
                t = trie
                for c in word:
                    if c not in t:
                        t[c] = dict()
                    t = t[c]
                t['#'] = '#'

    print(t,trie)
    result = set()
    for ro in range(row):
        for co in range(col):
            findwords(matrix, trie, ro, co,'')

    return result


matrix = [['o','a','a','n'], ['e','t','a','e'], ['i','h','k','r'],['i','f','l','v']]
words = ["oath","pea","eat","rain"]

print(wordsearch(matrix,words))

