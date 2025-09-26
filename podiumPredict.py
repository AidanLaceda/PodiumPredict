import pandas as pd

op = "https://www.openpowerlifting.org/"

'''
Format:
Lifter: website + "u/" + lifter
Lifter stats: website + "api/liftercsv/" + lifter
'''

#lifter = input("Enter lifter's name: ").replace(" ", "").lower()
temp = "adamduane"
lifter_stats = op + "api/liftercsv/" + temp



lifterDF = pd.read_csv(lifter_stats)
lifterDF = lifterDF[["Best3SquatKg", "Best3BenchKg", "Best3DeadliftKg", "TotalKg"]]
print(lifterDF)