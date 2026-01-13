from labyrinth_game.constants import ROOMS


def describe_current_room(game_state: dict) -> None:
    room_name = game_state["current_room"]
    room = ROOMS[room_name]

    print(f"\n== {room_name.upper()} ==")
    print(room["description"])

    items = room.get("items", [])
    if items:
        print("Вы видите предметы:", ", ".join(items))
    else:
        print("Здесь нет видимых предметов.")

    exits = room.get("exits", {})
    if exits:
        print("Выходы:", ", ".join(exits.keys()))
    else:
        print("Выходов нет.")

    if room.get("puzzle"):
        print("Здесь есть загадка. Используйте команду: solve")
