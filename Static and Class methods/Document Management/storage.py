from category import Category
from document import Document
from topic import Topic


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

    def get_item_by_id(self, item_id, obj):
        for item in obj:
            if item.id == item_id:
                return item

    def edit_category(self, category_id: int, new_name: str):
        category = self.get_item_by_id(category_id, self.categories)
        category.name = new_name

    def edit_topic(self, topic_id: int, new_topic: str, new_storage_folder: str):
        topic = self.get_item_by_id(topic_id, self.topics)
        topic.topic = new_topic
        topic.storage_folder = new_storage_folder

    def edit_document(self, document_id: int, new_file_name: str):
        document = self.get_item_by_id(document_id, self.documents)
        document.file_name = new_file_name

    def delete_category(self, category_id):
        category = self.get_item_by_id(category_id, self.categories)
        self.categories.remove(category)

    def delete_topic(self, topic_id):
        topic = self.get_item_by_id(topic_id, self.topics)
        self.topic.remove(topic)

    def delete_document(self, document_id):
        document = self.get_item_by_id(document_id)
        self.documents.remove(document)

    def get_document(self, document_id):
        return self.get_item_by_id(document_id, self.documents)

    def __repr__(self):
        output = []
        for doc in self.documents:
            output.append(str(doc))
        return '\n'.join(output)


c1 = Category(1, "work")
t1 = Topic(1, "daily tasks", "C:\\work_documents")
d1 = Document(1, 1, 1, "finilize project")

d1.add_tag("urgent")
d1.add_tag("work")

storage = Storage()
storage.add_category(c1)
storage.add_topic(t1)
storage.add_document(d1)

print(c1)
print(t1)
print(storage.get_document(1))
print(storage)
