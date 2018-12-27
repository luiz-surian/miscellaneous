import pkg_resources

packages = ' '.join([dist.project_name for dist in pkg_resources.working_set])


with open('pip_upgrade.bat', 'w') as bat_file:
    bat_file.write(
        '@echo off\n'
        f'pip install --upgrade {packages}\n'
        'pause'
    )
