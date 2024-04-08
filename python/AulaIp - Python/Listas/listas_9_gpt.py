ideal_training_time = int(input())
position_training_time_length = int(input())

position_training_time = []
for i in range(position_training_time_length):
    position, training_time = input().split()
    position_training_time.append([position, int(training_time), i])


def get_combinations(lst):
    if not lst:
        return [[]]

    first, rest = lst[0], lst[1:]
    without_first = get_combinations(rest)
    with_first = [subset + [first] for subset in without_first]
    return with_first + without_first


combinations = get_combinations(position_training_time)

possibilities = []
for combination in combinations:
    subset = [item[1] for item in combination]
    subset_positions = [item[0] for item in combination]
    if sum(subset) == ideal_training_time and list(range(min(subset_positions), max(subset_positions) + 1)) == subset_positions:
        possibilities.append((subset_positions, subset))

if possibilities:
    choosed_positions = ' '.join(map(str, possibilities[0][0]))
    print(
        f"Conquistamos nossa primeira estrela! Barbie e Chelsea arrasaram nos treinos das {choosed_positions}!")
else:
    print("Não treinamos na dose certa e infelizmente a estrela vai ter que ficar para a próxima")
