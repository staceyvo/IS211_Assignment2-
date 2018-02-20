#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Create a program that returns a birthday or logs an error."""

import argparse
import csv
import logging
import urllib2

from datetime import datetime


def downloadData(url):
    """This function called downloadData downloads the contents located at the url
    and returns it to the caller.

            Args:
                url takes a string called url

            Returns:
                Returns the contents located at the url.

    """
    response = urllib2.urlopen(url)
    return response.read()


def setLogger():
    """This function called setLogger creates a logger and returns it to a file error.log.

                Returns:
                    Returns any errors to the error.log file.

        """
    logging.basicConfig(filename='error.log', level=logging.ERROR)
    return logging.getLogger('assignment2')


def processData(data, logger):
    """Takes the contents of a file as the file, processes it line by line, returning
    it to a dictionary.  The dictionary maps a Person's ID to a tuple(name, birthday).
    Also converts birthday from a string to the correct format.

            Args:
                data which is all of the processed data from the processData function
                logger which logs the errors from incorrectly formatted data

            Returns:
                Returns a dictionary where the keys are id, name, birthday

    """
    splitter = data.split('\n')
    keys = splitter.pop(0).split(',')
    reader_list = csv.DictReader(splitter, fieldnames=keys)
    birthdays = [x for x in reader_list]
    result = {}

    counter = 0
    for person in birthdays:
        try:
            result[person['id']] = (person['name'], datetime.strptime(person['birthday'], '%d/%m/%Y'))
        except:
            logger.error('Error processing line #{} for ID #{}'.format(counter, person['id']))
        counter += 1
    return result


def displayPerson(personID, data):
    """This function called displayPerson prints out formatted information for the
        id entered by the user.

                Args:
                    personID holds all the possible ID's that could return a birthday
                    data which is all of the processed data from the processData function

                Returns:
                    Returns one of two possible messages

        """
    try:
        print('{}, {}'.format(data[personID][0], data[personID][1].strftime('%Y-%m-%d')))
    except:
        print('No user found with that id')


if __name__ == '__main__':
    # https://s3.amazonaws.com/cuny-is211-spring2015/birthdays100.csv
    # setting up argparse
    parser = argparse.ArgumentParser(description='Birthday')
    parser.add_argument('--url', help='URL that represents Birthdays for user id', required=True)
    args = vars(parser.parse_args())

    # download data
    data = downloadData(args['url'])

    # set up logger
    assignment2 = setLogger()

    # process data
    result = processData(data, assignment2)

    # give me a number and get a birthday
    personID = raw_input('Please enter a number.')

    while int(personID) > 0:
        displayPerson(personID, result)
        personID = raw_input('Please enter a number.')
