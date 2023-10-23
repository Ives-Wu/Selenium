import json

cookies_path = 'C:/Program Files/Python3/My_Python_Project/1023cookies.txt'
with open(cookies_path, 'r') as f:
    cookies = json.load(f)

# It seems only need to load 'name' and 'value' if you just want to load cookies for login, but it still to be verified.
"""""
n,d = [],{}
for c in cookies:
    d["name"] = c["name"]
    d["value"] = c["value"]
    n.append(d)
"""""

# In Selenium, the sameSite attribute value should typically be "Strict," "Lax," or "None."
# If you encounter an AssertionError when loading cookies, it means that some of the cookies contain an unsupported sameSite value.
for c in cookies:
    if "sameSite" in c and c["sameSite"] not in ["Strict", "Lax", "None"]:
        c["sameSite"] = "Lax"
        
with open(cookies_path, 'w') as f:
    json.dump(cookies, f)