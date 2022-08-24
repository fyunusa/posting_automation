# import OS module
import os
import shutil
import json


class Rp_folders:
	
	#---------------------methos to generate all rp folder list-----------------------------#
	def return_rps_folder_list(self):
		# path = "C:/Users/fyunu/OneDrive/Desktop/Gem_work/"

		self.path = input('input the directory to return all rp folders_list: ')

		rps_folders = list()

		#print subdirectories only
		for item in os.scandir(self.path):
			if os.path.isdir(item):
				rps_folders.append(item.name)
		
		return rps_folders
		

	#-------#----------#----------#---------#---------#
	#---------methos to return a list of all subdirectories in the rps folders------------------#
	def return_all_rps_subdirectories(self):

		# Get the list home directory
		# path = "C:/Users/fyunu/OneDrive/Desktop/Gem_work/"
		
		rps_folders = self.return_rps_folder_list()
		print(rps_folders)
		full_list = []

		path = self.path

		#---------loop through the rps folders list generated earlier------------#
		for names in rps_folders:
			full_rps_path = path+names
			print(full_rps_path)

			rps_list = list()
			rps_dict = dict()

			#loop through path & print subdirectories only
			for item in os.scandir(full_rps_path):
				if os.path.isdir(item):
					rps_list.append(item.name)

			#---------assign rp list to a dictionary----------#
			# rps_dict[f"{names}"] = rps_list
			rps_dict["{0}".format(names)] = rps_list
			full_list.append(rps_dict)

		return full_list

	#-------#----------#----------#---------#---------#
	#--------methos to convert the generated list of rp's dictionaries to a json data-----#
	def convert_folders_to_json(self):
		full_list = self.return_all_rps_subdirectories()

		json_object = json.dumps(full_list, indent=4)
		print(json_object)

		jsonFile = open('rp_folders.json', 'w')
		jsonFile.write(json_object)
		jsonFile.close()


if __name__ == "__main__":
	caller = Rp_folders()
	caller.convert_folders_to_json()


# "C:/Users/fyunu/OneDrive/Desktop/Gem_work/"