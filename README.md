# Python for Data Engineering

This repository contains my hands-on projects while learning data engineering.

## Projects

### 1. CSV Data Pipeline
- Handles dirty CSV data
- Performs validation, cleaning, transformation, and aggregation
- Outputs cleaned dataset and city-wise counts

📁 Location: `csv-data-pipeline/`

### 2. JSON Data Pipeline

- Handles nested JSON data structures
- Extracts user information and project details
- Filters users based on skills (Python) and project status
- Transforms and aggregates data into structured format
- Flattens nested JSON into row-level data for analysis

📁 Location: `json-data-pipeline/`

#### Key Features
- Nested JSON parsing
- Data filtering and transformation
- Flattening data into tabular format
- Clean pipeline logic with single-pass processing

#### Example Output (Flattened)
```json
[
  {"name": "Pranav", "project": "ETL Pipeline"},
  {"name": "Amit", "project": "Backend API"}
]