# @author yuliana morales
# as2-code-review
friends = []
userInfoDict = {}
postInfoDict = {}
def userInfo(user):
    global userInfoDict
    for line in user:
        li = line.strip().split(";")
        usrn = li[0]
        dspln = li[1]
        st = li[2]
        friends = li[3].strip("[]").split(",")
        # userInfoDict = dict(userName = usrn, displayName = dspln, state = st, friends = friends)
        userInfoDict[usrn] = [dspln, st, friends]
        # print(userInfoDict)

def postInfo(post):
    global postInfoDict
    for line in post:
        tokens = line.strip().split(";")
        postId = tokens[0]
        usrn = tokens[1]
        vsblity = tokens[2]
        postInfoDict[postId] = [usrn,vsblity]
        # postInfoDict = dict(postId = postId, username = usrn, visibility = vsblity)
        # print(postInfoDict)

# main
if __name__ == '__main__':
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
            try:
                with open(ufn) as userFile:
                    userInfo(userFile)
                with open(pfn) as postFile:
                    postInfo(postFile)

                print('loaded succesfully')
            except Exception as e:
                print('error ', e)
                break

        elif givenOption == 2:
            givenPostId = input('Input post ID: ')
            givenUsername = input('input username: ')
            # if userInfoDict and postInfoDict:
            if postInfoDict[givenPostId][1] == 'friend':
                # print(type(userInfoDict[postInfoDict[givenPostId][0]][2]))
                # check friend list of the post author given postId
                for token in userInfoDict[postInfoDict[givenPostId][0]][2]:
                    # print("ggiven", givenUsername, "TOKEN", token)
                    if token == givenUsername:
                        print("Output: Access Permitted")
                    else:
                        print("Output: Access Denied")
            elif postInfoDict[givenPostId][1] == 'public':
                print("Output: Access Permitted")
            else:
                print("Output: Access Denied")

        elif givenOption ==3:
            # retrive postts
            posts = ""
            gUsrn = input('input: ')
            for token in postInfoDict:
                if postInfoDict[token][0] == gUsrn:
                    posts += token + ", "
                elif postInfoDict[token][1] == 'friend':
                    for friend in userInfoDict[postInfoDict[token][0]][2]:
                        if friend == gUsrn:
                            posts += token + ", "
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
                if userInfoDict[user][1] == givenLoc.upper():
                    allUsers += userInfoDict[user][0] + ", "

            print("Output: ", allUsers)
        elif givenOption == 5:
            break
