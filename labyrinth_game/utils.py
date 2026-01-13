from labyrinth_game.constants import ROOMS


def describe_current_room(game_state: dict) -> None:
    current_room = game_state["current_room"]
    room = ROOMS[current_room]

    print(f"\n== {current_room.upper()} ==")
    print(room["description"])

    items = room["items"]
    if items:
        print("Вы видите предметы:", ", ".join(items))
    else:
        print("Здесь нет видимых предметов.")

    exits = room["exits"]
    print("Выходы:", ", ".join(exits.keys()))

    if room["puzzle"] is not None:
        print("Здесь есть загадка. Используйте команду: solve")


def solve_puzzle(game_state: dict) -> None:
    current_room = game_state["current_room"]
    room = ROOMS[current_room]

    if room["puzzle"] is None:
        print("Загадок здесь нет.")
        return

    question, answer = room["puzzle"]
    print(question)
    user_answer = input("Ваш ответ: ").strip().lower()

    if user_answer == str(answer).strip().lower():
        print("Верно! Загадка решена.")
        room["puzzle"] = None

        # важное: если это сокровищница — отмечаем, что дверь открыта
        if current_room == "treasure_room":
            game_state["treasure_door_open"] = True
            print("Вы слышите щелчок механизма. Дверь в сокровищницу открыта!")
    else:
        print("Неверно. Попробуйте снова.")
