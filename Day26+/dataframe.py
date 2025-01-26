student_dict = {
    "student": ["Angela", "James", "Lily"],
    "score": [56, 77, 98]
}

# for (key, value) in student_dict.items():
#     print(key)
#     print(value)
    
# import pandas as pd
# student_data_frame = pd.DataFrame(student_dict)
# print(student_data_frame)

# for index, row in student_data_frame.iterrows():
#     # print(index)
#     print(row.student)
#     print(row.score)

new_list = [ n * 2 for n in range(1, 5) if n > 3]
print(new_list)

