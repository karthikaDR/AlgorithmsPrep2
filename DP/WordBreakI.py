def wordbreak(s, word):

    s1 = ''
    dp = [False for _ in range(len(s) + 1)]

    for i in range(len(s)):
        #Once it finds that a word is present in dictionary, then it wil
        #start searching the next element until end of string
        s1 = s[0:i+1]

        if s1 in word:
            dp[i] = True

        if dp[i] == True:

            if i == len(s) -1:
                return True
            for j in range(i+1,len(s)):
                s1 = s1 [i+1:j+1]
                if s1 in word:
                    dp[i] = True
                if j == len(s) - 1 and dp[i] ==True:
                    return True
    return False

    
    
s = "aaaaaaa"
word = ["aaaa", "aaa"]
print(wordbreak(s, word))

        
