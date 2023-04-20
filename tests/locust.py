from locust import HttpUser, SequentialTaskSet, task


class User(HttpUser):
    @task
    class SequenceOfTasks(SequentialTaskSet):
        @task
        def login(self):
            self.client.post("/showSummary", {
                "email": "john@simplylift.co"
            })

        @task
        def book(self):
            self.client.get("/book/Simply Lift/Spring Festival")

        @task
        def purchase(self):
            self.client.post("/purchasePlaces", {
                "competition": "Spring Festival",
                "club": "Simply Lift",
                "places": "3",
            })

        @task
        def display_points(self):
            self.client.get("/points")
