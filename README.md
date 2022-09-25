# Jupyter PgAdmin Proxy


Add PgAdmin4 to Jupyter binders by using jupyter-server-proxy extension. PgAdmin authenticate user using `webserver` auth mode, thus you don't need to set any login/password pair. In standart mode each user start he's own session, but you can set static login and passwor for all users can use one account (watch `jupyter_pgadmin_proxy/__init__.py)`.

![](/docs/pgadmin_binder.png)
## Install

### Requirements

* `jupyterlab>=2` or `notebook`
* `jupyter-server-proxy`
* `pgadmin4`
* `gunicorn` for Linux\MacOs or `waitress` for Windows

## Attributions

- [`jupyter-server-proxy`](https://github.com/jupyterhub/jupyter-server-proxy)
- [`pgadmin4`](https://www.pgadmin.org)

## License

BSD 3-Clause

## OS supporting
* `Linux`
* `MacOs`
* The extension supports `Windows`, but may not work in some configurations due to a bug described by https://github.com/jupyterhub/jupyter-server-proxy/issues/147
