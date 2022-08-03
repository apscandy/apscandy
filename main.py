import requests
from jinja2 import Environment, FileSystemLoader
import os

auth_token = os.environ["API_KEY"]

header = {'Authorization': 'Bearer ' + auth_token}
url = "https://api.github.com/user/repos"

response = list(requests.request("GET", url, headers=header).json())
response = [i for i in response if i["private"] == False]

# print(response[0].keys())
# print(response[0].values())

template_env = Environment(loader=FileSystemLoader(searchpath="./templates"))
template_html = template_env.get_template("base.html")

def create_readme() -> None:
    with open("./README.md", "w") as static_page:
        static_page.write(
            template_html.render(api_data_list=response)
        )
create_readme()