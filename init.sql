CREATE TABLE organisations (
  id VARCHAR(100) PRIMARY KEY,
  name VARCHAR(100),
  dataset_active_count INTEGER,
  dataset_warning_count INTEGER,
  dataset_error_count INTEGER
);

INSERT INTO organisations (id, name, dataset_active_count, dataset_warning_count, dataset_error_count) VALUES
  ('BOR', 'Borchester Borough Council Planning Authority', 20, 2, 1),
  ('NPT', 'Neath Port Talbot Planning Authority', 30, 5, 2);

CREATE TABLE datasets (
  /*id BIGSERIAL PRIMARY KEY,*/
  organisation_id VARCHAR(100) REFERENCES organisations(id),
  dataset VARCHAR(100),
  record_count INTEGER,
  warning_count INTEGER,
  error_count INTEGER,
  PRIMARY KEY(organisation_id, dataset)
);

INSERT INTO datasets (organisation_id, dataset, record_count, warning_count, error_count) VALUES
  ('BOR', 'Tree Preservation Zone', 500, 500, 1),
  ('BOR', 'Tree', 2000, 4000, 0),
  ('NPT', 'Tree Preservation Zone', 2000, 4000, 1),
  ('NPT', 'Tree', 2000, 4000, 1);