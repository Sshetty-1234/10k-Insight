# Loads in the 10 K files from the SEC website

from sec_edgar_downloader import Downloader

dl = Downloader("User/sohamshetty/desktop", "sohamshetty12@gmail.com", "10-K filings")

dl.get("10-K", "AAPL",after="1995-01-01", before="2023-01-01",download_details=True)
dl.get("10-K", "DELL",after="1995-01-01", before="2024-01-01",download_details=True)
print("Done")