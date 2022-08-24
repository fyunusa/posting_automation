# importing webdriver from selenium
from selenium import webdriver
# from  seleniumrequests import Chrome
from selenium.webdriver.common.keys import Keys


def generate_urls_for_posting1():
    pass

def generate_urls_for_posting2():
    pass

def sending_data_to_posting1():
    
    # driver = Chrome()
    driver = webdriver.Chrome(executable_path='chromedriver')

    # URL of website
    url = "https://media.dawahnigeria.com/scripts/php/posting1"

    # Album_id = input('input the Album ID to use in Posting1: ')
    # new_lec_qty = int(input('input the number of new quantities added: '))

    Album_id = "dnlectures2/Dr Tukur Adam Al-Manar (Kaduna)/Aqa'idus-Sufiyyah"
    new_lec_qty = 3

    # Opening the website
    driver.get(url)

    # contain input boxes
    textboxes1 = driver.find_elements_by_class_name("album_id")
    textboxes2 = driver.find_elements_by_class_name("qty")

    if textboxes1 and textboxes2:
        print('successfully found elements of tetbox1 and textbox2')
    else:
        print('omo me i no see textbox1 and 2 oooooooo')

     # Iterate through all input boxes
    for value in textboxes1:
        # enter value
        value.send_keys(Album_id)
 
    # Iterate through all textareas
    for value in textboxes2:
        # enter value
        value.send_keys(new_lec_qty)
    

    # getting the button by class name
    button = driver.find_element_by_class_name("submitter")
    print('tried to find button class now processing the button click function.')

    # clicking on the button
    try:
        generated_urls = []
        button.click()
        print('button clicked will generate urls now.....')

        gener_urls = driver.find_element_by_class_name("url")
        generated_urls.append(gener_urls.text)

        # Iterate through all urls
        # for value in generated_urls:
        #     # append to a list
        #     print(f'{value}\n')
            # generated_urls.append(value.text)
        
        # print(generated_urls)

    except Exception as e:
        print('unable to generate posting1 urls: ', e)
    
    return generated_urls
    # close the window
    # driver.close()


def sending_data_to_posting2():

    urls_to_post = ''
    posting1_data = sending_data_to_posting1()
    for links in posting1_data:
        #the urls to post and generate a csv file for
        urls_to_post += links
    
    print(urls_to_post)

    #setting download directory
    options = webdriver.ChromeOptions()
    prefs = {"download.default_directory" : "./csv_files_folder"}
    options.add_experimental_option("prefs",prefs)

    # driver = Chrome()
    driver = webdriver.Chrome(executable_path='chromedriver', chrome_options=options)

    # URL of website
    url = "https://media.dawahnigeria.com/scripts/php/posting2"

    # Opening the website
    driver.get(url)

    # contain input boxes
    textboxes1 = driver.find_elements_by_class_name("inputter2")
   
   #validating the checkbox
    if textboxes1:
        print('successfully found element of tetbox1')
    else:
        print('omo me i no see textbox1')
    
     # Iterate through input box
    for value in textboxes1:
        # enter value
        value.send_keys(urls_to_post)
 
    # getting the submit button by class name
    button = driver.find_element_by_class_name("submitter2")
    print('tried to find button class now processing the button click function.')

    # clicking on the button
    try:
        button.click()
        print('button clicked will generate csv now.....')
    except Exception as e:
        print('unable to generate csv: ', e)
    
    # close the window
    driver.close()

if __name__ == '__main__':
    # sending_data_to_posting1()
    sending_data_to_posting2()


# dpMY[A7oHc-

# home/dawahnig/public_html/dnlectures2