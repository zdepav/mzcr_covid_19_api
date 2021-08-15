from datetime import date, datetime, timezone
from enum import Enum
from typing import Iterator, Optional, Type, TypeVar
import os
import re
import requests

class ApiVersion(Enum) :
    V1 = 1, 'https://onemocneni-aktualne.mzcr.cz/api/v1/covid-19'
    V2 = 2, 'https://onemocneni-aktualne.mzcr.cz/api/v2/covid-19'
    V1_ICU = 1, 'https://dip.mzcr.cz/api/v1'

    def __init__(self, v: int, url: str) :
        self.version_number = v
        self.url = url


_local_timezone = datetime.now(timezone.utc).astimezone().tzinfo
_modified_regex = re.compile(r'"modified":\s*"([^"]+)"')

def is_expired(cache_file: str, file_name: str, api_version: ApiVersion) -> bool :
    r = requests.get(f'{api_version.url}/{file_name}.json', stream = True)
    modified_time: Optional[datetime] = None
    i = 0
    for line in r.iter_lines() :
        if (m := _modified_regex.search(line.decode('utf-8'))) is not None :
            modified_time = datetime.fromisoformat(m.group(1))
        elif i < 4 :
            i += 1
            continue

        r.close()
        break

    if modified_time is None :
        # modification time not found -> default to 1 day expiration
        return datetime.now().timestamp() - os.path.getmtime(cache_file) > 60 * 60 * 24
    else :
        return datetime.fromtimestamp(os.path.getmtime(cache_file), _local_timezone) < modified_time


T = TypeVar('T')

def get_csv_lines(file_name: str,
                  constructor: Type,
                  api_version: ApiVersion,
                  cache_dir: Optional[str]
                  ) -> Iterator[str] :

    url = f'{api_version.url}/{file_name}.csv'
    if cache_dir is not None :
        os.makedirs(cache_dir, exist_ok = True)
        cache_file = os.path.join(cache_dir, file_name + '.csv')
        if not os.path.isfile(cache_file) or is_expired(cache_file, file_name, api_version) :
            response = requests.get(url, stream = True)
            with open(cache_file, 'wb') as file :
                for line in response.iter_lines() :
                    file.write(line)
                    file.write(b'\n')

        with open(cache_file, 'rb') as file :
            while len(line := file.readline()) > 0 :
                yield line.rstrip(b'\r\n').decode('utf-8')

        return

    else :
        response = requests.get(url, stream = True)
        for line in response.iter_lines() :
            yield line.decode('utf-8')


def get_many(file_name: str,
             constructor: Type[T],
             api_version: ApiVersion,
             cache_dir: Optional[str]
             ) -> Iterator[T] :

    first_line = True
    for line in get_csv_lines(file_name, constructor, api_version, cache_dir) :
        if first_line :
            first_line = False
        elif len(line) > 0 :
            yield constructor(line.split(','))


def get_one(file_name: str,
            constructor: Type[T],
            api_version: ApiVersion,
            cache_dir: Optional[str]
            ) -> T :

    first_line = True
    for line in get_csv_lines(file_name, constructor, api_version, cache_dir) :
        if first_line :
            first_line = False
        elif len(line) > 0 :
            return constructor(line.split(','))

    raise Exception('Unable to load data.')


def bool_field(field: str) -> bool :
    return len(field) > 0


def int_field(field: str) -> int :
    if len(field) > 0 :
        return int(field)
    else :
        return -1


def float_field(field: str) -> float :
    if len(field) > 0 :
        return float(field)
    else :
        return -1.0


def date_field(field: str) -> Optional[date] :
    try :
        return date.fromisoformat(field)
    except ValueError :
        return None

