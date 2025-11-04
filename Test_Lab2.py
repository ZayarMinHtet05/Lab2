import Lab2

def find_min_max():
    input_arr = [12, 14, 16, 17, 18, 19, 20]
    result = []
    excepted_result = [12, 20]

    result = Lab2.calc_min_max_temp(input_arr)

    assert result == excepted_result

def calc_average():
    input_arr = [12, 14, 16, 17, 18, 19, 20]
    result = 0
    excepted_result = 14.14

    result = Lab2.calc_average_temp(input_arr)

    assert result == excepted_result

def calc_median_temp():
    input_arr = [12, 14, 16, 17, 18, 19, 20]
    result = 0
    excepted_result = 17

    result = Lab2.calc_median_temp(input_arr)

    assert result == excepted_result

