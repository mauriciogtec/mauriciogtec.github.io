# Mauricio's personal website

[![Netlify Status](https://api.netlify.com/api/v1/badges/e6df9d05-bdbb-4edc-9c89-872e526c6650/deploy-status)](https://app.netlify.com/sites/trusting-wilson-65327b/deploys)


This website was built on code from [Chris Holdgraf's new blog template](https://chrisholdgraf.com/blog/2020/sphinx-blogging/).

------------

This is my personal website, built with Sphinx!

## Build and preview the docs

**Build the docs**. Use `nox`, which handles all of the environment generation automatically.
To do so, follow these steps:

1. Install `nox`.

   ```shell
   pip install -U nox
   ```
2. Run `tox`

   ```shell
   nox -s docs
   ```

this should install a Sphinx environment and build the site, putting the output files in `_build/html`.

## Execute and interact with the code

**Run a live webserver**:

```shell
nox -s docs -- live
```

**Run a JupyterLab environment with necessary packages installed:

```shell
nox -s lab
```
