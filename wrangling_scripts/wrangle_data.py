import requests
import pandas as pd
import plotly.graph_objs as go
import plotly.colors
from collections import OrderedDict

# Reading in data from API and preparing the plotly visualizations

# default list of countries to be considered
country_default = OrderedDict([('Canada', 'CAN'), ('United States', 'USA'), 
  ('Brazil', 'BRA'), ('France', 'FRA'), ('India', 'IND'), ('Italy', 'ITA'), 
  ('Germany', 'DEU'), ('United Kingdom', 'GBR'), ('China', 'CHN'), ('Japan', 'JPN')])

def return_figures(countries=country_default):
    """Creates four plotly visualizations

    Args:
        None

    Returns:
        list (dict): list containing the four plotly visualizations

    """

    # use country default list if no other countries are specified by user
    if not bool(countries):
        countries = country_default
        
    # get country data ready to use it for World Bank API
    list_country_codes = list(countries.values())
    format_codes = [val.lower() for val in list_country_codes]
    format_codes = ';'.join(format_codes)

    # Worldbank indicators of interest: CO2 emissions, renewable electricity output, forest area, cereal yield
    indicators = ['EN.ATM.CO2E.PC', 'EG.ELC.RNEW.ZS', 'AG.LND.FRST.ZS', 'AG.YLD.CREL.KG']
    
    # create list containers for data and urls
    df_indicators = []
    urls = []
    
    # generate the API urls for all indicators
    for i in indicators:
        url = 'http://api.worldbank.org/v2/countries/' + format_codes +\
        '/indicators/' + i + '?date=1990:2015&per_page=1000&format=json'
        urls.append(url)

        # try to access the API and return error message if not able to
        try:
            r = requests.get(url)
            data = r.json()[1]
        except:
            print('Data could not be retrieved for ', i)
            
        # reformat data and append results to df_indicators list
        for i, value in enumerate(data):
            value['indicator'] = value['indicator']['value']
            value['country'] = value['country']['value']

        df_indicators.append(data)
    
    # first chart plots CO2 emissions from 1990 to 2014 in top 10 economies 
    # as a line chart
    graph_one = []   
    df_one = pd.DataFrame(df_indicators[0])

    countrylist = df_one.country.unique().tolist()
  
    for country in countrylist:
        x_val = df_one[df_one['country'] == country].date.tolist()
        y_val =  df_one[df_one['country'] == country].value.tolist()
        graph_one.append(
            go.Scatter(
            x = x_val,
            y = y_val,
            mode = 'lines',
            name = country
            )
        )

    layout_one = dict(title = 'CO2 emissions in kilotons',
                xaxis = dict(title = 'Year', autotick=False, tick0=1990, dtick=5),
                yaxis = dict(title = 'Kilotons'),
                )

# second chart plots forest area for 2017 as a bar chart    
    graph_two = []
    df_two = pd.DataFrame(df_indicators[2])
    df_two.sort_values('value', ascending=False, inplace=True)
    df_two = df_two[df_two['date'] == '2014'] 

    graph_two.append(
        go.Bar(
            x = df_two.country.tolist(),
            y = df_two.value.tolist(),
        )
    )

    layout_two = dict(title = 'Forest area as a percentage of land area in 2014',
                xaxis = dict(title = 'Country',),
                yaxis = dict(title = 'Percentage'),
                )

    # third chart plots renewable electricity output as a percentage from 1990 to 2015
    graph_three = []
    df_three = pd.DataFrame(df_indicators[1])

    countrylist = df_three.country.unique().tolist()
  
    for country in countrylist:
        x_val = df_three[df_three['country'] == country].date.tolist()
        y_val =  df_three[df_three['country'] == country].value.tolist()
        graph_three.append(
            go.Scatter(
            x = x_val,
            y = y_val,
            mode = 'lines',
            name = country
            )
        )

    layout_three = dict(title = 'Proportion of renewable electricity output',
                xaxis = dict(title = 'Year'),
                yaxis = dict(title = 'Percentage')
                       )
    
# fourth chart shows cereal yield over time
    graph_four = []
    df_four = pd.DataFrame(df_indicators[3])

    countrylist = df_four.country.unique().tolist()
  
    for country in countrylist:
        x_val = df_four[df_four['country'] == country].date.tolist()
        y_val =  df_four[df_four['country'] == country].value.tolist()
    
        graph_four.append(
          go.Scatter(
          x = x_val,
          y = y_val,
          mode = 'lines',
          name = country
          )
        )

    layout_four = dict(title = 'Cereal yield in kilogram per hectare',
                xaxis = dict(title = 'Year'),
                yaxis = dict(title = 'Kg per hectare'),
                )
    
    # append all charts to the figures list
    figures = []
    figures.append(dict(data=graph_one, layout=layout_one))
    figures.append(dict(data=graph_two, layout=layout_two))
    figures.append(dict(data=graph_three, layout=layout_three))
    figures.append(dict(data=graph_four, layout=layout_four))

    return figures