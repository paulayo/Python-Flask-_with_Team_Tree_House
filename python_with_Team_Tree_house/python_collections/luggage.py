def packer(name=None, **kwargs):
    print(kwargs)



def unpacker(first_name=None, last_name=None):
    if first_name and last_name:
        print("Hi {} {}!".format(first_name, last_name))
    else:
        print("Hi no name")



packer(name="kenneth", num=100, spanish_inquistion=None)
unpacker(**{"last_name": "oloyede", "first_name": "Paul"})

course_minutes = {"Python Basics": 232, "Django Basics": 233, "Flask Basics": 432, "Java Basics": 263}

for course, minute in course_minutes.items():
    print("{} is {} minutes long".format(course, minute))
