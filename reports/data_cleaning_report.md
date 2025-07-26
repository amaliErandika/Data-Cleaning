# 🧹 Data Cleaning Report - Hotel Booking Demand Dataset

**Prepared by:** G.A.E.Ganhewage  
**Date:** 2020/07/20

---

## 1. Original Dataset Statistics

- **Total Rows**: 119,390  
- **Total Columns**: 32  
- **Initial Issues Detected**:
  - Missing values
  - Duplicate entries
  - Outliers in numerical columns
  - Inconsistent categorical entries
  - Illogical values (e.g., total guests = 0)

---

## 2. Issues Identified and Their Impact

| Issue                           | Description                                                                 |
|--------------------------------|-----------------------------------------------------------------------------|
| Missing Values                 | Found in `children`, `country`, `agent`, and `company` columns             |
| Duplicate Records              | Exact duplicates and near-duplicates identified                            |
| Outliers                       | Extreme values in `adr`, `lead_time`, `babies`, etc.                       |
| Categorical Inconsistencies    | Unstandardized entries in `meal`, `country`, `distribution_channel`, etc. |
| Illogical Values               | Rows with adults=0, children=0, and babies=0 (i.e., no guests)             |
| Date Format Issues             | Arrival date was split into day, month, and year columns                   |

---

## 3. Cleaning Strategies Applied

| Cleaning Step                      | Strategy Used                                                                 |
|-----------------------------------|--------------------------------------------------------------------------------|
| Missing Value Handling            | Filled missing `children` with 0, agent/company with 0, country with 'Unknown' |
| Duplicate Removal                 | Dropped exact duplicates                                                      |
| Outlier Treatment                 | Used IQR and Z-score methods; capped/extreme values removed as needed         |
| Categorical Standardization       | Stripped spaces, capitalized values, mapped aliases                           |
| Illogical Row Removal             | Removed rows with total guests = 0                                            |
| Date Unification                  | Created unified `arrival_date` from day, month, and year columns              |
| New Feature                       | Added `total_guests = adults + children + babies`                             |

---

## 4. Final Dataset Statistics

- **Total Rows After Cleaning**: 87377
- **Total Columns**: 33
- **Duplicates Removed**: 7
- **Missing Values Remaining**: 0
- **Invalid Rows Removed**: 7

---

## 5. Assumptions Made During Cleaning

- Rows with no guests are considered invalid.
- Missing `children`, `agent`, or `company` implies zero or not applicable.
- All dates fall within a valid range (2015–2017).
- Extreme outliers in `adr` are likely due to data entry errors.

---

## 6. Output Files

- `hotel_booking_cleaned.csv` – Cleaned dataset  
- `data_dictionary_cleaned.md` – Describes each field in the cleaned dataset

