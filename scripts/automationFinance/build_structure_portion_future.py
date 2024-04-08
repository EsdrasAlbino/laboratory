import utils
import dates_formatter


def build_structure_portion_future(path_file):
    with open(path_file) as file:
        dates = dates_formatter.Dates()

        file_edit = file.read().split('\n\n')

        data_structure = []
        element_submited = []
        data_current_relative = ""

        data_filter = dates.data_filter

        for element in file_edit:
            if element in data_filter or utils.contains_string(element, "JAN") or utils.contains_string(element, "FEV") or utils.contains_string(element, "MAR") or utils.contains_string(element, "ABR") or utils.contains_string(element, "MAI") or utils.contains_string(element, "JUN") or utils.contains_string(element, "JUL") or utils.contains_string(element, "AGO") or utils.contains_string(element, "SET") or utils.contains_string(element, "OUT") or utils.contains_string(element,     "NOV") or utils.contains_string(element, "DEZ"):
                splited_element = element.split(" ")
                if splited_element[0].isdigit():
                    data_current_relative = dates.date_current_relative_today(
                        splited_element[1], int(splited_element[0]))
                else:
                    data_current_relative = dates.date_relative_ago_week(
                        element)
            else:

                if utils.contains_string(element, "R$"):
                    element_submited.append(
                        utils.replace_value(element.split(" ")[1]))
                    data_structure.append(element_submited)
                    element_submited = []
                else:
                    if data_current_relative in element_submited:
                        element_submited.append(element)
                    else:

                        element_submited.append(data_current_relative)
                        element_submited.append(element)  # Category
                        element_submited.append(element)  # Title

        return data_structure
