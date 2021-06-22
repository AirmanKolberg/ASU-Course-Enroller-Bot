from asu_requests import *
from twilio_functions import text_me
from time import sleep

# This number is just a test
test_course_num = '79462'


if __name__ == '__main__':

    # Get URL based on course number
    course_url = generate_page_url(test_course_num)
    seats_available = False

    while not seats_available:

        # Search for available seats
        available, total = get_course_seats(course_url)
        response = f"{available} of {total} seats open."

        # Show the results
        print(response)

        # When seats are available, notify me and end the while loop
        if available > 0:

            text_me(response)
            seats_available = True

        # Check every ten seconds
        sleep(10)
