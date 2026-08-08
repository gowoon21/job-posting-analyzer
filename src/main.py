from .parser import parse_job_posting
#.을 붙이는 이유는 같은 src 패키지 안의 parser.py를 불러오겠다는 뜻


def main():
    posting = parse_job_posting()
    print(posting)


if __name__ == "__main__":
    main()