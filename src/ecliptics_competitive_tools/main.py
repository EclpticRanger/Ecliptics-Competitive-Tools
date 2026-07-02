

def get_int_line(input_text: str = "", split_string: str = " "):
    """

    Returns A list of intigers seporated by the inputed character
    """

    return [int(s) for s in list_put(input_text, split_string)]


def get_float_line(input_text: str = "", split_string: str = " "):
    """

    Returns A list of floats seporated by the inputed character

    """
    return [float(s) for s in list_put(input_text, split_string)]


def get_bool_line(input_text: str = "", split_string: str = " ", true_character: str = "true", flase_character: str = "false", defult: bool = False):
    """

    Returns A list of Bool seporated by the inputed character

    defaults:
        Split_character: " "
        True: "true"
        False: "false"

    """
    bool_list = input(input_text)
    bool_list = bool_list.split(split_string)
    for i in range(bool_list):
        if bool_list[i] == true_character:
            bool_list[i] = True
        elif bool_list[i] == flase_character:
            bool_list[i] = False
        else:
            bool_list[i] = defult
    return bool_list
    


def int_put(input_text: str = "", ):
    """
    Returns an input converted to an int
    """
    return int(input(input_text))


def float_put(input_text: str = "", ):
    """
    Returns an input converted to an float
    """
    return float(input(input_text))


def list_put(input_text: str = "", split_string: str = " "):
    """
    Returns an input converted to an List of strings
    """
    return input(input_text).split(split_string)


def tuple_put(input_text: str = "", split_string: str = " "):
    """
    Returns an input converted to an Tupel of strings
    """
    return tuple(input(input_text).split(split_string))