from fastapi import FastAPI
import os

app = FastAPI()

@app.get('/')
async def root():

  name = os.getenv("name", "World")
  return {'message': 'hello '+ name + ' from Python.'}
