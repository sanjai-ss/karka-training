# def calculate_electricity_bill():
consumer_data = {"consumer_name=": "user",
    "eb_reading": [1100, 1200, 1350, 1650, 2050]} 
List=[]
amount=0  
for i in range(len(consumer_data["eb_reading"])-1):
    unit_consumption=consumer_data["eb_reading"][i+1]-consumer_data["eb_reading"][i]
    if unit_consumption<100:
        print("no bill")
    elif unit_consumption>=100 and unit_consumption<=199:
        amount=unit_consumption*2
        # print(f"month={i+1}\nunits_consumed :{unit_consumption}\nbill_amount :{unit_consumption*2}\n")
        # amount=amount+unit_consumption*2
    elif unit_consumption>=200 and unit_consumption<=499:
        amount=unit_consumption*5
        # print(f"month={i+1}\nunits_consumed :{unit_consumption}\nbill_amount :{unit_consumption*5}\n")
        # amount=amount+unit_consumption*5
    elif unit_consumption>=500 and unit_consumption<=999:
        amount=unit_consumption*10
        # print(f"month={i+1}\nunits_consumed :{unit_consumption}\nbill_amount :{unit_consumption*10}\n")
        # amount=amount+unit_consumption*10
    elif unit_consumption>=1000:
        amount=unit_consumption*14
        # print(f"month={i+1}\nunits_consumed :{unit_consumption}\nbill_amount :{unit_consumption*14}\n")
        # amount=amount+unit_consumption*14

    dictionary_view={"month": i+1,
    "units_consumed": unit_consumption,
    "billAmount": amount}   
    List.append(dictionary_view)
# print(List)
# print("total_amount=",amount)

file=open("/home/sanjai/Documents/sanjai.txt","w")
# file.write("i'm sanjai and i'm from tamilnadu")
for item in List:
    for items in item:
        # file.write(item)
        print(items)
    # print(file.read())
# file.close()


    






        

    
