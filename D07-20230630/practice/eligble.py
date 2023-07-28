passed_out_year = int(input("which year you passed out from college"))
print(type(passed_out_year))

is_eligible=passed_out_year>=2021 and passed_out_year<=2023
if is_eligible:
        print("this student is eligible")
else:
        print("this student is not eligible")
