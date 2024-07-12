import os
from functools import cache

import requests

orgs_sql = ("SELECT DISTINCT o.organisation, o.name "
            "FROM provision p "
            "INNER JOIN organisation o "
            "ON p.organisation = o.organisation ")

orgs_column_map = {
    "organisation_id": 0,
    "organisation_name": 1
}

org_provisions_sql_template = ("SELECT p.organisation, o.name, p.dataset, rle.endpoint, rle.resource "
                               "FROM provision p "
                               "INNER JOIN organisation o "
                               "    ON o.organisation = p.organisation "
                               "INNER JOIN dataset d "
                               "    ON p.dataset = d.dataset "
                               "LEFT JOIN reporting_latest_endpoints rle "
                               "    ON REPLACE(rle.organisation, '-eng', '') = p.organisation "
                               "    AND rle.pipeline = p.dataset "
                               "WHERE p.organisation = '<organisation_id>' "
                               "ORDER BY p.organisation, o.name, p.dataset")

org_provisions_column_map = {
    "organisation_id": 0,
    "organisation_name": 1,
    "dataset": 2,
    "endpoint": 3,
    "resource": 4,
}

resource_issue_counts_sql_template = ("SELECT it.severity, count(*) AS count "
                                      "FROM issue i "
                                      "INNER JOIN issue_type it "
                                      "ON i.issue_type = it.issue_type "
                                      "WHERE i.resource = '<resource_id>' "
                                      "GROUP BY it.severity")

resource_issue_counts_column_map = {
    "severity": 0,
    "count": 1
}

@cache
def datasette_base_url():
    return os.environ.get("DATASETTE_BASE_URL", "https://datasette.planning.data.gov.uk")


def query_orgs():
    return _query_digital_land(orgs_sql)


def query_org_provisions(organisation_id):
    org_provisions_sql = org_provisions_sql_template.replace("<organisation_id>", organisation_id)
    return _query_digital_land(org_provisions_sql)


def query_resource_issue_counts(resource_id):
    resource_issue_counts_sql = resource_issue_counts_sql_template.replace("<resource_id>", resource_id)
    return _query_digital_land(resource_issue_counts_sql)


def _query_digital_land(sql):
    base_url = datasette_base_url()
    url = f"{base_url}/digital-land.json?sql={sql}"
    response = requests.get(url)
    return response.json()["rows"]