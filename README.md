
# Python SQLite Database Interaction

## Deaths & Insurance Database Overview

This database, "Deaths&Insurance.db", provides insights into potentially excess deaths and health insurance coverage across the United States. It is comprised of two tables:

1. **Potentially_excess_deaths** contains data related to observed deaths, expected deaths, and potentially excess deaths for different states, age ranges, and causes of death.
2. **Health_Insurance_Coverage** provides data about health insurance coverage, uninsured rates, and various insurance metrics for different states.

## Tables Description

**Potentially_excess_deaths**
- Year: The year of data collection.
- CauseofDeath: Cause of death.
- State: State name.
- StateFIPSCode: Federal Information Processing Standards (FIPS) code for the state.
- HHSRegion: Health and Human Services (HHS) Region code.
- AgeRange: Age range of the deceased individuals.
- Benchmark: Data benchmark.
- Locality: Locality type.
- ObservedDeaths: The number of observed deaths.
- Population: The population of the locality or state.
- ExpectedDeaths: The number of expected deaths.
- PotentiallyExcessDeaths: The number of potentially excess deaths.
- PercentPotentiallyExcessDeaths: The percentage of potentially excess deaths.

**Health_Insurance_Coverage**
- State: State name.
- Various columns related to uninsured rates, insurance coverage changes, employer health insurance coverage, marketplace health insurance coverage, tax credits, Medicaid and Medicare enrollment for different years.

## The SQL Query

The provided SQL query aims to join the two tables on the State column and aggregate data to find the total observed deaths, potentially excess deaths, and the average percentage of potentially excess deaths for each state in 2015. Additionally, it fetches relevant health insurance data from 2015. The results are sorted based on the total number of potentially excess deaths.


