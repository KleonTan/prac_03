OUTPUT_FILE_1 = "temps_input.txt"
OUTPUT_FILE_2 = "temps_output.txt"
in_file = open(OUTPUT_FILE_1, 'r')
out_file = open(OUTPUT_FILE_2, 'w')
for line in in_file:
    celsius = 5 / 9 * (float(line) - 32)
    print(celsius, file=out_file)
in_file.close()
out_file.close()
