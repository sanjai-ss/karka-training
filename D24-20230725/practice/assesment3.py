# to find the making cost of jewellery
monthly_gold_rate=[{"month":"january",
                    "gold_rate":4500,
                    "jewell_list":[{"name":"chain",
                                    "making_cost":12},
                                    {"name":"ring",
                                    "making_cost":13}]},
                    {"month":"february",
                    "gold_rate":5000,
                    "jewell_list":[{"name":"chain",
                                    "making_cost":14},
                                    {"name":"ring",
                                    "making_cost":15}]},
                    {"month":"march",
                    "gold_rate":3500,
                    "jewell_list":[{"name":"chain",
                                    "making_cost":16},
                                    {"name":"ring",
                                    "making_cost":17}]},
                    {"month":"april",
                    "gold_rate":2000,
                    "jewell_list":[{"name":"chain",
                                    "making_cost":18},
                                    {"name":"ring",
                                    "making_cost":19}]}]
dic=[]
value={}
from pprint import pprint
for item in monthly_gold_rate:
    for i in item["jewell_list"]:
        month=item["month"]
        gold=item["gold_rate"]
        percentage=i["making_cost"]
        name=i["name"]
        jewell=((percentage*gold)/100)+gold
        rate=(f"month : {month}, the making cost of {name}  : {jewell}")
        dic.append(rate)
pprint(dic)