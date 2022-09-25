import setuptools

setuptools.setup(
    name="jupyter-pgadmin-proxy",
    version="0.1",
    author="azhig",
    license="BSD-3-Clause",
    description="PgAdmin extension for Jupyter",
    long_description_content_type="text/markdown",
    packages=setuptools.find_packages(),
    keywords=["Jupyter", "pgadmin"],
    classifiers=["Framework :: Jupyter"],
    entry_points={"jupyter_serverproxy_servers": ["pgadmin = jupyter_pgadmin_proxy:setup_pgadmin"]},
    package_data={"jupyter_pgadmin_proxy": ["icons/*", "config/*"]},
    install_requires=["jupyter-server-proxy", "pgadmin4", "gunicorn"],
    extras_require={"win32": ["waitress"]},
)
