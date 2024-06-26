from typing import Any, Sequence
from django.forms import ClearableFileInput, Select



class CustomFileImput(ClearableFileInput):
    template_name = "widgets/custom_file.html"

class CustomSelect(Select):
    template_name = "widgets/custom_select.html"

    def __init__(self, attrs= None, choices=()):
        default_attrs = {"class": "select is-link"}
        if attrs:
            for attr_key, attr_value in attrs.items():
                if attr_key in default_attrs.keys():
                    default_attrs[attr_key] += " " + attr_value
                else:
                    default_attrs[attr_key] = attr_value
        super().__init__(default_attrs)
        self.choices = choices