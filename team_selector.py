import random

players = ['Cameron', 'Michelle', 'Harley',
           'Sue', 'Charles', 'Finn', 'Jake',
           'Anthony', 'Carl', 'David', 'Frances',
           'Jeffrey', 'Taylor', 'PooperPants', 'SpongeBob',
           'Patrick', 'Gary', 'Sandy', 'Squidward', 'Mr.Krabs']
print("\nWelcome to Team Allocator!")

while True:
    random.shuffle(players)
    response = input("Is it a team or individual sport? \
                     \nType 'team' or 'individual': ")
    if response == 'team':

        team1 = players[:len(players)//3]
        print("\nTeam 1 Captain: " + random.choice(team1))
        print("\nTeam: 1")
        for player in team1:
            print(player)

        team2 = players[len(players)//3:(len(players)//3)*2]
        print("\nTeam 2 Captain: " + random.choice(team2))
        print("\nTeam 2: ")
        for player in team2:
            print(player)

        team3 = players[(len(players)//3)*2:]
        print("\nTeam 3 Captain: " + random.choice(team3))
        print("\nTeam 3: ")
        for player in team3:
            print(player)

        response = input("\nAre you okay with these selections? Type 'y' or 'n': ")
        if response == "y":
            break
    else:
        for i in range(0, 20, 2):
            print(players[i] + " vs " + players[i + 1])
            start = random.randrange(i, i + 2)
            print(players[start] + " starts")
