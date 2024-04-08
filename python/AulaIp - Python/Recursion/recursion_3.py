
def check_thief(name_thief, string_concat):
    name_thief = name_thief.lower()
    string_concat = string_concat.lower()

    if len(string_concat) == 0:
        return False
    else:
        if name_thief[0] == string_concat[0]:
            if (name_thief == string_concat):
                return True
            else:
                return check_thief(name_thief, string_concat[:len(string_concat)-1])

        return check_thief(name_thief, string_concat[1:])


def main():
    name_thief = input()
    string_concat = input()

    outuput = check_thief(name_thief, string_concat)

    if outuput:
        print(f"Encontrei, o culpado é o {name_thief}!")
    else:
        print(f"Não era o {name_thief}, tenho que continuar procurando.")


main()
