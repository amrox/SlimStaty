import re
import inflection


def camel_case(s: str, uppercase_first_letter=False) -> str:
    if len(s) == 0:
        return ""

    s = re.sub(r'-', r'_', s)

    return inflection.camelize(s,
                               uppercase_first_letter=uppercase_first_letter)

def snake_case(s: str) -> str:
    return inflection.underscore(s)
