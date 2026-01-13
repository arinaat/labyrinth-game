from labyrinth_game.utils import describe_current_room
from labyrinth_game.player_actions import show_inventory


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
        else:
            print("Пока доступны только команды: look / inventory / quit / exit")


if __name__ == "__main__":
    main()
