

# test-case valid params
import requests
import pytest
def test_search_valid_movie():
    # base_url
    base_url = "https://www.omdbapi.com/"

    # params
    api_key = "23f82659"
    s = "matrix"

    # url
    url = f"{base_url}?apikey={api_key}&s={s}"

    # send requests
    response = requests.get(url)

    # фактического результат
    status_code, response_result = response.status_code, response.json()['Response']

    # expected result
    expected_status_code = range(200, 400)
    expected_response_result = "True"

    # проверка совпадения наших ожиданий и фактического результат
    assert (status_code in expected_status_code) and response_result == expected_response_result

