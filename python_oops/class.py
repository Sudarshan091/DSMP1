# def power(base, exponent=2):
#     return base ** exponent
# value=power(2)    
# print(value)

# def add_item(item, lst=None):
#     # item=int(input('enter the numbers '))

#     if lst is None:
#         lst = []
#     lst.append(item)
#     return lst
# item=int(input('enter the numbers '))
# new=add_item(item)
# print(new)

# def greet_user(**info):
#     for key, value in info.items():
#         print(f"{key}: {value}")

# greet_user(name="Alice", age=25, city="New York", country="india")

parser = argparse.ArgumentParser(
                    prog='ProgramName',
                    description='What the program does',
                    epilog='Text at the bottom of help')
parser.add_argument('filename')           # positional argument
parser.add_argument('-c', '--count')      # option that takes a value
parser.add_argument('-v', '--verbose',
                    action='store_true')  # on/off flag
args = parser.parse_args()
print(args.filename, args.count, args.verbose)