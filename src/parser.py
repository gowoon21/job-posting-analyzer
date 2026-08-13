from .crawler import get_job_info
from .models import JobPosting


def parse_job_posting():
    url = "https://www.saramin.co.kr/zf_user/jobs/relay/view?view_type=search&rec_idx=54679793&location=ts&searchword=python&searchType=recently&paid_fl=n&search_uuid=80fc6306-c96c-4423-96de-9683daf616bf&t_ref=search&t_ref_content=generic#seq=0"

    company_name, job_title, location = get_job_info(url)

    return JobPosting(
        company_name= company_name,                  #회사 이름
        job_title= job_title,                       #직무
        location= location,                         #지역
        employment_type= "정규직",                   #고용 형태
        experience= "경력",                          #경력
        education= "학력 무관",                      #학력
        salary= "연봉 협의",                         #급여
        tech_stacks=["Python"],                     #기술 스택
        preferred_qualifications=[]                 #우대사항
    )