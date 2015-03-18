import csv

class FlightSchedule:

  def __init__(self, flights = None, plane_identifiers = None):
      self.flights = flights
      self.plane_identifiers = plane_identifiers

  def read_data_from_file(self):
    file = open('flight_data.csv')
    reader = csv.reader(file)
  
    members = []
    identifiers = []

    #read data for all rows
    for row in reader:
      members.append(row[0])

    #find unique identifiers
      if row[1] not in identifiers:
        identifiers.append(row[1])

    self.flights = members
    self.plane_identifiers = identifiers

    #print(members)#prints all 241 flights
    #print(identifiers)#prints all 101 unique identifiers

    return FlightSchedule(members, identifiers)

    file.close()

  #function identifies longest flight in file
  def determine_longest_flight(self):
    file = open('flight_data.csv')
    reader = csv.reader(file)
  
    member_list = []

    longest = 0

    for row in reader:
      if float(row[4]) > longest:
        longest = float(row[4])
        number = row[0]

    return number

    file.close()
