from avro.datafile import DataFileReader
from avro.io import DatumReader
import time

reader = DataFileReader(open("STUDENT_DETAILS.avro", "rb"), DatumReader())

tic = time.perf_counter()

for student in reader:
    print(student)

toc = time.perf_counter()
print(f"Time elapsed: {toc - tic} seconds")