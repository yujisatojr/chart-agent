from fastapi import FastAPI, Request, HTTPException, status
from fastapi.responses import JSONResponse, FileResponse, RedirectResponse
from fastapi.middleware.cors import CORSMiddleware
from fastapi.staticfiles import StaticFiles
from helper_functions import generate_chart
import os
import uvicorn

app = FastAPI()
# app.mount("/", StaticFiles(directory="../client/build", html=True), name="site")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
async def index():
    static_file_path = os.path.join('../client/build', 'index.html')
    if os.path.isfile(static_file_path):
        return FileResponse(static_file_path)
    else:
        raise HTTPException(status_code=404, detail="File not found")

@app.exception_handler(404)
async def custom_404_handler(request: Request, exc: HTTPException):
    return RedirectResponse('/')

@app.get("/generate_chart")
async def get_chart(query: str = None):
    if query is None:
        return JSONResponse(status_code=404, content={"error": "Please provide a query."})

    result = generate_chart(query)

    return JSONResponse(content=result, status_code=200)

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=5000, debug=True)