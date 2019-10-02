from school_search import SchoolDataSearch
import time


school_search = SchoolDataSearch("school_data.csv", "state_mapping.csv")
school_search.generate_reverse_index()

school_search.search_schools("elementary school highland park")
school_search.search_schools("jefferson belleville")
school_search.search_schools("riverside school 44")
school_search.search_schools("granada charter school")
school_search.search_schools("foley high alabama")
school_search.search_schools("KUSKOKWIM")
