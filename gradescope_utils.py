import requests
import pandas as pd
import bs4 as bs
import numpy as np
import html
import json
import vars
from io import StringIO

cookies = vars.cookies

def request_gradescope(url):
    res = requests.get(
        vars.GRADESCOPE_URL + url,
        cookies=cookies
    )
    return res

def mark_correct(url, rubric_ids, csrf):
    data = vars.DEFAULT_POST_DATA

    for id in rubric_ids:
        data['rubric_items'].update({id: {"score": False}})

    data['rubric_items'].get(rubric_ids[0])['score'] = True

    headers = vars.POST_HEADERS
    headers['X-Csrf-Token'] = csrf
    headers['Referer'] = url

    requests.post(vars.GRADESCOPE_URL + url[0:-6] + "/save_grade", json=data, cookies=cookies, headers=headers)

def get_zero_table(url):
    response = request_gradescope(url)

    soup = bs.BeautifulSoup(response.content, "lxml")
    table = soup.findAll("table")[0]

    df = pd.read_html(StringIO(str(table)),encoding='utf-8', header=0)[0]
    df['href'] = pd.Series([np.where(tag.has_attr('href'),tag.get('href'),"no link") for tag in table.find_all('a') if '?' not in tag.get("href")])

    zero_scored = df.loc[df["Score"] == 0]
    return zero_scored.astype({"href":"str"})

def parse_grade_page(page):
    soup = bs.BeautifulSoup(page.content, "lxml")
    
    props = soup.findAll("div", {"data-react-class": "SubmissionGrader"})[0].get("data-react-props")
    props = html.unescape(props)
    props = json.loads(props)

    answer = props["submission"]["answers"]["0"]

    rubric_items = props["rubric_items"]
    rubric_ids = []

    for dict in rubric_items:
        rubric_ids.append(dict["id"])
    
    csrf = soup.select_one('meta[name="csrf-token"]')['content']
    
    return (answer, rubric_ids, csrf)