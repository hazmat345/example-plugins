import re

from setuptools import setup


def find_version(version_file):
    version_line = open(version_file, "rt").read()
    match_object = re.search(r"^__version__ = ['\"]([^'\"]*)['\"]", version_line, re.M)

    if not match_object:
        raise RuntimeError("Unable to find version string in %s" % version_file)

    return match_object.group(1)


setup(
    name="jinja",
    version=find_version("jinja/__version__.py"),
    description="Plugin that demonstrates Jinja2 templates",
    url="https://beer-garden.io",
    author="The Beergarden Team",
    author_email=" ",
    license="MIT",
    packages=["jinja"],
    include_package_data=True,
    install_requires=["brewtils", "jinja2"],
    classifiers=[
        "Intended Audience :: Developers",
        "Programming Language :: Python :: 2",
        "Programming Language :: Python :: 2.7",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.5",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
    ],
)
