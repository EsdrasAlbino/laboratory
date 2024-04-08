def main():
    str_random = input()
    price_item = 0
    up_case = sum([1 for i in str_random if i.isupper()])
    low_case = len(str_random) - up_case
    size_string = up_case + low_case

    def price_rercusive(k):
        if k == 0:
            return 1
        else:
            return (k * price_rercusive(k-1))

    if (up_case == low_case):
        price_item = size_string**2
    else:
        k = max(up_case, low_case)
        price_item = price_rercusive(k) * size_string

    if price_item >= 100:
        print(f"Hum... {price_item}? Acho que na volta eu compro")
    else:
        print(f"{price_item}! Vou comprar todos!")


main()
