from flask import Flask
from src.XMLDocument import XMLDocument
from src.WikiAPI import WikiAPI

app = Flask(__name__)


@app.route('/')
def hello_world():
    get_wiki_content = WikiAPI()
    return get_wiki_content.get_page_header_text_image("Ivan Vazov")


if __name__ == '__main__':
    app.run()

    get_wiki_content = WikiAPI()
    print(get_wiki_content.get_page_header_text("Ivan Vazov"))
