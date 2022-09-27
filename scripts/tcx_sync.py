"""
If you do not want bind any account
Only the gpx files in GPX_OUT sync
"""

from config import JSON_FILE, SQL_FILE, TCX_FOLDER

from utils import make_activities_file
from tcxparser import TCXParser


@property
def distance(self):
    m = self.activity.Lap[0].DistanceMeters
    return m if m else 0


TCXParser.distance = distance


if __name__ == "__main__":
    print("only sync tcx files in TCX_OUT")
    make_activities_file(SQL_FILE, TCX_FOLDER, JSON_FILE, file_suffix="tcx")
