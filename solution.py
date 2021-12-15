import csv
import sys

ls_dict = []
ls_dict_len = 0
fruit_type_set = set()
fruit_type_dict = {}
fruit_type_name_dict = {}
fruit_type_profile_dict = {}
over_3_days_dict = {}


def run_program():
    global ls_dict
    num_args = len(sys.argv)
    if num_args == 2:
        file_name = sys.argv[1]
        #file_name = "basket.csv"
        ls_dict = read_basket_file(file_name)
        total_number_of_fruit()
        total_types_of_fruit()
        count_each_fruit_desc()
        fruit_type_profiles()
        left_over_three_days()
    else:
        print("ERROR. Command should have the form:")
        print("python solution.py <Input File Path>")


def read_basket_file(name):
    read_list = []
    with open(name, 'r') as csv_file:
        csv_reader = csv.DictReader(csv_file)

        for line in csv_reader:
            read_list.append(line)
            # print(line)
    return read_list


def total_number_of_fruit():
    print("----------")
    global ls_dict_len
    ls_dict_len = len(ls_dict)
    print("Total number of fruit: {}".format(ls_dict_len))
    # print(ls_dict)


def total_types_of_fruit():
    for row in range(ls_dict_len):
        name_val = str(ls_dict[row]['name']).lower()
        fruit_type_set.add(name_val)
        # print(name_val)
    print("------------------")
    # print(fruit_type_set)
    print("Types of fruit: {}".format(len(fruit_type_set)))


def count_each_fruit_desc():
    print("----------------------")
    global ls_dict
    for fruit in fruit_type_set:
        fruit_type_cnt = 0
        fruit_over_3_days = 0
        size_set = set()
        color_shape_set = set()
        # shape_set = set()
        for row in range(ls_dict_len):
            if str(ls_dict[row]['name']).lower() == fruit:
                fruit_type_cnt += 1
                if int(ls_dict[row]['days']) > 3:
                    fruit_over_3_days += 1
                size_set.add(ls_dict[row]['size'])
                color_shape_set.add(ls_dict[row]['color'])
                color_shape_set.add(ls_dict[row]['shape'])
        fruit_type_dict.update({fruit: fruit_type_cnt})
        if fruit_over_3_days > 0:
            over_3_days_dict.update({fruit: fruit_over_3_days})
        fruit_type_name_dict.update({fruit: size_set})
        fruit_type_profile_dict.update({fruit: color_shape_set})

    #print(fruit_type_dict)
    sorted_fruit_type_dict = {x: y for x, y in sorted(fruit_type_dict.items(), key=lambda y: y[1], reverse=True)}
    print("The number of each type of fruit in descending order")
    for x, y in sorted_fruit_type_dict.items():
        print("{}: {}".format(x, y))


def fruit_type_profiles():
    print("--------------------------")
    print("The characteristics (size, color, shape, etc.) of each fruit by type")
    #print(fruit_type_name_dict)
    #print(fruit_type_profile_dict)
    for fruit, size in fruit_type_name_dict.items():
        for item in size:
            print("\n{} {}:".format(item, fruit), end=" ")
            for k, val in fruit_type_profile_dict.items():
                for v in val:
                    if k == fruit:
                        print("{},".format(v), end=" ")


def left_over_three_days():
    print("\n------------------------------")
    print("Have any fruit been in the basket for over 3 days")
    # over_3_days_cnt = len(over_3_days_dict)
    for x, y in over_3_days_dict.items():
        if y > 1:
            print("{} {}s are over 3 days old".format(y, x))
        else:
            print("{} {} are over 3 days old".format(y, x))


def main():
    run_program()


if __name__ == '__main__':
    main()