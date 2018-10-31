---
title: "COUNTX Function (DAX) | Microsoft Docs"
ms.prod: powerbi 
ms.technology: dax
ms.date: 5/22/2018
ms.reviewer: owend
ms.topic: reference
author: minewiskan
ms.author: owend
manager: kfile
---
# COUNTX Function (DAX)
Counts the number of rows that contain a number or an expression that evaluates to a number, when evaluating an expression over a table.  
  
## Syntax  
  
```dax
COUNTX(<table>,<expression>)  
```
  
#### Parameters  
  
|Term|Definition|  
|--------|--------------|  
|**table**|The table containing the rows to be counted.|  
|**expression**|An expression that returns the set of values that contains the values you want to count.|  
  
## Return Value  
An integer.  
  
## Remarks  
The COUNTX function takes two arguments. The first argument must always be a table, or any expression that returns a table. The second argument is the column or expression that is searched by COUNTX.  
  
The COUNTX function counts only numeric values, dates, or strings. Arguments that are logical values or text that cannot be translated into numbers are not counted. If the function finds no rows to count, it returns a blank.  When there are rows, but none meets the specified criteria, then the function returns 0.  
  
If you want to count logical values, or text, use the COUNTA or COUNTAX functions.  
  
## Example  
The following formula returns a count of all rows in the Product table that have a list price.  
  
```dax
=COUNTX(Product,[ListPrice])  
```
  
## Example  
The following formula illustrates how to pass a filtered table to COUNTX for the first argument. The formula uses a filter expression to get only the rows in the Product table that meet the condition, ProductSubCategory = "Caps", and then counts the rows in the resulting table that have a list price. The FILTER expression applies to the table Products but uses a value that you look up in the related table, ProductSubCategory.  
  
```dax
=COUNTX(FILTER(Product,RELATED(ProductSubcategory[EnglishProductSubcategoryName])="Caps", Product[ListPrice])  
```
  
## See Also  
[COUNT Function &#40;DAX&#41;](count-function-dax.md)  
[COUNTA Function &#40;DAX&#41;](counta-function-dax.md)  
[COUNTAX Function &#40;DAX&#41;](countax-function-dax.md)  
[COUNTX Function &#40;DAX&#41;](countx-function-dax.md)  
[Statistical Functions &#40;DAX&#41;](statistical-functions-dax.md)  
  
