from fc_utils import almostEqual, Tree
import heapq
import copy
from collections import Counter, deque
################################################################################
# Algorithm Name: Prefix or Preprocessing Pattern
# preprocessed = [initial value] * (n + 1)
# for i in range(n):
#   update preprocessed[i + 1] based on preprocessed[i] and current element
# return preprocessed
#
# Time Complexity: O(N)
################################################################################

# Example: averagePrices
def preprocessStocks(prices):
    """
    Preprocess a list of stock prices for fast average-price queries.

    Args:
        prices (list[float]): List of stock prices, where index i represents 
            the price at time i.
    
    Returns:
        list[float]: A preprocessed data structure that supports O(1) 
            average queries.
    """
    preprocessed = [0] * (len(prices) + 1)
    for i in range(len(prices)):
        preprocessed[i + 1] = preprocessed[i] + prices[i]
    return preprocessed

def getAverage(preprocessed, i, j):
    """
    Compute the average stock price between indices i and j using
    the preprocessed data.

    Args:
        preprocessed (list[float]): The prefix-sum or equivalent data
            structure produced by `preprocessStocks`.
        i (int): Start index (inclusive).
        j (int): End index (exclusive).
    
    Returns:
        float: Average stock price in the range [i, j).
    """
    return (preprocessed[j] - preprocessed[i]) / (j - i)

def testAveragePrices():
    prices = [3.0, 4.5, 3.6, 3.1, 2.7, 4.8, 5.1]
    preprocessed = preprocessStocks(prices)
    assert(almostEqual(getAverage(preprocessed, 0, 7), 3.8285714))
    assert(almostEqual(getAverage(preprocessed, 0, 5), 3.38))
    assert(almostEqual(getAverage(preprocessed, 0, 3), 3.7))
    assert(almostEqual(getAverage(preprocessed, 6, 7), 5.1))
    assert(almostEqual(getAverage(preprocessed, 4, 7), 4.2))
    assert(almostEqual(getAverage(preprocessed, 2, 7), 3.86))
    assert(almostEqual(getAverage(preprocessed, 3, 4), 3.1))
    assert(almostEqual(getAverage(preprocessed, 1, 6), 3.74))
    assert(almostEqual(getAverage(preprocessed, 2, 5), 3.1333333))

# Example: countSublists
def countSublists(L, k):
    """
    Count the number of non-empty contiguous sublists whose sum equals k.

    This function uses a prefix-sum and hashmap approach to efficiently count
    all sublists (continuous portions of the list) whose elements add up to k.
    It runs in O(N) time, where N is the length of the input list.

    Args:
        L (list[int]): List of integers.
        k (int): Target sum value.

    Returns:
        int: Number of non-empty sublists whose sum equals k.

    Time Complexity: O(N) — each element is processed once.
    """
    preMap = {0 : 1}
    preSum = res = 0
    for elem in L:
        preSum += elem
        res += preMap.get(preSum - k, 0)
        preMap[preSum] = 1 + preMap.get(preSum, 0)
    return res

def testCountSublists():
    L = [3, 4, 7, 2, -3, 1, 4, 2]
    assert(countSublists(L, 7) == 4)   # [3, 4], [7], [7, 2, -3, 1], [1, 4, 2]
    assert(countSublists(L, 4) == 4)   # [4], [2, -3, 1, 4], [4], [-3, 1, 4, 2]
    assert(countSublists(L, 5) == 1)   # [1, 4]
    assert(countSublists(L, 0) == 1)   # [2, -3, 1]

    L = [2, 4, 5, -2]
    assert(countSublists(L, 9) == 2)    # [2, 4, 5, -2], [4, 5]

    L = [1, 2, 1, 2, 1]
    assert(countSublists(L, 3) == 4)   # [1, 2], [2, 1], [1, 2], [2, 1]
    assert(countSublists(L, 4) == 2)   # [1, 2, 1], [1, 2, 1]

    L = [-1, -2, -3]
    assert(countSublists(L, -3) == 2)  # [-1, -2], [-3]

    L = [0, 0]
    assert(countSublists(L, 0) == 3)  # [0], [0, 0], [0]
    assert(countSublists(L, 1) == 0)

    L = [5]
    assert(countSublists(L, 5) == 1)
    assert(countSublists(L, 0) == 0)

def productExceptSelf(L):
    """
    Return a list where each element is the product of all other elements in L.

    This function computes, for each index i, the product of all elements
    in the list L except L[i]. 

    Args:
        L (list[int]): A list of integers with at least two elements.

    Returns:
        list[int]: A list M of the same length as L, where M[i] equals
        the product of all elements in L except L[i].

    Time Complexity: O(N)
    """
    n = len(L)
    preprocessed = [1] * (n + 1)
    for i in range(n):
        preprocessed[i + 1] = preprocessed[i] * L[i]
    
    postprocessed = [1] * (n + 1)
    for i in range(n - 1, -1, -1):
        postprocessed[i] = postprocessed[i + 1] * L[i]
    
    res = [1] * n
    for i in range(n):
        res[i] = preprocessed[i] * postprocessed[i + 1]
    return res

def testProductExceptSelf():
    assert(productExceptSelf([2, 5, 3, 1]) == [15, 6, 10, 30])
    assert(productExceptSelf([2, 5, 3, 1, 10]) == [150, 60, 100, 300, 30])
    assert(productExceptSelf([3, 6, 5]) == [30, 15, 18])
    assert(productExceptSelf([1, 2]) == [2, 1])

# More Examples to Work Through
# queryProducts: exactly the same logic as averagePrices
def preprocess(L):
    preprocessed = [1] * (len(L) + 1)
    for i in range(len(L)):
        preprocessed[i + 1] = preprocessed[i] * L[i]
    return preprocessed

def getProduct(preprocessed, i, j):
    return preprocessed[j] / preprocessed[i]

def testQueryProducts():
    L = [4, 2, 1, 8, 3, 5, 2]
    preprocessed = preprocess(L)
    assert(getProduct(preprocessed, 0, 1) == 4)
    assert(getProduct(preprocessed, 0, 2) == 8)
    assert(getProduct(preprocessed, 0, 3) == 8)
    assert(getProduct(preprocessed, 0, 4) == 64)
    assert(getProduct(preprocessed, 0, 7) == 1920)
    assert(getProduct(preprocessed, 6, 7) == 2)
    assert(getProduct(preprocessed, 5, 7) == 10)
    assert(getProduct(preprocessed, 4, 7) == 30)
    assert(getProduct(preprocessed, 2, 5) == 24)
    assert(getProduct(preprocessed, 2, 6) == 120)
    assert(getProduct(preprocessed, 1, 4) == 16)
    assert(getProduct(preprocessed, 1, 5) == 48)
    assert(getProduct(preprocessed, 3, 4) == 8)

# balanceIndex: logic exactly the same as productExceptSelf
def balanceIndex(L):
    n = len(L)
    preprocessed = [0] * (n + 1)
    for i in range(n):
        preprocessed[i + 1] = preprocessed[i] + L[i]
    
    postprocessed = [0] * (n + 1)
    for i in range(n - 1, -1, -1):
        postprocessed[i] = postprocessed[i + 1] + L[i]
        
    for i in range(n):
        if preprocessed[i] == postprocessed[i + 1]:
            return i
    return None

def testBalanceIndex():
    assert(balanceIndex([3, 5, 1, 4, 2, 2]) == 2)   # 3 + 5 == 4 + 2 + 2
    assert(balanceIndex([1, -3, 2, 1]) == 0)        # 0 == -3 + 2 + 1
    assert(balanceIndex([5, -3, -2, 1]) == 3)       # 5 - 3 - 2 == 0
    assert(balanceIndex([1, 0, 1]) == 1)            # 1 == 1
    assert(balanceIndex([0, 0, 0]) == 0)            # 0 == 0 + 0
    assert(balanceIndex([5]) == 0)                  # 0 == 0

    assert(balanceIndex([2, -2, 1, 2]) == None)
    assert(balanceIndex([2, 1, 1, 2]) == None)
    assert(balanceIndex([3, 3]) == None)
    assert(balanceIndex([]) == None)

################################################################################
# Data Structure: Stacks -- FILO

# Algorithm Name: Monotonic Stack
# Initialize result structure (e.g., list of default values)
# stack = []
#
# for each element in sequence (forward or backward):
#     while stack is not empty and current element violates monotonic property:
#         pop from stack
#         (optionally update result based on popped element or current element)
#
#     push current element (or its index) onto stack
# return result
#
# Time Complexity: O(N)
# Space Complexity: O(N)
################################################################################

# Example: nextGreaterElement
def nextGreaterElement(L):
    """
    Return a list where each element is the next greater element to its right.

    For each index i in L, this function finds the first element to the right
    of L[i] that is greater than L[i]. If no such element exists, the result
    contains -1 at that position.

    Args:
        L (list[int]): List of integers.

    Returns:
        list[int]: List M such that M[i] is the next greater element to the
        right of L[i], or -1 if none exists.

    Time Complexity: O(N) — each element is pushed and popped at most once.
    """
    res = [-1] * len(L)
    # monotonic decreasing stack (elem, pos)
    stack = []
    for currPos, currElem in enumerate(L):
        while stack != [] and L[currPos] > stack[-1][0]:
            prev, prevPos = stack.pop()
            res[prevPos] = currElem
        stack.append((currElem, currPos))
    return res

def testNextGreaterElement():
    assert(nextGreaterElement([8, 5, 8, 12, 15]) == [12, 8, 12, 15, -1])
    assert(nextGreaterElement([4, 7, 2, 7, 1, 9]) == [7, 9, 7, 9, 9, -1])
    assert(nextGreaterElement([6, 2, 7, 1, 5]) == [7, 7, -1, 5, -1])
    assert(nextGreaterElement([10, 5, 3, 8]) == [-1, 8, 8, -1])
    assert(nextGreaterElement([5, 4, 3, 2, 1]) == [-1, -1, -1, -1, -1])
    assert(nextGreaterElement([1, 2, 3, 4, 5]) == [2, 3, 4, 5, -1])
    assert(nextGreaterElement([3, 3, 3, 3]) == [-1, -1, -1, -1])
    assert(nextGreaterElement([5]) == [-1])
    assert(nextGreaterElement([]) == [])

# Example: dailyTemperatures
def dailyTemperatures(temperatures):
    """
    Return a list where each element is the next greater element to its right.

    For each index i in L, this function finds the first element to the right
    of L[i] that is greater than L[i]. If no such element exists, the result
    contains -1 at that position. The function runs in O(N) time using a
    monotonic decreasing stack.

    Args:
        L (list[int]): List of integers.

    Returns:
        list[int]: List M such that M[i] is the next greater element to the
        right of L[i], or -1 if none exists.

    Time Complexity: O(N).
    """
    res = [0] * len(temperatures)
    stack = [] # (temp, pos) pair
    for currPos, currTemp in enumerate(temperatures):
        while stack != [] and currTemp > stack[-1][0]:
            prevTemp, prevPos = stack.pop()
            res[prevPos] = currPos - prevPos
        stack.append((currTemp, currPos))
    return res

def testDailyTemperatures():
    assert(dailyTemperatures([73,74,75,71,69,72,76,73]) == [1,1,4,2,1,1,0,0])
    assert(dailyTemperatures([30,40,50,60]) == [1,1,1,0])
    assert(dailyTemperatures([30,60,90]) == [1,1,0])

# Example: stockSpan
def stockSpan(prices):
    """
    Return the stock span for each day.

    The stock span of a stock's price on day i is the number of consecutive
    days leading up to and including day i where the price was less than or
    equal to the price on day i. The function uses a monotonic decreasing
    stack to compute spans efficiently in O(N) time.

    Args:
        prices (list[int]): List of stock prices, where prices[i] represents
        the stock price on day i.

    Returns:
        list[int]: A list where each element at index i represents the stock
        span for day i.

    Example:
        >>> stockSpan([100, 80, 60, 70, 60, 75, 85])
        [1, 1, 1, 2, 1, 4, 6]
        # Explanation:
        # - Day 0: span = 1 (first day)
        # - Day 1: span = 1 (80 < 100)
        # - Day 2: span = 1 (60 < 80)
        # - Day 3: span = 2 ([60, 70])
        # - Day 4: span = 1 (60 < 70)
        # - Day 5: span = 4 ([60, 70, 60, 75])
        # - Day 6: span = 6 ([80, 60, 70, 60, 75, 85])

    Time Complexity: O(N) — each index is pushed and popped from the stack at most once.
    """
    stack = [] # (price, pos) monotonic decreasing
    res = [1] * (len(prices))
    
    for currPos, currPrice in enumerate(prices):
        while stack != [] and currPrice >= stack[-1][0]:
            prevPrice, prevPos = stack.pop()
            res[currPos] = res[currPos] + res[prevPos]
        stack.append((currPrice, currPos))
    return res

def testStockSpan():
    # assert(stockSpan([100, 80, 60, 70, 60, 75, 85]) == [1, 1, 1, 2, 1, 4, 6])
    assert(stockSpan([20, 20, 15, 40, 40, 35, 50]) == [1, 2, 1, 4, 5, 1, 7])
    assert(stockSpan([70, 70, 85, 30, 30, 55, 95]) == [1, 2, 3, 1, 2, 3, 7])
    assert(stockSpan([1, 2, 3, 4, 5]) == [1, 2, 3, 4, 5])
    assert(stockSpan([9, 7, 5, 3, 1]) == [1, 1, 1, 1, 1])
    assert(stockSpan([10, 10, 10]) == [1, 2, 3])
    assert(stockSpan([5]) == [1])
    assert(stockSpan([]) == [])

################################################################################
# Data Structure: Min/Max Heap

# Algorithm Name: kSmallest / kLargest
################################################################################
def findKthLargest(nums, k):
    minHeap = []
    for num in nums:
        heapq.heappush(minHeap, num)
        if len(minHeap) > k:
            heapq.heappop(minHeap)
    return minHeap[0]

def testFindKthLargest():
    assert(findKthLargest([3,2,1,5,6,4], 2) == 5)
    assert(findKthLargest([3,2,3,1,2,4,5,5,6], 4) == 4)

# Example: topKFrequent
def topKFrequent(nums, k):
    valToFreq = Counter(nums)
    
    minHeap = [] # (freq, val) pair
    for val, freq in valToFreq.items():
        heapq.heappush(minHeap, (freq, val))
        if len(minHeap) > k:
            heapq.heappop(minHeap)
    return [val for (freq, val) in minHeap]

def testTopKFrequent():
    assert(topKFrequent([1,1,1,2,2,3], 2) == [2,1])
    assert(topKFrequent([1], 1) == [1])
    assert(topKFrequent([1,2,1,2,1,2,3,1,3,2], 2) == [1,2])

# Example: kSmallestPairs
def kSmallestPairs(nums1, nums2, k):
    """
    Return the k pairs with the smallest sums from two sorted arrays.

    Given two integer arrays nums1 and nums2 (both sorted in non-decreasing
    order) and an integer k, this function returns the k pairs (u, v)
    where u is from nums1 and v is from nums2 such that the sum u + v
    is among the k smallest possible pair sums.

    The function uses a min-heap to efficiently generate the next smallest
    pair sum in O(k log k) time complexity.

    Args:
        nums1 (list[int]): The first sorted integer array.
        nums2 (list[int]): The second sorted integer array.
        k (int): The number of smallest pairs to return.

    Returns:
        list[list[int]]: A list of k pairs [u, v] with the smallest sums.
        If there are fewer than k possible pairs, returns all of them.
    
    Time Complexity:
        O(k log k)
    """
    n1, n2 = len(nums1), len(nums2)
    minHeap = [] # (sums, i, j)
    for i in range(n1):
        heapq.heappush(minHeap, (nums1[i] + nums2[0], i, 0))
    res = []
    while len(res) < k and len(minHeap) > 0:
        currSum, i, j = heapq.heappop(minHeap)
        res.append([nums1[i], nums2[j]])
        if j + 1 < n2:
            heapq.heappush(minHeap, (nums1[i] + nums2[j + 1], i, j + 1))    
    return res

def testKSmallestPairs():
    assert(kSmallestPairs([1,7,11], [2,4,6], 3) == [[1,2],[1,4],[1,6]])
    assert(kSmallestPairs([1,1,2], [1,2,3], 2) == [[1,1],[1,1]])
    assert(kSmallestPairs([1,2,4,5,6], [3,5,7,9], 3) == [[1,3],[2,3],[1,5]])
    assert(kSmallestPairs([1,2,4,5,6], [3,5,7,9], 20) == [[1,3],[2,3],[1,5],[2,5],[4,3],[1,7],[5,3],[2,7],[4,5],[6,3],[1,9],[5,5],[2,9],[4,7],[6,5],[5,7],[4,9],[6,7],[5,9],[6,9]])


################################################################################
# Data Structure: Min/Max Heap

# Algorithm Name: Minimum Completion Time -- Event-driven simulation
################################################################################

def fastestPizzaProduction(cookTimes, numPizzas):
    availableWorkers = [] # (availableTime, cookTime)
    for cookTime in cookTimes:
        heapq.heappush(availableWorkers, (cookTime, cookTime))
    
    currTime = 0
    while numPizzas > 0:
        currTime, cookTime = heapq.heappop(availableWorkers)
        nxtAvailableTime = currTime + cookTime
        heapq.heappush(availableWorkers, (nxtAvailableTime, cookTime))
        numPizzas -= 1
    return currTime

def testFastestPizzaProduction():
    cookTimes = [2, 6, 4, 1]
    assert(fastestPizzaProduction(cookTimes, 7) == 4) 
    assert(fastestPizzaProduction(cookTimes, 6) == 4) 
    assert(fastestPizzaProduction(cookTimes, 11) == 6) 
    assert(fastestPizzaProduction(cookTimes, 12) == 7) 
    assert(fastestPizzaProduction(cookTimes, 13) == 8) 
    assert(fastestPizzaProduction(cookTimes, 0) == 0)
    assert(fastestPizzaProduction(cookTimes, 1) == 1)
    
    assert(fastestPizzaProduction([3], 1) == 3)
    assert(fastestPizzaProduction([3], 2) == 6)
    assert(fastestPizzaProduction([3], 3) == 9)
    assert(fastestPizzaProduction([2, 2, 2], 6) == 4)
    assert(fastestPizzaProduction([5, 5], 4) == 10)
    assert(fastestPizzaProduction([1, 2], 100) == 67)
    
    assert(fastestPizzaProduction([1, 10, 3, 7], 4) == 3)
    assert(fastestPizzaProduction([1, 10, 3, 7], 8) == 6)
    
    assert(fastestPizzaProduction([1, 100], 10) == 10)
    assert(fastestPizzaProduction([1, 100], 101) == 100)

# Example: minMeetingRooms
def minMeetingRooms(intervals):
    """
    Return the minimum number of meeting rooms required to hold all meetings.

    Each meeting is represented by an interval [start, end], where 'start' and 'end'
    are the meeting start and end times. The goal is to determine the fewest number
    of rooms needed so that no meetings overlap in the same room.

    This function uses a min-heap (priority queue) to track the earliest meeting end
    time. As new meetings start, we either reuse a room (if the earliest meeting has
    ended) or allocate a new room.

    Args:
        intervals (list[list[int]]): A list of meeting time intervals where
            intervals[i] = [start_i, end_i].

    Returns:
        int: The minimum number of meeting rooms required to accommodate all meetings
        without overlap.

    Time Complexity:
        O(N log N) — Sorting intervals and using a heap for active meetings.
    """
    intervals.sort()
    rooms = 0
    roomSchedule = [] # (endTime) pair
    for start, end in intervals:   
        while len(roomSchedule) > 0 and start >= roomSchedule[0]:
            heapq.heappop(roomSchedule)
        heapq.heappush(roomSchedule, end)
        rooms = max(rooms, len(roomSchedule))
    return rooms

def testMinMeetingRooms():
    # Room 1: (1, 4), (5, 6)
    # Room 2: (2, 3)
    assert(minMeetingRooms([(5, 6), (1, 4), (2, 3)]) == 2)

    # Room 1: (0, 10)
    # Room 2: (1, 5), (9, 12)   <--- Note, (9, 12) could also be in room 3 or 4
    # Room 3: (2, 7)
    # Room 4: (3, 8)
    assert(minMeetingRooms([(0, 10), (1, 5), (2, 7), (3, 8), (9, 12)]) == 4)

    # Room 1: (0, 30)
    # Room 2: (5, 10), (15, 20)
    assert(minMeetingRooms([(0, 30), (5, 10), (15, 20)]) == 2)

    # Room 1: (1, 5), (6, 9)    <--- Note, (6, 9) could also be in room 2 or 3
    # Room 2: (1, 5)
    # Room 3: (3, 6)
    assert(minMeetingRooms([(1, 5), (6, 9), (1, 5), (3, 6)]) == 3)

    # Room 1: (1, 5), (6, 10)
    # Room 2: (2, 6)
    # Room 3: (3, 7)
    assert(minMeetingRooms([(1, 5), (2, 6), (3, 7), (6, 10)]) == 3)

    assert(minMeetingRooms([(7, 10), (2, 4)]) == 1)
    assert(minMeetingRooms([(0, 1), (1, 2), (2, 3)]) == 1)
    assert(minMeetingRooms([(1, 2)]) == 1)
    assert(minMeetingRooms([]) == 0)

def fastestGradingTime(gradingTimes, speedups, numQuizzes):
    availableTA = [] # (availableTime, gradingTime, speedups, numQuizzesGraded)

    for i in range(len(gradingTimes)):
        heapq.heappush(availableTA, (gradingTimes[i], gradingTimes[i], speedups[i], 1))

    currTime = 0
    while numQuizzes > 0:
        currTime, gradingTime, speedup, numQuizzesGraded = heapq.heappop(availableTA)
        if numQuizzesGraded == 2:
            newGradingTime, newSpeedup = gradingTime - speedup, 0
        else:
            newGradingTime, newSpeedup = gradingTime, speedup
        heapq.heappush(availableTA, (currTime + newGradingTime, newGradingTime, newSpeedup, numQuizzesGraded + 1))
        numQuizzes -= 1
    return currTime

def testFastestGradingTime():
    gradingTimes = [2, 6, 4, 3]
    speedups     = [1, 2, 1, 2]

    # TA 0: 4 quizzes (2 + 2 + 1 + 1 = 6 mins)
    # TA 1: 1 quiz    (6 mins)
    # TA 2: 1 quiz    (4 mins)
    # TA 3: 2 quizzes (3 + 3 = 6 mins)
    assert(fastestGradingTime(gradingTimes, speedups, 8) == 6)

    # TA 0: 5 quizzes (2 + 2 + 1 + 1 + 1 = 7 mins)
    # TA 1: 1 quiz    (6 mins)
    # TA 2: 1 quiz    (4 mins)
    # TA 3: 3 quizzes (3 + 3 + 1 = 7 mins)
    assert(fastestGradingTime(gradingTimes, speedups, 10) == 7)
    assert(fastestGradingTime(gradingTimes, speedups, 9) == 7)

    # TA 0: 6 quizzes (2 + 2 + 1 + 1 + 1 + 1 = 8 mins)
    # TA 1: 1 quiz    (6 mins)
    # TA 2: 2 quizzes (4 + 4 = 8 mins)
    # TA 3: 4 quizzes (3 + 3 + 1 + 1 = 8 mins)
    assert(fastestGradingTime(gradingTimes, speedups, 13) == 8)
    assert(fastestGradingTime(gradingTimes, speedups, 12) == 8)
    assert(fastestGradingTime(gradingTimes, speedups, 11) == 8)

    assert(fastestGradingTime(gradingTimes, speedups, 4) == 4)
    assert(fastestGradingTime(gradingTimes, speedups, 3) == 4)
    assert(fastestGradingTime(gradingTimes, speedups, 2) == 3)
    assert(fastestGradingTime(gradingTimes, speedups, 1) == 2)
    
    gradingTimes = [4, 10, 7, 3, 6]
    speedups     = [1,  4, 3, 1, 2]

    # TA 0: 2 quizzes (4 + 4 = 8 mins)      4 + 4 + 2*6
    # TA 1: 0 quizzes (0 mins)              10 + 10
    # TA 2: 1 quiz    (7 mins)              7 + 7 + 4
    # TA 3: 3 quizzes (3 + 3 + 2 = 8 mins)  3 + 3 + 2*7
    # TA 4: 1 quiz    (6 mins)              6 + 6 + 4*2
    assert(fastestGradingTime(gradingTimes, speedups, 7) == 8)
    assert(fastestGradingTime(gradingTimes, speedups, 24) == 20)


################################################################################
# Data Structure: Min/Max Heap

# Algorithm Name: Minimum Completion Time -- Time-driven simulation
################################################################################
def leastInterval(tasks, n):
    """
    Return the minimum number of CPU intervals required to finish all tasks.

    Each task takes exactly one CPU interval to execute. After running a task
    of type X, you must wait at least `n` intervals before running X again.
    During cooldown intervals, the CPU may be idle or run a different task.

    The function determines the minimum total time units (CPU intervals)
    needed to execute all tasks while respecting the cooldown constraint.

    Args:
        tasks (list[str]): A list of uppercase letters representing task types.
            Each element corresponds to one execution of that task.
        n (int): The required number of idle intervals between identical tasks.

    Returns:
        int: The minimum number of time units to complete all tasks.

    Example:
        >>> leastInterval(["A","A","A","B","B","B"], 2)
        8
        # One optimal schedule: A → B → idle → A → B → idle → A → B

    Time Complexity:
        O(T log K), where T is the total number of tasks and
        K is the number of distinct task types (heap operations per task).
    """
    cooldown = deque() # (availableTime, numTasksLeft) pair
    taskToFreq = Counter(tasks)
    availableTask = [-freq for freq in taskToFreq.values()]
    heapq.heapify(availableTask)

    time = 0
    while len(cooldown) > 0 or len(availableTask) > 0:
        time += 1

        if len(availableTask) > 0:
            remaining = 1 + heapq.heappop(availableTask)
            if remaining != 0:
                cooldown.append((time + n, remaining))  

        while len(cooldown) > 0 and cooldown[0][0] <= time:
            heapq.heappush(availableTask, cooldown.popleft()[1])

    return time

def testLeastInterval():
    assert(leastInterval(["A","A","A","B","B","B"], 2) == 8)
    assert(leastInterval(["A","C","A","B","D","B"], 1) == 6)
    assert(leastInterval(["A","A","A", "B","B","B"], 3) == 10)

################################################################################
# Algorithm Name: Recursion
#
# 1. Define the objective:
#    "If I call this function, what result should I expect? 
#     What does it compute or return, and in what format?"
#
# 2. Base case:
#    Handle the simplest version of the problem directly 
#    (the stopping condition for recursion).
#    Wrote this the last.
#
# 3. Recursive case:
#    Assume the function works correctly for a smaller or next step 
#    (trust the recursion).
#    Focus only on what the current step should do 
#    before or after that recursive call.
################################################################################

# Example: powerset
def powerset(L):
    if L == []:
        return [[]]
    else:
        psFromRest = powerset(L[1:])
        res = []
        for ps in psFromRest:
            res.append(ps.copy())
            res.append([L[0]] + ps)
        return sorted(res)

def testPowerSet():
    # Make sure that your output list is sorted. 
    L = [1, 2, 3]
    output = [[], [1], [2], [3], [1, 2], [1, 3], [2, 3], [1, 2, 3]]
    assert(powerset(L) == sorted(output))

    L = [5, -8]
    output = [[], [-8], [5], [5, -8]]
    assert(powerset(L) == sorted(output))

    L = [-1]
    output = [[], [-1]]
    assert(powerset(L) == sorted(output))

    L = []
    assert(powerset(L) == [[]])

# Example: preorder
def getTreePreorder(tree):
    if tree.isLeaf():
        return [tree.getValue()]
    else:
        res = [tree.getValue()]
        for child in tree.getChildren():
            res += getTreePreorder(child)
        return res

def testGetTreePreorder():
    '''
             ┌─── 2 ─────── 5 ─────── 8 
             │
             ├─── 3 
    ─── 1 ───┤
             │         ┌─── 6 
             └─── 4 ───┤
                       └─── 7 
    '''
    t1 = Tree(1,
              Tree(2,
                   Tree(5,
                        Tree(8)
                       )
                  ),
              Tree(3),
              Tree(4,
                   Tree(6),
                   Tree(7)
                  )
             )
    assert(getTreePreorder(t1) == [1, 2, 5, 8, 3, 4, 6, 7])

    '''
    ─── 4 ─────── 5 
    '''
    t2 = Tree(4,
              Tree(5),
             )
    assert(getTreePreorder(t2) == [4, 5])

    '''
                       ┌─── b 
             ┌─── a ───┤
    ─── 6 ───┤         └─── c 
             │
             └─── 4 ─────── 5
    '''
    t3 = Tree(6,
              Tree('a',
                   Tree('b'),
                   Tree('c')
                  ),
              Tree(4,
                   Tree(5),
                  )
             )
    assert(getTreePreorder(t3) == [6, 'a', 'b', 'c', 4, 5])

    '''
             ┌─── 2 
    ─── 1 ───┤
             └─── 3
    '''
    t4 = Tree(1,
              Tree(2),
              Tree(3)
             )
    assert(getTreePreorder(t4) == [1, 2, 3])

    '''
    ─── 0 
    '''
    t5 = Tree(0)
    assert(getTreePreorder(t5) == [0])

################################################################################
# Algorithm Name: Recursive DFS
# def dfs(node):
#     # 1. Base case: check for goal or stopping condition
#     if node satisfies desired condition:
#         return desired output

#     # 2. Recursive case: explore neighbors / children
#     for neighbor in node.getNeighbors():
#         result = dfs(neighbor)
#         if result is desired output:
#             return result   # stop early if found

#     # 3. If nothing found
#     return not found / None / False
################################################################################

# Example: dfsSearch
def dfsSearch(t, v):
    if t.getValue() == v:
        return True
    else:
        for child in t.getChildren():
            if dfsSearch(child, v):
                return True
        return False

def testDFSSearch():
    t1 = Tree(1,
              Tree(2,
                   Tree(5,
                        Tree(8))),
              Tree(3),
              Tree(4,
                   Tree(6),
                   Tree(7)))
    assert(dfsSearch(t1, 1) == True)
    assert(dfsSearch(t1, 2) == True)
    assert(dfsSearch(t1, 5) == True)
    assert(dfsSearch(t1, 7) == True)
    assert(dfsSearch(t1, 8) == True)
    
    assert(dfsSearch(t1, 9) == False)
    assert(dfsSearch(t1, 12) == False)
    assert(dfsSearch(t1, -1) == False)
    
    t2 = Tree(4,
              Tree(5))
    
    assert(dfsSearch(t2, 4) == True)
    assert(dfsSearch(t2, 5) == True)
    
    assert(dfsSearch(t2, 1) == False)
    assert(dfsSearch(t2, 8) == False)
    
    t3 = Tree(6,
              Tree('a',
                   Tree('b'),
                   Tree('c')),
              Tree(4,
                   Tree(5)))

    assert(dfsSearch(t3, 6) == True)
    assert(dfsSearch(t3, 'a') == True)
    assert(dfsSearch(t3, 'b') == True)
    assert(dfsSearch(t3, 'c') == True)
    assert(dfsSearch(t3, 4) == True)
    assert(dfsSearch(t3, 5) == True)
    
    assert(dfsSearch(t3, "s") == False)
    assert(dfsSearch(t3, 12) == False)
    assert(dfsSearch(t3, -1) == False)


# Example: dfsTraversal
def dfsTraversal(graph, startNode):
    return dfsTraversalHelper(graph, startNode, set())

def dfsTraversalHelper(graph, currNode, visited):
    if currNode in visited:
        return []
    else:
        visited.add(currNode)
        res = [currNode]
        for neighbor in graph[currNode]:
                res += dfsTraversalHelper(graph, neighbor, visited)
        return res

def testDFSTraversal():
    graph = {
        'A' : ['B', 'D', 'F'],
        'B' : ['C', 'D', 'E'],
        'C' : ['A', 'D'],
        'D' : ['A'],
        'E' : [],
        'F' : ['D', 'E'],
    }
    assert(dfsTraversal(graph, 'A') == ['A', 'B', 'C', 'D', 'E', 'F'])
    assert(dfsTraversal(graph, 'B') == ['B', 'C', 'A', 'D', 'F', 'E'])
    assert(dfsTraversal(graph, 'C') == ['C', 'A', 'B', 'D', 'E', 'F'])
    assert(dfsTraversal(graph, 'D') == ['D', 'A', 'B', 'C', 'E', 'F'])
    assert(dfsTraversal(graph, 'E') == ['E'])
    assert(dfsTraversal(graph, 'F') == ['F', 'D', 'A', 'B', 'C', 'E'])

# Example: citiesVisited
def citiesVisited(flights, destination):
    if flights.getValue() == destination:
        return [destination]
    else:
        res = [flights.getValue()]
        for neighborCity in flights.getChildren():
            potentialPath = citiesVisited(neighborCity, destination)
            if potentialPath != None:
                return res + potentialPath
        return None

def testCitiesVisited():
    pghFlights = Tree('PGH',
                      Tree('DET',
                      Tree('DEN'),
                      Tree('ORD')),
                      Tree('IAD',
                           Tree('PHX')),
                      Tree('LGA',
                           Tree('SAN'),
                           Tree('JFK'),
                           Tree('LAX')))
    assert(citiesVisited(pghFlights, 'JFK') == ['PGH', 'LGA', 'JFK'])
    assert(citiesVisited(pghFlights, 'IAD') == ['PGH', 'IAD'])
    assert(citiesVisited(pghFlights, 'PGH') == ['PGH'])

    mcoFlights = Tree('MCO',
                      Tree('MIA',
                            Tree('SEA',
                                 Tree('LGA'),
                                 Tree('IAD')),
                            Tree('ORD')),
                      Tree('SFA',
                           Tree('DFW')),
                      Tree('LAX',
                           Tree('PGH'),
                           Tree('JFK',
                                Tree('PHX')),
                           Tree('SAN')))
    assert(citiesVisited(mcoFlights, 'MIA') == ['MCO', 'MIA'])
    assert(citiesVisited(mcoFlights, 'DFW') == ['MCO', 'SFA', 'DFW'])
    assert(citiesVisited(mcoFlights, 'PHX') == ['MCO', 'LAX', 'JFK', 'PHX'])

def maxBranchSum(tree):
    if tree.isLeaf():
        return tree.getValue()
    else:
        res = float('-inf')
        for child in tree.getChildren():
            potentialBranchSum = maxBranchSum(child)
            res = max(res, tree.getValue() + potentialBranchSum)
        return res

def testMaxBranchSum():
    '''
                        ┌─── 8 
             ┌─── 5 ────┤
             │          └─── -3 
    ─── 1 ───┤
             │          ┌─── 40 
             └─── -9 ───┤
                        └─── 8 
    '''
    t = Tree(1,
             Tree(5,
                  Tree(8),
                  Tree(-3)),
             Tree(-9,
                  Tree(40),
                  Tree(8)))
    assert(maxBranchSum(t) == 32)   # 1 - 9 + 40 = 32

    '''
             ┌─── 3 
             │
    ─── 2 ───┼─── 100 ─────── 4 
             │
             └─── -5 ──────── 1000 
    '''
    t = Tree(2,
             Tree(3),
             Tree(100, Tree(4)),
             Tree(-5, Tree(1000)))
    assert(maxBranchSum(t) == 997)   # 2 - 5 + 100 = 997

    '''
               ┌─── -20 ─────── -1 
    ─── -10 ───┤
               └─── -30 
    '''
    t = Tree(-10,
             Tree(-20, Tree(-1)),
             Tree(-30))
    assert(maxBranchSum(t) == -31)  # -10 - 20 - 1 = -31

    '''
    ─── 5 ─────── 4 ─────── 3 ─────── 2 
    '''
    t = Tree(5, Tree(4, Tree(3, Tree(2))))
    assert(maxBranchSum(t) == 14)   # 5 + 4 + 3 + 2 = 14


################################################################################
# Algorithm Name: Iterative DFS
################################################################################
def iterativeDFS(graph, startNode):
    toVisit = [startNode]
    visited = []

    while len(toVisit) > 0:
        currNode = toVisit.pop()

        if currNode in visited:
            continue

        visited.append(currNode)
        for neighbor in graph[currNode]:
            toVisit.append(neighbor)
    return visited

def testIterativeDFS():
    graph = {
        'A' : ['B', 'D', 'F'],
        'B' : ['C', 'D', 'E'],
        'C' : ['A', 'D'],
        'D' : ['A'],
        'E' : [],
        'F' : ['D', 'E'],
    }

    assert(iterativeDFS(graph, 'A') == ['A', 'F', 'E', 'D', 'B', 'C'])
    assert(iterativeDFS(graph, 'B') == ['B', 'E', 'D', 'A', 'F', 'C'])
    assert(iterativeDFS(graph, 'C') == ['C', 'D', 'A', 'F', 'E', 'B'])
    assert(iterativeDFS(graph, 'D') == ['D', 'A', 'F', 'E', 'B', 'C'])
    assert(iterativeDFS(graph, 'E') == ['E'])
    assert(iterativeDFS(graph, 'F') == ['F', 'E', 'D', 'A', 'B', 'C'])

################################################################################
# Algorithm Name: (Iterative) BFS
################################################################################
def bfs(graph, startNode):
    toVisit = deque([startNode])
    visited = []

    while len(toVisit) > 0:
        currNode = toVisit.popleft()

        if currNode in visited:
            continue
        visited.append(currNode)
        for neighbor in graph[currNode]:
            toVisit.append(neighbor)
    return visited

def testBFS():

    graph = {
        'A' : ['B', 'D', 'F'],
        'B' : ['C', 'D', 'E'],
        'C' : ['A', 'D'],
        'D' : ['A'],
        'E' : [],
        'F' : ['D', 'E'],
    }
    assert(bfs(graph, 'A') == ['A', 'B', 'D', 'F', 'C', 'E'])
    assert(bfs(graph, 'B') == ['B', 'C', 'D', 'E', 'A', 'F'])
    assert(bfs(graph, 'C') == ['C', 'A', 'D', 'B', 'F', 'E'])
    assert(bfs(graph, 'D') == ['D', 'A', 'B', 'F', 'C', 'E'])
    assert(bfs(graph, 'E') == ['E'])
    assert(bfs(graph, 'F') == ['F', 'D', 'E', 'A', 'B', 'C'])

def isComplete(tree):
    toVisit = deque([tree])
    foundEmpty = False

    while len(toVisit) > 0:
        currNode = toVisit.popleft()

        if currNode == None:
            foundEmpty = True
        else:
            if foundEmpty == True:
                return False
            for child in currNode.getChildren():
                toVisit.append(child)
    return True

def testIsComplete():
    # t = Tree(1,
    #         Tree(2, Tree(4), Tree(5)),
    #         Tree(3, Tree(6), Tree(7)))
    # assert(isComplete(t) == True)

    t = Tree(1,
            Tree(2, None, Tree(5)),
            Tree(3, Tree(6)))
    assert(isComplete(t) == False) 

################################################################################
# Algorithm Name: Backtracking
#
# def backtracker(input):
#     # Generally the initial state includes the input, 
#     # but likely also includes additional information
#     return backtrackingHelper(initialState)

# def backtrackingHeper(state):
#     if "we're in a solution state":
#         # If you've reached a solution state, the answer to the 
#         # problem should be contained in the state (likely it's
#         # just one of the variables passed into the function)
#         return solution
#     else:
#         for move in "possible moves from this state":
#             if "the move is legal":
#                 "make the move to generate a new state"
#                 potentialSoln = backtrackingHelper(newState)
#                 if potentialSoln != None:
#                     return potentialSoln
#                 # If the move was made non-mutatingly, you don't need 
#                 # to explicitly undo it. But if it was made mutatingly, 
#                 # you need to explicitly undo the move
#                 "undo the move to restore the state"
#         return None
################################################################################

# Example: happyMatching
def happyMatching(TAs, taPrefs, studentPrefs):
    if len(studentPrefs) != len(taPrefs):
        return None
    mapSoFar = {ta : None for ta in TAs}
    return happyMatchingHelper(TAs, taPrefs, studentPrefs, 0, mapSoFar)

def happyMatchingHelper(TAs, taPrefs, studentPrefs, i, mapSoFar):
    if i == len(TAs):
        return mapSoFar
    else:
        for stud in taPrefs[TAs[i]]:
            if TAs[i] in studentPrefs[stud] and stud not in mapSoFar.values():
                mapSoFar[TAs[i]] = stud
                potentialMap = happyMatchingHelper(TAs, taPrefs, studentPrefs, i + 1, mapSoFar)
                if potentialMap != None:
                    return potentialMap
                mapSoFar[TAs[i]] = None
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


# Example: solveMiniSudoku
def solveMiniSudoku(board):
    newBoard = copy.deepcopy(board)
    rows, cols, blockSize = len(board), len(board[0]), len(board)
    rowVisited = {row : set() for row in range(rows)} 
    colVisited = {col : set() for col in range(cols)}
    blockVisited = {block : set() for block in range(blockSize)}
    for row in range(rows):
        for col in range(cols):
            num = board[row][col]
            blockIdx = row // 2 * 2 + col // 2
            if board[row][col] == 0:
                continue
            elif num not in rowVisited[row] and num not in colVisited[col] and num not in blockVisited[blockIdx]:
                rowVisited[row].add(num)
                colVisited[col].add(num)
                blockVisited[blockIdx].add(num)
            else:
                return None
    return solveMiniSudokuHelper(newBoard, 0, 0, rowVisited, colVisited, blockVisited)

def solveMiniSudokuHelper(board, r, c, rowVisited, colVisited, blockVisited):
    rows, cols = len(board), len(board[0])
    if r == rows:
        return board
    
    (nr, nc) = (r, c + 1) if c + 1 < cols else (r + 1, 0)
    
    if board[r][c] != 0:
        return solveMiniSudokuHelper(board, nr, nc, rowVisited, colVisited, blockVisited)
    
    b = r // 2 * 2 + c // 2
    for d in range(1, 5):
        if (d not in blockVisited[b] and
            d not in rowVisited[r] and 
            d not in colVisited[c]):
                board[r][c] = d
                rowVisited[r].add(d)
                colVisited[c].add(d)
                blockVisited[b].add(d)
                potentialSolns = solveMiniSudokuHelper(board, nr, nc, rowVisited, colVisited, blockVisited)
                if potentialSolns != None:
                    return potentialSolns
                board[r][c] = 0
                rowVisited[r].remove(d)
                colVisited[c].remove(d)
                blockVisited[b].remove(d)
    return None

def testSolveMiniSudoku():
    board1  = [[3, 0, 0, 0],
               [0, 1, 0, 3],
               [4, 0, 1, 0],
               [0, 0, 0, 0]]
    solved1 = [[3, 4, 2, 1],
               [2, 1, 4, 3],
               [4, 3, 1, 2],
               [1, 2, 3, 4]]
    board1Copy = copy.deepcopy(board1)
    assert(solveMiniSudoku(board1) == solved1)
    assert(board1 == board1Copy) # verify we do not mutate the original board

    board2  = [[4, 0, 0, 2],
               [0, 2, 0, 0],
               [0, 0, 3, 0],
               [0, 0, 0, 1]]
    solved2 = [[4, 3, 1, 2],
               [1, 2, 4, 3],
               [2, 1, 3, 4],
               [3, 4, 2, 1]]
    board2Copy = copy.deepcopy(board2)
    assert(solveMiniSudoku(board2) == solved2)
    assert(board2 == board2Copy) # verify we do not mutate the original board

    board3  = [[0, 3, 0, 0],
               [0, 0, 0, 3],
               [1, 0, 0, 0],
               [0, 0, 4, 0]]
    solved3 = [[2, 3, 1, 4],
               [4, 1, 2, 3], 
               [1, 4, 3, 2], 
               [3, 2, 4, 1]]
    board3Copy = copy.deepcopy(board3)
    assert(solveMiniSudoku(board3) == solved3)
    assert(board3 == board3Copy) # verify we do not mutate the original board
    
    board4 = [[4, 3, 0, 0], # This board has no solution
              [1, 0, 3, 0],
              [0, 0, 2, 0],
              [4, 1, 0, 1]]
    board4Copy = copy.deepcopy(board4)
    assert(solveMiniSudoku(board4) == None)
    assert(board4 == board4Copy) # verify we do not mutate the original board

    board5 = [[4, 0, 2, 1], # This board has no solution
              [2, 1, 4, 3],
              [1, 2, 3, 0],
              [3, 0, 1, 4]]
    board5Copy = copy.deepcopy(board5)
    assert(solveMiniSudoku(board5) == None)
    assert(board5 == board5Copy) # verify we do not mutate the original board

    board6 = [[4, 1, 2, 3], # This board is full but illegal; it has no solution
              [2, 3, 4, 1],
              [1, 4, 3, 2],
              [4, 2, 1, 3]]
    board6Copy = copy.deepcopy(board6)
    assert(solveMiniSudoku(board6) == None)
    assert(board6 == board6Copy) # verify we do not mutate the original board

# Example: kightsTour
def solveKnightsTour(rows, cols):
    board = [[0] * cols for _ in range(rows)]
    board[0][0] = 1
    return solveKnightsTourHelper(rows, cols, 0, 0, board)

def solveKnightsTourHelper(rows, cols, r, c, boardSoFar):
    directions = [(2, 1), (1, 2), (-1, 2), (-2, 1), (-2, -1), (-1, -2), (1, -2), (2, -1)]
    if boardSoFar[r][c] == rows * cols:
        return boardSoFar
    else:
        for (dr, dc) in directions:
            nr, nc = r + dr, c + dc
            if (0 <= nr < rows and 0 <= nc < cols and boardSoFar[nr][nc] == 0):
                boardSoFar[nr][nc] = boardSoFar[r][c] + 1
                potentialSolns = solveKnightsTourHelper(rows, cols, nr, nc, boardSoFar)
                
                if potentialSolns != None:
                    return potentialSolns
                boardSoFar[nr][nc] = 0
        return None

def testKnightsTour():
    solution = solveKnightsTour(3, 4)
    assert(isValidKnightsTour(3, 4, solution))

    solution = solveKnightsTour(3, 3)
    assert(solution == None)

    solution = solveKnightsTour(4, 4)
    assert(solution == None)

    solution = solveKnightsTour(3, 1)
    assert(solution == None)

# This helper function is used by the test function above
def isValidKnightsTour(rows, cols, solutionBoard):
    # Verify correct dimensions and rectangular board
    if len(solutionBoard) != rows:
        return False
    for row in solutionBoard:
        if len(row) != cols:
            return False
    # Map each number to the (row, col) it exists at
    # Verify each number from 1 to rows*cols appears exactly once
    locations = dict()
    for row in range(rows):
        for col in range(cols):
            num = solutionBoard[row][col]
            if num in locations:
                return False
            if num <= 0 or rows*cols < num:
                return False
            locations[num] = (row, col)
    # Verify each move is a legal move:
    for move in range(1, rows*cols):
        row0, col0 = locations[move]
        row1, col1 = locations[move+1]
        drow = abs(row0 - row1)
        dcol = abs(col0 - col1)
        if not ((drow == 1 and dcol == 2) or (drow == 2 and dcol == 1)):
            return False
    return True

################################################################################
# Algorithm Name: Dijkstra's Algorithm / Distances
################################################################################
def singleSourceShortestPath(graph, startNode):
    distances = {node : float('inf') for node in graph}
    toVisit = [(0, startNode)]

    while len(toVisit) > 0:
        currDist, currNode = heapq.heappop(toVisit)
        if currDist < distances[currNode]:
            distances[currNode] = currDist
            for neighbor, weight in graph[currNode].items():
                toVisit.append((weight + currDist, neighbor))
    return distances

def testSingleSourceDijkstra():
    graph = {
        'S' : {'A' : 1, 'C' : 5},
        'A' : {'B' : 2},
        'B' : {'C' : 1, 'D' : 5},
        'C' : {'D' : 3},
        'D' : {},
        'E' : {'D' : 2}
    }
    assert(singleSourceShortestPath(graph, 'S') == {'S': 0, 'A': 1, 'B': 3, 'C': 4, 'D': 7, 'E': float('inf')})

def singleDestinationShortestPath(graph, endNode):
    reversedGraph = {node : {} for node in graph}
    for u in graph:
        for v, weight in graph[u].items():
            reversedGraph[v][u] = weight

    distances = {node : float('inf') for node in graph}
    toVisit = [(0, endNode)]

    while len(toVisit) > 0:
        currDist, currNode = heapq.heappop(toVisit)
        if currDist < distances[currNode]:
            distances[currNode] = currDist
            for neighbor, weight in reversedGraph[currNode].items():
                heapq.heappush(toVisit, (weight + currDist, neighbor))
    return distances

def testSingleDestinationDijkstra():
    graph = {
        'S' : {'A' : 1, 'C' : 5},
        'A' : {'B' : 2},
        'B' : {'C' : 1, 'D' : 5},
        'C' : {'D' : 3},
        'D' : {},
        'E' : {'D' : 2}
    }
    expected = {'S': 7, 'A': 6, 'B': 4, 'C': 3, 'D': 0, 'E': 2}
    assert(singleDestinationShortestPath(graph, 'D') == expected)

    graph = {
        'A': {'B': 4, 'C': 2},
        'B': {'C': 5, 'D': 10},
        'C': {'E': 3},
        'D': {},
        'E': {'D': 4}
    }
    expected = {'A': 9, 'B': 10, 'C': 7, 'D': 0, 'E': 4}
    assert(singleDestinationShortestPath(graph, 'D') == expected)

    graph = {
        '1': {'2': 7, '3': 9, '6': 14},
        '2': {'3': 10, '4': 15},
        '3': {'4': 11, '6': 2},
        '4': {'5': 6},
        '5': {},
        '6': {'5': 9}
    }
    expected = {'1': 20, '2': 21, '3': 11, '4': 6, '5': 0, '6': 9}
    assert(singleDestinationShortestPath(graph, '5') == expected)

    graph = {
        'X': {'Y': 2},
        'Y': {'Z': 2},
        'Z': {'W': 2},
        'W': {}
    }
    expected = {'X': 6, 'Y': 4, 'Z': 2, 'W': 0}
    assert(singleDestinationShortestPath(graph, 'W') == expected)

    graph = {
        'P': {'Q': 8, 'R': 2},
        'Q': {'S': 3},
        'R': {'S': 7, 'T': 4},
        'S': {'T': 1},
        'T': {}
    }
    expected = {'P': 6, 'Q': 4, 'R': 4, 'S': 1, 'T': 0}
    assert(singleDestinationShortestPath(graph, 'T') == expected)

def singlePairShortestPath(graph, startNode, endNode):
    distances = {node : float("inf") for node in graph}
    toVisit = [(0, startNode)]

    while len(toVisit) > 0:
        currDist, currNode = heapq.heappop(toVisit)

        if currNode == endNode:
            return currDist
        
        if currDist < distances[currNode]:
            distances[currNode] = currDist

            for neighbor, weight in graph[currNode].items():
                heapq.heappush(toVisit, (currDist + weight, neighbor))
    return distances

def testSinglePairDijkstra():
    # Test 1
    graph = {
        'S': {'A': 1, 'C': 5},
        'A': {'B': 2},
        'B': {'C': 1, 'D': 5},
        'C': {'D': 3},
        'D': {},
        'E': {'D': 2}
    }
    # Shortest S → D = S → A → B → C → D = 1 + 2 + 1 + 3 = 7
    assert(singlePairShortestPath(graph, 'S', 'D') == 7)

    # Test 2
    graph = {
        'A': {'B': 4, 'C': 2},
        'B': {'C': 5, 'D': 10},
        'C': {'E': 3},
        'D': {},
        'E': {'D': 4}
    }
    # Shortest A → D = A → C → E → D = 2 + 3 + 4 = 9
    assert(singlePairShortestPath(graph, 'A', 'D') == 9)

    # Test 3
    graph = {
        '1': {'2': 7, '3': 9, '6': 14},
        '2': {'3': 10, '4': 15},
        '3': {'4': 11, '6': 2},
        '4': {'5': 6},
        '5': {},
        '6': {'5': 9}
    }
    # Shortest 1 → 5 = 1 → 3 → 6 → 5 = 9 + 2 + 9 = 20
    assert(singlePairShortestPath(graph, '1', '5') == 20)

    # Test 4
    graph = {
        'X': {'Y': 2},
        'Y': {'Z': 2},
        'Z': {'W': 2},
        'W': {}
    }
    # Shortest X → W = 2 + 2 + 2 = 6
    assert(singlePairShortestPath(graph, 'X', 'W') == 6)

    # Test 5
    graph = {
        'P': {'Q': 8, 'R': 2},
        'Q': {'S': 3},
        'R': {'S': 7, 'T': 4},
        'S': {'T': 1},
        'T': {}
    }
    # Shortest P → T = P → R → T = 2 + 4 = 6
    assert(singlePairShortestPath(graph, 'P', 'T') == 6)

    # Test 6
    graph = {
        'A': {'B': 1, 'C': 4},
        'B': {'C': 2, 'D': 7},
        'C': {'D': 3},
        'D': {}
    }
    # Shortest A → D = A→B→C→D = 1+2+3 = 6
    assert(singlePairShortestPath(graph, 'A', 'D') == 6)

################################################################################
# Algorithm Name: Dijkstra's Algorithm / Path Reconstruction
################################################################################
def singleSourceShortestPathWithReconstruction(graph, startNode):
    distances = {node : float('inf') for node in graph}
    parents = {node : None for node in graph}
    toVisit = [(0, startNode, None)]

    while len(toVisit) > 0:
        currDist, currNode, parent = heapq.heappop(toVisit)

        if currDist < distances[currNode]:
            distances[currNode] = currDist
            parents[currNode] = parent
            for neighbor, weight in graph[currNode].items():
                    heapq.heappush(toVisit, (weight + currDist, neighbor, currNode))
    return distances, reconstructPath(parents, startNode)

def reconstructPath(parents, startNode):
    paths = {}
    for node, parent in parents.items():
        if node == startNode or parent == None:
            continue
        
        path = []
        currNode = node
        while currNode != None:
            path.append(currNode)
            currNode = parents[currNode]
        paths[node] = list(reversed(path))
    return paths

def testSingleSourceDijkstraWithPaths():
    graph = {
        'S': {'A': 1, 'C': 5},
        'A': {'B': 2},
        'B': {'C': 1, 'D': 5},
        'C': {'D': 3},
        'D': {},
        'E': {'D': 2}
    }
    expectedPath = {
        'A': ['S', 'A'],
        'B': ['S', 'A', 'B'],
        'C': ['S', 'A', 'B', 'C'],
        'D': ['S', 'A', 'B', 'C', 'D']
    }
    dist, path = singleSourceShortestPathWithReconstruction(graph, 'S')
    assert(path == expectedPath)

    graph = {
        'A': {'B': 4, 'C': 2},
        'B': {'C': 5, 'D': 10},
        'C': {'E': 3},
        'D': {},
        'E': {'D': 4}
    }
    expectedPath = {
        'B': ['A', 'B'],
        'C': ['A', 'C'],
        'D': ['A', 'C', 'E', 'D'],
        'E': ['A', 'C', 'E']
    }
    dist, path = singleSourceShortestPathWithReconstruction(graph, 'A')
    assert(path == expectedPath)

    graph = {
        '1': {'2': 7, '3': 9, '6': 14},
        '2': {'3': 10, '4': 15},
        '3': {'4': 11, '6': 2},
        '4': {'5': 6},
        '5': {},
        '6': {'5': 9}
    }
    expectedPath = {
        '2': ['1', '2'],
        '3': ['1', '3'],
        '4': ['1', '3', '4'],
        '5': ['1', '3', '6', '5'],
        '6': ['1', '3', '6']
    }
    dist, path = singleSourceShortestPathWithReconstruction(graph, '1')
    assert(path == expectedPath)

def allShortestPaths(graph, startNode, endNode):
    distances = { }
    parents = {node : set() for node in graph}
    toVisit = [(0, startNode, None)]

    while len(toVisit) > 0:
        currDist, currNode, parent = heapq.heappop(toVisit)

        if currNode not in distances or currDist < distances[currNode]:
            distances[currNode] = currDist
            parents[currNode] = {parent}
            for neighbor, weight in graph[currNode].items():
                if neighbor not in distances:
                    heapq.heappush(toVisit, (currDist + weight, neighbor, currNode))
        
        elif currDist == distances[currNode]:
            parents[currNode].add(parent)
        
    return reconstructPaths(parents, startNode, endNode)

def reconstructPaths(parents, startNode, endNode):
    if startNode == endNode:
        return [[startNode]]
    else:
        paths = []
        for parent in parents[endNode]:
            parentalPaths = reconstructPaths(parents, startNode, parent)
            for parentalPath in parentalPaths:
                paths.append(parentalPath + [endNode])
        return paths

def testAllShortestPaths():
    graph = {
        'A' : {'B' : 7, 'C' : 4, 'D' : 5},
        'B' : {'E' : 2},
        'C' : {'D' : 1, 'E' : 5},
        'D' : {'B' : 3, 'E' : 4},
        'E' : {}
    }
    resAE = [['A', 'B', 'E'], ['A', 'C', 'D', 'E'], ['A', 'C', 'E'], ['A', 'D', 'E']]
    assert(sorted(allShortestPaths(graph, 'A', 'E')) == resAE)
    
    resAC = [['A', 'C']]
    assert(sorted(allShortestPaths(graph, 'A', 'C')) == resAC)
    
    resAD = [['A', 'C', 'D'], ['A', 'D']]
    assert(sorted(allShortestPaths(graph, 'A', 'D')) == resAD)
    
    resCE = [['C', 'D', 'E'], ['C', 'E']]
    assert(sorted(allShortestPaths(graph, 'C', 'E')) == resCE)
    
    graph = {
        'X': {'Y': 1, 'Z': 1},
        'Y': {'S': 1, 'Z': 0},
        'Z': {'S': 1, 'Y': 0},
        'S': {'T': 1},
        'T': {}
    }
    resXT = [
        ['X', 'Y', 'S', 'T'],
        ['X', 'Z', 'S', 'T'],
        ['X', 'Y', 'Z', 'S', 'T'],
        ['X', 'Z', 'Y', 'S', 'T'],
    ]
    assert((sorted(allShortestPaths(graph, 'X', 'T')) == sorted(resXT)) == False)

################################################################################
# Algorithm Name: BellmanFord
# 
# Get distances from source to every node if no negative weight cycles
# Or return None if there are negative weight cycles
################################################################################
def relaxEdge(graph, distances):
    changed = False
    for u, neighbors in graph.items():
        for v, weight in neighbors.items():
            if distances[u] + weight < distances[v]:
                distances[v] = distances[u] + weight
                changed = True
    return changed

def bellmanFord(graph, startNode):
    n = len(graph)
    distances = {node : float('inf') for node in graph}
    distances[startNode] = 0

    for _ in range(n - 1):
        relaxEdge(graph, distances)
    
    if relaxEdge(graph, distances):
        return None
    
    return distances

def testBellmanFord(): 
    # Graph with negative cycles
    graph = {
        'A' : {'B' : 2, 'C' : 1},
        'B' : {'E' : -3},
        'C' : {'A' : 4, 'D' : -8},
        'D' : {'A' : 7, 'E' : 5},
        'E' : {'C' : 2}
    }
    assert(bellmanFord(graph, 'A') == None)

    # Make sure it still works on old graph
    graph = {
        'A' : {'B' : 2, 'C' : 1},
        'B' : {'E' : -3},
        'C' : {'A' : 4, 'D' : -7},
        'D' : {'A' : 7, 'E' : 5},
        'E' : {'C' : 3}
    }
    assert(bellmanFord(graph, 'A') == {'B': 2, 'D': -6, 'A': 0, 'C': 1, 'E': -1})

def main():
    # Prefix Algorithm
    testAveragePrices()
    testCountSublists()
    testProductExceptSelf()
    testQueryProducts()
    testBalanceIndex()

    # Monotonic Stack Algorithm
    testNextGreaterElement()
    testDailyTemperatures()
    testStockSpan()

    # kLargest / kSmallest 
    testFindKthLargest()
    testTopKFrequent()
    testKSmallestPairs()

    # Minimum Completion Time Algorithm
    testFastestPizzaProduction()
    testMinMeetingRooms()
    testFastestGradingTime()

    testLeastInterval()

    testPowerSet()

    testDFSSearch()
    testDFSTraversal()
    testCitiesVisited()
    testMaxBranchSum()

    testIterativeDFS()
    testBFS()
    testIsComplete()

    testHappyMatching()
    testSolveMiniSudoku()
    testKnightsTour()

    testSingleSourceDijkstra()
    testSingleDestinationDijkstra()
    testSinglePairDijkstra()

    testSingleSourceDijkstraWithPaths()
    testAllShortestPaths()

    testBellmanFord()
    print("Passed sample test cases!")



main()


