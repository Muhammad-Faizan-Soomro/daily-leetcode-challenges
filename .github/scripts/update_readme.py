import os
import datetime

README_FILE = "README.md"

def generate_table():
    files = [
        f for f in os.listdir('.') 
        if f.endswith('.py') and not f.startswith('.')
    ]
    files = [(f, os.path.getmtime(f)) for f in files]
    files.sort(key=lambda x: x[1])  # sort oldest → latest

    table = "| Day | Date | Problem # | Problem Name | Solution |\n"
    table += "|-----|------------|-----------|--------------|----------|\n"
    
    for idx, (f, mtime) in enumerate(files, start=1):
        problem_num, problem_name = f.replace(".py", "").split(". ", 1)
        date_str = datetime.datetime.fromtimestamp(mtime).strftime("%Y-%m-%d")
        table += f"| {idx} | {date_str} | {problem_num} | {problem_name} | [Code]({f}) |\n"
    return table

def update_readme():
    with open(README_FILE, "r") as f:
        content = f.read()

    table = generate_table()
    start_marker = "<!-- START_TABLE -->"
    end_marker = "<!-- END_TABLE -->"

    if start_marker in content and end_marker in content:
        before = content.split(start_marker)[0]
        after = content.split(end_marker)[1]
        new_content = f"{before}{start_marker}\n{table}\n{end_marker}{after}"
    else:
        # fallback if markers missing
        new_content = content + "\n\n" + table

    with open(README_FILE, "w") as f:
        f.write(new_content)

if __name__ == "__main__":
    update_readme()
