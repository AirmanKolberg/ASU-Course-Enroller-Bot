import requests
from bs4 import BeautifulSoup


# Returns (seats_open[int], total_seats[int])
def get_course_seats(url):

    # Set cookies parameter for BeautifulSoup
    cookies = {"onlineCampusSelection": "O"}

    # Parse the HTML data
    soup = BeautifulSoup(requests.get(url, cookies=cookies).content, "html.parser")

    # Grab the string of available seats (will return 'x of y' string, ie 12 of 100)
    results = soup.select_one(".availableSeatsColumnValue").get_text(strip=True, separator=" ")

    # Retrieve the two ints (available and total seats)
    split_results = results.split(' ')
    final_variables = (int(split_results[0]), int(split_results[2]))

    return final_variables


def generate_page_url(class_num):

    return f'https://webapp4.asu.edu/catalog/myclasslistresults?t=2217&k={class_num}&hon=F&promod=F&c=ASUONLINE&e=all&page=1'


if __name__ == '__main__':
    pass
