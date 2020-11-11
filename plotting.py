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
	test1_values.append(dict(class_dict_old[x])["COSC"])
	test2_values.append(dict(class_dict_old[x])["CHEM"])

for x in class_dict_new:
	year_values.append(x)
	econ_values.append(dict(class_dict_new[x])["ECON"])
	test_values.append(dict(class_dict_new[x])["BIOL"])
	test1_values.append(dict(class_dict_new[x])["COSC"])
	test2_values.append(dict(class_dict_new[x])["CHEM"])


plot1 = plt.figure(1)
plt.plot(year_values, econ_values, "r")
plt.plot(year_values, test_values, "b")
plt.plot(year_values, test1_values, "g")
plt.plot(year_values, test2_values, "y")
plt.legend(["Economics", "Biology", "Computer Science", "Chemistry"])
plt.ylabel('Number of classes')
plt.xlabel('Year (YYYY) + Semester (01/02)')
plt.xticks([x for x in range(0,len(year_values),7)])

plt.show()