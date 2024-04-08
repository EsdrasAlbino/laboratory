def processing_data(data, months):
    pure_data = data.split(" - ")
    name = pure_data[0]
    other_datas = pure_data[1].split(" ")
    profession, status, month_number = other_datas[0], other_datas[1], int(
        other_datas[2])

    organization_months(months, name, profession, status, month_number)


def organization_months(months, name, profession, status, month_number):
    famous_information = {
        'name': name, 'profession': profession, 'status': status}

    months[month_number-1].append(famous_information)


def is_fake_natty(data_analysis):
    fake_natty = []

    for i in data_analysis:
        if i.status == "fake":
            fake_natty.append(f"{i.name} - {i.profession}")

    return fake_natty


def main():
    all_months = ([], [], [], [], [], [], [], [], [], [], [], [])
    quantify_famous = int(input())
    for i in range(quantify_famous):
        famous_data = input()
        processing_data(famous_data, all_months)

    month_require = int(input())

    famous_month_require = all_months[month_require-1]

    sorted(famous_month_require, key=lambda student: student.name)

    famous_fake = is_fake_natty(famous_month_require)

    if len(famous_fake) > 0:
        # print("Os fake nattys do mês são:\n")
        print(famous_fake)
    else:
        print("Até agora não temos ninguém pra expor na internet neste mês :(")


main()
