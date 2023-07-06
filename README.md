# Sports Snooze - Web Application of Deep Analysis of Olympics
## Introduction
This is an Exploratory Data Analysis project to analyze the modern Olympic Games, including all the Games from Athens 1896 to Tokyo 2020. This analysis provides an opportunity to ask questions about how the Olympics have evolved over time, including questions about the participation and performance of women, different nations, and different sports and events.

## Data Source
The dataset from 1896 to 2016 is collected from [here](https://www.kaggle.com/datasets/heesoo37/120-years-of-olympic-history-athletes-and-results). The dataset contains two files: athlete_events.csv and noc_regions.csv. <br>
The file athlete_events.csv contains 271116 rows and 15 columns. Each row corresponds to an individual athlete competing in an individual Olympic event (athlete events). The columns are:

1. ID - Unique number for each athlete
1. Name - Athlete's name
1. Sex - M or F
1. Age - Integer
1. Height - In centimetres
1. Weight - In kilograms
1. Team - Team name
1. NOC - National Olympic Committee 3-letter code
1. Games - Year and season
1. Year - Integer
1. Season - Summer or Winter
1. City - Host city
1. Sport - Sport
1. Event - Event
1. Medal - Gold, Silver, Bronze, or NA <br>

The file noc_regions.csv contains 230 rows and 3 columns. Each row corresponds to an individual region. The columns are:

1. NOC (National Olympic Committee 3 letter code)
1. region
1. notes

The data for Tokyo 2020 Olympics is obtained from [here](https://www.kaggle.com/datasets/fearsomejockey/olympics-dataset-2020-tokyo-dataset).

## Python Web App
This project is deployed on Streamlit Community Cloud. You can access the web app [Sports_Snooze](https://shivam-bansal1-sports-snooze-app-3tyvgn.streamlit.app/).<br>
**Note: All the graphs and charts are interactive. You can hover over the graphs and charts to get more information. You can also download the graphs and charts in png format.**


## Features of the Web App
The web app provides a brief overview of the dataset. It provides users to choose between 5 options to explore the dataset. The options are:

1. Medal Tally
1. Overall Analysis
1. Country-wise Analysis
1. Athlete-wise Analysis
1. News

### 1. Medal Tally
This section provides the medal tally of all the countries that have participated in the Olympics. 
1. The medal tally is displayed in a table format. The table can also be filtered by selecting the Country Name and Year from the dropdown list.
1. No. of medals won over the years by each country(Geo Map).

### 2. Overall Analysis
This section provides the overall analysis of the Olympics. It provides information like:

1. Top Statistics of the Olympics (Edition, Hosts, Sports, Events, Nations, Athletes)
1. No. of countries participating in the Olympics over the years (Line Graph)
1. No. of events organized over the years (Line Graph)
1. No. of athletes participating over the years (Line Graph)
1. Table of top 15 athletes who have won the most number of medals in the Olympics. This table can also be filtered by selecting the Sports Name from the dropdown list.

### 3. Country-wise Analysis
This section provides a country-wise analysis of the Olympics. It contains a dropdown list where user can select Country Name, based on that the section will display the following information:

1. Medal Tally over the years for that country (Line Graph)
1. In which sport does the country excel the most (Heatmap)
1. Top 10 athletes of that country (Table)

### 4. Athlete-wise Analysis
This section provides an athlete-wise analysis of the Olympics.

1. Distribution of Age of the athletes for Winning Medals (Curves)
1. Distribution of Age w.r.t Sports only who have won Gold Medals (Curves)
1. Men Vs Women Participation Over the Years (Line Graph)

### 5. News
This section shows news related to Olympics and related sports.

## How to run the project locally
1. Clone the repository using git clone https://github.com/shivam-bansal1/sports_snooze.git in the terminal
1. Install the required libraries (mentioned in requirements.txt)
1. Run the command streamlit run app.py to run the app locally
1. The web app will open in the browser
