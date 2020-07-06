import sys
from datetime import timedelta

BATTERY_CAPACITY = 12800 # in mAh
CHARGE_CURRENT = 1700 # in mAh
CHARGE_EFFICIENCY = 1.1 # 90% 

def main():
  try:
    # Args
    currentPercentage = int(sys.argv[1])
    desiredPercentage = int(sys.argv[2])

    currentPercentageInMah = (BATTERY_CAPACITY / 100) * currentPercentage
    remainingMah = BATTERY_CAPACITY - currentPercentageInMah

    # Calculate charge time
    chargeTimeInMinutes = round((remainingMah / CHARGE_CURRENT) * CHARGE_EFFICIENCY, 1) * 60
    chargeTimeInTimeFormat = str(timedelta(minutes=chargeTimeInMinutes))[:-3]
    chargeTimeHours = chargeTimeInTimeFormat.split(":")

    # Print out result
    print(f"Battery currently has: {currentPercentage}% \nYou want: {desiredPercentage}%")
    print(f"""\nThis will approximately take: {chargeTimeInTimeFormat.split(':')[0]} hour(s) and {chargeTimeInTimeFormat.split(':')[1]} minutes, with a charge efficiency of {(int(0.9*100))}%.""")  
  except Exception:
    raise ValueError("usage: (currentPercentage) (desiredPercentage) // example: 30 70") from None

main()


  
