import requests


token = "" # settings > integrations tokens > get integration token

url = "https://api.medium.com/v1"

header = {
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8",
    "Accept-Encoding": "gzip, deflate, br",
    "Accept-Language": "en-US,en;q=0.5",
    "Connection": "keep-alive",
    "Host": "api.medium.com",
    "TE": "Trailers",
    "Upgrade-Insecure-Requests": "1",
    "User-Agent": "Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:89.0) Gecko/20100101 Firefox/89.0"
}


if __name__ == "__main__":
    from pprint import pprint

    # getUserId
    response = requests.get(
        url=url + "/me",
        headers=header,
        params={"accessToken": token}
    )

    if response.status_code == 200:
        pprint(response.json())
        print('- - - - ')
        response_json = response.json()
        userId = response_json["data"]["id"]

    # getPublications
    response = requests.get(
        url=f"{url}/users/{userId}/publications",
        headers=header,
        params={"accessToken": token}
    )

    if response.status_code == 200:
        pprint(response.json())
        print('- - - - ')

    # listContributions
    response = requests.get(
        url=f"{url}/users/{userId}/publications",
        headers=header,
        params={"accessToken": token}
    )

    if response.status_code == 200:
        publications = response.json()["data"]

        for publication in publications:
            publicationId = publication["id"]
            response = requests.get(
                url=f"{url}/publications/{publicationId}/contributors",
                headers=header,
                params={"accessToken": token}
            )
            pprint(response.json())
            print('- - - - ')
