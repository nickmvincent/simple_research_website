# YAML based system for personal website and CV

## Workflow for updating website

- Manually update `base.yaml`
- Run `convert.py`


## Current workflow

- Manually update `base.yaml`
- Run `convert.py` to generate a new `index.html` based on `template.html` and content in `base.yaml`
- Upload `index.html` (and any new static files) to website.
- Run `prep_for_render_cv.py` to create a processed yaml file, `cv_pubs.yaml`, which you should then manually copy to the `Nicholas_Vincent_CV.yaml` file (rendercv is intentionally opinionated about key names, etc)


### What does prep_for_render_cv populate?
`prep_for_render_cv.py` will process the following categories from base.yaml

- 'archival_publications'
- 'workshop_publications'
- 'other_publications'
- 'news_coverage'
- 'selected_talks'

### Things in the rendercv folder that are NOT in base.yaml

- undergraduate_research_mentoring
- mentoring
- conference_service
- other_service

### Things in the details.yaml file

- additional affiliations

## Exact dates that might mess w/ Yaml