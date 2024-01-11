# Sample data for AgML crop yield forecasting
Sample data for grain maize or corn in the United States.

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

### Features included in grain_maize_US.csv
This file excludes yield trend (features).

For leave-one-out cross-validation.

## Raw data
Included in county-data-US.zip. For AgML, we only use the following:
* METEO_COUNTY_US.csv: Meteo data including maximum, minimum, average daily air temperature (Îõ); sum of daily precipitation (PREC) (mm); sum of daily evapotranspiration of short vegetation (ET0) (Penman-Monteith, Allen et al., (1998)) (mm); climate water balance = (PREC - ET0) (mm). Source: Boogaard et al. (2022).
* REMOTE_SENSING_COUNTY_US.csv: Fraction of Absorbed Photosynthetically Active Radiation (Smoothed) (FAPAR). Source: Copernicus GLS (2020).
* SOIL_COUNTY_US.csv: Soil water holding capacity. Source: WISE Soil Property Database (Batjes, 2016).
* YIELD_COUNTY_US.csv: County yield statistics (bushels/acre). Source: NASS (USDA-NASS, 2022).
