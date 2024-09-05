from setuptools import setup, find_packages

setup(
    name="flow-log-parser",
    version="0.1.6",
    packages=find_packages(where="src"),
    package_dir={"": "src"},
    install_requires=[],
    entry_points={
        "console_scripts": [
            "flow-log-parser=flow_log_parser.__main__:main",
        ],
    },
    author="Sabiq Khan",
    description="Parses a given VPC flow log file based on a given lookup table CSV file.",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
)