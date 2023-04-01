from scholarly import scholarly
import jsonpickle
import json
from datetime import datetime
import os

author: dict = scholarly.search_author_id(os.environ['GOOGLE_SCHOLAR_ID'])
scholarly.fill(author, sections=['basics', 'indices', 'counts', 'publications'])
name = author['name']
author['updated'] = str(datetime.now())
author['publications'] = {v['author_pub_id']:v for v in author['publications']}
print(json.dumps(author, indent=2))
os.makedirs('results', exist_ok=True)
with open(f'results/gs_data.json', 'w') as outfile:
    json.dump(author, outfile, ensure_ascii=False)

shieldio_data = {
  "schemaVersion": 1,
  "label": "citations",
  "message": f"{author['citedby']}",
}
with open(f'results/gs_data_shieldsio.json', 'w') as outfile:
    json.dump(shieldio_data, outfile, ensure_ascii=False)

shieldio_data_hindex = {
  "schemaVersion": 1,
  "label": "h-index",
  "message": f"{author['hindex']}",
}
with open(f'results/gs_data_shieldsio_hindex.json', 'w') as outfile:
    json.dump(shieldio_data_hindex, outfile, ensure_ascii=False)

shieldio_data_i10 = {
  "schemaVersion": 1,
  "label": "i10-index",
  "message": f"{author['i10index']}",
}
with open(f'results/gs_data_shieldsio_i10.json', 'w') as outfile:
    json.dump(shieldio_data_i10, outfile, ensure_ascii=False)
