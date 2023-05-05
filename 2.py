def players_repr(players):
    players_sorted = sorted(players, key=lambda d: d["name"])
    for player in players_sorted:
        print(f"{player['name']=}, {player['age']=}, {player['number']=}")
        print("-" * 90)
    print()


def players_add(players):
    while True:
        player_new = dict()
        player_new.update(
            name=input("Enter the name: "),
            age=int(input("Enter the age: ")),
            number=int(input("Enter the number: ")),
        )
        players.append(player_new)
        players_repr(players)
        break


def players_del(players, find_name):
    players = list(filter(lambda i: i["name"] != find_name, players))
    players_repr(players)


def players_find(key, value, players):
    if value.isalpha():
        print([player for player in players if player[key] == value])
    else:
        print([player for player in players if player[key] == int(value)])
    print()


def players_get_by_name(players, find_name):
    print([player for player in players if player["name"] == find_name])
    print()


def main():
    team = [
        {"name": "Petro", "age": 20, "number": 1},
        {"name": "Kateryna", "age": 30, "number": 2},
        {"name": "Mykhailo", "age": 20, "number": 3},
        {"name": "Petro", "age": 25, "number": 4},
    ]
    while True:
        print("Menu: ")
        print("1. Representation")
        print("2. Add")
        print("3. Delete")
        print("4. Find")
        print("5. Get by name")
        print("-" * 50)
        print("0. Exit")
        print()
        choice = list(range(6))
        if not (user_input := int(input(f"Enter number menu {choice}: "))):
            break
        if user_input == 1:
            players_repr(team)

        if user_input == 2:
            players_add(team)

        if user_input == 3:
            players_del(team, input("Enter the name to delete: "))
        if user_input == 4:
            players_find(
                input("Enter the parameter (name, age or number): "),
                input("Enter value of param(f.e. Peter or 20): "),
                team,
            )
        if user_input == 5:
            players_get_by_name(team, input("Enter the name to find: "))
        if user_input == 0:
            break


if __name__ == "__main__":
    main()
