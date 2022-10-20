
#!/usr/bin/env python3
# Created by: Lia Duggan
# Created on: Oct. 16th, 2022
# This program tells the user if the
# number they put in is even or odd


def main():

    # Getting the integer
    user_integer_as_string = input("Enter an integer: ")

    try:
        user_integer_as_int = int(user_integer_as_string)

    except Exception:
        print(user_integer_as_string, "is not a valid integer")

    # Determine if the number is even or odd.
    else:
        if user_integer_as_int == 0:
            print(user_integer_as_string + " isn't even or odd")
        elif user_integer_as_int % 2 == 0:
            print(user_integer_as_string + " is an even number")
        else:
            print(user_integer_as_string + " is an odd number")

    finally:
        print("Thanks for playing!")


if __name__ == "__main__":
    main()
