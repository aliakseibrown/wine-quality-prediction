import setuptools

with open("README.md", "r", encoding="utf-8") as f:
    long_discription = f.read()

__version__ = "0.0.0"

REPO_NAME = "wine-quality-prediction"
AUTHOR_USER_NAME = "aliakseibrown"
SRS_REPO = "wineProject"
AUTHOR_EMAIL = "alexeybrown2099@gmail.com"

setuptools.setup (
    name = SRS_REPO,
    version = __version__,
    author = AUTHOR_USER_NAME,
    author_email = AUTHOR_EMAIL,
    description = "a python package for ml app",
    long_discription = long_discription,
    long_discription_content = "text/markdown",
    url=f"https://github.com/{AUTHOR_USER_NAME}/{REPO_NAME}",
    project_urls={
        "Bug Tracker" : f"https://github.com/{AUTHOR_USER_NAME}/{REPO_NAME}/issues"
    },
    package_dir = {"":"srs"},
    packages = setuptools.find_packages(where="srs")
)