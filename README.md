# LVTShift

**LVTShift** is a toolkit for modeling Land Value Tax (LVT) shifts in counties across the United States. It provides utilities for fetching, processing, and analyzing parcel, tax, and census data, and includes example workflows for real-world counties. LVTShift is created and maintained by the Center for Land Economics ([landeconomics.org](url))

## Features

- Fetch and join Census demographic and boundary data (`census_utils.py`)
- Model property tax and LVT scenarios (`lvt_utils.py`)
- Example: South Bend, IN analysis notebook (`examples/southbend.ipynb`)

## Getting Started

1. Clone the repo:
   ```sh
   git clone https://github.com/YOURUSERNAME/LVTShift.git
   cd LVTShift
   ```

2. Install dependencies:
   ```sh
   pip install -r requirements.txt
   ```

3. Explore the example notebook:
   ```sh
   cd examples
   jupyter notebook southbend.ipynb
   ```

## File Structure
- `census_utils.py` - Fetches demographic data and boundaries from the U.S. Census API.
- `lvt_utils.py` - Functions to calculate current taxes and model split-rate or land value tax scenarios.
- `cloud_utils.py` - Utilities for downloading data from ArcGIS services and saving to Azure Blob Storage.
- `examples/` - Example notebooks demonstrating workflows (currently includes `southbend.ipynb`).
- `PROGRESS.md` - Ongoing notes about repository development and next steps.

## Typical Workflow
1. **Define Policy**: Decide whether the shift is revenue neutral and choose the
   land-to-building rate ratio (e.g., 4:1). Identify how exemptions and caps
   should apply.
2. **Gather Data**: Locate your county's parcel dataset from its GIS portal or
   assessor's office. The example notebook demonstrates how to pull data from an
   ArcGIS API.
3. **Recreate Current Taxes**: Use `calculate_current_tax` to verify that your
   dataset matches published revenue figures.
4. **Model the Shift**: Apply `model_split_rate_tax` with your policy settings
   to compute new taxes for each parcel.
5. **Analyze Results**: Summarize impacts by neighborhood or property type and
   join Census demographics using `census_utils.py` for further insight.

These steps mirror the methodology explained in the accompanying article on
Progress and Poverty, which walks through the South Bend example in detail.
