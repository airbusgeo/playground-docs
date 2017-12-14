# OneAtlas Playground Documentation

## Documentation 

This documentation is powered by MkDocs

Prerequisites 

```pip install mkdocs mkdocs-material pymdown-extensions```

Check ```docs/``` for the raw markdown files.

To edit and see live changes, edit the markdown files while running `mkdocs serve`. The site is available at http://localhost:8000
         
To deploy build the site 

```bash
mkdocs build --clean
gcloud app deploy
```
## Former app.yaml

```yaml

service: docs
runtime: python27
api_version: 1
threadsafe: true
manual_scaling:
  instances: 1

handlers:
# Handle the main page by serving the index page.
# Note the $ to specify the end of the path, since app.yaml does prefix matching.
- url: /$
  static_files: site/index.html
  upload: site/index.html

# Handle folder urls by serving the index.html page inside.
- url: /(.*)/$
  static_files: site/\1/index.html
  upload: site/.*/index.html

# Handle nearly every other file by just serving it.
- url: /(.+)
  static_files: site/\1
  upload: site/(.*)
```
