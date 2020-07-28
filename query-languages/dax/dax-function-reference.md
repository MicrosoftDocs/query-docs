---
title: "DAX function reference | Microsoft Docs"
ms.service: powerbi 
ms.date: 07/24/2020
ms.reviewer: owend
ms.topic: reference
author: minewiskan
ms.author: owend

---
# DAX function reference

This function reference provides detailed information including syntax, parameters, Return values, and examples for each of the over 200 functions used in Data Analysis Expression (DAX) formulas.  

> [!IMPORTANT]
> Not all DAX functions are supported or included in earlier versions of Power BI Desktop, Analysis Services, and Power Pivot in Excel.  

## Examples

Many reference articles contain examples showing formulas and results created in an Excel workbook with a Power Pivot in Excel data model. The data model contains data imported from the AdventureWorksDW sample databases. The sample workbook is no longer available.

This reference is not intended to serve as a tutorial or provide in-depth guidance on how to create formulas for data models containing data from a specific data source.

## In this section  

[New DAX functions](new-dax-functions.md) - These functions are new or are existing functions that have been significantly updated.  

[Date and time functions](date-and-time-functions-dax.md) - These functions in DAX are similar to date and time functions in Microsoft Excel. However, DAX functions are based on the datetime data types used by Microsoft SQL Server.  
  
[Filter functions](filter-functions-dax.md) - These functions help you return specific data types, look up values in related tables, and filter by related values. Lookup functions work by using tables and relationships between them. Filtering functions let you manipulate data context to create dynamic calculations.  

[Financial functions](financial-functions-dax.md) - These functions are used in formulas that perform financial calculations, such as net present value and rate of return.
  
[Information functions](information-functions-dax.md) - These functions look at a table or column provided as an argument to another function and tells you whether the value matches the expected type. For example, the ISERROR function returns TRUE if the value you reference contains an error.  
  
[Logical functions](logical-functions-dax.md) - These functions return information about values in an expression. For example, the TRUE function lets you know whether an expression that you are evaluating returns a TRUE value.  
  
[Math and Trig functions](math-and-trig-functions-dax.md) - Mathematical functions in DAX are similar to Excel's mathematical and trigonometric functions. However, there are some differences in the numeric data types used by DAX functions.  
  
[Other functions](other-functions-dax.md) - These functions perform unique actions that cannot be defined by any of the categories most other functions belong to.  
  
[Parent and Child functions](parent-and-child-functions-dax.md) - These Data Analysis Expressions (DAX) functions help users manage data that is presented as a parent/child hierarchy in their data models.  

[Relationship functions](relationship-functions-dax.md) - These functions are for managing and utilizing relationships between tables. For example, you can specify a particular relationship to be used in a calculation.  

[Statistical functions](statistical-functions-dax.md) - These functions perform aggregations. In addition to creating sums and averages, or finding minimum and maximum values, in DAX you can also filter a column before aggregating or create aggregations based on related tables.  

[Table manipulation functions](table-functions-dax.md) - These functions help create new or manipulate existing tables.
  
[Text functions](text-functions-dax.md) - With these functions, you can return part of a string, search for text within a string, or concatenate string values. Additional functions are for controlling the formats for dates, times, and numbers.  

[Time intelligence functions](time-intelligence-functions-dax.md) - These functions help you create calculations that use built-in knowledge about calendars and dates. By using time and date ranges in combination with aggregations or calculations, you can build meaningful comparisons across comparable time periods for sales, inventory, and so on.  
  
## See also

[DAX Syntax Reference](dax-syntax-reference.md)  
[DAX Operator Reference](dax-operator-reference.md)  
[DAX Parameter-Naming Conventions](dax-parameter-naming-conventions.md)