# Cory Cusick
# ITEC 312-940
# Ocean Levels # Assuming the ocean's level is currently rising at about 1.6 millimeters per year, create an application that displays the number of millimeters that the ocean will have risen each year for the next 25 years.
rise_per_year = 1.6
print("Year\tAnnual Level Rise (mm)")
print("-" * 30)
for year in range(1, 26):
    total_rise = year * rise_per_year
    print(f"{year}\t\t{total_rise:.1f}")