import subprocess
import pyautogui
import time
import os

ssms_path = r"C:\Program Files (x86)\Microsoft SQL Server Management Studio 20\Common7\IDE\Ssms.exe"
video_path = r"C:\Users\Administrator\Videos\Bhooth.Bangla.2026.1080p.Hindi.DS4K.WEB-DL.5.1.ESub.x264-HDHub4u.Ms.mkv"

query = """
USE AdventureWorksLT2022;

SELECT CompanyName,
       COUNT(*) AS TotalCustomers
FROM SalesLT.Customer
WHERE CustomerID IN (1,2,3,4,5,6,8,9)
GROUP BY CompanyName;
"""

while True:
    # Open SSMS
    subprocess.Popen(ssms_path)
    time.sleep(15)

    # Connect
    pyautogui.press("enter")
    time.sleep(10)

    # New Query
    pyautogui.hotkey("ctrl", "n")
    time.sleep(3)

    # Type SQL
    pyautogui.write(query, interval=0.02)

    # Execute
    pyautogui.press("f5")
    time.sleep(5)
   
    

    # Close SSMS
    pyautogui.hotkey("alt", "f4")
    time.sleep(2)

    # Don't Save
    pyautogui.press("n")
    time.sleep(2)

    # Open video
    os.startfile(video_path)

    # Play for 5 minutes
    time.sleep(30)

    # Close video player (change process name if needed)
    subprocess.run(["taskkill", "/F", "/IM", "Video.UI.exe"], shell=True)