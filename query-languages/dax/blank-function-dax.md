---
title: "BLANK Function (DAX) | Microsoft Docs"
ms.service: powerbi 

ms.date: 11/07/2018
ms.reviewer: owend
ms.topic: reference
author: minewiskan
ms.author: owend
manager: kfile
---
# BLANK Function (DAX)
Returns a blank.  
  
## Syntax  
  
```dax
BLANK()  
```
  
## Return Value  
A blank.  
  
## Remarks  
Blanks are not equivalent to nulls. DAX uses blanks for both database nulls and for blank cells in Excel. For more information, see [Data Types Supported (SSAS Tabular)](https://msdn.microsoft.com/en-us/92993f7b-7243-4aec-906d-0b0379798242).  
  
Some DAX functions treat blank cells somewhat differently from Microsoft Excel. Blanks and empty strings ("") are not always equivalent, but some operations may treat them as such. For details on the behavior of an individual function or operator, see [DAX Function Reference](dax-function-reference.md).  
  
## Example  
The following example illustrates how you can work with blanks in formulas. The formula calculates the ratio of sales between the Resellers and the Internet channels. However, before attempting to calculate the ratio the denominator should be checked for zero values. If the denominator is zero then a blank value should be returned; otherwise, the ratio is calculated.  
  
```dax
=IF( SUM(InternetSales_USD[SalesAmount_USD])= 0   , BLANK()   , SUM(ResellerSales_USD[SalesAmount_USD])/SUM(InternetSales_USD[SalesAmount_USD])   )  
```

The table shows the expected results when this formula is used to create a PivotTable.  
  
|Reseller to Internet sales ratio|Column Labels||||  
|------------------------------------|-----------------|----|----|----|  
|Row Labels|Accessories|Bikes|Clothing|Grand Total|  
|2005||2.65||2.89|  
|2006||3.33||4.03|  
|2007|1.04|2.92|6.63|3.51|  
|2008|0.41|1.53|2.00|1.71|  
|Grand Total|0.83|2.51|5.45|2.94|  
  
Note that, in the original data source, the column evaluated by the BLANK function might have included text, empty strings, or nulls. If the original data source was a SQL Server database, nulls and empty strings are different kinds of data. However, for this operation an implicit type cast is performed and DAX treats them as the same.  
  
## See Also  
[Text Functions &#40;DAX&#41;](text-functions-dax.md)  
[ISBLANK Function &#40;DAX&#41;](isblank-function-dax.md)  
  
