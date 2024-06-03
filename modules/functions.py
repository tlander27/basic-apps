FILEPATH = "todos.txt"

def get_todos(filepath=FILEPATH):
    """Opens file to store To-do data and returns list"""
    with open(filepath, 'r') as file_local:
        todos_local = file_local.readlines()
    return todos_local


def write_todos(todos_arg, filepath=FILEPATH):
    """Writes To-do items to file"""
    with open(filepath, 'w') as file_local:
        file_local.writelines(todos_arg)


if __name__ in "__main__":
    print(get_todos("../todos.txt"))