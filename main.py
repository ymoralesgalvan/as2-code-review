# @author yuliana morales
# as2-code-review
friends = []
userInfoDict = {}
postInfoDict = {}
def userInfo(user):
    global userInfoDict
    for line in user:
        # strip for whitespaces then split
        li = line.strip().split(";")
        usrn = li[0]
        dspln = li[1]
        st = li[2]
        # strip for [] in friends list then sep by comma
        friends = li[3].strip("[]").split(",")
        # userInfoDict = dict(userName = usrn, displayName = dspln, state = st, friends = friends)
        # key is username and values in list
        userInfoDict[usrn] = [dspln, st, friends]
        # print(userInfoDict)

def postInfo(post):
    global postInfoDict
    for line in post:
        # strip for whitespace then split
        tokens = line.strip().split(";")
        postId = tokens[0]
        usrn = tokens[1]
        vsblity = tokens[2]
        # key as post id and values in list
        postInfoDict[postId] = [usrn,vsblity]
        # postInfoDict = dict(postId = postId, username = usrn, visibility = vsblity)
        # print(postInfoDict)

# main
if __name__ == '__main__':
    # consists of 1, 2, 3, 4, 5.using range to not type all numbers
    options = range(1,6)
    while True:
        givenOption = int(input(
            'enter a number:(1.) load data (2.) check visibility (3.) retrieve posts (4.) search users (5.) terminate : '))
        if givenOption not in options:
            print('enter a valid option. 1-5')
            continue;
        elif(givenOption == 1):
            ufn = input('Enter user file path: ')
            pfn = input('enter post file path: ')
            # open files with given paths, using with to close
            try:
                with open(ufn) as userFile:
                    userInfo(userFile)
                with open(pfn) as postFile:
                    postInfo(postFile)
                # confirmation message 
                print('loaded succesfully')
            except Exception as e:
                print('error ', e)
                break

        elif givenOption == 2:
            # check visibility
            givenPostId = input('Input post ID: ')
            givenUsername = input('input username: ')
            # if userInfoDict and postInfoDict:
            # postinfo dictionary[ postId]: username[0], visibility[1]
            if postInfoDict[givenPostId][1] == 'friend':
                # print(type(userInfoDict[postInfoDict[givenPostId][0]][2]))
                # check friend list of the post author given postId
                # traverse userinfo dictionary (friend list)
                for token in userInfoDict[postInfoDict[givenPostId][0]][2]:
                    # print("ggiven", givenUsername, "TOKEN", token)
                    if token == givenUsername:
                        print("Output: Access Permitted")
                    else:
                        print("Output: Access Denied")
            # if post is public
            elif postInfoDict[givenPostId][1] == 'public':
                print("Output: Access Permitted")
            else:
                print("Output: Access Denied")

        elif givenOption ==3:
            # retrive postts
            posts = ""
            gUsrn = input('input: ')
            for token in postInfoDict:
                # if the author is usrname,visibility is true
                if postInfoDict[token][0] == gUsrn:
                    posts += token + ", "
                # if post visibility == friend
                elif postInfoDict[token][1] == 'friend':
                    # traverse friend list from user dict given username from post dict
                    for friend in userInfoDict[postInfoDict[token][0]][2]:
                        if friend == gUsrn:
                            posts += token + ", "
                # check if post if public, visibility true for every user
                elif postInfoDict[token][1] == 'public':
                    posts += token + ", "
                # if len(posts) > 1:
                #     posts += ", "
            print("Output: ", posts)

        elif givenOption ==4:
            # search by location
            allUsers = ""
            givenLoc = input('Input: ')
            for user in userInfoDict:
                # check where users location is given location
                # compare given location to uppercase
                if userInfoDict[user][1] == givenLoc.upper():
                    allUsers += userInfoDict[user][0] + ", "
            # string with all users
            print("Output: ", allUsers)
        elif givenOption == 5:
            break
