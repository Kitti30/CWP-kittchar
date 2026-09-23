def checkmate(board):
    rows = board.splitlines()

    if len(rows) == 0:
        print("Error: Board is empty.")
        return

    size = len(rows)

    for row in rows:
        if len(row) != size:
            print("Error: Board must be a square.")
            return

    for row in rows:
        for piece in row:
            if piece not in ".KQRPB":
                print("Error: Invalid character on board.")
                return

    king_row = -1
    king_col = -1
    king_count = 0

    for r in range(size):
        for c in range(size):
            if rows[r][c] == "K":
                king_row = r
                king_col = c
                king_count += 1

    if king_count == 0:
        print("Error: Board must contain one King.")
        return
    if king_count > 1:
        print("Error: Board must contain only one King.")
        return

    pawn_row = king_row + 1

    if pawn_row < size:
        if king_col - 1 >= 0:
            if rows[pawn_row][king_col - 1] == "P":
                print("Success")
                return
        if king_col + 1 < size:
            if rows[pawn_row][king_col + 1] == "P":
                print("Success")
                return

    bishop_directions = [
        (-1, -1),
        (-1, 1),
        (1, -1),
        (1, 1)
    ]

    for dr, dc in bishop_directions:
        r = king_row + dr
        c = king_col + dc

        while 0 <= r < size and 0 <= c < size:
            piece = rows[r][c]
            if piece != ".":
                if piece == "B" or piece == "Q":
                    print("Success")
                    return
                break

            r += dr
            c += dc

    rook_directions = [
        (-1, 0),
        (1, 0),
        (0, -1),
        (0, 1)
    ]

    for dr, dc in rook_directions:
        r = king_row + dr
        c = king_col + dc

        while 0 <= r < size and 0 <= c < size:
            piece = rows[r][c]
            if piece != ".":
                if piece == "R" or piece == "Q":
                    print("Success")
                    return
                break

            r += dr
            c += dc

    print("Fail")