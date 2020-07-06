import sys
from datetime import timedelta
import time

BATTERY_CAPACITY = 12800 # in mAh
CHARGE_CURRENT = 1700 # in mAh
CHARGE_EFFICIENCY = 1.1 # 90% 

def printUsage(text, color):
  """ Simple print function with color """
  print(f"{color}{text}")

def main():
  currentPercentage = 0
  desiredPercentage = 0

  try:
    # Get and process args
    currentPercentage = int(sys.argv[1])
    desiredPercentage = int(sys.argv[2])
  except Exception:
    raise ValueError("usage: (\u001b[31;1mcurrentPercentage\u001b[37m)\u001b[37m (\u001b[31;1mdesiredPercentage\u001b[37m)\u001b[37m \u001b[32;1mor \u001b[37m(\u001b[31;1mcurrentmAh\u001b[37m)\u001b[37m (\u001b[31;1mdesiredPercentage\u001b[37m)")

  mAhMode = False

  if currentPercentage > 100:
      mAhMode = True

  if mAhMode == False:
      currentPercentageInMah = int((BATTERY_CAPACITY / 100) * currentPercentage)
  else:
      currentPercentageInMah = currentPercentage

  desiredPercentageInMah = int((BATTERY_CAPACITY / 100) * desiredPercentage)
  if desiredPercentageInMah < currentPercentageInMah:
     raise ValueError("\u001b[31;1mCurrent percentage or mAh higher than desired percentage! Invalid arguments!")
    
  printUsage("Tool created by: Bastian Pedersen.", "\u001b[33;1m")
  printUsage("NB: This tool is not 100% accurate. Factors such as temperature affect charging speed.", "\u001b[31;1m")
  time.sleep(1.5)

  mahNeeded = desiredPercentageInMah - currentPercentageInMah

  # Calculate charge time
  chargeTimeInMinutes = (mahNeeded / CHARGE_CURRENT * 1.1) * 60

  chargeTimeInTimeFormat = str(timedelta(minutes=chargeTimeInMinutes))[:-3]

  chargeTimeHours = chargeTimeInTimeFormat.split(":")
  if chargeTimeHours[1] == "00":
    chargeTimeHours[1] = "0"

  # Print out result
  if mAhMode == False:
    printUsage(f"\nBattery currently has: {currentPercentage}% \nYou want: {desiredPercentage}%", "\u001b[37m")
  else:
    printUsage(f"\nBattery currently has: {int((currentPercentage / BATTERY_CAPACITY) * 100)}% \nYou want: {desiredPercentage}%", "\u001b[37m")

  printUsage(f"""\nThis will approximately take: {chargeTimeHours[0]} hour(s) and {chargeTimeHours[1]} minutes, with a charge efficiency of {(int(0.9*100))}%.""", "\u001b[37m")  

 
main()


  
