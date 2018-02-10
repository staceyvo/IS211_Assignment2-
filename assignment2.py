import csv
import urllib2

from datetime import datetime


def downloadData(url):
    """Write a function called  downloadData , which takes in a string called  url.
    The purpose of this function is to download the contents located at the  url
    and return it to the caller. You should use urllib2 for this. Do not catch any
    exceptions here, as this will be done later."""
    response = urllib2.urlopen('https://s3.amazonaws.com/cuny-is211-spring2015/birthdays100.csv')
    return response.read()


def setLogger():
    raise Exception('Not implemented')


def processData(data):
    """Write a function called  processData , which takes the contents of the file as the first
    parameter, processes the file line by line, and returns a dictionary that maps a person’s ID
    to a tuple of the form (name, birthday). The birthday needs to be a Datetime object, not a
    string. You will have to process the birthday, which has a format of dd/mm/yyyy, and convert
    it into a Datetime object """

    reader_list = csv.DictReader(data.split('\n'))
    birthdays = [x for x in reader_list]
    result = {}

    for person in birthdays:
        try:
            result[person['id']] = (person['name'], datetime.strptime(person['birthday'], '%d/%m/%Y'))
        except:
            raise Exception('Not implemented:need to log')
    return result

def displayPerson():
    raise Exception('Not implemented')


if __name__ == '__main__':
    # setting up argparse

    # download data
    downloadData()

    # set up logger
    setLogger()

    # process data
    processData()

    # give me a number and get a birthday
    personID = int(raw_input('Please enter a number.'))

    while personID > 0:
        displayPerson(personID)
        personID = int(raw_input('Please enter a number.'))
