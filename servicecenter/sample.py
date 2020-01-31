from fastapi import FastAPI 
app = FastAPI()


@app.get("/")
def hello():
	return "hi"
@app.put("/")
def hello():
	return "hi"
@app.post("/")
def hello(name:str, id:int):
	return "hi"