def findWords(board, words):
        def  dfs(board, i, j, trie, partial):
            if '#' in trie:
                res.add(partial)
            if not (0 <= i < len(board)) or not (0 <= j < len(board[0])) or board[i][j] not in trie:
                return
            temp = board[i][j]
            board[i][j] = '@'
            for dx, dy in directions:
               dfs(board, i+dx, j+dy, trie[temp], partial+temp) 
            board[i][j] = temp
        trie, res = dict(), set()
        directions = ((0, 1), (0, -1), (1, 0), (-1, 0))
        for word in words:
            t = trie
            for c in word:
                if c not in t:
                    t[c] = dict()
                t = t[c]
            t['#'] = '#'
        for i in range(len(board)):
            for j in range(len(board[0])):
                dfs(board, i, j, trie, '')
        return res

board = [['o','a','a','n'], ['e','t','a','e'], ['i','h','k','r'],['i','f','l','v']]
words = ["oath","pea","eat","rain"]
print(findWords(board, words))