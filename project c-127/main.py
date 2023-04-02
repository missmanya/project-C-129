import pandas as pd

final_stars_df = pd.read_csv('/content/PRO-NASA-Exoplanet-Scraped-Data/final_scraped_data.csv')
archive_stars_df = pd.read_csv('/content/PRO-NASA-Exoplanet-Scraped-Data/PSCompPars.csv')


final_stars_df.head()
archive_stars_df.head()

final_stars_df.drop(columns=['mass','discovery_date'], inplace=True)
final_stars_df.head()

archive_stars_df.head()

header=["name", "light_years_from_earth", "planet_mass", "stellar_magnitude", "discovery_date", "hyperlink","planet_type","discovery_date", "mass", "planet_radius", "orbital_radius", "orbital_period", "eccentricity"]
final_stars_df= pd.DataFrame(columns=header)
final_stars_df= pd.merge()

final_stars_df.shape
archive_stars_df.shape

page1=pd.read_csv('/content/PRO-NASA-Exoplanet-Scraped-Data/updated_scraped_data.csv')
page2=pd.read_csv('/content/PRO-NASA-Exoplanet-Scraped-Data/new_scraped_data.csv')
page1.head()

page2.head()
finalframe=pd.merge(page1,page2)
finalframe.head()




