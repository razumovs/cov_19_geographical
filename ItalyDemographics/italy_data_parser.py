import io

import pandas as pd
import requests


def read_regioni():
    url = "https://raw.githubusercontent.com/razumovs/cov_19_geographical/master/ItalyDemographics/regioni.csv"
    print(url)
    urlData = requests.get(url).content
    rawData = pd.read_csv(io.StringIO(urlData.decode("utf-8")))
    return rawData


def read_density():
    url = "https://raw.githubusercontent.com/razumovs/cov_19_geographical/master/ItalyDemographics/population_density_regions_italy.csv"
    print(url)
    urlData = requests.get(url).content
    rawData = pd.read_csv(io.StringIO(urlData.decode("utf-8")), sep="\t")
    return rawData


region_df = read_regioni()
region_population_df = read_density()

# population density information - the source is from 2019,
# and may not match the region information from demo.istat.it exactly (2018)
# shoud be ok for the purposes of getting population density and male/female
def get_list_population_stat_by_region(region: str):
    return region_population_df.loc[region_population_df["Regione"] == region]


def get_number_population_denstiy_by_region(region: str):
    df = get_list_population_stat_by_region(region)
    return df["Density"].iloc[0]


def get_number_population_by_region(region: str):
    df = get_list_population_stat_by_region(region)
    return df["Population"].iloc[0]


def get_number_area_by_region(region: str):
    df = get_list_population_stat_by_region(region)
    return df["Area_km"].iloc[0]

# demographics information
def get_list_population_by_region(region: str):
    region_res = region_df.loc[region_df["Regione"] == region]
    return region_res


def get_number_male_population_by_region(region: str):
    df = get_list_population_by_region(region)
    return df["Totale Maschi"][101]


def get_number_female_population_by_region(region: str):
    df = get_list_population_by_region(region)
    return df["Totale Femmine"][101]


def get_total_population_by_region(region: str):
    return get_number_male_population_by_region(
        region
    ) + get_number_female_population_by_region(region)


def get_age_range(df_location, age_lower_bound, age_upper_bound):
    age_column = df_location["Età"]
    sum_female_number = 0
    sum_male_number = 0
    if age_lower_bound < 0:
        age_lower_bound = 0
    if age_upper_bound > 100:
        age_upper_bound = 100
    for i in range(age_lower_bound, age_upper_bound + 1, 1):
        if i in age_column:
            sum_female_number += df_location["Totale Femmine"][i]
            sum_male_number += df_location["Totale Maschi"][i]
    return (sum_female_number, sum_male_number)


def get_age_range_by_region(region: str, age_lower_bound, age_upper_bound):
    df_location = get_list_population_by_region(region)
    return get_age_range(df_location, age_lower_bound, age_upper_bound)
