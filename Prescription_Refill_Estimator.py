# Cory Cusick

while True:
    import datetime

    print("\n\t\tThis app counts the number of days left until a prescription needs to be refilled")
    print("\n\t\tThis app helps determine refill dates for prescriptions")

    prescriptionName = {}
    prescriptionQuanity = {}
    dailyQuanity = {}

    dueDate = (datetime.date.today() + datetime.timedelta(days=30)).isoformat()
    dueDateNinety = (datetime.date.today() + datetime.timedelta(days=90)).isoformat()

    prescriptionName = str(input("\n\t\t\tWhat is the name of the prescription?: "))

    prescriptionQuanity = int(input("\n\t\t\tWhat is the quanity of pills prescribed?: "))

    dailyQuanity = int(input(f"\n\t\t\tHow many pills of {prescriptionName} a day?: "))

    if (prescriptionQuanity == 30):
        print(f"\n\t\tFor a 30 day supply taken daily, the refill for {prescriptionName} will be due: " + str(dueDate))
    elif (prescriptionQuanity == 90):
        print(f"\n\t\tFor a 90 day supply taken daily, the refill for {prescriptionName} will be due: " + str(dueDateNinety))

    Restart = input("\n\n\t\tWould you like to restart and enter more information? Enter y for yes or n for no: ")

    if Restart not in ('y' or 'Y'):
        print("\n\t\tThank you for your time")
        break

    if Restart == "y" or "Y":
        continue
