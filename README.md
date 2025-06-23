# 📊 Bar Chart Race: Top Indian Companies by Net Worth (2014–2025)

This project visualizes the year-wise evolution of the top Indian companies based on their **annual net worth** using a dynamic bar chart race animation.

---

## 📌 Project Highlights

- 🏢 **Data Source**: [Screener.in](https://www.screener.in/)
- 📈 **Visualization Tool**: `bar_chart_race` Python library
- 🧠 **Tech Used**: Python, Pandas, MoviePy, FFmpeg
- 📹 **Output**: Animated `final_net_worth.mp4` video (15 seconds)

---

## 🔍 Objective

To demonstrate how the net worth rankings of top Indian companies have changed over time and to practice:
- Web scraping of time-series financial data
- Data cleaning & transformation
- Bar chart race animation
- Video editing (slowing down final output)

---

## 📦 Requirements

- Installing Dependencies: pandas, bar_chart_race, moviepy, etc.

## Procedure
1. Scraping the Data:-
    - I tried various methods including BeautifulSoup and html5 libraries but the best that worked was pandas for me. So, I finally scraped the screener.in webpage using read_html function from pandas for 76 various tickers, which I found were the topmost companies in India.
    - Now, there was no direct net worth column in the balance sheet table on screener so the net worth has been calculated as a sum of Equity Capital and Reserves.
    - Once extracted, this dataset was saved in an excel file for further transformations.

2. Transforming the Data:-
    - The dataset consisted of various discrepancies which were then cleaned and transformed using Power Query Editor.

3. Using the Bar Chart Race library for creating this awesome visualization:-
    - The cleaned datatset was extracted to the Python script and cleaned a bit further more and the visulaization was created.
    - Now, the library has a fix fps of 30 which ended up always creating a 5 second video which was too fast for me so I used ffmpeg which is bash based tool to slow down the video to it's 1/3rd speed which provides me the final video.

## Files and their purpose
- try1.ipynb : This is for my rough work and has no use other than that.
- dataScraper.py : This is used to scrape the companies' data from screener.in.
- net_worth_timeseries.xlsx : This is the file that was loaded after scraping.
- net_worth_timeseries_cleaned.xlsx : This is the cleaned file created after cleaning the dataset in the Power Query Editor.
- netWorthRace.py : This is the file that, after running, created the beautiful visulaization with the desired parameters.
- net_worth_barchart_race.mp4 : This is the 5 second video with very fast visuals that got created.
- final_net_worth.mp4 : This is the final 16 seconds video that got created after slowing the video down using ffmpeg.