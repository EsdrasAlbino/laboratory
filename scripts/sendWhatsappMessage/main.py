import pywhatkit
import csv
import time
import datetime
import gspread


file = "csv_data/data.csv"
step = {}

gc = gspread.service_account()
sh = gc.open("Controle_Escolas")
worksheet = sh.get_worksheet(0)

idx = 1

while True:
    try:

        values_list = worksheet.row_values(idx)
        time.sleep(2)
        idx += 1
        print(values_list)

        if not values_list[8]:
            print("enviar")

    except:
        time.sleep(5)
        break


with open(file, mode='r', encoding='utf-8') as csv_file:
    csv_reader = csv.reader(csv_file)
    count_run_total = 20
    count_run_current = 1

    for row in csv_reader:
        minute_current = datetime.datetime.now().minute
        hour_current = datetime.datetime.now().hour

        print(row[3])

        number = row[3].replace(" ", "").replace(
            "(", "").replace(")", "").replace("-", "")

        if (number.split("9")[0] == "81" or number.split("9")[0] == "87"):

            # Send a WhatsApp Message to a Contact at 1:30 PM
            pywhatkit.sendwhatmsg(
                f"+55{number}", f"Olá, {row[0]}. Tudo bem?😁\n\nSou o Esdras Albino, do time da Tangram Educação Financeira. Estou com uma boa proposta que acredito ser muito valiosa para você. Posso enviar uma mensagem explicando os detalhes?", hour_current, minute_current+2)
            time.sleep(5)
            count_run_current += 1
        if (count_run_current == count_run_total):
            break
        # break
