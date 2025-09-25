# def chickenNuggets(nuggetPacks, numToBuy):
#     if numToBuy < 0:
#         return False
#     elif numToBuy == 0:
#         return True
#     elif numToBuy > 0:
#         for pack in nuggetPacks:
#             if chickenNuggets(nuggetPacks, numToBuy - pack):
#                 return True
#         return False
    
# def chickenNuggets(nuggetPacks, numToBuy):
#     if numToBuy < 0:
#         return (False, [])
#     elif numToBuy == 0:
#         return (True, [])
#     elif numToBuy > 0:
#         for pack in nuggetPacks:
#             solved, res = chickenNuggets(nuggetPacks, numToBuy - pack)
#             if solved:
#                 return (True, [pack] + res)
#         return (False, [])
    
def chickenNuggets(nuggetPacks, numToBuy):
    if numToBuy < 0:
        return None
    elif numToBuy == 0:
        return []
    elif numToBuy > 0:
        for pack in nuggetPacks:
            res = chickenNuggets(nuggetPacks, numToBuy - pack)
            if res is not None:
                return [pack] + res
        return None

def testChickenNuggets():
    print('To buy 11 with packs [4, 10]:', chickenNuggets([4, 10], 11))
    print('To buy 14 with packs [4, 10]:', chickenNuggets([4, 10], 14))
    
testChickenNuggets()