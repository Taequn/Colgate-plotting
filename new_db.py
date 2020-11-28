import requests
import re
import json
import old_db as db

#check capacity of classes

department_dict = {
	"ALST": "Africana and Latin American Studies",
	"ANTH": "Anthropology",
	"ARTS": "Art and Art History",
	"AHUM": "Arts and Humanities",
	"ASIA": "Asian Studies",
	"ASTR": "Astronomy",
	"BIOL": "Biology",
	"CHEM": "Chemistry",
	"CHIN": "Chinese",
	"CLAS": "The Classics",
	"COSC": "Computer Science",
	"ECON": "Economics",
	"EDUC": "Educational Studies",
	"ENGL": "English",
	"ENST": "Environmental Studies",
	"FMST": "Film and Media Studies",
	"FREN": "French",
	"GEOG": "Geography",
	"GEOL": "Geology",
	"GERM": "German",
	"GREK": "Greek",
	"HEBR": "Hebrew",
	"HIST": "History",
	"ITAL": "Italian",
	"JAPN": "Japanese",
	"JWST": "Jewish Studies",
	"LATN": "Latin",
	"LGBT": "Lesbian, Gay, Bisexual, Transgender, and Queer Studies",
	"CORE": "CORE studies",
	"LING": "Linguistics",
	"MATH": "Mathematics",
	"ARAB": "Middle Eastern and Islamic Studies (Language)",
	"MIST": "Middle Eastern and Islamic Studies",
	"MUSE": "Museum Studies",
	"MUSI": "Music",
	"NAST": "Native American Studies",
	"NASC": "Natural Science",
	"NEUR": "Neuroscience",
	"PCON": "Peace and Conflict Studies",
	"PHIL": "Philosophy",
	"PHYS": "Physics",
	"POSC": "Political Science",
	"PSYC": "Psychology",
	"RELG": "Religion",
	"REST": "Russian and Eurasian Studies",
	"SOSC": "Social Sciences",
	"SOCI": "Sociology",
	"SPAN": "Spanish",
	"THEA": "Theater",
	"UNST": "University Studies",
	"WMST": "Women’s Studies",
	"WRIT": "Writing and Rhetoric",
	"FSEM": "First year seminar",
	"HUMN": "Test",
	"LCTL": "Less Commonly Taught Languages"
}

semester_links = open("colgate_links.csv", "r").read()
semester_links = semester_links.split(";")

#prints classes/students for each semester through Fall 2015 to Spring 2021
def access_data(classes=False, students=False, location=None):
	complete_dict={}
	
	for link in range(len(semester_links)):
		if location==None:
			page = requests.get(semester_links[link])
		else:
			page = requests.get(location)

		result_dict = json.loads(page.text)
		counting_dict = {}

		for x in department_dict:
			counting_dict[x]=0

		if (classes==True):
			for x in result_dict:
				counting_dict[x["DISPLAY_KEY"][:4]]+=1

		elif (students==True):
			for x in result_dict:
				counting_dict[x["DISPLAY_KEY"][:4]]+=int(x["SEATS"][:x["SEATS"].find("/")])
				#print(int(x["SEATS"][:x["SEATS"].find("/")]))

		elif (classes==False and students==False):
			return "You gotta make either classes or students True in parameters"

		complete_dict[result_dict[0]["TERM_CODE"]]=counting_dict.items()

	#print("Year: %s, %s semester" % (result_dict[0]["TERM_CODE"][:4], result_dict[0]["TERM_CODE"][-1]))
	#print(sorted(counting_dict.items(), key=lambda x: x[1], reverse=True))
	#print()
	return complete_dict


#print(counting_classes(students=True)["201801"])
#counting_classes()
#print(counting_students()["201801"])




		



