# import OS module
import os
import shutil
import json
from pathlib import Path


class Rp_folders:
	
	#---------------------methos to generate all rp folder list-----------------------------#
	def return_rps_folder_list(self, path):

		# self.path = input('input the directory to return all rp folders_list: ')
		self.path = path
		rps_folders = list()
		
		#print subdirectories only
		for path in Path(self.path).iterdir():
			if path.is_dir():
				rps_folders.append(path.as_posix())
		return rps_folders
		

	#-------#----------#----------#---------#---------#
	#---------methos to return a list of all subdirectories in the rps folders------------------#
	def return_all_rps_subdirectories(self):

		# Get the list home directory
		rps_folders = self.return_rps_folder_list()
		print(rps_folders)
		print()
		full_list = []
		rps_dict = dict()

		path = self.path

		#---------loop through the rps folders list generated earlier------------#
		for names in rps_folders:
			full_rps_path = names
			cleaned_part2 = names.split("/")
			#print(full_rps_path)
			print()
			rps_list = list()
			#rps_dict = dict()

			#loop through path & print subdirectories only
			for path2 in Path(full_rps_path).iterdir():
				if path2.is_dir():
					cleaned_part = path2.as_posix().split("/")
					rps_list.append(cleaned_part[6])

			#---------assign rp list to a dictionary----------#
			# rps_dict[f"{names}"] = rps_list
			rps_dict["{0}".format(cleaned_part2[5])] = rps_list
			#full_list.append(rps_dict)

		return rps_dict

	#-------#----------#----------#---------#---------#
	#--------methos to convert the generated list of rp's dictionaries to a json data-----#
	def convert_folders_to_json(self):
		full_list = self.return_all_rps_subdirectories()

		json_object = json.dumps(full_list, indent=4)
		print(json_object)
		
		dir_name_split = self.path.split("/")
		print(dir_name_split)
		jsonFile = open('{0}_rp_folders.json'.format(dir_name_split[4]), 'w')
		jsonFile.write(json_object)
		jsonFile.close()


if __name__ == "__main__":
	caller = Rp_folders()
	#caller.return_all_rps_subdirectories()
	caller.convert_folders_to_json()
