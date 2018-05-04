#function that'll determine if matrix is adequate
def rowCheck(arr):
    entryCount = len(arr[0].split())
    for row in arr:
        if len(row.split()) != entryCount:
            return False
    return True

# object that forms a matrix from an array of row vectors
class Matrix:
    #constructor
    def __init__(self,arr):
        if rowCheck(arr):
            self.arr = []
            for row in arr:
                self.arr.append(row.split())

            for row in range(0, len(self.arr)):
                for entry in range(0, len(self.arr[row])):
                    self.arr[row][entry] = float(self.arr[row][entry])

        else:
            self.arr = []

    #accessors:
    def getEntry(self, row, column):
        if row > 0 and column > 0:
            return self.arr[row-1][column-1]

    def getRowDim(self):
        return len(self.arr[0])

    def getColDim(self):
        return len(self.arr)

    def getRowVect(self, rowNum):
        if rowNum > 0:
            return self.arr[rowNum-1]

    def getColVect(self, colNum):
        if colNum > 0:
            vectList = []
            for row in self.arr:
                vectList.append(row[colNum-1])
            return vectList

    #mutators:

    def replace(self, row, col, entry): #replaces an entry in the matrix
        self.arr[row-1][col-1] = float(entry)

    def swap(self,rowA,rowB): #elem row opp: row swapping
        self.arr[rowA-1], self.arr[rowB-1] = self.arr[rowB-1], self.arr[rowA-1]

    def mult(self,row,coeff): #elem row opp: multiplying row by a non zero constant
        if coeff != 0:
            for entry in range(0,len(self.arr[row-1])):
                self.arr[row-1][entry] = coeff * self.arr[row-1][entry]

    def addNTimes(self, rowA, rowB, coeff): #elem row opp: adding a multiple of one row to another
        if coeff != 0:
            for entry in range(0, len(self.arr[rowA-1])):
                self.arr[rowA-1][entry] = self.arr[rowA-1][entry] + coeff * self.arr[rowB-1][entry]

def printMtrx(*mtrx): #prints out the matrix
    for mat in list(mtrx):
        for time in range(1,mat.getColDim()+1):
            print(mat.getRowVect(time))
        print('\n')

def genNullMtrx(rowDim, colDim):
    zero = '0 '
    rowStr = ''
    matList = []
    for elem in range(0,rowDim):
        rowStr += zero
    for elem in range(0,colDim):
        matList.append(rowStr)

    return Matrix(matList)

#MATRIX ARITHMETIC
def rowMatch(*mats): #verifies that rows have the same length
    dim = list(mats)[0].getRowDim()
    for mat in list(mats):
        if mat.getRowDim() != dim:
            return False

    return True

def colMatch(*mats): #verifies that columns have the length
    dim = list(mats)[0].getColDim()
    for mat in list(mats):
        if len(mat.getColVect(1)) != dim:
            return False

    return True

def vectSum(*vect):
    vector = []
    for elem in range(0, len(list(vect)[0])):
        sum = 0
        for indVect in list(vect):
            sum += indVect[elem]
        vector.append(sum)

    return vector

def mtrxAdd(*mats):
    if rowMatch(*mats) and colMatch(*mats):
        mtrxRslt = genNullMtrx(list(mats)[0].getRowDim(), list(mats)[0].getColDim())
        for mtrxNum in range(0,len(list(mats))):
            for rowNum in range(0,mtrxRslt.getColDim()):
                mtrxRslt.arr[rowNum] = vectSum(mtrxRslt.arr[rowNum], list(mats)[mtrxNum].arr[rowNum])
    return mtrxRslt

def scalarMult(matrix, coeff):
    for row in range(1, matrix.getColDim()+1):
        matrix.mult(row, coeff)
    print(matrix.arr)
    return matrix

def transpose(matrix):
    vectList = []
    strList = []

    for column in range(1,matrix.getRowDim()+1):
        vectList.append(matrix.getColVect(column))

    for vect in vectList:
        vectStr = ''
        for entry in vect:
            vectStr += (str(entry) + ' ')
        strList.append(vectStr)

    return Matrix(strList)

def matMult(mtrxA, mtrxB): #Will only work with two matrices and will serve as part of a function that can take an infinite amount of matrices
    # #FIX MEEEE!!!! Problem: Some column vectors are 0
    if mtrxA.getRowDim() == mtrxB.getColDim():
        matRslt = genNullMtrx(mtrxA.getColDim(), mtrxB.getRowDim())
        for rowNum in range(1, matRslt.getColDim()+1):
            for colNum in range(1, matRslt.getRowDim()):
                entry = 0
                for entryNum in range(1,mtrxA.getRowDim()+1):
                    entry += (mtrxA.getEntry(rowNum,entryNum) * mtrxB.getEntry(entryNum, colNum)) #slight mistale around here
                matRslt.replace(rowNum, colNum, entry)

    return matRslt

def trace(mtrx):
    if mtrx.getRowDim() == mtrx.getColDim():
        trace = 0
        for i in range(1,mtrx.getRowDim()+1):
            trace += mtrx.getEntry(i,i)
    return trace

def chngPivot(i=1,j=1, i_new = 0, j_new = 0):
    return i + i_new, j + j_new

def entryCheck(mtrx,i,j):
    return mtrx.getEntry(i,j) == 0

def elimPrtcl(mtrx,i,j): #what to do when pivot isn't 0
    rowList = list(range(1,mtrx.getColDim()+1))
    rowList.__delitem__(i-1)
    mtrx.mult(i,1/mtrx.getEntry(i,j))
    for rowNum in rowList:
        mtrx.addNTimes(rowNum,i, - (mtrx.getEntry(rowNum,j)/mtrx.getEntry(i,j)))
    return i+1, j+1

def swapPrtcl(mtrx,i,j): #what to do when pivot is 0
    rowList = list(range(1, mtrx.getColDim() + 1))
    rowList.__delitem__(i - 1)
    for rowNum in rowList:
        if mtrx.getEntry(rowNum,j-1) != 1:
            mtrx.swap(i, rowNum)
        break
    return i,j

def rref(mtrx): #Not done
    i,j = chngPivot()
    entry = mtrx.getEntry(i,j)
    caseSelec = {
        True:swapPrtcl(mtrx,i,j), #CASE 1: Pivot is equal to 0.
        False: elimPrtcl(mtrx,i,j) #CASE 2: Pivot is a non-zero number and elimination protocol is initiated

    }
    i, j = caseSelec[entryCheck(mtrx,i,j)]
