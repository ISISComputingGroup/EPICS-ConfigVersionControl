import time
import subprocess
from watchdog.observers import Observer
from ISISFileEventHandler import ISISFileEventHandler
from VersionControlWrapper import VersionControlWrapper
from constants import *


class ConfigVersionControl:

    def __init__(self, working_directory):
        self.working_directory = working_directory
        self.version_control = VersionControlWrapper(working_directory, SVN_TYPE)
#       check that supplied directory is under version control
        try:
            self.version_control.info(working_directory)

        except subprocess.CalledProcessError as e:
            print e
            raise Exception("Info failed: Directory may not be under version control")
        else:
            event_handler = ISISFileEventHandler(self.version_control)
            self.observer = Observer()
            self.observer.schedule(event_handler, working_directory, recursive=True)
            self.observer.start()

    def stop(self):
#        print "in stop method"
        self.observer.stop()
        self.observer.join()

#   i.e. not automatically via the file observer firing an event, but after a new configuration is created
#   or an existing one updated via the GUI.
    def add(self, file_path):
        self.version_control.add(file_path)

#   and supply a message for the commit (e.g. change to configuration)
#   i.e. not automatically as explained above
    def commit(self, commit_comment):
        self.version_control.commit(commit_comment)

    def update(self, update_path=""):
        if update_path == "":
            update_path = self.working_directory
        self.version_control.update(update_path)

#   ToDo: OPTIONAL (but important!) - call method supplied by host when file modified
#   (i.e. let "host" know what's going on)

if __name__ == "__main__":
    path = 'C:\Instrument\Apps\EPICS\ISIS\ConfigVersionControl\svnlocal'
    test = ConfigVersionControl(path)
    test.update()
    time.sleep(10)
    test.stop()