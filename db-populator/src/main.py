import click
from sqlalchemy.orm import Session

import datasette
from crud import engine
from models import Organisation, Dataset


@click.command()
def populate():
    db_engine_builder = engine()

    org_rows = datasette.query_orgs()

    for org_row in org_rows:
        org_model = Organisation(
            id=org_row[datasette.orgs_column_map["organisation_id"]],
            name=org_row[datasette.orgs_column_map["organisation_name"]]
        )

        org_provisions_rows = datasette.query_org_provisions(org_model.id)

        for org_provision_row in org_provisions_rows:
            # TODO: Replace hard-coded record count
            dataset_model = Dataset(organisation_id=org_model.id,
                                    dataset=org_provision_row[datasette.org_provisions_column_map["dataset"]],
                                    record_count=500,
                                    warning_count=0,
                                    error_count=0)

            resource_id = org_provision_row[datasette.org_provisions_column_map["resource"]]
            if resource_id:
                count_records = datasette.query_resource_issue_counts(resource_id)

                # The count records have structure like so:
                # [['warning', 2], ['error', 1]]
                dataset_model.warning_count = \
                    next(filter(lambda x: x[datasette.resource_issue_counts_column_map["severity"]] == "warning",
                                count_records),
                         ["warning", 0]
                    )[1]
                dataset_model.error_count = \
                    next(
                        filter(lambda x: x[datasette.resource_issue_counts_column_map["severity"]] == "error", count_records),
                        ["error", 0]
                    )[1]

            org_model.datasets.append(dataset_model)

            org_model.dataset_active_count = len(org_model.datasets)
            org_model.dataset_warning_count = len(list(filter(lambda x: x.warning_count > 0, org_model.datasets)))
            org_model.dataset_error_count = len(list(filter(lambda x: x.error_count > 0, org_model.datasets)))

        with Session(db_engine_builder) as session:
            print(org_model)
            print(org_model.datasets)
            session.merge(org_model)
            session.commit()


if __name__ == '__main__':
    populate()
