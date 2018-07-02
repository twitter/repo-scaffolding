#!/usr/bin/env python3

"""
Copyright 2018 Twitter, Inc.
Licensed under the Apache License, Version 2.0
http://www.apache.org/licenses/LICENSE-2.0
"""

"""
This script can be used to add license headers to all the source files of a project.
It is designed to be safe, so do not worry and try it out!

Works with languages with nonempty value in MAP_LANGUAGE_TO_COMMENT_CHARS

"""


import argparse
import datetime
import itertools
import os
import sys


"""
The License Header
"""
LICENSE_HEADER = """
Copyright {} Twitter, Inc.
Licensed under the Apache License, Version 2.0
http://www.apache.org/licenses/LICENSE-2.0
""".format(datetime.datetime.now().year).split("\n")


MAP_EXTENTION_TO_LANGUAGE = \
    {
        '.C': 'C++',
        '.H': 'C++',
        '.PL': 'Perl',
        '.R': 'R',
        '._js': 'JavaScript',
        '.adb': 'Ada',
        '.apacheconf': 'ApacheConf',
        '.applescript': 'AppleScript',
        '.asm': 'Assembly',
        '.asp': 'ASP',
        '.aux': 'TeX',
        '.aw': 'PHP',
        '.b': 'Brainfuck',
        '.bas': 'Visual Basic',
        '.bats': 'Shell',
        '.bf': 'Brainfuck',
        '.bib': 'TeX',
        '.builder': 'Ruby',
        '.c': 'C',
        '.c++': 'C++',
        '.clj': 'Clojure',
        '.cmake': 'CMake',
        '.coffee': 'CoffeeScript',
        '.cpp': 'C++',
        '.cs': 'C#',
        '.css': 'CSS',
        '.csx': 'C#',
        '.ctp': 'PHP',
        '.cu': 'Cuda',
        '.cxx': 'C++',
        '.dfm': 'Pascal',
        '.diff': 'Diff',
        '.dtx': 'TeX',
        '.el': 'Emacs Lisp',
        '.elm': 'Elm',
        '.emacs': 'Emacs Lisp',
        '.erb': 'HTML+ERB',
        '.f': 'FORTRAN',
        '.f90': 'FORTRAN',
        '.frm': 'Visual Basic',
        '.frx': 'Visual Basic',
        '.gemspec': 'Ruby',
        '.go': 'Go',
        '.god': 'Ruby',
        '.gyp': 'Python',
        '.h++': 'C++',
        '.hh': 'C++',
        '.hpp': 'C++',
        '.hs': 'Haskell',
        '.hsc': 'Haskell',
        '.htm': 'HTML',
        '.html': 'HTML',
        '.http': 'HTTP',
        '.hxx': 'C++',
        '.ino': 'Arduino',
        '.ins': 'TeX',
        '.io': 'Io',
        '.irbrc': 'Ruby',
        '.java': 'Java',
        '.jinja': 'HTML+Django',
        '.jl': 'Julia',
        '.js': 'JavaScript',
        # '.json': 'JSON',
        '.jsp': 'Java Server Pages',
        '.jsx': 'JavaScript',
        '.kt': 'Kotlin',
        '.ktm': 'Kotlin',
        '.kts': 'Kotlin',
        '.less': 'Less',
        '.lisp': 'Common Lisp',
        '.ll': 'LLVM',
        '.lpr': 'Pascal',
        '.ltx': 'TeX',
        '.lua': 'Lua',
        '.m': 'Objective-C',
        '.mak': 'Makefile',
        '.matlab': 'Matlab',
        # '.md': 'Markdown',
        '.mkii': 'TeX',
        '.mkiv': 'TeX',
        '.mkvi': 'TeX',
        '.ml': 'OCaml',
        '.mm': 'Objective-C',
        '.mspec': 'Ruby',
        '.mustache': 'HTML+Django',
        # '.nginxconf': 'Nginx',
        '.nqp': 'Perl',
        '.numpy': 'NumPy',
        '.pas': 'Pascal',
        '.perl': 'Perl',
        '.ph': 'Perl',
        '.php': 'PHP',
        '.php3': 'PHP',
        '.php4': 'PHP',
        '.php5': 'PHP',
        '.phpt': 'PHP',
        '.phtml': 'HTML+PHP',
        '.pl': 'Perl',
        '.plx': 'Perl',
        '.pm6': 'Perl',
        '.pod': 'Perl',
        '.podspec': 'Ruby',
        '.prg': 'xBase',
        '.psgi': 'Perl',
        '.py': 'Python',
        '.pyt': 'Python',
        '.pytb': 'Python traceback',
        '.pyw': 'Python',
        '.pyx': 'Cython',
        '.r': 'R',
        '.rb': 'Ruby',
        '.rbuild': 'Ruby',
        '.rbw': 'Ruby',
        '.rbx': 'Ruby',
        # '.rest': 'reStructuredText',
        '.rs': 'Rust',
        # '.rst': 'reStructuredText',
        '.ru': 'Ruby',
        '.sage': 'Sage',
        '.sass': 'Sass',
        '.scala': 'Scala',
        '.scss': 'SCSS',
        '.sh': 'Shell',
        '.sql': 'SQL',
        '.sty': 'TeX',
        '.tcc': 'C++',
        '.tex': 'TeX',
        '.thor': 'Ruby',
        '.tmux': 'Shell',
        '.toc': 'TeX',
        '.tpp': 'C++',
        '.ts': 'TypeScript',
        '.vb': 'Visual Basic',
        '.vba': 'Visual Basic',
        '.vbs': 'Visual Basic',
        '.vim': 'VimL',
        '.w': 'C',
        '.watchr': 'Ruby',
        '.wsgi': 'Python',
        '.xhtml': 'HTML',
        # '.xml': 'XML',
        '.xpy': 'Python',
        # '.yaml': 'YAML',
        # '.yml': 'YAML',
    }

"""
The keys in MAP_LANGUAGE_TO_COMMENT_CHARS make an exhaustive list of the values in MAP_EXTENTION_TO_LANGUAGE.
Please keep both of them in sync.

The values in the list are the characters used to prepare the License Header as a comment block.

First elemenet starts a block comment
Second element is prepended to the lines in comment body
Third element ends a block comment

EXAMPLE (Scala): For a comment like below

/**
 * A
 * block
 * comment
 */

Set the following in MAP_LANGUAGE_TO_COMMENT_CHARS

'Scala': ['/**', ' * ', ' */']
"""
MAP_LANGUAGE_TO_COMMENT_CHARS = \
    {
        'ASP': ['', '\' ', ''],
        'Ada': [], # TODO
        'ApacheConf': [], # TODO
        'AppleScript': ['', '-- ', ''],
        'Arduino': [], # TODO
        'Assembly': ['', '; ', ''],
        'Brainfuck': [], # TODO
        'C': ['/*', ' * ', ' */'],
        'C#': ['/*', '  ', '*/'],
        'C++': ['/*', ' *', ' */'],
        'CMake': ['', '# ', ''],
        'CSS': ['/*', '', '*/'],
        'Clojure': ['', '; ', ''],
        'CoffeeScript': ['###', '', '###'],
        'Common Lisp': ['', '; ', ''],
        'Cuda': [], # TODO
        'Cython': ['"""', '', '"""'],
        'Diff': [], # TODO
        'Elm': [], # TODO
        'Emacs Lisp': ['', '; ', ''],
        'FORTRAN': [], # TODO
        'Go': ['', '//', ''],
        'HTML': ['<!--', '', ' --!>'],
        'HTML+Django': ['<!--', '', ' --!>'],
        'HTML+ERB': ['<!--', '', ' --!>'],
        'HTML+PHP': ['<!--', '', ' --!>'],
        'HTTP': [], # TODO
        'Haskell': ['', '-- ', ''],
        'Io': [], # TODO
        'JSON': ['', '// ', ''],
        'Java': ['', '// ', ''],
        'Java Server Pages': ['', '// ', ''],
        'JavaScript': ['', '// ', ''],
        'Julia': ['###', '  ', '###'],
        'Kotlin': ['/**', ' * ', ' */'],
        'LLVM': [], # TODO
        'Less': ['/*', '', '*/'],
        'Lua': ['--[=====[', '', '--]=====]'],
        'Makefile': ['', '# ', ''],
        'Markdown': ['<!--', '', ' --!>'],
        'Matlab': [], # TODO
        'Nginx': [], # TODO
        'NumPy': ['"""', '', '"""'],
        'OCaml': ['(*', '', ' *)'],
        'Objective-C': ['', '// ', ''],
        'PHP': ['<!--', '', ' --!>'],
        'Pascal': [], # TODO
        'Perl': ['', '# ', ''],
        'Python': ['"""', '', '"""'],
        'Python traceback': [], # TODO
        'R': ['', '# ', ''],
        'Ruby': ['', '# ', ''],
        'Rust': ['', '// ', ''],
        'SCSS': ['/*', '', '*/'],
        'SQL': ['', '-- ', ''],
        'Sage': [], # TODO
        'Sass': ['/*', '', '*/'],
        'Scala': ['/**', ' * ', ' */'],
        'Shell': ['', '# ', ''],
        'TeX': ['', '% ', ''],
        'TypeScript': ['/**', '* ', '*/'],
        'VimL': [], # TODO
        'Visual Basic': [], # TODO
        'XML': ['<!--', '', ' --!>'],
        'YAML': ['', '# ', ''],
        'reStructuredText': ['', '.. ', ''],
        'xBase': [], # TODO
    }


"""
Argument Parsing
"""
class FullPaths(argparse.Action):
    """Expand user- and relative-paths"""
    def __call__(self, parser, namespace, values, option_string=None):
        setattr(namespace, self.dest, os.path.abspath(os.path.expanduser(values)))

def is_dir(dirname):
    """Checks if a path is an actual directory"""
    if not os.path.isdir(dirname):
        msg = "{0} is not a directory".format(dirname)
        raise argparse.ArgumentTypeError(msg)
    else:
        return dirname


parser = argparse.ArgumentParser(description="Recursively add license headers to source files")
parser.add_argument('source_dir', help="Path to the root of the directory containing source files",
    action=FullPaths, type=is_dir)
args = parser.parse_args()
print("LOG: Path detected :", args.source_dir, "\n")


"""
Utility functions
"""
def query_yes_no(question, default="yes"):
    """Ask a yes/no question via input() and return their answer.

    "question" is a string that is presented to the user.
    "default" is the presumed answer if the user just hits <Enter>.
        It must be "yes" (the default), "no" or None (meaning
        an answer is required of the user).

    The "answer" return value is True for "yes" or False for "no".
    """
    valid = {"yes": True, "y": True, "ye": True,
             "no": False, "n": False}
    if default is None:
        prompt = " [y/n] "
    elif default == "yes":
        prompt = " [Y/n] "
    elif default == "no":
        prompt = " [y/N] "
    else:
        raise ValueError("invalid default answer: '%s'" % default)

    while True:
        sys.stdout.write(question + prompt)
        choice = input().lower()
        if default is not None and choice == '':
            return valid[default]
        elif choice in valid:
            return valid[choice]
        else:
            sys.stdout.write("Please respond with 'yes' or 'no' "
                             "(or 'y' or 'n').\n")


"""
"""
print("Please make sure that the source directory is tracked by a version control like git.")
print("Also make sure you do not have any uncommitted changes in your repository.")
print("It will later enable you to run 'git checkout -- .' and revert all the changes made by this script.")
if not query_yes_no("Proceed ahead?"):
    sys.exit(1)

files_with_extensions = []

for root, directories, filenames in os.walk(args.source_dir):
    if ".git" in root.split("/"):
        continue
    for filename in filenames:
        path_to_file = os.path.join(root, filename)
        _, file_extension = os.path.splitext(path_to_file)
        files_with_extensions.append((path_to_file, file_extension))

source_files = []
not_source_files = []
for file in files_with_extensions:
    if file[1] in MAP_EXTENTION_TO_LANGUAGE:
        source_files.append(file)
    else:
        not_source_files.append(file)

# print("LOG: Not making any changes to the following files. The script does not recognize them as a source file")
# for file in not_source_files:
#     print('\t -', file[0][len(args.source_dir):])

# print("LOG: All the source files")
# for file in source_files:
#     print('\t -', file[0][len(args.source_dir):])

"""
Detect if License Headers exist

Check first 50 lines for keywords "Copyright" and "License" both.
If found, remove the file from source_files
"""
files_with_headers = []
files_without_headers = []
for file in source_files:
    with open(file[0]) as f:
        first_50_lines = "".join([x.strip() for x in itertools.islice(f, 50)])
    first_50_lines = first_50_lines.lower()
    if "copyright" in first_50_lines and "license" in first_50_lines:
        files_with_headers.append(file)
    else:
        files_without_headers.append(file)

# print("LOG: Found {} source file(s) with existing License headers".format(len(files_with_headers)))
# for file in files_with_headers:
#     print("\t", file[0][len(args.source_dir):])

# Mention all the languages and their comment characters
languages = {}
# key: Language Name
# value: list of files

for file in files_without_headers:
    lang = MAP_EXTENTION_TO_LANGUAGE[file[1]]
    try:
        languages[lang].append(file)
    except KeyError:
        languages[lang] = [file]


"""
Prepare comment block for each language
"""
map_language_to_block_comment = {}

for lang in languages:
    try:
        characters = MAP_LANGUAGE_TO_COMMENT_CHARS[lang]
    except KeyError:
        print("ERROR: Language '{}' not found in MAP_LANGUAGE_TO_COMMENT_CHARS. Please Keep both dictionaries in sync".format(lang))
        continue

    if len(characters) != 3:
        print("ERROR: Language '{}' does not have the required 3 block comment characters. Check MAP_LANGUAGE_TO_COMMENT_CHARS".format(lang))
        continue

    comments = []
    comments.append(characters[0] + LICENSE_HEADER[0])
    for line in LICENSE_HEADER[1:-1]:
        comments.append(characters[1] + line)
    comments.append(characters[-1] + LICENSE_HEADER[-1])

    map_language_to_block_comment[lang] = "\n".join(comments)

if map_language_to_block_comment:
    print("LOG: List of languages and their block comments\n")
    for lang in map_language_to_block_comment:
        print(lang, "\n")
        print(map_language_to_block_comment[lang], "\n")


"""
Make the changes

Exceptional cases:
    - If the first two bytes of the file are "#!", skip the first line
"""
for file in files_without_headers:
    with open(file[0]) as f:
        file_text = f.read()
    lang = MAP_EXTENTION_TO_LANGUAGE[file[1]]
    comment = map_language_to_block_comment[lang]

    new_file_text = ""

    if file_text[:2] == "#!":
        lines = file_text.split("\n", 1)
        lines.insert(1, comment)
        new_file_text = "\n".join(lines)
    else:
        new_file_text = comment + "\n" + file_text
    with open(file[0], 'w') as f:
        f.write(new_file_text)


"""
Finished!
"""
print("LOG: Finished! Make sure to run `git diff` and verify the diff")
print("You can do `git checkout -- .` to revert all the unstaged changes")
