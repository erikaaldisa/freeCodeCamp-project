import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns
from pandas.plotting import register_matplotlib_converters
register_matplotlib_converters()

# Import data (Make sure to parse dates. Consider setting index column to 'date'.)
df = pd.read_csv("fcc-forum-pageviews.csv", parse_dates=["date"], index_col="date")

# Clean data
df = df[(df["value"] >= df["value"].quantile(0.025)) &
        (df["value"] <= df["value"].quantile(0.975))]


def draw_line_plot():
    # Draw line plot
    fig, ax = plt.subplots(figsize=(16, 6))
    ax = sns.lineplot(data=df, x="date", y="value")
    ax.set_xlabel("Date")
    ax.set_ylabel("Page Views")
    ax.set_title("Daily freeCodeCamp Forum Page Views 5/2016-12/2019")

    # Save image and return fig (don't change this part)
    fig.savefig('line_plot.png')
    return fig

def draw_bar_plot():
    # Copy and modify data for monthly bar plot

    df_bar = df.copy().reset_index()
    df_bar["year"] = df_bar["date"].dt.year
    df_bar["month"] = df_bar["date"].dt.month
    df_bar = df_bar.groupby(["year", "month"]).mean()
    df_bar = df_bar.unstack(level=-1)

    # Draw bar plot
    month_names=['January', 'February', 'March', 'April', 'May', 'June', 'July', 
             'August', 'September', 'October', 'November', 'December']
    
    fig = df_bar.plot(kind= 'bar', figsize = (15,10)).figure
    plt.xlabel('Years')
    plt.ylabel('Average Page Views')
    lg = plt.legend(title= 'Months', fontsize = 15, labels = month_names)
    title = lg.get_title()
    title.set_fontsize(15)

    # Save image and return fig (don't change this part)
    fig.savefig('bar_plot.png')
    return fig

def draw_box_plot():
    # Prepare data for box plots (this part is done!)
    df_box = df.copy()
    df_box.reset_index(inplace=True)
    df_box['year'] = [d.year for d in df_box.date]
    df_box['month'] = [d.strftime('%b') for d in df_box.date]

    # Draw box plots (using Seaborn)
    month_names = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']
    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(16, 6))

    sns.boxplot(ax=ax1, data=df_box, x="year", y="value")
    ax1.set_title("Year-wise Box Plot (Trend)")
    ax1.set_xlabel('Year')
    ax1.set_ylabel('Page Views')

    sns.boxplot(ax=ax2, data=df_box, x="month", y="value",order=month_names)
    ax2.set_title("Month-wise Box Plot (Seasonality)")
    ax2.set_xlabel('Month')
    ax2.set_ylabel('Page Views')

    # Save image and return fig (don't change this part)
    fig.savefig('box_plot.png')
    return fig
