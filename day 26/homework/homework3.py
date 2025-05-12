def type_of_answer():
    magaliti = input("sheiyvane magaliti: ")
    result = eval(magaliti) if magaliti else None
    return type(result) if result is not None else "araswori magaliti"