from models import JobPosting


def parse_job_posting():
    print("채용공고를 불러옵니다.")

    return JobPosting(
        company_name= "OpenAI",       #회사 이름
        job_title= "Python Developer",          #직무
        location= "Seoul",           #지역
        employment_type= "정규직",    #고용 형태
        experience= "신입",         #경력
        education= "학력 무관",          #학력
        salary= "연봉 협의",             #급여
        tech_stacks=["Python", "FastAPI"],        #기술 스택
        preferred_qualifications=["Git 사용 경험"]       #우대사항
    )