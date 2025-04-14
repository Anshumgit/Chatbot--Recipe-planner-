# ---Greeting---
print("Welcome to food planner ChatBot")
print("Hola, I amf Zor.")
print("What can I cook for you")
print("Press 'exit' and 'bye' to Quit")
# ---RECIPE DATABASE---
r = {
    "pasta": {
        "ingredients": ["pasta", "tomato sauce", "garlic", "olive oil", "basil"],
        "instructions":"Boil the pasta. In a pan, sauté garlic in olive oil, add tomato sauce, and basil. Mix with pasta."
    },
    "omelette": {
        "ingredients": ["eggs", "milk", "cheese", "salt", "pepper"],
        "instructions":"Beat the eggs with milk, add salt and pepper. Pour into a pan, add cheese, and cook until set."
    },
    "salad": {
        "ingredients": ["lettuce", "tomato", "cucumber", "olive oil", "lemon"],
        "instructions":"Chop lettuce, tomato, and cucumber. Drizzle with olive oil and lemon juice. Toss and serve."
    },
    "maggi": {
        "ingredients": ["maggi noodles", "water", "maggi tastemaker", "vegetables (optional)"],
        "instructions":"Boil water, add vegetables if desired. Add maggi noodles and tastemaker. Cook for 2-3 minutes until noodles are soft."
    },
    "tea": {
        "ingredients": ["water", "milk", "tea leaves", "sugar", "cardamom (optional)", "ginger (optional)"],
        "instructions": "Boil water with cardamom and ginger. Add tea leaves, simmer for 1-2 minutes. Add milk and sugar, simmer for 2 more minutes. Strain and serve hot."
    },
    "kheer": {
        "ingredients": ["rice", "milk", "sugar", "cardamom", "chopped nuts (optional)"],
        "instructions":"Boil milk, add rice, and cook until rice is soft. Add sugar, cardamom, and nuts. Cook until it thickens. Serve chilled or warm."
    },
    "paneer butter masala": {
        "ingredients": ["paneer", "tomato", "cream", "butter", "garam masala", "onion", "ginger"],
        "instructions":"Cook onions, ginger, and tomatoes with spices. Add paneer and cream, simmer until thick. Serve with naan or rice."
    },

    "chole bhature": {
        "ingredients": ["chickpeas", "onion", "tomato", "garam masala", "bhature flour", "yogurt"],
        "instructions":"Cook chickpeas with spices. Prepare bhature dough with flour and yogurt. Fry bhature and serve with chole."
    }
}   

week_end = {
    "breakfast": ["omelette", "pancakes", "smoothie", "tea"],
    "lunch": ["pasta", "maggi", "salad", "chole bhature"],
    "dinner": ["paneer butter masala", "veg biryani", "dal tadka", "chole bhature"]
}

d = ["chocolate cake", "vanilla sponge", "red velvet cake", 
            "caramel pudding", "rice pudding", "chocolate mousse",
            "vanilla ice cream", "strawberry sorbet", "mint chocolate chip"]

# ---STARTING---
while True:
    print("1. Enter letter 'W' For week End food")
    print("2. Enter Word 'R' to cook ")
    print("3. Enter Word 'D' for Dessert ")
    user_inp=input("Please Enter Word Here:").lower()
    
    if "exit" in user_inp or "bye" in user_inp:
        print("\n")
        print("Chef Zor: Goodbye! Happy cooking! ")
        break

    if user_inp in ['hello','hi','hola']:
        print("Chef Zor: Hello! My name is Zor I am a chef")

    # --- Recipe Request---
    elif "r" in user_inp:
        print("Chef Zor: Sure! Just tell me the dish you're interested in (e.g., maggi, tea, paneer butter masala).")
        dish= input("Make a dish here:")

        if dish in r:
            recipe = r[dish]
            print(f"\nChef Zor: Here's the recipe for {dish.title()}!")

            print("Ingredients:")
            for ingredient in recipe["ingredients"]:
                print(f" - {ingredient}",end="\n") 

            print("\nInstructions:")
            print(f"{recipe['instructions']}")
        else:
            print("Chef Zor: Sorry! I don't have that recipe")
            print("Try another one")
            print("We have chole bhature,kheer,salad,pasta")
    
    # ---Weekend special---
    elif "w" in user_inp:
        print("\n")
        print("Chef Zor: Great! Here is some Week End food")
        for meal,dishes in week_end.items():
            print(f" \n{meal.title()}:")
            for dish in dishes:
                print(f"-{dish.title()}")
        print("\n")

    elif "d" in user_inp:
        print("\n")
        print("Chef Zor: Great! Here is some Some sweet for you")
        for sweet in d:
            print(f"-{sweet}")
        print("\n")

    else:
        print("Chef Zor: Sorry, I didn't understand that. Please try again.")

    