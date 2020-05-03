## Climate Change Data Dashboard
How much CO2 is emitted by countries and what is the forest area? What insights can be derived about the climate action taken by individual countries using data? This dashboard allows users to interactively explore data from the World Bank that describes different metrics relating to climate change worldwide.

## Table of Contents
* [Installation](#Installation)
* [Project Motivation](#motivation)
* [File Description](#description)
* [Results](#Results)
* [Licensing, Authors, Acknowledgements](#licensing)

## Installation
The code requires Python versions of 3.* as well as Bootstrap 4.0, Flask, pandas and requests.
In addition, for deployment the package gunicorn needs to be installed as well.

## Project Motivation <a name="motivation"></a>
This dashboard was developed to provide an overview of climate change related information in interactive
graphs to allow the user to explore its different dimensions. Plotly was used to make the plots
dynamic.

![Screenshot of webapp](https://github.com/julianikulski/climate-change-data/blob/master/myapp/static/img/webapp.PNG)

## File Description <a name="description"></a>
In the folder myapp, all relevant HTML, CSS and Python files to render the dashboard are included. The
wrangling_scripts folder consists of a Python file that brings the data in the right shape to be
displayed in the dashboard. The remaining files (requirements.txt, Procfile, myapp) are used for deployment of the dashboard.

## Licensing, Authors, Acknowledgements <a name="licensing"></a>
The underlying data used for the analysis comes from the [World Bank](https://data.worldbank.org/summary-terms-of-use). Feel free to use the code to add additional features to the data dashboard.
