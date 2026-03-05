
events=["squad_wipe","sniper_kill","vehicle_explosion","clutch_win"]

def detect():
 import random
 return random.choice(events)

if __name__=="__main__":
 print(detect())
