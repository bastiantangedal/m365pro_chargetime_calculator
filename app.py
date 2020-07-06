import sys
from datetime import timedelta
import time

BATTERY_CAPACITY = 12800 # in mAh
CHARGE_CURRENT = 1700 # in mAh
CHARGE_EFFICIENCY = 1.1 # 90% 

def printUsage(text, color):
  print(f"{color}{text}")

def main():
  try:
    # Args
    currentPercentage = int(sys.argv[1])
    desiredPercentage = int(sys.argv[2])

    printUsage("Tool created by: Bastian Pedersen.", "\u001b[33;1m")
    printUsage("NB: This tool is not 100% accurate. Factors such as temperature affect charging speed.", "\u001b[31;1m")
    time.sleep(1.5)

    currentPercentageInMah = int((BATTERY_CAPACITY / 100) * currentPercentage)
    remainingMah = BATTERY_CAPACITY - currentPercentageInMah

    # Calculate charge time
    chargeTimeInMinutes = int(round((remainingMah / CHARGE_CURRENT) * CHARGE_EFFICIENCY, 1) * 60)
    chargeTimeInTimeFormat = str(timedelta(minutes=chargeTimeInMinutes))[:-3]
    chargeTimeHours = chargeTimeInTimeFormat.split(":")

    # Print out result
    printUsage(f"\nBattery currently has: {currentPercentage}% \nYou want: {desiredPercentage}%", "\u001b[37m")
    printUsage(f"""\nThis will approximately take: {chargeTimeHours[0]} hour(s) and {chargeTimeHours[1]} minutes, with a charge efficiency of {(int(0.9*100))}%.""", "\u001b[37m")
    
  except Exception:
    raise ValueError("usage: (currentPercentage) (desiredPercentage) // example: 30 70") from None

main()


  
