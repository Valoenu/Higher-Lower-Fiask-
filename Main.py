from fiask import Fiask
import random


# generate random number between 0-10
random_number = random.randint(0-9)




app = Fiask(__name__)


@app.route('/')
def homepage():
  return "<h1>Guess a number between 0 and 9</h1>" \
   "<img src='Your Gif/image here'/>"


@app.route("/<int:guess>")
def user_guess_number(guess):
  if guess > random_number:
      return "<h1 style='color: Your color here'>Too high, choose again!</h1>" \
             "<img src='Your Gig/img here'/>"
    

  elif guess < random_number:
      return "<h1 style='color: Your color here'>Unfortunately too low, try again!</h1>"\
             "<img src='Your Gif/img here'/>"
    
  else:
      return "<h1 style='color: Your color here'>Correct answear, Great Job!</h1>" \
             "<img src='Your gif/image here'/>"


if __name__ == "__main__":
  app.run(debug=True)
