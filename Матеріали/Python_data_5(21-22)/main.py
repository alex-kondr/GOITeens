import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt


# https://drive.google.com/drive/folders/1DYK70daRFy6nz4yMVNYQu8IDkR41oZXi


# Series.str.lower()
# data = {
#     'Name': ['Anna Smith', 'BEN JOHNSON', 'Clara Lee', 'DAVID KIM']
# }
# df = pd.DataFrame(data)
# df['Name_Lower'] = df['Name'].str.lower()

# Series.str.upper()
# data = {
#     'Name': ['Anna Smith', 'Ben Johnson', 'Clara Lee', 'David Kim']
# }
# df = pd.DataFrame(data)
# df['Name_Upper'] = df['Name'].str.upper()

# str.capitalize()
# df['Name_Capitalized'] = df['Name'].str.capitalize()

# str.title()
# df['Name_Title'] = df['Name'].str.title()

# 💡 Важливо. Методи .str можуть повертати помилки, якщо у серії є NaN або інші нестрокові значення.
# df['Name_Lower'] = df['Name'].str.lower().fillna('unknown')

# Ви можете комбінувати кілька методів обробки тексту в одному рядку.
# df['Name_Clean'] = df['Name'].str.strip().str.lower()

# Пошук і заміна тексту

# str.contains()
# Series.str.contains(pat, case=True, flags=0, na=None, regex=True)
# pat: Патерн для пошуку (може бути рядком або регулярним виразом).
# case: Визначає чутливість до регістру (за замовчуванням True).
# na: Значення, яке буде використовуватися для NaN (за замовчуванням NaN).
# regex: Визначає, чи слід використовувати регулярні вирази (за замовчуванням True)

# data = {
#     'Comment': ['I love Python!', 'Pandas is great.', 'Regular expressions are powerful.', 'Data analysis with Pandas.', 'Python is versatile.']
# }
# df = pd.DataFrame(data)
# df['Contains_Pandas'] = df['Comment'].str.contains('Pandas')

# str.find()
# Series.str.find(sub, start=0, end=None)
# sub: Підрядок для пошуку.
# start: Початкова позиція пошуку (за замовчуванням 0).
# end: Кінцева позиція пошуку (за замовчуванням None, що означає до кінця рядка).

# data = {
#     'Sentence': ['The quick brown fox', 'jumps over the lazy dog', 'Python programming is fun', 'Pandas makes data easy', 'Regular expressions are useful']
# }
# df = pd.DataFrame(data)
# df['Position_data'] = df['Sentence'].str.find('data')

# Метод replace() дозволяє замінювати певні підрядки або шаблони у текстових даних на інші значення.
# Series.replace(to_replace, value=None, inplace=False, regex=False)
# to_replace: Підрядок або шаблон для заміни.
# value: Значення, на яке слід замінити to_replace.
# inplace: Якщо True, змінює серію на місці (за замовчуванням False).
# limit: Максимальна кількість замін.
# regex: Якщо True, to_replace розглядається як регулярний вираз.
# method: Метод заповнення ('pad', 'bfill' тощо).

# data = {
#     'Product': ['Apple Pie', 'Banana Bread', 'Cherry Tart', 'Date Cookie', 'Elderberry Jam']
# }
# df = pd.DataFrame(data)
# df['Product_Updated'] = df['Product'].replace('Pie', 'Cake', regex=False)

# Заміна кількох значень одночасно:
# data = {
#     'Status': ['pending', 'completed', 'in_progress', 'failed', 'completed']
# }
# df = pd.DataFrame(data)
# df['Status_Updated'] = df['Status'].replace({
#     'pending': 'Awaiting',
#     'completed': 'Done',
#     'failed': 'Error'
# }, regex=False)

# Приклад 1: Пошук електронних адрес
# data = {
#     'ReviewID': [1, 2, 3, 4, 5],
#     'ReviewText': [
#         'Please contact us at support@example.com for assistance.',
#         'No email provided in this review.',
#         'Reach out to john.doe@domain.co.uk for more info.',
#         'Send your feedback to feedback@service.io!',
#         'This review does not contain an email.'
#     ]
# }
# df = pd.DataFrame(data)
# email_pattern = r'[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\\.[a-zA-Z0-9-.]+'
# df['Contains_Email'] = df['ReviewText'].str.contains(email_pattern, regex=True)

# Приклад 2: Перевірка формату дати
# data = {
#     'EntryID': [1, 2, 3, 4, 5],
#     'Date': ['12/05/2021', '31-12-2020', '01/01/2022', '2021/07/15', '15/08/2021']
# }
# df = pd.DataFrame(data)
# date_pattern = r'^\\d{2}/\\d{2}/\\d{4}$'
# df['Valid_Date'] = df['Date'].str.contains(date_pattern, regex=True)

# Приклад 3: Видалення HTML-тегів
# data = {
#     'CommentID': [1, 2, 3, 4, 5],
#     'Comment': [
#         '<p>This is a <strong>great</strong> product!</p>',
#         'No HTML tags here.',
#         '<div>Check out our <a href="#">website</a>.</div>',
#         'Another comment with <em>emphasis</em>.',
#         'Clean text without tags.'
#     ]
# }
# df = pd.DataFrame(data)
# html_pattern = r'<.*?>'
# df['Clean_Comment'] = df['Comment'].str.replace(html_pattern, '', regex=True)

# Приклад 4: Видалення цифр з рядка
# data = {
#     'Code': ['A123', 'B456', 'C789', 'D012', 'E345']
# }
# df = pd.DataFrame(data)
# df['Code_Clean'] = df['Code'].replace(r'\\d+', '', regex=True)

# Приклад 5: Заміна пунктуації
# data = {
#     'Feedback': ['Great job!!!', 'Could be better??', 'Excellent!', 'Not bad...', 'Terrible!!!?']
# }
# df = pd.DataFrame(data)
# df['Feedback_Clean'] = df['Feedback'].replace('[!?]', '.', regex=True)

# ВЕКТОРИЗАЦІЯ VS ЦИКЛИ
# ❌ Неефективний приклад (цикл):
# data = {
#     'Text': ['Sample text one.', 'Another sample text!', 'More text data...'] * 333333 + ['Final sample text.']
# }
# df = pd.DataFrame(data)
# clean_text = []
# for text in df['Text']:
#     clean = re.sub(r'[^\\w\\s]', '', text)
#     clean_text.append(clean)
# df['Clean_Text'] = clean_text

# ✅ Ефективний приклад (векторизація):
# data = {
#     'Text': ['Sample text one.', 'Another sample text!', 'More text data...'] * 333333 + ['Final sample text.']
# }
# df = pd.DataFrame(data)
# df['Clean_Text'] = df['Text'].str.replace('[^\\w\\s]', '', regex=True)

# Категоріальні дані
# data = {
#     'Category': ['A', 'B', 'A', 'C', 'B'] * 200000
# }
# df = pd.DataFrame(data)
# df['Category'] = df['Category'].astype('category')

# Методи .str можуть не працювати з NaN. Використовуйте fillna() перед застосуванням:
# df['Comment'] = df['Comment'].fillna('')
# df['Comment_Clean'] = df['Comment'].str.strip().str.lower()