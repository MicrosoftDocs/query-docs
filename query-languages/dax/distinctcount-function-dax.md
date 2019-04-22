---
title: "DISTINCTCOUNT function (DAX) | Microsoft Docs"
ms.service: powerbi 
ms.date: 04/22/2019
ms.reviewer: owend
ms.topic: reference
author: minewiskan
ms.author: owend
manager: kfile
---
# DISTINCTCOUNT
Counts the number of distinct values in a column.  
  
## Syntax  
  
```dax
DISTINCTCOUNT(<column>)  
```
  
#### Parameters  

|Term  |Description|  
|---------|---------|
|column     | The column that contains the values to be counted |        

  
## Return value  
The number of distinct values in *column*.  
  
## Remarks  
The only argument allowed to this function is a column. You can use columns containing any type of data. When the function finds no rows to count, it returns a BLANK, otherwise it returns the count of distinct values.  
  
## Example  
The following example shows how to count the number of distinct sales orders in the column ResellerSales_USD[SalesOrderNumber].  
  
```dax
=DISTINCTCOUNT(ResellerSales_USD[SalesOrderNumber])  
```dax
Using the above measure in a table with calendar year in the side and product category on top gives the following results:  
  
|**Distinct Reseller Orders count**|**Column Labels**||||||  
|-|-|-|-|-|-|-|  
|**Row Labels**|**Accessories**|**Bikes**|**Clothing**|**Components**||**Grand Total**|  
|2005|135|345|242|205||366|  
|2006|356|850|644|702||1015|  
|2007|531|1234|963|1138||1521|  
|2008|293|724|561|601||894|  
||||||1|1|  
|**Grand Total**|**1315**|**3153**|**2410**|**2646**|**1**|**3797**|  
  
In the above example, note that the rows Grand Total numbers do not add up, this happens because the same order might contain line items, in the same order, from different product categories.  
  
## See also  
[COUNT function &#40;DAX&#41;](count-function-dax.md)  
[COUNTA function &#40;DAX&#41;](counta-function-dax.md)  
[COUNTAX function &#40;DAX&#41;](countax-function-dax.md)  
[COUNTX function &#40;DAX&#41;](countx-function-dax.md)  
[Statistical functions &#40;DAX&#41;](statistical-functions-dax.md)  
  
