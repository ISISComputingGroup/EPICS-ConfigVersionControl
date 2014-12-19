# Abstraction class to sit between file monitoring functions and Version Control System

from SVNVersionControl import SVNVersionControl
from constants import *


class VersionControlWrapper:

    def __init__(self, working_directory, vc_type):
        self.working_directory = working_directory
        if vc_type == SVN_TYPE:
            self.implements = SVNVersionControl()
        else:
            pass
#           ToDo: OPTIONAL - default case and something to deal with GIT if chosen as version control system

    def info(self, path):
#   return some information on the repository
        self.implements.info(path)

    def add(self, path):
#   add file to repository
        self.implements.add(path)

    def commit(self, commit_comment="Default Comment - Changed File"):
#   commit changes to repository
#   SVN (and possibly GIT) requires a comment for each commit.
        self.implements.commit(self.working_directory, commit_comment)

#   ToDo: OPTIONAL - reset "commit required" variable

    def update(self, update_path):
#   update local file from repository
        self.implements.update(update_path)
