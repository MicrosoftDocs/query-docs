---
title: "DISTINCT Function (DAX) | Microsoft Docs"
ms.custom: ""
ms.date: "12/28/2017"
ms.prod: "powerbi"
ms.reviewer: ""
ms.suite: ""
ms.technology: 
  - "analysis-services"
  - "daxlang"
ms.tgt_pltfrm: ""
ms.topic: "language-reference"
f1_keywords: 
  - "sql13.as.daxref.DISTINCT.f1"
helpviewer_keywords: 
  - "DISTINCT function"
  - "Unique values"
ms.assetid: e4f1e082-873d-40a7-a7d3-5e231ce14053
caps.latest.revision: 6
author: "Minewiskan"
ms.author: "owend"
manager: "mblythe"
---
# DISTINCT Function (DAX)
Returns a one-column table that contains the distinct values from the specified column. In other words, duplicate values are removed and only unique values are returned.  
  
> [!NOTE]  
> This function cannot be used to return values into a cell or column on a worksheet; rather, you nest the DISTINCT function within a formula, to get a list of distinct values that can be passed to another function and then counted, summed, or used for other operations.  
  
## Syntax  
  
```  
DISTINCT(<column>)  
```  
  
#### Parameters  
  
|Term|Definition|  
|--------|--------------|  
|**column**|The column from which unique values are to be returned. Or, an expression that returns a column.|  
  
## Return Value  
A column of unique values.  
  
## Remarks  
The results of DISTINCT are affected by the current filter context. For example, if you use the formula in the following example to create a measure, the results would change whenever the table was filtered to show only a particular region or a time period.  
  
## Related Functions  
The VALUES function is similar to DISTINCT; it can also be used to return a list of unique values, and generally will return exactly the same results as DISTINCT. However, in some context VALUES will return one additional special value. For more information, see [VALUES Function &#40;DAX&#41;](../DAX/values-function-dax.md).  
  
## Example  
The following formula counts the number of unique customers who have generated orders over the internet channel. The table that follows illustrates the possible results when the formula is added to a PivotTable.  
  
```  
=COUNTROWS(DISTINCT(InternetSales_USD[CustomerKey]))  
```  
Note that you cannot paste the list of values that DISTINCT returns directly into a column. Instead, you pass the results of the DISTINCT function to another function that counts, filters, or aggregates values by using the list. To make the example as simple as possible, here the table of distinct values has been passed to the COUNTROWS function.  
  
|Unique Internet customers|Column Labels||||  
|-----------------------------|-----------------|----|----|----|  
|Row Labels|Accessories|Bikes|Clothing|Grand Total|  
|2005||1013||1013|  
|2006||2677||2677|  
|2007|6792|4875|2867|9309|  
|2008|9435|5451|4196|11377|  
|Grand Total|15114|9132|6852|18484|  
  
Also, note that the results are not additive. That is to say, the total number of unique customers in *2007* is not the sum of unique customers of *Accessories*, *Bikes* and *Clothing* for that year. The reason is that a customer can be counted in multiple groups.  
  
## See Also  
[Filter Functions &#40;DAX&#41;](../DAX/filter-functions-dax.md)  
[FILTER Function &#40;DAX&#41;](../DAX/filter-function-dax.md)  
[RELATED Function &#40;DAX&#41;](../DAX/related-function-dax.md)  
[VALUES Function &#40;DAX&#41;](../DAX/values-function-dax.md)  
  
