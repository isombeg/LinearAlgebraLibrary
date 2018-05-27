from main_lib import *

m1_a = Matrix(['1 0 0', '0 1 0', '0 0 1'])
m1_b = Matrix(['1 0 0', '0 1 0', '0 0 0']) #Doesn't work
m1_c = Matrix(['0 1 0', '0 0 1', '0 0 0']) #Doesn't work
m1_d = Matrix(['1 0 3 1', '0 1 2 4'])
m1_e = Matrix(['1 2 0 3 0', '0 0 1 1 0', '0 0 0 0 1'])
m1_f = Matrix(['0 0', '0 0', '0 0'])
m1_g = Matrix([' 1 -7 5 5', '0 1 3 2'])

m2_a = Matrix(['1 1 2 8', '-1 -2 3 1', '3 -7 4 10'])
m2_b = Matrix(['2 2 2 0', '-2 5 2 1', '8 1 4 -1'])
m2_c = Matrix(['1 -1 2 -1 -1', '2 1 -2 -2 -2', '-1 2 -4 1 1', '-3 0 0 -3 -3'])
m2_d = Matrix(['0 -2 3 1', '3 6 -3 -2', '6 6 3 5'])

'''
Testcase 1a: rref_check(m1_a,m1_b,m1_c,m1_d,m1_e,m1_f,m1_g)
Expected output: [True, True, True, True, True, True, False]
Real Output: TypeError: '<' not supported between instances of 'NoneType' and 'bool'

Problem: Function can't determine if a matrix is row reduced if there's a row vector with all zeroes
Solution: condList.append(leadingOneCheck(row)) -> condList.append(leadingOneCheck(row) or fullZeroCheck(row))


Testcase 1b: rref_check(m1_a,m1_b,m1_c,m1_d,m1_e,m1_f,m1_g)
Expected output: [True, True, True, True, True, True, False]
Real Output: [True, True, True, False, False, True, False]

Problem: When a matrix has a column vector that has a 1 in it but it's not a leading 1, algorithm concluded it's not in rref automatically
Solution: Added code that ignores column vectors that need not to be looked at


Testcase 1c: rref_check(m1_a,m1_b,m1_c,m1_d,m1_e,m1_f,m1_g)
Expected output: [True, True, True, True, True, True, False]
Real Output: [True, True, True, True, True, True, False]


Testcase 2.1: rref(m2_a)
Expected output: Matrix(['1 0 0 3', '0 1 0 1', '0 0 1 2'])
Real Output: Matrix(['1 0 0 3', '0 1 0 1', '0 0 1 2'])

Testcase 2.2: rref(m2_b)
Expected output: Matrix(['1 0 -0.4285714286 -0.1428571429', '0 1 0.5714285714 -0.1428571429'])
Real Output: IndexError: list index out of range

Testcase 2.1: rref(m2_c):
Expected output: Matrix(['1 -1 2 -1 -1', ' 0 1 -2 0 0', '0 0 0 0 0', '0 0 0 0 0'])
Real Output: Never ended

Testcase 2.1: rref(m2_d):
Expected output: Matrix(['1 1 0.5 0.83333333', '0 1 -1.5 -1.5', '0 0 0 -2'])
Real Output: IndexError: list index out of range

Notes for rref:
    - Incapable of solving a system where there is a trivial solution
'''

printMtrx(rref(m2_d))
