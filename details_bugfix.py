import subprocess

# Read the log file
with open('./log_bugfix.txt', 'r',encoding='utf-16 le') as log_file:
    log_content = log_file.read()

# Split the log content into individual commits
commits = log_content.split('\n\n')

# Open a file for writing the output
output_file_name = 'output_bugfix_detail.txt'
with open(output_file_name, 'w') as output_file:
    # Iterate through each commit
    for commit in commits:
        # Split the commit into lines
        commit_lines = commit.split('\n', 1)  # Split only at the first newline

        # Extract the commit SHA value
        commit_info = commit_lines[0].split()
        if len(commit_info) >= 2 and commit_info[0] == 'commit':
            commit_sha = commit_info[1]
            print(f'Processing commit {commit_sha}')

            # Use git show to get commit information
            git_show_output = subprocess.check_output(['git', 'show', commit_sha], universal_newlines=True)

            # Write the git show output to the output file
            output_file.write(f'Git show output for commit {commit_sha}:\n')
            output_file.write(git_show_output)
            output_file.write('\n' + '-' * 80 + '\n')  # Separating commits
        else:
            print(f'Skipping invalid commit: {commit_lines[0]}')

print(f'Git show outputs written to {output_file_name}')
