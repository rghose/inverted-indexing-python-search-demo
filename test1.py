from count_schools import CountSchools, Constants

count_schools = CountSchools("school_data.csv",
                             indexes=[Constants.STATE_INDEX, Constants.METRO_INDEX, Constants.CITY_INDEX])
count_schools.print_counts()
