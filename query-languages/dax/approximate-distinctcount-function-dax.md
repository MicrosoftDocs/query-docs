---
description: "Learn more about: APPROXIMATEDISTINCTCOUNT"
title: "APPROXIMATEDISTINCTCOUNT function (DAX)"
---
# APPROXIMATEDISTINCTCOUNT

[!INCLUDE[applies-to-measures-columns-tables](includes/applies-to-measures-columns-tables.md)]

Returns an *estimated* count of unique values in a column. This function invokes a corresponding aggregation operation in the data source, which is optimized for query performance, but with slightly reduced accuracy. This function can be used with the following data sources: Azure SQL, Azure Synapse dedicated SQL pool, BigQuery, Databricks, and Snowflake. This function requires DirectQuery mode. Import mode and dual storage mode are not supported.
  
## Syntax  
  
```dax
APPROXIMATEDISTINCTCOUNT(<columnName>)
```
  
### Parameters  

|Term  |Description|  
|---------|---------|
|`column` | The column that contains the values to be counted. This cannot be an expression.  |

## Return value

The approximate number of distinct values in `column`.  
  
## Remarks  

The only argument to this function is a column. You can use columns containing any type of data. When the function finds no rows to count, it returns a BLANK, otherwise it returns the count of distinct values.
