from labyrinth_game.constants import ROOMS
from labyrinth_game.utils import describe_current_room


def show_inventory(game_state: dict) -> None:
    inventory = game_state["player_inventory"]
    if inventory:
        print("Инвентарь:", ", ".join(inventory))
    else:
        print("Инвентарь пуст.")


def move_player(game_state: dict, direction: str) -> None:
    current_room = game_state["current_room"]
    exits = ROOMS[current_room]["exits"]

    if direction not in exits:
        print("Нельзя пойти в этом направлении")
        return

    game_state["current_room"] = exits[direction]
    game_state["steps_taken"] += 1
    describe_current_room(game_state)
