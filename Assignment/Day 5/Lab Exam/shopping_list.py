"""
Name : Ayush Kumar
Description : Shopping List Command Line Application with File Persistence

"""
class ShoppingList:
    def __init__(self, filename="shopping_list.txt"):
        self.filename = filename
        self.items = {}   
        self.load_items()

    def start_menu(self):
        print("\nWhat do you want to add to your shopping list?")
        print("Enter 'DONE' to stop adding items.")
        print("Enter 'HELP' for additional info.")
        print("Enter 'SHOW' to see your shopping list.")
        print("Enter 'REMOVE' to remove an item.")
        print("Enter 'CLEAR' to clear the list.")
        print("Enter 'SEARCH' to search items.")
        print("-" * 40)

    def normalize_item(self, name):
        return name.strip().capitalize()

    def parse_item(self, user_input):
        parts = user_input.split()
        if len(parts) >= 2 and parts[-1].lower().startswith("x") and parts[-1][1:].isdigit():
            name = " ".join(parts[:-1])
            quantity = int(parts[-1][1:])
        else:
            name = user_input
            quantity = 1

        return self.normalize_item(name), quantity

    def add_to_list(self, user_input):
        name, quantity = self.parse_item(user_input)

        if name in self.items:
            self.items[name] += quantity
            print(f"{name} quantity updated to x{self.items[name]}.")
        else:
            self.items[name] = quantity
            print(f"{name} (x{quantity}) was added to your shopping list.")

        print(f"You have {len(self.items)} items on your list.")

    def remove_item(self, item):
        item = self.normalize_item(item)

        if item in self.items:
            del self.items[item]
            print(f"{item} was removed from your shopping list.")
        else:
            print(f"{item} was not found in your shopping list.")

        print(f"You have {len(self.items)} items on your list.")

    def clear_list(self):
        confirm = input("Are you sure you want to clear the entire shopping list? (yes/no): ").lower()
        if confirm == "yes":
            self.items.clear()
            print("Shopping list cleared.")
        else:
            print("Clear operation cancelled.")

    def search_item(self, keyword):
        keyword = keyword.lower()
        found = False

        for item, qty in self.items.items():
            if keyword in item.lower():
                print(f"- {item} (x{qty})")
                found = True

        if not found:
            print("No matching items found.")

    def show_shopping_list(self):
        if not self.items:
            print("Your shopping list is empty.")
            return

        print("\nMy Shopping List:")
        for item in sorted(self.items):
            print(f"- {item} (x{self.items[item]})")

    def save_items(self):
        try:
            with open(self.filename, "w") as f:
                for item, qty in self.items.items():
                    f.write(f"{item},{qty}\n")
        except IOError:
            print("Error saving shopping list.")

    def load_items(self):
        try:
            with open(self.filename, "r") as f:
                for line in f:
                    if "," in line:
                        item, qty = line.strip().split(",")
                        self.items[item] = int(qty)
        except FileNotFoundError:
            self.items = {}
        except IOError:
            print("Error loading shopping list.")


def main():
    shopping_list = ShoppingList()
    shopping_list.start_menu()

    while True:
        try:
            command = input("> ").strip()

            if not command:
                continue

            cmd_upper = command.upper()

            if cmd_upper == "DONE":
                shopping_list.save_items()
                print("See you soon!")
                print("Your shopping list has been saved.")
                shopping_list.show_shopping_list()
                break

            elif cmd_upper == "HELP":
                shopping_list.start_menu()

            elif cmd_upper == "SHOW":
                shopping_list.show_shopping_list()

            elif cmd_upper == "REMOVE":
                shopping_list.show_shopping_list()
                item = input("What do you want to remove?: ")
                shopping_list.remove_item(item)

            elif cmd_upper == "CLEAR":
                shopping_list.clear_list()

            elif cmd_upper == "SEARCH":
                keyword = input("Enter item name to search: ")
                shopping_list.search_item(keyword)

            else:
                shopping_list.add_to_list(command)

        except EOFError:
            shopping_list.save_items()
            print("\nEOF detected. Shopping list saved. Goodbye!")
            break


if __name__ == "__main__":
    main()