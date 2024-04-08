ideal_training_time = int(input())
position_training_time_length = int(input())
position_training_time = list()

for i in range(position_training_time_length):
    position_training_time.append(input().split(' '))
    position_training_time[-1].append(i)

combinations = []

for i in range(2 ** position_training_time_length):
    subset = []
    for j in range(position_training_time_length):
        if (i // (2 ** j)) % 2 == 1:
            subset.append(position_training_time[j])
    combinations.append(subset)

possibilities = list()

for combination in combinations:
    if combination != []:
        possibilities.append([[],0,[]])
        for item in combination:
            possibilities[-1][0].append(item[0])
            possibilities[-1][1] += int(item[1])
            possibilities[-1][2].append(item[2])

choosed_positions = None
for possibility in possibilities:
    if possibility[1] == ideal_training_time:
        sequencial = 1
        for index in range(1,len(possibility[2])):
            if possibility[2][index - 1] + 1 != possibility[2][index]:
                sequencial = 0
        if sequencial == 1:
            choosed_positions = ' '.join(possibility[0])
if choosed_positions == None:
    print("Não treinamos na dose certa e infelizmente a estrela vai ter que ficar para a próxima")
else:
    print(f"Conquistamos nossa primeira estrela! Barbie e Chelsea arrasaram nos treinos das {choosed_positions}!")