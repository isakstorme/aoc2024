import sys
import requests

#run file with python inputloader {day_nbr}
url = "https://adventofcode.com/"
fetch_path = url + "2024/day/" + sys.argv[1] + "/input"
print(fetch_path)
file_path = "input/input" + sys.argv[1] + ".txt"
with open("session/session.txt") as cookie:
    session = cookie.read()
r = requests.get(fetch_path, cookies={"session": session})
with open(file_path, "w") as f:
    f.write(r.text)

