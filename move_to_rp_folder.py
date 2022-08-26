import json
import shutil
import os

#--------move files-----------------------#
def split_lecture_details():

    lec1 = ['Shaykh Qamarudeen Yunus_Public Lecture - Agboye Islam loro Awon Akanda Eda (Yoruba)_DN.amr',
    'Dr Muhammad Baba Assudany_Tafseer - Suratul Ahla [Q87] (21-02-22) (Hausa)_DN.mpeg',
    'Shaykh Muhammad Bn Uthmann_Ramadan Tafseer 1443 - Suratul Baqarah [Q2vs1-20] Day 001 (22-01-22) (Hausa)_DN']

    rp_name_list,rp_title_list,lec_title_list = [],[],[]

    for file in lec1:
        #--------split the filename to xtract lecture_category, rp_name, rp_title-------#
        splitted_file_name= file.split("_")
        splitted_file_name[1] = splitted_file_name[1].split("-")

        xtracted_rp_name = splitted_file_name[0]
        xtrctd_rp_lec_catg =  splitted_file_name[1][0] 

        splitted_rp_title = xtracted_rp_name.split(" ")
        xtracted_rp_title = splitted_rp_title[0]

        #---------append each rp_name, title, lec_title to equivalent list---------------#
        rp_name_list.append(xtracted_rp_name)
        rp_title_list.append(xtracted_rp_title)
        lec_title_list.append(xtrctd_rp_lec_catg)
    
    #-------return each list----------#
    return [lec_title_list, rp_title_list, rp_name_list]
#-------#----------#----------#---------#---------#

def  check_related_rp_names():
    # lec_title_list = split_lecture_details()[0]
    rp_title_list = split_lecture_details()[1]
    rp_name_list = split_lecture_details()[2]

    related_names_data = load_json_data()[2]

    #-----loop through the rp_title_list and search the json data using the each title as key---------#
    index = 0
    discovered_rp_names = []

    for title in rp_title_list:
        title_catg = related_names_data[title]
    
        #-----loop through the related names and look if the lecture rp_name
        #  exist in the related names and return the server folder rp name----#
        for catgry in title_catg:
            if rp_name_list[index] in catgry:
                print(f"the related name found for: {rp_name_list[index]} is :==> {catgry.get(rp_name_list[index])}")
                discovered_rp_names.append(catgry.get(rp_name_list[index]))
            else:
                print(f"no related name found for {rp_name_list[index]}")

        print()
        index = index + 1

    return discovered_rp_names
#-------#----------#----------#---------#---------#

def check_related_rp_subdirectories():      

    #------------collect the Dn & Dn2 json details------------#
    Dn_lec = load_json_data()[0]
    Dn_lec2 = load_json_data()[1]

    #---------collect the actual rp server folder names---------#
    rp_folder_name = check_related_rp_names()

    #--------collect each lecture title from lecture details-----------#
    lecture_title = split_lecture_details()[0]
  
  #--------loop through each jsons and return the right rp subfolders-----------#
    sub_folders_dict = {}
    index = 0
    for lec_title in lecture_title:
        try:
            print(f"searching for {rp_folder_name[index]} in Dn lecture...")
            print()
            search_rp = Dn_lec[rp_folder_name[index]]
            print(f"Located {rp_folder_name[index]} in Dn lectures with respective folders: {search_rp}")
            print()
        except Exception as e:
            print('failed to locate in DN1 rp: ',e)
            print(f'Now looking for {rp_folder_name[index]} in Dn lectures2...')
            print()
            
            try:
                search_rp = Dn_lec2[rp_folder_name[index]]
                print(f"Located {rp_folder_name[index]} in Dn lectures2 with respective folders: {search_rp}")
                print()

            except Exception as e:
                print('failed to locate in DN2 rp: ',e)
                print()

        sub_folders_dict["{0}".format(rp_folder_name[index])] = search_rp

        index = index + 1

    # print(sub_folders_dict)
    return sub_folders_dict
            
#-------#----------#----------#---------#---------#
def check_all_words(words1, word2):
    import re
    return all(re.search(r'\b{}\b'.format(word2), words1))

def chck_right_lect_dirtry():
    rps_sub_dirtry = check_related_rp_subdirectories()
    lec_title_list = split_lecture_details()[0]
    verified_rp_names = check_related_rp_names()

    print(lec_title_list)
    print()

    print(rps_sub_dirtry)
    print(verified_rp_names)
    print()


    # if any(check_all_words(diretry, lec_title_list[index].split(' '))):
    #     print(f"{rp}==>{diretry}")

    index = 0
    for rp in verified_rp_names:
        rp_sub_dirs = rps_sub_dirtry[rp]
        for diretry in rp_sub_dirs:
            # print('i am here........')
            # print(diretry)
            try:
                
                if any(check_all_words(diretry, lec_title_list[index].split(' '))):
                    print(f"{rp}==>{diretry}")
                else:
                    print(f"unable to find suitable match for {rp} ==> {diretry}")

            except Exception as e:
                print(e)
            
            index = index + 1


       
    # for diretry in rps_sub_dirtry:
    #     words = lec_title.split(" ")
    #     check_all = re.search(r'\b{}\b'.format(lec_title))

    pass

#-------#----------#----------#---------#---------#
def load_json_data():

    # Opening JSON file
    Dn1 = open('json_files/dnlectures_rp_folders.json')
    Dn2 = open('json_files/dnlectures2_rp_folders.json')
    Relate_names = open('json_files/related_names.json')

    #----------- returns JSON object as a dictionary-----------#
    data1 = json.load(Dn1)
    data2 = json.load(Dn2)
    data3 = json.load(Relate_names)
    
    
    # list
    # all_rps_dn1 = []
    # all_rps_dn2 = []
    # all_possible_names = []
    # print(data)

    #---------Iterating through the jsons---------#
    # for items1 in data1:
    #     all_rps_dn1.append(items1)
    
    # for items2 in data2:
    #     all_rps_dn2.append(items2)
    
    # for items3 in data3:
    #     all_possible_names.append(items3)

    
    # Closing file
    Dn1.close()
    Dn2.close()
    Relate_names.close()

    return [data1, data2,  data3]

if __name__ == "__main__":
    # print(load_json_data()[2])
    print(split_lecture_details()[2])
    # check_related_rp_names()
    # check_related_rp_subdirectories()
    # chck_right_lect_dirtry()
