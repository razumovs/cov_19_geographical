from italy_data_parser import *

# examples for region_density information
region_density_information = get_list_population_stat_by_region("Piemonte")
population_num = get_number_population_by_region("Piemonte")
population_dense = get_number_population_density_by_region("Piemonte")
region_area = get_number_area_by_region("Piemonte")

s = f"population:{population_num} area:{region_area} density:{population_dense}"
print(s)


region_population = get_list_population_by_region("Abruzzo")
(females, males) = get_age_range(region_population, 99, 100)
print("females ages: 99-100 ", females, " males ages: 99-100 ", males)
ret1 = get_number_male_population_by_region("Piemonte")
print("number of males in selected region ", ret1)
ret2 = get_number_female_population_by_region("Piemonte")
print("number of females in selected region ", ret2)
ret = get_total_population_by_region("Piemonte")
print("total population in selected region ", ret)


result_italy = open("{}/{}".format(".", "italy_demographics.csv"), "w", encoding="utf-8")

#https://worldpopulationreview.com/countries/smoking-rates-by-country/  - italy smoking rate (not region based)
#	Total Smoking Rate,Male Smoking Rate,Female Smoking Rate
# 24.00%	28.30%	19.70%
#obesity from CIA factbook 2016
#19.9
result_italy.write("State,Population,Area,Density,Male,Female,0-04,5-9,10-14,15-19,20-24,25-29,30-34,35-39,40-44,45-49,50-54,55-59,60-64,65-69,70-74,75-79,80+, TotalSmokingRate, MaleSmokingRate,FemaleSmokingRate,Obesity2016")
result_italy.write("\n")

for key in region_population_df["Regione"]:
    region_population = get_list_population_by_region(key)
    s = key +","+ str(get_total_population_by_region(key))+","+str(get_number_area_by_region(key))+","+str(get_number_population_density_by_region(key))+","+str(get_number_male_population_by_region(key))+","+str(get_number_female_population_by_region(key))

    (f,m) = get_age_range(region_population,0,4)
    s = s + "," + str(f+m)
    (f,m) = get_age_range(region_population,5,9)
    s = s + "," + str(f+m)
    (f,m) = get_age_range(region_population,10,14)
    s = s + "," + str(f+m)
    (f,m) = get_age_range(region_population,15,19)
    s = s + "," + str(f+m)
    (f,m) = get_age_range(region_population,20,24)
    s = s + "," + str(f+m)
    (f,m) = get_age_range(region_population,25,29)
    s = s + "," + str(f+m)
    (f,m) = get_age_range(region_population,30,34)
    s = s + "," + str(f+m)
    (f,m) = get_age_range(region_population,35,39)
    s = s + "," + str(f+m)
    (f,m) = get_age_range(region_population,40,44)
    s = s + "," + str(f+m)
    (f,m) = get_age_range(region_population,45,49)
    s = s + "," + str(f+m)
    (f,m) = get_age_range(region_population,50,54)
    s = s + "," + str(f+m)
    (f,m) = get_age_range(region_population,55,59)
    s = s + "," + str(f+m)
    (f,m) = get_age_range(region_population,60,64)
    s = s + "," + str(f+m)
    (f,m) = get_age_range(region_population,65,69)
    s = s + "," + str(f+m)
    (f,m) = get_age_range(region_population,70,74)
    s = s + "," + str(f+m)
    (f,m) = get_age_range(region_population,75,79)
    s = s + "," + str(f+m)
    (f,m) = get_age_range(region_population,80,100)
    s = s + "," + str(f+m)
    s = s + "," + "24.00, 28.30,19.70,19.9"

    result_italy.write(s)
    result_italy.write("\n")

#examples for region_density information
region_density_information = get_list_population_stat_by_region("Piemonte")
population_num = get_number_population_by_region("Piemonte")
population_dense = get_number_population_density_by_region("Piemonte")
region_area = get_number_area_by_region("Piemonte")

s = f"source1 population, {population_num}, region area: {region_area} population density {population_dense}"
print(s)

