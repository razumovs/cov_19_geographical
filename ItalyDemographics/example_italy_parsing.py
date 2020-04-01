from italy_data_parser import *

# examples for region_density information
region_density_information = get_list_population_stat_by_region("Piemonte")
population_num = get_number_population_by_region("Piemonte")
population_dense = get_number_population_denstiy_by_region("Piemonte")
region_area = get_number_area_by_region("Piemonte")
smoker_share = get_number_smoker_share_by_region("Piemonte")

s = f"population:{population_num} area:{region_area} density:{population_dense} smokers share:{smoker_share}"
print(s)


region_population = get_list_population_by_region("Piemonte")
(females, males) = get_age_range(region_population, 99, 100)
print("females ages: 99-100 ", females, " males ages: 99-100 ", males)
ret1 = get_number_male_population_by_region("Piemonte")
print("number of males in selected region ", ret1)
ret2 = get_number_female_population_by_region("Piemonte")
print("number of females in selected region ", ret2)
ret = get_total_population_by_region("Piemonte")
print("total population in selected region ", ret)
