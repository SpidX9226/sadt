from fastapi import FastAPI
from fastapi.requests import HTTPConnection

from app.logger import logger
from app.models import Numbers
from app.models import User
from app.models import User_2
from app.models import Feedback

web_app = FastAPI()

user = User(name="Said Makhov", id=1)
feedbacks = []

@web_app.get("/")
def read_root():
    logger.info("hello")
    print("read root code: {}")
    return {"message": "Авторелоад действительно работает"}

@web_app.get("/users")
def get_user():
    return user

@web_app.post("/users")
def create_user(user: User_2):
    is_adult = user.age >= 18
    return {
        "name": user.name,
        "age": user.age,
        "is_adult": is_adult
    }

@web_app.post("/feedback")
def send_feedback(fb: Feedback):
    feedbacks.append(fb.model_dump())

    logger.info(feedbacks)

    return {
        "message": f"Feedback received. Thank you, {fb.name}"
    }

@web_app.post("/calculate")
def read_calculate(num: Numbers):
    res = num.num1 + num.num2
    return {"result": res}

@web_app.get("/sqrt/{num}")
def get_sqrt(num: int):
    return {"result": num*num}