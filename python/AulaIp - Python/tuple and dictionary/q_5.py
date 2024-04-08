class Suspect:
    def __init__(self, name):
        self.name = name
        self.characteristics = {}
        self.judged = False

    def update_characteristics(self, characteristics):
        self.characteristics.update(characteristics)

    def judge(self):
        if self.judged:
            return "Eu já tenho o meu veredito, e o meu veredito, " + self.name + ":\n" + ("Natural" if self.is_natural() else "FAKE NATTY! USOU O SUCO!")
        return "Quem é esse crazy man? Não tá aqui na database"

    def is_natural(self):
        if "Biceps" in self.characteristics and int(self.characteristics["Biceps"][:-2]) > 45:
            if "Treino" in self.characteristics and self.parse_time(self.characteristics["Treino"]) >= 30:
                if "Frequencia" in self.characteristics and int(self.characteristics["Frequencia"][:-5]) >= 4:
                    if "BF" in self.characteristics and int(self.characteristics["BF"][:-1]) < 10:
                        if "Suor" in self.characteristics and self.characteristics["Suor"] == "Seco":
                            return True
        return False

    def parse_time(self, time_str):
        if "hora" in time_str:
            return int(time_str.split()[0]) * 60
        elif "minuto" in time_str:
            return int(time_str.split()[0])
        else:
            return int(time_str.split()[0]) / 60

    def is_judged(self):
        return self.judged

    def set_judged(self):
        self.judged = True


class NattyMeter:
    def __init__(self):
        self.suspects = []

    def add_suspect(self, name):
        self.suspects.append(Suspect(name))
        return "Novo suspeito: " + name

    def update_suspect(self, name, characteristics):
        suspect = self.find_suspect(name)
        if suspect:
            suspect.update_characteristics(characteristics)
            return name + " atualizado com sucesso"
        return "Quem é esse crazy man? Não tá aqui na database"

    def remove_suspect(self, name):
        suspect = self.find_suspect(name)
        if suspect:
            self.suspects.remove(suspect)
            return name + " removido da lista de suspeitos, está limpo"
        return "Quem é esse crazy man? Não tá aqui na database"

    def judge_suspect(self, name):
        suspect = self.find_suspect(name)
        if suspect:
            return suspect.judge()
        return "Quem é esse crazy man? Não tá aqui na database"

    def natty_meter(self):
        total_suspects = len(self.suspects)
        natural_count = sum(suspect.is_natural() for suspect in self.suspects)
        if total_suspects == 0:
            return "Oh yeah, vivemos em uma sociedade sem suco, um great day"
        percentage = (natural_count / total_suspects) * 100
        return "NOOO! " + str(int(percentage)) + "% USARAM O SUCO"

    def find_suspect(self, name):
        for suspect in self.suspects:
            if suspect.name == name:
                return suspect
        return None


natty_app = NattyMeter()
output = []
while True:
    command = input()

    if command == "FIM":
        break

    if command == "Adicionar suspeito":
        name = input()
        output.append(natty_app.add_suspect(name))
    elif command == "Atualizar suspeito":
        name, characteristics = input().split("-> ")
        characteristics_list = characteristics.split(", ")
        characteristics_dict = {}
        key, value = characteristics_list[0].split(": ")
        characteristics_dict[key] = value

        output.append(natty_app.update_suspect(name, characteristics_dict))
    elif command == "Remover suspeito":
        name = input()
        output.append(natty_app.remove_suspect(name))
    elif command == "Julgamento":
        name = input()
        output.append(natty_app.judge_suspect(name))
    elif command == "NattyMeter":
        output.append(natty_app.natty_meter())

for line in output:
    print(line)
