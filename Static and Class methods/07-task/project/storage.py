from project.category import Category
from project.document import Document
from project.topic import Topic


def get_item_by_id(item_id, collection):
    return [el for el in collection if el.id == item_id][0]


class Storage:
    def __init__(self):
        self.categories = []
        self.topics = []
        self.documents = []

    def add_category(self, category: Category):
        if category not in self.categories:
            self.categories.append(category)

    def add_topic(self, topic: Topic):
        if topic not in self.topics:
            self.topics.append(topic)

    def add_document(self, document: Document):
        if document not in self.documents:
            self.documents.append(document)

    def edit_category(self, category_id: int, new_name: str):
        category = get_item_by_id(category_id, self.categories)
        category.name = new_name

    def edit_topic(self, topic_id: int, new_topic: str, new_storage_folder: str):
        topic = get_item_by_id(topic_id, self.topics)
        topic.topic = new_topic
        topic.storage_folder = new_storage_folder

    def edit_document(self, document_id: int, new_file_name: str):
        document = get_item_by_id(document_id, self.documents)
        document.file_name = new_file_name

    def delete_category(self, category_id):
        self.categories.remove(get_item_by_id(category_id, self.categories))

    def delete_topic(self, topic_id):
        self.topics.remove(get_item_by_id(topic_id, self.topics))

    def delete_document(self, document_id):
        self.documents.remove(get_item_by_id(document_id, self.topics))

    def get_document(self, document_id):
        return get_item_by_id(document_id, self.documents)

    def __repr__(self):
        result = [repr(d) for d in self.documents]
        return '\n'.join(result)
