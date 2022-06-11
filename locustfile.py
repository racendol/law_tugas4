import random
import string
from locust import HttpUser, constant, task, between

class MahasiswaTest(HttpUser):
    wait_time = constant(1)

    #stress idempotent
    # @task
    # def read_idempotent(self):
    #     self.client.get('/read/123123')

    #stress not idempotent
    @task
    def read_normal(self):
        self.client.get('/read/123123/123')

    #host: http://localhost:8888

