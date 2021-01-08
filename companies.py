#!/usr/bin/env python

import csv
import yaml

with open(r'iframe_companies.yaml') as file:
    documents = yaml.safe_load(file)

    with open('iframe_companies.csv', 'w', newline='') as file:
        fieldnames = ["company", "host", "company_slug"]
        writer = csv.DictWriter(file, fieldnames=fieldnames)
        writer.writeheader()
        for item, companies in documents.items():
            for company in companies:
                # Create csv file            
                writer.writerow(company)
    print("[Created file]: iframe_companies.csv")

