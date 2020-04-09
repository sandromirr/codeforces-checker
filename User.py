import requests


class User:
    def __init__(self, name):
        self.name = name
        self.rating = 0
        self.rank = ""
        self.get_info()

    def get_info(self):
        url = f"https://codeforces.com/api/user.info?handles={self.name}"
        response = requests.get(url)
        if response.status_code == 200:
            json = response.json()
            self.rating = json['result'][0]['rating']
            self.rank = json['result'][0]['rank']

    def about_me(self):
        print(f"{self.name} {self.rating} {self.rank}")

    def check_solved_problem(self, problem_name, start, end):
        print(f"{start}-{end}")
        url = f"https://codeforces.com/api/user.status?handle={self.name}&from={start}&count={end}"
        response = requests.get(url)
        if response.status_code == 200:
            json = response.json()['result']
            #print(json)
            # return 0;
            for item in json:
                name = item['problem']['name']
                verdict = item['verdict']
                print(f"{name} {verdict}")
                if name == problem_name and verdict == 'OK':
                    return True
            if len(json) != 0:
                l = end
                r = end + 10
                return self.check_solved_problem(problem_name, l,r)

        return False

    def check_user_solved_problem(self, name):
      return self.check_solved_problem(name,1,10)