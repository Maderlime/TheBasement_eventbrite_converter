import pandas as pd
def create_csv(zoom_link, eventbrite_link):
    myname = eventbrite_link + "finished.csv"
    zoom_df = pd.read_excel(zoom_link).rename({"First Name": "FirstName"}, axis = 1)
    eventbrite_csv = pd.read_csv(eventbrite_link).rename({"First Name": "FirstName"}, axis = 1)
    eventbrite_csv["attended"] = eventbrite_csv["Last Name"].isin(zoom_df["Last Name"])
    eventbrite_csv_final = eventbrite_csv.drop(['Order #', 'Order Date'], axis=1)
    eventbrite_csv_final.to_csv(myname,index=False)
    print(sum(eventbrite_csv_final["attended"] == True))

stuff = input("enter zoom_link(xlsx),eventbrite(csv)")
separated = stuff.split(",")
create_csv(separated[0], separated[1])