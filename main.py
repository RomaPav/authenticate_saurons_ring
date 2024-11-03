import uvicorn
from fastapi import FastAPI
from starlette.middleware.cors import CORSMiddleware

from controller.auth_controller import router

app = FastAPI()

origins = [
    "http://localhost:4200",
    "https://myfrontenddomain.com",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(router, prefix="/users")
@app.get("/")
async def read_root():
    return {"message": "Welcome to my API!"}

if __name__ == "__main__":
    uvicorn.run("main:app", host="127.0.0.1", port=8000, reload=True)

# if __name__ == "__main__":
#     import uvicorn
#     uvicorn.run(app, host="0.0.0.0", port=5000)
