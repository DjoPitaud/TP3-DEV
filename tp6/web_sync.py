from sys import exit as sysexit, argv

from get_content import get_content
from write_content import write_content



def main():

    if not argv[1]:
        print("You must input a url(https://www.example.com)")
        sysexit(1)
    
    url = argv[1]
    output_file = "/tmp/web_page"

    content = get_content(url)
    write_content(content, output_file)
    
if __name__ == "__main__":
    main()