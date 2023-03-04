import random


def playere():
    try:
        player_choice = []
        while len(set(player_choice)) < 6:
            player = int(input("Podaj liczby "))
            if 0 < player < 50:
                player_choice.append(player)
        print(f'Your numbers: {sorted(set(player_choice))}')
        return player_choice
    except ValueError:
        print("Enter a number!")
        return playere()


def lotto():
    l = [i for i in range(1, 49)]
    random.shuffle(l)
    ltt = l[1: 7]
    x = set(playere()) & set(ltt)
    y = len(x)
    if len(x) < 3:
        return f"""You guessed {y} numbers
        Winning numbers were: {sorted(ltt)}"""
    elif len(x) >= 3:
        return f"Congratulations! You guessed {y} numbers!" \
               f"The winning numbers: {sorted(ltt)}"


print(lotto())
