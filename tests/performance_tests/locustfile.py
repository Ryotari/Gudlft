from locust import HttpUser, task


class ProjectPerfTest(HttpUser):

    @task()
    def home(self):
        self.client.get("/")

    @task
    def login(self):
        self.client.post('/showSummary', {'email': 'admin@irontemple.com'})

    @task
    def purchase_points(self):

        self.client.post(
            '/purchasePlaces',
            {
                'club': "Iron Temple",
                'competition': 'Future Competition',
                'places': "1"
            }
        )
