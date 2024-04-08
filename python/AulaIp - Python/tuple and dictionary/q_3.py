def slice_list(list, positions):
    result = []
    start = 0
    for pos in positions:
        if list[start:pos]:
            result.append(list[start:pos])
        start = pos
    result.extend(list[start:])
    return result


def organization_stack(stacks, code):
    positions_zero = []
    group_list_stack = []
    lists_order_stack = []
    for idx, stack in enumerate(stacks):
        if '+' in stack:
            values_concat = []
            separetor_terms = stack.split("+")
            for term in separetor_terms:
                values_concat.append(str(code[term]))
            lists_order_stack.append(int(''.join(values_concat)))
        else:
            lists_order_stack.append(code[stack])

        if lists_order_stack[idx] == 0:
            positions_zero.append(idx)

    slice_list(lists_order_stack, positions_zero)
    return group_list_stack


def possible_form_stack(stacks):
    for stack in stacks:
        for idx, items_stack in enumerate(stack):
            if idx+1 != items_stack:
                return 'NO'
    return 'YES'


code = {
    "Oooh look at him": 0,
    "Baseball bat": 1,
    "Aesthetic": 2,
    "Fake Natty": 3,
    "Chris Bumbstead, o CBUM": 4,
    "Pope Francis": 5,
    "O suco vicia": 6,
    "I don't know you tell me": 7,
    "Não é mesmo?": 8,
    "Rodrigo Goes out": 9,
}

number_person_in_event = int(input())
person_in_stack = []

for i in range(number_person_in_event):
    person_in_stack.append(input())

group_stacks = organization_stack(person_in_stack, code)
print_stack_possible = possible_form_stack(group_stacks)
print(print_stack_possible)
