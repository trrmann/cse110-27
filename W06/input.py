def input_integer(question: str, retry_message: str, minimum_int: int = "undefined", maximum_int: int = "undefined", default_int:  int = "undefined"):
    has_min = False
    has_max = False
    has_default = False
    if minimum_int != "undefined":
        has_min = True
        minimum_int = int(minimum_int)
    if maximum_int != "undefined":
        has_max = True
        maximum_int = int(maximum_int)
    if default_int != "undefined":
        has_default = True
        default_int = int(default_int)
    has_limit = has_min or has_max
    if has_limit and has_min:
        integer = minimum_int - 1
    elif has_limit:
        integer = maximum_int + 1
    elif has_default:
        integer = default_int
    else:
        integer = -1
    if has_limit and has_min and has_max:
        while (integer < minimum_int) or (integer > maximum_int):
            try:
                integer = int(input(question))
                if ((integer < minimum_int) or (integer > maximum_int)) and has_default:
                    integer = default_int
                elif (integer < minimum_int) or (integer > maximum_int):
                    print(retry_message)
            except ValueError:
                if has_default:
                    integer = default_int
                else:
                    print(retry_message)
    elif has_limit and has_min:
        while (integer < minimum_int):
            try:
                integer = int(input(question))
                if (integer < minimum_int) and has_default:
                    integer = default_int
                elif (integer < minimum_int):
                    print(retry_message)
            except ValueError:
                if has_default:
                    integer = default_int
                else:
                    print(retry_message)
    elif has_limit:
        while (integer > maximum_int):
            try:
                integer = int(input(question))
                if (integer > maximum_int) and has_default:
                    integer = default_int
                elif (integer > maximum_int):
                    print(retry_message)
            except ValueError:
                if has_default:
                    integer = default_int
                else:
                    print(retry_message)
    else:
        try:
            integer = int(input(question))
        except ValueError:
            if has_default:
                integer = default_int
    return integer

def input_float(question: str, retry_message: str, minimum_float: float = "undefined", maximum_float: float = "undefined", default_float:  float = "undefined"):
    has_min = False
    has_max = False
    has_default = False
    if minimum_float != "undefined":
        has_min = True
        minimum_float = float(minimum_float)
    if maximum_float != "undefined":
        has_max = True
        maximum_float = float(maximum_float)
    if default_float != "undefined":
        has_default = True
        default_float = float(default_float)
    has_limit = has_min or has_max
    if has_limit and has_min:
        float_value = minimum_float - 0.0001
    elif has_limit:
        float_value = maximum_float + 0.0001
    elif has_default:
        float_value = default_float
    else:
        float_value = -0.0001
    if has_limit and has_min and has_max:
        while (float_value < minimum_float) or (float_value > maximum_float):
            try:
                float_value = float(input(question))
                if ((float_value < minimum_float) or (float_value > maximum_float)) and has_default:
                    float_value = default_float
                elif (float_value < minimum_float) or (float_value > maximum_float):
                    print(retry_message)
            except ValueError:
                if has_default:
                    float_value = default_float
                else:
                    print(retry_message)
    elif has_limit and has_min:
        while (float_value < minimum_float):
            try:
                float_value = int(input(question))
                if (float_value < minimum_float) and has_default:
                    float_value = default_float
                elif (float_value < minimum_float):
                    print(retry_message)
            except ValueError:
                if has_default:
                    float_value = default_float
                else:
                    print(retry_message)
    elif has_limit:
        while (float_value > maximum_float):
            try:
                float_value = int(input(question))
                if (float_value > maximum_float) and has_default:
                    float_value = default_float
                elif (float_value > maximum_float):
                    print(retry_message)
            except ValueError:
                if has_default:
                    float_value = default_float
                else:
                    print(retry_message)
    else:
        try:
            float_value = int(input(question))
        except ValueError:
            if has_default:
                float_value = default_float
    return float_value

def input_bool(question: str, retry_message: str, valid_true_list: str = "undefined", valid_false_list: str = "undefined", default_bool:  bool = "undefined", validation_case_sensative: bool = False):
    has_valid_true = False
    has_valid_false = False
    has_default = False
    valid_true_is_list = False
    valid_true_is_boolean = False
    valid_true_is_string = False
    valid_false_is_list = False
    valid_false_is_boolean = False
    valid_false_is_string = False
    validation_case_sensative = bool(validation_case_sensative)
    if valid_true_list != "undefined":
        has_valid_true = True
        if(type(valid_true_list) == type(["", ""])):
            valid_true_is_list = True
        elif(type(valid_true_list) == type(True)):
            valid_true_is_boolean = True
        else:
            valid_true_is_string = True
    if valid_false_list != "undefined":
        has_valid_false = True
        if(type(valid_false_list) == type(["", ""])):
            valid_false_is_list = True
        elif(type(valid_false_list) == type(True)):
            valid_false_is_boolean = True
        else:
            valid_false_is_string = True
    if not validation_case_sensative:
        if valid_true_is_list:
            counter = 0
            while counter < len(valid_true_list):
                valid_true_list[counter] = valid_true_list[counter].upper()
                counter = counter + 1
        elif valid_true_is_string:
            valid_true_list = valid_true_list.upper()
        if valid_false_is_list:
            counter = 0
            while counter < len(valid_false_list):
                valid_false_list[counter] = valid_false_list[counter].upper()
                counter = counter + 1
        elif valid_false_is_string:
            valid_false_list = valid_false_list.upper()
    if default_bool != "undefined":
        has_default = True
        default_bool = bool(default_bool)
    has_validation = has_valid_true or has_valid_false
    valid_response = not has_validation
    boolean = False
    if has_validation and has_valid_true and has_valid_false:
        while not valid_response:
            try:
                response = input(question)
                if valid_true_is_list and not validation_case_sensative and (response.upper() in valid_true_list):
                    valid_response = True
                    boolean = True
                elif valid_true_is_list and validation_case_sensative and (response in valid_true_list):
                    valid_response = True
                    boolean = True
                elif not validation_case_sensative and (response.upper() == valid_true_list):
                    valid_response = True
                    boolean = True
                elif validation_case_sensative and (response == valid_true_list):
                    valid_response = True
                    boolean = True
                elif valid_false_is_list and not validation_case_sensative and (response.upper() in valid_false_list):
                    valid_response = True
                    boolean = False
                elif valid_false_is_list and validation_case_sensative and (response in valid_false_list):
                    valid_response = True
                    boolean = False
                elif not validation_case_sensative and (response.upper() == valid_false_list):
                    valid_response = True
                    boolean = False
                elif validation_case_sensative and (response == valid_false_list):
                    valid_response = True
                    boolean = False
                elif valid_true_is_boolean and (bool(response.capitalize()) == valid_true_list):
                    valid_response = True
                    boolean = True
                elif valid_false_is_boolean and (bool(response.capitalize()) == valid_false_list):
                    valid_response = True
                    boolean = False
                elif has_default:
                    valid_response = True
                    boolean = default_bool
                else:
                    print(retry_message)
            except ValueError:
                if has_default:
                    boolean = default_bool
                else:
                    print(retry_message)
    elif has_validation and has_valid_true:
        while not valid_response:
            try:
                response = input(question)
                if valid_true_is_list and not validation_case_sensative and (response.upper() in valid_true_list):
                    valid_response = True
                    boolean = True
                elif valid_true_is_list and validation_case_sensative and (response in valid_true_list):
                    valid_response = True
                    boolean = True
                elif not validation_case_sensative and (response.upper() == valid_true_list):
                    valid_response = True
                    boolean = True
                elif validation_case_sensative and (response == valid_true_list):
                    valid_response = True
                    boolean = True
                elif valid_true_is_boolean and (bool(response.capitalize()) == valid_true_list):
                    valid_response = True
                    boolean = True
                elif has_default:
                    valid_response = True
                    boolean = default_bool
                else:
                    print(retry_message)
            except ValueError:
                if has_default:
                    boolean = default_bool
                else:
                    print(retry_message)
    elif has_validation:
        while not valid_response:
            try:
                response = input(question)
                if valid_false_is_list and not validation_case_sensative and (response.upper() in valid_false_list):
                    valid_response = True
                    boolean = False
                elif valid_false_is_list and validation_case_sensative and (response in valid_false_list):
                    valid_response = True
                    boolean = False
                elif not validation_case_sensative and (response.upper() == valid_false_list):
                    valid_response = True
                    boolean = False
                elif validation_case_sensative and (response == valid_false_list):
                    valid_response = True
                    boolean = False
                elif valid_false_is_boolean and (bool(response.capitalize()) == valid_false_list):
                    valid_response = True
                    boolean = False
                elif has_default:
                    valid_response = True
                    boolean = default_bool
                else:
                    print(retry_message)
            except ValueError:
                if has_default:
                    boolean = default_bool
                else:
                    print(retry_message)
    else:
        try:
            response = bool(input(question))
        except ValueError:
            if has_default:
                boolean = default_bool
    return boolean
