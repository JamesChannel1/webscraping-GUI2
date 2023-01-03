import tkinter as tk
import time
from bs4 import BeautifulSoup
import requests
import io
from PIL import Image, ImageTk
import os
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService

service = ChromeService(executable_path='C:\Program Files (x86)\chromedriver.exe')
driver = webdriver.Chrome(service=service)

main = tk.Tk()
main.geometry("300x300")
main.title("webscraping images tool")

l = tk.Label(main, text="Enter URL:")
l.pack()
entry = tk.Entry(width=50)
entry.pack()



def fun0a():
    url = entry.get()
    r = requests.get(url)
    soup = BeautifulSoup(r.content, "html.parser")
    image_tags = soup.find_all("img")
    driver.get(url)
    time.sleep(5)
    soup = BeautifulSoup(r.content, "html.parser")
    image_tags = soup.find_all("img")
    os.makedirs("images", exist_ok=True)
    time.sleep(0.5)
    for image in image_tags:
        # Skip the image if it doesn't have a src attribute
        if "src" in image.attrs and image["src"].strip():
            img_url = image["src"]
        else:
            continue
        if not img_url.startswith("http"):
            continue
        img_data = requests.get(img_url).content
        with open(f"images/{img_url.split('/')[-1]}", "wb") as f:
            f.write(img_data)
        image = Image.open(io.BytesIO(img_data))
        photo = ImageTk.PhotoImage(image)
        l.config(image=photo)
        l.image = photo
        main.update()


def fun3a():
    fun0a()


b2 = tk.Button(main, text="Click", command=fun3a)
b2.pack()

main.mainloop()
