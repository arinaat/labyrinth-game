from labyrinth_game.utils import describe_current_room, solve_puzzle
from labyrinth_game.player_actions import move_player, show_inventory, take_item, use_item


def main() -> None:
    game_state = {
        "player_inventory": [],
        "current_room": "entrance",
        "game_over": False,
        "steps_taken": 0,
    }

    print("Добро пожаловать в Лабиринт сокровищ!")
    describe_current_room(game_state)

    while not game_state["game_over"]:
        command = input("> ").strip().lower()

        if command in ("quit", "exit"):
            game_state["game_over"] = True
            print("Вы вышли из игры.")

        elif command == "look":
            describe_current_room(game_state)

        elif command == "inventory":
            show_inventory(game_state)

        elif command == "solve":
            solve_puzzle(game_state)

        elif command == "go":
            print("Куда идти? Пример: go north")

        elif command.startswith("go "):
            parts = command.split(maxsplit=1)
            direction = parts[1] if len(parts) > 1 else ""
            if not direction:
                print("Куда идти? Пример: go north")
            else:
                move_player(game_state, direction)

        elif command == "take":
            print("Что подобрать? Пример: take torch")

        elif command.startswith("take "):
            parts = command.split(maxsplit=1)
            item_name = parts[1] if len(parts) > 1 else ""
            take_item(game_state, item_name)

        elif command == "use":
            print("Что использовать? Пример: use torch")

        elif command.startswith("use "):
            parts = command.split(maxsplit=1)
            item_name = parts[1] if len(parts) > 1 else ""
            use_item(game_state, item_name)

        else:
            print("Команды: look / inventory / go <dir> / take <item> / use <item> / solve / quit")


if __name__ == "__main__":
    main()
