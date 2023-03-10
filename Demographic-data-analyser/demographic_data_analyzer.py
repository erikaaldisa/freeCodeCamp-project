import pandas as pd


def calculate_demographic_data(print_data=True):
    # Read data from file
    df = pd.read_csv('adult.data.csv') 

    # How many of each race are represented in this dataset? This should be a Pandas series with race names as the index labels.
    race_count = df["race"].value_counts()

    # What is the average age of men?
    average_age_men = round(df[df["sex"]=="Male"]["age"].mean(),1)

    # What is the percentage of people who have a Bachelor's degree?
    df2 = df.groupby(["education"]).count()
    df2["%"] = (df2["age"]/df2["age"].sum())*100
    percentage_bachelors = round(df2["%"]["Bachelors"],1)

    # What percentage of people with advanced education (`Bachelors`, `Masters`, or `Doctorate`) make more than 50K?
    # What percentage of people without advanced education make more than 50K?

    # with and without `Bachelors`, `Masters`, or `Doctorate`
    edu_list = ["Bachelors", "Masters", "Doctorate"]
    df3 = df[(df["education"].isin(edu_list))& (df["salary"]==">50K")]
    df4 = df[(df["education"].isin(edu_list))]
    df5 = df[(~df["education"].isin(edu_list))& (df["salary"]==">50K")]
    df6 = df[(~df["education"].isin(edu_list))]

    higher_education = df[(df["education"].isin(edu_list))& (df["salary"]==">50K")]
    lower_education = df[(~df["education"].isin(edu_list))& (df["salary"]==">50K")]

    # percentage with salary >50K
    higher_education_rich = round(df3.shape[0]/df4.shape[0]*100,1)
    lower_education_rich = round(df5.shape[0]/df6.shape[0]*100,1)

    # What is the minimum number of hours a person works per week (hours-per-week feature)?
    min_work_hours = df["hours-per-week"].min()

    # What percentage of the people who work the minimum number of hours per week have a salary of >50K?
    num_min_workers = df[df["hours-per-week"] == df["hours-per-week"].min()]

    rich_percentage = round(len(num_min_workers[num_min_workers["salary"]==">50K"])/len(num_min_workers)*100,1)

    # What country has the highest percentage of people that earn >50K?
    pct = lambda x: 100 * x / x.sum()
    df7 = df.groupby(["native-country","salary"]).count()
    df8 = df7.groupby(["native-country"]).apply(pct)['age'].reset_index()
    df9 = df8[df8["salary"]== ">50K"].sort_values(by="age", ascending=False)

    highest_earning_country = df9.iloc[0,0]
    highest_earning_country_percentage = round(df9.iloc[0,-1],1)

    # Identify the most popular occupation for those who earn >50K in India.
    df10 = df.groupby(["native-country", "salary"]).get_group(("India", ">50K"))
    df10 = df10.groupby(["occupation"])["age"].count().sort_values(ascending=False)
    top_IN_occupation = df10.index[0]

    # DO NOT MODIFY BELOW THIS LINE

    if print_data:
        print("Number of each race:\n", race_count) 
        print("Average age of men:", average_age_men)
        print(f"Percentage with Bachelors degrees: {percentage_bachelors}%")
        print(f"Percentage with higher education that earn >50K: {higher_education_rich}%")
        print(f"Percentage without higher education that earn >50K: {lower_education_rich}%")
        print(f"Min work time: {min_work_hours} hours/week")
        print(f"Percentage of rich among those who work fewest hours: {rich_percentage}%")
        print("Country with highest percentage of rich:", highest_earning_country)
        print(f"Highest percentage of rich people in country: {highest_earning_country_percentage}%")
        print("Top occupations in India:", top_IN_occupation)

    return {
        'race_count': race_count,
        'average_age_men': average_age_men,
        'percentage_bachelors': percentage_bachelors,
        'higher_education_rich': higher_education_rich,
        'lower_education_rich': lower_education_rich,
        'min_work_hours': min_work_hours,
        'rich_percentage': rich_percentage,
        'highest_earning_country': highest_earning_country,
        'highest_earning_country_percentage':
        highest_earning_country_percentage,
        'top_IN_occupation': top_IN_occupation
    }
