#Ex.1.)
from __future__ import division
DNA ="ACTGATCGATTACGTATAGTATTTGCTATCATACATATATATCGATGCGTTCAT"
A_Count = DNA.count('A')
print(A_Count)
T_Count = DNA.count('T')
print(T_Count)
AT_Count = A_Count + T_Count
print(AT_Count)
AT_Count / len(DNA)
