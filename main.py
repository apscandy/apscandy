import requests
from jinja2 import Environment, FileSystemLoader
import os

class Config:
    # auth_token = os.environ["API_KEY"]
    auth_token = "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"
    header = {'Authorization': 'Bearer ' + auth_token}
    url = "https://api.github.com/user/repos"

class Fetch:
    response = list(requests.request("GET", Config.url, headers=Config.header).json())
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