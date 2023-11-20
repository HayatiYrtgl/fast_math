import random as ra


# fast math game
class fast_math:
   # initialize
   def __init__(self, level=None):
       
      # lists
      self.list_operations = list("+-/%*")
      self.point = 0
      self.level = level
      self.question = ""
      # print game is starting
      print(f"Game is Starting \nDiffuculty:{self.level}\nPoint{self.point}\n")
      
      self.start_game()
   
      
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
    
   def game_loop(self, range_size=None):
               
               while True:
                   for i in range(range_size):
                       self.operation(sayi=i)
                       
                   self.question += "==?"
                   print(self.question)
                   
                   # user input
                   user_input = input("what is the result of operations: ")
                   
                   self.question = self.question.replace("?", user_input)
                   
                   print(self.question)
                   
                   result = eval(self.question)
                   # evaluate
                   if result:
                       self.point += 10
                       print("10 points earned, Total Point:", self.point, "\n")
                       self.question = ""
                       break
                   else:
                       self.point -= 10
                       print("10 points losed, Total Points:", self.point, "\n")
                       self.question = ""
                       break
                       
   def operation(self, sayi):
                   if sayi%2 == 0:
                       self.question += str(ra.randint(0, 15))
                   elif sayi%2 == 1:
                       self.question += ra.choice(self.list_operations)
                   

               
   