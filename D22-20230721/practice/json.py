# calculate_electricity_bill():
name="sanjai"
reading=[1000,1200,1450,1750,2000]
consumer_data = {"consumer_name=": name,
    "eb_reading": reading} 
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
        # amount=amount+unit_consumption*10
    elif unit_consumption>=1000:
        amount=unit_consumption*14
        # print(f"month={i+1}\nunits_consumed :{unit_consumption}\nbill_amount :{unit_consumption*14}\n")
        # amount=amount+unit_consumption*14

    dictionary_view={"month": i+1,
    "units_consumed": unit_consumption,
    "billAmount": amount}   
    List.append(dictionary_view)
    