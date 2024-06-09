from setuptools import setup, find_packages

setup(
    name='MobileDogs',
    version='0.1.0',
    author='Degtyariov Kirill',
    author_email='k.degtyarev4@mail.ru',
    description='A FastAPI project for managing dog collars and related information',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    url='<URL>',
    packages=find_packages(where='src'),
    package_dir={'': 'src'},
    include_package_data=True,
    install_requires=[
        'fastapi==0.95.2',
        'uvicorn==0.18.2',
        'sqlalchemy==1.4.36',
        'elasticsearch==8.2.1',
    ],
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.6',
)
