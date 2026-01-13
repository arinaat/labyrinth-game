from labyrinth_game.player_actions import (
    attempt_open_treasure,
    move_player,
    show_inventory,
    solve_current_room_puzzle,
    take_item,
    use_item,
)
from labyrinth_game.utils import describe_current_room


def main() -> None:
    game_state = {
        "player_inventory": [],
        "current_room": "entrance",
        "game_over": False,
        "steps_taken": 0,
        "health": 100,
        "treasure_door_open": False,
        "hall_puzzle_solved": False,
    }

    print("Добро пожаловать в Лабиринт сокровищ!")
    describe_current_room(game_state)

    while not game_state["game_over"]:
        command = input("> ").strip().lower()

        if command in ("quit", "exit"):
            print("Вы вышли из игры.")
            break

        if command == "look":
            describe_current_room(game_state)
            continue

        if command == "inventory":
            show_inventory(game_state)
            continue

        if command == "solve":
            solve_current_room_puzzle(game_state)
            continue

        if command == "open":
            attempt_open_treasure(game_state)
            continue

        if command == "go":
            print("Куда идти? Пример: go north")
            continue

        if command.startswith("go "):
            direction = command.split(maxsplit=1)[1]
            move_player(game_state, direction)
            continue

        if command == "take":
            print("Что подобрать? Пример: take torch")
            continue

        if command.startswith("take "):
            item_name = command.split(maxsplit=1)[1]
            take_item(game_state, item_name)
            continue

        if command == "use":
            print("Что использовать? Пример: use torch")
            continue

        if command.startswith("use "):
            item_name = command.split(maxsplit=1)[1]
            use_item(game_state, item_name)
            continue

        print(
            "Команды: look / inventory / go <dir> / take <item> / use <item> / "
            "solve / open / quit"
        )


if __name__ == "__main__":
    main()
