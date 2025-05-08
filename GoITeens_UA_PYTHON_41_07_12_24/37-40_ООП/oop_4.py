# class Animal:
#     type = "Animal"

#     def __init__(self, weight: float):
#         print("Call __init__ method")
#         self.weight = weight

#     def eating(self):
#         print(f"{self.type}: Я їм їжу...")
#         self.weight += 0.5

#     def run(self):
#         print(f"{self.type}: Я біжу ->")
#         self.weight -= 0.3


# class Dog(Animal):
#     type = "Dog"

#     def bark(self):
#         print(f"{self.type} say: Bark, bark!")

#     def run(self):
#         print(f"{self.type}: Я біжу ->")
#         self.weight -= 0.4


# class Cat(Animal):
#     type = "Cat"

#     def meow(self):
#         print(f"{self.type} say: Meow...mrrrrrrr")


# class Paw:
#     def eating(self):
#         print("Я лапою їм їжу...")

#     def up(self):
#         print("Я підняв ляпу...")

#     def down(self):
#         print("Я опускаю лапу...")


# class BlackDog(Dog):
#     paw = Paw()


# dog = Dog(7)
# cat = Cat(2.6)

# black_dog = BlackDog(12)

# print(f"{black_dog.type}: Моя вага: '{black_dog.weight = }' кг")
# black_dog.eating()
# print(f"{black_dog.type}: Моя вага: '{black_dog.weight = }' кг")

# input()
# black_dog.run()
# print(f"{black_dog.type}: Моя вага: '{black_dog.weight = }' кг")

# black_dog.paw.up()
# black_dog.paw.down()



# class Human:
#     name = ""

#     def voice(self):
#         print(f"Hello! My name is {self.name}")


# class Developer(Human):
#     field_description = "My Programming language"
#     value = ""

#     def make_some_code(self):
#         return f"{self.field_description} is {self.value}"


# class PythonDeveloper(Developer):
#     value = "Python"


# class JSDeveloper(Developer):
#     value = "JavaScript"


# p_dev = PythonDeveloper()
# p_dev.name = 'Bob'
# p_dev.voice()   # Hello! My name is Bob
# print(p_dev.make_some_code())  # My Programming language is Python


# js_dev = JSDeveloper()
# print(js_dev.make_some_code())  # My Programming language is JavaScript



# class MyClass:
#     attr_class = 5

#     def __new__(cls, *args, **kwargs):
#         print("Call __new__ method...")
#         return super().__new__(cls)

#     def __init__(self, value: str|float = "Hello"):
#         print(f"Class __init__ method... {value = }")
#         self.value = value
#         self.my_list = [1]

#     def __del__(self):
#         print("Call __del__ method...")

#     def __call__(self, value):
#         print(self.__dict__)
#         print(f"Call __call__ method, {value = }")

#     def __len__(self):
#         print("Call __len__ method...")
#         return len(self.my_list)

#     def __str__(self):
#         print("Call __str__ method...")
#         return f"My atrr {self.value = }"

#     def __add__(self, other): # +
#         print("Call __add__ method...")
#         return self.attr_class + other.attr_class
#         # return f"{self.value} {other.value}"

#     def __sub__(self, other): # -
#         pass

#     def __truediv__(self, other): # /
#         pass

#     def __floordiv__(self, other):  # //
#         pass

#     def __mod__(self, other): # %
#         pass

#     def __mul__(self, other): # *
#         pass

#     def __pow__(self, other): # **
#         pass

#     def __gt__(self, other): # >
#         pass

#     def __lt__(self, other): # <
#         pass

#     def __eq__(self, other): # ==
#         pass

#     @staticmethod
#     def my_func(value):
#         print(f"Value by my_func '{value}'")

#     @classmethod
#     def my_class_method(cls):
#         print(f"Attr class '{cls.attr_class}'")


# class Message:
#    def process(self):
#        pass


# class TextMessage(Message):
#    def process(self):
#        return "Processing text message."


# class ImageMessage(Message):
#    def process(self):
#        return "Processing image message."


# class AudioMessage(Message):
#    def process(self):
#        return "Processing audio message."


# class VideoMessage(Message):
#    def process(self):
#        return "Processing video message."


# class DocumentMessage(Message):
#    def process(self):
#        return "Processing document message."


# def process_message(message: Message):
#    print(message.process())


# messages = [TextMessage(), ImageMessage(), AudioMessage(), VideoMessage(), DocumentMessage()]


# for msg in messages:
#    process_message(msg)


# class FileProcessor:
#    def process(self):
#        return "Processing a generic file."


# class TextFileProcessor(FileProcessor):
#    def process(self):
#        return "Processing a text file."


# class JsonFileProcessor(FileProcessor):
#    def process(self):
#        return "Processing a JSON file."


# from abc import ABC, abstractmethod


# class PaymentProcessor(ABC):
#    @abstractmethod
#    def process_payment(self, amount):
#        pass


# class CreditCardProcessor(PaymentProcessor):
#    def process_payment(self, amount):
#        print(f"Processing credit card payment of ${amount}")


# class PayPalProcessor(PaymentProcessor):
#    def process_payment(self, amount):
#        print(f"Processing PayPal payment of {amount} USD.")


# class DocumentManager(ABC):
#    @abstractmethod
#    def open_document(self, filepath):
#        pass


#    @abstractmethod
#    def save_document(self, filepath):
#        pass


# class WordDocumentManager(DocumentManager):
#    def open_document(self, filepath):
#        print(f"Opening Word document at {filepath}")


#    def save_document(self, filepath):
#        print(f"Saving Word document to {filepath}")


# class ExcelDocumentManager(DocumentManager):
#    def open_document(self, filepath):
#        print(f"Opening Exel document at {filepath}")


#    def save_document(self, filepath):
#        print(f"Saving Exel document to {filepath}")

# def manage_document(manager: DocumentManager, filepath: str):
#    manager.open_document(filepath)
#    manager.save_document(filepath)


# word_manager = WordDocumentManager()
# exel_manager = ExcelDocumentManager()


# manage_document(word_manager, "report.pdf")
# manage_document(exel_manager, "summary.docx")
