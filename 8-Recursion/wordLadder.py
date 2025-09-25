def wordLadder(words):
    return wordLadderHelper(words, [])

def wordLadderHelper(words, ladder):
    if words == []:
        return ladder
    else:
        for i in range(len(words)):
            word = words[i]
            if (ladder == []) or (word[0] == ladder[-1][-1]):
                ladder.append(word)
                words.pop(i)
                potentialLadder = wordLadderHelper(words, ladder)
                if potentialLadder is not None:
                    return potentialLadder
                ladder.pop()
                words.insert(i, word)
        return None

def testWordLadder():
    print("Testing wordLadder()...", end=" ")
    
    assert(wordLadder(['goose', 'toad', 'dog', 'elk',]) == 
                            ['toad', 'dog', 'goose', 'elk'])
    
    assert(wordLadder(['goose', 'toad', 'cat', 'elk']) == 
                            None)
    print("Passed!")

testWordLadder()