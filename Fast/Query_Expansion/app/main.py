from fastapi import FastAPI
from app.api.QE import qe
# import uvicorn

app = FastAPI(openapi_url="/api/v1/query_expansion/openapi.json", docs_url="/api/v1/query_expansion/docs")

app.include_router(qe, prefix="/api/v1/query_expansion", tags=["query_expansion"])

# if __name__ == "__main__":
#     uvicorn.run("main:app", host="0.0.0.0", port=8080)