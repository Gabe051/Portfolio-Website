import sys
import tkinter as tk
import time
from tkinter import filedialog
from tkinter import simpledialog as simpledialog
from pathlib import Path
import subprocess

root = tk.Tk()
root.withdraw()

file_path = filedialog.askdirectory()
if not file_path:
    sys.exit()
    
print("Folder selected: "+file_path)
folder = Path(file_path)
images = [ image for image in folder.iterdir() if image.suffix.lower() in {".png", ".jpg", ".jpeg"}]

base_folder = Path.cwd()
full_folder = base_folder / "images" / "full" / folder.name
thumbnail_folder = base_folder / "images" / "thumbnail" / folder.name

full_folder.mkdir(parents=True, exist_ok=True)
thumbnail_folder.mkdir(parents=True, exist_ok=True)

image_names = []

portfolio_title = simpledialog.askstring("Enter Name","Enter a name for the Portfolio Section:")

print("Converting images to full and thumbnail ...")
for image in images:
    webpimage = image.with_suffix(".webp")
    output = full_folder / webpimage.name 
    
    subprocess.run(["magick", str(image), "-quality", "92", str(output)], check=True)
    output = thumbnail_folder / webpimage.name
    subprocess.run(["magick", str(image), "-resize", "25%", "-quality", "92", str(output)], check=True)
    image_names.append(webpimage.name)
    print(image)  
print("Finished!")

section_name = folder.name
section_open_html = (
    f"            <hr>"
    f"            <section>\n"
    f"                <h3>{portfolio_title}</h3>\n"
    f"                <div class=\"gallery\">\n"
)


images_html = ""
for name in image_names:
    images_html += (
    f'                    <img loading="lazy" ' 
    f'src="images/Thumbnail/{section_name}/{name}" '
    f'data-full="images/Full/{section_name}/{name}">\n'
    )


section_close_html = (
    f'                </div>\n'
    f'                <hr>\n'
    f'            </section>\n'
    f'            <!--lastsection-->'
)

full_image_html = section_open_html + images_html + section_close_html

print("Building HTML")
html_path = base_folder / "index.html"

with html_path.open("r", encoding='utf-8') as html_file:
    source_code = html_file.read()

source_code = source_code.replace("<!--lastsection-->", full_image_html,1)

with html_path.open("w", encoding='utf-8') as html_file:
    html_file.write(source_code)

print("DONE!")
time.sleep(10)