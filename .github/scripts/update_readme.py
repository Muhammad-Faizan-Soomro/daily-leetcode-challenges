import os
import urllib.parse

README_FILE = "README.md"

def generate_table():
    files = [
        f for f in os.listdir('.') 
        if f.endswith('.py') and not f.startswith('.') and os.path.isfile(f)
    ]
    files.sort(key=lambda x: os.path.getmtime(x))  # oldest → latest

    table = "| Day | Problem # | Problem Name | Solution |\n"
    table += "|-----|-----------|--------------|----------|\n"
    
    for idx, f in enumerate(files, start=1):
        problem_num, problem_name = f.replace(".py", "").split(". ", 1)

        # Encode filename for valid Markdown link
        encoded_filename = urllib.parse.quote(f)

        table += f"| {idx} | {problem_num} | {problem_name} | [Code]({encoded_filename}) |\n"
    return table

def update_readme():
    with open(README_FILE, "r", encoding="utf-8") as f:
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

    with open(README_FILE, "w", encoding="utf-8") as f:
        f.write(new_content)

if __name__ == "__main__":
    update_readme()
