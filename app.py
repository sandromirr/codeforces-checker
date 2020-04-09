from User import User

if __name__ == "__main__":
    user = User("sandromirr")
    user.about_me()
    print(user.check_user_solved_problem('Bus to Udayland'))