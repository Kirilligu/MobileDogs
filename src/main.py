from fastapi import FastAPI
from .database import engine, Base
from .users.router import router as users_router
from .devices.router import router as devices_router
from .tasks.router import router as tasks_router
from .logging_config import setup_logger

Base.metadata.create_all(bind=engine)
app = FastAPI()

app_logger = setup_logger('app_logger', 'logs/app.log')
user_logger = setup_logger('user_logger', 'logs/user.log')
device_logger = setup_logger('device_logger', 'logs/device.log')

app.include_router(users_router, prefix="/users", tags=["users"])
app.include_router(devices_router, prefix="/devices", tags=["devices"])
app.include_router(tasks_router, prefix="/tasks", tags=["tasks"])
