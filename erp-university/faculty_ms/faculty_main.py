from fastapi import FastAPI

from controller import admin, assignments, books

faculty_app = FastAPI()

faculty_app.include_router(admin.router)
faculty_app.include_router(assignments.router)
faculty_app.include_router(books.router)