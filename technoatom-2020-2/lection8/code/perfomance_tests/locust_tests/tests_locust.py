from locust import HttpUser, TaskSet, task, between


class IOSUserBehavior(TaskSet):
    def on_start(self):
        r = self.client.get("/", auth=('yar', 333))
        self.client.headers.update({'Authorization': r.request.headers['Authorization']})

    def on_stop(self):
        self.client.get("/logout")

    @task
    def profile(self):
        self.client.get("/profile")


class AndroidUserBehavior(TaskSet):

    def on_start(self):
        r = self.client.get("/", auth=('iliya', 123))
        self.client.headers.update({'Authorization': r.request.headers['Authorization']})

    def on_stop(self):
        self.client.get("/logout")

    @task
    def shareware(self):
        self.client.get("/shareware")

    @task
    def photo(self):
        self.client.get("/photo")


class WebsiteUser(HttpUser):
    tasks = [IOSUserBehavior, AndroidUserBehavior]
    wait_time = between(1, 2)
