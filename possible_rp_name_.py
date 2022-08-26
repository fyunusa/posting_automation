import os
import shutil
import json
import json
from pathlib import Path
from rp_json_file_generator import Rp_folders

# /Users/Umarvee/Documents/DN/posting_automation/possible_rp_name_.py

class PossibleNames:

    def __init__(
        self,
        parent: str,
        json: str
    ) -> None:

        self.parent_dir = parent
        self.json_file_name = json
        self.all_possible_names = dict()
        # self.root_dir = "/home/dawahnig/public_html/"
    
    def scrape_root_dir(self) -> list():
        #-----return all rps folder in the root dir-----#
        rpcaller = Rp_folders()
        return rpcaller.return_rps_folder_list(self.parent_dir)

    def scrape_rp_dir(
        self,
        rpname: str,
        rpname_dict: dict,
    ) -> dict():

        #----initialixe rpname_dict with the rpname as key nd empty array as value
        rpname_dict[rpname.split("/")[-1]] = []
        # print(rpname.split("/")[-1])
        parsed_dir = []
        parsed_files = []

        while len(rpname_dict[rpname.split("/")[-1]]) < 5:
            # print("in the while loop......")
            if len(os.listdir(rpname)) == 0:
                print("empty directory")
                status = 0
            else:
                status = 1
                for itm in Path(rpname).iterdir():
                    if itm.as_posix().endswith('.mp3') and itm.as_posix() not in parsed_files:
                        parsed_files.append(itm.as_posix())
                        # print("item not in list of parsed files and is a file")
                        splitted_file_name = itm.as_posix().split("_")
                        xtracted_rp_name = splitted_file_name[0]
                        if xtracted_rp_name not in rpname_dict[rpname.split("/")[-1]]:
                            rpname_dict[rpname.split("/")[-1]].append(xtracted_rp_name)

                    elif itm.is_dir() and itm.as_posix() not in parsed_dir:
                        # print("item not in list of parsed directories and is a directory")
                        #----adding this to keep track of inner_dir that have been parsed----#
                        parsed_dir.append(itm.as_posix())
                        for file in os.listdir(itm.as_posix()):
                            if file.endswith('.mp3') and len(rpname_dict[rpname.split("/")[-1]]) < 5:
                                splitted_file_name = file.split("_")
                                xtracted_rp_name = splitted_file_name[0]
                                if xtracted_rp_name not in rpname_dict[rpname.split("/")[-1]]:
                                    rpname_dict[rpname.split("/")[-1]].append(xtracted_rp_name)
                            else:
                                pass
                    
                    elif itm.as_posix() in parsed_dir or itm.as_posix() in parsed_files:
                        status = 0
                        print("i am breaking....")
    
            
            if status == 0:
                break

                

        print("Done extracting possible names of {0}".format(rpname))
        print(" ")
    
        return rpname_dict

    def json_data_writer(self, content) -> None:
        jsonFile = open('{0}_rp_folders.json'.format(self.json_file_name), 'a')
        jsonFile.write(json.dumps(content, indent=4))
        # jsonFile.write(",")
        jsonFile.close()


    def process_rootdir_content(self) -> None:
        for itm in self.scrape_root_dir():
            print("Sent {0} for processing".format(itm))
            result = self.scrape_rp_dir(itm, self.all_possible_names)
        
        self.json_data_writer(result)
        print("Done generating possible rpnames check your json file for output")
    
    def reformat_processed_data(
        self,
        json_file: str
    ) -> None:

        #----------- returns JSON object as a dictionary-----------#
        open_data = open("{0}.json".format(json_file))
        data_load = json.load(open_data)
        print(data_load['Shaykh Abubakar Abbas Rijiyar Lemo (Kano)'])

if __name__ == "__main__":
    caller = PossibleNames('/home/dawahnig/public_html/dnlectures2/', "possible_names")
    # caller.process_rootdir_content()
    caller.reformat_processed_data('possible_names_rp_folders')

    # try_possible_names_rp_folders.json