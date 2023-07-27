passed_out_year = input("which year you passed out from college")
print(passed_out_year)

passed_out_year=int(passed_out_year)
type_of_passed_out_year=type(passed_out_year)
print(type_of_passed_out_year)

is_eligible=passed_out_year>=2021 and passed_out_year<=2023
if is_eligible:
        print("this student is eligible")
else:
        print("this student is not eligible")
