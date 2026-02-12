# TOday we explore data types for fastapi 

def get_full_name(first_name, last_name):
    full_name = first_name.title() + " " + last_name.title()
    return full_name


print(get_full_name("john", "doe"))



# check the error 
# def get_name_with_age(name: str , age :int):
#     name_with_age = name + " is this old: " + age
#     return name_with_age

# print(get_name_with_age("talha","20"))
