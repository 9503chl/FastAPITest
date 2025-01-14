from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

import requests as req

app = FastAPI()

db = []

class City(BaseModel):
    name: str
    timezone: str

@app.get("/")
async def root():
    return {"message": "API Test"}

#특정 도시 정보 id로 Get
@app.get("/cities/{city_id}") 
async def get_city(city_id: int):
    city = db[city_id]
    #r = req.get(f"http://worldtimeapi.org/api/timezone/{city.timezone}")
    #cur_time = r.json()["datetime"]
    #return {"name": city.name, "timezone": city.timezone, "current_time": cur_time}
    return{"name": city.name, "timezone": city.timezone}


#모든 리스트에 있는 정보 Get
@app.get("/cities") 
async def get_cities():
    try:
        results = []
        for city in db:
            #r = req.get(f"http://worldtimeapi.org/api/timezone/{city.timezone}")
            #cur_time = r.json()["datetime"]
            #results.append({"name": city.name, "timezone": city.timezone, "current_time": cur_time})
            results.append({"name": city.name, "timezone": city.timezone})

        return results
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
    
#도시 추가 Post
@app.post("/cities") 
async def create_city(city: City):
    db.append(city)
    return city

#도시 삭제 Delete
@app.delete("/cities/{city_id}") 
def delete_city(city_id: int):
    db.pop(city_id)
    return {"message": f"{city_id}번 도시가 삭제되었습니다"}
