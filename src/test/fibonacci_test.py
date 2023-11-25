import sys
sys.path.append("./src")
from main import app


def test_fibonacci():
    client = app.test_client()

    #test1 (サンプル入力１（正常）)
    response = client.get('/fib?n=99')
    assert response.status_code == 200
    result = response.get_json()["result"]
    assert result == 218922995834555169026

    #test2（異常パラメータ）
    response = client.get('/fib?n=-1')
    assert response.status_code == 400

    #test2（異常パラメータ）
    response = client.get('/fib?n=hoge')
    assert response.status_code == 400

    #test3（異常パラメータ）
    response = client.get('/fib?n=0')
    assert response.status_code == 400

if __name__ == "__main__":
    test_fibonacci()

