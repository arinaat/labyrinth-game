from __future__ import annotations

import math

from labyrinth_game.constants import EVENT_MODULO, ROOMS


def describe_current_room(game_state: dict) -> None:
    room_key = game_state["current_room"]
    room = ROOMS[room_key]

    title = room_key.upper()
    print(f"\n== {title} ==")
    print(room["description"])
    print(f"HP: {game_state.get('health', 100)}/100")

    items = room.get("items", [])
    if items:
        print("Вы видите предметы:", ", ".join(items))
    else:
        print("Здесь нет видимых предметов.")

    exits = room.get("exits", {})
    if exits:
        print("Выходы:", ", ".join(exits.keys()))

    if room.get("puzzle"):
        print("Здесь есть загадка. Используйте команду: solve")


def pseudo_random(seed: int, modulo: int) -> int:
    """
    Детерминированная псевдослучайность без random:
    возвращает целое в диапазоне [0, modulo).
    """
    if modulo <= 0:
        return 0

    x = math.sin(seed * 12.9898) * 43758.5453
    frac = x - math.floor(x)
    return int(frac * modulo)


def solve_puzzle(game_state: dict) -> bool:
    room_key = game_state["current_room"]
    puzzle = ROOMS[room_key].get("puzzle")

    if not puzzle:
        print("Загадки здесь нет.")
        return False

    question, answer = puzzle
    print(question)

    user_answer = input("Ваш ответ: ").strip().lower()
    correct = answer.strip().lower()

    # Альтернативные варианты для "10"
    if correct == "10":
        accepted = {"10", "десять"}
        is_ok = user_answer in accepted
    else:
        is_ok = user_answer == correct

    if not is_ok:
        print("Неверно. Попробуйте снова.")
        # Если ошибся в trap_room — активируем ловушку
        if room_key == "trap_room":
            trigger_trap(game_state)
        return False

    print("Верно! Загадка решена.")
    ROOMS[room_key]["puzzle"] = None

    # Награда зависит от комнаты
    if room_key == "hall":
        game_state["hall_puzzle_solved"] = True
        print("Вы чувствуете, как что-то в лабиринте изменилось...")
    elif room_key == "trap_room":
        if "coin" not in ROOMS[room_key]["items"]:
            ROOMS[room_key]["items"].append("coin")
        print("На полу появляется монетка.")
    else:
        if "coin" not in game_state["player_inventory"]:
            game_state["player_inventory"].append("coin")
        print("Вы получаете награду: coin")

    return True


def trigger_trap(game_state: dict) -> None:
    """
    Ловушка:
    - если инвентарь не пуст: теряешь случайный предмет
    - если пуст: получаешь урон 
    """
    game_state["traps_triggered"] = int(game_state.get("traps_triggered", 0)) + 1
    again = game_state["traps_triggered"] > 1

    inv = game_state.get("player_inventory", [])
    steps = int(game_state.get("steps_taken", 0))

    if inv:
        idx = pseudo_random(steps, len(inv))
        lost = inv.pop(idx)
        prefix = "Ловушка снова сработала" if again else "Ловушка сработала"
        print(f"{prefix}! Вы потеряли предмет: {lost}.")
        return

    roll = pseudo_random(steps, 10)

    if roll < 3:
        roll = 3

    damage = 15 + roll * 3
    game_state["health"] = max(0, int(game_state.get("health", 100)) - damage)

    prefix = "Ловушка снова сработала" if again else "Ловушка сработала"
    print(f"{prefix}! Вы получили урон (-{damage}).")
    print(f"HP: {game_state['health']}/100")

    if game_state["health"] <= 0:
        print("Ваше здоровье на нуле. Вы проиграли.")
        game_state["game_over"] = True


def random_event(game_state: dict) -> None:
    """
    Случайные события после перемещения.
    3 сценария:
    0) находка coin в комнате
    1) испуг (меч помогает)
    2) ловушка (ТОЛЬКО trap_room и если нет torch)
    """
    steps = int(game_state.get("steps_taken", 0))
    happen = pseudo_random(steps, EVENT_MODULO)  
    if happen != 0:
        return

    roll = pseudo_random(steps + 7, 3)  

    if roll == 0:
        room_key = game_state["current_room"]
        items = ROOMS[room_key].setdefault("items", [])
        if "coin" not in items:
            items.append("coin")
            print("Вы находите на полу монетку (coin).")
        return

    if roll == 1:
        if "sword" in game_state.get("player_inventory", []):
            print("Вы слышите шорох... но меч придаёт уверенности.")
            print("Опасность отступила.")
        else:
            print("Вы слышите шорох из темноты. Вам не по себе.")
        return

    # roll == 2: ловушка — строго по условиям
    if game_state["current_room"] != "trap_room":
        return

    if "torch" in game_state.get("player_inventory", []):
        print("Свет факела помогает заметить ловушку заранее. Вы избегаете её.")
        return

    trigger_trap(game_state)


def show_help(commands: dict) -> None:
    print("Доступные команды:")
    width = 16
    for cmd, desc in commands.items():
        print(f"  {cmd:<{width}} {desc}")
