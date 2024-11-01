import tkinter as tk
from tkinter import filedialog
import csv
import os
import pandas as pd
from selenium import webdriver

from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import pandas as pd
from selenium import webdriver
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import pandas as pd
driver = webdriver.Chrome()
driver = webdriver.Chrome()
import random

def open_source_file():
    global source_path
    source_path = filedialog.askopenfilename(filetypes=[("CSV Files", "*.csv")])
    if source_path:
        source_label.config(text="Source File: " + source_path)

def open_destination_folder():
    global destination_folder
    destination_folder = filedialog.askdirectory()
    print(destination_folder)
    if destination_folder:
        destination_label.config(text="Destination Folder: " + destination_folder)

def read_and_save():
    if source_path and destination_folder:
        filename = os.path.basename(source_path)
        destination_path = os.path.join(destination_folder, filename)

        with open(source_path, newline='') as csvfile, open(destination_path, 'w', newline='') as outputfile:
            
            csv_reader = pd.read_csv(csvfile)
            stocks=list(csv_reader['Symbol'])
            for i in stocks:
                url='https://in.tradingview.com/chart/?symbol=NSE%3A{}'
                driver.get(url.format(i))
                # driver.find_element(By.XPATH, '//*[@id="header-toolbar-intervals"]/button').click()
                
                # driver.find_element(By.XPATH,'//*[@id="overlap-manager-root"]/div/span/div[1]/div/div/div/div[24]/div').click()
                time.sleep(random.randint(7, 15))
                driver.save_screenshot(destination_folder+'/{}.png'.format(i))
                status_label.config(text=i)

               
    else:
        status_label.config(text="Please select source file and destination folder.")

root = tk.Tk()
root.title("CSV File Copy")

source_path = ""
destination_folder = ""

source_button = tk.Button(root, text="Select Csv  File which contain symobol Column", command=open_source_file)
source_button.pack(padx=20, pady=10)

destination_button = tk.Button(root, text="Select Destination Folder", command=open_destination_folder)
destination_button.pack(padx=20, pady=10)

source_label = tk.Label(root, text="Source File: ")
source_label.pack()

destination_label = tk.Label(root, text="Destination Folder: ")
destination_label.pack()

copy_button = tk.Button(root, text="Scan The Chart", command=read_and_save)
copy_button.pack(padx=20, pady=10)

status_label = tk.Label(root, text="")
status_label.pack()

root.mainloop()
