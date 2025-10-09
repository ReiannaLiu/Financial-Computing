"""
def backtracker(input):
    # Generally the initial state includes the input, 
    # but likely also includes additional information
    return backtrackingHelper(initialState)

def backtrackingHeper(state):
    if "we're in a solution state":
        # If you've reached a solution state, the answer to the 
        # problem should be contained in the state (likely it's
        # just one of the variables passed into the function)
        return solution
    else:
        for move in "possible moves from this state":
            if "the move is legal":
                "make the move to generate a new state"
                potentialSoln = backtrackingHelper(newState)
                if potentialSoln != None:
                    return potentialSoln
                # If the move was made non-mutatingly, you don't need 
                # to explicitly undo it. But if it was made mutatingly, 
                # you need to explicitly undo the move
                "undo the move to restore the state"
        return None
"""

'''
Background: a word ladder is a list of words where the last letter 
of each word is the first letter of the next word. 

Given: A list of words 
Return: A reordered list of those words that is a word ladder, 
or None if it's impossible.
'''

# BACKTRACKING -- NON-MUTATING
def wordLadder(words):
    return wordLadderHelper(words, [])

def wordLadderHelper(words, ladder):
    if words == []:
        return ladder
    else:
        for i in range(len(words)):
            word = words[i]
            if not ladder or word[0] == ladder[-1][-1]:
                words.pop(i)
                ladder.append(word)
                potentialSoln = wordLadderHelper(words, ladder)
                if potentialSoln is not None:
                    return potentialSoln
                words.insert(i, word)
                ladder.pop()
        return None
    
# BACKTRACKING -- MUTATING
def wordLadder(words):
    return wordLadderHelper(words, [])

def wordLadderHelper(words, ladder):
    if words == []:
        return ladder
    else:
        for i in range(len(words)):
            word = words[i]
            rest = words[:i] + words[i+1:]
            if not ladder or word[0] == ladder[-1][-1]:
                newLadder = ladder + [word]
                solution = wordLadderHelper(rest, newLadder)
                if solution is not None:
                    return solution
        return None

def testWordLadder():
    assert(wordLadder(['goose', 'dog', 'elk', 'toad']) ==
                      ['toad', 'dog', 'goose', 'elk'])
    assert(wordLadder(['goose', 'cat', 'elk', 'toad']) ==
                      None)

testWordLadder()