from fastapi import FastAPI
from starlette.middleware.cors import CORSMiddleware

from app.api.user_package.router import router as users_router
from app.api.pond_package.router import router as ponds_router
from app.api.device_package.router import router as devices_router
from app.api.vibration_package.router import router as vibrations_router
from app.api.vibrationhealth_package.router import router as vibrationhealths_router

from app.database import get_db

def create_app():
    # Initialize FastAPI app
    app = FastAPI()

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
