def display_main_menu():
    print("Enter some numbers separated by commas (eg. 5, 67, 89, 1)")

def get_user_input():
    user_input = input()
    string_list = user_input.split(",")

    float_list = []
    for num_str in string_list:
        float_list.append(float(num_str))

    return float_list

def calc_average_temp(num_list):
    total = sum(num_list)
    average = total/ len (num_list)
    return average

def calc_min_max_temp(num_list):
    maximum = max (num_list)
    minimum = min (num_list)

    return [minimum, maximum]

def sort_temp(num_list):
    sorted_list = sorted(num_list)
    return sorted_list

def calc_median_temp(num_list):
    sorted_list = sort_temp(num_list)
    length = len(sorted_list)

    if length % 2 ==0:
        mid1 = length // 2 -1 
        mid2 = length // 2
        median = (sorted_list[mid1]+ sorted_list[mid2]) / 2
    else:
        mid = length // 2
        median = sorted_list[mid]

    return median


def main():
    display_main_menu()
    median = get_user_input()
    print(sort_temp(median))
    print("Average :",calc_average_temp(median))
    print("Min & Max :",calc_min_max_temp(median))
    print("Median :" ,calc_median_temp(median))


main()
