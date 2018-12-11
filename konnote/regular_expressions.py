from django.core.validators import RegexValidator
phone_regex = RegexValidator(regex=r'^\+?1?\d{9,15}$',
                             message="Phone number must be entered in the format: "
                                     "'+254722722722'. Up to 15 digits allowed.")
postal_code_regex = RegexValidator(regex=r'^\d{5,6}$',
                                   message="Postal Code must be entered in the format: '00100'. "
                                           "Up to 6 digits allowed.")
alphabet_only_regex = RegexValidator(regex=r'^[a-zA-Z]*$',
                                     message="Use Alphabet characters only. No numericals.")