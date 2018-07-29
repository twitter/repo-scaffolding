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
import logging
import os
import sys
import shutil
import subprocess
import tempfile


"""
The License Header
"""
LICENSE_HEADER = """
Copyright {} Twitter, Inc.
Licensed under the Apache License, Version 2.0
http://www.apache.org/licenses/LICENSE-2.0
""".format(datetime.datetime.now().year).split("\n")


# Comment out non-source extensions e.g. .md
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


"""
Utility
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


class color(object):
   PURPLE = '\033[95m'
   CYAN = '\033[96m'
   DARKCYAN = '\033[36m'
   BLUE = '\033[94m'
   GREEN = '\033[92m'
   YELLOW = '\033[93m'
   RED = '\033[91m'
   BOLD = '\033[1m'
   UNDERLINE = '\033[4m'
   END = '\033[0m'


def apply_changes(source_path, skip_log=False):
    files_with_extensions = []

    for root, directories, filenames in os.walk(source_path):
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

    if not skip_log:
        logging.info("Not making any changes to the following files. The script does not recognize them as a source file")
        for file in not_source_files:
            logging.info('\t - ' + file[0][len(source_path):])

    # print("All the source files")
    # for file in source_files:
    #     print('\t -', file[0][len(source_path):])

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

    if not skip_log:
        print("\nFound {} source file(s) with existing License headers".format(len(files_with_headers)))
        logging.info("\nFound {} source file(s) with existing License headers".format(len(files_with_headers)))
        for file in files_with_headers:
            logging.info("\t " + file[0][len(source_path):])


    """
    Prepare comment block for each language
    """

    languages = {}
    # key: Language Name
    # value: list of files

    for file in files_without_headers:
        lang = MAP_EXTENTION_TO_LANGUAGE[file[1]]
        try:
            languages[lang].append(file)
        except KeyError:
            languages[lang] = [file]


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
        if characters[0] != "":
            comments.append(characters[0] + LICENSE_HEADER[0])
        for line in LICENSE_HEADER[1:-1]:
            comments.append(characters[1] + line)
        comments.append(characters[-1] + LICENSE_HEADER[-1])

        map_language_to_block_comment[lang] = "\n".join(comments)

    if map_language_to_block_comment and not skip_log:
        logging.info("\n\nList of languages and their block comments\n")
        for lang in map_language_to_block_comment:
            logging.info(lang + "\n")
            logging.info(map_language_to_block_comment[lang] + "\n")


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

    if not skip_log:
        print("{} source file(s) need to be updated".format(len(files_without_headers)))
        logging.info("{} source file(s) need to be updated".format(len(files_without_headers)))


def get_current_branch(path):
    # Save current working directory
    cur_dir = os.getcwd()
    os.chdir(path)
    cur_branch = ""
    try:
        output = subprocess.check_output(["git", "branch"]).decode("utf-8")
        for line in output.split("\n"):
            if line[:2] == "* ":
                cur_branch = line[2:]
                break
    except Exception as e:
        print("Error in get_current_branch function", e)
        print("Are you the repository is tracked by git?")

    return cur_branch

def entry():
    """
    Parse arguments
    """
    parser = argparse.ArgumentParser(description="Recursively add license headers to source files")
    parser.add_argument('source_dir', help="Path to the root of the directory containing source files",
        action=FullPaths, type=is_dir)
    args = parser.parse_args()
    print("Path detected :", color.BOLD + args.source_dir + color.END)
    current_branch = get_current_branch(args.source_dir)
    if current_branch:
        print("Branch detected -", color.BOLD + current_branch, color.END, "\n")


    """
    Enable logging to a file
    """
    # f = tempfile.NamedTemporaryFile(delete=False, suffix=".log")
    # f.close()
    # LOG_FILENAME = f.name
    LOG_FILENAME = "header-" + datetime.datetime.now().isoformat() + ".log"

    logging.basicConfig(filename=LOG_FILENAME, level=logging.DEBUG, format="%(message)s")

    print(color.YELLOW + "* Please make sure that the source directory is tracked by git.")
    print("* Create a new branch before proceeding ahead.")
    print("* Make sure you do not have any uncommitted changes in your repository.")
    print("It will later enable you to run 'git checkout -- .' and revert all the changes made by this script." + color.END)
    if not query_yes_no("Proceed ahead? (Don't worry, this won't make changes yet)", default="no"):
        print("Aborted!")
        sys.exit(1)


    """
    Make a temporary copy of the source directory and make changes there
    """
    tempdir = tempfile.mkdtemp()
    shutil.rmtree(tempdir)  # shutil.copytree mandates the destination to not exist
    print(color.BOLD, "\nCreating a copy of the project at\n")
    print("\t", color.GREEN, tempdir, color.END)
    shutil.copytree(args.source_dir, tempdir)

    apply_changes(tempdir)

    print(color.BOLD, "\nApplied changes to the copy of the project\n", color.END)
    print("1. Make sure to run `git diff` in the following directory and verify the diff.\n")
    print("\t$ cd", tempdir)
    print("\t$ git diff\n")
    print("2. Review the detailed log file - " + color.BOLD + os.getcwd() + "/" + LOG_FILENAME, color.END)
    print("3. Run the unit tests and build the project.")
    print("\nIf everything looks good in the copy of the project, proceed ahead.")
    print("Changes will now be made to " + color.BOLD + args.source_dir + color.END)
    if not query_yes_no("Want to continue?", default="no"):
        print("Aborted!")
        sys.exit(1)

    apply_changes(args.source_dir, skip_log=True)

    print(color.GREEN + "\nFinished running the script!")
    print("You can do `git checkout -- .` to revert all the unstaged changes")
    print("`git checkout -- <path>` can also undo a specific file or multiple files in a directory" + color.END)


if __name__ == '__main__':
    # Clear screen
    os.system('clear')

    entry()
