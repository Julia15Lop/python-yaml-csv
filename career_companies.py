#!/usr/bin/env python

import csv
import yaml

with open(r'career_companies.yaml') as file:
    documents = yaml.safe_load(file)

    with open('career_companies.csv', 'w', newline='') as file:
        fieldnames = ["company", "host", "site_name"]
        writer = csv.DictWriter(file, fieldnames=fieldnames)
        writer.writeheader()
        for item, companies in documents.items():
            for company in companies:
                # Create csv file            
                writer.writerow(company)
    print("[Created file]: career_companies.csv")

