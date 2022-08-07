import requests
from jinja2 import Environment, FileSystemLoader
import os

class Config:
    auth_token = os.environ["API_KEY"]
    header = {'Authorization': 'Bearer ' + auth_token}
    api_url = "https://api.github.com/user/repos"
    user_url = "https://api.github.com/users/apscandy"

class Fetch:
    profile = requests.request("GET", Config.user_url).json()
    response = list(requests.request("GET", Config.api_url, headers=Config.header).json())
    response = [i for i in response if i["private"] == False]


class UpdateReadme:
    template_env = Environment(loader=FileSystemLoader(searchpath="./templates"))
    template_html = template_env.get_template("base.html")

    def create_readme() -> None:
        with open("./README.md", mode="w") as static_page:
            static_page.write(
                UpdateReadme.template_html.render(api_data_list=Fetch.response)
            )

if __name__ == "__main__":
    UpdateReadme.create_readme()