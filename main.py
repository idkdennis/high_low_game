import random
from art import logo, vs
from gamedata import data

score = 0
winner = random.randint(0, 50)

while True:
    print(logo)

    b = random.randint(0, 50)
    while b == winner:
        b = random.randint(0, 50)

    print(
        f"Compare A: {data[winner]['name']} a "
        f"{data[winner]['description']} "
        f"from {data[winner]['country']}"
    )

    print(vs)

    print(
        f"Against B: {data[b]['name']} a "
        f"{data[b]['description']} "
        f"from {data[b]['country']}"
    )

    choice = input("Who has more followers? Type 'A' or 'B': ").lower()

    c = data[winner]['follower_count']
    d = data[b]['follower_count']

    def checker(c, d):
        if c > d:
            return "a"
        elif c < d:
            return "b"

    t = checker(c, d)

    if choice == t:
        if t == 'b':
            winner = b
        score += 1
        print("\n" * 50)
        print(f"your score is :{score}")
    else:
        print("wrong answer")
        print(f"your score is :{score}")
        break
