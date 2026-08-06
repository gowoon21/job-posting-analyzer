from models import JobPosting
from parser import parse_job_posting


def main():
    posting = parse_job_posting()

    print(posting)
    parse_job_posting()


if __name__ == "__main__":
    main()