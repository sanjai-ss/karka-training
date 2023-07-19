education_details=[{"study":"B.tech",
                    "institute":"cape",
                    "semester_marks":[{"semester":1,
                                       "subjects":["computer programming","maths","data science"],
                                       "grade":"A"},
                                       {"semester":2,
                                       "subjects":["computer programming","maths","machine learning"],
                                       "grade":"B"}]},
                    {"study":"M.tech",
                    "institute":"cape",
                    "semester_marks":[{"semester":1,
                                       "subjects":["computer programming","maths","deep learning"],
                                       "grade":"C"},
                                       {"semester":2,
                                       "subjects":["computer programming","maths"," advanced AI"],
                                       "grade":"A"}]}]

for details in education_details:
    marks=details["semester_marks"]
    # for mark in marks:
    print(marks[0])