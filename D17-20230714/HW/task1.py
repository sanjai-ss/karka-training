# personal detail management
def detail():
        data=[{"name":"sanjai",
           "place":"nagercoil",
           "age":20},
           {"name":"barathi",
            "place":"thovalai",
            "age":20},
           {"name":"akshaya",
            "place":"theroor",
            "age":21},
           {"name":"alfreena",
            "place":"south thamaraikulam",
             "age":20},
           {"name":"sharmila",
            "place":"monday market",
            "age":22},
           {"name":"shivaraj",
            "place":"vadasery",
            "age":21}]
        for i in data:
                name=i["name"]
                age=i["age"]
                place=i["place"]

        if age>20:
                print(f"i'm {name} from {place}")
                print(f"i am {name}, i'm {age} years old. and i am from {place}.")

        
detail()
