from typing import List

board = [
    "......................",
    "......##########......",
    "......#........#......",
    "......#........#......",
    "......#........#####..",
    "....###............#..",
    "....#............###..",
    "....##############....",
]


def flood_fill(input_board: List[str], old: str, new: str, x: int, y: int) -> List[str]:
    """Returns board with old values replaced with new values
    through flood filling starting from the coordinates x, y
    Args:
        input_board (List[str])
        old (str): Value to be replaced
        new (str): Value that replaces the old
        x (int): X-coordinate of the flood start point
        y (int): Y-coordinate of the flood start point
    Returns:
        List[str]: Modified board
    """

    # Implement your code here.
    m = len(input_board)
    n = len(input_board[0])

    if x >= m or y >= n:
        return []

    output_board = input_board[:]

    def dfs(cr_x: int, cr_y: int):
        if output_board[cr_x][cr_y] == old:
            output_board[cr_x] = output_board[cr_x][:cr_y] + new + output_board[cr_x][cr_y + 1:]

            # S0 detailed, cool job
            if cr_x < m - 1:  # check the boundary correctness
                dfs(cr_x + 1, cr_y)

            if cr_y < n - 1:
                dfs(cr_x, cr_y + 1)

            if cr_x > 0:
                dfs(cr_x - 1, cr_y)

            if cr_y > 0:
                dfs(cr_x, cr_y - 1)

        else:
            return

    dfs(x, y)

    return output_board


modified_board = flood_fill(input_board=board, old=".", new="~", x=5, y=12)

for a in modified_board:
    print(a)

# Expected output:
# ......................
# ......##########......
# ......#~~~~~~~~#......
# ......#~~~~~~~~#......
# ......#~~~~~~~~#####..
# ....###~~~~~~~~~~~~#..
# ....#~~~~~~~~~~~~###..
# ....##############....
