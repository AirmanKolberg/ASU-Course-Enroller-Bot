from asu_requests import *

test_num = '79462'


if __name__ == '__main__':

    # This number is just a test
    course_url = generate_page_url(test_num)
    available, total = get_course_seats(course_url)
    print(available)
    print(total)
