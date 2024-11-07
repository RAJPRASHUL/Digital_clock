import random
min=1
max=6

def roll_dice():
    roll=random.randint(min,max)
    return roll
   
while True:
    player_num=input("enter the number player between 2-4\n")
    if player_num.isdigit():
        player_num=int(player_num)
        if(2<= player_num <=4 ):
            break
        else:
            ("enter player between 2-4")
    else:
        print("Invalid input")

current_score=0
max_score=50
player_bb= [0]*player_num
while current_score < max_score:
        for player_idx in range(player_num):
                while True:
                        player_ans=input(f"player number {player_idx+1} do you want to roll the dice (Y|N)\t")
                        player_ans=player_ans.lower()
                        if(player_ans=="y"):
                            player_scored = roll_dice()
                            print(f"player score  {player_scored}")
                            
                            if player_scored==1:
                                player_bb[player_idx]=0
                                print("Your score has been converted to ZERO!")
                                break
                            else:
                                player_bb[player_idx]+=player_scored
                                print(f"your current score is {player_bb[player_idx]}")
                                # player_bb[player_idx]+=current_score
                                if player_bb[player_idx] >=50:
                                    print(f"Player {player_idx+1} has won the match")
                                    exit(0)
                                    
                        elif player_ans == "n":
                           break
                        else:
                           print("Invalid input. Please enter Y or N.")