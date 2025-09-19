def test_get_current_positive(qa_auto_ctrl):
    response_current = qa_auto_ctrl.get_current().json()
    assert response_current['status'] == 'ok'

def test_get_current_negative(qa_auto_ctrl):
    response_current = qa_auto_ctrl.get_current(status_code=401, uses_cookies=False).json()

def test_get_current_some_feature(qa_auto_ctrl):
    response_current = qa_auto_ctrl.get_current().json()
    assert response_current['status'] == 'ok'


