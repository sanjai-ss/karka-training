# to find the lowest gold price
monthly_gold_rate=[{"month":"january",
                    "gold_rate":4500},
                    {"month":"february",
                    "gold_rate":5000},
                    {"month":"march",
                    "gold_rate":3500},
                    {"month":"april",
                    "gold_rate":2000}]

gold_rate=monthly_gold_rate[0]["gold_rate"]
value=0
for item in monthly_gold_rate:
    if item["gold_rate"]<gold_rate:
        gold_rate=item["gold_rate"]
        month1=item["month"]
    if item["gold_rate"]>value:
        value=item["gold_rate"]
        month2=item["month"]
print(f"{value} is the greatest price and its month is {month2}\n{gold_rate} is the lowest price and its month is {month1}")

# gold1=(monthly_gold_rate[0]["gold_rate"])
# gold2=(monthly_gold_rate[1]["gold_rate"])
# gold3=(monthly_gold_rate[2]["gold_rate"])
# month1=(monthly_gold_rate[0]["month"])
# month2=(monthly_gold_rate[1]["month"])
# month3=(monthly_gold_rate[2]["month"])
# if gold1<gold2:
#         if gold1<gold3:
#             print(f"{gold1}is the lowest price and its month is {month1}")
# if gold2<gold1:
#         if gold2<gold3:
#             print(f"{gold2}is the lowest price and its month is {month2}")
# if gold3<gold1:
#         if gold3<gold2:
#             print(f"{gold3}is the lowest price and its month is {month3}")