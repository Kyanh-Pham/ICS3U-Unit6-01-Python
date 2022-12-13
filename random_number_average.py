#!/usr/bin/env python3
# Created by: Kyanh Pham
# Created on: Dec 2022
# This program generates 10 random numbers and finds the average

import random


def main():
    # this function uses an array

    random_numbers = []

    for loop_counter in range(0, 10):
        single_random_number = random.randint(0, 100)
        random_numbers.append(single_random_number)
        print("The random number is: {0}".format(random_numbers[loop_counter]))

    # sum(random_numbers) adds all variables in the array
    average = sum(random_numbers) / len(random_numbers)
    print("")
    print("The average is {0}".format(average))

    print("\nDone.")


if __name__ == "__main__":
    main()
