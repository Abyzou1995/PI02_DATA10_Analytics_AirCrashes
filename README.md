<p align=center><img src="src/logo-henry.png"><p>

# <h1 align=center> Analytics Project - HENRY DATA SCIENCE <h/>
## <h2 align=center> Airplane Crashes <h/>
### <h3 align=center> By Angel Bello Merlo <h/>
<p align="center">
<img src="src/airplane-crash.jpg"  height=300>
</p>

## Topic

Air accidents are unexpected and unwanted events that involve aircraft and cause physical damage to people or to the aircraft itself. A plane crash can involve any type of aircraft, including commercial jets, private jets, helicopters, gliders, and hot air balloons.

Air crashes can be caused by a variety of factors, including human error, equipment failure, weather issues, maintenance issues, air traffic management failures, design issues, or manufacturing issues. And as for its consequences, they can be both in terms of human and economic losses.

That's why the aviation industry, regulatory authorities, and researchers work tirelessly to improve aviation safety and prevent future accidents.

For this reason, the analysis of historical air accident data is essential to improve aviation safety. The systematic collection and analysis of crash data can help investigators identify patterns, trends, and contributing factors that could lead to improvements in safety, from helping improve the training of pilots and maintenance personnel, as well as to improve the design and manufacture of aircraft and aviation equipment.

## ETL process
Extract, Transform and load process was carried out following these steps.

Original Dataset:
[Original Dataset ](https://github.com/Abyzou1995/PI02_DATA10_Analytics_AirCrashes/tree/main/Dataset_original)

This process can be seen there:
[ETL Analytics ](https://github.com/Abyzou1995/PI02_DATA10_Analytics_AirCrashes/blob/main/ETL.ipynb)
Dataset after ETL:
[ETL Dataset ](https://github.com/Abyzou1995/PI02_DATA10_Analytics_AirCrashes/tree/main/Dataset_final)

## EDA 
Exploratory Data Analysis was carried out following these steps.
+ Cleaning datased done.
+ Use libraries like pandas_profiling, missingno, pandas, matplotlib.
+ Investigate the relationships between the variables of the datasets.
+ The EDA should include interesting graphs to extract data.
+ Check if there are outliers or anomalies.

<p align=center><img src="src/EDA.png"><p>

This process can be seen there:
[EDA Analytics ](https://github.com/Abyzou1995/PI02_DATA10_Analytics_AirCrashes/blob/main/EDA.ipynb)
Dataset after EDA:
[EDA Dataset ](https://github.com/Abyzou1995/PI02_DATA10_Analytics_AirCrashes/tree/main/Dataset_final)

## KPIs

1. Mortality Rate.

      $$Rate=N° Fatalities/N° Aboard$$

2. Accident Fatality Rate.

      $$Rate=N° Accidents With Fatalities/N° Accidents$$

3. Accident Death Rate.

      $$Rate=N° Accidents With Fatalities/N° Accidents$$

4. Variation Accidents Rate.

      $$Rate=(N° Accidents (N)year-N°Accicents(N-1)Year) /N°Accicents(N-1)Year$$

This process can be seen there:
[KPIs Analytics ](https://github.com/Marcostamal/PI_MASA_DE/blob/main/Data_Cleaning_Plataformas.ipynb)

## Function ML Movie Recommendation System for the API Development

+ This consists of recommending movies to users based on similar movies, so the score similarity between that movie and the rest of the movies must be found, they will be ordered according to the similarity score and it will return a list with 5 values

Based on research articules, features and ML text-analysis model were chosen.
1. Features: genres, overview(sample based on Popularity due to an excesive computational cost if whole dataset is used).
2. TF-IDF (Term Frequency–Inverse Document Frequency) for Natural Language Proccesing ML model using Scikit-learn.

<p align=center><img src="src/EDA2.png"><p>

This process can be seen there:
[Model MLops Movie Recommendation System ](https://github.com/Marcostamal/PI_MASA_DE/blob/main/Data_Cleaning_Plataformas.ipynb)

## Deployment
+ Making the company data available using the FastAPI framework.
+ Render is an unified cloud to build and run all your apps and websites.
<p align=center><img src="src/Render.png"><p>

Deployed API can be seen there:
[Render API Movie Recommendation System ](https://github.com/Marcostamal/PI_MASA_DE/blob/main/Data_Cleaning_Plataformas.ipynb)

## Video Tutorial
This video can be seen there:
[MLops Movie Recommendation System ](https://github.com/Marcostamal/PI_MASA_DE/blob/main/Data_Cleaning_Plataformas.ipynb)

