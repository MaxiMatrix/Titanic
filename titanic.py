# loads the data and reads it
from load_data import load_data

# Load the data from the provided module
all_data = load_data()


def help():
    """Displays the available commands for the user."""
    print("""Available commands: 
help
show_countries
top_countries <num_countries>""")


def show_countries():
    """Displays a list of unique countries sorted alphabetically."""
    list_of_values = []
    for ships in all_data["data"]:
        for key, val in ships.items():
            if key == "COUNTRY":
                list_of_values.append(val)
    lst_of_countries = list(set(list_of_values))
    lst_of_countries.sort()
    for item in lst_of_countries:
        print(item)
    print()


def country_frequency():
    """Returns a dictionary with countries as keys and their frequency as values."""
    country_freq_dict = {}
    for ships in all_data["data"]:
        for ship, val in ships.items():
            if ship == "COUNTRY":
                if val not in country_freq_dict:
                    country_freq_dict[val] = 0
                country_freq_dict[val] += 1
    return country_freq_dict


def top_n_countries(freq, n=5):
    """Displays the top 'n' countries by ship count."""
    key_list = []
    value_list = []
    sorted_dict = dict(sorted(freq.items(), key=lambda item: item[1]))
    for key, value in sorted_dict.items():
        key_list.append(key)
        value_list.append(value)
    for item in range(n):
        print(f"{item + 1}. {key_list[-(item+1)]}: {value_list[-(item+1)]}")


def main():
    """The main function makes the program run."""
    print("Welcome to the Ships CLI! Enter 'help' to view available commands.")
    while True:
        user_input = input("> ").strip().lower()
        if user_input == "help":
            help()
        elif user_input == "show_countries":
            show_countries()
        elif user_input.startswith("top_countries"):
            try:
                num_countries = user_input.split()[1]
                top_n_countries(country_frequency(), int(num_countries))
            except (ValueError, IndexError):
                print("Please enter the command in the format: top_countries <num>")
        elif user_input == "exit":
            print("Exiting the Ships CLI. Goodbye!")
            break
        else:
            print("Invalid command. Enter 'help' to see available commands.")

print("Hello")
if __name__ == "__main__":
    main()
