# CMPS 2200 Recitation 6
## Answers

**Name:** Kailen Mitchell


Place all written answers from `recitation-06.md` here for easier grading.



- **d.**

File | Fixed-Length Coding | Huffman Coding | Fixed-Length/Huffman
----------------------------------------------------------------------
f1.txt        |        1340        |       826         | 1.62
alice29.txt   |        1039367     |      676374       | 1.54
asyoulik.txt  |        876253      |      606448       | 1.44
grammar.lsp   |        26047       |      17356        | 1.50
fields.c      |         78050      |      56206        | 1.39

Do you see a consistent trend? If so, what is it?

The ratio is around 1.6-1.4
The ratio seems to be decreasing slightly but that could be a coincidence. 



- **e.**

  For each chracter, the Huffman cost is length of huffman encoding * the frequency of that character
  Since we would get a balanced tree with frequencies that are all the same, the length of the encoding
  would start with 1 and would increase by 1 for each level deep we go into the tree.
  
  From 1 to log(n) is the number of levels
  
  For each level the length of encoding is increasing by 1
  
  For each level the number of nodes is increasing by *2 for each node or 2*d-1 nodes total where d is the depth


  cost = $\Sigma$ (from 1-log(x)) : n * F * 2*(log(n))-1
  
  where x is the number of terms and F is the frequency constant
