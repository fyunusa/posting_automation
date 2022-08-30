import os
import json
from pathlib import Path
from rp_json_file_generator import Rp_folders


class PossibleNames:
    def __init__(
        self,
        parent: str,
        json: str
    ) -> None:

        self.parent_dir = parent
        self.json_file_name = json
        self.all_possible_names = dict()
    
    def scrape_root_dir(self) -> list():
        #-----return all rps folder in the root dir-----#
        rpcaller = Rp_folders()
        return rpcaller.return_rps_folder_list(self.parent_dir)

    def scrape_rp_dir(
        self,
        rpname: str,
        rpname_dict: dict,
    ) -> dict():

        """
            #-------------------ALGO--------------------#
            :param status 
                is used to detect when to terminate main while loop
            :param parsed_dir & parsed_files
                is used to store files that have been encountered to avoid multiple interaction

            Step1:: initialixe rpname dict with rpname and empty array as value
            Step2:: while len of each empty array above keep searching for possible name to add
            Step3:: checks for empty directory to terminate loop
            Step4:: encounter files and check if name is different from known names
            Step5:: encounter directory and dive in to check for other possible names
        """
        rpname_dict[rpname.split("/")[-1]] = []
        parsed_dir = []
        parsed_files = []

        while len(rpname_dict[rpname.split("/")[-1]]) < 5:
            if len(os.listdir(rpname)) == 0:
                print("empty directory")
                status = 0
            else:
                status = 1
                for itm in Path(rpname).iterdir():
                    if itm.as_posix().endswith('.mp3') and itm.as_posix() not in parsed_files:
                        parsed_files.append(itm.as_posix())
                        splitted_file_name = itm.as_posix().split("_")
                        xtracted_rp_name = splitted_file_name[0]
                        if xtracted_rp_name not in rpname_dict[rpname.split("/")[-1]]:
                            rpname_dict[rpname.split("/")[-1]].append(xtracted_rp_name)

                    elif itm.is_dir() and itm.as_posix() not in parsed_dir:
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

        """
            #-------------------ALGO--------------------#
            Step1:: load json data from file
            Step2:: loop through the json data to group by titles and initialixe dict
            Step3:: loop through the json data set rp lastname as begin of section in dict
            Step4:: loop through list in each json_data.keys nd swap positions btw child nd parent
        """
        #----------- returns JSON object as a dictionary-----------#
        open_data = open("{0}.json".format(json_file))
        data_load = json.load(open_data)
        #------extract rp grps by title and initialize empty dict------#
        extrct_rp_grp = {itm.split(" ")[0]:{} for itm in data_load.keys()}
        count = 0

        for rp in data_load.keys():

            try:
                extrct_rp_grp[rp.split(" ")[0]]["{0} -- {1} -- {2}".format(rp.split(" ")[-2],rp.split(" ")[-1], count)] = ""
            except IndexError:
                extrct_rp_grp[rp.split(" ")[0]]["{0} -- {1}".format(rp.split(" ")[-1], count)] = ""
            
            for name in data_load[rp]:
                extrct_rp_grp[rp.split(" ")[0]][name] = rp
            
            count = count + 1
            

        json_object = json.dumps(extrct_rp_grp, indent=4)
        jsonFile = open('json_files/_processed_possible_rp_names.json', 'w')
        jsonFile.write(json_object)
        jsonFile.close()
		

if __name__ == "__main__":
    caller = PossibleNames('/home/dawahnig/public_html/dnlectures2/', "possible_names")
    # caller.process_rootdir_content()
    caller.reformat_processed_data('possible_names_rp_folders')
