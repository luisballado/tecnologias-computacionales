"""
Basic video exporting example
"""

import pathlib
from abc import ABC, abstractmethod

class VideoExporter(ABC):
    """Basic representation of video exporting codec."""

    @abstractmethod
    def prepare_export(self,video_data):
        """Prepares video data for exporting."""

    @abstractmethod
    def do_export(self,folder:pathlib.Path):
        """Exports the video data to a folder."""

class LosslessVideoExporter(VideoExporter):
    """Lossless video exporting codec."""

    def prepare_export(self,video_data):
        print("Preparing video data for lossless export.")

    def do_export(self,folder:pathlib.Path):
        print("Exporting video data in lossless format to")

        
