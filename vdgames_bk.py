import requests
from bs4 import BeautifulSoup
import pandas as pd
import numpy as np

# Initialize lists
rank, gname, publisher, developer, vgchartz_score, critic_score, user_score = [], [], [], [], [], [], []
total_shipped, total_sales, sales_na, sales_pal, sales_jp, other_sales, release_date, last_update = [], [], [], [], [], [], [], []
genre, year, platforms = [], [], []

pages = 25 #Number of pages to scrape

# List of genres
genres = ['Action-Adventure', 'Action', 'Adventure', 'Board Game', 'Education', 'Fighting', 'Misc', 'MMO',
          'Music', 'Party', 'Platform', 'Puzzle', 'Racing', 'Role-Playing', 'Sandbox', 'Shooter', 'Simulation',
          'Sport', 'Strategy']

# Loop through each year and genre
for goty_year in range(2007, 2023):
    for current_genre in genres:
        url_head = 'http://www.vgchartz.com/gamedb/?page='
        url_tail = '&console=&region=All&developer=&publisher=&genre=' + current_genre + '&boxart=Both&ownership=Both'
        url_tail += '&results=50&order=Sales&showtotalsales=1&showpublisher=1&showvgchartzscore=1'
        url_tail += '&shownasales=1&showdeveloper=1&showcriticscore=1&showpalsales=1&showreleasedate=1'
        url_tail += '&showuserscore=1&showjapansales=1&showlastupdate=1&showothersales=1&showshipped=1'
        url_tail += f'&goty_year={goty_year}&genre={current_genre}'

        for page in range(1, pages + 1):  # Adjust the range to include the last page
            url = f'{url_head}{page}{url_tail}'
            response = requests.get(url)
            soup = BeautifulSoup(response.text, 'html.parser')
          
            print(f"Page: {page}, GOTY Year: {goty_year}, Genre: {current_genre}")

            # Inside the loop where you fetch additional data for each game
            for tr in soup.select('div#generalBody table tr'):
                try:
                    td_list = tr.find_all('td')
                    
        
                    
                    # Extracting the second image and its alt value
                    second_image = tr.find_all('img')[1]
                    alt_value = second_image['alt'] 
                    print(f"Alt Value of the second image: {alt_value}")
                  
        

                    # Your existing data processing logic goes here
                    rank.append(int(td_list[0].text.strip()) if td_list[0].text.strip().isdigit() else np.nan)
                    title = td_list[2].text.strip()
                    gname.append(title)
                    publisher.append(td_list[4].text.strip())
                    developer.append(td_list[5].text.strip())
                    vgchartz_score_text = td_list[6].text.strip()
                    vgchartz_score.append(vgchartz_score_text if vgchartz_score_text != "N/A" else np.nan)
                    critic_score_text = td_list[7].text.strip()
                    critic_score.append(critic_score_text if critic_score_text != "N/A" else np.nan)
                    user_score.append(td_list[8].text.strip() if td_list[8].text.strip() != "N/A" else np.nan)
                    total_shipped.append(td_list[9].text.strip() if td_list[9].text.strip() != "N/A" else np.nan)
                    total_sales.append(td_list[10].text.strip() if td_list[10].text.strip() != "N/A" else np.nan)
                    sales_na.append(td_list[11].text.strip() if td_list[11].text.strip() != "N/A" else np.nan)
                    sales_pal.append(td_list[12].text.strip() if td_list[12].text.strip() != "N/A" else np.nan)
                    sales_jp.append(td_list[13].text.strip() if td_list[13].text.strip() != "N/A" else np.nan)
                    other_sales.append(td_list[14].text.strip() if td_list[14].text.strip() != "N/A" else np.nan)
                    release_date.append(td_list[15].text.strip() if td_list[15].text.strip() != "N/A" else np.nan)
                    last_update.append(td_list[16].text.strip() if td_list[16].text.strip() != "N/A" else np.nan)
                    genre.append(current_genre)
                    year.append(goty_year)
                    platforms.append(alt_value)  # Append the platform alt value

                except IndexError:
                    print("Index error occurred. Skipping this row.")
                    continue  # Skip the current row if there's an index error

# Create a dictionary with lists
data = {
    'Rank': rank, 'Name': gname, 'Publisher': publisher, 'Developer': developer,
    'VGChartz_Score': vgchartz_score, 'Critic_Score': critic_score, 'User_Score': user_score,
    'Total_Shipped': total_shipped, 'Total_Sales': total_sales, 'NA_Sales': sales_na, 'PAL_Sales': sales_pal,
    'Japan_Sales': sales_jp, 'Other_Sales': other_sales, 'Release_Date': release_date, 'Last_Update': last_update,
    'Genre': genre, 'Year': year, 'Platforms':platforms
}

# Check lengths of all lists
list_lengths = {col: len(data[col]) for col in data}
print(f"List Lengths: {list_lengths}")


# Create DataFrame
columns = {
    'Rank': rank, 'Name': gname, 'Publisher': publisher, 'Developer': developer,'Platforms':platforms,
    'VGChartz_Score': vgchartz_score, 'Critic_Score': critic_score, 'User_Score': user_score,'Genre': genre, 'Year': year,
    'Total_Shipped': total_shipped, 'Total_Sales': total_sales, 'NA_Sales': sales_na, 'PAL_Sales': sales_pal,
    'Japan_Sales': sales_jp, 'Other_Sales': other_sales, 'Release_Date': release_date, 'Last_Update': last_update
    
}

df = pd.DataFrame(columns)
df.replace(np.nan, 'NA', inplace=True)
df.to_csv("vgsales.csv", sep=",", encoding='utf-8', index=False)

