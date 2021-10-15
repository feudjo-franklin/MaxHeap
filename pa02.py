class MaxHeap:
    def __init__(self, keys):
        build_max_heapify(keys)
        self.keys = keys

    def maximum(self):
        return self.keys[0]

    def extractMax(self):
        self.keys[0], self.keys[-1] = self.keys[-1], self.keys[0]
        das_max = self.keys.pop()
        max_heapify(self.keys, 0)
        return das_max

    def increaseKey(self,i,k):
        if k < self.keys[i]:
            return "k too small"
        self.keys[i] = k
        while i > 0 and self.keys[i//2 -1 if i%2 == 0 else i//2] < self.keys[i]:
            self.keys[i], self.keys[i//2 -1 if i%2 == 0 else i//2] = self.keys[i//2 -1 if i%2 == 0 else i//2], self.keys[i]
            i = i//2 -1 if i%2 == 0 else i//2

    def insert(self,k):
        self.keys.append(-1)
        n = len(self.keys)-1
        self.increaseKey(n,k)

    def heapSort(self):
        build_max_heapify(self.keys)
        A = []
        n = len(self.keys)-1
        while n > 0:
            self.keys[0], self.keys[n] = self.keys[n], self.keys[0]
            A.insert(0,self.keys.pop())
            n-=1
            max_heapify(self.keys,0)
        A.insert(0,self.keys.pop())
        A.reverse()
        self.keys = A
            
        
        







def max_heapify(A,i):
    l = 2*i+1
    r = 2*i+2
    n = len(A)
    lg = 2*n
    if l < n and A[l] > A[i]:
        lg = l
    else:
        lg = i
    if r < n and A[r] > A[lg]:
        lg = r
    if lg != i:
        A[i], A[lg] = A[lg], A[i]
        max_heapify(A,lg)

def build_max_heapify(A):
    n = len(A)//2 - 1
    for i in range(n,-1,-1):
        max_heapify(A,i)
        
    
