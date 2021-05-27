def get_input() -> (float,float,str):
    a=float(input("a >> "))
    operatie=input("operatie >> ")
    b = float(input("b >> "))
    return a, operatie, b


def suma(a: float, b: float) -> float:
    return a+b


def subt(a: float, b: float) -> float:
    return a-b


def mult(a: float, b: float) -> float:
    return a*b


def div(a: float, b: float) -> float:
    try:
        return a/b
    except ZeroDivisionError:
        return 0


def calculator():
    alpha, operation, beta  = get_input()
    variabila = ""
    if operation == "+":
        variabila = suma(alpha, beta)
        print(variabila)
    elif operation == "-":
        variabila=subt(alpha, beta)
        print(variabila)
    elif operation == "*":
        variabila = mult(alpha, beta)
        print(variabila)
    elif operation == "/":
        variabila = div(alpha, beta)
        print(variabila)
    return variabila


while True:
    calculator()




