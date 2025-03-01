import requests
from bs4 import BeautifulSoup


# price	area	bedrooms	bathrooms	stories	mainroad	guestroom	basement	hotwaterheating	airconditioning	parking	prefarea	furnishingstatus
# 13300000	7420	4	2	3	yes	no	no	no	yes	2	yes	furnished
# 12250000	8960	4	4	4	yes	no	no	no	yes	3	no	furnished
# 12250000	9960	3	2	2	yes	no	yes	no	no	2	yes	semi-furnished
# 12215000	7500	4	2	2	yes	no	yes	no	yes	3	yes	furnished
# 11410000	7420	4	1	2	yes	yes	yes	no	yes	2	no	furnished
# 10850000	7500	3	3	1	yes	no	yes	no	yes	2	yes	semi-furnished
# 10150000	8580	4	3	4	yes	no	no	no	yes	2	yes	semi-furnished
# 10150000	16200	5	3	2	yes	no	no	no	no	0	no	unfurnished
# 9870000	8100	4	1	2	yes	yes	yes	no	yes	2	yes	furnished

def get_data():
    url = "https://data.1337ai.org/"
    page = requests.get(url)
    soup = BeautifulSoup(page.content, 'html.parser')
    table = soup.find_all('table')[0]
    rows = table.find_all('tr')
    data = []
    for row in rows:
        cols = row.find_all('td')
        cols = [ele.text.strip() for ele in cols]
        data.append([ele for ele in cols if ele])
        # save the data in a file csv
        with open('data.csv', 'w') as f:
            f.write("price,area,bedrooms,bathrooms,stories,mainroad,guestroom,basement,hotwaterheating,airconditioning,parking,prefarea,furnishingstatus\n")
            for row in data:
                f.write(",".join(row
                                 ) + "\n")
    return data

if __name__ == '__main__':
    data = get_data()
    print("data scrapped successfully and saved in data.csv")