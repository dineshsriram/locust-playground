from locust import HttpLocust, TaskSet, task

class UserBehavior(TaskSet):
    def on_start(self):
        """ on_start is called when a Locust start before any task is scheduled """
        self.createUser()

    def createUser(self):
        self.client.post("/user", {"firstName":"Dinesh", "lastName": "Sriram", "email": "dinesh@test.com"})

    @task
    def getAllUsers(self):
        response=self.client.get("/user")
	print(response.content)

    @task
    def getUserId(self):
        self.client.get("/user/1")

class User(HttpLocust):
    task_set = UserBehavior
    min_wait = 500
    max_wait = 1000
