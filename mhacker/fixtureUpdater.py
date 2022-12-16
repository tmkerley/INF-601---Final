"""
This program should call API-ninjas to build an exercise model.
It should write a FIXTURES file to init a database with exercises
and muscles.

API fields are name, type, muscle, equipment, difficulty,instructions
"""
import requests, json
from pathlib import Path
from os import stat

# file name and path are distinct variables for customization
FILENAME = "fixtures.JSON"
FILEPATH = Path.cwd() / "workouts/fixtures/"
# Constant for muscles from API-Ninja's acceptable list
MUSCLES = {
    'abdominals',
    'abductors',
    'adductors',
    'biceps',
    'calves',
    'chest',
    'forearms',
    'glutes',
    'hamstrings',
    'lats',
    'lower_back',
    'middle_back',
    'neck',
    'quadriceps',
    'traps',
    'triceps',
}

# function to open fixture file
def loadFixtureFile():
    # sets the file path
    file = FILEPATH / Path(FILENAME)

    # if file exists load file, else create it
    if file.is_file():
        print("Fixture file found at " + str(file)
        + ".\n  Loading existing data...")
        activefile = open(file, "r")
        # checks if file is empty and reads existing JSON, and converts it to a python object
        if stat(file).st_size != 0:
            data = json.loads(activefile.read())
        else:
            data = []

        activefile.close()

    else:
        print("Fixture file not found at: " + str(file))
        print("Creating file...")
        activefile = open(file, "x")
        if file.is_file():
            print("File created.")
            data = []
        else:
            print("File creation error")
            return

    return data

# writes given data to fixture file
def writeToFxitureFile(data):
    file = FILEPATH / Path(FILENAME)

    # file writing 
    activefile = open(file, "w")
    activefile.write(data)
    activefile.close()
    print("Data written.")
    return

def apiTypeFormatChange (apiList):
    for entry in apiList:
        if 'type' in entry:
            # assign type to temp
            tempTypeValue = entry["type"]
            # delete dictionary type entry
            entry.pop("type")
            # add dictionary aType entry with temp
            entry['aType'] = tempTypeValue
    
    print("Types Updated...")
    return apiList

# loads fixture data as a python object
fixtureContent = loadFixtureFile()

existingExerciseCount = len(fixtureContent)
print(str(existingExerciseCount) + " exercises exist.")

# Loops for all muscles, API-Ninja only returns 10 entries
for muscle in MUSCLES:
    # request current muscle
    api_url = 'https://api.api-ninjas.com/v1/exercises?muscle={}'.format(muscle)
    response = requests.get(api_url, headers={'X-Api-Key': 'XAnRBGt717T92RQT6/9rig==UD2M9TYjxtSswYLY'})

    # if to check if request was succesful.
    if response.status_code == requests.codes.ok:
        print(muscle + " request successful...")
        newList = json.loads(response.text)
    else:
        print("Error:", response.status_code, response.text)
        break

    # walks through the response
    for i in newList:
        newExercise = True

        # empty records check
        if len(fixtureContent) != 0:
            # looks for new exercise
            for j in fixtureContent:
                if j == i:
                    newExercise = False
                    print(j['name'], " does not match ", i['name'])
                    break
        else:
            newExercise = True
        
        # checks and adds new exercise
        if newExercise:
            i['id'] = existingExerciseCount + 1
            existingExerciseCount += 1
            fixtureContent.append(i)
            print("Writing new exercise: " + i['name'])

print(str(len(fixtureContent)) + " is the new total.")
apiTypeFormatChange(fixtureContent)
print("Data written, closing file...")

# converts python Object to JSON, saves, and closes it
writeToFxitureFile(json.dumps(fixtureContent))