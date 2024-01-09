import os

from storage.logger import PhonebookLogger
from utils.formatting import CsvToTxtConverter, CsvToXmlConverter, CsvToJsonConverter, CsvToHtmlConverter

# Определим базовый путь к директории с данными
BASE_DATA_PATH = 'storage/data_phonebook'

# Определим пути к различным файлам
path_csv = os.path.join(BASE_DATA_PATH, 'Phonebook.csv')
path_txt = os.path.join(BASE_DATA_PATH, 'Phonebook.txt')
path_xml = os.path.join(BASE_DATA_PATH, 'Phonebook.xml')
path_json = os.path.join(BASE_DATA_PATH, 'Phonebook.json')
path_html = os.path.join(BASE_DATA_PATH, 'Phonebook.html')
log_path_str = os.path.join(BASE_DATA_PATH, 'Phonebook_log.csv')

# Создаем глобальные экземпляры классов
logger = PhonebookLogger(log_path_str)
csv_to_txt_converter = CsvToTxtConverter(path_csv, path_txt)
csv_to_xml_converter = CsvToXmlConverter(path_csv, path_xml)
csv_to_json_converter = CsvToJsonConverter(path_csv, path_json)
csv_to_html_converter = CsvToHtmlConverter(path_csv, path_html)
# Можно добавить здесь другие глобальные экземпляры, если они нужны
