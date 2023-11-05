cookies = {
    "_gradescope_session": "",
    "signed_token": "",
}

url = "/courses/581622/questions/28905257/submissions"
answers = ["LDR R3 R3 0"]
assembly = True

GRADESCOPE_URL="https://www.gradescope.com"

NEGATIVE_ZERO=r'-(?=0*$)'
BASE_AND_COMMENT=r'[#xb](?=\d+(?:;|$)|-\d+(?:;|$))|;.*$'

DEFAULT_POST_DATA={'rubric_items': {}, "question_submission_evaluation":{"points":None,"comments":None}}
POST_HEADERS={"X-Csrf-Token":None,"Referer":None,"Content-Type":"application/json","Origin":"https://www.gradescope.com","Sec-Fetch-Site":"same-origin","Sec-Fetch-Mode":"cors","Sec-Fetch-Dest":"empty","X-Requested-With":"XMLHttpRequest","Accept":"application/json, text/javascript, */*; q=0.01"}