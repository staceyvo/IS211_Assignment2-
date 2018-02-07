

def downloadData():
    raise Exception('Not implemented')

def setLogger():
    raise Exception('Not implemented')

def processData():
    raise Exception('Not implemented')

def displayPerson():
    raise Exception('Not implemented')

if __name__=='__main__':
    #setting up argparse

    #download data
    downloadData()

    #set up logger
    setLogger()

    #process data
    processData()

    #give me a number and get a birthday
    personID = int(raw_input('Please enter a number.'))

    while personID > 0:
        displayPerson(personID)
        personID = int(raw_input('Please enter a number.'))