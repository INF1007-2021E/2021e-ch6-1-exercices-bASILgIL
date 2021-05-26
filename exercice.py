#!/usr/bin/env python
# -*- coding: utf-8 -*-


def order(values: list = None) -> list:
    if values is None:
        # TODO: demander les valeurs ici
        values = []
        while len(values) < 10:
            valeurs = input("Entrez une valeur: ")
            values.append(valeurs)

    sorted_values = ", ".join(sorted(values))#sorted() doesnt affect the list permanently but .sort() changes the list and it stays changed

    return print(sorted_values)


def anagrams(words: list = None) -> bool:
    if words is None:
        # TODO: demander les mots ici
        words = []
        while len(words) < 2:
            mot = input("Svp entrez un mot: ")
            if mot.isalpha():
                words.append(mot)
            else:
                print("T'as foire g! Ca rentre pas ds ta ptite tete de con! Recommence caliss!")

    if sorted(words[0]) == sorted(words[1]):
        print(str(True) + "\n" + "Les deux mots sont des anagrammes! :)")
    else:
        print(str(False) + "\n" + "Les deux mots ne sont malheureusement pas des anagrammes. :(")

    #return sorted(words[0]) == sorted(words[1]) sans paprass




def contains_doubles(items: list) -> bool:
    """new_list = []
    for elem in items:
        if elem not in new_list:
            new_list.append(elem)

    return (len(new_list) < len(items))
"""
    new_list = set(items)
    return (len(new_list) < len(items))


def best_grades(student_grades: dict) -> dict:
    # TODO: Retourner un dictionnaire contenant le nom de l'étudiant ayant la meilleure moyenne ainsi que sa moyenne
    best_student = {}
    for student, list_grades in student_grades.items():
        moyenne = sum(list_grades)/len(list_grades)
        if len(best_student) == 0 or moyenne > list(best_student.values())[0]:#goes through the first coindition then the next
            best_student = {student: moyenne}
        #elif moyenne > list(best_student.values())[0]:
            #best_student = {student: moyenne}

    return best_student


def frequence(sentence: str) -> dict:
    # TODO: Afficher les lettres les plus fréquentes
    frequence_dict = {letter: sentence.count(letter) for letter in sentence}
    sorted_keys = sorted(frequence_dict, key=frequence_dict.__getitem__, reverse=True)#sans paranthese cest pour tous les elements et cest ordonne par rapport aux valeurs
    for key in sorted_keys:
        if frequence_dict[key] > 5:
            print(f"Le caractere {key} revient {frequence_dict[key]} fois.")



def get_recipes():
    # TODO: Demander le nom d'une recette, puis ses ingredients et enregistrer dans une structure de données
    pass


def print_recipe(ingredients) -> None:
    # TODO: Demander le nom d'une recette, puis l'afficher si elle existe
    pass


def main() -> None:
    #print(f"On essaie d'ordonner les valeurs...")
    #order()

    #print(f"On vérifie les anagrammes...")
    #print(anagrams())

    my_list = [3, 3, 5, 6, 1, 1]
    print(f"Ma liste contient-elle des doublons? {contains_doubles(my_list)}")

    grades = {"Bob": [90, 65, 20], "Alice": [85, 75, 83]}
    best_student = best_grades(grades)
    print(f"{list(best_student.keys())[0]} a la meilleure moyenne: {list(best_student.values())[0]}")

    sentence = "bonjour, je suis une phrase. je suis compose de beaucoup de lettre. oui oui"
    frequence(sentence)

    print("On enregistre les recettes...")
    recipes = get_recipes()

    print("On affiche une recette au choix...")
    print_recipe(recipes)


if __name__ == '__main__':
    main()
