import pandas as pd

data = pd.read_csv("TeamsList.csv")
TableNames = ["CurrentProgram", "ContactEmail", "Team", "MissingTasks", "MondayBoardLink"]

all_programs = data["CurrentProgram"]
all_ContactEmail = data["ContactEmail"]
all_Team = data["Team"]
all_MissingTasks = data["MissingTasks"]
all_MondayLink = data["MondayBoardLink"]




def create_email(x):
    # name, incompleted, track, boardlink
    str_form = (
        "{} \n\n\nHi {}!\n\nHope your team has been well through this uncertain quarter. \n\nNoticed there is some inactivity in your Monday board. Your {} are not yet all finished. As the team lead for your team, you are responsible for ensuring the {} program requirements are completed and tracked accordingly in monday.com by the end of this quarter. \n\nHere is a quick link to your board! {} \n\nFriendly reminder that you need to complete all the tasks in Monday.com by the end of the quarter. If not, you need to notify Jacques (CC'ed) via email. You can also schedule an appointment with him at https://basementmentorhours.as.me/JacquesChirazi. \n\nBest of luck as we reach the end of week 10 and into finals week :)\n\n Warm regards,\n Madeline Tjoa \n Marketing and Communications Intern @ The Basement"
    )
    return str_form.format(
        x["ContactEmail"], x["Team"], x["MissingTasks"], x["CurrentProgram"], x["MondayBoardLink"]
    )
def startup_tree_email(x):
    str_form = (
        "{}{}{}{}{}{}"
    )
    return str_form.format(
        x["ContactEmail"], x["Team"], x["MissingTasks"], x["CurrentProgram"], x["MondayBoardLink"]
    )
data['customized_script'] = data.apply(create_email, axis=1)
print(data.head())

f= open("emails.txt","w+")

for i in data['customized_script']:
     f.write(i)
     f.write("\n \n \n \n \n ")

f.close()