from models import JobPosting
from parser import parse_job_posting
from crawler import get_job_info


def main():
    posting = parse_job_posting()

    print(posting)


if __name__ == "__main__":
    main()