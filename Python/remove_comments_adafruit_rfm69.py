# '''The adafruit_rfm69.py file as it is will not fit on the
# Feather M0 CircuitPython I am using.  This file strips out
# the comments into another file.
# '''
import re
# Open adafruit_rfm69.py
with open('/Users/margaret/Documents/EnergyMonitoring/HappyDayNeighbors/Python/RFM69/Adafruit_CircuitPython_RFM69/adafruit_rfm69.py') as rfm69_file:
# Open stripped_rfm69.py
    with open('/Users/margaret/Documents/EnergyMonitoring/HappyDayNeighbors/Python/RFM69/Adafruit_CircuitPython_RFM69/stripped_rfm69.py','w+') as output_file:
        count_line_comments = 0
        count_help_comments = 0
        in_help = False
        lines_in_file = 0
        for line in rfm69_file:
            lines_in_file += 1
            if (re.match(r'#',line.lstrip())):
                count_line_comments += 1
            # do in_help check before searching for start and end of help
            # documentation.  This way, in_help will be set correctly and
            # the """ lines will be taken care of.
            elif (re.match(r'"""',line.lstrip())):
                in_help = not in_help
                count_help_comments += 1
                if (re.search('[a-zA-Z]',line) and line.rstrip().endswith(r'"""')):
                    in_help = False # doc help contained on one line
                    count_help_comments += 1
            elif (in_help):
                count_help_comments += 1
            elif not re.match(r'^\s*$', line):
                # skip if line has only \t\n\r and whitespace
                output_file.write(line)
        print('Total number of lines: '+str(lines_in_file))
        num_code_lines = lines_in_file - count_line_comments - count_help_comments
        print('Number of code lines: '+str(num_code_lines))
        num_comment_lines = count_line_comments + count_help_comments
        print('Number of comment lines: '+str(num_comment_lines))
# Loop through each line of the file
# if the line starts wtih #, skip.
# if the line is within a help comment line, skip.  Else write line to
#   stripped_rfm69.py.
# print out number of lines in adafruit_rfm69.py
# print out number of lines in stripped_rfm69.py
