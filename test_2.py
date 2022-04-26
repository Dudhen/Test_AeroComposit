import re

map = "11100\n" \
      "11010\n" \
      "11000\n" \
      "01101\n"

print('Карта:\n' + map)

general_indexes = [[i for i, val in enumerate(re.findall(r'.', i_str)) if val == '1'] for i_str in map.split('\n')]
count = []
previous_list = []
for i_list in general_indexes:
    for i_index in i_list:
        if i_index not in previous_list and i_index - 1 not in i_list:
            count.append(i_index)
    previous_list = i_list
print("Количество найденных островов:", len(count))