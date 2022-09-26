import re
import csv

# Regex expln: https://regex101.com/r/9da5t3/1
regex_pattern = r'^"([\d-]*) ([\d\.:]*) (\d+) ([\S]+) ([\S\.]*) \[(.+)\] (([\d\.,]+) ""(\S+) (.+)"" status: (\d+) len: (\d+) time: ([\d\.]+)|(.+))"$'
regex_pattern_instance = r'^"([\d-]*) ([\d\.:]*) (\d+) ([\S]+) ([\S\.]*) \[(.+)\] ((\S+) ([0-9a-f\-]+)? .+)$'
regex_pattern_non_match = r'(\d+)'
fil = open("nova.csv", "r")
log_lines = fil.readlines()
header = ['Content']

# Try to match each log line with the regex.
# If matched, then print the status, len, and time from their groups.
# If not, print the log line as is.
with open('novaparse.csv', 'w', encoding='UTF8') as f:
  dw = csv.DictWriter(f, fieldnames=header)
  dw.writeheader()
  
  for line in log_lines:
    line = line.rstrip()
    matched = re.search(regex_pattern, line)

    if matched:
      if matched.group(9):
        #print("Found match. Type: " + matched.group(4) + ", Request: " + matched.group(9) + ", Status code: " + matched.group(11) + ", len: " + matched.group(12) + ", time: " + matched.group(13))
        print(("verbose level is " + matched.group(4) + " Request type is " +  matched.group(9) + " Status code is " + matched.group(11)),file=f)
      else:
        mat_3 = re.search(regex_pattern_instance, line)
        line_2 = line.replace(mat_3.group(9), "")
        mat_3 = re.search(regex_pattern_instance, line_2)
        print(("verbose level is " + mat_3.group(4) + " " + mat_3.group(7)), file=f)
    else:
      rewritten_line = line
      non_logs_match = re.findall(regex_pattern_non_match, line)
      if non_logs_match:
        for number in non_logs_match:
          rewritten_line = rewritten_line.replace(number, "")
        print(rewritten_line, file=f)
  f.close()
