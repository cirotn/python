import git

# Get a reference to the repo
repo = git.Repo("..")

# Print out active branch
active_branch = repo.active_branch
print("Active branch: {}".format(active_branch))

# Get a list of last 10 commits
commits = list(repo.iter_commits(max_count=10))
print("Num commits: {}".format(len(commits)))

# Get commits in a range
commit_range =  "HEAD~{}..HEAD".format(len(commits)-1)
other_commits = list(repo.iter_commits(commit_range))
assert commits[0].hexsha == other_commits[0].hexsha

# Print some info on latest commit
summary = commits[0].summary
print("Last commit: {}".format(summary))
sha = str(commits[0].hexsha)
print("Last commit sha: {}".format(sha))
author = commits[0].author
print("Last commit author: {}".format(author))

# Checkout oldest commit
#repo.git.checkout(str(commits[-1].hexsha))

# Checkout master branch
#repo.git.checkout("master")
