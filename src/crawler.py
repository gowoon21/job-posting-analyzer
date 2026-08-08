import requests   #requests 파일 사용
from bs4 import BeautifulSoup   #bs4 패키지 안에 있는 BeautifulSoup 사용하겠다

def get_job_info(url):
    response = requests.get(url)
    # requests.get(url) : 해당 url에 get 요청을 보내는 코드

    soup = BeautifulSoup(response.text, "html.parser")
    # response.text : 서버에서 받은 HTML 내용을 문자열로 꺼냄
    # BeautifulSoup(..., "html.parser") : 그 HTML을 Python이 다루기 쉽게 분석함

    job_title = soup.find("h2").get_text(strip=True)
    # HTML에서 첫 번째 <h2>를 찾아서 job_title에 저장

    location_text = soup.find(string=lambda text: text and "Technical Success - Seoul, South Korea" in text)
    # 텍스트 중에 "Seoul"이 들어간 첫 번째 문자열을 찾는 방식
    # find_all() : 조건에 맞는 모든 요소를 찾음
    
    location = location_text.split(" - ")[1]
    # 문자열을 " - " 기준으로 나눔
    
    return job_title, location


if __name__ == "__main__":
    url = "https://openai.com/careers/ai-deployment-engineer-seoul-south-korea/"
    #접속하고 싶은 웹페이지 주소 저장 변수

    job_title, location = get_job_info(url)

    print(job_title)
    print(location)

