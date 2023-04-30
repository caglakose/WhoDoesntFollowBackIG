from bs4 import BeautifulSoup

# Open the followers.html file
with open('followers.html', 'r') as f:
    followers_html = f.read()

# Open the following.html file
with open('following.html', 'r') as f:
    following_html = f.read()

# Parse the HTML files using BeautifulSoup
followers_soup = BeautifulSoup(followers_html, 'html.parser')
following_soup = BeautifulSoup(following_html, 'html.parser')

# Get a list of usernames and their follow dates for your followers
followers_list = []
for div in followers_soup.find_all('div', {'class': '_a6-p'}):
    username = div.find_all('a')[0].text
    follow_date = div.find_all('div')[1].text
    followers_list.append({'username': username, 'follow_date': follow_date})

# Get a list of usernames and their follow dates for accounts you are following
following_list = []
for div in following_soup.find_all('div', {'class': '_a6-p'}):
    username = div.find_all('a')[0].text
    follow_date = div.find_all('div')[1].text
    following_list.append({'username': username, 'follow_date': follow_date})

# Find accounts that are not following you back
not_following_back = set([d['username'] for d in following_list]) - set([d['username'] for d in followers_list])

# Print the results
print('Accounts that are not following you back:')
for account in not_following_back:
    print(account)
