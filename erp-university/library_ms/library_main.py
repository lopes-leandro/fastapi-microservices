from fastapi import FastAPI

from controller import admin, management

library_app = FastAPI()

library_app.include_router(admin.router)
library_app.include_router(management.router)