import requests   # requests 파일 사용
from bs4 import BeautifulSoup   # bs4 패키지 안에 있는 BeautifulSoup 사용


def get_job_info(url):
    # 브라우저에서 접속하는 것처럼 User-Agent 정보를 함께 보냄
    headers = {
        "User-Agent": "Mozilla/5.0"
    }

    # URL에 GET 요청을 보내 HTML을 받아옴
    response = requests.get(url, headers=headers)
    # 요청에 문제가 있으면 오류 발생
    response.raise_for_status()

    # 받아온 HTML을 BeautifulSoup으로 분석
    soup = BeautifulSoup(response.text, "html.parser")

    #공고 제목
    # 사람인 페이지의 title 태그 찾기
    title_tag = soup.find("title")

    if title_tag:
        # title 태그 안의 글자만 가져옴
        title_text = title_tag.get_text(strip=True)

        # 회사명 추출
        company_name = title_text.split("]", 1)[0].replace("[", "").strip()

        # 공고 제목 추출
        # 회사명 부분 제거
        job_title = title_text.split("] ", 1)[1]
        # "(D-55) - 사람인" 부분 제거
        job_title = job_title.rsplit("(D-", 1)[0].strip()

    else:
        company_name = "회사명 없음"
        job_title = "직무명 없음"

    # 근무지역은 아직 사람인 방식으로 수정하지 않았음
    location = "장소명 없음"

    # 페이지에 잇는 모든 <dt> 찾음
    dt_tags = soup.find_all("dt")

    for dt in dt_tags:
        # 그중 글자가 '근무지역'인 걸 찾음
        if dt.get_text(strip=True) == "근무지역":
            # 바로 옆에 있는 <dd> 가져와라
            dd = dt.find_next_sibling("dd")

            if dd:
                location = dd.get_text(" ", strip=True)
                location = location.replace("지도보기", "").strip()

            break

    return company_name, job_title, location


if __name__ == "__main__":
    url = "https://www.saramin.co.kr/zf_user/jobs/relay/view?rec_idx=54672562"

    company_name, job_title, location = get_job_info(url)

    print(company_name)
    print(job_title)
    print(location)