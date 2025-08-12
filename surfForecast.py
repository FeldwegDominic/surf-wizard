from scraper import Scraper  # Assumes your base class is in scraper.py

class SurfForecastScraper(Scraper):
    def __init__(self, base_url, headers=None):
        super().__init__(base_url, headers)

    def get_energy_with_timestamps(self, path=""):
        soup = self.scrape(path)
        if not soup:
            return []

        # Extract day cells from the header row
        day_cells = soup.select("tr.forecast-table__row.forecast-table-days > td.forecast-table-days__cell")

        date_list = []
        for cell in day_cells:
            colspan = int(cell.get("colspan", 1))

            day_name_div = cell.select_one("div.forecast-table__value.forecast-table-days__content > div:nth-child(1)")
            day_number_div = cell.select_one("div.forecast-table__value.forecast-table-days__content > div:nth-child(2)")

            if not day_name_div or not day_number_div:
                continue  # skip empty or locked days

            day_name = day_name_div.get_text(strip=True)
            day_number = day_number_div.get_text(strip=True)

            # Just combine as a string here, e.g. "Wednesday 13"
            date_str = f"{day_name} {day_number}"

            # Repeat the date string colspan times to match timeslots
            date_list.extend([date_str] * colspan)

        # Extract times and energies
        time_cells = soup.select("td.forecast-table__cell.forecast-table-time__cell span.forecast-table__value")
        energy_cells = soup.select("td.forecast-table__cell.forecast-table-energy__cell strong")

        results = []
        for date_str, time_cell, energy_cell in zip(date_list, time_cells, energy_cells):
            time_str = time_cell.get_text(strip=True)
            energy_str = energy_cell.get_text(strip=True)

            results.append({
                "date": date_str,
                "time": time_str,
                "energy": energy_str
            })

        return results