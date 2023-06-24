location_venon = input().lower()
location_my_one = input().lower()


get_venon = False

if location_my_one == location_venon:
    print("Ahá, te encontrei e é o fim das suas férias!")
    get_venon = True

else:
    print("Carambolas, ele não está aqui. Ele continua se divertindo!")


if not get_venon:
    location_my_two = input().lower()
    if location_my_two == location_venon:
        print("Ahá, te encontrei e é o fim das suas férias!")
        get_venon = True
    else:
        print("Carambolas, ele não está aqui. Ele continua se divertindo!")


if not get_venon:
    location_my_three = input().lower()
    if location_my_three == location_venon:
        print("Ahá, te encontrei e é o fim das suas férias!")
        get_venon = True
    else:
        print("Carambolas, ele não está aqui. Ele continua se divertindo!")

if not get_venon:
    print("AAAAAAAH, ele escapou de vez!")
