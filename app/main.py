from fastapi import Depends, FastAPI, Response, status
from sqlalchemy.orm import Session
from sqlalchemy.exc import OperationalError
from starlette.middleware.cors import CORSMiddleware

from app.api.device_package.router import router as device_router
from app.api.pond_package.router import router as pond_router
from app.api.users_package.router import router as users_router
from app.api.vibration_package.router import router as vibration_router
from app.api.vibrationhealth_package.router import router as vibrationhealth_router

from .database import get_db, engine
from .sqladmin import create_admin

description = """
The Smart Vibration Monitoring System for Shrimp Paddle Wheel Aerator's API Server is a component of a larger system designed to monitor the vibrations of shrimp paddle wheel aerators. This API server provides a way to interact with the system programmatically.
"""

def create_app():
    app = FastAPI(
        title="The Smart Vibration Monitoring System API Server",
        description=description,
        version="0.0.1",
        contact={
            "name": "Yahya Aqrom",
            "url": "https://yahyaqr.github.io/",
            "email": "aqrom.yahya75@gmail.com",
        },
    )

    # Enable CORS via middleware
    app.add_middleware(
        CORSMiddleware,
        allow_credentials=True,
        allow_headers=['*'],
        allow_methods=['*'],
        allow_origins=['*'],
    )

    app.include_router(device_router)
    app.include_router(pond_router)
    app.include_router(users_router)
    app.include_router(vibration_router)
    app.include_router(vibrationhealth_router)
    
    create_admin(app, engine)

    return app

app = create_app()

@app.get("/", tags=["Debug"])
def check_db(db: Session = Depends(get_db)):
    try:
        db.execute("SELECT 1")  # Execute a simple query to check database connectivity
        return Response(content="Database is accessible", status_code=status.HTTP_200_OK)
    except OperationalError as e:
        error_message = f"Database connection error: {str(e)}"
        return Response(content=error_message, status_code=status.HTTP_500_INTERNAL_SERVER_ERROR)

