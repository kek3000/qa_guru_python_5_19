from pprint import pprint

import requests

api_url = 'https://reqres.in/api/'


def test_list_user_get():
    response = requests.get(f'{api_url}users?page=1')

    pprint(response.text)
    assert response.status_code == 200
    assert response.json()['total'] == 12


def test_single_user_get():
    response = requests.get(f'{api_url}users/7')

    pprint(response.text)
    assert response.status_code == 200
    assert response.json()['data']['id'] == 7
    assert response.json()['data']['email'] == 'michael.lawson@reqres.in'


def test_single_user_not_found_get():
    response = requests.get(f'{api_url}users/771231317')

    pprint(response.text)
    assert response.status_code == 404


def test_create_user_post():
    response = requests.post(
        url=f'{api_url}users/',
        json={
            "name": "Nikita",
            "job": "AQA"}
    )

    pprint(response.text)
    assert response.status_code == 201
    assert response.json()['name'] == 'Nikita'
    assert response.json()['job'] == 'AQA'


def test_update_user_put():
    response = requests.put(
        url=f'{api_url}users/123',
        json={
            "name": "Nikita",
            "job": "Team Lead QA"}
    )
    pprint(response.text)
    assert response.status_code == 200
    assert response.json()['name'] == 'Nikita'
    assert response.json()['job'] == 'Team Lead QA'


def test_update_user_patch():
    response = requests.patch(
        url=f'{api_url}users/123',
        json={
            "name": "Nikita",
            "job": "Team Lead QA"}
    )
    pprint(response.text)
    assert response.status_code == 200
    assert response.json()['name'] == 'Nikita'
    assert response.json()['job'] == 'Team Lead QA'


def test_update_user_delete():
    response = requests.delete(f'{api_url}users/123131231')

    pprint(response.text)
    assert response.status_code == 204


def test_register_user_successfull_post():
    response = requests.post(
        url=f'{api_url}register/',
        json={
            "email": "eve.holt@reqres.in",
            "password": "pistol"}
    )

    pprint(response.text)
    assert response.status_code == 200
    assert response.json()['id'] != ''
    assert response.json()['token'] != ''


def test_register_user_unsuccessfull_post():
    response = requests.post(
        url=f'{api_url}register/',
        json={
            "email": "n.alekseev@comagic.dev"}
    )

    pprint(response.text)
    assert response.status_code == 400
    assert response.json()['error'] == 'Missing password'


def test_login_user_successfull_post():
    response = requests.post(
        url=f'{api_url}login/',
        json={
            "email": "eve.holt@reqres.in",
            "password": "cityslicka"}
    )

    pprint(response.text)
    assert response.status_code == 200
    assert response.json()['token'] != ''


def test_login_user_unsuccessfull_post():
    response = requests.post(
        url=f'{api_url}login/',
        json={
            "email": "n.alekseev@comagic.dev"}
    )

    pprint(response.text)
    assert response.status_code == 400
    assert response.json()['error'] == 'Missing password'
