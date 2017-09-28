import random
def read_occupations(file_name):
    # Read the file
    # 'U' is the universal newline (in case the csv file was made in Windows)
    source = open(file_name, 'rU')
    # Strip of newlines at the beginning of end of file before splitting/parsing
    lines = source.read().strip('\n').split('\n')
    source.close()
    csv_dict = {}
    # Remove the title line
    lines.pop(0)
    for line in lines:
        # Check if the job title includes commas and if so account for it
        if line[0:1] is '"':
            # Find the second quote
            end_quote = line[1:].find('"') + 1
            # Define the list accordingly
            temp = line[end_quote+2:].split(',') #contains the percentage and link
            fields = [line[1:end_quote], temp[0], temp[1]]
        else:
            fields = line.split(',')
        csv_dict[fields[0]] = [float(fields[1]), fields[2]]
    return csv_dict


def random_profession(professions):
    num = random.randint(1,998)
    for element in professions:
      #We keep subtracting the percentages until num becomes a negative number: we know that it falls within the range of the specific occupation when its negative
        num -= professions[element][0] * 10
        if num < 0:
            return element
    #returns -1 if something went wrong
    return -1;
