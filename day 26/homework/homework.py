def detect_type_category(value):
    if type(value) == str:
        return "Text"
    elif type(value) == int or type(value) == float:
        return "Number"
    elif type(value) == bool:
        return "Logic"
   
    