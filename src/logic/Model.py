from src.rendering.Board import Board


class Model:
    def __init__(self, size: int = 15):
        self._board = Board(size)
        self.game_over = False
        self.winner = 0

    def piece(self, x: int, y: int) -> int:
        """Return the current piece at (x, y).

        Args:
            x: X-coordinate (0-based index), must satisfy 0 <= x < size
            y: Y-coordinate (0-based index), must satisfy 0 <= y < size

        Returns:
            0 for empty, 1 for black piece, or 2 for white piece.

        Raises:
            ValueError: if coordinates are out of bounds.
        """
        return self._board.piece(x, y)

    def size(self):
        """Get the edge length of the board.

        Returns:
            The board's size as a positive integer.
        """
        return self._board.size()

    def clear(self):
        """Reset the entire board to empty state.

        All positions will be set to 0.
        """
        self._board.clear()

    def add_piece(self, x: int, y: int, piece: int) -> None:
        """If the game is not over, place a piece at specified coordinates.
        Then check whether there is a winner and whether the game is over.

        Args:
            x: X-coordinate (0-based), 0 <= x < size
            y: Y-coordinate (0-based), 0 <= y < size
            piece: 1 for black, 2 for white

        Raises:
            ValueError: If coordinates are invalid or position is occupied.
        """
        if not self.game_over:
            self._board.add_piece(x, y, piece)
            self.winner = self.is_winner(x, y)
            self.empty_space_exists()

    def get_board(self) -> Board:
        """Return the current board."""
        return self._board

    def empty_space_exists(self):
        """Return true and change the attribute 'game_over' to True
        if there is at least one empty space on the board.
        """
        for i in range(self.size()):
            for j in range(self.size()):
                if self.piece(i, j) == 0:
                    return True
        self.game_over = True
        return False

    def is_winner(self, x: int, y: int):
        """Return 0 if there is no winner at coordinate (x, y).
        Otherwise, return 1 for the winning of black, or 2 for the winning of white.
        Then change the attribute 'game_over' to True.
        """
        raise NotImplementedError

    def __str__(self):
        """Generate human-readable string representation of the board.

        Example format:
            - '*' for black pieces (1)
            - '0' for white pieces (2)
            - ' ' for empty positions (0)

        Returns:
            Multi-line string visualizing the board state.
        """
        return self._board.__str__()
