import turtle
from prettytable import PrettyTable

timmy = turtle.Turtle()
timmy.shape("turtle")
timmy.color("green")
timmy.forward(100)
timmy.left(90)
timmy.forward(100)
timmy.left(90)
timmy.forward(100)
timmy.left(90)
timmy.forward(100)
timmy.left(90)
timmy.left(45)
timmy.forward(140)
timmy.left(90)
timmy.forward(70)
timmy.left(90)
timmy.forward(70)
timmy.left(90)
timmy.forward(140)




my_screen = turtle.Screen()

my_screen.exitonclick()

# table = PrettyTable()
# table.align = "c"
# table.field_names = ["Pokemon", "Type"]
# table.add_rows(
#   [
#     ["Pikachu", "Electric"],
#     ["Murkrow", "Flying/Dark"],
#   ]
# )
# print(table)