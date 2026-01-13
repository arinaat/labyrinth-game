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


def take_item(game_state: dict, item_name: str) -> None:
    if not item_name:
        print("Что подобрать? Пример: take torch")
        return

    current_room = game_state["current_room"]
    room_items = ROOMS[current_room]["items"]

    if item_name not in room_items:
        print("Такого предмета здесь нет.")
        return

    room_items.remove(item_name)
    game_state["player_inventory"].append(item_name)
    print(f"Вы подняли предмет: {item_name}")


def use_item(game_state: dict, item_name: str) -> None:
    if not item_name:
        print("Что использовать? Пример: use torch")
        return

    inventory = game_state["player_inventory"]
    if item_name not in inventory:
        print("У вас нет такого предмета.")
        return

    if item_name == "torch":
        print("Факел освещает путь. Теперь вы лучше видите стены и выходы.")
    elif item_name == "sword":
        print("Вы уверенно держите меч. Это добавляет смелости.")
    elif item_name == "bronze_box":
        print("Шкатулка заперта. Возможно, нужен ключ.")
    elif item_name == "rusty_key":
        print("Вы пробуете ржавый ключ. Кажется, он может подойти к чему-то важному.")
    elif item_name == "ancient_book":
        print("Вы листаете древнюю книгу. В ней много непонятных символов.")
    else:
        print("Вы не знаете, как использовать этот предмет.")
