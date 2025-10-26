import colorama, pathlib
#from .task_four_bot_helper import main as task4_main
import task_four_bot_helper
#################### Taks 1 ####################
def salaries_data(path) -> list[float]:
    """
    Reads a file containing salary data and returns a list of salaries. 
    Format of each line in the file: "Name Surname,Salary".
    Args:
        path (str): The path to the salary data file.
    Returns:
        list: A list of salaries as floats.
    """
    salaries = []
    with open(path , 'r', encoding='utf-8') as file:
        for line in file:
            try:
                name_surname, salary = line.split(',')
                salaries.append(float(salary))
            except ValueError:
                continue  # Skip lines that don't conform to the expected format

    return salaries


def average_salary(salaries: list[float]) -> float:
    """
    Calculates the average salary from a list of salaries.
    Args:
        salaries (list): A list of salaries as floats.
    Returns:
        float: The average salary.
    """
    if not salaries:
        return 0.0
    return sum(salaries) / len(salaries)


def sum_of_salaries(salaries: list[float]) -> float:
    """
    Calculates the total sum of salaries from a list of salaries.
    Args:
        salaries (list): A list of salaries as floats.
    Returns:
        float: The total sum of salaries.
    """
    return sum(salaries)

#################### End of Task 1 ####################

####################    Task 2     ####################

def get_cats_info(path) -> list[dict]:
    """
    Reads a file containing cats data in format "id,name,age" and returns a list of dictionaries.
    Args:
        path (str): The path to the cats data file.
    Returns:
        list: A list of dictionaries with keys 'id', 'name', and 'age'.
    """
    cats = []
    with open(path, 'r', encoding='utf-8') as file:
        for line in file:
            try:
                cat_id, name, age = line.strip().split(',')
                cats.append({'id': cat_id, 'name': name, 'age': int(age)})
            except ValueError:
                continue  # Skip lines that don't conform to the expected format

    return cats


def display_cats_info(cats: list[dict]) -> None:
    """
    Displays information about each cat from a list of cat dictionaries.
    Args:
        cats (list): A list of dictionaries with keys 'id', 'name', and 'age'.
    """
    for cat in cats:
        print(f"Cat ID: {cat['id']}, Name: {cat['name']}, Age: {cat['age']} years")

#################### End of Task 2 ####################

####################    Task 3     ####################

def display_directory_tree(path: str, absolute: bool = False, except_of: list[str] | None = None) -> None:
    """
    Displays the directory tree starting from `path` with optional exclusions.
    Args:
        path (str): The root directory path to display the tree from.
        absolute (bool): Whether to display absolute paths. Defaults to False.
        except_of (list[str] | None): A list of directory or file names to exclude. Defaults to None.
    Returns:
        None
    """
    root_path = pathlib.Path(path).resolve()
    excluded = set(except_of or [])

    colorama.init()
    try:
        print(_colorize(_display_label(root_path, root_path, absolute), root_path))
        _print_children(root_path, root_path, absolute, excluded, prefix="~")
    finally:
        colorama.deinit()


def _print_children(current: pathlib.Path, root: pathlib.Path, absolute: bool, excluded: set[str], prefix: str = "") -> None:
    """ 
    Recursively prints the children of the current directory with proper formatting.
    Args:
        current (pathlib.Path): The current directory path.
        root (pathlib.Path): The root directory path.
        absolute (bool): Whether to display absolute paths.
        excluded (set): A set of directory or file names to exclude.
        prefix (str): The prefix string for formatting.
    Returns:
        None
    """
    entries = [
        child
        for child in sorted(current.iterdir(), key=lambda item: (not item.is_dir(), item.name.lower()))
        if child.name not in excluded
    ]

    for index, child in enumerate(entries):
        is_last = index == len(entries) - 1
        connector = "└── " if is_last else "├── "
        next_prefix = prefix + ("    " if is_last else "│   ")

        label = connector + _display_label(child, root, absolute)
        print(prefix + _colorize(label, child))

        if child.is_dir():
            _print_children(child, root, absolute, excluded, next_prefix)


def _display_label(path: pathlib.Path, root: pathlib.Path, absolute: bool) -> str:
    """ 
    Returns the display label for a given path, either absolute or relative to root.
    Args:
        path (pathlib.Path): The path to display.
        root (pathlib.Path): The root directory path.
        absolute (bool): Whether to display absolute paths.
    Returns:
        str: The display label for the path.
    """
    if absolute:
        return str(path.resolve())
    if path == root:
        label = "."
    else:
        label = str(path.relative_to(root))

    if path.is_dir():
        return f"{label}/"
    return label


def _colorize(label: str, path: pathlib.Path) -> str:
    """
    Applies color coding to the label based on whether it's a directory or file type.
    Args:
        label (str): The label to colorize.
        path (pathlib.Path): The path associated with the label.
    Returns:
        str: The colorized label.
    """
    if path.is_dir():
        style = colorama.Style.BRIGHT + colorama.Fore.CYAN
    else:
        extension_styles = {
            ".py": colorama.Style.BRIGHT + colorama.Fore.GREEN,
            ".txt": colorama.Fore.YELLOW,
            ".md": colorama.Fore.MAGENTA,
        }
        style = extension_styles.get(path.suffix.lower(), colorama.Fore.WHITE)
    return f"{style}{label}{colorama.Style.RESET_ALL}"
    

#################### End of Task 3 ####################

####################    Task 4     ####################



#################### End of Task 3 ####################


def task_1():
    """
    Executes Task 1: Reads salary data, calculates average and total salaries, and prints the results.
    """
    path = 'salaries.txt'
    salaries = salaries_data(path)
    avg_salary = average_salary(salaries)
    total_salary = sum_of_salaries(salaries)

    
    print(f'Average Salary: {avg_salary}')
    print(f'Total Sum of Salaries: {total_salary}')
    

def task_2():
    """ 
    Executes Task 2: Reads cats data and displays the information.
    """
    path = 'cats_data.txt'
    cats = get_cats_info(path)
    display_cats_info(cats)


def task_3():    
    """ 
    Executes Task 3: Displays the directory tree structure.
    """
    path = '.'  # Current directory
    display_directory_tree(path, absolute=False, except_of=['.git', '__pycache__', '.venv'])

def task_4():
    """ 
    Executes Task 4: Runs the command-line bot application.
    """
    task_four_bot_helper.main()

def main():
    """ Main function to execute tasks. """
    print("-" * 20)
    print("Task 1: Salary Data Analysis")
    task_1()
    print("Task 1 completed.")
    print("-" * 20)
    print("Task 2: Cats Information Display")
    task_2()
    print("Task 2 completed.")
    print("-" * 20)
    print("Task 3: Directory Tree Display")
    task_3()
    print("Task 3 completed.")
    print("-" * 20)
    print("Task 4: Command-Line Bot Application")
    task_4()
    print("Task 4 completed.")
    print("-" * 20)


if __name__ == "__main__":
    main()
    
