from __future__ import annotations

from labyrinth_game.constants import ROOMS
from labyrinth_game.utils import describe_current_room, random_event, solve_puzzle


def show_inventory(game_state: dict) -> None:
    inv = game_state.get("player_inventory", [])
    if inv:
        print("Инвентарь:", ", ".join(inv))
    else:
        print("Инвентарь пуст.")


def move_player(game_state: dict, direction: str) -> None:
    current_room = game_state["current_room"]
    exits = ROOMS[current_room]["exits"]

    if direction not in exits:
        print("Нельзя пойти в этом направлении.")
        return

    target_room = exits[direction]

    # Вход в treasure_room только если:
    # 1) есть ключ
    # 2) решена загадка в hall
    if target_room == "treasure_room":
        if "rusty_key" not in game_state.get("player_inventory", []):
            print("Дверь заперта. Похоже, нужен ключ.")
            return
        if not game_state.get("hall_puzzle_solved", False):
            print("Что-то удерживает дверь. Возможно, сначала нужно решить")
            print("загадку в зале.")
            return
        print("Вы используете найденный ключ и проходите дальше.")

    game_state["current_room"] = target_room
    game_state["steps_taken"] = int(game_state.get("steps_taken", 0)) + 1

    describe_current_room(game_state)

    # Случайные события — только после успешного перехода
    random_event(game_state)


def take_item(game_state: dict, item_name: str) -> None:
    room_key = game_state["current_room"]
    items = ROOMS[room_key].get("items", [])

    if item_name not in items:
        print("Такого предмета здесь нет.")
        return

    game_state.setdefault("player_inventory", []).append(item_name)
    items.remove(item_name)
    print(f"Вы подняли: {item_name}")


def use_item(game_state: dict, item_name: str) -> None:
    inv = game_state.get("player_inventory", [])
    if item_name not in inv:
        print("У вас нет такого предмета.")
        return

    if item_name == "torch":
        print("Факел горит ярче. Теперь вы лучше видите в темноте.")
        return

    if item_name == "sword":
        print("Вы крепче сжимаете меч. Чувствуете уверенность.")
        return

    if item_name == "ancient_book":
        print("Вы читаете древнюю книгу. Некоторые символы совпадают с")
        print("надписями на стенах.")
        return

    if item_name == "bronze_box":
        print("В бронзовой шкатулке оказывается записка: '10'.")
        return

    if item_name == "rusty_key":
        print("Ключ тяжёлый и старый. Похоже, он для сокровищницы.")
        return

    print("Вы не знаете, как использовать этот предмет.")


def attempt_open_treasure(game_state: dict) -> None:
    if game_state["current_room"] != "treasure_room":
        print("Здесь нечего открывать.")
        return

    items = ROOMS["treasure_room"].get("items", [])
    if "treasure_chest" not in items:
        print("Сундука здесь нет.")
        return

    if "rusty_key" not in game_state.get("player_inventory", []):
        print("Сундук заперт. Нужен ключ.")
        return

    if ROOMS["treasure_room"].get("puzzle"):
        print("Сундук защищён кодом. Сначала используйте solve.")
        return

    items.remove("treasure_chest")
    print("Сундук открывается... Внутри сокровища! Вы победили!")
    game_state["game_over"] = True


def solve_current_room_puzzle(game_state: dict) -> None:
    ok = solve_puzzle(game_state)
    if not ok:
        return

    # Если в treasure_room решили код — сразу можно открыть сундук
    if game_state["current_room"] == "treasure_room":
        game_state["treasure_door_open"] = True
        print("Замок щёлкает. Теперь можно открыть сундук командой open.")
