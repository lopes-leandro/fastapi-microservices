from fastapi import Depends, FastAPI, Request, Response
from fastapi.responses import RedirectResponse

from controller import university
from gateway.api_router import RedirectFacultyPortalException, RedirectLibraryPortalException, RedirectStudentPortalException, call_api_gateway
from student_ms import student_main
from library_ms import library_main
from faculty_ms import faculty_main
from loguru import logger

app = FastAPI()

logger.add("info.log", format="Log: [{extra[log_id]}]: {time} - {level} - {message} ", level="INFO", enqueue = True)
app.mount("/erp-university/student", student_main.student_app)
app.mount("/erp-university/faculty", faculty_main.faculty_app)
app.mount("/erp-university/library", library_main.library_app)

# 
app.include_router(university.router, dependencies=[Depends(call_api_gateway)], prefix='/erp-university')

# Trata a exceção personalizada lançada por call_api_gateway e 
# faz o redirecionamento para o microsserviço apropriado
@app.exception_handler(RedirectLibraryPortalException)
def exception_handler_library(request: Request, exc: RedirectLibraryPortalException) -> Response:
    return RedirectResponse(
        url='http://localhost:8000/erp-university/library/index'
    )

@app.exception_handler(RedirectStudentPortalException)
def exception_handler_library(request: Request, exc: RedirectStudentPortalException) -> Response:
    return RedirectResponse(
        url='http://localhost:8000/erp-university/student/index'
    )

@app.exception_handler(RedirectFacultyPortalException)
def exception_handler_library(request: Request, exc: RedirectFacultyPortalException) -> Response:
    return RedirectResponse(
        url='http://localhost:8000/erp-university/faculty/index'
    )