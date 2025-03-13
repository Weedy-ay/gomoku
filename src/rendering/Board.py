import copy


class Board:
    """Represents a game board for piece placement.

    The board is a square grid of specified size, where positions can be
    occupied by black pieces (1), white pieces (2), or be empty (0).

    Attributes:
        _size: The edge length of the square board, defaulting to 15.
    """

    def __init__(self, size: int = 15, given_board: bool = False, board: list = None):
        """Initialize a Gomoku board with specified size or a provided board configuration.

        The board is represented by a 2D list where:
        - 0 represents an empty position
        - 1 represents a black stone
        - 2 represents a white stone

        Args:
            size (int, optional): Edge length of the square board. Must be a positive integer.
                Defaults to 15. Ignored if `given_board` is True.
            given_board (bool, optional): Flag to indicate whether to use a custom board.
                When True, the `board` parameter must be provided. Defaults to False.
            board (list, optional): A square 2D list representing a pre-configured board.
                Required when `given_board` is True. Each row must have the same length as
                the board size. The provided board will be deep copied to prevent external
                modifications. This is primarily for debugging purposes.

        Raises:
            ValueError: If provided parameters are invalid:
                - `size` is not a positive integer (when using default initialization)
                - `board` is not a square 2D list (when using custom board)
                - Row/column lengths mismatch in custom board
                - Invalid stone values (not 0, 1, or 2) in custom board

        Note:
            When using a custom board (`given_board=True`):
            - The board is deep copied to ensure isolation from external modifications
            - The first dimension represents rows (vertical axis), the second represents columns (horizontal axis)
        """
        if given_board:
            # Validate custom board structure
            if not board or not all(len(row) == len(board) for row in board):
                raise ValueError("Invalid custom board - must be a square 2D list")

            # Validate stone values
            valid_values = {0, 1, 2}
            for row in board:
                for val in row:
                    if val not in valid_values:
                        raise ValueError(f"Invalid stone value {val}. Must be 0, 1, or 2")

            self._size = len(board)
            self._pieces = copy.deepcopy(board)
        else:
            # Validate size parameter
            if not isinstance(size, int) or size < 1:
                raise ValueError(f"Invalid board size: {size}. Must be a positive integer")

            self._size = size
            self._pieces = [[0 for _ in range(size)] for _ in range(size)]

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


