from os import listdir
from os.path import isfile, join
import numpy
 
obfuscation_method = "optimal/rse"
# obfuscation_method = "fastoptimal/rse"

dataset = "temp336cycles" #temp336cycles, traffic100, traffic500
 
mypath = "./output/{}/{}".format(dataset, obfuscation_method)
onlyfiles = [ f for f in listdir(mypath) if isfile(join(mypath,f)) ]
	
mae_d = {}
rmse_d = {}

fixed_k = 5
fixed_e = 4
#fixed k, fixed e, different d
for file_name in onlyfiles:
	for d in range(10):
		if "_K{}_".format(fixed_k) in file_name and "_e{}_".format(fixed_e) in file_name and "_d{}_".format(d) in file_name and "_s50_".format(d) in file_name and "matrix" not in file_name:
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
			if d in mae_d:
				mae_d[d].append(numpy.mean(mae))
				rmse_d[d].append(numpy.mean(rmse))
			else:
				mae_d[d] = [numpy.mean(mae)]
				rmse_d[d] = [numpy.mean(rmse)]

print "--------- k={} e={}----------".format(fixed_k, fixed_e)
print "d MAE RMSE"
for d in range(10):
	print "{} {} {}".format(d, numpy.mean(mae_d[d]), numpy.mean(rmse_d[d]))


# mae_k = {}
# rmse_k = {}
# fixed_e = 4
# vary_k = [int(number_regions*0.1), int(number_regions*0.2), int(number_regions*0.3), int(number_regions*0.4), int(number_regions*0.5)]
# # fixed e, different k
# for file_name in onlyfiles:
# 	for k in vary_k:
# 		if "_K{}_".format(k) in file_name and (obfuscation_method == "no" or "_e{}_".format(fixed_e) in file_name) and "matrix" not in file_name:
# 			with open(mypath+"/"+file_name) as inputfile:
# 				lineno = 0
# 				mae = []
# 				rmse = []
				
# 				for line in inputfile:
# 					lineno += 1
# 					if lineno == 1:
# 						continue
# 					words = line.split(",")
# 					mae.append(float(words[2]))
# 					rmse.append(float(words[3]))
# 			if k in mae_k:
# 				mae_k[k].append(numpy.mean(mae))
# 				rmse_k[k].append(numpy.mean(rmse))
# 			else:
# 				mae_k[k] = [numpy.mean(mae)]
# 				rmse_k[k] = [numpy.mean(rmse)]


# print "---------- e={} ----------".format(fixed_e)
# print "k MAE RMSE"
# for k in vary_k:
# 	print "{} {} {}".format(k, numpy.mean(mae_k[k]), numpy.mean(rmse_k[k]))

