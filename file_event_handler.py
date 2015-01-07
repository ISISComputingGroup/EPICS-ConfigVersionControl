from watchdog.events import FileSystemEventHandler
import string


class ISISFileEventHandler(FileSystemEventHandler):

    def __init__(self, version_control):

        #ToDo: OPTIONAL - check class has supplied valid version control method
        #e.g. print class(version_control)
        self.version_control = version_control

    def on_any_event(self, event):
        #when something happens in the specified directory

        filename = event.src_path

        #ignore all file activity in the ".svn" directory:
        if string.find(filename, ".svn") == -1:

            #ToDo: OPTIONAL - ignore all files already present in repository
            #otherwise after an update(), module will spot new files and try to add them again!

            #check for "created" event and call add() and commit() methods
            if event.event_type == "created":
                self.version_control.add(filename)
                self.version_control.commit()

            #check for "modified" event and call commit()
            if event.event_type == "modified":
                #ToDo: OPTIONAL - if config files edited manually, set variable to indicate commit required
                self.version_control.commit()

        #ToDo: OPTIONAL - monitor "commit required" variable and commit periodically
        #e.g. 1 minute

        #ToDo: OPTIONAL and to be discussed - remove file from repository when deleted from file system