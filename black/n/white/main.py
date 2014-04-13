import logging
import os
import markdown
from jinja2 import Environment, FileSystemLoader
from black.n.white.directory_structure import InputDirectoryStructure, OutputDirectoryStructure

__author__ = 'gautam'


class BlackNWhite:
    POST_TEMPLATE_FILE = "post.html"

    def __init__(self, base_directory):
        logging.info("Base Directory {}".format(base_directory))
        self.base_dir = base_directory
        self.posts_dir = InputDirectoryStructure.posts_dir(self.base_dir)
        self.templates_dir = InputDirectoryStructure.templates_dir(self.base_dir)
        self.jinja2_env = Environment(loader=FileSystemLoader(self.templates_dir))

    def _render_markdown_with_template(self, markdown_text, template_path, template_arg_name="post"):
        md_html = markdown.markdown(markdown_text)
        template = self.jinja2_env.get_template(template_path)
        html = template.render(**{
            template_arg_name: md_html
        })
        return html


    def _process_post_(self, file):
        path = os.path.join(self.posts_dir, file)

        logging.info("Processing File {}".format(path))

        with open(path, "r") as md_file:
            md_text = md_file.read()

        html = self._render_markdown_with_template(md_text, self.POST_TEMPLATE_FILE)
        output_posts_dir = OutputDirectoryStructure.posts_dir(self.base_dir)
        render_file_path = os.path.join(output_posts_dir, file.replace(".md", ".html"))
        with open(render_file_path, "w") as html_file:
            html_file.write(html)

    def _generate_index_(self):
        logging.info("Generating Index...")
        output_posts_dir = OutputDirectoryStructure.posts_dir(self.base_dir)
        file_list = os.listdir(output_posts_dir)
        logging.info("Found Files {}".format(file_list))
        template = self.jinja2_env.get_template("index.html")
        html = template.render(posts_dir=output_posts_dir.split("/")[-1], file_list=file_list)
        with open(os.path.join(self.base_dir, "index.html"), "w") as file:
            file.write(html)


    def render_blog(self):
        logging.info("Posts Directory")
        for file in os.listdir(self.posts_dir):
            if file.endswith(".md"):
                self._process_post_(file)
        self._generate_index_()