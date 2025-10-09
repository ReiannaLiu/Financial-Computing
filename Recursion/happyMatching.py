def happyMatching(TAs, taPrefs, studentPrefs):
    resSoFar = {ta : None for ta in TAs}
    return happyMatchingHelper(TAs, taPrefs, studentPrefs, 0, resSoFar)

def happyMatchingHelper(TAs, taPrefs, studentPrefs, i, resSoFar):
    if i == len(TAs):
        return resSoFar
    else:
        currTA = TAs[i]
        for student in taPrefs[currTA]:
            if (currTA in studentPrefs[student] and
                student not in resSoFar.values()):
                resSoFar[currTA] = student
                potentialSolns = happyMatchingHelper(TAs, taPrefs, studentPrefs, i + 1, resSoFar)
                if potentialSolns != None:
                    return potentialSolns
                resSoFar[currTA] = None
        return None

def testHappyMatching():
    TAs = ['A', 'B', 'C']
    taPrefs = { 'A' : ['1', '2'],
                'B' : ['3', '2'],
                'C' : ['1']
              }
    studentPrefs = { '1' : ['A', 'B', 'C'],
                     '2' : ['A', 'B'],
                     '3' : ['A', 'B', 'C']
                   }
    res = happyMatching(TAs, taPrefs, studentPrefs)
    assert(verifyHappyMatching(taPrefs, studentPrefs, res))

    TAs = ['Amber', 'Anna', 'Isaac']
    taPrefs = { 'Amber' : ['s2', 's1'],
                'Anna' : ['s2'],
                'Isaac' : ['s3']
              }
    studentPrefs = { 's1' : ['Amber', 'Isaac'],
                     's2' : ['Anna'],
                     's3' : ['Isaac', 'Anna']
                   }
    res = happyMatching(TAs, taPrefs, studentPrefs)
    assert(verifyHappyMatching(taPrefs, studentPrefs, res))

    TAs = ['Yuktha', 'Rhea', 'Lauren', 'Amber']
    taPrefs = { 'Yuktha' : ['s1', 's2', 's3'],
                'Rhea' : ['s4', 's2'],
                'Lauren' : ['s2', 's4', 's1'],
                'Amber' : ['s1', 's2', 's3', 's4'] }
    studentPrefs = { 's1' : ['Yuktha'],
                     's2' : ['Lauren'],
                     's3' : ['Amber'],
                     's4' : ['Rhea'] 
                   }
    res = happyMatching(TAs, taPrefs, studentPrefs)
    assert(verifyHappyMatching(taPrefs, studentPrefs, res))

    TAs = ['Yuktha', 'Rhea', 'Lauren', 'Amber']
    taPrefs = { 'Yuktha' : ['s1', 's3'],
                'Rhea' : ['s2', 's4'],
                'Lauren' : ['s1'],
                'Amber' : ['s1', 's3'] 
              }
    studentPrefs = { 's1' : ['Yuktha', 'Amber', 'Lauren'],
                     's2' : ['Rhea'],
                     's3' : ['Yuktha'],
                     's4' : ['Amber', 'Rhea'] 
                   }
    assert(happyMatching(TAs, taPrefs, studentPrefs) == None)


# This function is used by the test function above
def verifyHappyMatching(taPrefs, studentPrefs, res):
    allStudents = []
    for ta in res:
        student = res[ta]
        if student in allStudents: # different TAs are matched with the same student
            return False
        elif student not in taPrefs[ta]: # ta wants the student
            return False
        elif ta not in studentPrefs[student]: # student wants the ta
            return False
        allStudents.append(student)
    return True

def main():
    testHappyMatching()

main()