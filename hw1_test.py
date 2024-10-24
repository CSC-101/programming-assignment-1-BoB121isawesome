import data
import hw1
import unittest
from data import Price,Point,Rectangle

# Write your test cases for each part below.

class TestCases(unittest.TestCase):
    # Part 1
    def test_vowel_count_test(self):
        input="How much wood would a woodchuck chuck?"
        expected=11
        self.assertEqual(hw1.vowel_count(input), expected)

    def test_vowel_count_test_2(self):
        input="aUdiO test"
        expected=5
        self.assertEqual(hw1.vowel_count(input), expected)

    # Part 2
    def test_short_lists(self):
        input=[[2,3],[2,3,1],[5,3],[0]]
        expected = [[2,3],[5,3]]
        self.assertEqual(hw1.shorts_list(input), expected)

    def test_short_lists_2(self):
        input=[[6,21,5],[2,3,1],[2,6],[0],[2,52]]
        expected = [[2,6],[2,52]]
        self.assertEqual(hw1.shorts_list(input), expected)


    # Part 3
    def test_ascending_pairs(self):
        input=[[2,3],[2,3,1],[5,3],[23,3]]
        expected=[[2,3],[2,3,1],[3,5],[3,23]]
        self.assertEqual(hw1.ascending_pairs(input), expected)

    def test_ascending_pairs_2(self):
        input=[[6,2],[1,5,2,3,1],[36,2],[23,3]]
        expected=[[2,6],[1,5,2,3,1],[2,36],[3,23]]
        self.assertEqual(hw1.ascending_pairs(input), expected)

    # Part 4
    def test_add_prices(self):
        item1=Price(2,64)
        item2=Price(5,43)
        expected=8.07
        self.assertEqual(expected,hw1.add_prices(item1,item2))

    def test_add_prices_2(self):
        item1=Price(10632,99)
        item2=Price(501,42)
        expected=11134.41
        self.assertEqual(expected,hw1.add_prices(item1,item2))

    # Part 5
    def test_rectangle_area(self):
        rectangle = data.Rectangle(Point(-1, -2),Point(4,0))
        expected=10
        self.assertEqual(expected,hw1.rectangle_area(rectangle))

    def test_rectangle_area_2(self):
        rectangle = data.Rectangle(Point(5, -20),Point(-23,-2))
        expected=504
        self.assertEqual(expected,hw1.rectangle_area(rectangle))

    # Part 6
    def test_books_by_author(self):
        book1 = data.Book(["Dr.Suess"], "Cat in the Hat")
        book2 = data.Book(["Dr.Suess"], "All the Places You'll Go")
        book3 = data.Book(["Dr.Suess","Dr.Suess Friend"], "The Lorax")
        book4 = data.Book(["Bob"], "Bob's Book")
        author="Dr.Suess"
        book_list = [book1,book2,book3,book4]
        self.assertEqual(["Cat in the Hat","All the Places You'll Go","The Lorax"],hw1.books_by_author(author,book_list))

    def test_books_by_author_2(self):
        book1 = data.Book(["Nroom"], "Cat in the Hat")
        book2 = data.Book(["#1 Author", "Nroom"], "All the Places You'll Go")
        book3 = data.Book(["Dr.Suess","Dr.Suess Friend"], "The Lorax")
        book4 = data.Book(["Nroom"], "Nroom's Book")
        author="Nroom"
        book_list = [book1,book2,book3,book4]
        self.assertEqual(["Cat in the Hat","All the Places You'll Go","Nroom's Book"],hw1.books_by_author(author,book_list))

    # Part 7
    def test_circle_bound(self):
        top_left_point=Point(0,6)
        bottom_right_point=Point(8,0)
        inside_rectangle = Rectangle(top_left_point,bottom_right_point)
        expected=data.Circle(Point(4,3),5)
        self.assertEqual(expected,hw1.circle_bound(inside_rectangle))

    def test_circle_bound_2(self):
        top_left_point=Point(-7,16)
        bottom_right_point=Point(9,-14)
        inside_rectangle = Rectangle(top_left_point,bottom_right_point)
        expected=data.Circle(Point(1,1),17)
        self.assertEqual(expected,hw1.circle_bound(inside_rectangle))

    # Part 8
    def test_below_pay_average(self):
        employee1= data.Employee("Bob", 16)
        employee2= data.Employee("Dr.Suess", 7)
        employee3= data.Employee("Jeff", 13)
        employee4= data.Employee("Nobody", 28)
        employee_list=[employee1,employee2,employee3,employee4]
        expected=["Dr.Suess","Jeff"]
        self.assertEqual(expected,hw1.below_pay_average(employee_list))

    def test_below_pay_average_2(self):
        employee1= data.Employee("Bob", 14)
        employee2= data.Employee("Dr.Suess", 15)
        employee3= data.Employee("Jeff", 17)
        employee4= data.Employee("Nobody", 21)
        employee_list=[employee1,employee2,employee3,employee4]
        expected=["Bob","Dr.Suess"]
        self.assertEqual(expected,hw1.below_pay_average(employee_list))

if __name__ == '__main__':
    unittest.main()
