from setuptools import setup, find_packages
from pathlib import Path


requires = ['sh']

path_to_testhelpers = Path(__file__).parent / "autograder/test_helpers"
paths_to_testhelpers = [str(p) for p in path_to_testhelpers.iterdir()]

setup(
    name="assignment-autograder",
    packages=["autograder"],
    version="2.3.1",
    install_requires=requires,
    package_data={
        "autograder": [
            "default_config.ini",
        ] + paths_to_testhelpers,
    },
    entry_points={
        'console_scripts': ['autograder=autograder.__main__:main']
    },

    # metadata to display on PyPI
    author="Stanislav Zmiev",
    author_email="szmiev2000@gmail.com",
    description="Automatic assignment grading for instructor use in programming courses",
    license="MIT",
    project_urls={"Source Code": "https://github.com/Ovsyanka83/autograder"},
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Environment :: Console',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Natural Language :: English',
        'Operating System :: OS Independent',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
    ]
)
