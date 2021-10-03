from ursina import * 
from random import randint

def update():
    global apple_dy, score, basket_dx
    apple.y = apple.y + time.dt * apple_dy

    basket.x = basket.x + held_keys["right arrow"] * time.dt * basket_dx
    basket.x = basket.x - held_keys["left arrow"] * time.dt * basket_dx

    hit_info = apple.intersects()
    if hit_info.hit:
        Audio("thud2.wav")
        apple.x = randint(-4, 4)
        apple.y = 4
        score += 1
        print_on_screen(f"Apples Caught: {score}", position = (-.8, .45), scale = 2, duration = 2)

    if apple.y < -4:
        Audio("lost.wav")
        print_on_screen("Oops! You Lost. Let's Restart", position = (0, 0), origin = (0, 0), scale = 4, duration = 3)
        score = 0
        apple.x = randint(-4, 4)
        apple.y = 10    


# Creating Window
app = Ursina()

left_wall = Entity(model = "quad", color = color.white, scale = (.6, 10), position = (-7, 0, 0))
right_wall = duplicate(left_wall, x = 7)

apple = Entity(model = "quad", texture = "apple4.png", position = (randint(-4, 4), 10), collider = "box")
basket = Entity(model = "quad", texture = "basket.png", position = (0, -4), collider = "box")
apple_dy = -4
basket_dx = 5
score = 0


app.run()