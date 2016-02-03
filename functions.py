import sys

def showEnvironment(environment):
    contentTable = environment.getContentTable()
    for i in contentTable:
        for j in i:
            sys.stdout.write(j.getName() + ' - ')
        print ''