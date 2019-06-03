import sys

user1 = input("Enter your name:")
user2 = input("and your name:")

u1_ans = input("%s choose Rock/Paper/Scissors ?" % user1)
u2_ans = input("%s choose Rock/Paper/Scissors ?" % user2)


game_die = {'rock':1, 'paper':2, 'scissors':3}

print(u1_ans, u2_ans)
print(game_die.get(str(u1_ans).lower ), game_die.get(str(u2_ans).lower))

def compare(u1, u2):
    if u1 == u2:
        return("It's a TIE.")
    elif u1 == 'rock':
        if u2 == 'sicissors':
            return("Rock Wins.")
        else:
            return("Paper Wins.")
    elif u1 == 'scissors':
        if u2 == 'paper':
            return('Scissors Wins.')
        else:
            return("Rock Wins.")
    elif u1 == 'paper':
        if u2 == 'rock':
            return("Paper wins.")
        else:
            return("Sessiors Wins.")
    else:
        return("Invalid Inpur.")

print(compare(u1_ans, u2_ans))

