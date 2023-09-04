# Возьмите любые 1-3 задания из прошлых домашних заданий.
# Добавьте к ним логирование ошибок и полезной информации.
# Также реализуйте возможность запуска из командной строки с передачей параметров.

import argparse
import logging
from Student_Exceptions import StudentNameError, InvalidSubjectError, InvalidScoreError
from Student import Student


logging.basicConfig(filename='student.log', level=logging.ERROR, format='%(asctime)s - %(levelname)s - %(massage)s')

def main():
    parser = argparse.ArgumentParser(description='Process student information.')
    parser.add_argument('name', help='Student name')
    parser.add_argument('csv_filename', help='CSV filename')
    args = parser.parse_args()

    try:
        student = Student(args.name, args.csv_filename)

        #Вызываем ошибку класса Student
        student.add_score('Math', 6)

    except StudentNameError:
        logging.error('Invalid student name format.')
    except InvalidSubjectError as e:
        logging.error(f'Invalid subject: {e.subject}')
    except InvalidScoreError as e:
        logging.error(f'Invalid score: {e.score}')

if __name__ == '__main__':
    main()
