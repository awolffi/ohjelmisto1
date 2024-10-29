class Publication:
    def __init__(self, name):
        self.name = name

    def print_information(self):
        print(self.name)


class Book(Publication):
    def __init__(self, name, author, pages):
        self.author = author
        self.pages = pages
        super().__init__(name)

    def print_information(self):
        super().print_information()
        print(f"author: {self.author} size: {self.pages} pages.")

class Magazine(Publication):
    def __init__(self, name, editor):
        self.editor = editor
        super().__init__(name)

    def print_information(self):
        super().print_information()
        print(f"editor: {self.editor}")

works = []

works.append(Magazine("Donald duck", "Aki Hyyppä"))
works.append(Book("Compartment No. 6", "rosa liksom", "192"))

for p in works:
    p.print_information()