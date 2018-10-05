from datetime import datetime, timedelta
import random
import os
import shutil
import subprocess

source = 'git@github.com'

def roundTime(dt=None, roundTo=60):
   """
   https://stackoverflow.com/questions/3463930/how-to-round-the-minute-of-a-datetime-object-python/10854034#10854034
   """
   if dt == None:
      dt = datetime.datetime.now()
   seconds = (dt.replace(tzinfo=None) - dt.min).seconds
   rounding = (seconds+roundTo/2) // roundTo * roundTo
   return dt + timedelta(0, rounding-seconds, -dt.microsecond)


def fake_commit(user,repo,days):

    beginning = """#!/usr/bin/env bash
                    REPO={0}
                    git init $REPO
                    cd $REPO
                    touch README.md
                    git add README.md
                    touch pharzan_fake_commit
                    git add pharzan_fake_commit
                """.format(repo)
    ending = """
            git remote add origin {0}:{1}/$REPO.git
            git pull origin master
            git push -u origin master
            """.format(source,user)
    lines = []
    lines.append(beginning)
    
    commitdate = datetime.today()

    for i in range(days):
        rnd = random.randint(1, 20)
        commitdate = roundTime(
            datetime.today() - timedelta(days=i), roundTo=60*60)
        for j in range(rnd):
            template = '''GIT_AUTHOR_DATE={0} GIT_COMMITTER_DATE={1} git commit --allow-empty -m "pharzan" > /dev/null\n'''.format(commitdate.isoformat(), commitdate.isoformat())
            lines.append(template)

    lines.append(ending)
    with open('commits.sh', 'w') as f:
        for line in lines:
            f.write(line)
    os.chmod('commits.sh', 0o755)

def main():
    username = input("Enter Username: ")
    repo = input('Enter repository name to fake commits: ')
    days = int(input('Enter number of days to go back in time: '))
    
    fake_commit(username, repo, days)
    subprocess.call(['./commits.sh'])

if __name__ == '__main__':
    main()
