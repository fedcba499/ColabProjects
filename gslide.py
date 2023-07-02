#-*- coding: utf-8 -*-

import os, time
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
from selenium import webdriver
from PIL import Image

def capture_gslide(gslide_url):
    driver = webdriver.Chrome()
    driver.implicitly_wait(10)
    driver.get(gslide_url)
    time.sleep(3)

    title = driver.title.split('.',1)[0]

    # get the number of slides
    actions = ActionChains(driver)
    actions.send_keys(Keys.END)
    actions.perform()
    max_page = int(driver.current_url.rsplit('.',1)[-1][1:])
    print("Total Number of Slides: " + str(max_page))
    time.sleep(3)

    # start the presentation
    keys = Keys()
    actions = ActionChains(driver)
    actions.send_keys(keys.CONTROL + keys.SHIFT + keys.F5)
    actions.key_down(keys.SHIFT).key_down(keys.CONTROL).send_keys(keys.F5)
    actions.perform()
    time.sleep(8)

    # move to next page until the end
    actions = ActionChains(driver)
    counter = 1
    image_list = []
    save_folder = "C:\\"+ title
    os.mkdir(save_folder)

    while counter <= int(max_page):
        if counter > int(driver.current_url.rsplit('.',1)[-1][1:]):
            counter -= 1 
        fname = '{}.png'.format(str(counter).zfill(2))
        pdfname = title + ".pdf"
        save_dir = os.path.join(save_folder, fname)
        save_pdf = os.path.join(save_folder, pdfname)
        driver.save_screenshot(save_dir)
        print('Page '+str(counter) + ' was captured.')

        im = Image.open(save_dir)
        image = im.convert('RGB')
        image_list.append(image)        

        if(counter == max_page):
            image_list[0].save(save_pdf, save_all=True, append_images=image_list[1:])

        counter = int(driver.current_url.rsplit('.',1)[-1][1:])+1

        actions.click()
        actions.perform()

        time.sleep(2)       


    print('Done')

url = input("Please enter Google Slides Link - ")

capture_gslide(url)