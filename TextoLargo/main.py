#!/usr/bin/env python
# -*- coding: utf-8 -*-

def main():
    words_to_change = {"Alice": "Bob",
                       "she": "he",
                       "her": "his",
                       "herself": "himself",
                       "Lewis Carroll": "Luisa Bermeo"}

    with open("./alice.txt", "r") as file:
        line_counter = 0

        for line in file:
            for word in words_to_change:
                # Reemplaza cualquier valor Alice por Bob
                line = line.replace(word, words_to_change[word])

            print(line, end="")
            line_counter += 1

            if line_counter == 20:
                input("Presione ENTER para ver mas...")
                line_counter = 0


if __name__ == "__main__":
    main()
