from .models import JobPosting
from .crawler import get_job_info


def parse_job_posting():
    print("채용공고를 불러옵니다.")

    url = "https://openai.com/careers/ai-deployment-engineer-seoul-south-korea/"

    job_title, location = get_job_info(url)

    return JobPosting(
        company_name= "OpenAI",                     #회사 이름
        job_title= job_title,              #직무
        location= location,                          #지역
        employment_type= "정규직",                   #고용 형태
        experience= "경력",                          #경력
        education= "학력 무관",                      #학력
        salary= "연봉 협의",                         #급여
        tech_stacks=["Python"],                     #기술 스택
        preferred_qualifications=[]                 #우대사항
    )