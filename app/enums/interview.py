from enum import IntEnum


class InterviewLanguage(IntEnum):
    ENGLISH = 1
    UKRAINIAN = 2
    RUSSIAN = 3


class InterviewDifficultyLevel(IntEnum):
    EASY = 1
    MEDIUM = 2
    HARD = 3


class InterviewStatus(IntEnum):
    CREATED = 1
    IN_PROGRESS = 2
    COMPLETED = 3
    FAILED = 4