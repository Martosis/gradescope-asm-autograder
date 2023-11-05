import re

def process_answer(answer):
    answer = answer.replace(",", " ").strip()
    answer = re.sub(r'\s+', ' ', answer)
    return re.sub(vars.NEGATIVE_ZERO, '', re.sub(vars.BASE_AND_COMMENT, '', answer).upper())