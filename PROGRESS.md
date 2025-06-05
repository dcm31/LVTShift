# Progress Notes

## Date: 2025-06-05

### Initial Exploration
- Cloned repository `LVTShift` containing utilities for Land Value Tax modeling.
- Examined `README.md`, which outlines basic usage but is concise (30 lines).
- Reviewed main modules:
  - `census_utils.py` – functions to fetch Census data and match shapefiles to census block groups.
  - `lvt_utils.py` – functions for calculating current taxes and modeling split-rate taxes with exemptions and caps.
  - `cloud_utils.py` – utilities for downloading data from ArcGIS services and saving to Azure.
- Explored example notebook `examples/southbend.ipynb` (not opened here).
- No automated tests or requirements file found.
- Attempted to fetch blog post from substack but received HTTP 403 due to network restrictions.

### Observations / TODOs
- **Documentation**: README stops at "## File Structure"; could elaborate on directories and usage examples.
- **Testing**: No test suite is present. Future work could include adding unit tests for core functions.
- **Dependencies**: No `requirements.txt` in repo. Need to document Python packages required (pandas, geopandas, census, us, shapely, requests, azure-storage-blob, etc.).
- **Examples**: Expand on provided example or add additional notebooks for other counties.
- **Automated Data Fetch**: Ensure environment variables/keys (e.g., Census API, Azure credentials) are documented for reproducibility.

