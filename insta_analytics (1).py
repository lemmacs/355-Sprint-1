import re

def extract_usernames_from_html(html_text):
    pattern = r'https://www\.instagram\.com/([^/"]+)'
    usernames = re.findall(pattern, html_text)
    return usernames

def follow_requests(pending_requests):
    requests = [user for user in pending_requests]
    return requests

def find_users_dont_folllow_back(following, followers):
    dontFollowBacks = [user for user in followers if user not in following]
    return dontFollowBacks

def find_unfollowers(followers, following):
    unfollowers = [user for user in following if user not in followers]
    return unfollowers

# Read content from 'following.html' and 'followers_1.html'
if __name__ == "__main__":
    print("Please make sure to attach the following files to your folder before running"  + '\n' + 'followers_1.html' + '\n' + 'following.html' + '\n' + 'pending_follow_request')
    try:
        with open('following.html', 'r', encoding='utf-8') as following_file:
            following_text = following_file.read()
        
        with open('followers_1.html', 'r', encoding='utf-8') as followers_file:
            followers_text = followers_file.read()
        
        with open('pending_follow_requests.html', 'r', encoding='utf-8') as pending_requests_file:
            pending_request_text = pending_requests_file.read()
    except Exception as e:
        print("Please make sure to add the 3 corresponding files to the folder before running")
        
    # Extract usernames from HTML contents
    followers = extract_usernames_from_html(followers_text)
    following = extract_usernames_from_html(following_text)
    pending_requests = extract_usernames_from_html(pending_request_text)
    username = input("Please enter your username: ")
    
    userResponse = input("What would you like to see? " + "\n" + 'A = Users not following you back' + "\n" + "B = Users you don't follow back" + "\n" + 
    "C = Pending requests" + "\n" ).lower()
    if userResponse == 'a':
        # Find unfollowers 
        unfollowers = find_unfollowers(followers, following)
        print(username + " these users aren't following you back")
        for unfollower in unfollowers :
            print(unfollower)
    elif userResponse == 'b':
        dontFollowBacks = find_users_dont_folllow_back(following, followers)
        print(username + " these users you don't follow back")
        for dontFollowBack in dontFollowBacks:
            print(dontFollowBack)
    elif userResponse == 'c':
        requests = follow_requests
        print(username + " these users haven't declined or accepted your follow request")
        for pending_request in pending_requests:
            print(pending_request)
    else:
        print("Please enter a valid response")
        
