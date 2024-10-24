from data import Circle, Book, Point
import math

# Part 1
# Write your functions for each part in the space below.
# Counts the number of vowels in the given word.
# Parameters:word (str): The input string to check for vowels.
# Returns: int: The number of vowels found in the input word.
def vowel_count(word:str):
    count=0
    vowels="aeiouAEIOU"
    for x in word:
        if x in vowels:
            count+=1
    return count

# Part 2
# Filters and returns sublists from the input list where each sublist contains exactly 2 integers.
# Parameters: lists (list[list[int]]): A list of sublists, where each sublist contains integers.
# Returns: list[list[int]]: A list containing only sublists with exactly 2 integers.
def shorts_list(lists:list[list[int]]):
    shorts=[]
    for idx in lists:
        if len(idx)==2:
            shorts.append(idx)
    return shorts

# Part 3
# Sorts all sublists of length 2 in ascending order and returns the modified list of sublists.
# Parameters: lists (list[list[int]]): A list of sublists, where each sublist contains integers.
# Returns: list[list[int]]: The original list with all sublists of length 2 sorted in ascending order.
def ascending_pairs(lists:list[list[int]]):
    new_lists=[]
    for idx in range(len(lists)):
        if len(lists[idx]) == 2:
            lists[idx].sort()
            new_lists.append(lists[idx])
        else:
            new_lists.append(lists[idx])
    return new_lists

# Part 4
# Adds the prices of two items, including dollars and cents, and returns the total sum.
# Parameters: item1 (Item): The first item with dollars and cents attributes.
# item2 (Item): The second item with dollars and cents attributes.
# Returns: float: The total price of the two items.
def add_prices(item1,item2):
    sum=0
    cents=(item1.cents+item2.cents)/100
    if cents>=1:
        sum+=1
        cents-=1
    sum=sum+item1.dollars+item2.dollars+cents
    return sum

# Part 5
# Calculates the area of a rectangle using the coordinates of its top-left and bottom-right corners.
# Parameters: rectangle (Rectangle): A rectangle object with top_left and bottom_right attributes.
#Returns: float: The area of the rectangle.
def rectangle_area(rectangle):
    return abs(rectangle.top_left.x-rectangle.bottom_right.x)*abs(rectangle.bottom_right.y-rectangle.top_left.y)

# Part 6
# Returns a list of book titles by the specified author.
# Parameters:author (str): The name of the author to search for.
# books (list[Book]): A list of Book objects, each with an authors attribute.
# Returns:list[str]: A list of titles of books written by the specified author.
def books_by_author(author:str,books:list[Book]):
    list_by_author = []
    for book in books:
        for i in book.authors:
            if author == i:
                list_by_author.append(book.title)
    return list_by_author

# Part 7
# Creates a circle that bounds a given rectangle, with the circle's center at the rectangle's center
# and its radius calculated from the center to one of the rectangle's corners.
# Parameters: rectangle (Rectangle): A rectangle object with top_left and bottom_right attributes.
#Returns:Circle: A circle object with a center and radius that bounds the rectangle.
def circle_bound(rectangle):
    center_x=(rectangle.bottom_right.x+rectangle.top_left.x)/2
    center_y=(rectangle.top_left.y+rectangle.bottom_right.y)/2
    center=Point(center_x,center_y)
    radius=math.sqrt((center_x-rectangle.top_left.x)**2+(center_y-rectangle.top_left.y)**2)
    return Circle(center,radius)

# Part 8
#Returns a list of employee names who are paid below the average pay rate in the provided list of employees.
#Parameters:employee_list (list[Employee]): A list of Employee objects, each with a pay_rate attribute.
#Returns:list[str]: A list of names of employees whose pay rate is below the average.
def below_pay_average(employee_list):
    total_pay=0
    underpaid=[]
    for employee in employee_list:
        total_pay+=employee.pay_rate
    average_pay=total_pay/len(employee_list)
    for employee in employee_list:
        if employee.pay_rate<average_pay:
            underpaid.append(employee.name)
    return underpaid
