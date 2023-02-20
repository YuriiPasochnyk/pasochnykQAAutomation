import requests


class GitHub:

    def get_user(self, usernam):
        r = requests.get(f"https://api.github.com/users/{usernam}")
        body = r.json()

        return body

    def search_repo(self, name):
        r = requests.get("https://api.github.com/search/repositories",
        params={"q": name}
        )
        body = r.json() 

        return body   