
# Video Game Sales Scraper

<div align="center">
  <img src="assets/headline.jpg" alt="Banner Image">
</div>

## Overview

This project aims to scrape video game sales data from the VGChartz website using web scraping techniques. The scraped data includes information such as game rank, name, publisher, developer, scores, sales figures, and more.

## Table of Contents

- [Video Game Sales Scraper](#video-game-sales-scraper)
  - [Overview](#overview)
  - [Table of Contents](#table-of-contents)
  - [Installation](#installation)
  - [Usage](#usage)
  - [Dependencies](#dependencies)
  - [How to Run](#how-to-run)
  - [Data Columns](#data-columns)
  - [Output](#output)
  - [Contributing](#contributing)
  - [License](#license)

## Installation

To run this scraper, make sure you have Python installed on your machine. Additionally, install the required libraries using:

```bash
pip install requests beautifulsoup4 pandas numpy
```

## Usage

This scraper is designed to fetch video game sales data from VGChartz based on specified parameters such as genre and year.

## Dependencies

- [Requests](https://docs.python-requests.org/en/master/): Used to send HTTP requests.
- [Beautiful Soup](https://www.crummy.com/software/BeautifulSoup/bs4/doc/): A library for pulling data out of HTML and XML files.
- [Pandas](https://pandas.pydata.org/): A data manipulation and analysis library.
- [NumPy](https://numpy.org/): A library for the Python programming language, adding support for large, multi-dimensional arrays and matrices.

## How to Run

1. Clone the repository:

```bash
git clone https://github.com/your-username/vgchartz-scraper.git
```

2. Change into the project directory:

```bash
cd vgchartz-scraper
```

3. Run the scraper:

```bash
python scraper.py
```

## Data Columns

The following columns are included in the scraped data:

- `Rank`: Game rank.
- `Name`: Game name.
- `Publisher`: Game publisher.
- `Developer`: Game developer.
- `VGChartz_Score`: VGChartz score.
- `Critic_Score`: Critic score.
- `User_Score`: User score.
- `Total_Shipped`: Total shipped units.
- `Total_Sales`: Total sales units.
- `NA_Sales`: Sales in North America.
- `PAL_Sales`: Sales in the PAL region.
- `Japan_Sales`: Sales in Japan.
- `Other_Sales`: Sales in other regions.
- `Release_Date`: Release date of the game.
- `Last_Update`: Last update date.
- `Genre`: Game genre.
- `Year`: Year of release.
- `Platforms`: Game platforms.

## Output

The scraped data is saved in a CSV file named `output.csv` in the project directory.

## Contributing

Contributions are welcome! Please follow the [Contributing Guidelines](CONTRIBUTING.md).

## License

This project is licensed under the [MIT License](LICENSE).

