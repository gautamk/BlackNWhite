import os

__author__ = 'gautam'

POSTS_DIRECTORY = "_posts_"

class DirectoryStructure:

    @staticmethod
    def posts_directory(base_directory):
        return os.path.join(base_directory, POSTS_DIRECTORY)