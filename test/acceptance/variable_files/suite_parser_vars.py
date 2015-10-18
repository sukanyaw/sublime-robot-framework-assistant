from os import path


def get_variables():
    root_dir = path.dirname(path.abspath(__file__))
    resource_dir = get_resource_path(root_dir)
    var = {}
    var['SIMPLE_RESOURCE'] = create_simple_resource(resource_dir)
    var['SIMPLE_TEST'] = create_simple_test(resource_dir)
    var['SIMPLE_VAR'] = create_simple_var(resource_dir)
    return var


def create_simple_var(resource_dir):
    result = {}
    result['file_name'] = 'simple_variable_file.py'
    result['file_path'] = path.join(resource_dir, result['file_name'])
    result['variables'] = ['${VARIABLE_FILE_1}', '${VARIABLE_FILE_2}']
    return result


def create_simple_test(resource_dir):
    result = {}
    result['file_name'] = 'simple_test.robot'
    result['file_path'] = path.join(resource_dir, result['file_name'])
    result['libraries'] = [{'library_name': 'Selenium2Library',
                            'library_alias': None}]
    result['resources'] = [path.join(resource_dir, 'simple_resrouce2.robot')]
    result['variable_files'] = [
        [path.join(resource_dir, 'simple_variable_file.py'),
            'arg11',
            'arg22']
        ]
    result['variables'] = ['${VAR2}']
    kws = {}
    kws['mykw1'] = my_kw_1()
    kws['mykw2'] = my_kw_2()
    result['keywords'] = kws
    return result


def create_simple_resource(resource_dir):
    result = {}
    result['file_name'] = 'simple_resource.robot'
    result['file_path'] = path.join(resource_dir, result['file_name'])
    result['libraries'] = [{'library_name': 'Selenium2Library',
                            'library_alias': None}]
    result['variable_files'] = [
        [path.join(resource_dir, 'simple_variable_file.py'),
            'arg11',
            'arg22']
        ]
    result['resources'] = [path.join(resource_dir, 'simple_resrouce2.robot')]
    kws = {}
    kws['mykw1'] = my_kw_1()
    kws['mykw2'] = my_kw_2()
    result['keywords'] = kws
    result['variables'] = ['${VAR1}']
    return result


def get_resource_path(root_dir):
    return path.normpath(
        path.join(
            root_dir,
            '..',
            '..',
            'resource',
            'test_data'
            )
        )


def get_args(**args):
    arg = []
    for k in args:
        if args[k] is not None:
            arg.append('${' + k + '}=${' + args[k] + '}')
        else:
            arg.append('${' + k + '}')
    return arg


def my_kw_1():
    kw = {}
    kw['keyword_arguments'] = get_args(arg1='False', arg2='True')
    kw['documentation'] = 'Some documentation'
    kw['tags'] = ['some_tag', 'other_tag']
    kw['keyword_name'] = 'My Kw 1'
    return kw


def my_kw_2():
    kw = {}
    kw['keyword_arguments'] = get_args(arg2='False', arg4=None)
    kw['documentation'] = 'Some documentation.\\nIn multi line'
    kw['tags'] = ['tag1']
    kw['keyword_name'] = 'My Kw 2'
    return kw
