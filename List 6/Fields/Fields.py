from jutge import read

def find_growings(field):
    m = len(field)
    n = len(field[0])

    # Initialize visited array to keep track of visited areas
    visited = [[False] * n for _ in range(m)]

    def is_valid_area(row, col):
        # Check if the area is within the field boundaries
        return 0 <= row < m and 0 <= col < n

    def explore_growing(row, col):
        # Mark the current area as visited
        visited[row][col] = True

        # Explore adjacent areas
        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        for dx, dy in directions:
            new_row = row + dx
            new_col = col + dy

            if is_valid_area(new_row, new_col) and not visited[new_row][new_col] and field[new_row][new_col] != 0:
                explore_growing(new_row, new_col)

    count = 0
    for i in range(m):
        for j in range(n):
            if field[i][j] != 0 and not visited[i][j]:
                explore_growing(i, j)
                count += 1

    return count


while True:
    try:
        m = read(int)
        n = read(int)

        field = []
        for _ in range(m):
            row = read(list)
            field.append(row)

        num_growings = find_growings(field)
        print(num_growings)

    except EOFError:
        break
