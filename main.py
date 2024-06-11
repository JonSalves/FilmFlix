import Add, delete, update, read, search


def read_file():
    try:
        with open("Options.txt") as file_read:
            fr = file_read.read()
            return fr
    except FileNotFoundError as fnf:
        print(f"Error handling file because {fnf}")


def film_menu():
    option = 0
    options_list = ["1", "2", "3", "4", "5", "6"]

    menu_choices = read_file()

    while option not in options_list:

        print(menu_choices)

        option = input("Choose and option")

        if option not in options_list:
            print("Please enter a valing number")

    return option


main_Program = True

while main_Program:
    main_menu = film_menu()

    match main_menu:
        case "1":
            Add.add_record()

        case "2":
            delete.delete_record()

        case "3":
            update.update_record()

        case "4":
            read.read_records()

        case "5":
            search.search_report()

        case _:
            main_Program = False

input("Press 'Enter' to EXIT the Menu/App")