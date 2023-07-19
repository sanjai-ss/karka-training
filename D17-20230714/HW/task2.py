# cricket player statistics
# cricket player details

player_details=[{"name":"yuvraj singh",
                 "country":"india",
                 "century":17,
                 "half century":71,
                 "wickets":148,
                 "hat trick wickets":8,
                 "top batting score":[169,145,139,87,96]},
                 {"name":"michael hussey",
                 "country":"australia",
                 "century":22,
                 "half century":72,
                 "wickets":9,
                 "hat trick wickets":0,
                 "top batting score":[195,134,181,95,112]},
                 {"name":"sir alastair cook",
                 "country":"england",
                 "century":38,
                 "half century":76,
                 "wickets":1,
                 "hat trick wickets":0,
                 "top batting score":[294,142,215,182,173]},
                 {"name":"mahela jayawardene ",
                 "country":"sri lanka",
                 "century":54,
                 "half century":136,
                 "wickets":14,
                 "hat trick wickets":0,
                 "top batting score":[374,257,261,193,136]},
                 {"name":"graeme smith",
                 "country":"south africa",
                 "century":37,
                 "half century":90,
                 "wickets":26,
                 "hat trick wickets":6,
                 "top batting score":[277,169,242,155,139]}]
def cricket():
    content=0
    for i in player_details:
        if i["century"]>10:
            content=content+1

        if i["hat trick wickets"]>5:
            name=i["name"]
        b=0
        for a in i["top batting score"]:
            if a>b:
                b=a
        print(b)
    score=(f"the number of players who have scored more than 10 centuries from the list is {content}")
    print(score)
    print(name)
cricket()

