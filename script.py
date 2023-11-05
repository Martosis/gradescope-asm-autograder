import gradescope_utils
import assembly_utils
from vars import url, answers, assembly

table = gradescope_utils.get_zero_table(url)

for index, row in table.iterrows():
    try:
        url = row.iloc[-1]
        grade_page = gradescope_utils.request_gradescope(url)
        
        answer, rubric_ids, csrf = gradescope_utils.parse_grade_page(grade_page)

        if assembly:
            answer = assembly_utils.process_answer(answer)

        if answer in answers:
            gradescope_utils.mark_correct(url, rubric_ids, csrf)
    except:
        pass