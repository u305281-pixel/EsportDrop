
import random

teams=["Team Alpha","Team Bravo"]

def predict():
 return {
 "match":f"{teams[0]} vs {teams[1]}",
 "alpha_win_probability":f"{random.randint(40,70)}%"
 }

if __name__=="__main__":
 print(predict())
