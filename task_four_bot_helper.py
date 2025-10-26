import colorama
from colorama import Fore, Style
from helpers import greeting, validate_name, validate_phone_number, list_contacts, close

CONTACTS_DB = {} # In-memory contacts database

def parse_input(user_input: str) -> tuple[str, list[str]]:
    """
    Parses user input for commands and arguments.
    Normalizes and validates the input.
    Args:
        user_input (str): The raw input string from the user.
    Returns:
        tuple[str, list[str]]: A tuple containing the command and a list of arguments.
    """
    parts = user_input.strip().lower().split()
    command = parts[0] if parts else ''
    args = parts[1:] if len(parts) > 1 else []
    return command, args


def assert_exception_output(exception_text: str) -> None:
    """
    Wrappers function to display beautiful colorama exception messages.
    Args:
        exception_text (str): The exception message to display.
    """
    print(f"{Style.BRIGHT}{Fore.RED}Error: {exception_text}{Style.RESET_ALL}")


def handle_command(command: str, args: list[str]) -> None:
    """
    Handles commads based on user input,
    calls appropriate functions.
    Args:
        command (str): The command to execute.
        args (list): A list of arguments for the command.
    """
    if command == 'hello':
        print(f"{Style.BRIGHT}{Fore.CYAN}{greeting()}")
    elif command == 'add' and len(args) == 2:
        name, phone_number = args
        if validate_name(name) and validate_phone_number(phone_number):
            CONTACTS_DB[name] = phone_number
            print(f"{Fore.GREEN}Contact {Style.BRIGHT}{name}{Style.RESET_ALL}{Fore.GREEN} added with phone number {Style.BRIGHT}{phone_number}")
        else:
            assert_exception_output("Invalid name or phone number format.")
    elif command == 'change' and len(args) == 2:
        name, new_phone_number = args
        if name in CONTACTS_DB and validate_phone_number(new_phone_number):
            CONTACTS_DB[name] = new_phone_number
            print(f"{Fore.GREEN}Contact {Style.BRIGHT}{name}{Style.RESET_ALL}{Fore.GREEN} updated with new phone number {Style.BRIGHT}{new_phone_number}")
        else:
            assert_exception_output("Contact not found or invalid phone number format.")
    elif command == 'phone' and len(args) == 1:
        name = args[0]
        if name in CONTACTS_DB:
            print(f"{Style.BRIGHT}{Fore.BLUE}{name}{Style.RESET_ALL}{Fore.BLUE}'s phone number is {Style.BRIGHT}{CONTACTS_DB[name]}")
        else:
            assert_exception_output("Contact not found.")
    elif command == 'all':
        contacts = list_contacts(CONTACTS_DB)
        print(f"{Fore.YELLOW}{contacts}")
    elif command in ['exit', 'close', 'bye', 'q']:
        print(f"{Style.BRIGHT}{Fore.MAGENTA}{close()}")
        exit()
    elif command == 'menu':
        print(main_menu())
    else:
        assert_exception_output("Unknown command. Please try again.")


def main_menu() -> str:
    """
    Displays the main menu options to the user.
    """
    menu_text = (
        f"{Style.BRIGHT}{Fore.BLUE}Please choose an option:{Style.RESET_ALL}\n"
        f"  {Fore.CYAN}* hello{Style.RESET_ALL} - Greet the user\n"
        f"  {Fore.CYAN}* add [name] [phone_number]{Style.RESET_ALL} - Add a new contact\n"
        f"  {Fore.CYAN}* change [name] [new_phone_number]{Style.RESET_ALL} - Update an existing contact\n"
        f"  {Fore.CYAN}* phone [name]{Style.RESET_ALL} - Retrieve a contact's phone number\n"
        f"  {Fore.CYAN}* all{Style.RESET_ALL} - Display all contacts\n"
        f"  {Fore.CYAN}* exit/close/bye/q{Style.RESET_ALL} - Exit the application\n"
        f"  {Fore.CYAN}* menu{Style.RESET_ALL} - Show this menu again\n"
    )
    return menu_text



def main():
    """
    Main function to run the command-line bot application.
    """
    colorama.init(autoreset=True)
    print(main_menu())
    while True:
        user_input = input(f"{Fore.BLUE}Enter command: {Style.RESET_ALL}")
        command, args = parse_input(user_input)
        handle_command(command, args)
