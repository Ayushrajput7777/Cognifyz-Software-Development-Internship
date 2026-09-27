# Task 1: Text-Based Adventure Game
def start_game():
    print("=== Treasure Hunt ===")
    name = input("Tumhara naam kya hai? ")
    print(f"\nWelcome {name}! Tum ek andhere jungle me ho.")

    choice1 = input("Aage 2 raste hai - left / right? : ").lower()

    if choice1 == "left":
        print("\nTumhe ek nadi mili!")
        choice2 = input("Swim karoge ya boat ka wait? (swim/wait): ").lower()
        if choice2 == "wait":
            print("Boat aayi! Tum treasure tak pahuch gaye. YOU WIN!")
        else:
            print("Nadi me crocodile tha! GAME OVER!")
    elif choice1 == "right":
        print("\nTumhe ek sher mila! Sher so raha hai.")
        choice2 = input("Chup chap nikaloge ya bhaagoge? (sneak/run): ").lower()
        if choice2 == "sneak":
            print("Tum bach gaye aur treasure mil gaya! YOU WIN!")
        else:
            print("Sher jaag gaya! GAME OVER!")
    else:
        print("Galat choice! GAME OVER!")

start_game()