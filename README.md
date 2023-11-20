# Fast Math Game

This Python script is a fast-paced math game where the user needs to solve a series of random arithmetic operations quickly. The game has three difficulty levels: beginner, medium, and advanced.

## Initialization

```python
import random as ra

class fast_math:
    def __init__(self, level=None):
        self.list_operations = list("+-/%*")
        self.point = 0
        self.level = level
        self.question = ""
        print(f"Game is Starting \nDifficulty: {self.level}\nPoint: {self.point}\n")
        self.start_game()
```

## Methods

### `start_game()`

```python
def start_game(self):
    if self.level == "beginner":
        for i in range(10):
            self.game_loop(range_size=5)
    elif self.level == "medium":
        for i in range(10):
            self.game_loop(range_size=7)
    else:
        for i in range(10):
            self.game_loop(range_size=9)
```

### `game_loop(range_size)`

```python
def game_loop(self, range_size=None):
    while True:
        for i in range(range_size):
            self.operation(sayi=i)
            
        self.question += "==?"
        print(self.question)
        
        user_input = input("What is the result of the operations: ")
        
        self.question = self.question.replace("?", user_input)
        
        print(self.question)
        
        result = eval(self.question)
        
        if result:
            self.point += 10
            print("10 points earned, Total Point:", self.point, "\n")
            self.question = ""
            break
        else:
            self.point -= 10
            print("10 points lost, Total Points:", self.point, "\n")
            self.question = ""
            break
```

### `operation(sayi)`

```python
def operation(self, sayi):
    if sayi % 2 == 0:
        self.question += str(ra.randint(0, 15))
    elif sayi % 2 == 1:
        self.question += ra.choice(self.list_operations)
```

## Usage

```python
# Example usage
game = fast_math(level="beginner")
```

The script initializes a `fast_math` class instance with a specified difficulty level and starts the game. The user is prompted to solve a series of random arithmetic operations within a time limit to earn points. The difficulty level determines the range of numbers and operations involved in each round.
