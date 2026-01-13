from labyrinth_game.constants import ROOMS


def describe_current_room(game_state: dict) -> None:
    room_name = game_state["current_room"]
    room = ROOMS[room_name]
    print(f"\n== {room_name.upper()} ==")
    print(room["description"])
