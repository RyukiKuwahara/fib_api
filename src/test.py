import sys
from main import app

def test_fibonacci():
    client = app.test_client()

    # test1 （正常）
    response = client.get('/fib?n=10', headers={'Content-Type': 'application/json'})
    assert response.status_code == 200
    result = response.get_json()["result"]
    assert result == 55

    # test2 (サンプル入力１（正常）)
    response = client.get('/fib?n=99', headers={'Content-Type': 'application/json'})
    assert response.status_code == 200
    result = response.get_json()["result"]
    assert result == 218922995834555169026

    # test3（異常パラメータ）
    response = client.get('/fib?n=-1', headers={'Content-Type': 'application/json'})
    assert response.status_code == 400

    # test4（異常パラメータ）
    response = client.get('/fib?n=hoge', headers={'Content-Type': 'application/json'})
    assert response.status_code == 400

    # test5（異常パラメータ）
    response = client.get('/fib?n=0', headers={'Content-Type': 'application/json'})
    assert response.status_code == 400

    # test6（異常ヘッダー）
    response = client.get('/fib?n=1')
    assert response.status_code == 415

if __name__ == "__main__":
    test_fibonacci()
