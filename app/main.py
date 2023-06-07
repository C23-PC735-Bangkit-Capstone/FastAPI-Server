from fastapi import FastAPI
from starlette.middleware.cors import CORSMiddleware

from app.api.user_package.router import router as users_router
from app.api.pond_package.router import router as ponds_router
from app.api.device_package.router import router as devices_router
from app.api.vibration_package.router import router as vibrations_router
from app.api.vibrationhealth_package.router import router as vibrationhealths_router

from app.database import get_db

description = """
The Smart Vibration Monitoring System for Shrimp Paddle Wheel Aerator's API Server is a component of a larger system designed to monitor the vibrations of shrimp paddle wheel aerators. This API server provides a way to interact with the system programmatically.
"""

def create_app():
    # Initialize FastAPI app
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

    app.include_router(users_router)
    app.include_router(ponds_router)
    app.include_router(devices_router)
    app.include_router(vibrations_router)
    app.include_router(vibrationhealths_router)

    return app


application = create_app()
