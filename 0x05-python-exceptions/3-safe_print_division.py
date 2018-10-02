def safe_print_division(a, b):
    try:
        print("Inside Result: ", end="")
        result = a / b
    except:
        result = None
    finally:
        print("{}".format(result))
    return result
