from setuptools import setup, find_packages
def get_requirement(path):
    hyphen_e_dot='-e .'
    with open(path) as file:
        line=file.readlines()
        for req in line:
            req.replace("\n",'')
        if hyphen_e_dot in req:
            line.remove(hyphen_e_dot)

    return line
setup(
    name="MLprog",
    version="0.1",
    author='Avinash',
    author_email='avinashmbhat18@gmail.com',
    packages=find_packages(),
    install_requires=get_requirement('requirements.txt')
)
