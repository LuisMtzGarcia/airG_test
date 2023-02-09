import requests

def return_vehicles(page_number=1):
    """Returns a JSON from the Response."""

    url = f"https://swapi.dev/api/vehicles/?page={page_number}"

    response = requests.get(url=url)

    results = response.json()["results"]

    return results


def list_manufacturers():

    manufacturers = set()
    page_number = 1

    while len(manufacturers) < 5:
        results = return_vehicles(page_number)
        for result in results:
            manufacturer = result["manufacturer"].strip().title()
            if len(manufacturers) < 5:
                manufacturers.add(manufacturer)
        page_number += 1
    
    return list(sorted(manufacturers))


print(list_manufacturers())