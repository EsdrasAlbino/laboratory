N = int(input())
M = int(input())
exactSum = False
time_training = []
positions = []

for i in range(M):
    position_training_time = input().split(' ')
    position, minutes_done = position_training_time[0], position_training_time[1]
    positions.append(position)
    time_training.append(minutes_done)

time_training_done = [int(element) for element in time_training]

for i in range(len(time_training_done)):
    position = []
    sum = 0
    for j in range(i, len(time_training_done)):
        sum += time_training_done[j]
        position.append(positions[j])

        if sum == N:
            exactSum = True
            break
    if exactSum:
        break

if exactSum:
    positions_print = ' '.join(position)
    print(
        f'Conquistamos nossa primeira estrela! Barbie e Chelsea arrasaram nos treinos das {positions_print}!')
else:
    print('Não treinamos na dose certa e infelizmente a estrela vai ter que ficar para a próxima')
