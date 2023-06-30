travel_log=[{'country':'France','visits':12,'cities':['Lille','Paris','Dijon']},
            {'country':'India','visits':5,'cities':['Rishikesh','Bengaluru','Varanasi']}]
ask='y'
while ask=='y':
    def add_new_country(coun,vis,city):
        new={}
        new['country']=coun
        new['visits']=vis
        new['cities']=city
        travel_log.append(new)
        print(travel_log)    
    coun=input("Which country did you visit? ")
    vis=int(input("How many times? "))
    city=input("Cities visited seperated by a comma. ").split(',')

    add_new_country(coun,vis,city)

    ask=input("Do you wish to add more? y/n\n").lower()
        
