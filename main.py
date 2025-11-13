from fastapi import FastAPI
# from uvicorn import uvicorn
app = FastAPI()

@app.get("test/")
def basic_endpoints():
   return{"msg":"hi from test"}



# if __name__ == "__main__":
#     uvicorn.run(app, host="localhost", port=8000)