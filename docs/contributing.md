Any kind of contribution is more than welcomed! There are several ways you can contribute:

- Opening [GitHub issues](https://github.com/y-sunflower/pyfonts/issues) to list the bugs you've found
- Implementation of new features or resolution of existing bugs
- Enhancing the documentation

## How `pyfonts` works

Under the bonnet, `pyfonts` does several things, but it can be summarised as follows:

- Take the user's data (font name, weight, italics) and create a url that will be passed to Google's Font API.
- Parse the response to obtain the url of the actual font file
- Retrieve the font file from a temporary file
- Use this temporary file to create a matplotlib font object (which is [`FontProperties`](https://matplotlib.org/stable/api/font_manager_api.html#matplotlib.font_manager.FontProperties){target=‘ \_blank’})
- Return this object

By default, the font file url is cached to reduce the number of requests required and improve performance. The cache can be cleared with `clear_pyfonts_cache()`.

## Setting up your environment

### Install for development

- Fork the repository to your own GitHub account.

- Clone your forked repository to your local machine (ensure you have [Git installed](https://git-scm.com/book/en/v2/Getting-Started-Installing-Git)):

```bash
git clone https://github.com/YOURUSERNAME/pyfonts.git
cd pyfonts
```

- Create a new branch:

```bash
git checkout -b my-feature
```

- Set up your Python environment (ensure you have [uv installed](https://docs.astral.sh/uv/getting-started/installation/)):

```bash
uv sync --all-extras --dev
uv pip install -e .
```

### Code!

You can now make changes to the package and start coding!

### Run the test

- Test that everything works correctly by running:

```bash
uv run pytest
```

### Preview documentation locally

```bash
uv run mkdocs serve
```

### Push changes

- Commit and push your changes:

```bash
git add -A
git commit -m "description of what you did"
git push
```

- Go back to your fork and click on the "Open a PR" popup

Congrats! Once your PR is merged, it will be part of `pyfonts`.

<br>
