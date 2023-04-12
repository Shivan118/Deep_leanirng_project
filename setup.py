import setuptools

with open("README.md", "r", encoding="utf-8") as f:
    long_desciption = f.read()

__version__ = "0.0.1"

REPO_NAME = "Deep_leanirng_project"
AUTHOR_USER_NAME = "Shivan118"
SRC_REPO = "Deep_leanirng_project"
AUTHOR_EMAIL = "kshivan848@gmail.com"


setuptools.setup(name = SRC_REPO,
                 version = __version__,
                 author = AUTHOR_USER_NAME,
                 author_email = AUTHOR_EMAIL,
                 description ="A Small Deep learning project",
                 long_desciption = long_desciption,
                 long_desciption_content = "text/markdown",
                 url=f"https://github.com/{AUTHOR_USER_NAME}/{REPO_NAME}",
                project_urls={
                    "Bug Tracker": f"https://github.com/{AUTHOR_USER_NAME}/{REPO_NAME}/issues",
                },
                package_dir={"": "src"},
                packages=setuptools.find_packages(where="src")
)

