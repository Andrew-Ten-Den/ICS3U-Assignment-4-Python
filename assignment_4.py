#!/usr/bin/env python3

# Created by: Andrew Ten-Den
# Created on: April 2022
# This program lets the user see if they can vote


def main():
    # this function lets the user see if they can vote

    # input
    try:
        age = int(input("How old are you?: "))

        # process & output
        if age >= 18:
            print("\nYou are eligible to vote!")
        elif 0 <= age <= 17:
            print("\nYou are not eligible to vote!")
        else:
            print("\nPlease input your age (a positive integer).")
    except Exception:
        print("\nPlease input your age (a positive integer).")
    finally:
        print("")
        print("Done")


if __name__ == "__main__":
    main()
