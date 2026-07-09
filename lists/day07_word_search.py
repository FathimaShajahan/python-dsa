def exist(board, word):
    if not board or not board[0]:
        return False

    rows = len(board)
    cols = len(board[0])

    def dfs(r, c, index):
        # Entire word matched
        if index == len(word):
            return True

        # Boundary check and character check
        if (
            r < 0 or r >= rows or
            c < 0 or c >= cols or
            board[r][c] != word[index]
        ):
            return False

        # Mark current cell as visited
        temp = board[r][c]
        board[r][c] = "#"

        # Search in four directions
        found = (
            dfs(r + 1, c, index + 1) or
            dfs(r - 1, c, index + 1) or
            dfs(r, c + 1, index + 1) or
            dfs(r, c - 1, index + 1)
        )

        # Backtrack
        board[r][c] = temp

        return found

    # Try every cell as the starting point
    for r in range(rows):
        for c in range(cols):
            if dfs(r, c, 0):
                return True

    return False


# ------------------- MAIN PROGRAM -------------------

while True:
    try:
        rows = int(input("Enter number of rows: "))
        cols = int(input("Enter number of columns: "))

        if rows <= 0 or cols <= 0:
            print("Rows and columns must be greater than 0.\n")
            continue
        break

    except ValueError:
        print("Please enter valid integers.\n")


board = []

print("\nEnter the board row by row (space-separated):")

for i in range(rows):
    while True:
        row = input(f"Row {i + 1}: ").split()

        if len(row) != cols:
            print(f"❌ Error: Please enter exactly {cols} characters.")
        else:
            board.append(row)
            break


while True:
    word = input("\nEnter word: ").strip()

    if word == "":
        print("❌ Word cannot be empty.")
    else:
        break


print("\nBoard:")
for row in board:
    print(" ".join(row))

print("\nWord:", word)

print("\nOutput:", exist(board, word))