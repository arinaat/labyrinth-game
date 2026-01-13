def show_inventory(game_state: dict) -> None:
    inventory = game_state["player_inventory"]
    if inventory:
        print("Инвентарь:", ", ".join(inventory))
    else:
        print("Инвентарь пуст.")
