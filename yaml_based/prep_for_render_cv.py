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

news_coverage = []
for entry in data['news_coverage']:
    new_entry = {
        "bullet": "{}. [{}]({}). {}, {}".format(entry["authors"], entry['title'], entry['url'], entry['source'], entry['date'])
    }
    news_coverage.append(new_entry)

selected_talks = []
for entry in data['selected_talks']:
    new_entry = {}
    if entry.get('event_url'):
        s = "Event: [{}]({})".format(entry['location'], entry['event_url'])
    else:
        s = "Event: {}".format( entry['location'])

    if entry.get('video_url'):
        s += " ([Video](entry.video_url))"
    new_entry = {
        "name": entry['name'],
        "date": entry['date'],
        "highlights": [
            s
        ]
    }
    selected_talks.append(new_entry)
    

workshops_organized = []
for entry in data['workshops_organized']:
    new_entry = {
        "bullet": "{}. [{}]({}). {}, {}".format(entry["authors"], entry['title'], entry['url'], entry['description'], entry['year'])
    }
    workshops_organized.append(new_entry)

        

new_data = {
    'archival_publications': pubs,
    'workshop_publications': workshop_pubs,
    'other_publications': other_pubs,
    'news_coverage': news_coverage,
    'selected_talks': selected_talks,
    'workshops_organized': workshops_organized
}

class MyDumper(yaml.Dumper):

    def increase_indent(self, flow=False, indentless=False):
        return super(MyDumper, self).increase_indent(flow, False)

with open('cv_pubs.yaml', 'w') as outfile:
    yaml.dump(new_data, outfile,  Dumper=MyDumper, default_flow_style=False)