from datetime import datetime



fmlyMmbrs = {"Mother": "1234567890", "Brother": "5678901234", "Father": "2345678901", "Sister": "3547896102", "Grandfather": "3456789012"}


def shwFmly():
    print("\nSaved Family Members")
 
    if len(fmlyMmbrs) == 0:
        print("No contacts found")
    else:
        for nm, nmbr in fmlyMmbrs.items():
            print(f"- {nm}: {nmbr}")
    print() 



def sndNtfctn():
    print("\nSelect Notification Type:")
    print("1. Emergency Alert")
    print("2. Share Current Location")
    print("3. Health Update")
    print("4. Custom Message")

    chc = input("Enter choice: ").strip() 

    if chc == "1":
        msg = "Emergency alert: I need help"
    elif chc == "2":
        lctn = "VIT Bhopal Hostel"  
        msg = f"My location: {lctn}"
    elif chc == "3":
        msg = "Health update: I am not feeling well, please try to stay in touch."
    elif chc == "4":
        msg = input("Enter custom message: ")
        if not msg:  
            print("Message empty..")
            return
    else:
        print("\nInvalid choice")
        return 


    sndr = input("\nEnter your name: ")
    if not sndr:  
        sndr = "Unknown"
    

    lrtTm = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    print("\nSending notification to all family members...\n")



    cnt = 0 
    for nm, nmbr in fmlyMmbrs.items():
        print(f"Notification sent to {nm} ({nmbr})")
        cnt += 1 



    print("\nNOTIFICATION DETAILS")
    print(f"Sender     : {sndr}")
    print(f"Timestamp  : {lrtTm}")
    print(f"Message    : {msg}\n")


def ddFmlyMmbr():
    nm = input("Enter family member name: ").strip()
    nmbr = input("Enter contact number: ").strip()
    

    if nm and nmbr: 
        if nm in fmlyMmbrs:  
            print(f"\n{nm} already exists. Overwriting...\n")
        fmlyMmbrs[nm] = nmbr
        print(f"\n{nm} added to family contacts.\n")
    else:
        print("\nError: Name or number missing\n")  # edge case handling


def mn():
    rnng = True  
    while rnng:
        print("\n" + "="*50)
        print("    EMERGENCY CONTACT ALERT SYSTEM")
        print("="*50)
        print("1. View Family Members")
        print("2. Send Notification")
        print("3. Add Family Member")
        print("4. Exit")
        print("="*50)
        
        try:
            chc = input("\nEnter your choice (1-4): ").strip()
        except KeyboardInterrupt:  # handle Ctrl+C
            print("\n\nExiting...")
            rnng = False
            continue
        
        
        if chc == "1":
            shwFmly()
        elif chc == "2":
            sndNtfctn()
        elif chc == "3":
            ddFmlyMmbr()
        elif chc == "4":
            print("\nThank you for using Emergency Contact Alert System!")
            print("Stay safe!\n")
            rnng = False  
        else:
            print("\nInvalid choice! Please enter a number between 1-4.\n")
            

if __name__ == "__main__":
    mn()
    
