from fastapi import FastAPI

app = FastAPI()

@app.get('/')
async def f_index():
    return {"FIO": "Барсукова Яна Сергеевна"}

@app.get('/users')
async def f_indexU():
    return {"Telephone": "89025415700"}

@app.get('/tools')
async def f_indexT():
    return {"Skills": "знание нескольких языков программирования"}