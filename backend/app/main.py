from fastapi import FastAPI, status
from fastapi.routing import APIRoute

app = FastAPI()


@app.get('/test', status_code=status.HTTP_200_OK)
def test():

    return {'message': 'All Oka'}