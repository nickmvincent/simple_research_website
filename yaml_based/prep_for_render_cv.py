import yaml


with open('base.yaml', 'r') as file:
    data = yaml.safe_load(file)

print(data['publications'])

new_data = {}

pubs = []
workshop_pubs = []
other_pubs = []

keys = ['title', 'authors', 'date', 'journal', 'doi']
for entry in data['publications']:
    new_entry = {}
    for k, v in entry.items():
        if k in keys:
            new_entry[k] = v
    pubs.append(new_entry)

for entry in data['workshop_papers']:
    new_entry = {}
    for k, v in entry.items():
        if k in keys:
            new_entry[k] = v
    workshop_pubs.append(new_entry)

for entry in data['other_papers']:
    new_entry = {}
    for k, v in entry.items():
        if k in keys:
            new_entry[k] = v
    other_pubs.append(new_entry)

new_data = {
    'archival_publications': pubs,
    'workshop_publications': workshop_pubs,
    'other_publications': other_pubs
}

with open('cv_pubs.yaml', 'w') as outfile:
    yaml.dump(new_data, outfile)