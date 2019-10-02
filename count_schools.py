import csv


class Constants:
    NAME_INDEX = 3
    CITY_INDEX = 4
    STATE_INDEX = 5
    METRO_INDEX = 8


class School:
    def __init__(self, nces_id: int, agency_id: int, op_agency: str, name: str, city: str, state: str, lat: float,
                 lng: float, metro: str, urban: str, status: int):
        self.nces_id = nces_id
        self.agency_id = agency_id
        self.op_agency = op_agency
        self.name = name
        self.city = city
        self.state = state
        self.lat = lat
        self.lng = lng
        self.metro_locale = metro
        self.urban_locale = urban
        self.status = status


class SchoolData:
    """
    CSV row in the format:
    NCESSCH,LEAID,LEANM05,SCHNAM05,LCITY05,LSTATE05,LATCOD,LONCOD,MLOCALE,ULOCALE,status05
    """
    def __init__(self, file_name, indexes=[]):
        self.schools = []
        self.total_schools = 0
        self.states = {}
        self.metro_locale = {}
        self.cities = {}
        self.indexes = {}

        for index in indexes:
            self.indexes[index] = {}

        with open(file_name, 'r', encoding="latin-1") as csv_file:
            csv_reader = csv.reader(csv_file, delimiter=',')
            line_count = 0
            for row in csv_reader:
                if line_count == 0:
                    line_count += 1
                    continue

                # create indexes for items that need to be queried
                # these are maps for columns that need to be queried and
                # are known before-hand.
                for index in indexes:
                    current_index = self.indexes[index]
                    data = row[index]
                    if data not in current_index:
                        current_index[data] = 1
                    else:
                        current_index[data] += 1

                self.total_schools += 1
                self.schools.append(row)


class CountSchools(SchoolData):
    def get_city_with_most_schools(self):
        cities_dict = self.indexes[Constants.CITY_INDEX]
        city = max(cities_dict, key=cities_dict.get)
        tup = (city, cities_dict[city])
        return tup

    def print_counts(self):
        print("Total Schools: %d" % self.total_schools)
        print("Schools by State:")
        print(self.indexes[Constants.STATE_INDEX])
        print("Schools by Metro-centric locale:")
        print(self.indexes[Constants.METRO_INDEX])
        city, count = self.get_city_with_most_schools()
        verb = "school"
        if count > 1:
            verb = "schools"
        print("City with most schools: %s (%d %s)" % (city, count, verb))
        print("Unique cities with at least one school: %d" % len(self.indexes[Constants.CITY_INDEX]))

