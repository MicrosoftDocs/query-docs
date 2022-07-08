---
description: "Learn more about: CROSSFILTER"
title: "CROSSFILTER function | Microsoft Docs"
ms.service: powerbi 
ms.subservice: dax 
ms.date: 04/16/2021
ms.reviewer: owend
ms.topic: reference
author: minewiskan
ms.author: owend 
recommendations: false

---
# CROSSFILTER

Specifies the cross-filtering direction to be used in a calculation for a relationship that exists between two columns.  
  
## Syntax  
  
```dax
CROSSFILTER(<columnName1>, <columnName2>, <direction>)  
```
  
### Parameters  
  
|Term|Definition|  
|--------|--------------|  
|columnName1|The name of an existing column, using standard DAX syntax and fully qualified, that usually represents the many side of the relationship to be used; if the arguments are given in reverse order the function will swap them before using them. This argument cannot be an expression.|  
|columnName2|The name of an existing column, using standard DAX syntax and fully qualified, that usually represents the one side or lookup side of the relationship to be used; if the arguments are given in reverse order the function will swap them before using them. This argument cannot be an expression.|  
|Direction|The cross-filter direction to be used. Must be one of the following:<br /><br />**None** - No cross-filtering occurs along this relationship.<br /><br />**Both** - Filters on either side filters the other side.<br /><br />**OneWay** - Filters on the one side or the lookup side of a relationship filter the other side. This option cannot be used with a one-to-one relationship . Don’t use this option on a many-to-many relationship because it is unclear which side is the lookup side; use OneWay_LeftFiltersRight or OneWay_RightFiltersLeft instead.<br /><br />**OneWay_LeftFiltersRight** - Filters on the side of \<columnName1> filter the side of \<columnName2>. This option cannot be used with a one-to-one or many-to-one relationship.<br /><br />**OneWay_RightFiltersLeft** - Filters on the side of \<columnName2> filter the side of \<columnName1>. This option cannot be used with a one-to-one or many-to-one relationship.|  
  
## Return value

The function returns no value; the function only sets the cross-filtering direction for the indicated relationship, for the duration of the query.  
  
## Remarks  
  
- In the case of a 1:1 relationship, there is no difference between the one and both direction.  
  
- CROSSFILTER can only be used in functions that take a filter as an argument, for example: CALCULATE, CALCULATETABLE, CLOSINGBALANCEMONTH, CLOSINGBALANCEQUARTER, CLOSINGBALANCEYEAR, OPENINGBALANCEMONTH, OPENINGBALANCEQUARTER, OPENINGBALANCEYEAR, TOTALMTD, TOTALQTD and TOTALYTD functions.  
  
- CROSSFILTER uses existing relationships in the model, identifying relationships by their ending point columns.  
  
- In CROSSFILTER, the cross-filtering setting of a relationship is not important; that is, whether the relationship is set to filter one, or both directions in the model does not affect the usage of the function. CROSSFILTER will override any existing cross-filtering setting.  
  
- An error is returned if any of the columns named as an argument is not part of a relationship or the arguments belong to different relationships.  
  
- If CALCULATE expressions are nested, and more than one CALCULATE expression contains a CROSSFILTER function, then the innermost CROSSFILTER is the one that prevails in case of a conflict or ambiguity.  

- [!INCLUDE [function-not-supported-in-directquery-mode](includes/function-not-supported-in-directquery-mode.md)]

## Example

In the following model diagram, both DimProduct and DimDate have a single direction relationship with FactOnlineSales.  
  
![CROSSFILTER_Examp_DiagView](media/crossfilter-examp-diagview.png "CROSSFILTER_Examp_DiagView")  
  
By default, we cannot get the Count of Products sold by year:  
  
![CROSSFILTER_Examp_PivotTable1](media/crossfilter-examp-pivottable1.png "CROSSFILTER_Examp_PivotTable1")  
  
There are  two ways to get the count of products by year:  
  
- Turn on bi-directional cross-filtering on the relationship. This will change how filters work for all data between these two tables.  
  
- Use the CROSSFILTER function to change how the relationships work for just this measure.  
  
When using DAX, we can use the CROSSFILTER function to change how the cross-filter direction behaves between two columns defined by a relationship. In this case, the DAX expression looks like this:  
  
```dax
BiDi:= CALCULATE([Distinct Count of ProductKey], CROSSFILTER(FactInternetSales[ProductKey], DimProduct[ProductKey] , Both))
```

By using the CROSSFILTER function in our measure expression, we get the expected results:  
  
![CROSSFILTER_Examp_PivotTable2](media/crossfilter-examp-pivottable2.png "CROSSFILTER_Examp_PivotTable2")  
