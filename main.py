from tkinter import *
import os.path
import pickle
root = Tk()
# Creating the screen Variable
screen = 1

# Set the Icon
icon = PhotoImage(file="images\icon.png")
root.iconphoto(FALSE, icon)

# Change the Background Colour
root.configure(bg="LIGHT GREY")

# Change the Title of the Window
root.title("Amazon Fresh")

# Set the Window Size
root.geometry("1366x768")

# Creating the font settings for the widgets
Title_font_settings = ("Bell MT", 32, "bold")
Interactive_font_settings = ("Amazon Ember", 16, "bold")
item_desc_font_settings = ("Amazon Ember", 32, "bold")

# Creating the item data variables
Onion = 50
Carrot = 50
Potato = 50
Radish = 50
Cabbage = 50
Tomato = 50

Eggplant = 70
Bitter_gourd = 90
Lady_fingers = 60
Bell_peppers = 70
Egg = 50
Bread = 35

Cauliflower = 40
Lettuce = 50
Broccoli = 100
Corn = 50
Milk = 66
Sugar = 50

Beetroot = 70
Cheese = 50
Butter = 40
Honey = 50
Pepper = 20
Coconutmilk = 50

Almonds = 60
Coconutoil = 30
Jaggery = 60
Coconutwater = 30
Cocoapowder = 50
Curd = 25

Greentea = 30
Jaggerypowder = 50
Salt = 10
Tarmarind = 80
Peanutbutter = 50
Ghee = 100

# List of all the items
items = ["onion", "carrot", "potato", "radish", "cabbage", "tomato", "eggplant", "bittergourd", "ladyfingers", "bellpeppers", "egg", "bread", 'cauliflower', 'lettuce', 'broccoli', 'corn', 'milk', 'sugar', 'beetroot', 'cheese', 'butter', 'honey', 'pepper', 'coconutmilk', 'almonds', 'coconutoil', 'jaggery', 'coconutwater', "cocoapowder", 'curd', 'greentea', 'jaggerypowder', 'salt', 'tamarind', "peanutbutter", 'ghee']

vegetable_genre = ["onion", "carrots", "potato", "radish", "cabbage", "tomato", "eggplant", "bitter gourd", "ladyfinger", "capsicum", "cauliflower", "lettuce", "broccoli", "corn", "beetroot"]
dairy_genre = ["milk", "cheese", "butter", "curd", "ghee"]
spices_genre = ["pepper", "salt", "tamarind"]
others_genre = ["egg", "bread", 'sugar', 'honey', 'coconutmilk', 'almonds', 'coconutoil', 'jaggery', 'coconut water', "cocoapowder", 'greentea', 'jaggerypowder', "peanutbutter"]

item = items
# User variable
Username = ""

# Defining the quantity variables
quantity = 1
amt = 1
multiplier = 1
quantity_type = "Kg"

# Defining new functions:

# Function for moving to the next screen


def screen_next():
    global screen
    if screen == 1:
        screen += 1
        previous_screen_button["state"] = "normal"

        onion_button.grid_remove()
        carrot_button.grid_remove()
        potato_button.grid_remove()
        radish_button.grid_remove()
        cabbage_button.grid_remove()
        tomato_button.grid_remove()

        eggplant_button.grid(row=1, column=0, padx=20, pady=15)
        bitter_gourd_button.grid(row=1, column=2, padx=20, pady=15)
        lady_fingers_button.grid(row=1, column=4, padx=20, pady=15)
        bell_peppers_button.grid(row=2, column=0, padx=20, pady=15)
        egg_button.grid(row=2, column=2, padx=20, pady=15)
        bread_button.grid(row=2, column=4, padx=20, pady=15)

    elif screen == 2:
        screen += 1

        eggplant_button.grid_remove()
        bitter_gourd_button.grid_remove()
        lady_fingers_button.grid_remove()
        bell_peppers_button.grid_remove()
        egg_button.grid_remove()
        bread_button.grid_remove()

        cauliflower_button.grid(row=1, column=0, padx=20, pady=15)
        lettuce_button.grid(row=1, column=2, padx=20, pady=15)
        broccoli_button.grid(row=1, column=4, padx=20, pady=15)
        corn_button.grid(row=2, column=0, padx=20, pady=15)
        milk_button.grid(row=2, column=2, padx=20, pady=15)
        sugar_button.grid(row=2, column=4, padx=20, pady=15)

    elif screen == 3:
        screen += 1

        cauliflower_button.grid_remove()
        lettuce_button.grid_remove()
        broccoli_button.grid_remove()
        corn_button.grid_remove()
        milk_button.grid_remove()
        sugar_button.grid_remove()

        beetroot_button.grid(row=1, column=0, padx=20, pady=15)
        cheese_button.grid(row=1, column=2, padx=20, pady=15)
        butter_button.grid(row=1, column=4, padx=20, pady=15)
        honey_button.grid(row=2, column=0, padx=20, pady=15)
        pepper_button.grid(row=2, column=2, padx=20, pady=15)
        coconutmilk_button.grid(row=2, column=4, padx=20, pady=15)

    elif screen == 4:
        screen += 1

        beetroot_button.grid_remove()
        cheese_button.grid_remove()
        butter_button.grid_remove()
        honey_button.grid_remove()
        pepper_button.grid_remove()
        coconutmilk_button.grid_remove()

        almonds_button.grid(row=1, column=0, padx=20, pady=15)
        coconutoil_button.grid(row=1, column=2, padx=20, pady=15)
        jaggery_button.grid(row=1, column=4, padx=20, pady=15)
        coconutwater_button.grid(row=2, column=0, padx=20, pady=15)
        cocoapowder_button.grid(row=2, column=2, padx=20, pady=15)
        curd_button.grid(row=2, column=4, padx=20, pady=15)

    elif screen == 5:
        screen += 1
        next_screen_button["state"] = "disabled"

        almonds_button.grid_remove()
        coconutoil_button.grid_remove()
        jaggery_button.grid_remove()
        coconutwater_button.grid_remove()
        cocoapowder_button.grid_remove()
        curd_button.grid_remove()

        greentea_button.grid(row=1, column=0, padx=20, pady=15)
        jaggerypowder_button.grid(row=1, column=2, padx=20, pady=15)
        salt_button.grid(row=1, column=4, padx=20, pady=15)
        tarmarind_button.grid(row=2, column=0, padx=20, pady=15)
        peanutbutter_button.grid(row=2, column=2, padx=20, pady=15)
        ghee_button.grid(row=2, column=4, padx=20, pady=15)

# Function for moving to the previous screen


def screen_prev():
    global screen
    if screen <= 1:
        screen = 1
        previous_screen_button["state"] = "disabled"
    elif screen == 2:
        screen -= 1
        previous_screen_button["state"] = "disabled"
        eggplant_button.grid_remove()
        bitter_gourd_button.grid_remove()
        lady_fingers_button.grid_remove()
        bell_peppers_button.grid_remove()
        egg_button.grid_remove()
        bread_button.grid_remove()

        onion_button.grid(row=1, column=0, padx=20, pady=15)
        carrot_button.grid(row=1, column=2, padx=20, pady=15)
        potato_button.grid(row=1, column=4, padx=20, pady=15)
        radish_button.grid(row=2, column=0, padx=20, pady=15)
        cabbage_button.grid(row=2, column=2, padx=20, pady=15)
        tomato_button.grid(row=2, column=4, padx=20, pady=15)

    elif screen == 3:
        screen -= 1
        cauliflower_button.grid_remove()
        lettuce_button.grid_remove()
        broccoli_button.grid_remove()
        corn_button.grid_remove()
        milk_button.grid_remove()
        sugar_button.grid_remove()

        eggplant_button.grid(row=1, column=0, padx=20, pady=15)
        bitter_gourd_button.grid(row=1, column=2, padx=20, pady=15)
        lady_fingers_button.grid(row=1, column=4, padx=20, pady=15)
        bell_peppers_button.grid(row=2, column=0, padx=20, pady=15)
        egg_button.grid(row=2, column=2, padx=20, pady=15)
        bread_button.grid(row=2, column=4, padx=20, pady=15)

    elif screen == 4:
        screen -= 1
        next_screen_button["state"] = "normal"
        beetroot_button.grid_remove()
        cheese_button.grid_remove()
        butter_button.grid_remove()
        honey_button.grid_remove()
        pepper_button.grid_remove()
        coconutmilk_button.grid_remove()

        cauliflower_button.grid(row=1, column=0, padx=20, pady=15)
        lettuce_button.grid(row=1, column=2, padx=20, pady=15)
        broccoli_button.grid(row=1, column=4, padx=20, pady=15)
        corn_button.grid(row=2, column=0, padx=20, pady=15)
        milk_button.grid(row=2, column=2, padx=20, pady=15)
        sugar_button.grid(row=2, column=4, padx=20, pady=15)

    elif screen == 5:
        screen -= 1
        next_screen_button["state"] = "normal"
        almonds_button.grid_remove()
        coconutoil_button.grid_remove()
        jaggery_button.grid_remove()
        coconutwater_button.grid_remove()
        cocoapowder_button.grid_remove()
        curd_button.grid_remove()

        beetroot_button.grid(row=1, column=0, padx=20, pady=15)
        cheese_button.grid(row=1, column=2, padx=20, pady=15)
        butter_button.grid(row=1, column=4, padx=20, pady=15)
        honey_button.grid(row=2, column=0, padx=20, pady=15)
        pepper_button.grid(row=2, column=2, padx=20, pady=15)
        coconutmilk_button.grid(row=2, column=4, padx=20, pady=15)

    elif screen == 6:
        screen -= 1
        next_screen_button["state"] = "normal"
        greentea_button.grid_remove()
        jaggerypowder_button.grid_remove()
        salt_button.grid_remove()
        tarmarind_button.grid_remove()
        peanutbutter_button.grid_remove()
        ghee_button.grid_remove()

        almonds_button.grid(row=1, column=0, padx=20, pady=15)
        coconutoil_button.grid(row=1, column=2, padx=20, pady=15)
        jaggery_button.grid(row=1, column=4, padx=20, pady=15)
        coconutwater_button.grid(row=2, column=0, padx=20, pady=15)
        cocoapowder_button.grid(row=2, column=2, padx=20, pady=15)
        curd_button.grid(row=2, column=4, padx=20, pady=15)


def list_screen():
    global screen
    global prev_screen
    global image_button
    global item_title

    if screen == 1:
        frame.grid_forget()
        back_button.grid_forget()
        image_button.grid_forget()
        item_title.grid_forget()
        add_button.grid_forget()
        item_quantity_value.grid_forget()
        subtract_button.grid_forget()
        buy_now_button.grid_forget()
        add_to_cart_button.grid_forget()
        if message_label.winfo_exists():
            message_label.grid_forget()

        Title_1.grid(row=0, column=0, columnspan=5, padx=150, pady=15)
        onion_button.grid(row=1, column=0, padx=20, pady=15)
        carrot_button.grid(row=1, column=2, padx=20, pady=15)
        potato_button.grid(row=1, column=4, padx=20, pady=15)
        radish_button.grid(row=2, column=0, padx=20, pady=15)
        your_orders_button.grid(row=4, column=2, padx=50)
        cabbage_button.grid(row=2, column=2, padx=20, pady=15)
        tomato_button.grid(row=2, column=4, padx=20, pady=15)
        next_screen_button.grid(row=4, column=3, pady=50)
        previous_screen_button.grid(row=4, column=1, pady=50)
        check_out_button.grid(row=4, column=4, rowspan=2)
        search_button.grid(row=4, column=0, pady=15)
        previous_screen_button["state"] = "disabled"
        next_screen_button["state"] = "normal"
    elif screen == 2:
        frame.grid_forget()
        back_button.grid_forget()
        image_button.grid_forget()
        item_title.grid_forget()
        add_button.grid_forget()
        item_quantity_value.grid_forget()
        subtract_button.grid_forget()
        buy_now_button.grid_forget()
        add_to_cart_button.grid_forget()
        if message_label.winfo_exists():
            message_label.grid_forget()

        Title_1.grid(row=0, column=0, columnspan=5, padx=150, pady=15)
        eggplant_button.grid(row=1, column=0, padx=20, pady=15)
        bitter_gourd_button.grid(row=1, column=2, padx=20, pady=15)
        lady_fingers_button.grid(row=1, column=4, padx=20, pady=15)
        bell_peppers_button.grid(row=2, column=0, padx=20, pady=15)
        egg_button.grid(row=2, column=2, padx=20, pady=15)
        bread_button.grid(row=2, column=4, padx=20, pady=15)
        next_screen_button.grid(row=4, column=3, pady=50)
        previous_screen_button.grid(row=4, column=1, pady=50)
        your_orders_button.grid(row=4, column=2, padx=50)
        search_button.grid(row=4, column=0, pady=15)
        check_out_button.grid(row=4, column=4, rowspan=2)
        previous_screen_button["state"] = "normal"
        next_screen_button["state"] = "normal"

    elif screen == 3:
        frame.grid_forget()
        back_button.grid_forget()
        image_button.grid_forget()
        item_title.grid_forget()
        add_button.grid_forget()
        item_quantity_value.grid_forget()
        subtract_button.grid_forget()
        buy_now_button.grid_forget()
        add_to_cart_button.grid_forget()
        if message_label.winfo_exists():
            message_label.grid_forget()
        Title_1.grid(row=0, column=0, columnspan=5, padx=150, pady=15)
        cauliflower_button.grid(row=1, column=0, padx=20, pady=15)
        lettuce_button.grid(row=1, column=2, padx=20, pady=15)
        broccoli_button.grid(row=1, column=4, padx=20, pady=15)
        corn_button.grid(row=2, column=0, padx=20, pady=15)
        your_orders_button.grid(row=4, column=2, padx=50)
        milk_button.grid(row=2, column=2, padx=20, pady=15)
        sugar_button.grid(row=2, column=4, padx=20, pady=15)
        next_screen_button.grid(row=4, column=3, pady=50)
        previous_screen_button.grid(row=4, column=1, pady=50)
        search_button.grid(row=4, column=0, pady=15)
        check_out_button.grid(row=4, column=4, rowspan=2)
        previous_screen_button["state"] = "normal"
        next_screen_button["state"] = "normal"

    elif screen == 4:
        frame.grid_forget()
        back_button.grid_forget()
        image_button.grid_forget()
        item_title.grid_forget()
        add_button.grid_forget()
        item_quantity_value.grid_forget()
        subtract_button.grid_forget()
        buy_now_button.grid_forget()
        add_to_cart_button.grid_forget()
        if message_label.winfo_exists():
            message_label.grid_forget()

        Title_1.grid(row=0, column=0, columnspan=5, padx=150, pady=15)
        beetroot_button.grid(row=1, column=0, padx=20, pady=15)
        cheese_button.grid(row=1, column=2, padx=20, pady=15)
        butter_button.grid(row=1, column=4, padx=20, pady=15)
        honey_button.grid(row=2, column=0, padx=20, pady=15)
        your_orders_button.grid(row=4, column=2, padx=50)
        pepper_button.grid(row=2, column=2, padx=20, pady=15)
        coconutmilk_button.grid(row=2, column=4, padx=20, pady=15)
        next_screen_button.grid(row=4, column=3, pady=50)
        previous_screen_button.grid(row=4, column=1, pady=50)
        your_orders_button.grid(row=4, column=2, padx=50)
        search_button.grid(row=4, column=0, pady=15)
        check_out_button.grid(row=4, column=4, rowspan=2)
        previous_screen_button["state"] = "normal"
        next_screen_button["state"] = "normal"

    elif screen == 5:
        frame.grid_forget()
        back_button.grid_forget()
        image_button.grid_forget()
        item_title.grid_forget()
        add_button.grid_forget()
        item_quantity_value.grid_forget()
        subtract_button.grid_forget()
        buy_now_button.grid_forget()
        add_to_cart_button.grid_forget()
        if message_label.winfo_exists():
            message_label.grid_forget()

        Title_1.grid(row=0, column=0, columnspan=5, padx=150, pady=15)
        almonds_button.grid(row=1, column=0, padx=20, pady=15)
        coconutoil_button.grid(row=1, column=2, padx=20, pady=15)
        jaggery_button.grid(row=1, column=4, padx=20, pady=15)
        coconutwater_button.grid(row=2, column=0, padx=20, pady=15)
        cocoapowder_button.grid(row=2, column=2, padx=20, pady=15)
        your_orders_button.grid(row=4, column=2, padx=50)
        curd_button.grid(row=2, column=4, padx=20, pady=15)
        next_screen_button.grid(row=4, column=3, pady=50)
        previous_screen_button.grid(row=4, column=1, pady=50)
        search_button.grid(row=4, column=0, pady=15)
        check_out_button.grid(row=4, column=4, rowspan=2)
        previous_screen_button["state"] = "normal"
        next_screen_button["state"] = "normal"

    elif screen == 6:
        frame.grid_forget()
        back_button.grid_forget()
        image_button.grid_forget()
        item_title.grid_forget()
        add_button.grid_forget()
        item_quantity_value.grid_forget()
        subtract_button.grid_forget()
        buy_now_button.grid_forget()
        add_to_cart_button.grid_forget()
        if message_label.winfo_exists():
            message_label.grid_forget()

        Title_1.grid(row=0, column=0, columnspan=5, padx=150, pady=15)
        greentea_button.grid(row=1, column=0, padx=20, pady=15)
        jaggerypowder_button.grid(row=1, column=2, padx=20, pady=15)
        salt_button.grid(row=1, column=4, padx=20, pady=15)
        tarmarind_button.grid(row=2, column=0, padx=20, pady=15)
        peanutbutter_button.grid(row=2, column=2, padx=20, pady=15)
        ghee_button.grid(row=2, column=4, padx=20, pady=15)
        next_screen_button.grid(row=4, column=3, pady=50)
        previous_screen_button.grid(row=4, column=1, pady=50)
        your_orders_button.grid(row=4, column=2, padx=50)
        search_button.grid(row=4, column=0, pady=15)
        check_out_button.grid(row=4, column=4, rowspan=2)
        previous_screen_button["state"] = "normal"
        next_screen_button["state"] = "disabled"

    elif screen == "search screen":
        search_button_2.grid_remove()
        list_box.grid_remove()
        search_entry.grid_remove()

        all_genre_button.grid_remove()
        vegetables_genre_button.grid_remove()
        dairy_genre_button.grid_remove()
        spices_genre_button.grid_remove()
        other_genre_button.grid_remove()

        if prev_screen == 1:
            screen = 1
            Title_1.grid(row=0, column=0, columnspan=5, padx=150, pady=15)
            onion_button.grid(row=1, column=0, padx=20, pady=15)
            your_orders_button.grid(row=4, column=2, padx=50)
            carrot_button.grid(row=1, column=2, padx=20, pady=15)
            potato_button.grid(row=1, column=4, padx=20, pady=15)
            radish_button.grid(row=2, column=0, padx=20, pady=15)
            cabbage_button.grid(row=2, column=2, padx=20, pady=15)
            tomato_button.grid(row=2, column=4, padx=20, pady=15)
            next_screen_button.grid(row=4, column=3, pady=50)
            previous_screen_button.grid(row=4, column=1, pady=50)
            check_out_button.grid(row=4, column=4, rowspan=2)
            search_button.grid(row=4, column=0, pady=15)
            previous_screen_button["state"] = "disabled"
        elif prev_screen == 2:
            screen = 2
            Title_1.grid(row=0, column=0, columnspan=5, padx=150, pady=15)
            eggplant_button.grid(row=1, column=0, padx=20, pady=15)
            bitter_gourd_button.grid(row=1, column=2, padx=20, pady=15)
            lady_fingers_button.grid(row=1, column=4, padx=20, pady=15)
            bell_peppers_button.grid(row=2, column=0, padx=20, pady=15)
            egg_button.grid(row=2, column=2, padx=20, pady=15)
            your_orders_button.grid(row=4, column=2, padx=50)
            bread_button.grid(row=2, column=4, padx=20, pady=15)
            next_screen_button.grid(row=4, column=3, pady=50)
            previous_screen_button.grid(row=4, column=1, pady=50)
            search_button.grid(row=4, column=0, pady=15)
            check_out_button.grid(row=4, column=4, rowspan=2)

        elif prev_screen == 3:
            screen = 3
            Title_1.grid(row=0, column=0, columnspan=5, padx=150, pady=15)
            cauliflower_button.grid(row=1, column=0, padx=20, pady=15)
            lettuce_button.grid(row=1, column=2, padx=20, pady=15)
            broccoli_button.grid(row=1, column=4, padx=20, pady=15)
            corn_button.grid(row=2, column=0, padx=20, pady=15)
            milk_button.grid(row=2, column=2, padx=20, pady=15)
            sugar_button.grid(row=2, column=4, padx=20, pady=15)
            your_orders_button.grid(row=4, column=2, padx=50)
            next_screen_button.grid(row=4, column=3, pady=50)
            previous_screen_button.grid(row=4, column=1, pady=50)
            search_button.grid(row=4, column=0, pady=15)
            check_out_button.grid(row=4, column=4, rowspan=2)

        elif prev_screen == 4:
            screen = 4
            Title_1.grid(row=0, column=0, columnspan=5, padx=150, pady=15)
            beetroot_button.grid(row=1, column=0, padx=20, pady=15)
            cheese_button.grid(row=1, column=2, padx=20, pady=15)
            butter_button.grid(row=1, column=4, padx=20, pady=15)
            honey_button.grid(row=2, column=0, padx=20, pady=15)
            pepper_button.grid(row=2, column=2, padx=20, pady=15)
            coconutmilk_button.grid(row=2, column=4, padx=20, pady=15)
            next_screen_button.grid(row=4, column=3, pady=50)
            previous_screen_button.grid(row=4, column=1, pady=50)
            search_button.grid(row=4, column=0, pady=15)
            your_orders_button.grid(row=4, column=2, padx=50)
            check_out_button.grid(row=4, column=4, rowspan=2)

        elif prev_screen == 5:
            screen = 5
            Title_1.grid(row=0, column=0, columnspan=5, padx=150, pady=15)
            almonds_button.grid(row=1, column=0, padx=20, pady=15)
            coconutoil_button.grid(row=1, column=2, padx=20, pady=15)
            jaggery_button.grid(row=1, column=4, padx=20, pady=15)
            coconutwater_button.grid(row=2, column=0, padx=20, pady=15)
            cocoapowder_button.grid(row=2, column=2, padx=20, pady=15)
            curd_button.grid(row=2, column=4, padx=20, pady=15)
            next_screen_button.grid(row=4, column=3, pady=50)
            previous_screen_button.grid(row=4, column=1, pady=50)
            search_button.grid(row=4, column=0, pady=15)
            check_out_button.grid(row=4, column=4, rowspan=2)
            your_orders_button.grid(row=4, column=2, padx=50)

        elif prev_screen == 6:
            screen = 6
            Title_1.grid(row=0, column=0, columnspan=5, padx=150, pady=15)
            greentea_button.grid(row=1, column=0, padx=20, pady=15)
            jaggerypowder_button.grid(row=1, column=2, padx=20, pady=15)
            salt_button.grid(row=1, column=4, padx=20, pady=15)
            tarmarind_button.grid(row=2, column=0, padx=20, pady=15)
            peanutbutter_button.grid(row=2, column=2, padx=20, pady=15)
            ghee_button.grid(row=2, column=4, padx=20, pady=15)
            next_screen_button.grid(row=4, column=3, pady=50)
            previous_screen_button.grid(row=4, column=1, pady=50)
            search_button.grid(row=4, column=0, pady=15)
            check_out_button.grid(row=4, column=4, rowspan=2)
            next_screen_button["state"] = "disabled"
            your_orders_button.grid(row=4, column=2, padx=50)

def item_screen(item):
    global screen
    global image_button
    global item_title
    global quantity
    global quantity_type
    global item_quantity_value
    global item_val
    global item_price
    global message_label
    global amt

    item_val = item
    item_val = str(item_val)
    text = ""
    if item == "onion":
        screen = 1
        item = onion_image
        item_price = Onion
        text = "Fresh Onions"
        quantity = 1
        quantity_type = "Kg"
        amt = 1
    elif item == "carrot":
        screen = 1
        item = carrot_image
        item_price = Carrot
        text = "Fresh Carrots"
        quantity = 1
        quantity_type = "Kg"
        amt = 1
    elif item == "potato":
        screen = 1
        item = potato_image
        item_price = Potato
        text = "Fresh Potatoes"
        quantity = 1
        quantity_type = "Kg"
        amt = 1
    elif item == "radish":
        screen = 1
        item = radish_image
        item_price = Radish
        text = "Fresh Radishes"
        quantity = 1
        quantity_type = "Kg"
        amt = 1
    elif item == "cabbage":
        screen = 1
        item = cabbage_image
        item_price = Cabbage
        text = "Fresh Cabbages"
        quantity = 1
        quantity_type = "Kg"
        amt = 1
    elif item == "tomato":
        screen = 1
        item = tomato_image
        item_price = Tomato
        text = "Fresh Tomatoes"
        quantity = 1
        quantity_type = "Kg"
        amt = 1
    elif item == "eggplant":
        screen = 2
        item = eggplant_image
        item_price = Eggplant
        text = "Fresh Aubergines"
        quantity = 1
        quantity_type = "Kg"
        amt = 1
    elif item == "bittergourd":
        screen = 2
        item = bitter_gourd_image
        item_price = Bitter_gourd
        text = "Fresh Bitter Gourds"
        quantity = 1
        quantity_type = "Kg"
        amt = 1
    elif item == "ladyfingers":
        screen = 2
        item = lady_fingers_image
        item_price = Lady_fingers
        text = "Fresh Lady fingers"
        quantity = 1
        quantity_type = "Kg"
        amt = 1
    elif item == "bellpeppers":
        screen = 2
        item = bell_peppers_image
        item_price = Bell_peppers
        text = "Fresh Bell peppers"
        quantity = 1
        quantity_type = "Kg"
        amt = 1
    elif item == "egg":
        screen = 2
        item = egg_image
        item_price = Egg
        text = "Fresh Eggs"
        quantity = 1
        quantity_type = "dzn"
        amt = 1
    elif item == "bread":
        screen = 2
        item = bread_image
        item_price = Bread
        text = "Brittania VitaRich Bread"
        quantity = 1
        quantity_type = "Pack"
        amt = 1
    elif item == "cauliflower":
        screen = 3
        item = cauliflower_image
        item_price = Cauliflower
        text = "Fresh Cauliflowers"
        quantity = 500
        quantity_type = "g"
        amt = 1
    elif item == "lettuce":
        screen = 3
        item = lettuce_image
        item_price = Lettuce
        text = "Fresh Lettuce"
        quantity = 500
        quantity_type = "g"
        amt = 1
    elif item == "broccoli":
        screen = 3
        item = broccoli_image
        item_price = Broccoli
        text = "Packaged Broccoli"
        quantity = 500
        quantity_type = "g"
        amt = 1
    elif item == "corn":
        screen = 3
        item = corn_image
        item_price = Corn
        text = "Fresh Corn Cobs"
        quantity = 500
        quantity_type = "g"
        amt = 1
    elif item == "milk":
        screen = 3
        item = milk_image
        item_price = Milk
        text = "Amul Taaza Toned Milk"
        quantity = 1
        quantity_type = "Pack"
        amt = 1
    elif item == "sugar":
        screen = 3
        item = sugar_image
        item_price = Sugar
        text = "Natural Sugar"
        quantity = 1
        quantity_type = "Pack"
        amt = 1
    elif item == "beetroot":
        screen = 4
        item = beetroot_image
        item_price = Beetroot
        text = "Fresh Beetroot"
        quantity = 1
        quantity_type = "Kg"
        amt = 1
    elif item == "cheese":
        screen = 4
        item = cheese_image
        item_price = Cheese
        text = "Amul Cheese"
        quantity = 1
        quantity_type = "Pack"
        amt = 1
    elif item == "butter":
        screen = 4
        item = butter_image
        item_price = Butter
        text = "Amul Butter"
        quantity = 1
        quantity_type = "Pack"
        amt = 1
    elif item == "honey":
        screen = 4
        item = honey_image
        item_price = Honey
        text = "Dabur Honey"
        quantity = 1
        quantity_type = "Pack"
        amt = 1
    elif item == "pepper":
        screen = 4
        item = pepper_image
        item_price = Pepper
        text = "Black Pepper"
        quantity = 1
        quantity_type = "Pack"
        amt = 1
    elif item == "coconutmilk":
        screen = 4
        item = coconutmilk_image
        item_price = Coconutmilk
        text = "KTC Coconut Milk"
        quantity = 1
        quantity_type = "Pack"
        amt = 1
    elif item == "almonds":
        screen = 5
        item = almonds_image
        item_price = Almonds
        text = "Vinit Almonds "
        quantity = 1
        quantity_type = "Pack"
        amt = 1
    elif item == "coconutoil":
        screen = 5
        item = coconutoil_image
        item_price = Coconutoil
        text = "Dabur Coconutoil"
        quantity = 1
        quantity_type = "Pack"
        amt = 1
    elif item == "jaggery":
        screen = 5
        item = jaggery_image
        item_price = Jaggery
        text = "UDUPI Jaggery Cubes"
        quantity = 1
        quantity_type = "Pack"
        amt = 1
    elif item == "coconutwater":
        screen = 5
        item = coconutwater_image
        item_price = Coconutwater
        text = "Natural Coconutwater"
        quantity = 1
        quantity_type = "Pack"
        amt = 1
    elif item == "cocoapowder":
        screen = 5
        item = cocoapowder_image
        item_price = Cocoapowder
        text = "Cocoa Powder"
        quantity = 1
        quantity_type = "Pack"
        amt = 1
    elif item == "curd":
        screen = 5
        item = curd_image
        item_price = Curd
        text = "Fresh Curd"
        quantity = 1
        quantity_type = "Pack"
        amt = 1
    elif item == "greentea":
        screen = 6
        item = greentea_image
        item_price = Greentea
        text = "Lipton Greentea"
        quantity = 1
        quantity_type = "Pack"
        amt = 1
    elif item == "jaggerypowder":
        screen = 6
        item = jaggerypowder_image
        item_price = Jaggerypowder
        text = "Jaggery Powder"
        quantity = 1
        quantity_type = "Pack"
        amt = 1
    elif item == "salt":
        screen = 6
        item = salt_image
        item_price = Salt
        text = "Tata Salt"
        quantity = 1
        quantity_type = "Pack"
        amt = 1
    elif item == "tamarind":
        screen = 6
        item = tamarind_image
        item_price = Tarmarind
        text = "KTC Pure Tamarind"
        quantity = 1
        quantity_type = "Pack"
        amt = 1
    elif item == "peanutbutter":
        screen = 6
        item = peanutbutter_image
        item_price = Peanutbutter
        text = "Bega Peanut Butter"
        quantity = 1
        quantity_type = "Pack"
        amt = 1
    elif item == "ghee":
        screen = 6
        item = ghee_image
        item_price = Ghee
        text = "Amul Cow Ghee"
        quantity = 1
        quantity_type = "Pack"
        amt = 1

    item_title = Label(root, text=text)
    item_quantity_value = Label(root, text=str(quantity) + " " + quantity_type)
    image_button = Button(frame, borderwidth=0, image=item)

    item_title.configure(font=item_desc_font_settings, bg="LIGHT GREY")
    item_quantity_value.configure(font=item_desc_font_settings, bg="LIGHT GREY")
    image_button.configure(bg="WHITE")

    if screen == 1:

        Title_1.grid_remove()
        onion_button.grid_remove()
        carrot_button.grid_remove()
        potato_button.grid_remove()
        radish_button.grid_remove()
        cabbage_button.grid_remove()
        tomato_button.grid_remove()
        next_screen_button.grid_remove()
        previous_screen_button.grid_remove()
        search_button.grid_remove()
        check_out_button.grid_remove()
        your_orders_button.grid_remove()
    elif screen == 2:

        Title_1.grid_remove()
        eggplant_button.grid_remove()
        bitter_gourd_button.grid_remove()
        lady_fingers_button.grid_remove()
        bell_peppers_button.grid_remove()
        egg_button.grid_remove()
        bread_button.grid_remove()
        next_screen_button.grid_remove()
        previous_screen_button.grid_remove()
        search_button.grid_remove()
        check_out_button.grid_remove()
        search_button.grid_remove()
        your_orders_button.grid_remove()
    elif screen == 3:

        Title_1.grid_remove()
        cauliflower_button.grid_remove()
        lettuce_button.grid_remove()
        broccoli_button.grid_remove()
        corn_button.grid_remove()
        milk_button.grid_remove()
        sugar_button.grid_remove()
        next_screen_button.grid_remove()
        previous_screen_button.grid_remove()
        search_button.grid_remove()
        check_out_button.grid_remove()
        search_button.grid_remove()
        your_orders_button.grid_remove()
    elif screen == 4:

        Title_1.grid_remove()
        beetroot_button.grid_remove()
        cheese_button.grid_remove()
        butter_button.grid_remove()
        honey_button.grid_remove()
        pepper_button.grid_remove()
        coconutmilk_button.grid_remove()
        next_screen_button.grid_remove()
        previous_screen_button.grid_remove()
        search_button.grid_remove()
        search_button.grid_remove()
        check_out_button.grid_remove()
        your_orders_button.grid_remove()
    elif screen == 5:

        Title_1.grid_remove()
        almonds_button.grid_remove()
        coconutoil_button.grid_remove()
        jaggery_button.grid_remove()
        coconutwater_button.grid_remove()
        cocoapowder_button.grid_remove()
        curd_button.grid_remove()
        next_screen_button.grid_remove()
        previous_screen_button.grid_remove()
        search_button.grid_remove()
        check_out_button.grid_remove()
        search_button.grid_remove()
        your_orders_button.grid_remove()
    elif screen == 6:

        Title_1.grid_remove()
        greentea_button.grid_remove()
        jaggerypowder_button.grid_remove()
        salt_button.grid_remove()
        tarmarind_button.grid_remove()
        peanutbutter_button.grid_remove()
        ghee_button.grid_remove()
        next_screen_button.grid_remove()
        previous_screen_button.grid_remove()
        search_button.grid_remove()
        check_out_button.grid_remove()
        search_button.grid_remove()
        your_orders_button.grid_remove()

    message_label = Label(root, text="")
    message_label.configure(font=Interactive_font_settings, bg="LIGHT GREY")

    frame.grid(row=0, column=0, rowspan=5)
    back_button.grid(row=0, column=0)
    image_button.grid(row=2, column=0, columnspan=100)
    item_title.grid(row=0, column=1, columnspan=10, padx=50)
    add_button.grid(row=1, column=3, padx=50)
    item_quantity_value.grid(row=1, column=2)
    subtract_button.grid(row=1, column=1, padx=50)
    buy_now_button.grid(row=2, column=1, columnspan=2, padx=50)
    add_to_cart_button.grid(row=2, column=2, columnspan=2, padx=160)
    message_label.grid(row=3, column=1, columnspan=3, padx=50)


def increase_item_quantity():
    global quantity
    global quantity_type
    global amt

    if quantity_type == "g":
        quantity += 500
        amt += 1
    elif quantity_type != "g":
        quantity += 1
        amt += 1
    if quantity >= 5 and quantity_type != "g":
        quantity = 5
    elif quantity >= 2000 and quantity_type == "g":
        quantity = 2000
    if amt >= 5 and quantity_type != "g":
        amt = 5
    elif amt >=4 and quantity_type == "g":
        amt = 4
    item_quantity_value["text"] = str(quantity) + " " + quantity_type


def decrease_item_quantity():
    global quantity
    global item_val
    global quantity_type
    global amt

    if quantity_type == "g":
        quantity -= 500
        amt -= 1
    elif quantity_type != "g":
        quantity -= 1
        amt -= 1
    if quantity <= 1 and quantity_type != "g":
        quantity = 1
    elif quantity <= 500 and quantity_type == "g":
        quantity = 500
    if amt <= 1:
        amt = 1
    item_quantity_value["text"] = str(quantity) + " " + quantity_type


def buy_now_page():
    global Thank_you_label
    global back_to_main_menu_button
    global quit_button
    global item_val
    global quantity
    global quantity_type
    global amt
    global item_text
    global qnt
    global cost
    global total
    global total_cost

    frame.grid_forget()
    back_button.grid_forget()
    image_button.grid_forget()
    item_title.grid_forget()
    add_button.grid_forget()
    item_quantity_value.grid_forget()
    subtract_button.grid_forget()
    buy_now_button.grid_forget()
    add_to_cart_button.grid_forget()
    if message_label.winfo_exists():
        message_label.grid_forget()

    if item_val == "onion":
        price = Onion
        text = "Onion"
    elif item_val == "carrot":
        price = Carrot
        text = "Carrot"
    elif item_val == "potato":
        price = Potato
        text = "Potato"
    elif item_val == "radish":
        price = Radish
        text = "Radish"
    elif item_val == "cabbage":
        price = Cabbage
        text = "Cabbage"
    elif item_val == "tomato":
        price = Tomato
        text = "Tomato"
    elif item_val == "eggplant":
        price = Eggplant
        text = "Eggplant"
    elif item_val == "bittergourd":
        price = Bitter_gourd
        text = "Bitter gourd"
    elif item_val == "ladyfingers":
        price = Lady_fingers
        text = "Lady fingers"
    elif item_val == "bellpeppers":
        price = Bell_peppers
        text = "Bell peppers"
    elif item_val == "egg":
        price = Egg
        text = "Egg"
    elif item_val == "bread":
        price = Bread
        text = "Bread"
    elif item_val == "cauliflower":
        price = Cauliflower
        text = "Cauliflower"
    elif item_val == "lettuce":
        price = Lettuce
        text = "Lettuce"
    elif item_val == "broccoli":
        price = Broccoli
        text = "Broccoli"
    elif item_val == "corn":
        price = Corn
        text = "Corn"
    elif item_val == "milk":
        price = Milk
        text = "Milk"
    elif item_val == "sugar":
        price = Sugar
        text = "Sugar"
    elif item_val == "beetroot":
        price = Beetroot
        text = "Beetroot"
    elif item_val == "cheese":
        price = Cheese
        text = "Cheese"
    elif item_val == "butter":
        price = Butter
        text = "Butter"
    elif item_val == "honey":
        price = Honey
        text = "Honey"
    elif item_val == "pepper":
        price = Pepper
        text = "Pepper"
    elif item_val == "coconutmilk":
        price = Coconutmilk
        text = "Coconut milk"
    elif item_val == "almonds":
        price = Almonds
        text = "Almonds"
    elif item_val == "coconutoil":
        price = Coconutoil
        text = "Coconut oil"
    elif item_val == "jaggery":
        price = Jaggery
        text = "Jaggery"
    elif item_val == "coconutwater":
        price = Coconutwater
        text = "Coconut water"
    elif item_val == "cocoapowder":
        price = Cocoapowder
        text = "Cocoa powder"
    elif item_val == "curd":
        price = Curd
        text = "Curd"
    elif item_val == "greentea":
        price = Greentea
        text = "Green tea"
    elif item_val == "jaggerypowder":
        price = Jaggerypowder
        text = "Jaggery powder"
    elif item_val == "salt":
        price = Salt
        text = "Salt"
    elif item_val == "tarmarind":
        price = Tarmarind
        text = "Tarmarind"
    elif item_val == "peanutbutter":
        price = Peanutbutter
        text = "Peanut butter"
    elif item_val == "ghee":
        price = Ghee
        text = "Ghee"

    item_text = Label(root, text=text, padx=200, pady=130)
    qnt = Label(root, text=str(quantity)+quantity_type)
    cost = Label(root, text=price*amt)
    total = Label(root, text="Total Amount to be paid", padx=250)
    total_cost = Label(root, text=price*amt)

    item_text.configure(font=item_desc_font_settings, bg="LIGHT GREY")
    qnt.configure(font=item_desc_font_settings, bg="LIGHT GREY")
    cost.configure(font=item_desc_font_settings, bg="LIGHT GREY")
    total.configure(font=item_desc_font_settings, bg="LIGHT GREY")
    total_cost.configure(font=item_desc_font_settings, bg="LIGHT GREY")

    item_text.grid(row=0, column=0)
    qnt.grid(row=0, column=1)
    cost.grid(row=0, column=3)
    total.grid(row=1, column=0, columnspan=3)
    total_cost.grid(row=1, column=3)
    purchase_button.grid(row=2, column=3)
    back_to_main_menu_button.grid(row=2, column=0)


def add_to_cart():
    global Title_1
    global message_label
    global filename
    global item_val
    global item_price
    global no_of_items

    fh = open(filename, "r+")
    data = fh.read()
    items = data.split()
    if item_val not in items and len(items)//4 < 5:
        fh.write(item_val + " " + str(quantity) + quantity_type + " " + str(item_price) + " " + str(amt) + " ")
        message_label["text"] = "Item Has been Added to the Cart"
    elif item_val not in items and len(items)//4 == 5:
        message_label["text"] = "Maximum limit of cart reached"
    elif item_val in items:
        message_label["text"] = "Item is already in the cart"
    fh.close()

    fh = open(filename, "r+")
    data = fh.read()
    items = data.split()
    no_of_items = len(items)//4
    Title_1["text"] = f"User: {user}                                        No. of items in cart: {no_of_items}"

    fh.close()


def main_menu():
    global Thank_you_label
    global back_to_main_menu_button
    global quit_button
    global Title_1
    global onion_button
    global carrot_button
    global potato_button
    global radish_button
    global cabbage_button
    global tomato_button
    global next_screen_button
    global previous_screen_button
    global screen
    global item_text
    global cost
    global qnt
    global total
    global total_cost
    global no_of_items
    global filename

    Thank_you_label.grid_forget()
    back_to_main_menu_button.grid_forget()
    quit_button.grid_forget()

    try:
        item_text.grid_forget()
        qnt.grid_forget()
        cost.grid_forget()
        total.grid_forget()
        total_cost.grid_forget()
        purchase_button.grid_forget()
        back_to_main_menu_button.grid_forget()
    except NameError:
        if no_of_items > 0:
            fh = open(filename, "w")
            fh.close()
            no_of_items = 0
            Title_1["text"] = f"User: {user}                                        No. of items in cart: {no_of_items}"
    screen = 1
    Title_1.grid(row=0, column=0, columnspan=5, padx=150, pady=15)
    onion_button.grid(row=1, column=0, padx=20, pady=15)
    carrot_button.grid(row=1, column=2, padx=20, pady=15)
    potato_button.grid(row=1, column=4, padx=20, pady=15)
    radish_button.grid(row=2, column=0, padx=20, pady=15)
    cabbage_button.grid(row=2, column=2, padx=20, pady=15)
    tomato_button.grid(row=2, column=4, padx=20, pady=15)
    next_screen_button.grid(row=4, column=3, pady=50)
    previous_screen_button.grid(row=4, column=1, pady=50)
    search_button.grid(row=4, column=0, pady=15)
    check_out_button.grid(row=4, column=4, rowspan=2)
    previous_screen_button["state"] = "disabled"
    next_screen_button["state"] = "normal"
    your_orders_button.grid(row=4, column=2, padx=50)


def purchase_screen():
    global filename
    global user
    global item_text
    global qnt
    global cost
    global total
    global total_cost
    global purchase_button
    global Thank_you_label
    global back_to_main_menu_button
    global quit_button
    global no_of_items
    global item_1_bill_text
    global item_2_bill_text
    global item_3_bill_text
    global item_4_bill_text
    global item_5_bill_text
    global item_1_quantity_text
    global item_2_quantity_text
    global item_3_quantity_text
    global item_4_quantity_text
    global item_5_quantity_text
    global item_1_cost_text
    global item_2_cost_text
    global item_3_cost_text
    global item_4_cost_text
    global item_5_cost_text
    global total_text
    global total_amount
    global orders_filename

    fh = open(filename, "r+")
    data = fh.read()
    fh.close()
    orders_filename = user + "_orders.txt"
    if os.path.isfile(orders_filename):
        fh = open(orders_filename, "r+")
        dat = fh.read().split("\n")
        for i in range(len(dat)):
            if dat[i] == "":
                dat.pop(i)
    else:
        fh = open(orders_filename, "w+")
        dat = fh.read().split("\n")
        for i in range(len(dat)):
            if dat[i] == "":
                dat.pop(i)

    print(dat)
    if len(dat) < 5:
        fh.write(data + "\n")
    fh.close()

    item_text.grid_forget()
    qnt.grid_forget()
    cost.grid_forget()
    total.grid_forget()
    total_cost.grid_forget()
    purchase_button.grid_forget()

    fh = open(filename, "w+")
    fh.close()
    no_of_items = 0
    Title_1["text"] = f"User: {user}                                        No. of items in cart: {no_of_items}"
    item_1_bill_text.grid_forget()
    item_1_quantity_text.grid_forget()
    item_1_cost_text.grid_forget()

    item_2_bill_text.grid_forget()
    item_2_quantity_text.grid_forget()
    item_2_cost_text.grid_forget()

    item_3_bill_text.grid_forget()
    item_3_quantity_text.grid_forget()
    item_3_cost_text.grid_forget()

    item_4_bill_text.grid_forget()
    item_4_quantity_text.grid_forget()
    item_4_cost_text.grid_forget()

    item_5_bill_text.grid_forget()
    item_5_quantity_text.grid_forget()
    item_5_cost_text.grid_forget()

    total_text.grid_forget()
    total_amount.grid_forget()

    purchase_button.grid_forget()
    back_out_of_check_out_button.grid_forget()

    Thank_you_label.grid(row=0, column=0, columnspan=2, padx=20, pady=100)
    back_to_main_menu_button.grid(row=1, column=0)
    quit_button.grid(row=1, column=1)


def character_limit(entry_text):
    if len(entry_text.get()) > 0:
        entry_text.set(entry_text.get()[:6])

def Sign_up(username, password):
    global no_of_items
    global user
    global Title_1
    global filename

    if os.path.isfile("users.bin") != True:
        fh = open("users.bin", "wb+")
        fh.close()
        
    user = username
    characters = []
    for i in user:
        characters.append(i)
    if len(characters) == 0:
        enter_user_message["text"] = "Please Enter a Username"
    elif len(characters) < 6:
        enter_user_message["text"] = "The Username should have 6 characters"
    elif len(characters) == 6:
        enter_user_message["text"] = " "

    if len(characters) == 6:
        filename = user + ".txt"
        fh = open("users.bin", "wb+")
        try:
            data = pickle.load(fh)
        except EOFError:
            data = {}
        fh.close()
        data[username] = password
        fh = open("users.bin", "wb+")
        pickle.dump(data, fh)
        print(data)
        fh.close()
        username_entry.delete(0, END)
        password_entry.delete(0, END)
        if not os.path.isfile(filename):
            fh = open(filename, "a+")
            data = fh.read()
            items = data.split()
            no_of_items = len(items)//4


def Log_in(username, password):
    global no_of_items
    global user
    global Title_1
    global filename

    if os.path.isfile("users.bin") != True:
        fh = open("users.bin", "wb+")
        fh.close()
    user = username
    characters = []
    for i in user:
        characters.append(i)
    if len(characters) == 0:
        enter_user_message["text"] = "Please Enter a Username"
    elif len(characters) < 6:
        enter_user_message["text"] = "The Username should have 6 characters"
    elif len(characters) == 6:
        enter_user_message["text"] = " "
    
    fh = open("users.bin", "rb+")
    try:
        data = pickle.load(fh)
    except EOFError:
        data = {}
    if username in data.keys():
        if data[username] == password:
            print("Ok")
            filename = user + ".txt"

            if os.path.isfile(filename):
                fh = open(filename, "r+")
                data = fh.read()
                items = data.split()
                no_of_items = len(items)//4

            frame2.place_forget()
            name_text.grid_forget()
            username_entry.grid_forget()
            sign_up_button.grid_forget()
            log_in_button.grid_forget()
            enter_user_message.grid_forget()

            # Creating the Title For Screen 1
            Title_1 = Label(root, text=f"User: {user}                                        No. of items in cart: {no_of_items}")
            Title_1.configure(font=Title_font_settings, bg="LIGHT GREY")

            Title_1.grid(row=0, column=0, columnspan=5, padx=150, pady=15)
            onion_button.grid(row=1, column=0, padx=20, pady=15)
            carrot_button.grid(row=1, column=2, padx=20, pady=15)
            potato_button.grid(row=1, column=4, padx=20, pady=15)
            radish_button.grid(row=2, column=0, padx=20, pady=15)
            cabbage_button.grid(row=2, column=2, padx=20, pady=15)
            tomato_button.grid(row=2, column=4, padx=20, pady=15)
            previous_screen_button.grid(row=4, column=1, pady=50)
            search_button.grid(row=4, column=0, pady=15)
            next_screen_button.grid(row=4, column=3, pady=50)
            check_out_button.grid(row=4, column=4, rowspan=2)
            your_orders_button.grid(row=4, column=2, padx=50)
        else:
            enter_user_message["text"] = "Incorrect Password"
    else:
        enter_user_message["text"] = "Incorrect Username"

def check_out():
    global filename
    global no_of_items
    global screen
    global item_1_bill_text
    global item_1_cost_text
    global item_1_quantity_text
    global item_2_bill_text
    global item_2_cost_text
    global item_2_quantity_text
    global item_3_bill_text
    global item_3_cost_text
    global item_3_quantity_text
    global item_4_bill_text
    global item_4_cost_text
    global item_4_quantity_text
    global item_5_bill_text
    global item_5_cost_text
    global item_5_quantity_text
    global total_text
    global total_amount
    fh = open(filename, "r+")
    items = fh.read().split()
    print(items)
    no_of_items = len(items) // 4

    if no_of_items != 0:
        if screen == 1:

            Title_1.grid_remove()
            onion_button.grid_remove()
            carrot_button.grid_remove()
            potato_button.grid_remove()
            radish_button.grid_remove()
            cabbage_button.grid_remove()
            tomato_button.grid_remove()
            next_screen_button.grid_remove()
            previous_screen_button.grid_remove()
            search_button.grid_remove()
            check_out_button.grid_remove()
            your_orders_button.grid_remove()
        elif screen == 2:

            Title_1.grid_remove()
            eggplant_button.grid_remove()
            bitter_gourd_button.grid_remove()
            lady_fingers_button.grid_remove()
            bell_peppers_button.grid_remove()
            egg_button.grid_remove()
            bread_button.grid_remove()
            next_screen_button.grid_remove()
            previous_screen_button.grid_remove()
            search_button.grid_remove()
            check_out_button.grid_remove()
            search_button.grid_remove()
            your_orders_button.grid_remove()
        elif screen == 3:

            Title_1.grid_remove()
            cauliflower_button.grid_remove()
            lettuce_button.grid_remove()
            broccoli_button.grid_remove()
            corn_button.grid_remove()
            milk_button.grid_remove()
            sugar_button.grid_remove()
            next_screen_button.grid_remove()
            previous_screen_button.grid_remove()
            search_button.grid_remove()
            check_out_button.grid_remove()
            search_button.grid_remove()
            your_orders_button.grid_remove()
        elif screen == 4:

            Title_1.grid_remove()
            beetroot_button.grid_remove()
            cheese_button.grid_remove()
            butter_button.grid_remove()
            honey_button.grid_remove()
            pepper_button.grid_remove()
            coconutmilk_button.grid_remove()
            next_screen_button.grid_remove()
            previous_screen_button.grid_remove()
            search_button.grid_remove()
            search_button.grid_remove()
            check_out_button.grid_remove()
            your_orders_button.grid_remove()
        elif screen == 5:

            Title_1.grid_remove()
            almonds_button.grid_remove()
            coconutoil_button.grid_remove()
            jaggery_button.grid_remove()
            coconutwater_button.grid_remove()
            cocoapowder_button.grid_remove()
            curd_button.grid_remove()
            next_screen_button.grid_remove()
            previous_screen_button.grid_remove()
            search_button.grid_remove()
            check_out_button.grid_remove()
            search_button.grid_remove()
            your_orders_button.grid_remove()
        elif screen == 6:

            Title_1.grid_remove()
            greentea_button.grid_remove()
            jaggerypowder_button.grid_remove()
            salt_button.grid_remove()
            tarmarind_button.grid_remove()
            peanutbutter_button.grid_remove()
            ghee_button.grid_remove()
            next_screen_button.grid_remove()
            previous_screen_button.grid_remove()
            search_button.grid_remove()
            check_out_button.grid_remove()
            search_button.grid_remove()
            your_orders_button.grid_remove()

        if no_of_items > 0:
            item_1_bill_text = Label(root, text=items[0].capitalize(), font=("Amazon Ember", 26, "bold"), bg="LIGHT GREY")
            item_1_quantity_text = Label(root, text=items[1], font=("Amazon Ember", 26, "bold"), bg="LIGHT GREY")
            item_1_cost_text = Label(root, text=int(items[2]) * int(items[3]), font=("Amazon Ember", 26, "bold"), bg="LIGHT GREY")
            total_cost = int(items[2]) * int(items[3])

            item_1_bill_text.grid(row=0, column=0, padx=350, pady=20)
            item_1_quantity_text.grid(row=0, column=1, padx=20)
            item_1_cost_text.grid(row=0, column=2)

            if no_of_items > 1:
                item_2_bill_text = Label(root, text=items[4].capitalize(), font=("Amazon Ember", 26, "bold"), bg="LIGHT GREY")
                item_2_quantity_text = Label(root, text=items[5], font=("Amazon Ember", 26, "bold"), bg="LIGHT GREY")
                item_2_cost_text = Label(root, text=int(items[6]) * int(items[7]), font=("Amazon Ember", 26, "bold"), bg="LIGHT GREY")
                total_cost = int(items[2]) * int(items[3]) + int(items[6]) * int(items[7])

                item_2_bill_text.grid(row=1, column=0, pady=20)
                item_2_quantity_text.grid(row=1, column=1)
                item_2_cost_text.grid(row=1, column=2)
                if no_of_items > 2:
                    item_3_bill_text = Label(root, text=items[8].capitalize(), font=("Amazon Ember", 26, "bold"), bg="LIGHT GREY")
                    item_3_quantity_text = Label(root, text=items[9], font=("Amazon Ember", 26, "bold"), bg="LIGHT GREY")
                    item_3_cost_text = Label(root, text=int(items[10]) * int(items[11]), font=("Amazon Ember", 26, "bold"), bg="LIGHT GREY")
                    total_cost = int(items[2]) * int(items[3]) + int(items[6]) * int(items[7]) + int(items[10]) * int(items[11])

                    item_3_bill_text.grid(row=2, column=0, padx=350, pady=20)
                    item_3_quantity_text.grid(row=2, column=1, padx=20)
                    item_3_cost_text.grid(row=2, column=2)
                    if no_of_items > 3:
                        item_4_bill_text = Label(root, text=items[12].capitalize(), font=("Amazon Ember", 26, "bold"), bg="LIGHT GREY")
                        item_4_quantity_text = Label(root, text=items[13], font=("Amazon Ember", 26, "bold"), bg="LIGHT GREY")
                        item_4_cost_text = Label(root, text=int(items[14]) * int(items[15]), font=("Amazon Ember", 26, "bold"), bg="LIGHT GREY")
                        total_cost = int(items[2]) * int(items[3]) + int(items[6]) * int(items[7]) + int(items[10]) * int(items[11]) + int(items[14]) * int(items[15])

                        item_4_bill_text.grid(row=3, column=0, padx=350, pady=20)
                        item_4_quantity_text.grid(row=3, column=1, padx=20)
                        item_4_cost_text.grid(row=3, column=2)
                        if no_of_items == 5:
                            item_5_bill_text = Label(root, text=items[16].capitalize(), font=("Amazon Ember", 26, "bold"), bg="LIGHT GREY")
                            item_5_quantity_text = Label(root, text=items[17], font=("Amazon Ember", 26, "bold"), bg="LIGHT GREY")
                            item_5_cost_text = Label(root, text=int(items[18]) * int(items[19]), font=("Amazon Ember", 26, "bold"), bg="LIGHT GREY")
                            total_cost = int(items[2]) * int(items[3]) + int(items[6]) * int(items[7]) + int(items[10]) * int(items[11]) + int(items[14]) * int(items[15]) + int(items[18]) * int(items[19])

                            item_5_bill_text.grid(row=4, column=0, padx=350, pady=20)
                            item_5_quantity_text.grid(row=4, column=1, padx=20)
                            item_5_cost_text.grid(row=4, column=2)

        total_text = Label(root, text="Total cost of all Items:", font=("Amazon Ember", 26, "bold"), bg="LIGHT GREY")
        total_amount = Label(root, text=total_cost, font=("Amazon Ember", 26, "bold"), bg="LIGHT GREY")

        total_text.grid(row=5, column=0, columnspan=2)
        total_amount.grid(row=5, column=2)
        back_out_of_check_out_button.grid(row=6, column=0)
        purchase_button.grid(row=6, column=2)


def back_to_the_main_screen_from_checkout():
    if no_of_items == 1:
        item_1_bill_text.grid_forget()
        item_1_quantity_text.grid_forget()
        item_1_cost_text.grid_forget()

        total_text.grid_forget()
        total_amount.grid_forget()

        purchase_button.grid_forget()
        back_out_of_check_out_button.grid_forget()

    elif no_of_items == 2:
        item_1_bill_text.grid_forget()
        item_1_quantity_text.grid_forget()
        item_1_cost_text.grid_forget()

        item_2_bill_text.grid_forget()
        item_2_quantity_text.grid_forget()
        item_2_cost_text.grid_forget()

        total_text.grid_forget()
        total_amount.grid_forget()

        purchase_button.grid_forget()
        back_out_of_check_out_button.grid_forget()

    elif no_of_items == 3:
        item_1_bill_text.grid_forget()
        item_1_quantity_text.grid_forget()
        item_1_cost_text.grid_forget()

        item_2_bill_text.grid_forget()
        item_2_quantity_text.grid_forget()
        item_2_cost_text.grid_forget()

        item_3_bill_text.grid_forget()
        item_3_quantity_text.grid_forget()
        item_3_cost_text.grid_forget()

        total_text.grid_forget()
        total_amount.grid_forget()

        purchase_button.grid_forget()
        back_out_of_check_out_button.grid_forget()

    elif no_of_items == 4:
        item_1_bill_text.grid_forget()
        item_1_quantity_text.grid_forget()
        item_1_cost_text.grid_forget()

        item_2_bill_text.grid_forget()
        item_2_quantity_text.grid_forget()
        item_2_cost_text.grid_forget()

        item_3_bill_text.grid_forget()
        item_3_quantity_text.grid_forget()
        item_3_cost_text.grid_forget()

        item_4_bill_text.grid_forget()
        item_4_quantity_text.grid_forget()
        item_4_cost_text.grid_forget()

        total_text.grid_forget()
        total_amount.grid_forget()

        purchase_button.grid_forget()
        back_out_of_check_out_button.grid_forget()

    elif no_of_items == 5:
        item_1_bill_text.grid_forget()
        item_1_quantity_text.grid_forget()
        item_1_cost_text.grid_forget()

        item_2_bill_text.grid_forget()
        item_2_quantity_text.grid_forget()
        item_2_cost_text.grid_forget()

        item_3_bill_text.grid_forget()
        item_3_quantity_text.grid_forget()
        item_3_cost_text.grid_forget()

        item_4_bill_text.grid_forget()
        item_4_quantity_text.grid_forget()
        item_4_cost_text.grid_forget()

        item_5_bill_text.grid_forget()
        item_5_quantity_text.grid_forget()
        item_5_cost_text.grid_forget()

        total_text.grid_forget()
        total_amount.grid_forget()

        purchase_button.grid_forget()
        back_out_of_check_out_button.grid_forget()

    if screen == 1:
        Title_1.grid(row=0, column=0, columnspan=5, padx=150, pady=15)
        onion_button.grid(row=1, column=0, padx=20, pady=15)
        carrot_button.grid(row=1, column=2, padx=20, pady=15)
        potato_button.grid(row=1, column=4, padx=20, pady=15)
        radish_button.grid(row=2, column=0, padx=20, pady=15)
        cabbage_button.grid(row=2, column=2, padx=20, pady=15)
        tomato_button.grid(row=2, column=4, padx=20, pady=15)
        search_button.grid(row=4, column=0, pady=15)
        next_screen_button.grid(row=4, column=3, pady=50)
        previous_screen_button.grid(row=4, column=1, pady=50)
        search_button.grid(row=4, column=0, pady=15)
        check_out_button.grid(row=4, column=4, rowspan=2)
        previous_screen_button["state"] = "disabled"
        your_orders_button.grid(row=4, column=2, padx=50)
    elif screen == 2:
        Title_1.grid(row=0, column=0, columnspan=5, padx=150, pady=15)
        eggplant_button.grid(row=1, column=0, padx=20, pady=15)
        bitter_gourd_button.grid(row=1, column=2, padx=20, pady=15)
        lady_fingers_button.grid(row=1, column=4, padx=20, pady=15)
        bell_peppers_button.grid(row=2, column=0, padx=20, pady=15)
        egg_button.grid(row=2, column=2, padx=20, pady=15)
        bread_button.grid(row=2, column=4, padx=20, pady=15)
        next_screen_button.grid(row=4, column=3, pady=50)
        previous_screen_button.grid(row=4, column=1, pady=50)
        check_out_button.grid(row=4, column=4, rowspan=2)
        search_button.grid(row=4, column=0, pady=15)
        your_orders_button.grid(row=4, column=2, padx=50)

    elif screen == 3:
        Title_1.grid(row=0, column=0, columnspan=5, padx=150, pady=15)
        cauliflower_button.grid(row=1, column=0, padx=20, pady=15)
        lettuce_button.grid(row=1, column=2, padx=20, pady=15)
        broccoli_button.grid(row=1, column=4, padx=20, pady=15)
        corn_button.grid(row=2, column=0, padx=20, pady=15)
        milk_button.grid(row=2, column=2, padx=20, pady=15)
        sugar_button.grid(row=2, column=4, padx=20, pady=15)
        next_screen_button.grid(row=4, column=3, pady=50)
        previous_screen_button.grid(row=4, column=1, pady=50)
        check_out_button.grid(row=4, column=4, rowspan=2)
        search_button.grid(row=4, column=0, pady=15)
        your_orders_button.grid(row=4, column=2, padx=50)

    elif screen == 4:
        Title_1.grid(row=0, column=0, columnspan=5, padx=150, pady=15)
        beetroot_button.grid(row=1, column=0, padx=20, pady=15)
        cheese_button.grid(row=1, column=2, padx=20, pady=15)
        butter_button.grid(row=1, column=4, padx=20, pady=15)
        honey_button.grid(row=2, column=0, padx=20, pady=15)
        pepper_button.grid(row=2, column=2, padx=20, pady=15)
        coconutmilk_button.grid(row=2, column=4, padx=20, pady=15)
        next_screen_button.grid(row=4, column=3, pady=50)
        previous_screen_button.grid(row=4, column=1, pady=50)
        check_out_button.grid(row=4, column=4, rowspan=2)
        search_button.grid(row=4, column=0, pady=15)
        your_orders_button.grid(row=4, column=2, padx=50)

    elif screen == 5:
        Title_1.grid(row=0, column=0, columnspan=5, padx=150, pady=15)
        almonds_button.grid(row=1, column=0, padx=20, pady=15)
        coconutoil_button.grid(row=1, column=2, padx=20, pady=15)
        jaggery_button.grid(row=1, column=4, padx=20, pady=15)
        coconutwater_button.grid(row=2, column=0, padx=20, pady=15)
        cocoapowder_button.grid(row=2, column=2, padx=20, pady=15)
        curd_button.grid(row=2, column=4, padx=20, pady=15)
        next_screen_button.grid(row=4, column=3, pady=50)
        previous_screen_button.grid(row=4, column=1, pady=50)
        check_out_button.grid(row=4, column=4, rowspan=2)
        search_button.grid(row=4, column=0, pady=15)
        your_orders_button.grid(row=4, column=2, padx=50)

    elif screen == 6:
        Title_1.grid(row=0, column=0, columnspan=5, padx=150, pady=15)
        greentea_button.grid(row=1, column=0, padx=20, pady=15)
        jaggerypowder_button.grid(row=1, column=2, padx=20, pady=15)
        salt_button.grid(row=1, column=4, padx=20, pady=15)
        tarmarind_button.grid(row=2, column=0, padx=20, pady=15)
        peanutbutter_button.grid(row=2, column=2, padx=20, pady=15)
        ghee_button.grid(row=2, column=4, padx=20, pady=15)
        next_screen_button.grid(row=4, column=3, pady=50)
        previous_screen_button.grid(row=4, column=1, pady=50)
        check_out_button.grid(row=4, column=4, rowspan=2)
        search_button.grid(row=4, column=0, pady=15)
        your_orders_button.grid(row=4, column=2, padx=50)
        next_screen_button["state"] = "disabled"

def Bring_up_search():
    global screen
    global prev_screen
    prev_screen = screen
    screen = "search screen"
    if prev_screen == 1:

        Title_1.grid_remove()
        onion_button.grid_remove()
        carrot_button.grid_remove()
        potato_button.grid_remove()
        radish_button.grid_remove()
        cabbage_button.grid_remove()
        tomato_button.grid_remove()
        next_screen_button.grid_remove()
        previous_screen_button.grid_remove()
        search_button.grid_remove()
        check_out_button.grid_remove()
        your_orders_button.grid_remove()
    elif prev_screen == 2:

        Title_1.grid_remove()
        eggplant_button.grid_remove()
        bitter_gourd_button.grid_remove()
        lady_fingers_button.grid_remove()
        bell_peppers_button.grid_remove()
        egg_button.grid_remove()
        bread_button.grid_remove()
        next_screen_button.grid_remove()
        previous_screen_button.grid_remove()
        search_button.grid_remove()
        check_out_button.grid_remove()
        your_orders_button.grid_remove()
    elif prev_screen == 3:

        Title_1.grid_remove()
        cauliflower_button.grid_remove()
        lettuce_button.grid_remove()
        broccoli_button.grid_remove()
        corn_button.grid_remove()
        milk_button.grid_remove()
        sugar_button.grid_remove()
        next_screen_button.grid_remove()
        previous_screen_button.grid_remove()
        search_button.grid_remove()
        check_out_button.grid_remove()
        your_orders_button.grid_remove()
    elif prev_screen == 4:

        Title_1.grid_remove()
        beetroot_button.grid_remove()
        cheese_button.grid_remove()
        butter_button.grid_remove()
        honey_button.grid_remove()
        pepper_button.grid_remove()
        coconutmilk_button.grid_remove()
        next_screen_button.grid_remove()
        previous_screen_button.grid_remove()
        search_button.grid_remove()
        check_out_button.grid_remove()
        your_orders_button.grid_remove()
    elif prev_screen == 5:

        Title_1.grid_remove()
        almonds_button.grid_remove()
        coconutoil_button.grid_remove()
        jaggery_button.grid_remove()
        coconutwater_button.grid_remove()
        cocoapowder_button.grid_remove()
        curd_button.grid_remove()
        next_screen_button.grid_remove()
        previous_screen_button.grid_remove()
        search_button.grid_remove()
        check_out_button.grid_remove()
        your_orders_button.grid_remove()
    elif prev_screen == 6:

        Title_1.grid_remove()
        greentea_button.grid_remove()
        jaggerypowder_button.grid_remove()
        salt_button.grid_remove()
        tarmarind_button.grid_remove()
        peanutbutter_button.grid_remove()
        ghee_button.grid_remove()
        next_screen_button.grid_remove()
        previous_screen_button.grid_remove()
        search_button.grid_remove()
        check_out_button.grid_remove()
        your_orders_button.grid_remove()

    search_button.grid_forget()
    search_button_2.grid(row=0, column=5)
    search_entry.grid(row=0, column=1, columnspan = 3)
    frame.grid(row=0, column=0)
    back_button.grid(row=0, column=0)
    list_box.grid(row=3, column=0, columnspan=15)

    all_genre_button.grid(row=2, column=0)
    vegetables_genre_button.grid(row=2, column=1)
    dairy_genre_button.grid(row=2, column=2)
    spices_genre_button.grid(row=2, column=3)
    other_genre_button.grid(row=2, column=4)

def search():
    typed = search_entry.get().lower()
    if typed in items:
        item = typed
        search_button_2.grid_remove()
        list_box.grid_remove()
        search_entry.grid_remove()

        all_genre_button.grid_remove()
        vegetables_genre_button.grid_remove()
        dairy_genre_button.grid_remove()
        spices_genre_button.grid_remove()
        other_genre_button.grid_remove()

        search_entry.grid_remove()
        list_box.grid_remove()
        item_screen(item)

def fillout(event):
    if list_box.get(ANCHOR) != "":
        search_entry.delete(0, END)
        search_entry.insert(0, list_box.get(ANCHOR))
    lookup(0)

def update(data):
    list_box.delete(0, END)
    for i in data:
        list_box.insert(END, i.capitalize())


def lookup(event):
    run = 0
    if search_entry.get().lower() == "":
        data = item
    else:
        data = []
        for i in item:
            if search_entry.get().lower() in i:
                data.append(items[run])
            run += 1
    update(data)

def change_genre(genre):
    if genre == "all":
        item = items
        search_entry.delete(0, END)
    elif genre == "vegetables":
        item = vegetable_genre
        search_entry.delete(0, END)
    elif genre == "dairy":
        item = dairy_genre
        search_entry.delete(0, END)
    elif genre == "spices":
        item = spices_genre
        search_entry.delete(0, END)
    elif genre == "other":
        item = others_genre
        search_entry.delete(0, END)
    lookup(0)
    update(item)

def your_orders():
    global orders_filename
    global user
    global screen
    orders_filename = user + "_orders.txt"
    if os.path.isfile(orders_filename):
        fh = open(orders_filename, "r+")
        data = fh.read().split("\n")
        data.pop()
    if len(data) != 0:
        if screen == 1:

            Title_1.grid_remove()
            onion_button.grid_remove()
            carrot_button.grid_remove()
            potato_button.grid_remove()
            radish_button.grid_remove()
            cabbage_button.grid_remove()
            tomato_button.grid_remove()
            next_screen_button.grid_remove()
            previous_screen_button.grid_remove()
            search_button.grid_remove()
            check_out_button.grid_remove()
            your_orders_button.grid_remove()
        elif screen == 2:

            Title_1.grid_remove()
            eggplant_button.grid_remove()
            bitter_gourd_button.grid_remove()
            lady_fingers_button.grid_remove()
            bell_peppers_button.grid_remove()
            egg_button.grid_remove()
            bread_button.grid_remove()
            next_screen_button.grid_remove()
            previous_screen_button.grid_remove()
            search_button.grid_remove()
            check_out_button.grid_remove()
            search_button.grid_remove()
            your_orders_button.grid_remove()
        elif screen == 3:

            Title_1.grid_remove()
            cauliflower_button.grid_remove()
            lettuce_button.grid_remove()
            broccoli_button.grid_remove()
            corn_button.grid_remove()
            milk_button.grid_remove()
            sugar_button.grid_remove()
            next_screen_button.grid_remove()
            previous_screen_button.grid_remove()
            search_button.grid_remove()
            check_out_button.grid_remove()
            search_button.grid_remove()
            your_orders_button.grid_remove()
        elif screen == 4:

            Title_1.grid_remove()
            beetroot_button.grid_remove()
            cheese_button.grid_remove()
            butter_button.grid_remove()
            honey_button.grid_remove()
            pepper_button.grid_remove()
            coconutmilk_button.grid_remove()
            next_screen_button.grid_remove()
            previous_screen_button.grid_remove()
            search_button.grid_remove()
            search_button.grid_remove()
            check_out_button.grid_remove()
            your_orders_button.grid_remove()
        elif screen == 5:

            Title_1.grid_remove()
            almonds_button.grid_remove()
            coconutoil_button.grid_remove()
            jaggery_button.grid_remove()
            coconutwater_button.grid_remove()
            cocoapowder_button.grid_remove()
            curd_button.grid_remove()
            next_screen_button.grid_remove()
            previous_screen_button.grid_remove()
            search_button.grid_remove()
            check_out_button.grid_remove()
            search_button.grid_remove()
            your_orders_button.grid_remove()
        elif screen == 6:

            Title_1.grid_remove()
            greentea_button.grid_remove()
            jaggerypowder_button.grid_remove()
            salt_button.grid_remove()
            tarmarind_button.grid_remove()
            peanutbutter_button.grid_remove()
            ghee_button.grid_remove()
            next_screen_button.grid_remove()
            previous_screen_button.grid_remove()
            search_button.grid_remove()
            check_out_button.grid_remove()
            search_button.grid_remove()
            your_orders_button.grid_remove()

        orders_filename = user + "_orders.txt"
        if os.path.isfile(orders_filename):
            fh = open(orders_filename, "r+")
            data = fh.read().split("\n")
            data.pop()
            if len(data) > 0:
                order_1 = data[0]
                order_1_contents = order_1.split()
                order_1_button.grid(row=1, column=0, padx=620, pady=20)
                print(order_1_contents)
                if len(data) > 1:
                    order_2 = data[1]
                    order_2_contents = order_2.split()
                    order_2_button.grid(row=2, column=0, pady=20)
                    print(order_2_contents)
                    if len(data) > 2:
                        order_3 = data[2]
                        order_3_contents = order_3.split()
                        order_3_button.grid(row=3, column=0, pady=20)
                        print(order_3_contents)
                        if len(data) > 3:
                            order_4 = data[3]
                            order_4_contents = order_4.split()
                            order_4_button.grid(row=4, column=0, pady=20)
                            print(order_4_contents)
                            if len(data) == 5:
                                order_5 = data[4]
                                order_5_contents = order_5.split()
                                order_5_button.grid(row=5, column=0, pady=20)
                                print(order_5_contents)
        back_from_order_list_button.grid(row=0, column=0)

def show_previous_orders(order_number):
    global item_1_bill_text
    global item_1_cost_text
    global item_1_quantity_text
    global item_2_bill_text
    global item_2_cost_text
    global item_2_quantity_text
    global item_3_bill_text
    global item_3_cost_text
    global item_3_quantity_text
    global item_4_bill_text
    global item_4_cost_text
    global item_4_quantity_text
    global item_5_bill_text
    global item_5_cost_text
    global item_5_quantity_text
    global total_text
    global total_amount
    global orders_filename
    global user

    orders_filename = user + "_orders.txt"
    if os.path.isfile(orders_filename):
        fh = open(orders_filename, "r+")
        data = fh.read().split("\n")
        data.pop()
        print(data)
        items = data[order_number-1].split()
        print(items)
        no_of_items = len(items) // 4

        if no_of_items != 0:
            if order_1_button.winfo_exists():
                order_1_button.grid_forget()
            if order_2_button.winfo_exists():
                order_2_button.grid_forget()
            if order_3_button.winfo_exists():
                order_3_button.grid_forget()
            if order_4_button.winfo_exists():
                order_4_button.grid_forget()
            if order_5_button.winfo_exists():
                order_5_button.grid_forget()

            if no_of_items > 0:
                item_1_bill_text = Label(root, text=items[0].capitalize(), font=("Amazon Ember", 26, "bold"), bg="LIGHT GREY")
                item_1_quantity_text = Label(root, text=items[1], font=("Amazon Ember", 26, "bold"), bg="LIGHT GREY")
                item_1_cost_text = Label(root, text=int(items[2]) * int(items[3]), font=("Amazon Ember", 26, "bold"), bg="LIGHT GREY")
                total_cost = int(items[2]) * int(items[3])

                item_1_bill_text.grid(row=0, column=0, padx=350, pady=20)
                item_1_quantity_text.grid(row=0, column=1, padx=20)
                item_1_cost_text.grid(row=0, column=2)

                if no_of_items > 1:
                    item_2_bill_text = Label(root, text=items[4].capitalize(), font=("Amazon Ember", 26, "bold"), bg="LIGHT GREY")
                    item_2_quantity_text = Label(root, text=items[5], font=("Amazon Ember", 26, "bold"), bg="LIGHT GREY")
                    item_2_cost_text = Label(root, text=int(items[6]) * int(items[7]), font=("Amazon Ember", 26, "bold"), bg="LIGHT GREY")
                    total_cost = int(items[2]) * int(items[3]) + int(items[6]) * int(items[7])

                    item_2_bill_text.grid(row=1, column=0, pady=20)
                    item_2_quantity_text.grid(row=1, column=1)
                    item_2_cost_text.grid(row=1, column=2)
                    if no_of_items > 2:
                        item_3_bill_text = Label(root, text=items[8].capitalize(), font=("Amazon Ember", 26, "bold"), bg="LIGHT GREY")
                        item_3_quantity_text = Label(root, text=items[9], font=("Amazon Ember", 26, "bold"), bg="LIGHT GREY")
                        item_3_cost_text = Label(root, text=int(items[10]) * int(items[11]), font=("Amazon Ember", 26, "bold"), bg="LIGHT GREY")
                        total_cost = int(items[2]) * int(items[3]) + int(items[6]) * int(items[7]) + int(items[10]) * int(items[11])

                        item_3_bill_text.grid(row=2, column=0, padx=350, pady=20)
                        item_3_quantity_text.grid(row=2, column=1, padx=20)
                        item_3_cost_text.grid(row=2, column=2)
                        if no_of_items > 3:
                            item_4_bill_text = Label(root, text=items[12].capitalize(), font=("Amazon Ember", 26, "bold"), bg="LIGHT GREY")
                            item_4_quantity_text = Label(root, text=items[13], font=("Amazon Ember", 26, "bold"), bg="LIGHT GREY")
                            item_4_cost_text = Label(root, text=int(items[14]) * int(items[15]), font=("Amazon Ember", 26, "bold"), bg="LIGHT GREY")
                            total_cost = int(items[2]) * int(items[3]) + int(items[6]) * int(items[7]) + int(items[10]) * int(items[11]) + int(items[14]) * int(items[15])

                            item_4_bill_text.grid(row=3, column=0, padx=350, pady=20)
                            item_4_quantity_text.grid(row=3, column=1, padx=20)
                            item_4_cost_text.grid(row=3, column=2)
                            if no_of_items == 5:
                                item_5_bill_text = Label(root, text=items[16].capitalize(), font=("Amazon Ember", 26, "bold"), bg="LIGHT GREY")
                                item_5_quantity_text = Label(root, text=items[17], font=("Amazon Ember", 26, "bold"), bg="LIGHT GREY")
                                item_5_cost_text = Label(root, text=int(items[18]) * int(items[19]), font=("Amazon Ember", 26, "bold"), bg="LIGHT GREY")
                                total_cost = int(items[2]) * int(items[3]) + int(items[6]) * int(items[7]) + int(items[10]) * int(items[11]) + int(items[14]) * int(items[15]) + int(items[18]) * int(items[19])

                                item_5_bill_text.grid(row=4, column=0, padx=350, pady=20)
                                item_5_quantity_text.grid(row=4, column=1, padx=20)
                                item_5_cost_text.grid(row=4, column=2)

            total_text = Label(root, text="Total cost of all Items:", font=("Amazon Ember", 26, "bold"),bg="LIGHT GREY")
            total_amount = Label(root, text=total_cost, font=("Amazon Ember", 26, "bold"), bg="LIGHT GREY")

            total_text.grid(row=5, column=0, columnspan=2)
            total_amount.grid(row=5, column=2)
            back_from_order_list_button.grid(row=6, column=1)

def back_from_order_list():
    global item_1_bill_text
    global item_1_cost_text
    global item_1_quantity_text
    global item_2_bill_text
    global item_2_cost_text
    global item_2_quantity_text
    global item_3_bill_text
    global item_3_cost_text
    global item_3_quantity_text
    global item_4_bill_text
    global item_4_cost_text
    global item_4_quantity_text
    global item_5_bill_text
    global item_5_cost_text
    global item_5_quantity_text
    global total_text
    global total_amount

    if order_1_button.winfo_exists():
        order_1_button.grid_forget()
    if order_2_button.winfo_exists():
        order_2_button.grid_forget()
    if order_3_button.winfo_exists():
        order_3_button.grid_forget()
    if order_4_button.winfo_exists():
        order_4_button.grid_forget()
    if order_5_button.winfo_exists():
        order_5_button.grid_forget()
    back_from_order_list_button.grid_forget()

    if screen == 1:
        Title_1.grid(row=0, column=0, columnspan=5, padx=150, pady=15)
        onion_button.grid(row=1, column=0, padx=20, pady=15)
        carrot_button.grid(row=1, column=2, padx=20, pady=15)
        potato_button.grid(row=1, column=4, padx=20, pady=15)
        radish_button.grid(row=2, column=0, padx=20, pady=15)
        cabbage_button.grid(row=2, column=2, padx=20, pady=15)
        tomato_button.grid(row=2, column=4, padx=20, pady=15)
        search_button.grid(row=4, column=0, pady=15)
        next_screen_button.grid(row=4, column=3, pady=50)
        previous_screen_button.grid(row=4, column=1, pady=50)
        search_button.grid(row=4, column=0, pady=15)
        check_out_button.grid(row=4, column=4, rowspan=2)
        previous_screen_button["state"] = "disabled"
        your_orders_button.grid(row=4, column=2, padx=50)
    elif screen == 2:
        Title_1.grid(row=0, column=0, columnspan=5, padx=150, pady=15)
        eggplant_button.grid(row=1, column=0, padx=20, pady=15)
        bitter_gourd_button.grid(row=1, column=2, padx=20, pady=15)
        lady_fingers_button.grid(row=1, column=4, padx=20, pady=15)
        bell_peppers_button.grid(row=2, column=0, padx=20, pady=15)
        egg_button.grid(row=2, column=2, padx=20, pady=15)
        bread_button.grid(row=2, column=4, padx=20, pady=15)
        next_screen_button.grid(row=4, column=3, pady=50)
        previous_screen_button.grid(row=4, column=1, pady=50)
        check_out_button.grid(row=4, column=4, rowspan=2)
        search_button.grid(row=4, column=0, pady=15)
        your_orders_button.grid(row=4, column=2, padx=50)

    elif screen == 3:
        Title_1.grid(row=0, column=0, columnspan=5, padx=150, pady=15)
        cauliflower_button.grid(row=1, column=0, padx=20, pady=15)
        lettuce_button.grid(row=1, column=2, padx=20, pady=15)
        broccoli_button.grid(row=1, column=4, padx=20, pady=15)
        corn_button.grid(row=2, column=0, padx=20, pady=15)
        milk_button.grid(row=2, column=2, padx=20, pady=15)
        sugar_button.grid(row=2, column=4, padx=20, pady=15)
        next_screen_button.grid(row=4, column=3, pady=50)
        previous_screen_button.grid(row=4, column=1, pady=50)
        check_out_button.grid(row=4, column=4, rowspan=2)
        search_button.grid(row=4, column=0, pady=15)
        your_orders_button.grid(row=4, column=2, padx=50)

    elif screen == 4:
        Title_1.grid(row=0, column=0, columnspan=5, padx=150, pady=15)
        beetroot_button.grid(row=1, column=0, padx=20, pady=15)
        cheese_button.grid(row=1, column=2, padx=20, pady=15)
        butter_button.grid(row=1, column=4, padx=20, pady=15)
        honey_button.grid(row=2, column=0, padx=20, pady=15)
        pepper_button.grid(row=2, column=2, padx=20, pady=15)
        coconutmilk_button.grid(row=2, column=4, padx=20, pady=15)
        next_screen_button.grid(row=4, column=3, pady=50)
        previous_screen_button.grid(row=4, column=1, pady=50)
        check_out_button.grid(row=4, column=4, rowspan=2)
        search_button.grid(row=4, column=0, pady=15)
        your_orders_button.grid(row=4, column=2, padx=50)

    elif screen == 5:
        Title_1.grid(row=0, column=0, columnspan=5, padx=150, pady=15)
        almonds_button.grid(row=1, column=0, padx=20, pady=15)
        coconutoil_button.grid(row=1, column=2, padx=20, pady=15)
        jaggery_button.grid(row=1, column=4, padx=20, pady=15)
        coconutwater_button.grid(row=2, column=0, padx=20, pady=15)
        cocoapowder_button.grid(row=2, column=2, padx=20, pady=15)
        curd_button.grid(row=2, column=4, padx=20, pady=15)
        next_screen_button.grid(row=4, column=3, pady=50)
        previous_screen_button.grid(row=4, column=1, pady=50)
        check_out_button.grid(row=4, column=4, rowspan=2)
        search_button.grid(row=4, column=0, pady=15)
        your_orders_button.grid(row=4, column=2, padx=50)

    elif screen == 6:
        Title_1.grid(row=0, column=0, columnspan=5, padx=150, pady=15)
        greentea_button.grid(row=1, column=0, padx=20, pady=15)
        jaggerypowder_button.grid(row=1, column=2, padx=20, pady=15)
        salt_button.grid(row=1, column=4, padx=20, pady=15)
        tarmarind_button.grid(row=2, column=0, padx=20, pady=15)
        peanutbutter_button.grid(row=2, column=2, padx=20, pady=15)
        ghee_button.grid(row=2, column=4, padx=20, pady=15)
        next_screen_button.grid(row=4, column=3, pady=50)
        previous_screen_button.grid(row=4, column=1, pady=50)
        check_out_button.grid(row=4, column=4, rowspan=2)
        search_button.grid(row=4, column=0, pady=15)
        your_orders_button.grid(row=4, column=2, padx=50)
        next_screen_button["state"] = "disabled"

    item_1_bill_text.grid_remove()
    item_1_cost_text.grid_remove()
    item_1_quantity_text.grid_remove()
    item_2_bill_text.grid_remove()
    item_2_cost_text.grid_remove()
    item_2_quantity_text.grid_remove()
    item_3_bill_text.grid_remove()
    item_3_cost_text.grid_remove()
    item_3_quantity_text.grid_remove()
    item_4_bill_text.grid_remove()
    item_4_cost_text.grid_remove()
    item_4_quantity_text.grid_remove()
    item_5_bill_text.grid_remove()
    item_5_cost_text.grid_remove()
    item_5_quantity_text.grid_remove()
    total_text.grid_remove()
    total_amount.grid_remove()

# Making the PNG Files Readable

# Photos for the first screen

onion = PhotoImage(file="images\onion.png")
carrot = PhotoImage(file="images\carrot.png")
potato = PhotoImage(file="images\potato.png")
radish = PhotoImage(file="images/radish.png")
cabbage = PhotoImage(file="images\cabbage.png")
tomato = PhotoImage(file="images/tomato.png")

# Photos for the Second screen
eggplant = PhotoImage(file="images\eggplant.png")
bittergourd = PhotoImage(file="images\Bitter Gourd.png")
ladyfingers = PhotoImage(file="images\lady finger.png")
bellpeppers = PhotoImage(file="images\capsicum.png")
egg = PhotoImage(file="images\eggs.png")
bread = PhotoImage(file="images/bread.png")

# Photos for the Third screen
cauliflower = PhotoImage(file="images\cauliflower.png")
lettuce = PhotoImage(file="images\lettuce.png")
broccoli = PhotoImage(file="images/broccoli.png")
corn = PhotoImage(file="images\Corn.png")
milk = PhotoImage(file="images\Milk.png")
sugar = PhotoImage(file="images\Sugar.png")

# Photos for the Fourth screen
beetroot = PhotoImage(file="images/beetroot.png")
cheese = PhotoImage(file="images\cheese.png")
butter = PhotoImage(file="images/butter.png")
honey = PhotoImage(file="images\honey.png")
pepper = PhotoImage(file="images\pepper.png")
coconutmilk = PhotoImage(file="images\coconutmilk.png")

# Photos for the Fifth screen
almonds = PhotoImage(file="images/almonds.png")
coconutoil = PhotoImage(file="images\coconutoil.png")
jaggery = PhotoImage(file="images\jaggery.png")
coconutwater = PhotoImage(file="images\coconutwater.png")
cocoapowder = PhotoImage(file="images\cocoapowder.png")
curd = PhotoImage(file="images\curd.png")

# Photos for the Sixth screen
greentea = PhotoImage(file="images\greentea.png")
jaggerypowder = PhotoImage(file="images\jaggerypowder.png")
salt = PhotoImage(file="images\salt.png")
tarmarind = PhotoImage(file="images/tarmarind.png")
peanutbutter = PhotoImage(file="images\peanutbutter.png")
ghee = PhotoImage(file="images\ghee.png")

back = PhotoImage(file="images/back.PNG")
add = PhotoImage(file="images/addition.png")
subtract = PhotoImage(file="images\minus.png")
cash = PhotoImage(file="images/rupee.png")
search_image = PhotoImage(file="images\search.png")
###########################################

# Photos for the first screen
onion_image = PhotoImage(file="images\onion_image.png")
carrot_image = PhotoImage(file="images\carrot_image.png")
potato_image = PhotoImage(file="images\potato_image.png")
radish_image = PhotoImage(file="images/radish_image.png")
cabbage_image = PhotoImage(file="images\cabbage_image.png")
tomato_image = PhotoImage(file="images/tomato_image.png")

# Photos for the Second screen
eggplant_image = PhotoImage(file="images\eggplant_image.png")
bitter_gourd_image = PhotoImage(file="images\Bitter Gourd_image.png")
lady_fingers_image = PhotoImage(file="images\lady finger_image.png")
bell_peppers_image = PhotoImage(file="images\capsicum_image.png")
egg_image = PhotoImage(file="images\eggs_image.png")
bread_image = PhotoImage(file="images/bread_image.png")

# Photos for the Third screen
cauliflower_image = PhotoImage(file="images\cauliflower_image.png")
lettuce_image = PhotoImage(file="images\lettuce_image.png")
broccoli_image = PhotoImage(file="images/broccoli_image.png")
corn_image = PhotoImage(file="images\Corn_image.png")
milk_image = PhotoImage(file="images\Milk_image.png")
sugar_image = PhotoImage(file="images\Sugar_image.png")

# Photos for the Third screen
beetroot_image = PhotoImage(file="images/beetroot_image.png")
cheese_image = PhotoImage(file="images\cheese_image.png")
butter_image = PhotoImage(file="images/butter_image.png")
honey_image = PhotoImage(file="images\honey_image.png")
pepper_image = PhotoImage(file="images\pepper_image.png")
coconutmilk_image = PhotoImage(file="images\coconutmilk_image.png")

# Photos for the Third screen
almonds_image = PhotoImage(file="images/almonds_image.png")
coconutoil_image = PhotoImage(file="images\coconutoil_jmage.png")
jaggery_image = PhotoImage(file="images\jaggery_image.png")
coconutwater_image = PhotoImage(file="images\coconutwater_image.png")
cocoapowder_image = PhotoImage(file="images\cocoapowder_jmage.png")
curd_image = PhotoImage(file="images\curd_image.png")

# Photos for the Third screen
greentea_image = PhotoImage(file="images\greentea_image.png")
jaggerypowder_image = PhotoImage(file="images\jaggerypowder_image.png")
salt_image = PhotoImage(file="images\salt_image.png")
tamarind_image = PhotoImage(file="images/tarmarind_image.png")
peanutbutter_image = PhotoImage(file="images\peanutbutter_image.png")
ghee_image = PhotoImage(file="images\ghee_image.png")

# Creating the Basic Frame
frame = LabelFrame(root, borderwidth=0, highlightthickness=0)
frame2 = LabelFrame(root, borderwidth=0, highlightthickness=0)
frame2.configure(bg="LIGHT GREY")
frame.configure(bg="LIGHT GREY")

# Creating the widgets for the user login screen
name_text = Label(frame2, text="Username:")
pass_text = Label(frame2, text="Password:")
username_entry_text = StringVar()
password_entry_text = StringVar()
username_entry_text.trace("w", lambda *args: character_limit(username_entry_text))
username_entry = Entry(frame2, width=18, font=("Amazon Ember", 24, "bold"), textvariable=username_entry_text)
password_entry = Entry(frame2, width=18, font=("Amazon Ember", 24, "bold"), textvariable=password_entry_text)
# submit_button = Entry(frame2, text="Submit", command= submit_name())
sign_up_button = Button(frame2, text="Sign Up", command = lambda: Sign_up(username_entry.get(), password_entry.get()))
log_in_button = Button(frame2, text="Log In", command = lambda: Log_in(username_entry.get(), password_entry.get()))
enter_user_message = Label(frame2, text=" ")

name_text.configure(font=Title_font_settings, bg="LIGHT GREY")
pass_text.configure(font=Title_font_settings, bg="LIGHT GREY")
sign_up_button.configure(font=Interactive_font_settings)
log_in_button.configure(font=Interactive_font_settings)
enter_user_message.configure(font=Interactive_font_settings, bg="LIGHT GREY")


# Creating the Buttons:

# Screen 1 Buttons:
onion_button = Button(root, image=onion, command=lambda: item_screen("onion"))
carrot_button = Button(root, image=carrot, command=lambda: item_screen("carrot"))
potato_button = Button(root, image=potato, command=lambda: item_screen("potato"))
radish_button = Button(root, image=radish, command=lambda: item_screen("radish"))
cabbage_button = Button(root, image=cabbage, command=lambda: item_screen("cabbage"))
tomato_button = Button(root, image=tomato, command=lambda: item_screen("tomato"))

# Screen 2 Buttons:
eggplant_button = Button(root, image=eggplant, command=lambda: item_screen("eggplant"))
bitter_gourd_button = Button(root, image=bittergourd, command=lambda: item_screen("bittergourd"))
lady_fingers_button = Button(root, image=ladyfingers, command=lambda: item_screen("ladyfingers"))
bell_peppers_button = Button(root, image=bellpeppers, command=lambda: item_screen("bellpeppers"))
egg_button = Button(root, image=egg, command=lambda: item_screen("egg"))
bread_button = Button(root, image=bread, command=lambda: item_screen("bread"))

# Screen 3 Buttons:
cauliflower_button = Button(root, image=cauliflower, command=lambda: item_screen("cauliflower"))
lettuce_button = Button(root, image=lettuce, command=lambda: item_screen("lettuce"))
broccoli_button = Button(root, image=broccoli, command=lambda: item_screen("broccoli"))
corn_button = Button(root, image=corn, command=lambda: item_screen("corn"))
milk_button = Button(root, image=milk, command=lambda: item_screen("milk"))
sugar_button = Button(root, image=sugar, command=lambda: item_screen("sugar"))

# Screen 4 Buttons:
beetroot_button = Button(root, image=beetroot, command=lambda: item_screen("beetroot"))
cheese_button = Button(root, image=cheese, command=lambda: item_screen("cheese"))
butter_button = Button(root, image=butter, command=lambda: item_screen("butter"))
honey_button = Button(root, image=honey, command=lambda: item_screen("honey"))
pepper_button = Button(root, image=pepper, command=lambda: item_screen("pepper"))
coconutmilk_button = Button(root, image=coconutmilk, command=lambda: item_screen("coconutmilk"))

# Screen 5 Buttons:
almonds_button = Button(root, image=almonds, command=lambda: item_screen("almonds"))
coconutoil_button = Button(root, image=coconutoil, command=lambda: item_screen("coconutoil"))
jaggery_button = Button(root, image=jaggery, command=lambda: item_screen("jaggery"))
coconutwater_button = Button(root, image=coconutwater, command=lambda: item_screen("coconutwater"))
cocoapowder_button = Button(root, image=cocoapowder, command=lambda: item_screen("cocoapowder"))
curd_button = Button(root, image=curd, command=lambda: item_screen("curd"))

# Screen 6 Buttons:
greentea_button = Button(root, image=greentea, command=lambda: item_screen("greentea"))
jaggerypowder_button = Button(root, image=jaggerypowder, command=lambda: item_screen("jaggerypowder"))
salt_button = Button(root, image=salt, command=lambda: item_screen("salt"))
tarmarind_button = Button(root, image=tarmarind, command=lambda: item_screen("tamarind"))
peanutbutter_button = Button(root, image=peanutbutter, command=lambda: item_screen("peanutbutter"))
ghee_button = Button(root, image=ghee, command=lambda: item_screen("ghee"))

# Interactive buttons:
next_screen_button = Button(root, text=">", command=screen_next)
previous_screen_button = Button(root, text="<", command=screen_prev)
back_button = Button(frame, image=back, command=list_screen)
add_button = Button(root, image=add, borderwidth=0, highlightthickness=0, command=increase_item_quantity)
subtract_button = Button(root, image=subtract, borderwidth=0, highlightthickness=0, command=decrease_item_quantity)
buy_now_button = Button(root, image=cash, text="BUY NOW", compound=LEFT, command=buy_now_page)
add_to_cart_button = Button(root, text="Add To Cart", command=add_to_cart)
purchase_button = Button(root, text="Purchase", command=purchase_screen)
Thank_you_label = Label(root, text="Thank You For Your Purchase, Would you like to continue browsing?")
back_to_main_menu_button = Button(root, text="Back", command=main_menu)
quit_button = Button(root, text="Quit", command=root.quit)
check_out_button = Button(root, text="Check Out", command=check_out)
back_out_of_check_out_button = Button(root, text="Back", command=back_to_the_main_screen_from_checkout)
your_orders_button = Button(root, text="Your Orders", command = your_orders)
order_1_button = Button(root, text="Order 1", command = lambda: show_previous_orders(1))
order_2_button = Button(root, text="Order 2", command = lambda: show_previous_orders(2))
order_3_button = Button(root, text="Order 3", command = lambda: show_previous_orders(3))
order_4_button = Button(root, text="Order 4", command = lambda: show_previous_orders(4))
order_5_button = Button(root, text="Order 5", command = lambda: show_previous_orders(5))
back_from_order_list_button = Button(root, text="Back", command=back_from_order_list)

all_genre_button = Button(root, text="All", command=lambda: change_genre("all"))
vegetables_genre_button = Button(root, text="Vegetables", command=lambda: change_genre("vegetables"))
dairy_genre_button = Button(root, text="Dairy", command=lambda: change_genre("dairy"))
spices_genre_button = Button(root, text="Spices", command=lambda: change_genre("spices"))
other_genre_button = Button(root, text="Other", command=lambda: change_genre("other"))

# Widgets for the search function:
search_button = Button(root, image=search_image, command=Bring_up_search)
search_button_2 = Button(root, image=search_image, command=search)
search_entry = Entry(root, width=70, font=("Amazon Ember", 19, "bold"))
list_box = Listbox(root, width=80, height= 20, font=("Amazon Ember", 21, "bold"))

if list_box.winfo_exists():
    update(item)

list_box.bind("<<ListboxSelect>>", fillout)
search_entry.bind("<KeyRelease>", lookup)

# Changing the font settings for the buttons
next_screen_button.configure(font=Interactive_font_settings, bg="white")
previous_screen_button.configure(font=Interactive_font_settings, bg="white")
purchase_button.configure(font=Interactive_font_settings)
buy_now_button.configure(font=Interactive_font_settings, bg="Green")
add_to_cart_button.configure(font=Interactive_font_settings, bg="Yellow")
Thank_you_label.configure(font=Title_font_settings, bg="LIGHT GREY")
back_to_main_menu_button.configure(font=Interactive_font_settings)
quit_button.configure(font=Interactive_font_settings)
check_out_button.configure(font=Interactive_font_settings, bg="white")
back_out_of_check_out_button.configure(font=Interactive_font_settings)
all_genre_button.configure(font=Interactive_font_settings)
vegetables_genre_button.configure(font=Interactive_font_settings)
dairy_genre_button.configure(font=Interactive_font_settings)
spices_genre_button.configure(font=Interactive_font_settings)
other_genre_button.configure(font=Interactive_font_settings)
your_orders_button.configure(font=Interactive_font_settings)
order_1_button.configure(font=Interactive_font_settings)
order_2_button.configure(font=Interactive_font_settings)
order_3_button.configure(font=Interactive_font_settings)
order_4_button.configure(font=Interactive_font_settings)
order_5_button.configure(font=Interactive_font_settings)
back_from_order_list_button.configure(font=Interactive_font_settings)


if screen == 1:
    previous_screen_button["state"] = "disabled"
elif screen == 3:
    next_screen_button["state"] = "disabled"

# To avoid a NameError:
item_1_bill_text = Label(root)
item_1_quantity_text = Label(root)
item_1_cost_text = Label(root)

item_2_bill_text = Label(root)
item_2_quantity_text = Label(root)
item_2_cost_text = Label(root)

item_3_bill_text = Label(root)
item_3_quantity_text = Label(root)
item_3_cost_text = Label(root)

item_4_bill_text = Label(root)
item_4_quantity_text = Label(root)
item_4_cost_text = Label(root)

item_5_bill_text = Label(root)
item_5_quantity_text = Label(root)
item_5_cost_text = Label(root)

total_text = Label(root)
total_amount = Label(root)

item_text = Label(root)
qnt = Label(root)
cost = Label(root)
total = Label(root)
total_cost = Label(root)

# Placing the Buttons on the Screen
frame2.place(x=380, y=250)
name_text.grid(row=0, column=0, padx=10, pady=10)
pass_text.grid(row=1, column=0)
username_entry.grid(row=0, column=1)
password_entry.grid(row=1, column=1)
sign_up_button.grid(row=2, column=0)
log_in_button.grid(row=2, column=1)
enter_user_message.grid(row=3, column=0, columnspan=2)

# Maximizing the window by default
root.minsize(width=1366, height=768)
root.maxsize(width=1366, height=768)

root.state('zoomed')

root.mainloop()
