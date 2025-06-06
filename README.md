# LVTShift

**LVTShift** is a toolkit for modeling Land Value Tax (LVT) shifts in counties across the United States. It provides utilities for fetching, processing, and analyzing parcel, tax, and census data, and includes example workflows for real-world counties. LVTShift is created and maintained by the Center for Land Economics ([landeconomics.org](https://landeconomics.org))

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

## Running the Web App

A simple Flask application is included in `webapp/app.py` that lets you either upload a parcel CSV **or provide a direct URL** to the data and immediately model a split-rate tax. To launch it:

```sh
pip install -r requirements.txt
python webapp/app.py
```

Then open [http://localhost:5000](http://localhost:5000) in your browser, either paste the link to your CSV or upload the file, and enter the column names along with the current revenue. The app will return the calculated millage rates and let you download a CSV with parcel-level results.

## Deploying to Heroku

To make the web app accessible on the public web, you can deploy it to a platform like **Heroku**:

1. [Create a free Heroku account](https://signup.heroku.com/) and install the [Heroku CLI](https://devcenter.heroku.com/articles/heroku-cli).
2. From your project directory, run `heroku create` to create a new app.
3. Push your code to Heroku (the repository includes a `Procfile` and `runtime.txt`):
   ```sh
   git push heroku HEAD:main
   ```
4. Heroku will install the dependencies from `requirements.txt` and start `gunicorn` via the `Procfile`.
5. Once deployment completes, run `heroku open` or visit the URL provided by the CLI to access the app in your browser.

Other platforms such as Fly.io or Render can be used similarly—just ensure the process runs `gunicorn webapp.app:app` and installs the Python dependencies.

## Deploying without the CLI

If you prefer to avoid command-line tools, you can deploy the web app entirely from the Heroku dashboard:

1. Fork this repository to your own GitHub account.
2. Log into [Heroku](https://dashboard.heroku.com/), click **New** → **Create new app**.
3. In the **Deploy** tab, choose **GitHub** as the deployment method and connect your fork.
4. Select the branch to deploy (usually `main`) and click **Deploy Branch**.
5. After the build finishes, click **Open App** to access your public URL.

You can also import the repository into an online IDE such as [replit.com](https://replit.com/) which automatically hosts the Flask app and provides a shareable URL.

### Launch on Binder

For a quick, no-signup option you can open the repository on [Binder](https://mybinder.org). Construct a link in the form:

```
https://mybinder.org/v2/gh/<your-github-username>/LVTShift/HEAD
```

Replace `<your-github-username>` with your GitHub handle. Binder installs the dependencies from `requirements.txt` and gives you a temporary Jupyter environment. The web app can be started from there and accessed via the temporary URL Binder provides.

## Running Tests

Install the test requirements and run `pytest`:

```sh
pip install -r requirements.txt
pytest
```

The minimal suite verifies the core tax-calculation utilities.
