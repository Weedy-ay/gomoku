class Board:
    """Represents a game board for piece placement.

    The board is a square grid of specified size, where positions can be
    occupied by black pieces (1), white pieces (2), or be empty (0).

    Attributes:
        size: The edge length of the square board, defaulting to 15.
    """

    def __init__(self, size: int = 15):
        """Initialize a square board with all positions empty.

        Args:
            size: Edge length of the board. Must be a positive integer.
        """
        self._size = size
        self._pieces = [[0 for _ in range(size)] for _ in range(size)]  # 0=empty, 1=black, 2=white

    def size(self) -> int:
        """Get the edge length of the board.

        Returns:
            The board's size as a positive integer.
        """
        return self._size

    def piece(self, x: int, y: int) -> int:
        """Get the piece at specified coordinates.

        Args:
            x: X-coordinate (0-based index), must satisfy 0 <= x < size
            y: Y-coordinate (0-based index), must satisfy 0 <= y < size

        Returns:
            0 for empty, 1 for black piece, or 2 for white piece.

        Raises:
            IndexError: If coordinates are out of bounds.
        """
        raise NotImplementedError

    def clear(self) -> None:
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

    def __str__(self) -> str:
        """Generate human-readable string representation.

        Example format:
            - '*' for black pieces (1)
            - '0' for white pieces (2)
            - ' ' for empty positions (0)

        Returns:
            Multi-line string visualizing the board state.
        """
        raise NotImplementedError


