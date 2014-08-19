
MEMOIR
######

2014-2015 MS in Computer Science : Optimization and Algorithms

Sorting under Partial Information in the Decision Tree Model (SUPI)


 > spec : 2013-2014 MEMOF403 course spec
 > code : implementation of encountered algorithms





PREVIOUS NOTES
######


[http://web.stanford.edu/~pmcmahon/ThesisWritingTips.pdf]
[http://arxiv.org/pdf/quant-ph/0412143v2.pdf]
[http://arxiv.org/pdf/quant-ph/0305025v1.pdf]


  - Average Case Analysis of the Merging Algorithm of Hwang and Lin 

    - \log_2 { n + m \choose n }, worst case -> n = m \log_2 { 2n \choose n } \log_2 \frac{2n!}{n!^2} O(n) (~2n) 
    - idea : interchange the role of the lists during computation (for random lists it's likely to happen only during the last steps of the computation) 
    - poll the array at app. \frac{m-j}{n-i} intervals 
    - O(n * log(m/n)) comp ? 
    - E ?

  - Making Octants Colorful and Related Covering Decomposition Problems 

    - translate of a negative octant? 
    - k colors, a family of convex bodies, every coloration of points can be colored s.t. any body of the family containing at least p(k) points contains at keast one of each color 
    - duals + corollaries 
    - here p(k) = k^a where a <6 
    - online / semi-online not applicable


  - On Generalized Comparison-Based Sorting Problems (alpha) 

    - sorting to and from a partial order 
    - partial order identification (open) 
    - sorting with forbidden comparisons (open) 
    - entropy :amount of information and uncertainty 
    - approximating the entropy : greedy (anti-)chain decompositions 
    - partial order production --> multiple selection 
    - sorting under partial information --> multiple merging 
    - page 8 downsets ??

  - Planning and Coding of Problems for an Electronic Computing Instrument Part II Volume II (April 1948)

  - The Clique Problem in Ray intersection Graphs 

  - Two Probabilistics Results on Merging 

    - 1.618 < \frac{m}{n} \le 3 
    - idea : randomly chose between the two next elements of A to be compared with the current to-be-inserted element from B