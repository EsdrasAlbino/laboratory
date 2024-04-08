import gspread
import csv
import time
import utils
import build_structure_portion_future as build_structure_portion_future
import dates_formatter


class Portions:
    def __init__(self, file, sh, portionState, state, mock):
        self.file = file
        self.sh = sh
        self.portionsState = portionState
        self.state = state
        self.mock = mock
        self.date = dates_formatter.Dates()

    def check_portion_total(self, title):
        title_list = title.split("/")
        number = 1
        if (len(title_list) > 1):
            number = title_list[1]
        return number

    def check_portion_current(self, title):
        title_list = title.split("/")
        title_list_splited = title_list[0].split(" ")
        number = title_list_splited[len(title_list_splited)-1]
        if (number.isdigit()):
            return number
        else:
            return 1

    def define_date_payment_to_portions(self, data, turn_day, invoice_due_date):
        date = data.split("-")
        if (len(date) < 3):
            date = data.split("/")

        day = date[2]
        month = date[1]
        year = date[0]
        if (int(day) >= turn_day):
            month = int(month) + 1

        data_format = f"{month}/{invoice_due_date}/{year}"
        return data_format

    # Generate portions for mock informations
    def generate_portions(self, inputs):
        portions = []
        for input in inputs:
            portion_total = int(input[5])
            if (portion_total > 1):
                for i in range(1, portion_total+1):
                    date = self.date.format_date(
                        self.date.format_date(input[0], 0), i-1)
                    category = input[1]
                    title = input[2]
                    amount = input[3]
                    portion_current = i

                    card = "Nubank Pessoal"
                    value_portion = round(amount / portion_total, 2)

                    portion = (date, category, title, value_portion,
                               portion_current, portion_total, card)
                    portions.append(portion)
            else:
                portions.append(input)

        return portions

    def split_description(self, string):
        description = string.split(" - ")
        if (len(description) < 4):
            description.append('N/A')

        destination = description[1]
        return destination

    def revenue_type(self, description):
        if utils.contains_string(description, "TANGRAM ENSINO"):
            return "Ativa"
        else:
            return "Passiva"

    def work_data(self, inputs_list):

        if (not self.portionsState):
            return self.build_data_transations()
        else:
            inputs = []
            data_build = None
            if (self.state == "csv"):
                with open(self.file, mode='r') as csv_file:
                    data_build = csv.reader(csv_file)
            elif self.state == "txt":
                data_build = build_structure_portion_future.build_structure_portion_future(
                    self.file)
            else:
                data_build = inputs_list
            for row in data_build:
                date = self.define_date_payment_to_portions(
                    row[0], 14, 21)
                category = utils.category_type(row[1])
                title = row[2]
                amount = row[3]
                portion_current = self.check_portion_current(title)
                portion_total = self.check_portion_total(title)
                card = "Nubank Pessoal"
                transaction = ((date, category, title, amount,
                               portion_current, portion_total, card))

                # N/A is a title that payment credit card bill
                inputs.append(transaction)
            if self.state == "mock":
                inputs = self.generate_portions(inputs)
        return inputs

    # TRANSATIONS WITHOUT PORTIONS

    def build_data_transations(self):
        transactions = []

        with open(self.file, mode='r') as csv_file:
            csv_reader = csv.reader(csv_file)
            for row in csv_reader:

                date = self.date.format_date(row[0], 0)
                amount = abs(float(row[1]))
                description_aux = row[3]
                description = self.split_description(row[3])
                category = utils.category_type(description)
                revenue = self.revenue_type(description_aux)
                transaction_type = "recebida" if utils.contains_string(
                    description_aux, "recebida") else "enviada"
                transaction = ((date, amount, description,
                               revenue, transaction_type, category))
                if (row[3] != 'Pagamento de fatura'):
                    transactions.append(transaction)
        return transactions

    def send_transition(self):

        inputs = self.work_data(self.mock)

        if (not self.portionsState):
            for transaction in inputs:
                if transaction[4] == "recebida":
                    ws_send = self.sh.get_worksheet(1)
                    ws_send.append_row(
                        [transaction[2], "", transaction[2], transaction[0],
                         "", transaction[3], transaction[1]], 2)
                    time.sleep(2)
                else:
                    ws_send = self.sh.get_worksheet(0)
                    ws_send.append_row(
                        [transaction[2], transaction[0],
                         transaction[1], "Débito", transaction[5], "1", "1",
                         "Débito", "Nubank Pessoal"], 2)
                    time.sleep(2)
        else:
            ws_send = self.sh.get_worksheet(0)

            for input in inputs:
                date = input[0]
                category = input[1]
                title = input[2]
                amount = input[3]
                portion_current = input[4]
                portion_total = input[5]
                card = input[6]
                ws_send.append_row([title, date, amount, "Crédito",
                                    category, portion_current,
                                    portion_total, card], 2)
                time.sleep(2)


# CARDS
# Nubank Pessoal
# Nubank MEI
# Will

# CATEGORIAS
# Contas
# Estética
# Investimentos
# Alimentação
# Transporte
# Moradia
# Momentos Significativos
# Bem estar
# Educação
# Imposto

# CSV ORDER FORMAT
# date,category,title,amount


def main():
    file = "data/csv_bank/report_nubank.csv"
    gc = gspread.service_account()
    sh = gc.open("Monthly Budget Spreadsheet")
    state = "mock"  # csv, txt, mock

    mock = [["10/02/2024", "Investimentos", "Fonte do Pc de Nicoly 1/7", 110.03], ["18/03/2024", "Investimentos",
                                                                                   "Grafica", 68.31], ["27/03/2024", "Investimentos", "Compra para loja de mamãe 1/4", 399.80]]
    # Verificar se colocar apenas o valor da parcela atual, ou, o valor total da compra
    is_portions = True
    spredsheet_portions = Portions(file, sh, is_portions, state, mock)
    spredsheet_portions.send_transition()


main()
