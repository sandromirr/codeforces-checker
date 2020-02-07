from User import User

if __name__ == "__main__":
    user = User("sandromirr")
    user.about_me()
    print(user.check_solved_problem("Domino piling",1,10))