# implementasikan listing koding di bawah ini dengan python
MAX = 100

def luDecomposition(mat, n):
    lower = [[0 for x in range(n)] for y in range(n)]
    upper = [[0 for x in range(n)] for y in range(n)]

    # Decomposing matrix into Upper and Lower triangular matrix
    for i in range(n):
        # Upper Triangular
        for k in range(i, n):
            # Summation of L(i, j) * U(j, k)
            sum = 0
            for j in range(i):
                sum += (lower[i][j] * upper[j][k])

            # Evaluating U(i, k)
            upper[i][k] = mat[i][k] - sum

        # Lower Triangular
        for k in range(i, n):
            if i == k:
                lower[i][i] = 1  # Diagonal as 1
            else:
                # Summation of L(k, j) * U(j, i)
                sum = 0
                for j in range(i):
                    sum += (lower[k][j] * upper[j][i])

                # Evaluating L(k, i)
                lower[k][i] = (mat[k][i] - sum) / upper[i][i]

    # Displaying the result
    print("Lower Triangular\t\tUpper Triangular")
    for i in range(n):
        # Lower
        for j in range(n):
            print(f"{lower[i][j]:.2f}", end="\t")
        print("", end="\t")

        # Upper
        for j in range(n):
            print(f"{upper[i][j]:.2f}", end="\t")
        print("")

# Driver code
mat = [
    [2, -1, -2],
    [-4, 6, 3],
    [-4, -2, 8]
]
luDecomposition(mat, 3)