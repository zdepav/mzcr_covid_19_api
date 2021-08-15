## About

Simple python wrapper for the official Czech Republic's Ministry of Health API for COVID-19
statistics available at
[https://onemocneni-aktualne.mzcr.cz/api/v2/covid-19](https://onemocneni-aktualne.mzcr.cz/api/v2/covid-19).

Curently only v2 API is supported.

## Dependencies

- Python 3.x (tested on 3.9, might not work properly on versions older than 3.7)
- python package `requests`

## Usage

Api can be accessed through `MzcrCovid19Api` class, which contains a method for each supported
endpoint. Most methods return iterator which lazily gets the data (except `zakladni_prehled` which 
returns a single record).

## Caching

To avoid re-downloading the data every time it is saved locally and only updated if the API reports
newer modified date. By default, the cache is stored in subdirectory `.cache` of the current working
directory. Cache location can be set in the MzcrCovid19Api constructor:

```python
MzcrCovid19Api(cache_directory_path='path/to/cache')
```

Path is given as a string and can be both absolute and relative. Using `None` instead of a path
disables caching. 

## Example 

```python
from mzcr_covid_19_api import MzcrCovid19Api

age_sum = 0
record_count = 0
for record in MzcrCovid19Api().umrti() :
    if record.datum.year == 2021 and record.pohlavi == 'M' :
        age_sum += record.vek
        record_count += 1

print(f'Průměrný věk úmrtí u mužů v roce 2021: {age_sum / record_count}')
```

## License

Code in this repository is available under the [MIT license](LICENSE)

Documentation is taken from the api (and is therefore only in czech language)

Licence for the data available through the API can be found
[here (CZ only)](http://data.gov.cz/podmínky-užití/volný-přístup/)
