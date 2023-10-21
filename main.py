from fastapi import FastAPI
from enum import Enum
from typing import Optional
from pydantic import BaseModel
app=FastAPI()

@app.get("/")
async def root():
    return {"message":"hello world"}

@app.post("/")
async def post():
    return {"message":"hello from the post route"}
@app.get("items/")
async def list_items():
    return {"messages":"list item root"}
# @app.get("/items/{item_id}")
# async def get_item(item_id:str):
#     return {"item_id":item_id}

class FoodEnum(str,Enum):
    fruits='fruits'
    vegetables='vegetables'
    dairy='dairy'

@app.get('/foods/{food_name}')
async def get_food(food_name:FoodEnum):
    if food_name.value=='vegetables':
        return {'foodname':food_name,'messages':'you are helathy' }
    if food_name.value=='fruits':
        return {'foodname':food_name,'messages':'this is a vitamin also good for health'}
    return {'messages':'i like this food though its not good for health'}

fake_item_db=[{'istiaq'},{'hasan'},{'arup'}]
@app.get('/items')
async def list_items(skip:int=0,limit:int=2 ):
    return fake_item_db[skip:skip+limit]
@app.get("/items/{item_id}")
async def get_items(item_id: str, q: str | None=None , short: bool = False):
    item={"item_id":item_id}
    if q:
        item.update({"q": q})
    if  not short:
        item.update(
            {'description':'lorem ipsum dolar sit ammet'}
        )
    return item
fakedb=[]
class Course(BaseModel):
    id:int
    name:str
    price:float
    is_early_bird:Optional[bool]=None

@app.get("/")
def read_root():
    return {"greetings":"welcome to LearnCOde.in"}

@app.get("/course")
def get_courses():
    return fakedb
@app.get("/courses/{course_id}")
def get_a_course(course_id:int):
    course=course_id-1
    return fakedb[course]
@app.post("/courses")

def add_course(course:Course):
    value=fakedb.append(course.dict())
    value.save
    return fakedb[-1]

@app.delete("/courses/{course_id}")
def delete_course(course_id:int):
    fakedb.pop(course_id-1)
    return {"task":"deletion successfull"}