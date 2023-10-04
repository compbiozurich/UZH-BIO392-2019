# Define the fixed value to add to all positionsoffset = 112702498# Open the input VCF file and create an output filewith open('merged_results.vcf', 'r') as input_file, open('output.vcf', 'w') as output_file:    for line in input_file:        if line.startswith('#'):            # Write header lines as is            output_file.write(line)        else:            # Split the line into fields            fields = line.strip().split('\t')            # Modify the position field by adding the offset            fields[1] = str(int(fields[1]) + offset)            # Write the modified line to the output file            output_file.write('\t'.join(fields) + '\n')print("Positions have been updated and saved to 'output.vcf'.")