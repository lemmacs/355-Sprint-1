print('Please make sure to attach the following files to your folder before running:')
print("- following.html")
print("- followers_1.html")
print("- pending_follow_requests.html")
# import statement
import re

# Function to extract Instagram usernames from HTML content
def get_usernames(htmlContent):
    pattern = r'https://www\.instagram\.com/([^/"]+)'
    allUsernames = re.findall(pattern, htmlContent)
    return allUsernames

# Function to get a list of usernames from pending follow requests
def follow_requests(pending_requests):
    requestUsernames = [username for username in pending_requests]
    return requestUsernames

# Function to find users who don't follow back
def find_users_dont_folllow_back(list_of_following, list_of_followers):
    dontFollowBackUsernames = [username for username in list_of_followers if username not in list_of_following]
    return dontFollowBackUsernames

# Function to identify unfollowers
def identify_unfollowers(list_of_followers, list_of_following):
    unfollowerUsernames = [username for username in list_of_following if username not in list_of_followers]
    return unfollowerUsernames

if __name__ == "__main__":
    try:
        # Read HTML files containing followers, following, and pending follow requests
        with open('following.html', 'r', encoding='utf-8') as following_text:
            following_data = following_text.read()
        
        with open('followers_1.html', 'r', encoding='utf-8') as followers_text:
            followers_data = followers_text.read()
        
        with open('pending_follow_requests.html', 'r', encoding='utf-8') as pending_requests_file:
            pending_request_text = pending_requests_file.read()
    except Exception as e:
        print("Please make sure to add the 3 corresponding files to the folder before running")
    
    # Get usernames from the HTML files
    following = get_usernames(following_data)
    followers = get_usernames(followers_data)
    pending_requests = get_usernames(pending_request_text)
    username = input("Please enter your username: ")
    
    # Prompt user for desired action
    userResponse = input("What would you like to see? " + "\n" + 'A = Users not following you back' + "\n" + "B = Users you don't follow back" + "\n" + 
    "C = Pending requests" + "\n" ).lower()
    
    # Display results based on user response
    if userResponse == 'a':
        unfollowers = identify_unfollowers(followers, following)
        print(username + " these users aren't following you back")
        for username in unfollowers :
            print(username)
    elif userResponse == 'b':
        dontFollowBacks = find_users_dont_folllow_back(following, followers)
        print(username + " these users you don't follow back")
        for username in dontFollowBacks:
            print(username)
    elif userResponse == 'c':
        requests = follow_requests
        print(username + " these users haven't declined or accepted your follow request")
        for username in pending_requests:
            print(username)
    else:
        print("Please enter a valid response")
