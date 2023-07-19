# list of data

data=[{"name":"sanjai",
       "sslc":{"tamil":67,
               "english":75,
               "maths":50,
               "science":68,
               "social":63}},
       {"name":"shalu",
       "sslc":{"tamil":92,
               "english":90,
               "maths":100,
               "science":97,
               "social":96}},
       {"name":"rocky",
       "sslc":{"tamil":76,
               "english":73,
               "maths":74,
               "science":60,
               "social":81}},
       {"name":"priya",
       "sslc":{"tamil":90,
               "english":86,
               "maths":98,
               "science":84,
               "social":92}},
       {"name":"sara",
       "sslc":{"tamil":82,
               "english":95,
               "maths":99,
               "science":84,
               "social":93},}]
# total of marks
a=0
for i in data:
    sslc=i["sslc"]
    name=i["name"]
    total=sslc["tamil"]+ sslc["english"]+ sslc["maths"]+sslc["science"]+sslc["social"]   
    percentage=(total/500)*100  
    print(f"the total of {name} is = {percentage}")
    if percentage>90:
        print ("eligible for maths bio")
    elif percentage>80:
        print("eligible for computer science")
    elif percentage>75 and sslc["maths"] >98:
        print("eligible for maths bio")
    elif percentage>70 and sslc["maths"] >98:
        print("eligible for computer science")
    else:
        print("not eligible")


       
       




        