from fastapi import FastAPI, Request, Form, Response #form is for html
from fastapi.templating import Jinja2Templates #language for the html
from fastapi.encoders import jsonable_encoder #encode the data in json format
import uvicorn
import json
import os
from dotenv import load_dotenv

from QASystem.retrievalandgeneration import get_result


app = FastAPI() #creating an object of fastapi class

templates = Jinja2Templates(directory="templates") #this reads the html file from template directory. 

#routing to the home route

@app.get('/')   #get method would fetch the response of the request given #request is coming through this url #used for searching
async def index(request: Request): #parameter is request with the value as Request
    return templates.TemplateResponse("index.html",{"request":request})


#question would be in str. 
@app.post("/get_answer")
async def get_answer(request:Request, question: str=Form(...)):
    print(question)
    answer = get_result(question)

    response_data = jsonable_encoder(json.dumps({"answer":answer}))
    res= Response(response_data)

    return res




if __name__=="__main__":
    uvicorn.run("app:app",host="0.0.0.0",port=8000,reload=True) #reload means in case of change in app it should be reflected there.




