# import OS module
import os
import shutil
import json
from pathlib import Path


class Rp_folders:
	
	#---------------------methos to generate all rp folder list-----------------------------#
	def return_rps_folder_list(self, dirpath):

		# self.path = input('input the directory to return all rp folders_list: ')
		self.path = dirpath
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
		full_list = dict()
		rps_dict = dict()
		path = self.path
		#---------loop through the rps folders list generated earlier------------#
		for names in rps_folders:
			full_rps_path = names
			cleaned_part2 = names.split("/")
			rps_list = list()

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

	#-------#----------#----------#---------#---------#
	def group_rps(
		self,
		rp_json_data : str
	) -> dict():

		rp_file = open(rp_json_data)
		# returns JSON object as a dictionary
		data = json.load(rp_file)
		extrct_rp_grp = {itm.split("/")[0].split(" ")[0]:[] for itm in data.keys()}
		for itm in data.keys():
			extrct_rp_grp[itm.split("/")[0].split(" ")[0]].append(itm) 
		
		json_object = json.dumps(extrct_rp_grp, indent=4)
		jsonFile = open('json_files/{0}_grouped_rps_.json'.format('dnlectures2'), 'w')
		jsonFile.write(json_object)
		jsonFile.close()
		
		return extrct_rp_grp
	
	def rps_and_subdirs(self, rps_data: list):

		# init_rps_dict = {rps.split("/")[-1]:{} for rps in rps_data}
		walked_data = dict()
		# for rps in Path(rps_data).iterdir():
		# 	if rps.is_dir():
		# 		full_sub_path = rps+''
		# 		new_rps_data[rps] = {}
		# 		self.rps_and_subdirs(rps_data)
		for rp_dir in rps_data:
			for root, subdirs, files in os.walk(rp_dir):
				# walked_data[root] = {subdirs:""}
				print(dict(subdirs))
				


		# scrape_rps_dict = {rps_dir.split("/")[-1]:{dir.as_posix().split("/")[6]} for rps_dir in rps_data for dir in Path(rps_dir).iterdir() if dir.is_dir() }




# /Users/Umarvee/Documents/DN/posting_automation/rp_json_file_generator.py

if __name__ == "__main__":
	caller = Rp_folders()
	# caller.return_all_rps_subdirectories()
	# caller.convert_folders_to_json()
	# print(caller.group_rps('json_files/dnlectures2_rp_folders.json'))
	caller.rps_and_subdirs(['/Users/Umarvee/Documents/DN/posting_automation/'])
