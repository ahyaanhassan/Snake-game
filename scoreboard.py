from turtle import Turtle
import time
ALIGNMENT="center"
FONT=("courier",24,"normal")

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score=0
        with open("data.txt") as data:
            self.high_score=int(data.read())
        # self.high_score=0
        self.color("white")
        self.penup()
        self.goto(0,270)
        self.hideturtle()
        self.update_score()
        
        

    def update_score(self):
        self.clear()
        self.write(f"Score: {self.score} High Score: {self.high_score}",align=ALIGNMENT,font=FONT)

    # def game_over(self):
    #     self.goto(0,0)
    #     self.write("GAME OVER",align=ALIGNMENT,font=FONT)

    def reset(self):
        if self.score>self.high_score:
            self.high_score=self.score
            with open('data.txt',"w") as data:
                data.write(f"{self.high_score}")
        self.score=0
        self.update_score()


   
        


    def increase_score(self):
        self.score=self.score+10
        
        self.update_score()


    
        
        