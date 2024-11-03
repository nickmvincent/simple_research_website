# YAML based system for personal website and CV

## Workflow for updating website

- Manually update `base.yaml`
- Run `convert.py`


## Current workflow

- Add or edit content in `base.yaml`
- Run `python3 convert.py` to generate a new `index.html`. This process uses the template in `template.html` and content in `base.yaml`
- You can now upload `index.html` (and any new static files) to website.
- Next, run `python3 prep_for_render_cv.py` to create a processed yaml file, `cv_pubs.yaml`, which you should then manually copy to the `Nicholas_Vincent_CV.yaml` file (rendercv is intentionally opinionated about key names, etc)
  - `prep_for_render_cv.py` will process the following categories from base.yaml
    - 'archival_publications'
    - 'workshop_publications'
    - 'other_publications'
    - 'news_coverage'
    - 'selected_talks'
  - to edit any other categories in the CV, edit `Nicholas_Vincent_CV.yaml` file directly
    - undergraduate_research_mentoring
    - mentoring
    - conference_service
    - other_service
- When you're done, write a commit message that captures the changes


### Things in the details.yaml file

- additional affiliations

## Exact dates that might mess w/ Yaml