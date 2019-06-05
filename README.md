# Tic-Tac-Toc-Game-demo
An one time interview question I have met

Requirements

1. implement `draw()` method to output the board
    ```
     | |
    -----
     | |
    -----
     | |
    ```
    to the stdout

2. implement `put(symbol, x, y)`
    Example: `put('X', 1, 2)`, and afterward calling `draw()` should show
    ```
     | |
    -----
    X| |
    -----
     | |
    ```

3. implement `has_won(symbol)`
    Example 1: Given board as
    ```
     | |
    -----
    X| |
    -----
     | |
    ```
    `has_won('X')` should return false

    Example 2: Given board as
    ```
    X| |
    -----
    X| |
    -----
    X| |
    ```
    or any other winning condition, `has_won('X')` should return true

4. implement `is_full()` method that returns whether the board is full of symbols

5. implement `play()` method that running a loop that
    1. allow the human player input the x and y coordinate to put 'X' symbols on the board
    2. let a computer foe to put 'O' symbols on the board
    3. end the game if anyone has won or the board is full.
