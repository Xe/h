#!/usr/bin/python

import sys, os
import random
import string
import re

choice = random.choice
randint = random.randint

def dc(n, m=20):
    return n < randint(0, m-1)

base_noun = [
    'TCP', 'IP', 'UDP', 'BGP', 'DNS', 'ARP spoof', 'ARP', 'JavaScript',
    'HTML', 'CSS', 'XML', 'SOAP', 'REST', 'SSL', 'socket', 'BSD', 'linux',
    'MPI', 'OpenMP', 'SYN/ACK', 'kernel', 'ELF', 'COFF', '68000', 'x86',
    'MIPS', 'ethernet', 'MAC', 'C', 'C++', 'Java', 'JSON', 'ruby',
    'python', 'linked list', 'radix trie', 'hash table', 'SQL', 'makefile',
    '/proc', '/dev/null', 'tty', 'regex', 'sed', 'vim', 's/// operation',
    'operation', 'port scanner', 'port scan', 'lookup table', 'anti-<noun>',
    '<verber> manual', '<verber> config', 'IRC', 'IRC bot', 'bootloader',
    'GNU/<noun>',
]


# I suppose it would be easier to create rules for a lot of these, but 
# I think LUTs are fine.

base_verb = [
    ( 'compile',       '-s',        '-d',        '-r',        'compiling' ),
    ( 'link',          '-s',       '-ed',       '-er',             '-ing' ),
    ( 'assemble',      '-s',        '-d',        '-r',       'assembling' ),
    ( 'load',          '-s',       '-ed',       '-er',             '-ing' ),
    ( 'boot',          '-s',       '-ed',       '-er',             '-ing' ),
    ( 'reset',         '-s',     'reset',      '-ter',            '-ting' ),
    ( 'remove',        '-s',        '-d',        '-r',         'removing' ),
    ( 'decompile',     '-s',        '-d',        '-r',      'decompiling' ),
    ( 'unlink',        '-s',       '-ed',       '-er',             '-ing' ),
    ( 'disassemble',   '-s',        '-d',        '-r',    'disassembling' ),
    ( 'unload',        '-s',       '-ed',       '-er',             '-ing' ),
    ( 'parse',         '-s',        '-d',        '-r',          'parsing' ),
    ( 'archive',       '-s',        '-d',        '-r',        'archiving' ),
    ( 'cherry-pick',   '-s',       '-ed',       '-er',             '-ing' ),
    ( 'overwrite',     '-s', 'overwrote',        '-r',      'overwriting' ),
    ( 'edit',          '-s',       '-ed',       '-or',             '-ing' ),
    ( 'compute',       '-s',        '-d',        '-r',        'computing' ),
    ( 'release',       '-s',        '-d',        '-r',        'releasing' ),
    ( 'transmit',      '-s',      '-ted',      '-ter',            '-ting' ),
    ( 'receive',       '-s',        '-d',        '-r',        'receiving' ),
    ( 'analyze',       '-s',        '-d',        '-r',        'analyzing' ),
    ( 'print',         '-s',       '-ed',       '-er',             '-ing' ),
    ( 'save',          '-s',        '-d',        '-r',           'saving' ),
    ( 'erase',         '-s',        '-d',        '-r',          'erasing' ),
    ( 'install',       '-s',       '-ed',       '-er',             '-ing' ),
    ( 'scan',          '-s',      '-ned',      '-ner',            '-ning' ),
    ( 'port scan',     '-s',      '-ned',      '-ner',            '-ning' ),
    ( 'nmap',          '-s',      '-ped',      '-per',            '-ping' ),
    ( 'DDOS',         '-es',      '-sed',      '-ser',            '-sing' ),
    ( 'exploit',       '-s',       '-ed',       '-er',             '-ing' ),
    ( 'send',          '-s',      'sent',       '-er',             '-ing' ),
    ( 'write',         '-s',     'wrote',        '-r',          'writing' ),
    ( 'detect',        '-s',       '-ed',       '-or',             '-ing' ),
    ( 'sniff',         '-s',       '-ed',       '-er',             '-ing' ),

    ( 'look up', 'looks up', 'looked up', 'looker upper', 'looking up' ),
    ( 'check out', 'checks out', 'checked out', 'checker outer', 'checking out' ),
    ( 'query', 'queries', 'queried', 'querier', 'querying' ),
]

base_service = [
    'Google', 'Amazon', 'Stack Overflow', 'Freenode', 'EFnet', 'Usenet',
    'this old GeoCities page', 'my website', '<person>\'s website',
]

base_hack_object = [
    'the <noun>', 'a(n) <noun>', 'the victim\'s <noun>', 'some <noun>',
    'a(n) <verber> from <service>', '<service>\'s <noun>',
    'the freeware <noun>', 'a configurable <noun>', 'a working <noun>',
    'a pre-<verbed> <verber>',
]

base_tool = [
    '<noun> <verber>',
    '<verbed> <noun>',
    '<verber>',
    '<verber> for <nouns>',
    '<verbing> <tool>',
    'thing that <verbs>',
    'thing for <verbing> <nouns>',
    'pre-<noun> <verber>',
    'anti-<noun> <verber>',
    '<verbing> tool',
    '<verber> subsystem',
    'professional <verber>',
    '<verber>-<verber> hybrid',
]

base_tools = [
    '<noun> <verber>s',
    '<verbed> <nouns>',
    '<verber>s',
    '<verbing> <tools>',
    'things for <verbing>',
    'pre-<noun> <verber>s',
]

base_person = [
    'Linus Torvalds',
    'Alan Cox',
    'Con Colivas',
    'Ingo Molnar',
    'Hans Reiser',
    'Ulrich Drepper',
    'Larry Wall',
    'William Pitcock',
    'Bill Gates',
    'Ken Thompson',
    'Brian Khernigan',
    'Dennis Ritchie',
    'Eric S. Raymond',
    'Richard M. Stallman',
    'DPR',
    'Sabu',
]

base_system = [
    'Amiga', 'C-64', 'IBM PC', 'Z80', 'VAX', 'the PDP-8',
]

base_time = [
    'way back', 'a few years ago', 'in the early 90\'s I think',
    'when everybody had a(n) <verber>',
    'before anybody knew who <person> was',
]

# <hack> is intransitive
# <tool> is singular

base_advice = [
    'Try <hacking>.',
    'Did you <hack> first?',
    'Read up on <hacking>.',
    'Check <service> for a(n) <tool>.',
    'See if the <tool> has <hacked> already.',
    'Did you check the <tool> config?',
    'Hm, sounds like a problem with the <tool>.',
    'Doesn\'t look like the <tool> is <hacking>.',
    'Check the "<tool>" wiki.',
    'You probably didn\'t <hack>.',
    'Check the "<tool>" website.',
    '<hack>, then send me the <tool> output.',
    'Pastebin your <tool> config.',
    'I think my <noun> has a(n) <verber>, try that.',
    '<hacking> worked for me.',
    'Did you enable the <tool>?',
    'No, the <tool> <hacks>. You want a(n) <tool>.',
    'Do you have a(n) <tool> installed?',
    'A(n) <tool> is needed to <hack>.',
    '<person> claims you can <hack>.',
    'I heard <person> <hacks> when that happens.',
    'I saw on <service>, you can <hack>.',
    'A(n) <tool> might do the trick.',
    'Make sure to delete your <tool>. That stuff is illegal.',
    'Did you <hack> before you <hacked>?',
    'Where did you <verb> the <tool> to?',
    'I don\'t know. Ask the guy who wrote your <tool>. I think <person>?',
    'Was this with a(n) <tool> or a(n) <tool>?',
    'Please use the official <tool>.',
    'That won\'t work. You can\'t just <hack>.',
    '<hack>, <hack>, and THEN <hack>. Sheesh.',
    'No, don\'t <hack>. <person> recently published a CVE about that.',
    '<verb>, <verb>, <verb>. This is our motto.',
    'Don\'t think too hard about <hacking>. The <tool> will do that.',
    'There\'s a(n) <noun> exploit floating around somewhere. Check <service>.',
    'Simple <tools> cannot <hack>. You need a good, solid <tool>.',
    'I had a(n) <tool> for <system> <time>.',
    'Sounds like you need a(n) <tool>. <person> wrote one for <service>.',
]

def simple_get(the_list):
    def get_thing():
        return choice(the_list)
    return get_thing

get_base_verb = simple_get(base_verb)
get_noun = simple_get(base_noun)
get_service = simple_get(base_service)
get_hack_object = simple_get(base_hack_object)
get_tool = simple_get(base_tool)
get_tools = simple_get(base_tools)
get_person = simple_get(base_person)
get_base_advice = simple_get(base_advice)
get_system = simple_get(base_system)
get_time = simple_get(base_time)

def get_nouns():
    n = get_noun()
    if not n[-1] in string.ascii_letters:
        return n + '\'s'
    if n.lower()[-1] in 'xs':
        return n + 'es'
    return n + 's'

def compute_verb(n):
    v = get_base_verb()
    base = v[0]
    ext = v[n]
    if ext[0] == '-':
        return base + ext[1:]
    return ext

def make_verb(n):
    def get_verb():
        return compute_verb(n)
    return get_verb

get_verb = make_verb(0)
get_verbs = make_verb(1)
get_verbed = make_verb(2)
get_verber = make_verb(3)
get_verbing = make_verb(4)

def make_hack(vf):
    def get_hack():
        return vf() + ' ' + get_hack_object()
    return get_hack

def get_hacker():
    return get_hack_object() + ' ' + get_verber()

get_hack = make_hack(get_verb)
get_hacks = make_hack(get_verbs)
get_hacked = make_hack(get_verbed)
get_hacking = make_hack(get_verbing)

index_get = {
    'verb':      get_verb,
    'verbs':     get_verbs,
    'verbed':    get_verbed,
    'verber':    get_verber,
    'verbing':   get_verbing,

    'noun':      get_noun,
    'nouns':     get_nouns,

    'hack':      get_hack,
    'hacks':     get_hacks,
    'hacked':    get_hacked,
    'hacker':    get_hacker,
    'hacking':   get_hacking,

    'service':   get_service,

    'tool':      get_tool,
    'tools':     get_tools,

    'person':    get_person,
    'system':    get_system,
    'time':      get_time,
}

def can_reduce(s):
    return '<' in s and '>' in s

def reduction(s):
    s = re.split('[<>]', s)
    for i, word in enumerate(s):
        if i % 2 == 0:
            continue
        up = False
        if all(x in string.ascii_uppercase for x in word):
            up = True
            word = word.lower()
        if not word in index_get:
            word = '?' + word
        else:
            word = index_get[word]()
        if up:
            word = word.upper()
        s[i] = word
    return ''.join(s)

def indefinite_articles(s):
    s = re.sub('([aA])\\(([nN])\\) ([AEFHILMNORSXaeiou])', '\\1\\2 \\3', s)
    s = re.sub('([aA])\\([nN]\\) ', '\\1 ', s)
    return s

def evaluate(s):
    while can_reduce(s):
        s = reduction(s)
    s = indefinite_articles(s)
    s = s[0].upper() + s[1:]
    return s

def get_advice():
    return evaluate(get_base_advice())

if __name__ == '__main__':
    if len(sys.argv) > 1:
        print(evaluate(sys.argv[1]))
    else:
        print(get_advice())

from util import hook

@hook.command
def hack(inp):
    res = ""
    if len(inp) > 1:
        res = evaluate(inp)
    else:
        res = evaluate(get_base_advice())

    return res
