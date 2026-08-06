from dataclasses import dataclass, field

@dataclass
class JobPosting:           #채용공고 설계도
    company_name: str       #회사 이름
    job_title: str          #직무
    location: str           #지역
    employment_type: str    #고용 형태
    experience: str         #경력
    education: str          #학력
    salary: str             #급여
    tech_stacks: list[str] = field(default_factory=list)        #기술 스택
    preferred_qualifications: list[str] = field(default_factory=list)       #우대사항
