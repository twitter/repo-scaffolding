#!/usr/bin/env python3

"""
Copyright 2018 Twitter, Inc.

Licensed under the Apache License, Version 2.0 (the "License");
you may not use this file except in compliance with the License.
You may obtain a copy of the License at

http://www.apache.org/licenses/LICENSE-2.0

Unless required by applicable law or agreed to in writing, software
distributed under the License is distributed on an "AS IS" BASIS,
WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
See the License for the specific language governing permissions and
limitations under the License.
"""

"""
This script can be used to add license headers to all the source files of a project.
It is designed to be safe, so do not worry and try it out!

Works with languages with nonempty value in MAP_LANGUAGE_TO_COMMENT_CHARS

"""

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
        '.json': 'JSON',
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
        '.md': 'Markdown',
        '.mkii': 'TeX',
        '.mkiv': 'TeX',
        '.mkvi': 'TeX',
        '.ml': 'OCaml',
        '.mm': 'Objective-C',
        '.mspec': 'Ruby',
        '.mustache': 'HTML+Django',
        '.nginxconf': 'Nginx',
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
        '.rest': 'reStructuredText',
        '.rs': 'Rust',
        '.rst': 'reStructuredText',
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
        '.xml': 'XML',
        '.xpy': 'Python',
        '.yaml': 'YAML',
        '.yml': 'YAML',
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
        'C': ['/*', ' *', ' */'],
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
        'HTML': ['<!-- ', '', ' --!>'],
        'HTML+Django': ['<!-- ', '', ' --!>'],
        'HTML+ERB': ['<!-- ', '', ' --!>'],
        'HTML+PHP': ['<!-- ', '', ' --!>'],
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
        'Markdown': ['<!-- ', '', ' --!>'],
        'Matlab': [], # TODO
        'Nginx': [], # TODO
        'NumPy': ['"""', '', '"""'],
        'OCaml': ['(*', '', ' *)'],
        'Objective-C': ['', '// ', ''],
        'PHP': ['<!-- ', '', ' --!>'],
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
        'XML': ['<!-- ', '', ' --!>'],
        'YAML': ['', '# ', ''],
        'reStructuredText': ['', '.. ', ''],
        'xBase': [], # TODO
    }
