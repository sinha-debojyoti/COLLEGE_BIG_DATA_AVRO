import csv

import avro.schema
from avro.datafile import DataFileWriter
from avro.io import DatumWriter

schema = avro.schema.parse(open("STUDENT_DETAILS.avsc").read())

writer = DataFileWriter(open("STUDENT_DETAILS.avro", "wb"), DatumWriter(), schema)

student_data_csv = csv.DictReader(open("STUDENT_DATA.csv"))
for row in student_data_csv:
    print(row)
    writer.append(row)

writer.close()
