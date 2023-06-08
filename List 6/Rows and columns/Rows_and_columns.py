from easyinput import read, read_line

rows = read(int)
columns = read(int)

matrix = []

for i in range(0, rows) :
    row = []
    for j in range(0, columns) :
        num = read(str)
        row.append(num)
    matrix.append(row)

line = read_line(skip_empty=True)


while line is not None:
    lSplit = line.split()
    if lSplit[0] == "row" :
        r = int(lSplit[1])
        print("row ", r, ": ", " ".join(matrix[r-1]), sep="")
    elif lSplit[0] == "column":
        c = int(lSplit[1])
        #pillar columna
        col = [row[c-1] for row in matrix]
        print("column ", c, ": ", " ".join(col), sep="")
    elif lSplit[0] == "element" :
        iPos = int(lSplit[1])
        jPos = int(lSplit[2])
        print("element ", iPos, " ", jPos, ": ", matrix[iPos-1][jPos-1], sep="")
    line = read_line(skip_empty=True)
