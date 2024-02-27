4. Git tags and releases 
Write command to create light weight git tag named "v1.0" for a commit in your local repositorys


Tags are a simple aspect of Git, they allow you to identify specific release versions of your code. You can think of a tag as a branch that doesn't change. Once it is created, it loses the ability to change the history of commits.

Annotated tags store extra metadata such as author name, release notes, tag-message, and date as full objects in the Git database. All this data is important for a public release of your project.


-bash
git tag v1.0
#makes a lightweight tag of name v1.0

git tag -a v1.0
#makes an Annotated tag of version 1.0.0 with no message

git tag -a v1.0.1 -m "This message will be displayed along with the tag!"
#version v1.0.1 created along with the message.

to see a specific version, we use the following command:
-bash
git show v1.0.1
#this command shows us the details of the tag along with the message.

output:
PS C:\Users\Hp\OneDrive\Desktop\github> git tag -a v2.3.3 -m "THis is a test etag "
PS C:\Users\Hp\OneDrive\Desktop\github> git show v2.3.3
tag v2.3.3
Tagger: Ashish Goswami <ashisgoswami6298@gmail.com>
Date:   Tue Jan 27 12:38:23 2024 +0530

THis is a test etag

commit fc32526c88e4cbd11514d5d07ee6428262f6c1bf (HEAD -> main, tag: v2.3.3, tag: v1.0.1, tag: v1.0.0, origin/main, origin/HEAD)
