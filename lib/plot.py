import math

yellow = 3
green = 2
red = 1
gray = 8
blue = 39
magenta = 170
magenta_light = 225

def bcolored(text, color):
    return f"\033[48;5;{color}m{text}\033[0m"

def colored(text, color):
    return f"\033[38;5;{color}m{text}\033[0m"

def crunch(data, min_value, max_value):
    def scale_op(n):
        division_result = (n - min(data)) / (max(data) - min(data)) 
        return ((max_value - min_value) * division_result) + min_value

    return [
        int(scale_op(n))
        for n in data
    ]

def bar(data, scale=(1, 50)):
    ordered = sorted(data)

    desired_min, desired_max = scale
    cmin = colored(desired_min, blue)
    cmax = colored(desired_max, blue)
    text = colored('Scale: ', blue)

    print(f"\n{text} {cmin} - {cmax} \n")
    for index, sample in enumerate(crunch(ordered, desired_min, desired_max)):
        word = sample + index
        color_bar = bcolored(''.ljust(sample), magenta)
        value_text = colored(data[index], magenta_light)
        print(f"{color_bar} {value_text}\n")

