# resume
my_resume=[{"name":"sanjai S",
            "e-mail":"sanjaimass20@gmail.com",
            "mobile no":7695853511,
            "soft skills":["creativity","communication","problem solving"],
            "hardskills":["critical thinking","project management"],
            "educational qualification":[{"course":"sslc",
                                          "percentage":66,
                                          "institute name":"ED willmott memorial SDA hr sec school",
                                          "passed out year":"2017-2018"},
                                         {"course":"hsc",
                                          "percentage":56,
                                          "institute name":"ED willmott memorial SDA hr sec school",
                                          "passed out year":"2019-2020"},
                                         {"course":"BA english",
                                          "percentage":62,
                                          "institute name":"govt arts and science college,kanyakumari",
                                          "passed out year":"2020-2023"}],
            "projects":[{"project_name":"sarathywebservices.com",
                         "project_description":"i played a major role in building this website and i designes the layout of this website",
                         "duration in month":0.8},
                         {"name":"calculatormax",
                          "description":"i played the key role in building this mobile application and this project performs advanced mathematical operations",
                          "duration in month":1.5}],
            "experience":[{"organisation":"sarathywebservices",
                          "role":"web developer",
                          "duration in year":1},
                          {"organisation":"zoho",
                           "role":"android developer",
                           "duration in year":1.5},
                           {"organisation":"benishsoftwares",
                            "role":"ui/ux designer",
                            "duration":1}],
            "hobbies":["browsing","listening music","workout","sleeping"],
            "personal details":{"father's name":"sri ranga rajan J",
                                "father's occupation":"coolie",
                                "languages known":["tamil","english"],
                                "DOB":"14/12/2002",
                                "gender":"male",
                                "marital status":"single",
                                "address":{"door no":56,
                                           "street":"kesavathirupapuram",
                                           "city":"nagercoil",
                                           "district":"kanyakumari",
                                           "state":"tamilnadu",
                                           "pincode":629003}}}]
# for details in my_resume:
#     info=details["educational qualification"]
#     for i in info:
#         print(f"course:",i["course"],"\npercentage:",i["percentage"],"\ninstitute name:",i["institute name"],"\npassed out year:",i["passed out year"])
for details in my_resume:
    info=details["personal details"]
    for i in info:
        b=(info[i])
        news=(info["address"])
        
        print(i,f":",b)
          
       