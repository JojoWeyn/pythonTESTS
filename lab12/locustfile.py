from locust import HttpUser, task, between

class MyUser(HttpUser):
    wait_time = between(1, 3)

    @task
    def read_root(self):
        self.client.get("/")

    @task
    def create_user(self):
        user_data = {
            "index": 1,
            "name": "Test User",
            "role": "admin"
        }
        self.client.post("/user", json=user_data)

    @task
    def get_users(self):
        self.client.get("/user")

    @task
    def get_user(self):
        self.client.get("/user/1")

    @task
    def delete_user(self):
        self.client.delete("/user/1")
