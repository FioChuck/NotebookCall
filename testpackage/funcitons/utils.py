def local_vars():
    try:
        from testpackage.variables.local_variables import vars
    except ImportError:
        print('local variable missing')
    return vars
