---
title: "DISTINCT (column) function (DAX) | Microsoft Docs"
ms.service: powerbi 
ms.date: 01/06/2021
ms.reviewer: owend
ms.topic: reference
author: minewiskan
ms.author: owend

---
# DISTINCT (column)

Returns a one-column table that contains the distinct values from the specified column. In other words, duplicate values are removed and only unique values are returned.  
  
> [!NOTE]  
> This function cannot be used to Return values into a cell or column on a worksheet; rather, you nest the DISTINCT function within a formula, to get a list of distinct values that can be passed to another function and then counted, summed, or used for other operations.  
  
## Syntax  
  
```dax
DISTINCT(<column>)  
```
  
### Parameters  
  
|Term|Definition|  
|--------|--------------|  
|column|The column from which unique values are to be returned. Or, an expression that returns a column.|  
  
## Return value

A column of unique values.  
  
## Remarks

- The results of DISTINCT are affected by the current filter context. For example, if you use the formula in the following example to create a measure, the results would change whenever the table was filtered to show only a particular region or a time period.  

- [!INCLUDE [function-not-supported-in-directquery-mode](includes/function-not-supported-in-directquery-mode.md)]

## Related functions

There is another version of the DISTINCT function, [DISTINCT (table)](distinct-table-function-dax.md), that returns a table by removing duplicate rows from another table or expression..

The VALUES function is similar to DISTINCT; it can also be used to return a list of unique values, and generally will return exactly the same results as DISTINCT. However, in some context VALUES will return one additional special value. For more information, see [VALUES function](values-function-dax.md).  
  
## Example

The following formula counts the number of unique customers who have generated orders over the internet channel. The table that follows illustrates the possible results when the formula is added to a PivotTable.  
  
```dax
= COUNTROWS(DISTINCT(InternetSales_USD[CustomerKey]))  
```

You cannot paste the list of values that DISTINCT returns directly into a column. Instead, you pass the results of the DISTINCT function to another function that counts, filters, or aggregates values by using the list. To make the example as simple as possible, here the table of distinct values has been passed to the COUNTROWS function.  
  
|Row Labels|Accessories|Bikes|Clothing|Grand Total|  
|-----------------------------|-----------------|----|----|----|  
|2005||1013||1013|  
|2006||2677||2677|  
|2007|6792|4875|2867|9309|  
|2008|9435|5451|4196|11377|  
|Grand Total|15114|9132|6852|18484|  
  
Also, note that the results are not additive. That is to say, the total number of unique customers in *2007* is not the sum of unique customers of *Accessories*, *Bikes* and *Clothing* for that year. The reason is that a customer can be counted in multiple groups.  
  
## See also

[Filter functions](filter-functions-dax.md)  
[FILTER function](filter-function-dax.md)  
[RELATED function](related-function-dax.md)  
[VALUES function](values-function-dax.md)  
