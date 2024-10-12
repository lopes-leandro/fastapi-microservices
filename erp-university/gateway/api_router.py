
from fastapi import Request

class RedirectLibraryPortalException(Exception):
    pass

class RedirectFacultyPortalException(Exception):
    pass

class RedirectStudentPortalException(Exception):
    pass

def call_api_gateway(request: Request):
    portal_id = request.path_params['portal_id']
    print(request.path_params)
    
    if portal_id == str(1):
        raise RedirectStudentPortalException()
    elif portal_id == str(2):
        raise RedirectFacultyPortalException()
    elif portal_id == str(3):
        raise RedirectLibraryPortalException()