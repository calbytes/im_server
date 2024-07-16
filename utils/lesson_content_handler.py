from bs4 import BeautifulSoup
import ast
import re

def get_dict_obj(obj):
    dict = ast.literal_eval(obj)
    return dict

def get_tuple_obj(obj):
    dict = ast.literal_eval(obj)
    lesson_order = dict["lesson_order"]
    lesson_name = dict["lesson_name"]
    chapter_name = dict["chapter_name"]
    unit_name = dict["unit_name"]
    curriculum_name = dict["curriculum_name"]
    subject_name = dict["subject_name"]
    content_title = dict["content_title"]
    content_body = dict["content_body"]
    body = clean_content(content_body)
    return (body, lesson_order, lesson_name, chapter_name, unit_name, curriculum_name, subject_name, content_title)

def clean_content(content):
    soup = BeautifulSoup(content, "html.parser")
    text_content = soup.get_text(separator="\n")
    cleaned_content = re.sub(r'\n\s*\n', '\n\n', text_content).strip()
    return cleaned_content