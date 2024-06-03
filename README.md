# Sample data for AgML crop yield forecasting
Sample data for grain maize and soft wheat. For grain maize, there is input and label data for Spain (ES) and the Netherlands (NL). Similarly, there are predesigned features and labels for the United States (US). For soft wheat, there is input and label data for Spain (ES) and the Netherlands (NL)

## Grain maize features and labels
### grain_maize_US_train.csv, grain_maize_US_test.csv
(For holdout evaluation)

Train split: 2000-2011

Test split: 2012-2018

Features from: Weather ([AgERA5](https://cds.climate.copernicus.eu/cdsapp#!/dataset/10.24381/cds.6c68c9bb?tab=overview)), Soil ([WISE](https://data.isric.org/geonetwork/srv/eng/catalog.search#/metadata/dc7b283a-8f19-45e1-aaed-e9bd515119bc)), FAPAR ([Copernicus GLS](https://land.copernicus.eu/global/products/fapar))

Also includes yield trend features (yield values of last five available years: YIELD-1, YIELD-2, ..., YIELD-5).

YIELD_TREND (a linear fit of yield trend features)

Yield (last column)

Feature design for weather and remote sensing based on crop calendar from a simple crop model called CSSF(see [reference](https://doi.org/10.24381/cds.b2f6f9f6)) (DVS changes 0-1, 1-2).

### grain_maize_US.csv
This file excludes yield trend (features).

For leave-one-out cross-validation.

## Input data and label data
* fpar: FPAR from [JRC_FPAR500m product](https://agricultural-production-hotspots.ec.europa.eu/data/indicators_fpar/).
* meteo: Weather variables and evapotranspiration from [AgERA5](https://doi.org/10.24381/cds.6c68c9bb). Evapotranspiration data is based on AgERA5 and prepared by [FAO](https://data.apps.fao.org/static/data/index.html?prefix=static%2Fdata%2Fc3s%2FAGERA5_ET0).
* ndvi: NDVI from the [NASA MOD09CMG product](https://lpdaac.usgs.gov/products/mod09cmgv061/#tools).
* soil: soil properties from the [WISE Soil project](https://data.isric.org/geonetwork/srv/eng/catalog.search#/metadata/dc7b283a-8f19-45e1-aaed-e9bd515119bc)
* soil moisture: Surface moisture and root zone moisture from [NASA GLDAS](https://ldas.gsfc.nasa.gov/gldas/model-output).
* yield: label data from harmonized subnational statistics published by [EC JRC](https://agri4cast.jrc.ec.europa.eu/DataPortal/).