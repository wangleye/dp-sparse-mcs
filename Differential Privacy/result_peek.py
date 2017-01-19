from os import listdir
from os.path import isfile, join
import numpy
 
# obfuscation_method = "optimal/rse"
# obfuscation_method = "fastoptimal/rse"
obfuscation_method = "exponential/rse"
# obfuscation_method = "naive"
# obfuscation_method = "no"

dataset = "humidity" #temp336cycles, traffic100, traffic500
number_regions = 50
 
mypath = "./output/{}/{}".format(dataset, obfuscation_method)
onlyfiles = [ f for f in listdir(mypath) if isfile(join(mypath,f)) ]
print onlyfiles
	
mae_e = {}
rmse_e = {}

fixed_k = int(number_regions*0.3)
#fixed k, different e
for file_name in onlyfiles:
	for e in [2, 4, 6, 8]:
		if "_K{}_".format(fixed_k) in file_name and (obfuscation_method != "optimal" or "_d1_" in file_name) and (obfuscation_method == "no" or "_e{}_".format(e) in file_name) and "matrix" not in file_name:
			with open(mypath+"/"+file_name) as inputfile:
				lineno = 0
				mae = []
				rmse = []
				
				for line in inputfile:
					lineno += 1
					if lineno == 1:
						continue
					words = line.split(",")
					mae.append(float(words[2]))
					rmse.append(float(words[3]))
			if e in mae_e:
				mae_e[e].append(numpy.mean(mae))
				rmse_e[e].append(numpy.mean(rmse))
			else:
				mae_e[e] = [numpy.mean(mae)]
				rmse_e[e] = [numpy.mean(rmse)]

print "--------- k={} ----------".format(fixed_k)
print "e MAE RMSE"
for e in [2, 4, 6, 8]:
	print "{} {} {}".format(e, numpy.mean(mae_e[e]), numpy.mean(rmse_e[e]))


mae_k = {}
rmse_k = {}
fixed_e = 4
vary_k = [int(number_regions*0.1), int(number_regions*0.2), int(number_regions*0.3), int(number_regions*0.4), int(number_regions*0.5)]
# fixed e, different k
for file_name in onlyfiles:
	for k in vary_k:
		if "_K{}_".format(k) in file_name  and (obfuscation_method != "optimal" or "_d1_" in file_name) and (obfuscation_method == "no" or "_e{}_".format(fixed_e) in file_name) and "matrix" not in file_name:
			with open(mypath+"/"+file_name) as inputfile:
				lineno = 0
				mae = []
				rmse = []
				
				for line in inputfile:
					lineno += 1
					if lineno == 1:
						continue
					words = line.split(",")
					mae.append(float(words[2]))
					rmse.append(float(words[3]))
			if k in mae_k:
				mae_k[k].append(numpy.mean(mae))
				rmse_k[k].append(numpy.mean(rmse))
			else:
				mae_k[k] = [numpy.mean(mae)]
				rmse_k[k] = [numpy.mean(rmse)]


print "---------- e={} ----------".format(fixed_e)
print "k MAE RMSE"
for k in vary_k:
	print "{} {} {}".format(k, numpy.mean(mae_k[k]), numpy.mean(rmse_k[k]))

