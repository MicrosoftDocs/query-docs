---
description: "Learn more about: COUNTX"
title: "COUNTX function (DAX) | Microsoft Docs"
ms.service: powerbi 
ms.subservice: dax 
ms.date: 08/14/2020
ms.reviewer: owend
ms.topic: reference
author: minewiskan
ms.author: owend 
recommendations: false

---
# COUNTX

Counts the number of rows that contain a non-blank value or an expression that evaluates to a non-blank value, when evaluating an expression over a table.  
  
## Syntax  
  
```dax
COUNTX(<table>,<expression>)  
```
  
### Parameters
  
|Term|Definition|  
|--------|--------------|  
|table|The table containing the rows to be counted.|  
|expression|An expression that returns the set of values that contains the values you want to count.|  
  
## Return value

An integer.  
  
## Remarks

- The COUNTX function takes two arguments. The first argument must always be a table, or any expression that returns a table. The second argument is the column or expression that is searched by COUNTX.  
  
- The COUNTX function counts only values, dates, or strings. If the function finds no rows to count, it returns a blank. 
  
- If you want to count logical values, use the COUNTAX function.  

- [!INCLUDE [function-not-supported-in-directquery-mode](includes/function-not-supported-in-directquery-mode.md)]
  
## Example 1

The following formula returns a count of all rows in the Product table that have a list price.  
  
```dax
= COUNTX(Product,[ListPrice])  
```
  
## Example 2

The following formula illustrates how to pass a filtered table to COUNTX for the first argument. The formula uses a filter expression to get only the rows in the Product table that meet the condition, ProductSubCategory = "Caps", and then counts the rows in the resulting table that have a list price. The FILTER expression applies to the table Products but uses a value that you look up in the related table, ProductSubCategory.  
  
```dax
= COUNTX(FILTER(Product,RELATED(ProductSubcategory[EnglishProductSubcategoryName])="Caps"), Product[ListPrice])  
```
  
## See also

[COUNT function](count-function-dax.md)  
[COUNTA function](counta-function-dax.md)  
[COUNTAX function](countax-function-dax.md)  
[Statistical functions](statistical-functions-dax.md)  
