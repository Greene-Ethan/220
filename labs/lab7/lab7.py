def weighted_average(in_file_name, out_file_name):
    open_file = open(in_file_name,"r")
    write_file = open(out_file_name,"w")
    reader = open_file.readlines()
    weight = 0
    grade = 1
    adding_those_grades = 0
    class_total = 0
    average_num = 0
    for line in reader:
        split_at_colon = line.split(":")

        just_names = split_at_colon[0]
        write_file.write(just_names + ": ")


        grades_with_n = split_at_colon[1]
        just_grades = grades_with_n.strip()
        grades_list = just_grades.split(" ")
        #weight_times_grade = eval(grades_list[weight]) * eval((grades_list[grade]))
        #adding_those_grades = (adding_those_grades + weight_times_grade) / 100
        weight = 0
        grade = 1
        #print(grades_list)
        added_grades = 0
        check_weight = 0
        for nums in line:
            if weight <= len(grades_list) and grade <= len(grades_list):
                weight_times_grade = eval(grades_list[weight]) * eval((grades_list[grade]))
                just_weight = eval(grades_list[weight])
                check_weight = check_weight + just_weight
                weight = weight + 2
                grade = grade + 2
                added_grades = added_grades + weight_times_grade

        if check_weight == 100:
            final_grade = added_grades / 100
            class_total = (class_total + final_grade)
            average_num = average_num + 1
            final_grades = round((final_grade),1)
            final_grades_chr = str(final_grades)
            write_file.write(final_grades_chr)
        elif check_weight < 100:
            less_weight = "Error: the weights are less than 100."
            write_file.write(less_weight)
        else:
            more_weight = "Error: the weights are more than 100."
            write_file.write(more_weight)
        write_file.write("\n")
    class_average = round((class_total / 3),1)
    final_class_average = str(class_average)
    write_file.write("class average: " + final_class_average)
    open_file.close()