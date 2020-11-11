import matplotlib.pyplot as plt
import oldDB as old
import newDB as new

econ_values = []
test_values = []
test1_values = []
test2_values = []
year_values = []
class_dict_old = old.access_data(classes=True)
class_dict_new = new.access_data(classes=True)


for x in class_dict_old:
	year_values.append(x)
	econ_values.append(dict(class_dict_old[x])["ECON"])
	test_values.append(dict(class_dict_old[x])["BIOL"])
	test1_values.append(dict(class_dict_old[x])["ENGL"])
	test2_values.append(dict(class_dict_old[x])["CORE"]+ dict(class_dict_old[x])["FSEM"])

for x in class_dict_new:
	year_values.append(x)
	econ_values.append(dict(class_dict_new[x])["ECON"])
	test_values.append(dict(class_dict_new[x])["BIOL"])
	test1_values.append(dict(class_dict_new[x])["ENGL"])
	test2_values.append(dict(class_dict_new[x])["CORE"] + dict(class_dict_new[x])["FSEM"])


plot1 = plt.figure(1)
plt.plot(year_values, econ_values, "r")
#plt.plot(year_values, test_values, "b")
plt.plot(year_values, test2_values, "y")
plt.legend(["Economics", "Core+FSEM"])
plt.xticks([x for x in range(0,len(year_values),7)])

plt.show()