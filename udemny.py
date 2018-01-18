# Udemy - Web Course Breakdown

# import modules 
import os
import csv

file_path = os.path.join('resources', 'WebDevelopment2.csv')

# Create a Python application that reads the data on Udemy Web Development offerings. 

# Empty lists 

title = []
price = []
subscriber_count = []
number_of_reviews = []
course_lenght = []

# open the file 
# with open(file_path, newline='', encoding='utf-8') as csv_file:

with open(file_path, newline='', encoding='utf-8') as csv_file:

    # read file 
    read_csv = csv.reader(csv_file, delimiter =",")


# Then store the contents of the Title, Price, Subscriber Count, Number of Reviews, and Course Length into Python Lists.
    for row in read_csv:
                
        title.append(row[1])
        # print(title)

        price.append(row[4])
       # print(price)

        subscriber_count.append(row[5])
       # print(subscriber_count)

        number_of_reviews.append(row[6])
       # print(number_of_reviews)

        course_lenght.append(row[7])
       # print(course_lenght)
    
# Then zip these lists together into a single tuple.

web_course = zip(title, price, subscriber_count, number_of_reviews, course_lenght)


# Finally, write the contents of your extracted data into a CSV. Make sure to include the titles of these columns in your csv.

output_file = os.path.join('resources', 'udemny.csv')

with open(output_file, 'w', newline="") as datafile:
    csv_writer = csv.writer(datafile, delimiter = ",")

    csv_writer.writerow(["Title", 'Price', 'Subscriber Count', 'Number of Reviews', 'Course Lenght'])
    csv_writer.writerow(web_course)