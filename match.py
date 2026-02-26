grade = int(input("Enter your grade :"))
is_interested_sports = input("Are you interested in sports? (yes/no) :").lower()
match grade:
    case 1:
        print("Let the children to play")
    case 2:
        print("Teach children to clean their room and surroundings")
    case 3:
        print("Teach the child to Respect elders and be kind to others")
    case 4 if is_interested_sports == "yes":
        print("Encourage the child to play sports and stay active")
    case 5 if is_interested_sports == "yes":
        print("Give preference to both studies and sports")
    case _:
        print("The child has a capability to take their own decision .Good Luck!")   