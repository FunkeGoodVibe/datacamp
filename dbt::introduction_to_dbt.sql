

/*
- dbt: data build tool. 
- primarilary handles the T in ETL 
- allows easy switching between data warehouses (such as snowflake, bigquery, postgres, duckdb...). 
- provides sql collobrations
- translates between sql dialiects 


WHat does dbt do? 
- Primararily defines the data models, and transformations using sql 
- Can define the relationships between data models 
- runs the data transforamtions / converting raw data from log files into database tables. 
- can test for data quality requirements 

dbt-core 


dbt 
dbt --version
dbt -h

dbt init (create a new project) 
dbt init ><project_name>


dbt is used by anyone who wants to transform data. 


Defining configuration with project profiles 

- A profile represents a given deployment scenario: 
  - development 
  - stating / test 
  - production 

a dbt project can have multiple profiles 
defined in the profiles.yml file. 

marketing_campaign_results: 
    target: dev 
    outputs: 
        dev: 
            type: duckdb 
            path: dbt.duckdb
        prod: 
            type: snowflake  
            ...
        user: my_user
        password: my_password
        port: 5432
        dbname: my_database
        schema: analytics_dev


YAML - yet another markup language. Text file, where spacing matters (like python). Used in many development scenarios for configuration. 

DuckDB: Open source, serverless database (similar to SQLlite)
    - Designed for analytics 
    - Vectorised (meaning FAST)
    - Easy to use


*/ 





-- Joining Data in SQL 
-- Introduction to Shell 
-- Data Warehouses concepts


/*
A data warehouse is a central repository of integrated data from one or more disparate sources, used to store large amounts of historical data for reporting, analysis, and business intelligence activities. It consolidates data, making it a "single source of truth" for making informed decisions, enabling trend analysis, and improving operational efficiency. 
Key functions and benefits
Data consolidation: It pulls data from various operational systems, such as sales, marketing, and finance, into a single, unified location.
Historical data storage: Unlike regular databases that are optimized for transactions, a data warehouse stores historical data, allowing businesses to analyze trends over time.
Improved performance: By separating analytical processing from operational systems, data warehouses prevent performance degradation in either system.
Enhanced data quality: The data is cleaned, transformed, and standardized during the loading process to ensure consistency and accuracy across the organization.
Business intelligence: It serves as the foundation for business intelligence tools, enabling users to run queries, create reports, and perform analysis to gain valuable insights.
Support for advanced analytics: It provides the historical and real-time data needed to develop and train machine learning models and predictive analytics algorithms. 
How it works
Extraction: Data is extracted from various source systems.
Transformation: The data is cleaned, transformed, and standardized for consistency and quality.
Loading: The transformed data is loaded into the central data warehouse, where it is organized for analysis.
Analysis: Business users and analysts can then access the data in the warehouse to run queries and reports. 
Data warehouse vs. data lake
A data warehouse stores structured data that has been formatted for a specific purpose, making it ideal for business intelligence and reporting.
A data lake stores vast amounts of raw, unstructured data in its original format, with the purpose often not yet defined. 
*/ 

dbt: 
  An ELT tool for managing your SQL transformations and
  data models. For more documentation on these
  commands, visit: docs.getdbt.com



Options:
  --cache-selected-only / --no-cache-selected-only
                                  At start of run,
                                  populate relational
                                  cache only for
                                  schemas containing
                                  selected nodes, or
                                  for all schemas of
                                  interest.
  -d, --debug / --no-debug        Display debug logging
                                  during dbt execution.
                                  Useful for debugging
                                  and making bug
                                  reports.
  -x, --fail-fast / --no-fail-fast
                                  Stop execution on
                                  first failure.
  --log-cache-events / --no-log-cache-events
                                  Enable verbose
                                  logging for
                                  relational cache
                                  events to help when
                                  debugging.
  --log-format [text|debug|json|default]
                                  Specify the format of
                                  logging to the
                                  console and the log
                                  file. Use --log-
                                  format-file to
                                  configure the format
                                  for the log file
                                  differently than the
                                  console.
  --log-format-file [text|debug|json|default]
                                  Specify the format of
                                  logging to the log
                                  file by overriding
                                  the default value and
                                  the general --log-
                                  format setting.
  --log-level [debug|info|warn|error|none]
                                  Specify the minimum
                                  severity of events
                                  that are logged to
                                  the console and the
                                  log file. Use --log-
                                  level-file to
                                  configure the
                                  severity for the log
                                  file differently than
                                  the console.
  --log-level-file [debug|info|warn|error|none]
                                  Specify the minimum
                                  severity of events
                                  that are logged to
                                  the log file by
                                  overriding the
                                  default value and the
                                  general --log-level
                                  setting.
  --log-path PATH                 Configure the 'log-
                                  path'. Only applies
                                  this setting for the
                                  current run.
                                  Overrides the
                                  'DBT_LOG_PATH' if it
                                  is set.
  --partial-parse / --no-partial-parse
                                  Allow for partial
                                  parsing by looking
                                  for and writing to a
                                  pickle file in the
                                  target directory.
                                  This overrides the
                                  user configuration
                                  file.
  --populate-cache / --no-populate-cache
                                  At start of run, use
                                  `show` or
                                  `information_schema`
                                  queries to populate a
                                  relational cache,
                                  which can speed up
                                  subsequent
                                  materializations.
  --print / --no-print            Output all {{ print()
                                  }} macro calls.
  --printer-width INTEGER         Sets the width of
                                  terminal output
  -q, --quiet / --no-quiet        Suppress all non-
                                  error logging to
                                  stdout. Does not
                                  affect {{ print() }}
                                  macro calls.
  -r, --record-timing-info PATH   When this option is
                                  passed, dbt will
                                  output low-level
                                  timing stats to the
                                  specified file.
                                  Example: `--record-
                                  timing-info
                                  output.profile`
  --send-anonymous-usage-stats / --no-send-anonymous-usage-stats
                                  Send anonymous usage
                                  stats to dbt Labs.
  --static-parser / --no-static-parser
                                  Use the static
                                  parser.
  --use-colors / --no-use-colors  Specify whether log
                                  output is colorized
                                  in the console and
                                  the log file. Use
                                  --use-colors-
                                  file/--no-use-colors-
                                  file to colorize the
                                  log file differently
                                  than the console.
  --use-colors-file / --no-use-colors-file
                                  Specify whether log
                                  file output is
                                  colorized by
                                  overriding the
                                  default value and the
                                  general --use-
                                  colors/--no-use-
                                  colors setting.
  --use-experimental-parser / --no-use-experimental-parser
                                  Enable experimental
                                  parsing features.
  -V, -v, --version               Show version
                                  information and exit
  --version-check / --no-version-check
                                  If set, ensure the
                                  installed dbt version
                                  matches the require-
                                  dbt-version specified
                                  in the
                                  dbt_project.yml file
                                  (if any). Otherwise,
                                  allow them to differ.
  --warn-error                    If dbt would normally
                                  warn, instead raise
                                  an exception.
                                  Examples include
                                  --select that selects
                                  nothing,
                                  deprecations,
                                  configurations with
                                  no associated models,
                                  invalid test
                                  configurations, and
                                  missing sources/refs
                                  in tests.
  --warn-error-options WARNERROROPTIONSTYPE
                                  If dbt would normally
                                  warn, instead raise
                                  an exception based on
                                  include/exclude
                                  configuration.
                                  Examples include
                                  --select that selects
                                  nothing,
                                  deprecations,
                                  configurations with
                                  no associated models,
                                  invalid test
                                  configurations, and
                                  missing sources/refs
                                  in tests. This
                                  argument should be a
                                  YAML string, with
                                  keys 'include' or
                                  'exclude'. eg.
                                  '{"include": "all",
                                  "exclude": ["NoNodesF
                                  orSelectionCriteria"]
                                  }'
  --write-json / --no-write-json  Whether or not to
                                  write the
                                  manifest.json and
                                  run_results.json
                                  files to the target
                                  directory
  -h, --help                      Show this message and
                                  exit.

Commands:
  build          Run all seeds, models, snapshots,...
  clean          Delete all folders in the...
  compile        Generates executable SQL from...
  debug          Test the database connection and...
  deps           Pull the most recent version of...
  docs           Generate or serve the...
  init           Initialize a new dbt project.
  list           List the resources in your project
  parse          Parses the project and provides...
  run            Compile SQL and execute against...
  run-operation  Run the named macro with any...
  seed           Load data from csv files into...
  show           Generates executable SQL for a...
  snapshot       Execute snapshots defined in your...
  source         Manage your project's sources
  test           Runs tests on data in deployed...

  Specify one of these sub-commands and you can find
  more help from there.