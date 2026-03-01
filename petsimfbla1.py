# ==================================================
# IMPORTS
# ==================================================
import turtle as trtl
import random


# ==================================================
# SCREEN SETUP
# ==================================================
wn = trtl.Screen()

trtl.hideturtle()

wn.bgcolor("pink")


HATDOG = "DogBandana_Hat.gif"
DogBandana = "DogBandana.gif"
TennisBall = "TennisBall.gif"
RubberDuck = "RubberDuck.gif"
FBLACOIN = "FBLACOIN.gif"
Toy1btn = "TennisBall_btn.gif"
Hat1btn = "CowboyHat_button.gif"
Toy2btn = "duck_button.gif"
Toy4btn = "FBLABTN.gif"
HATCAT = "CatCollar_Hat.gif"
CatCollar = "CatCollar.gif"
Donut = "Donut.gif"
DonutBtn = "DonutBtn.gif"
x2H_btn = "2xHbtn.gif"
x4H_btn = "4xHbtn.gif"
x10H_btn = "10xHbtn.gif"
OGDOG = "OGDog.gif"
OGCAT = "OGCAT.gif"
food_button_img1 = "foodbutton1.gif"
food_button_img2 = "foodbutton2.gif"
playbutton1 = "playbutton1.gif"
OGSADCAT = "OGSadCat.gif"
OGSADDOG = "OGSadDog.gif"
CleanBTN = "cleanbutton1.gif"
Burger = "burger.gif"
BurgerBTN = "burgerbtn.gif"
EXIT = "ExitBTN.gif"
RestBTN = "restbtn.gif"
Workbtn ="workbtn.gif"
pet1btn ="pet1btn.gif"
pet2btn ="pet2btn.gif"
playbutton2 = "playbutton2.gif"



RIGHT_X = 310

# Register all shapes with the turtle screen
image_list = [
    HATDOG, DogBandana, TennisBall, Toy1btn, Hat1btn, HATCAT, CatCollar, Donut, DonutBtn, x2H_btn, x4H_btn, OGDOG, OGCAT, food_button_img1, food_button_img2,
    OGSADCAT, OGSADDOG, x10H_btn, playbutton1, CleanBTN, Toy2btn,RubberDuck,Toy4btn, FBLACOIN, Burger,BurgerBTN, EXIT,RestBTN,Workbtn, pet1btn,pet2btn, playbutton2
]

for img in image_list:
    wn.addshape(img)


#create turtle that writes titles
title_writer = trtl.Turtle()
title_writer.hideturtle()
title_writer.penup()


#create choose a dog turtle
button_turtle1 = trtl.Turtle()
button_turtle1.hideturtle() 
button_turtle1.shape(pet2btn)
button_turtle1.shapesize(8,8)
button_turtle1.penup()
button_turtle1.goto(0, 0) 

#create choose a cat turtle
button_turtle2 = trtl.Turtle()
button_turtle2.hideturtle() 
button_turtle2.shape(pet1btn)
button_turtle2.shapesize(8,8)
button_turtle2.penup()
button_turtle2.goto(0, 200) 


# interaction Buttons (Food, Play, Rest, Clean)
food_button = trtl.Turtle()
food_button.hideturtle()
food_button.shapesize(3)
food_button.penup()
food_button.goto(150, -200)

rest_button = trtl.Turtle()
rest_button.hideturtle()
rest_button.shape(RestBTN)
rest_button.shapesize(3)
rest_button.fillcolor("blue")
rest_button.penup()
rest_button.goto(-150, -200)

clean_button = trtl.Turtle()
clean_button.hideturtle()
clean_button.shape(CleanBTN)
clean_button.shapesize(3)
clean_button.penup()
clean_button.goto(0, -300)

play_button = trtl.Turtle()
play_button.hideturtle()
play_button.shapesize(3)
play_button.penup()
play_button.goto(0, -200)


#creates the happiness bar
happy_bar_drawer = trtl.Turtle()
happy_bar_drawer.hideturtle()
happy_bar_drawer.penup()
happy_bar_drawer.goto(RIGHT_X, 100)

#creates the hunger bar
hunger_bar_drawer = trtl.Turtle()
hunger_bar_drawer.hideturtle()
hunger_bar_drawer.penup()
hunger_bar_drawer.goto(RIGHT_X, 150)

#creates the energy bar
energy_bar_drawer = trtl.Turtle()
energy_bar_drawer.hideturtle()
energy_bar_drawer.penup()
energy_bar_drawer.goto(RIGHT_X, 200) 

#creates the hygiene bar
hygiene_bar_drawer = trtl.Turtle()
hygiene_bar_drawer.hideturtle()
hygiene_bar_drawer.penup()
hygiene_bar_drawer.goto(RIGHT_X, 250)

#creates the turtle responsible for messages and pet status
message_trtl = trtl.Turtle()
message_trtl.hideturtle()
message_trtl.penup()
message_trtl.goto(0, 250)

#toy in the shop
toy_button = trtl.Turtle()
toy_button.hideturtle()
toy_button.shape(Toy1btn)
toy_button.shapesize(2, 3)
toy_button.penup()
toy_button.goto(-200,25) 
toy_button.hideturtle()

#duck in the shop
toy2_button= trtl.Turtle()
toy2_button.hideturtle()
toy2_button.shape(Toy2btn)
toy2_button.shapesize(2, 3)
toy2_button.penup()
toy2_button.goto(-300, 25) 
toy2_button.hideturtle()

#toy3 in the shop
toy3_button= trtl.Turtle()
toy3_button.hideturtle()
toy3_button.shape(DonutBtn)
toy3_button.shapesize(2, 3)
toy3_button.penup()
toy3_button.goto(-200, 100) 
toy3_button.hideturtle()

#toy4 in the shop
toy4_button= trtl.Turtle()
toy4_button.hideturtle()
toy4_button.shape(Toy4btn)
toy4_button.shapesize(2, 3)
toy4_button.penup()
toy4_button.goto(-400, 25) 
toy4_button.hideturtle()



#2x happiness mulitplier in the shop
buy2xH_button= trtl.Turtle()
buy2xH_button.hideturtle()
buy2xH_button.shape(x2H_btn)
buy2xH_button.shapesize(2, 3)
buy2xH_button.penup()
buy2xH_button.goto(-200, -50) 
buy2xH_button.hideturtle()



#4x happiness mulitplier in the shop
buy4xH_button= trtl.Turtle()
buy4xH_button.hideturtle()
buy4xH_button.shape(x4H_btn)
buy4xH_button.shapesize(2, 3)
buy4xH_button.penup()
buy4xH_button.goto(-300, -50) 
buy4xH_button.hideturtle()

#10x happiness mulitplier in the shop
buy10xH_button= trtl.Turtle()
buy10xH_button.hideturtle()
buy10xH_button.shape(x10H_btn)
buy10xH_button.shapesize(2, 3)
buy10xH_button.penup()
buy10xH_button.goto(-400, -50) 
buy10xH_button.hideturtle()

#cowboyhat in the shop
hat_button = trtl.Turtle()
hat_button.hideturtle()
hat_button.shape(Hat1btn)
hat_button.shapesize(2, 3)
hat_button.penup()
hat_button.goto(-400, 100) 
hat_button.hideturtle()

#toy4 in the shop
toy1_button = trtl.Turtle()
toy1_button.hideturtle()
toy1_button.shape(BurgerBTN)
toy1_button.shapesize(2, 3)
toy1_button.penup()
toy1_button.goto(-300, 100) 
toy1_button.hideturtle()


# Money and Expense Displays
money_writer = trtl.Turtle()
money_writer.hideturtle()
money_writer.penup()
money_writer.goto(-300, -100)

total_expenses = 0
expense_writer = trtl.Turtle()
expense_writer.hideturtle()
expense_writer.penup()
expense_writer.goto(RIGHT_X, -70) 

# Mini-game Access Button
work_button = trtl.Turtle()
work_button.hideturtle()
work_button.shape(Workbtn) 
work_button.penup()
work_button.goto(-300, -200)

# The Mini-game Target (The Coin)
game_coin = trtl.Turtle()
game_coin.hideturtle()
game_coin.shape(FBLACOIN)
game_coin.penup()

# A back button to return to the pet
back_button = trtl.Turtle()
back_button.hideturtle()
back_button.shape(EXIT)
back_button.penup()
back_button.goto(-350, 0)

# Mini-game Arena Dimensions
ARENA_X_MIN, ARENA_X_MAX = -200, 200
ARENA_Y_MIN, ARENA_Y_MAX = -150, 150

# Create a dedicated turtle to draw the box
arena_drawer = trtl.Turtle()
arena_drawer.hideturtle()
arena_drawer.speed(0)

# NEW: Create a  turtle for shop text 
shop_writer = trtl.Turtle()
shop_writer.hideturtle()
shop_writer.penup()
shop_writer.speed(0)

#Pet Objects 
pet1 = trtl.Turtle()
OGDOG = "OGDog.gif"
wn.addshape(OGDOG)
pet1.hideturtle()
pet1.shape(OGDOG)


pet2 = trtl.Turtle()
OGCAT = "OGCAT.gif"
wn.addshape(OGCAT)
pet2.hideturtle()
pet2.shape(OGCAT)
pet2.goto(0,-20)


# ==================================================
# GLOBAL GAME STATE VARIABLES
# ==================================================

happy = 100
hunger = 100
energy = 100
hygiene = 100
font_setup = ("Arial", 20, "bold")
bandana_given = False
multiplier = 1
list_of_items = []
money = 0
current_pet1_shape = OGDOG
current_pet2_shape = OGCAT
list_of_items = []
placed_items = [] 
chosen_pet = None
in_minigame = False

purchased_status = {
    "hat": False,
    "toy": False,
    "toy1": False,
    "toy2": False,
    "toy3": False,
    "toy4": False,
    "2xH": False,
    "4xH": False,
    "10xH": False
}

#functions for simulator

def show_title():
    """Displays the main title screen and starting instructions."""
    wn.bgcolor("pink")
    title_writer.goto(0, 50)
    title_writer.write("PET SIMULATOR", align="center", font=("Arial", 30, "bold"))
    title_writer.goto(0, -50)
    title_writer.write("Press 'Space' to Begin", align="center", font=("Arial", 15, "normal"))

def start_game():
    """Moves from title screen to instructions screen."""
    title_writer.clear()
    button_turtle1.hideturtle()
    button_turtle2.hideturtle()
    show_instructions()
    wn.onkeypress(start_pet_selection, "x")

def show_instructions():
    """Displays the instructions screen before pet selection."""
    wn.bgcolor("lightblue")
    title_writer.clear()
    # Title
    title_writer.goto(0, 220)
    title_writer.write(
        "HOW TO PLAY",
        align="center",
        font=("Arial", 32, "bold"))
    
    # Instructions block
    title_writer.goto(0, -130)
    title_writer.write(
        "🐶 Choose a pet (Dog or Cat)\n\n"
        "🍖 Keep Hunger above 0\n"
        "⚡ Keep Energy above 0\n"
        "🧼 Keep Hygiene above 0\n"
        "😊 Keep Happiness above 0\n\n"
        "🕹 Use buttons to feed, play, clean, and rest\n"
        "💼 Work to earn coins\n"
        "🛒 Buy all shop items to WIN\n\n"
        "❌ Let ANY stat reach 0 and you LOSE",
        align="center",
        font=("Arial", 16, "normal"))

    title_writer.goto(0, -200)
    title_writer.write(
        "Press X to Continue",
        align="center",
        font=("Arial", 18, "bold"))
    
def start_pet_selection():
    """Shows the pet selection screen."""
    title_writer.clear()
    wn.bgcolor("pink")
    button_turtle1.showturtle()
    button_turtle2.showturtle()
    title_writer.goto(0, -200)
    title_writer.write(
        "Choose a Pet!",
        align="center",
        font=("Arial", 40, "normal"))
    wn.onkeypress(None, "X")   
    
    
def ask_pet_name():
    """Opens a text input box to name the pet and displays it on screen."""
    name = wn.textinput("Pet Name", "Enter your pet's name:")
    name_writer = trtl.Turtle()
    name_writer.hideturtle()
    name_writer.penup()
    name_writer.goto(0, 150)
    name_writer.write(name,align="center",font=font_setup)

def start_pet1(x, y):
    """Sets up the game specifically for Pet 1 (the Dog)."""
    global chosen_pet
    chosen_pet = pet1
    title_writer.clear()       # clear title text
    button_turtle1.hideturtle()
    button_turtle2.hideturtle()
    pet1.showturtle()
    food_button.shape(food_button_img1)
    play_button.shape(playbutton1)
    ask_pet_name()
    feed_pet(x,y)
    play_pet(x,y)
    open_shop1()
    reward_10_money()
    update_displays()
    
    rest_button.showturtle()
    rest_button.onclick(rest_bar)
    clean_button.showturtle()
    clean_button.onclick(clean_bar)
    
    decrease_hunger()
    decrease_energy()
    decrease_hygiene()
    decrease_happiness()
    work_button.showturtle()
    work_button.onclick(start_minigame)
    setup_pet_room()
    
    
def start_pet2(x, y):
    """Sets up the game specifically for Pet 2 (the Cat)."""
    global chosen_pet
    chosen_pet = pet2
    title_writer.clear()
    button_turtle1.hideturtle()
    button_turtle2.hideturtle()
    pet2.showturtle()
    food_button.shape(food_button_img2)
    play_button.shape(playbutton2)
    ask_pet_name()
    feed_pet(x,y)
    play_pet(x,y)
    open_shop1()
    reward_10_money()
    update_displays()
    rest_button.showturtle()
    rest_button.onclick(rest_bar)
    clean_button.showturtle()
    clean_button.onclick(clean_bar)
    decrease_hunger()
    decrease_energy()
    decrease_hygiene()
    decrease_happiness()
    work_button.showturtle()
    work_button.onclick(start_minigame)
    setup_pet_room()
    
def update_displays():
    """updates all of the displays at once."""
    update_happiness_display()
    update_hunger_display()
    update_energy_display()
    update_hygiene_display()
    update_money_display()
    update_expense_display()  
    
def update_happiness_display():
    """Clears and redraws the current Happiness level."""
    happy_bar_drawer.clear()
    happy_bar_drawer.write(f" Happiness: {happy} ", align="center", font=font_setup)

def update_hunger_display():
    """Clears and redraws the current Hunger level."""
    hunger_bar_drawer.clear()
    hunger_bar_drawer.write(f" Hunger: {hunger} ", align="center", font=font_setup)

def update_money_display():
    """Clears and redraws the current total Money."""
    money_writer.clear()
    money_writer.write(f" Money: ${money} ", align="center", font=font_setup)

def update_hygiene_display():
    """Clears and redraws the current Hygiene level."""
    hygiene_bar_drawer.clear()
    hygiene_bar_drawer.write(f" Hygiene: {hygiene} ", align="center", font=font_setup)

def update_energy_display():
    """Clears and redraws the current Energy level."""
    energy_bar_drawer.clear()
    energy_bar_drawer.write(f" Energy: {energy} ", align="center", font=font_setup)

def update_expense_display():
    """Clears and redraws the total money spent in the shop."""
    expense_writer.clear()
    expense_writer.write(f"Total Spent: ${total_expenses}", align="center", font=font_setup)
    
def draw_arena():
    """Draws a boundary box with a 'screen' fill for visual appeal."""
    arena_drawer.clear()
    arena_drawer.penup()
    arena_drawer.goto(ARENA_X_MIN - 10, ARENA_Y_MAX + 10)
    arena_drawer.color("white") 
    arena_drawer.pensize(3)
    arena_drawer.pendown()
    for x in range(2):
        arena_drawer.forward((ARENA_X_MAX - ARENA_X_MIN) + 20)
        arena_drawer.right(90)
        arena_drawer.forward((ARENA_Y_MAX - ARENA_Y_MIN) + 20)
        arena_drawer.right(90)
    arena_drawer.penup()

def start_minigame(x, y):
    """Handles transition and draws the arena box."""
    global in_minigame
    in_minigame = True 
    for t in trtl.turtles():
        t.hideturtle()
    shop_writer.clear() 
    wn.bgcolor("darkblue")
    draw_arena() 
    message_trtl.clear()
    message_trtl.goto(0, 200) 
    message_trtl.write("CATCH THE COIN!", align="center", font=font_setup)
    game_coin.shape(FBLACOIN) 
    game_coin.showturtle()
    back_button.showturtle()
    move_coin()
    game_coin.onclick(earn_money_task)
    back_button.onclick(exit_minigame)
    
def exit_minigame(x, y):
    """Returns to the pet room after the mini-game."""
    global in_minigame
    in_minigame = False 
    
    arena_drawer.clear() 
    for t in trtl.turtles():
        t.hideturtle()
    
    wn.bgcolor("pink")
    

    setup_pet_room()

def move_coin():
    """Moves the coin ONLY within the arena boundaries."""
    if game_coin.isvisible():
        # Use our new constants instead of random numbers
        rand_x = random.randint(ARENA_X_MIN + 20, ARENA_X_MAX - 20)
        rand_y = random.randint(ARENA_Y_MIN + 20, ARENA_Y_MAX - 20)
        game_coin.goto(rand_x, rand_y)
        wn.ontimer(move_coin, 1000)

def earn_money_task(x, y):
    """Adds money and jumps to a new spot inside the box."""
    global money, multiplier
    money += (1* multiplier)
    update_displays()
    reward_10_money()
    rand_x = random.randint(ARENA_X_MIN + 20, ARENA_X_MAX - 20)
    rand_y = random.randint(ARENA_Y_MIN + 20, ARENA_Y_MAX - 20)
    game_coin.goto(rand_x, rand_y)
    
def setup_pet_room():
    """Shows all the standard UI elements for the pet's room."""
    # show the pet that was chosen
    if chosen_pet:
        chosen_pet.showturtle()
    food_button.showturtle()
    play_button.showturtle()
    work_button.showturtle()
    rest_button.showturtle()
    clean_button.showturtle()
    
    for item in placed_items:
        item.showturtle()
    # redraw all the shop buttons
    open_shop1() 
    
    # refresh the bars and text
    update_displays()
    check_pet_state()
    
def decrease_energy():
    """Reduces pet energy every 2 seconds and checks for exhaustion."""
    global energy
    if len(list_of_items) >= 6: return # Stop if game is won
    if energy > 0:
        energy -= 1 # decreases energy by 1
        update_energy_display()
        check_pet_state()
        lose_simulator()
        wn.ontimer(decrease_energy, 4000) # Decreases every 4 seconds
    else:
        energy_bar_drawer.clear()
        energy_bar_drawer.write("Your pet is exhausted!", align="center", font=font_setup)

def decrease_hygiene():
    """Reduces pet hygiene every 3 seconds."""
    global hygiene
    if len(list_of_items) >= 6: return
    if hygiene > 0:
        hygiene -= 1# decreases hygiene by 10
        update_hygiene_display()
        check_pet_state()
        lose_simulator()
        wn.ontimer(decrease_hygiene, 3000) # Decreases every 3 seconds
    else:
        hygiene_bar_drawer.clear()
        hygiene_bar_drawer.write("Your pet is dirty!", align="center", font=font_setup)
        
def rest_bar(x, y):
    """Refills energy when the rest button is clicked (capped at 100)."""
    global energy
    if energy < 100:
        energy += 10 # Increases energy by 10
        if energy > 100: 
            energy = 100 # Caps it at 100 max
    update_energy_display()

def clean_bar(x, y):
    """Refills hygiene when the clean button is clicked (capped at 100)."""
    global hygiene
    if hygiene < 100:
        hygiene += 10 # Increases hygiene by 10
        if hygiene > 100: 
            hygiene = 100 # Caps it at 100 max
    update_hygiene_display()    
    
def decrease_hunger():
    """Refills hunger when the food button is clicked (capped at 100)."""
    global hunger  
    # If they have 3 or more items, stop the timer 
    if len(list_of_items) >= 6:
        return 
    if hunger > 0:
        hunger -= 1  #decreases hunger by 1
        update_hunger_display()
        lose_simulator()
        wn.ontimer(decrease_hunger, 3000) # Decreases every 3 seconds
    else:
        hunger_bar_drawer.clear()
        hunger_bar_drawer.write("Your pet is starving!", align="center", font=font_setup)
        wn.ontimer(decrease_hunger, 3000)

def decrease_happiness():
    """Lowers and decreases happiness every 5 seconds """
    global happy
    
    if len(list_of_items) >= 6:
        return 

    if happy > 0:
        happy -= 1
        update_happiness_display()  
        check_pet_state()         # Check if the pet should turn 'Sad' or 'Unhappy'
        # Function runs every 5 seconds
        lose_simulator()
        wn.ontimer(decrease_happiness, 5000) 
    else:
        # If happy is already 0, keep checking every 5 seconds in case the user plays again
        wn.ontimer(decrease_happiness, 5000)
        
def happy_bar(x, y):
    """Increases happiness when play button is clicked (capped at 100)"""
    global happy
    if happy < 100:
        happy += 1 # Increase hunger (filling the stomach) when fed
        if happy > 100: happy = 10 
    update_happiness_display()
    reward_10_money()

def hunger_bar(x, y):
    """Refills hunger when the food button is clicked (capped at 100)."""
    global hunger
    if hunger < 100:
        hunger += 5 
        if hunger > 100: hunger = 100 
    update_hunger_display()
    
def check_pet_state():
    """Changes the background and pet image based on current stat levels."""
    global in_minigame
    if in_minigame:
        return 
        
    message_trtl.clear()   
    if hygiene < 50 or hunger < 50 or energy < 50:
        message_trtl.write("Status: Unhappy 🤒", align="center", font=font_setup)
        wn.bgcolor("olive")
        pet1.shape(OGSADDOG)
        pet2.shape(OGSADCAT)
    elif happy < 50:
        message_trtl.write("Status: Sad 😢", align="center", font=font_setup)
        wn.bgcolor("lightgray")
        pet1.shape(OGSADDOG)
        pet2.shape(OGSADCAT)   
    elif energy > 80:
        message_trtl.write("Status: Energetic! ⚡", align="center", font=font_setup)
        wn.bgcolor("orange")
        pet1.shape(current_pet1_shape) 
        pet2.shape(current_pet2_shape)
    else:
        message_trtl.write("Status: Happy 😊", align="center", font=font_setup)
        wn.bgcolor("pink")
        pet1.shape(current_pet1_shape)
        pet2.shape(current_pet2_shape)
    
def open_shop1():
    """Draws shop labels and shows only items NOT yet purchased."""
    shop_writer.clear() 
    shop_writer.goto(-300, 200)
    shop_writer.write("Shop", align="center", font=font_setup)
    # Prices
    shop_writer.goto(-200, 150)
    shop_writer.write("$50", align="center", font=font_setup)
    shop_writer.goto(-300, 150)
    shop_writer.write("$100", align="center", font=font_setup)
    shop_writer.goto(-400, 150)
    shop_writer.write("$250", align="center", font=font_setup)

    if not purchased_status["hat"]:
        hat_button.showturtle()
        hat_button.onclick(buy_hat)

    if not purchased_status["toy"]:
        toy_button.showturtle()
        toy_button.onclick(buy_toy)

    if not purchased_status["toy1"]:
        toy1_button.showturtle()
        toy1_button.onclick(buy_toy1)

    if not purchased_status["toy2"]:
        toy2_button.showturtle()
        toy2_button.onclick(buy_toy2)

    if not purchased_status["toy3"]:
        toy3_button.showturtle()
        toy3_button.onclick(buy_toy3)

    if not purchased_status["toy4"]:
        toy4_button.showturtle()
        toy4_button.onclick(buy_toy4)

    if not purchased_status["2xH"]:
        buy2xH_button.showturtle()
        buy2xH_button.onclick(buy2xH)

    if not purchased_status["4xH"]:
        buy4xH_button.showturtle()
        buy4xH_button.onclick(buy4xH)

    if not purchased_status["10xH"]:
        buy10xH_button.showturtle()
        buy10xH_button.onclick(buy10xH)

def buy_hat(x, y):
    """Purchases Cowboy Hat, updates pet appearance, and tracks item count."""
    global money, total_expenses, current_pet1_shape, current_pet2_shape
    cost = 250
    if money >= cost:
        purchased_status["hat"] = True 
        current_pet1_shape = HATDOG 
        current_pet2_shape = HATCAT
 
        
        pet1.shape(current_pet1_shape)
        pet2.shape(current_pet2_shape)
        
        money -= cost
        total_expenses += cost 
        update_money_display()
        update_expense_display()
        
        message_trtl.clear()
        message_trtl.write("Hat Purchased!", align="center", font=("Arial", 12, "normal"))  
        hat_button.onclick(None)
        list_of_items.append("cowboyHat")
        hat_button.hideturtle()
        win_simulator()
        
    else:
        message_trtl.clear()
        message_trtl.write(f"Need ${cost}!", align="center", font=("Arial", 12, "normal"))
        
def buy_toy1(x, y):
    """Purchases Burger, adds burger, and tracks item count."""
    global money, total_expenses 
    cost = 100
    if money >= cost:
        purchased_status["toy1"] = True
        money -= cost
        total_expenses += cost 
        update_money_display()
        update_expense_display()
        
        # Visual cue that it's bought
        message_trtl.clear()
        message_trtl.write("toy1 Purchased!", align="center", font=("Arial", 12, "normal"))
        bought_toy1 = True
    else:
        message_trtl.clear()
        message_trtl.write(f"Need ${cost}!", align="center", font=("Arial", 12, "normal"))
        bought_toy1 = False
    
    if bought_toy1 == True:
        toy1_trtl = trtl.Turtle()
        toy1_trtl.shape(Burger)
        toy1_trtl.penup()
        toy1_trtl.goto(40,-100) 
        list_of_items.append("burger")
        placed_items.append(toy1_trtl)
        toy1_button.hideturtle()
        
        win_simulator()
        
        
def buy_toy(x, y):
    """Purchases Tennis Ball, adds pet toy, and tracks item count."""
    global money, total_expenses 
    cost = 50
    if money >= cost:
        purchased_status["toy"] = True
        money -= cost
        total_expenses += cost 
        update_money_display()
        update_expense_display()
        message_trtl.clear()
        message_trtl.write("Toy Purchased!", align="center", font=("Arial", 12, "normal"))
        bought_toy = True
    else:
        message_trtl.clear()
        message_trtl.write(f"Need ${cost}!", align="center", font=("Arial", 12, "normal"))
        bought_toy = False
    
    if bought_toy == True:
        toy_trtl = trtl.Turtle()
        toy_trtl.shape(TennisBall)
        toy_trtl.penup()
        toy_trtl.goto(100,-100) #change*********
        list_of_items.append("TennisBall")
        placed_items.append(toy_trtl)
        toy_button.hideturtle()
        win_simulator()
    
def buy_toy2(x, y):
    """Purchases Rubber Duck, adds duck toy, and tracks item count."""
    global money, total_expenses
    cost = 100
    if money >= cost:
        purchased_status["toy2"] = True
        money -= cost
        total_expenses += cost
        # Create the duck toy
        toy2_trtl = trtl.Turtle()
        toy2_trtl.shape(RubberDuck)
        toy2_trtl.penup()
        toy2_trtl.goto(60, -100)
        placed_items.append(toy2_trtl)
        list_of_items.append("duck")
        toy2_button.hideturtle()
        update_money_display()
        update_expense_display()
        win_simulator()
        message_trtl.clear()
        message_trtl.write("Rubber Duck Purchased!", align="center",
                           font=("Arial", 12, "normal"))
    else:
        message_trtl.clear()
        message_trtl.write(f"Need ${cost}!", align="center",
                           font=("Arial", 12, "normal"))
        
        
def buy_toy3(x, y):
    """Purchases Donut, adds pet toy, and tracks item count."""
    global money, total_expenses
    cost = 50
    if money >= cost:
        purchased_status["toy3"] = True
        money -= cost
        total_expenses += cost
            
        toy3_trtl = trtl.Turtle()
        toy3_trtl.shape(Donut)
        toy3_trtl.penup()
        toy3_trtl.goto(140, -100)
        placed_items.append(toy3_trtl)
        toy3_button.hideturtle()
        list_of_items.append("Donut")
        update_displays()
        win_simulator()
        
def buy_toy4(x, y):
    """Purchases FBLA Coin, adds coin, and tracks item count."""
    global money, total_expenses
    cost = 250
    if money >= cost:
        purchased_status["toy4"] = True
        money -= cost
        total_expenses += cost 
        toy4_trtl = trtl.Turtle()
        toy4_trtl.shape(FBLACOIN)
        toy4_trtl.penup()
        toy4_trtl.goto(200, -100)
            
        toy4_button.hideturtle()
        list_of_items.append("FBLA Coin")
        placed_items.append(toy4_trtl)
        update_displays()
        win_simulator()
        
def buy2xH(x, y):
    """Purchases and activates the 2x Happiness multiplier."""
    global money, total_expenses, multiplier
    cost = 50
    if money >= cost:
        purchased_status["2xH"] = True
        money -= cost
        total_expenses += cost
        multiplier = 2 # Double earnings
        
        buy2xH_button.hideturtle()
        update_displays()
        message_trtl.clear()
        message_trtl.write("2x Earnings Active!", align="center", font=("Arial", 12, "normal"))
    else:
        message_trtl.clear()
        message_trtl.write(f"Need ${cost}!", align="center", font=("Arial", 12, "normal"))
        

def buy4xH(x, y):
    """Purchases and activates the 4x Happiness multiplier."""
    global money, total_expenses, multiplier
    cost = 100
    if money >= cost:
        purchased_status["4xH"] = True
        money -= cost
        total_expenses += cost
        multiplier = 4 # Quadruple earnings
        
        buy4xH_button.hideturtle()
        update_displays()
        message_trtl.clear()
        message_trtl.write("4x Earnings Active!", align="center", font=("Arial", 12, "normal"))

def buy10xH(x, y):
    """Purchases and activates the 10x Happiness multiplier."""
    global money, total_expenses, multiplier
    cost = 
    if money >= cost:
        purchased_status["10xH"] = True
        money -= cost
        total_expenses += cost
        multiplier = 10 # Massive earnings
        
        buy10xH_button.hideturtle()
        update_displays()
        message_trtl.clear()
        message_trtl.write("10x Earnings Active!", align="center", font=("Arial", 12, "normal"))
        
def reward_10_money():
    """Gives the pet a bandana reward automatically once happiness reaches 10."""
    global bandana_given, current_pet1_shape, current_pet2_shape 
    if money >= 10 and bandana_given == False:
        message_trtl.clear()
        message_trtl.write("You've earned $10. Here's a reward!")
        
        # Update the 'Memory' shapes
        current_pet1_shape = DogBandana 
        current_pet2_shape = CatCollar  
        
        pet1.shape(current_pet1_shape)
        pet2.shape(current_pet2_shape)
        bandana_given = True
        
def feed_pet(x,y):
    food_button.showturtle()
    food_button.onclick(hunger_bar)

def play_pet(x,y):
    play_button.showturtle()
    play_button.onclick(happy_bar)

def win_simulator():
    """Checks if 3 or more items have been bought. If so, clears screen and shows Win message. gives option to restart"""
    if len(list_of_items) >= 6:
        print("game won")

        # Hide and clear EVERY turtle
        for t in trtl.turtles():
            t.clear()
            t.hideturtle()
        wn.clearscreen()

        wn.bgcolor("pink")

        # Create win message
        winner = trtl.Turtle()
        winner.hideturtle()
        winner.penup()
        winner.goto(0, 0)
        winner.write("YOU WIN!", align="center",
                     font=("Arial", 50, "bold"))
        winner.goto(0, -150)
        winner.write("Press R to Restart",  align="center", font=("Arial", 18, "bold"))

    wn.onkeypress(restart_game, "r")
    wn.listen()
def lose_simulator():
    """Ends the game if any pet stat reaches 0. gives option to restart"""
    if in_minigame:
        return
    if happy <= 0 or hunger <= 0 or energy <= 0 or hygiene <= 0:
        print("game lost")
        # Stop timers by clearing screen
        for t in trtl.turtles():
            t.clear()
            t.hideturtle()

        wn.clearscreen()
        wn.bgcolor("black")

        # Create lose message
        loser = trtl.Turtle()
        loser.hideturtle()
        loser.penup()
        loser.goto(0, 0)
        loser.color("red")
        loser.write(
            "YOU LOST 💔\nYour pet was neglected!",align="center",font=("Arial", 40, "bold"))
        loser.goto(0, -150)
        loser.write("Press R to Restart", align="center", font=("Arial", 18, "bold"))

    wn.onkeypress(restart_game, "r")
    wn.listen()
def restart_game():
    """Safely restarts the entire program."""
    wn.bye()  # closes turtle window
    
# --- Program Execution Starts Here ---
def main():
    """Initializes the start screen and listens for the beginning of the game."""
    show_title() 
    wn.listen()
    wn.onkeypress(start_game, "space") # When space is pressed, run start_game
    button_turtle2.onclick(start_pet1)
    button_turtle1.onclick(start_pet2)
    
main()
wn.mainloop()