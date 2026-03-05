
import random

def analyze():
 return {
 "aim_accuracy": random.randint(60,95),
 "reaction_ms": random.randint(180,260),
 "survival_minutes": random.randint(12,28),
 "aggression_score": random.randint(50,90)
 }

if __name__ == "__main__":
 print(analyze())
