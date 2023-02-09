import requests

def return_vehicles(page_number=1):
    """Returns a JSON from the Response."""

    url = f"https://swapi.dev/api/vehicles/?page={page_number}"

    response = requests.get(url=url)

    results = response.json()["results"]

    return results


def list_manufacturers():
    """Returns a list of five unique manufacturers."""

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


def manufacturers_list_comprehension():
    """Same logic as list_manufacturers() but done with list comprehension."""

    manufacturers = set()
    page_number = 1

    while len(manufacturers) < 5:
        results = return_vehicles(page_number)
        manufacturers.update(
            result["manufacturer"].strip().title() for result in results if len(manufacturers) < 5
        )
        page_number += 1

    return sorted(manufacturers)


def print_results():
    manufacturers = list_manufacturers()
    list_comprehension = manufacturers_list_comprehension()

    print(f"Results: \n{manufacturers}")
    print(f"Results with list comprehension: \n{list_comprehension}")


print_results()