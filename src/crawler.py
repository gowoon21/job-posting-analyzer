import requests   # requests 파일 사용
from bs4 import BeautifulSoup   # bs4 패키지 안에 있는 BeautifulSoup 사용
from urllib.parse import urlparse, parse_qs


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


    # 모바일 사람인 페이지
    mobile_url = "https://m.saramin.co.kr/job-search/view"

    parsed_url = urlparse(url)
    query_parmas = parse_qs(parsed_url.query)

    rec_idx = query_parmas.get("rec_idx", [""])[0]

    mobile_params = {
        "rec_idx": rec_idx
    }

    mobile_response = requests.get(
        mobile_url,
        headers=headers,
        params=mobile_params
    )

    # 모바일 요청에 문제가 있으면 오류 발생
    mobile_response.raise_for_status()

    # 모바일 HTML 분석
    mobile_soup = BeautifulSoup(
        mobile_response.text,
        "html.parser"
    )


    # 공고 제목
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


    # 근무지역
    location = "장소명 없음"

    # 모바일 페이지의 전체 텍스트 확인
    page_text = mobile_soup.get_text(" ", strip=True)

    #지역명 목록
    regions = [
        "서울", "경기", "인천", "부산", "대구",
        "광주", "대전", "울산", "세종",
        "강원", "충북", "충남", "전북", "전남",
        "경북", "경남", "제주"
    ]

    for text in mobile_soup.stripped_strings:
        for region in regions:
            if text.startswith(region):
                # 상세주소가 아닌 짧은 지역 정보만 선택
                if len(text) < 30:
                    location = text
                    break

        if location != "장소명 없음":
            break


    return company_name, job_title, location


if __name__ == "__main__":
    url = "https://www.saramin.co.kr/zf_user/jobs/relay/view?view_type=search&rec_idx=54679793&location=ts&searchword=python&searchType=recently&paid_fl=n&search_uuid=80fc6306-c96c-4423-96de-9683daf616bf&t_ref=search&t_ref_content=generic#seq=0"

    company_name, job_title, location = get_job_info(url)

    print(company_name)
    print(job_title)
    print(location)