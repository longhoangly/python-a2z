#!/etc/python

import requests
import json

def get_list_of_restaurants():
    rests = requests.get(
        url="https://jsonmock.hackerrank.com/api/restaurants?page=1",
        headers={"content-type": "application/json"},
        verify=False,
    )
    total_pages = rests.json()["total_pages"]  # 27 pages
    # list of json objects, each object is a restaurant info
    restaurants = rests.json()["data"]

    for i in range(2, total_pages + 1):
        tmp_rests = requests.get(
            url=f"https://jsonmock.hackerrank.com/api/restaurants?page={i}",
            headers={"content-type": "application/json"},
            verify=False,
        )
        # concat all other pages' data
        restaurants += tmp_rests.json()["data"]

    with open("restaurants.json", "w") as file:
        file.write(json.dumps(restaurants))


def get_highest_rating_rests(json_path, city, budget):
    restaurants = []
    with open(json_path, 'r') as file:
        restaurants = json.loads(file.read())

    # list of restaurants within the city, and less then the budget
    filtered_rests = [
        r for r in restaurants if city == r["city"] and r["estimated_cost"] <= budget
    ]
    # get max_rating_restaurant obj
    try:
        max_rest = max(filtered_rests, key= lambda r: r["user_rating"]["aggregate_rating"])
    except:
        raise ValueError(f"No restaurant found within city {city} and under the budget {budget}")
    # get max_rating value e.g 4.7
    max_rating = max_rest["user_rating"]["aggregate_rating"]

    # get all restaurants within city & bugdet have same max_rating
    max_rating_rests = [
        r for r in filtered_rests if r["user_rating"]["aggregate_rating"] == max_rating
    ]
    return max_rating_rests

def get_lowest_code_rests(max_rating_rests):
    lowest_rest = min(max_rating_rests, key=lambda r: r["estimated_cost"])
    lowest_cost = lowest_rest["estimated_cost"]

    lowest_cost_rests = [r for r in max_rating_rests if lowest_cost == r["estimated_cost"]]

    print(lowest_cost_rests)
    return lowest_cost_rests


# get_list_of_restaurants()   # only run one time
max_rating_rests = get_highest_rating_rests("./restaurants.json", "bangalore", 400)
get_lowest_code_rests(max_rating_rests)