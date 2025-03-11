"""A module that contains classes that will help parse/process datasets"""

from dataclasses import dataclass
from typing import Optional


@dataclass
class Song:
    """A data class that contains data of a song in our database

    Instance Attributes:
    -

    """

    track_id: str
    artists: list[str]
    album_name: str


class Playlist:
    """This class has-a collection of song objects as well as functions that help compute data of the playlist"""
