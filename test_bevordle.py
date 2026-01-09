from pa4 import initialize_board, update_board, check_guess


# Board initialization tests

def test_initialize_board_default():
    board = initialize_board()
    assert len(board) == 6, f"Expected 6 rows, got {len(board)}"
    assert len(board[0]) == 5, f"Expected 5 cols, got {len(board[0])}"
    assert all(cell == '_' for row in board for cell in row), "Board not initialized with '_'"

def test_initialize_board_custom():
    board = initialize_board(4, 3)
    assert len(board) == 4, f"Expected 4 rows, got {len(board)}"
    assert len(board[0]) == 3, f"Expected 3 cols, got {len(board[0])}"


# Board update tests

def test_update_board():
    board = initialize_board()
    feedback = ['A', 'B', 'C', 'D', 'E']
    update_board(board, 1, feedback)
    assert board[1] == feedback, f"Row 1 should be {feedback}, got {board[1]}"


# Guess checking tests

def test_check_guess_all_green():
    keyboard = {letter: 'white' for letter in "ABCDEFGHIJKLMNOPQRSTUVWXYZ"}
    _, emojis = check_guess("APPLE", "APPLE", keyboard)
    assert emojis == ['🟩','🟩','🟩','🟩','🟩'], f"Expected all green, got {emojis}"
    for letter in "APPLE":
        assert keyboard[letter] == 'green', f"Expected {letter} to be green"

def test_check_guess_mixed_feedback():
    keyboard = {letter: 'white' for letter in "ABCDEFGHIJKLMNOPQRSTUVWXYZ"}
    _, emojis = check_guess("APPLE", "PLEAS", keyboard)
    assert emojis == ['🟨','🟨','🟨','🟨','⬜'], f"Expected mixed feedback, got {emojis}"
    assert keyboard['P'] == 'yellow', f"P should be yellow, got {keyboard['P']}"
    assert keyboard['L'] == 'yellow', f"L should be yellow, got {keyboard['L']}"
    assert keyboard['E'] == 'yellow', f"E should be yellow, got {keyboard['E']}"
    assert keyboard['A'] == 'yellow', f"A should be yellow, got {keyboard['A']}"
    assert keyboard['S'] == 'grey', f"S should be grey, got {keyboard['S']}"


# Run all tests manually

if __name__ == "__main__":
    test_initialize_board_default()
    test_initialize_board_custom()
    test_update_board()
    test_check_guess_all_green()
    test_check_guess_mixed_feedback()
    print("All tests passed!")
