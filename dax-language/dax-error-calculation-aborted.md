---
title: "DAX Error: CALCULATION ABORTED: MdxScript(instance) (00, 0) Function ‘DATEADD’ only works with contiguous date selections. | Microsoft Docs"
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
ms.assetid: d2c2b44d-f2ca-4ec5-9e6a-e090af0e8d64
caps.latest.revision: 7
author: "Minewiskan"
ms.author: "owend"
manager: "mblythe"
---
# DAX Error: CALCULATION ABORTED: MdxScript(instance) (00, 0) Function ‘DATEADD’ only works with contiguous date selections.
This error can occur when attempting to create (design-time) or use (run-time) a calculated field with a DAX time-intelligence function. In each case, an incontiguous date range is being passed to the time-intelligence function.  
  
## Cause at run-time  
This error can be displayed when a calculated field with a [Time Intelligence Functions &#40;DAX&#41;](../DAX/time-intelligence-functions-dax.md) is placed in the VALUES area of a PivotTable and date fields such as month or quarter are selected as slicers or filters before selecting a year.  
  
For example, the following calculated field formula calculates a total sales amount for the prior year; it contains a time-intelligence function DATEADD():  
  
`Prior Year Sales:=CALCULATE([Total Sales], DATEADD(Calendar[Date],-1,YEAR))`  
  
If we add Prior Year Sales to VALUES, then add Month as a slicer *before* adding Year and then selecting a particular year, this error can be displayed. The same applies if adding Month or Quarter to the Filters area before adding Year.  
  
![PivotTable with Month slicer](../DAX/media/daxerror-pivottable-slicer-month.png "PivotTable with Month slicer")  
  
This error can be returned:  
  
![DATEADD error](../DAX/media/daxerror.png "DATEADD error")  
  
In this case, the [DATEADD Function &#40;DAX&#41;](../DAX/dateadd-function-dax.md) in the Prior Year Sales formula can only determine an incontiguous list of dates: one month of dates from each year. There are dates for each month in every year, but those dates are not contiguous. For example, all March dates in 2011, 2012, 2013 don’t form a contiguous date range.  
  
## How to fix this error at run-time  
Using the example above, first add Year as a slicer or filter and select a year, then add Month or Quarter as a slicer or filter. You can then select one or more months or quarters to slice or filter on for the year selected.  
  
## Cause at design-time  
Time-intelligence functions require a date column specified for the ‘date’ argument. That date column must have a contiguous range of dates. This error can be returned if there is an incontiguous date value in one or more rows in the date column.  
  
If you imported your date table from a data source, many organizations run special processes that scan tables in databases for invalid values and replace those with a particular value. That is, if an invalid date is found, it is assigned a particular date value. This is often referred to as data cleansing or ETL. In either case, an invalid value found by an ETL process or the value it replaces with will be often be incontiguous.  
  
For example, in the following table, an invalid value was replaced with an easily identifiable value. The value 01/01/1900 while matches the date data type for the column, is incontiguous with the date values in the previous and next row:  
  
|Date|  
|--------|  
|01/01/2012|  
|01/02/2012|  
|01/03/2012|  
|**01/01/1900**|  
|01/05/2012|  
|01/06/2012|  
|01/07/2012|  
  
Users often specify a date column in a fact table as the date argument to a time-intelligence function. Because each row in a fact table often represents a single transaction or record at a particular time, those date values are often incontiguous. The date column specified as an argument to a time-intelligence function should always be in a separate, related date table.  
  
## How to fix this error at design-time  
If your date table was imported from a data source, use **Refresh** in Power Pivot to re-import any changes found at the source.  
  
Check your date column’s values to make sure they are in a contiguous order. If an incontiguous value is found, it will have to be corrected at the source and the date table will have to be refreshed.  
  
Create a separate date table and date column in your data model. Specify the new date column as the date argument in the formula causing the error.  Date tables are easy to create and add to a data model. For more information, see [Understand and create date tables in Power Pivot](http://office.microsoft.com/excel-help/understand-and-create-date-tables-in-power-pivot-in-excel-2013-HA104139621.aspx?CTT=5&origin=HA104146216).  
  
For more information, see [Dates in Power Pivot](http://office.microsoft.com/en-us/excel-help/dates-in-power-pivot-HA102836917.aspx?CTT=5&origin=HA104220543).  
  
