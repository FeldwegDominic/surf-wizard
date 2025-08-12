from surfForecast import SurfForecastScraper

if __name__ == "__main__":
    scraper = SurfForecastScraper("https://www.surf-forecast.com")
    data = scraper.get_energy_with_timestamps("/breaks/La-Piste/forecasts/latest/six_day")
    for entry in data:
        print(entry)