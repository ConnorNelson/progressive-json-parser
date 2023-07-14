from setuptools import setup, find_packages

setup(
    name="progressive_json_parser",
    version="0.1",
    packages=find_packages(),
    install_requires=[
        'lark',
    ],
    author="Connor Nelson",
    description="This is a progressive JSON parser.",
    python_requires='>=3.6',
)