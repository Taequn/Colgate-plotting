import matplotlib.pyplot as plt
import oldDB as old
import newDB as new

econ_values = []
test_values = []
test1_values = []
test2_values = []
test3_values = []
test4_values = []
year_values = []
class_dict_old = old.access_data(classes=True)
class_dict_new = new.access_data(classes=True)


for x in class_dict_old:
	year_values.append(x)
	econ_values.append(dict(class_dict_old[x])["HIST"])
	test_values.append(dict(class_dict_old[x])["PHIL"])
	test1_values.append(dict(class_dict_old[x])["ENGL"])
	test2_values.append(dict(class_dict_old[x])["CHEM"])
	test3_values.append(dict(class_dict_old[x])["BIOL"])
	test4_values.append(dict(class_dict_old[x])["COSC"])


for x in class_dict_new:
	year_values.append(x)
	econ_values.append(dict(class_dict_new[x])["HIST"])
	test_values.append(dict(class_dict_new[x])["PHIL"])
	test1_values.append(dict(class_dict_new[x])["ENGL"])
	test2_values.append(dict(class_dict_new[x])["CHEM"])
	test3_values.append(dict(class_dict_new[x])["BIOL"])
	test4_values.append(dict(class_dict_new[x])["COSC"])


plot1 = plt.figure(1)
plt.plot(year_values, econ_values, "r")
plt.plot(year_values, test_values, "b")
plt.plot(year_values, test1_values, "g")
plt.plot(year_values, test2_values, "y")
plt.plot(year_values, test3_values, "b")
plt.plot(year_values, test4_values, "#17becf")
plt.legend(["History", "Philosophy", "English", "Chemistry", "Biology", "Computer Science"])
plt.ylabel('Number of classes')
plt.xlabel('Year (YYYY) + Semester (01/02)')
plt.xticks([x for x in range(0,len(year_values),7)])

plt.show()