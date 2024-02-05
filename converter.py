import markdown
import sys

# python3 file-converter.py markdown inputfile outputfile
command = sys.argv[1]
in_file = sys.argv[2]
out_file = sys.argv[3]

if command == 'markdown':
    with open(in_file, encoding='utf-8') as f:
        md = f.read()
    output = markdown.Markdown(extensions=['tables']).convert(md)
    with open(out_file, 'w', encoding='utf-8') as f:
        f.write(output)