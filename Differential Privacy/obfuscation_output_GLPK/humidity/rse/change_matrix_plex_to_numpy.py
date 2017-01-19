file_name = "optimal_epsilon8_delta0.out_cplex"

file_str = ""
with open (file_name, "r") as inputfile:
	for line in inputfile:
		file_str += " " + line.strip()

file_str = file_str.replace("[", "").replace("]", "\n")

with open (file_name+"_new", "w") as outputfile:
	outputfile.write(file_str)