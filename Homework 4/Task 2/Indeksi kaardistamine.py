def index_data(index):
    return data[index]

data = [15, 33, 52, 65, 89, 96]

chosen_index = 3
value = index_data(chosen_index)

print(f"The value at index {chosen_index} is {value}.")