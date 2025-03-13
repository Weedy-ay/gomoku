from src.rendering.Board import Board


class Model:
    def __init__(self, size: int = 15):
        self._board = Board(size)

    def piece(self, x: int, y: int) -> int:
        """Return the current piece at (x, y).

        Args:
            x: X-coordinate (0-based index), must satisfy 0 <= x < size
            y: Y-coordinate (0-based index), must satisfy 0 <= y < size

        Returns:
            0 for empty, 1 for black piece, or 2 for white piece.

        Raises:
            IndexError: if coordinates are out of bounds.
        """
        raise NotImplementedError

    def size(self):
        """Get the edge length of the board.

        Returns:
            The board's size as a positive integer.
        """
        raise NotImplementedError

    def clear(self):
        """Reset the entire board to empty state.

        All positions will be set to 0.
        """
        raise NotImplementedError

    def add_piece(self, x: int, y: int, piece: int) -> None:
        """Place a piece at specified coordinates.

        Args:
            x: X-coordinate (0-based), 0 <= x < size
            y: Y-coordinate (0-based), 0 <= y < size
            piece: 1 for black, 2 for white

        Raises:
            ValueError: If coordinates are invalid or position is occupied.
        """
        raise NotImplementedError

    def game_over(self):
        """Return Ture if the game is over (there is a winner or
        there are no more empty places on the board).
        """
        raise NotImplementedError

    def get_board(self):
        """Return the current board."""
        raise NotImplementedError

    def empty_space_exists(self):
        """Return true if there is at least one empty space on the board."""
        raise NotImplementedError

    def winner(self):
        """Return 0 if there is no winner.
        Otherwise, return 1 for the winning of black, or 2 for the winning of white.
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
