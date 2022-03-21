import csv
import time

student_data_csv = csv.DictReader(open("STUDENT_DATA.csv"))

tic = time.perf_counter()

for student in student_data_csv:
    print(student)

toc = time.perf_counter()
print(f"Time elapsed: {toc - tic} seconds")
