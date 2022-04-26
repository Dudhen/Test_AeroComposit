numb = int(input("Введите число n (от 3 до 10): "))
if numb < 3 or numb > 10:
    while numb < 3 or numb > 10:
        numb = int(input("Вы ввели число, в недопустимом диапазоне! Введите число n еще раз: "))

matrix = [[0] * numb for i_cell in range(numb)]

matrix[numb // 2][numb // 2] = (numb * numb) - (numb % 2)

value = 0
for variable_calc in range(numb // 2):

    for i_index in range(numb - variable_calc * 2):
        matrix[variable_calc][i_index + variable_calc] = value
        value += 1

    for i_index in range(variable_calc + 1, numb - variable_calc):
        matrix[i_index][-variable_calc - 1] = value
        value += 1

    for i_index in range(variable_calc + 1, numb - variable_calc):
        matrix[-variable_calc - 1][-i_index - 1] = value
        value += 1

    for i_index in range(variable_calc + 1, numb - (variable_calc + 1)):
        matrix[-i_index - 1][variable_calc] = value
        value += 1

for i_string in matrix:
    print(*i_string)
