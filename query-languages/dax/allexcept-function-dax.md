---
title: "ALLEXCEPT Function (DAX) | Microsoft Docs"
ms.service: powerbi 

ms.date: 11/07/2018
ms.reviewer: owend
ms.topic: reference
author: minewiskan
ms.author: owend
manager: kfile
---
# ALLEXCEPT Function (DAX)
Removes all context filters in the table except filters that have been applied to the specified columns.  
  
## Syntax  
  
```dax
ALLEXCEPT(<table>,<column>[,<column>[,…]])  
```
  
#### Parameters  
  
|Term|Definition|  
|--------|--------------|  
|table|The table over which all context filters are removed, except filters on those columns that are specified in subsequent arguments.|  
|column|The column for which context filters must be preserved.|  
  
The first argument to the ALLEXCEPT function must be a reference to a base table; all subsequent arguments must be references to base columns. You cannot use table expressions or column expressions with the ALLEXCEPT function.  
  
## Return value  
A table with all filters removed except for the filters on the specified columns.  
  
## Remarks  
This function is not used by itself, but serves as an intermediate function that can be used to change the set of results over which some other calculation is performed.  
  
As described in the following table, you can use the ALL and ALLEXCEPT functions in different scenarios.  
  
|Function and Usage|Description|  
|----------------------|---------------|  
|ALL(Table)|Removes all filters from the specified table. In effect, ALL(Table) returns all of the values in the table, removing any filters from the context that otherwise might have been applied.<br /><br />This function is useful when you are working with many levels of grouping, and want to create a calculation that creates a ratio of an aggregated value to the total value.|  
|ALL (Column[, Column[, …]])|Removes all filters from the specified columns in the table; all other filters on other columns in the table still apply. All column arguments must come from the same table.<br /><br />The ALL(Column) variant is useful when you want to remove the context filters for one or more specific columns and to keep all other context filters.|  
|ALLEXCEPT(Table, Column1 [,Column2]...)|Removes all context filters in the table except filters that are applied to the specified columns.<br /><br />This is a convenient shortcut for situations in which you want to remove the filters on many, but not all, columns in a table.|  
  
## Example  
The following example presents a formula that you can use in a measure.  
  
The formula sums SalesAmount_USD and uses the ALLEXCEPT function to remove any context filters on the DateTime table except if the filter has been applied to the CalendarYear column.  
  
> [!NOTE]  
> The above example uses the tables, ResellerSales_USD and DateTime from the DAX sample workbook. For more information about samples, see [Get Sample Data](https://go.microsoft.com/fwlink/?LinkId=164474) .  
  
```dax
=CALCULATE(SUM(ResellerSales_USD[SalesAmount_USD]), ALLEXCEPT(DateTime, DateTime[CalendarYear]))  
```

Because the formula uses ALLEXCEPT, whenever any column but CalendarYear from the table DateTime is used to slice the PivotTable, the formula will remove any slicer filters, providing a value equal to the sum of SalesAmount_USD for the column label value, as shown in Table 1.  
  
However, if the column CalendarYear is used to slice the PivotTable, the results are different. Because CalendarYear is specified as the argument to ALLEXCEPT, when the data is sliced on the year, a filter will be applied on years at the row level, as shown in Table 2. The user is encouraged to compare these tables to understand the behavior of ALLEXCEPT().  
  
## See Also  
[Filter Functions &#40;DAX&#41;](filter-functions-dax.md)  
[ALL Function &#40;DAX&#41;](all-function-dax.md)  
[FILTER Function &#40;DAX&#41;](filter-function-dax.md)  
  
