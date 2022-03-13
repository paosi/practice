#!/usr/bin/env python3

def solution(string, markers):

    for marker in markers:
        print(marker)
        print(string.index(marker))
        if marker in string:
            piece = string[string.index(marker): string.index("\n")]
            print(piece)
            string = string.replace(piece, "").strip()
        else:
            continue

    return string





if __name__ == "__main__":


    string = "apples, pears # and bananas\ngrapes\nbananas !apples\n"
    markers = ["#", "!"]

    print(solution(string, markers))