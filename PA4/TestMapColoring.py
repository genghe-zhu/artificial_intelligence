# Genghe Zhu
# CS 76, PA4
# Fall 2022

from MapColoring import MapColoring
from CSP import backtracking_search

# simple example to make sure code runs
test = MapColoring(["WA", "NT", "SA"],
                      ["Red", "Blue", "Green"],
                      [("WA", "NT"),("WA", "SA"), ("NT","SA")])
result = backtracking_search(test)
print(result)

# simple test to make sure no solution should be given
test = MapColoring(["WA", "NT", "SA"],
                      ["Red", "Blue"],
                      [("WA", "NT"),("WA", "SA"), ("NT","SA")])
result = backtracking_search(test)
print(result)

# map of Australia 
test = MapColoring(["WA", "NT", "SA", "Q", "NSW", "V", "T"],
                      ["Red", "Blue", "Green"],
                      [("WA", "NT"),("WA", "SA"), ("NT","SA"),("NT","Q"),("SA","Q"),("Q","NSW"),("SA","NSW"),("SA","V"),("NSW","V")])
result = backtracking_search(test)
print(result)

# reorder states
test = MapColoring(["WA", "NSW", "T", "SA", "V", "Q", "NT"],
                      ["Red", "Blue", "Green"],
                      [("WA", "NT"),("WA", "SA"), ("NT","SA"),("NT","Q"),("SA","Q"),("Q","NSW"),("SA","NSW"),("SA","V"),("NSW","V")])
result = backtracking_search(test)
print(result)

# reorder states 
test = MapColoring(["WA", "V", "Q", "SA", "NT", "NSW", "T"],
                      ["Red", "Blue", "Green"],
                      [("WA", "NT"),("WA", "SA"), ("NT","SA"),("NT","Q"),("SA","Q"),("Q","NSW"),("SA","NSW"),("SA","V"),("NSW","V")])
result = backtracking_search(test)
print(result)

# map of US
test = MapColoring(["AK", "AL", "AR", "AZ", "CA", "CO", "CT", "DC", "DE", "FL", "GA",
                        "HI", "IA", "ID", "IL", "IN", "KS", "KY", "LA", "MA", "MD", "ME",
                        "MI", "MN", "MO", "MS", "MT", "NC", "ND", "NE", "NH", "NJ", "NM",
                        "NV", "NY", "OH", "OK", "OR", "PA", "RI", "SC", "SD", "TN", "TX",
                        "UT", "VA", "VT", "WA", "WI", "WV", "WY"], 
                    ["Red", "Blue", "Green", "Yellow"],
                    [("AL", "MS"), ("AL", "FL"), ("AL", "GA"), ("AL", "TN"),
                        ("AR", "LA"), ("AR", "MO"), ("AR", "MS"), ("AR", "OK"), ("AR", "TN"), ("AR", "TX"),
                        ("AZ", "CA"), ("AZ", "CO"), ("AZ", "NM"), ("AZ", "NV"), ("AZ", "UT"), 
                        ("CA", "NV"), ("CA", "OR"), 
                        ("CO", "KS"), ("CO", "NE"), ("CO", "NM"), ("CO", "OK"), ("CO", "UT"), ("CO", "WY"),
                        ("CT", "MA"), ("CT", "NY"), ("CT", "RI"),
                        ("DC", "MD"), ("DC", "VA"),
                        ("DE", "MD"), ("DE", "NJ"), ("DE", "PA"),
                        ("FL", "GA"),
                        ("GA", "NC"), ("GA", "SC"), ("GA", "TN"),
                        ("IA", "IL"), ("IA", "MN"), ("IA", "MO"), ("IA", "NE"), ("IA", "SD"), ("IA", "WI"),
                        ("ID", "MT"), ("ID", "NV"), ("ID", "OR"), ("ID", "UT"), ("ID", "WA"), ("ID", "WY"),
                        ("IL", "IN"), ("IL", "KY"), ("IL", "MO"), ("IL", "WI"),
                        ("IN", "KY"), ("IN", "MI"), ("IN", "OH"),
                        ("KS", "MO"), ("KS", "NE"), ("KS", "OK"),
                        ("KY", "MO"), ("KY", "OH"), ("KY", "TN"), ("KY", "VA"), ("KY", "WV"),
                        ("LA", "MS"), ("LA", "TX"),
                        ("MA", "NH"), ("MA", "NY"), ("MA", "RI"), ("MA", "VT"),
                        ("MD", "PA"), ("MD", "VA"), ("MD", "WV"),
                        ("ME", "NH"),
                        ("MI", "OH"), ("MI", "WI"),
                        ("MN", "ND"), ("MN", "SD"), ("MN", "WI"),
                        ("MO", "NE"), ("MO", "OK"), ("MO", "TN"),
                        ("MS", "TN"),
                        ("MT", "ND"), ("MT", "SD"), ("MT", "WY"),
                        ("NC", "SC"), ("NC", "TN"), ("NC", "VA"),
                        ("ND", "SD"),
                        ("NE", "SD"), ("NE", "WY"),
                        ("NH", "VT"),
                        ("NJ", "NY"), ("NY", "PA"),
                        ("NM", "OK"), ("NM", "TX"), ("NM", "UT"),
                        ("NV", "OR"), ("NV", "UT"),
                        ("NY", "PA"), ("NY", "VT"),
                        ("OH", "PA"), ("OH", "WV"),
                        ("OK", "TX"),
                        ("OR", "WA"),
                        ("PA", "WV"),
                        ("SD", "WY"),
                        ("TN", "VA"),
                        ("UT", "WY"),
                        ("VA", "WV"),])

result = backtracking_search(test)
print(result)