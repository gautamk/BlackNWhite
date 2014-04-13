import os

__author__ = 'gautam'


class BaseDirectoryStructure:
    @classmethod
    def posts_dir(cls, base_directory):
        raise NotImplementedError()

    @classmethod
    def templates_dir(cls, base_directory):
        raise NotImplementedError()


class InputDirectoryStructure(BaseDirectoryStructure):
    TEMPLATES_DIRECTORY = "_templates_"
    POSTS_DIRECTORY = "_posts_"

    @classmethod
    def posts_dir(cls, base_directory):
        return os.path.join(base_directory, cls.POSTS_DIRECTORY)

    @classmethod
    def templates_dir(cls, base_directory):
        return os.path.join(base_directory, cls.TEMPLATES_DIRECTORY)


class OutputDirectoryStructure(BaseDirectoryStructure):
    POSTS_DIRECTORY = "posts"

    @classmethod
    def posts_dir(cls, base_directory):
        return os.path.join(base_directory, cls.POSTS_DIRECTORY)