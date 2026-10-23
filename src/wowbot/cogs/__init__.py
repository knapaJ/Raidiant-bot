import typing
from .CogBase import CogBase
from typing import List

from .note_test import NoteTest

Cogs: List[type[CogBase]] = [
    NoteTest,
]
