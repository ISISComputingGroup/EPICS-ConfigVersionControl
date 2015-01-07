# Version Control class for dealing with SVN file operations

import subprocess
import os

class SVNVersionControl:

    def info(self, working_directory):
#   returns some information on the repository
        subprocess.check_call(["svn", "info", working_directory], stdout=subprocess.PIPE)

    def add(self, path):
#   adds a file to the repository
        subprocess.Popen("svn add \"" + path + "\"", stdout=subprocess.PIPE)

    def commit(self, working_directory, commit_comment):
#   commits changes to a file to the repository

        curr_dir = os.getcwd()
        os.chdir(working_directory)

        subprocess.Popen("svn commit -m \"" + commit_comment + "\"", stdout=subprocess.PIPE)
        os.chdir(curr_dir)

    def update(self, update_path):
#   updates local copy from the repository
        curr_dir = os.getcwd()
        os.chdir(update_path)
        p = subprocess.Popen("svn update", stdout=subprocess.PIPE)
        os.chdir(curr_dir)