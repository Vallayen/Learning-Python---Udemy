from turtle import Turtle, Screen
import pandas
image = "blank_states_img.gif"
score_count = 0
wrong_count = 0


screen = Screen()
screen.title(f"Us game, {score_count}/50")
screen.addshape(image)
screen.tracer(0)
pic = Turtle()
pic.shape(image)
screen.update()


#screen update
def screen_update():
  screen.title(f"Us game, {score_count}/50 states guessed. {wrong_count} wrong guesses")
  screen.update()


#get input function
def get_answer():
  if guessed_states:  # If there are already guessed states, change the prompt
      prompt = "Guess another state or type 'exit' to quit:"
  else:
      prompt = "Name a state:"
  return screen.textinput(title=f"{score_count}/50 States Correct", prompt=prompt).title()

# get CSV of states
states = pandas.read_csv("50_states.csv")

#func to place answer
def place_answer(answer_state, xcor, ycor):
  place = Turtle()
  place.penup()
  place.speed("fastest")
  place.hideturtle()
  place.goto(xcor, ycor)
  place.write(answer_state)
  screen.update()
  
  #Guessed states
guessed_states = []
  
game = True
while game:
  if len(guessed_states) >= 50:
    game = False
    
  
  answer_state = get_answer()
  
  if answer_state == "Exit":
    result = []
    all_states = states.state.to_list()
    for i in all_states:
      if i not in guessed_states:
        result.append(i)
    df = pandas.DataFrame(result)
    df.to_csv('states to learn.csv', index=False)
    game = False
  
  if answer_state in guessed_states:
    continue
  
  if answer_state not in guessed_states:
    if answer_state in states["state"].values:
      correct = states[states.state == answer_state]
      xcor = int(correct["x"])
      ycor = int(correct["y"])
      score_count += 1
      guessed_states.append(answer_state)
      place_answer(answer_state=answer_state, xcor=xcor, ycor=ycor)
      screen_update()
      
    if answer_state not in states["state"].values:
      wrong_count += 1
      screen_update()
    
  
# states to learn
