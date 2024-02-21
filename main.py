from fastapi import FastAPI

app = FastAPI() #Object instance


'''
@app: path operation decorator
get : Operation
("/") : base path
function : path operation function
'''

@app.get("/")  #Decorator
def sample(): 
    return {"a":[1,2,3],'b':{'a':1,'b':2,'c':True,'d':False}}


@app.get("/myfunction")
def sample():
    return {"Nithish":"Good boy",'mandatory':{"Sowjanya":"Good gitl",'swathi':'short girl','sonu':'dhost'}}

@app.get("/function")
def sample2():
    return "Mahesh and sonu are friends"

