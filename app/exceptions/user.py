from app.exceptions.common import (
    ObjectNotFoundError,
    ResourceConflictError,
)


class UserNotFoundError(ObjectNotFoundError):
    pass


class EmailAlreadyExistsError(ResourceConflictError):
    pass