SPECIAL_CHARACTERS = "!@#$%^&*()_-=+`~,./'[]<>?{}|\\"


def main():
    show_list()
    user_password = check_password()
    print("Your ", len(user_password), " character password is valid: ", user_password)


def show_list():
    print("Please enter a valid password")
    print("Your password must be between 5 and 15 characters, and contain:")
    print("    1 or more uppercase characters")
    print("    1 or more lowercase characters")
    print("    1 or more numbers")
    print("    and 1 or more special characters:  !@#$%^&*()_-=+`~,./'[]<>?{}|\\")


def check_password():
    lower = 0
    upper = 0
    digit = 0
    special = 0
    user_password = input(">")
    while lower == 0 or upper == 0 or digit == 0 or special == 0:
        for char in user_password:
            if char.islower():
                lower += 1
            elif char.isupper():
                upper += 1
            elif char.isdigit():
                digit += 1
            elif char in SPECIAL_CHARACTERS:
                special += 1
        if 5 < len(user_password) < 15 and lower > 0 and upper > 0 and digit > 0 and special > 0:
            return user_password
        print("Invalid password!")
        lower = 0
        upper = 0
        digit = 0
        special = 0
        user_password = input(">")


main()
