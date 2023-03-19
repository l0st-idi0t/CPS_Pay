import xlrd
import requests


def request_salaries():
    url = "https://www.cps.edu/about/finance/employee-position-files/"
    response = str(requests.get(url).content)

    #find most recent salary file
    filePos = response.find("globalassets/cps-pages/about-cps/finance/employee-position-files/")
    fileURL = "https://www.cps.edu/" + response[filePos : filePos + 100]
    fileName = response[filePos + 65 : filePos + 100]

    #download file
    r = requests.get(fileURL)
    with open(fileName, 'wb') as f:
        f.write(r.content)

    return fileName


def main():
    wb_file = request_salaries()
    wb = xlrd.open_workbook(wb_file)

    sheet = wb.sheet_by_index(0)


if __name__ == '__main__':
    main()