---
title: "DAX function reference | Microsoft Docs"
ms.service: powerbi 
ms.date: 03/29/2019
ms.reviewer: owend
ms.topic: reference
author: minewiskan
ms.author: owend
manager: kfile
---
# DAX function reference
This function reference provides detailed information including syntax, parameters, Return values, and examples for each of the over 200 functions used in Data Analysis Expression (DAX) formulas.  

> [!IMPORTANT]
> Not all DAX functions are supported or included in earlier versions of Power BI Desktop, Analysis Services, and Power Pivot in Excel.  

## Sample data

Most reference articles contain examples showing formulas and results created in an Excel workbook with a Power Pivot for Excel data model. The data model is connected to an AdventureWorksDW sample database as a datasource. The sample workbook is no longer available. 

You can [download the AdventureWorksDW sample database](https://github.com/Microsoft/sql-server-samples/releases/tag/adventureworks), or you can create a free [Azure SQL data warehouse](https://docs.microsoft.com/en-us/azure/sql-data-warehouse/create-data-warehouse-portal) with the AdventureWorksDW sample database to use as a datasource for Power BI Desktop, Excel, and Analysis Services tabular models. This DAX reference is not intended to provide guidance on connecting to sample data or creating data models.

## In this section  

[New DAX functions](new-dax-functions.md) - These functions are new or are existing functions that have been significantly updated.  

[Date and time functions &#40;DAX&#41;](date-and-time-functions-dax.md) - These functions in DAX are similar to date and time functions in Microsoft Excel. However, DAX functions are based on the datetime data types used by Microsoft SQL Server.  
  
[Time-intelligence functions &#40;DAX&#41;](time-intelligence-functions-dax.md) - These functions help you create calculations that use built-in knowledge about calendars and dates. By using time and date ranges in combination with aggregations or calculations, you can build meaningful comparisons across comparable time periods for sales, inventory, and so on.  
  
[Filter functions &#40;DAX&#41;](filter-functions-dax.md) - These functions help you return specific data types, look up values in related tables, and filter by related values. Lookup functions work by using tables and relationships between them. Filtering functions let you manipulate data context to create dynamic calculations.  
  
[Information functions &#40;DAX&#41;](information-functions-dax.md) - These functions look at a table or column provided as an argument to another function and tells you whether the value matches the expected type. For example, the ISERROR function returns TRUE if the value you reference contains an error.  
  
[Logical functions &#40;DAX&#41;](logical-functions-dax.md) - These functions return information about values in an expression. For example, the TRUE function lets you know whether an expression that you are evaluating returns a TRUE value.  
  
[Math and Trig functions &#40;DAX&#41;](math-and-trig-functions-dax.md) - Mathematical functions in DAX are similar to Excel's mathematical and trigonometric functions. However, t99[ are](https://github.com/Microsoft/sql-server-samples/releases/tag/adventureworks) some differences in the numeric data types used by DAX functions.  
  
[Other functions &#40;DAX&#41;](other-functions-dax.md) - These functions perform unique actions that cannot be defined by any of the categories most other functions belong to.  
  
[Parent and Child functions &#40;DAX&#41;](parent-and-child-functions-dax.md) - These Data Analysis Expressions (DAX) functions help users manage data that is presented as a parent/child hierarchy in their data models.  
  
[Statistical functions &#40;DAX&#41;](statistical-functions-dax.md) - These functions perform aggregations. In addition to creating sums and averages, or finding minimum and maximum values, in DAX you can also filter a column before aggregating or create aggregations based on related tables.  
  
[Text functions &#40;DAX&#41;](text-functions-dax.md) - With these functions, you can return part of a string, search for text within a string, or concatenate string values. Additional functions are for controlling the formats for dates, times, and numbers.  
  
## See also  
[DAX Syntax Reference](dax-syntax-reference.md)  
[DAX Operator Reference](dax-operator-reference.md)  
[DAX Parameter-Naming Conventions](dax-parameter-naming-conventions.md)  
  
