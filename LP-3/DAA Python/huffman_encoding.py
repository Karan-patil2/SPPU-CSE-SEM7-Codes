import heapq

class Node:
    def __init__(self, freq, symbol, left=None, right=None):
        self.freq, self.symbol, self.left, self.right = freq, symbol, left, right
    def __lt__(self, other):
        return self.freq < other.freq

def print_codes(node, code=''):
    if not node.left and not node.right:
        print(f"{node.symbol} -> {code}")
        return
    if node.left: print_codes(node.left, code + '0')
    if node.right: print_codes(node.right, code + '1')

chars = ['a', 'b', 'c', 'd', 'e', 'f']
freq = [5, 9, 12, 13, 16, 45]
heap = [Node(freq[i], chars[i]) for i in range(len(chars))]
heapq.heapify(heap)

while len(heap) > 1:
    l, r = heapq.heappop(heap), heapq.heappop(heap)
    heapq.heappush(heap, Node(l.freq + r.freq, l.symbol + r.symbol, l, r))

print_codes(heap[0])
