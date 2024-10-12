from fastapi import FastAPI

from controller import admin, assignments, books, reservation

student_app = FastAPI()

student_app.include_router(admin.router)
student_app.include_router(assignments.router)
student_app.include_router(books.router)
student_app.include_router(reservation.router)