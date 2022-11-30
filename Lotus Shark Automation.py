import random    # To Generate Random Coordinates.
import time      # To Delay the Program.
import pyautogui # To perform Clicking.	
import shutil 	 # To Manipulate Files.
import openpyxl  # To Manipulate csv files.	
import os        # To Manipulate Files

# Delaying the program so that User can open required
# tab when the preogram is started.
delay=time.sleep(1)
i=0
time.sleep(2)

#Initiating a Loop for the multiple iterations.
while(i<100):
    # Assgning random values to Hardpoints
    xi1=random.randint(564,568)
    yi1=254#random.randint(251,256)
    zi1=random.randint(185,189)
    xo1=random.randint(553,557)
    yo1=random.randint(482,486)
    zo1=random.randint(171,175)
    xi2=random.randint(100,999)
    yi2=random.randint(100,999)
    zi2=random.randint(100,999)
    xo2=random.randint(100,999)
    yo2=random.randint(100,999)
    zo2=random.randint(100,999)
    xi=xi1+(xi2*0.001)
    yi=yi1#+(yi2*0.001)
    zi=zi1+(zi2*0.001)
    xo=xo1+(xo2*0.001)
    yo=yo1+(yo2*0.001)
    zo=zo1+(zo2*0.001)
    xi=str(xi)
    yi=str(yi)
    zi=str(zi)
    xo=str(xo)
    yo=str(yo)
    zo=str(zo)
    
    # Clicking the Appropriate Buttons
    pyautogui.click(181,220)
    pyautogui.click(502,395)

    #Input the coordinates
    pyautogui.typewrite(xo)
    pyautogui.click(650,395)
    pyautogui.typewrite(yo)
    pyautogui.click(800,395)
    pyautogui.typewrite(zo)
    pyautogui.click(502,412)
    pyautogui.typewrite(xi)
    pyautogui.click(650,412)
    pyautogui.typewrite(yi)
    pyautogui.click(800,412)
    pyautogui.typewrite(zi)
    pyautogui.click(200,510)

    # Delaying to avoid any error.
    time.sleep(1)

    # Start the Simulation.
    pyautogui.click(170,396)

    # Opening the Excel
    pyautogui.click(62,498)
    pyautogui.click(62,595)
  
    # Delaying to avoid any error.
    time.sleep(1.5)

    # Saving the Excel File to default location.
    pyautogui.press('f12')
    #pyautogui.moveTo(38,480)
    pyautogui.typewrite('sdf.xlsx')
    pyautogui.click(200,661)
    pyautogui.click(200,74)
    pyautogui.press('enter')
    pyautogui.hotkey('alt','f4')
    time.sleep(0.5)

    # Move the file.
    shutil.move(r'C:\Users\HP\AppData\Local\Temp\sdf.xlsx',r'C:\Users\HP')
    time.sleep(1)
    
    # Open the moved Excel File in Python Environment.
    wb=openpyxl.load_workbook(r'C:\Users\HP\AppData\Local\Temp\sdf.xlsx')
    sheet=wb.active

    # Import the value from file to Python Environment.
    at=float(sheet['C157'].value)
    rt=float(sheet['A584'].value)
    ain=float(sheet['B584'].value)
    aout=float(sheet['C584'].value)
    ack=float(sheet['F584'].value)
    tr=float(sheet['G584'].value)
    
    # Remove the default location file.
    os.remove('sdf.xlsx')

    # Apply the filters to print the desired values.
    if(ack>50):
    	if((at<0.5)&(ain>35)):
        	print('\n',xi,yi,zi,xo,yo,zo)
                print(at,aout,ain,ack,tr,rt)

    # Exit the Excel.
    pyautogui.tripleClick(845,500)
    pyautogui.hotkey('alt','f4')
    time.sleep(0.1)
    i+=1