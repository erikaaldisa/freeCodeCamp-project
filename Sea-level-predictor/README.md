<h1 class="text-center big-heading">Sea Level Predictor</h1>

You will analyze a dataset of the global average sea level change since 1880. You will use the data to predict the sea level change through year 2050.

Use the data to complete the following tasks:
- Use Pandas to import the data from ```epa-sea-level.csv```.
- Use matplotlib to create a scatter plot using the ```Year``` column as the x-axis and the ```CSIRO Adjusted Sea Level``` column as the y-axis.
- Use the ```linregress``` function from ```scipy.stats``` to get the slope and y-intercept of the line of best fit. Plot the line of best fit over the top of the scatter plot. Make the line go through the year 2050 to predict the sea level rise in 2050.
- Plot a new line of best fit just using the data from year 2000 through the most recent year in the dataset. Make the line also go through the year 2050 to predict the sea level rise in 2050 if the rate of rise continues as it has since the year 2000.
- The x label should be ```Year```, the y label should be ```Sea Level (inches)```, and the title should be ```Rise in Sea Level```.

Unit tests are written for you under ```test_module.py```.

The boilerplate also includes commands to save and return the image.

<h3 class="text-center big-heading">Development</h3>

For development, you can use ```main.py``` to test your calculate() function. Click the "run" button and ```main.py``` will run.

<h3 class="text-center big-heading">Testing</h3>

We imported the tests from ```test_module.py``` to ```main.py``` for your convenience. The tests will run automatically whenever you hit the "run" button.

<h3 class="text-center big-heading">Data Source</h3>

[Global Average Absolute Sea Level Change](https://datahub.io/core/sea-level-rise), 1880-2014 from the US Environmental Protection Agency using data from CSIRO, 2015; NOAA, 2015.