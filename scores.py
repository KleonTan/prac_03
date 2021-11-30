"""
CP1404/CP5632 - Practical
Broken program to determine score status
"""

import random


def main():
    OUTPUT_FILE = "results.txt"
    scoresNums = get_scores_nums()
    get_random_scores(scoresNums, OUTPUT_FILE)


def get_scores_nums():
    scoresNums = int(input("How many scores you want:"))
    return scoresNums


def get_random_scores(scoresNums, OUTPUT_FILE):
    result = open(OUTPUT_FILE, 'w')
    for i in range(scoresNums):
        score = random.randint(0, 100)
        if score < 50:
            print("{} is Bad".format(score))
            print("{} is Bad".format(score), file=result)
        elif 50 <= score < 90:
            print("{} is Bad".format(score))
            print("{} is Passable".format(score), file=result)
        else:
            print("{} is Bad".format(score))
            print("{} is Excellent".format(score), file=result)
    result.close()


main()
