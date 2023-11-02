import math, queue
from collections import Counter

class TreeNode(object):
    # we assume data is a tuple (frequency, character)
    def __init__(self, left=None, right=None, data=None):
        self.left = left
        self.right = right
        self.data = data
    def __lt__(self, other):
        return(self.data < other.data)
    def children(self):
        return((self.left, self.right))
    
def get_frequencies(fname):
    ## This function is done.
    ## Given any file name, this function reads line by line to count the frequency per character. 
    f=open(fname, 'r')
    C = Counter()
    for l in f.readlines():
        C.update(Counter(l))
    return(dict(C.most_common()))

# given a dictionary f mapping characters to frequencies, 
# create a prefix code tree using Huffman's algorithm
def make_huffman_tree(f):
    p = queue.PriorityQueue()
    
    # construct heap from frequencies, the initial items should be
    # the leaves of the final tree
    for c in f.keys():
        p.put(TreeNode(None,None,(f[c], c)))

    # greedily remove the two nodes x and y with lowest frequency,
    # create a new node z with x and y as children,
    # insert z into the priority queue (using an empty character "")
    while (p.qsize() > 1):
        x = p.get()
        y = p.get()
        z = TreeNode(x,y,(x.data[0]+y.data[0],""))
        p.put(z)
        
    # return root of the tree

    return p.get()

"""
Complete the implementation of Huffman coding in
  `make_huffman_tree`. Note that we manipulate binary trees in the
  priority queue using the object `TreeNode`. Moreover, once the tree
  is constructed, we must compute the actual encodings by traversing
  the Huffman tree that has been constructed. To do this, complete the
  implementation of `get_code`, which is a typical recursive binary
  tree traversal. That is, given a tree node, we recursively visit the
  left and right subtrees, appending a `0` or `1` to the encoding in
  each direction as appropriate. If we visit a leaf of the tree (which
  represents a character in the alphabet) we store the
  collected encoding for that character in `code`.

"""

# perform a traversal on the prefix code tree to collect all encodings
def get_code(node, prefix="", code={}):
    if node.left != None:
        get_code(node.left, prefix + "0", code)
    if node.right != None:
        get_code(node.right, prefix + "1", code)
    if node.left == None and node.right == None:
        code[node.data[1]] = prefix
    return code

# given an alphabet and frequencies, compute the cost of a fixed length encoding
def fixed_length_cost(f):
    #  Compute cost for a fixed length encoding for each text file by calling function get_frequencies
    return sum(f.values()) * math.ceil(math.log(len(f),2))
 
# given a Huffman encoding and character frequencies, compute cost of a Huffman encoding
def huffman_cost(C, f):
    cost = 0
    for key in f:
        #f is a dictionary of letters mapped to frequencies
        #C is a distionary of nodes mapped to length of encodings
        cost += f[key] * len(C[key]) #for each item, length of encoding * the frequency of that character
    return cost

f = get_frequencies('fields.c')
print("Fixed-length cost:  %d" % fixed_length_cost(f))
T = make_huffman_tree(f)
C = get_code(T)
print("Huffman cost:  %d" % huffman_cost(C, f))