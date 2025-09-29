import pandas as pd

op = "https://www.openpowerlifting.org/"

'''
Format:
Lifter: website + "u/" + lifter
Lifter stats: website + "api/liftercsv/" + lifter
'''


def liftingcast_read(comp: csv):
    '''
        Pulls competition from Liftingcast as a CSV file. More relevant data may be pulled in the future
        to build a prediction model.

        comp
         CSV file containing the information of an existing OR upcoming powerlifting meet. Retrieves all relevant data
    '''

    compDF = pd.read_csv(comp)
    compDF = compDF[["Name", "Gender", "Team", "Lot", "Session", "Flight", "Awards Division", "Body Weight (kg)", "Weight Class"]]

    

def lifter_read(lifter: str):
    '''
        Searches for the lifter on OpenPowerlifting. Two outcomes: (1) The lifter exists on the OpenPowerlifting
        database (2) First time lifter, in which case they will be assigned a "WILDCARD" status.
        
        lifter
         Name of lifter to be searched. Lowercase first and last name, no spaces.
    '''

    lifter = lifter.replace(" ", "").lower()
    lifter_stats = op + "api/liftercsv/" + lifter   #URL for lifter's CSV
    try:
        lifterDF = pd.read_csv(lifter_stats)    #locate lifter on OpenPowerlifting
    except:
        pass    #Requires implementation

    finally:
        lifterDF = lifterDF[["Best3SquatKg", "Best3BenchKg", "Best3DeadliftKg", "TotalKg"]]
        print(lifterDF)

if __name__ == "__main__":
    lifter_read("aidanlaceda")
    
