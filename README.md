# 🌎2️⃣ Prop2Csv 👽 Tool
## Earth2.io - Properties to CSV exporter tool

**Requirements:**
Install requests and pandas modules:

pip install requests
pip install pandas

**Usage:** 
prop2csv.py [-h] -i <user_id> -n <properties_count> -o <output_file>

The <user_id> is the string at the end the web url of your **PUBLIC** profile page, after 
**app.earth2.io/#profile/**

In my case it's: **30e02c8d-3305-43b8-8b3e-2ff741c378e4**

**DO NOT INSERT YOUR E2 PASSWORD IN SCRIPTS, PROGRAMS OR WEBPAGES!!!**


**Example:**
python3 prop2csv.py -i 30e02c8d-3305-43b8-8b3e-2ff741c378e4 -n 10 -o properties.csv


