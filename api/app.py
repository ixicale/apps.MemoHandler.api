from venv import logger
import nest_asyncio
import uvicorn
from applications.router import Router
from aws_lambda_powertools import Tracer
from fastapi import APIRouter, FastAPI
from mangum import Mangum
from utils.constants import LOG_LEVEL, WORKING_ENV



##? SYNC TO ASYNC FOR METRICS AND LOGGER
nest_asyncio.apply()
logger.setLevel(LOG_LEVEL)

##? FASTAPI APP
app = FastAPI()


##? PATHS AND RESOURCES SETUP
router = APIRouter()
Router().dispatcher(router)
app.include_router(router)


##? AWS LAMBDA HANDLER
mangum_handler = Mangum(app)


if __name__ == "__main__":
    logger.debug(f"Working environment: {WORKING_ENV}")
    uvicorn.run(
        "app:app", host="0.0.0.0", port=8080, reload=bool(WORKING_ENV == "local")
    )
