import requests, smtplib, datetime
from bs4 import BeautifulSoup
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

now = datetime.datetime.now()

content = ''


# Extract the Hacker News Stories
def extract_news(url):
    print('Extracting Hacker News Stories...')
    cnt = ''
    cnt += ('<b>HN Top StoriesL </b>\n' + '<br>' + '-' * 50 + '<br>')
    response = requests.get(url)  # Getting the content of the url
    content = response.content
    soup = BeautifulSoup(content, 'html.parser')
    for i, tag in enumerate(soup.find_all('td', attrs={'class': 'title', 'valign': ''})):
        cnt += ((str(i + 1) + ' :: ' + tag.text + '\n' + '<br>') if tag.text != 'More' else '')
    return cnt


cnt = extract_news('https://news.ycombinator.com/')
content += cnt
content += ('<br>------<br>')
content += ('<br><br>End of Message')

# Email authentication
