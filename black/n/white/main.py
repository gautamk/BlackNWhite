import logging
import os
import markdown
from black.n.white import DirectoryStructure

__author__ = 'gautam'

class BlackNWhite:
    def __init__(self, base_directory):
        logging.info("Base Directory {}".format(base_directory))
        self.base_directory = base_directory

    def process_posts(self):
        logging.info("Posts Directory")
        posts_directory = DirectoryStructure.posts_directory(self.base_directory)
        for file in os.listdir(posts_directory):
            path = os.path.join(posts_directory, file)
            if file.endswith(".md"):
                logging.info("Processing File {}".format(path))
                markdown.markdownFromFile(input=path, output=os.path.join(posts_directory, file.replace(".md", "html")))
