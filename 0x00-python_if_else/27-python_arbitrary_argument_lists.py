#python arbitrary argument lists
def write_multiple_items(file, separator, *args):
    file.write(separator.join(args))

with open("output.txt", "w") as file:
    write_multiple_items(file , "--", "2", "2" )
