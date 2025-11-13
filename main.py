from fastapi import FastAPI
# from uvicorn import uvicorn
app = FastAPI()

@app.get("test/")
def basic_endpoints():
   return{"msg":"hi from test"}


@app.get("/test/{name}")
def test(name:str):
   return {"name":name}
   
@app.get("/fence/encrypt{text}")
def Fence_cipher_endpoints(text:str):
   return {"encrypted_text":text }   

