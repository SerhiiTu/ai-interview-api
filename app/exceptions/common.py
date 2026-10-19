from app.exceptions.base import AppException


class ObjectNotFoundError(AppException):
    pass


class ResourceConflictError(AppException):
    pass