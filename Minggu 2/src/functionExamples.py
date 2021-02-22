def standard_arg(arg):
    print(arg)

def pos_only_arg(arg= 1, /):
    print(arg)

def kwd_only_arg(*, arg=3):
    print(arg)

def combined_example(pos_only=1, /, standard=2, *, kwd_only=3):
    print(pos_only, standard, kwd_only)

def foo(name, /,**kwds):
    return 'name' in kwds
foo(1, **{'name': 2})
True