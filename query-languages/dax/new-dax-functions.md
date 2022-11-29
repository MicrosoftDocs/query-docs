---
description: "Learn more about: New DAX functions"
title: "New DAX functions | Microsoft Docs"
ms.service: powerbi 
ms.date: 06/20/2022
ms.subservice: dax 
ms.reviewer: owend
ms.topic: reference
author: minewiskan
ms.author: owend 
recommendations: false
---
# New DAX functions

DAX is continuously being improved with new functions and functionality to support new features. New functions and updates are included in service, application, and tool updates which in most cases are monthly.

While functions and functionality are being updated all the time, only those updates that have a visible and functional change exposed to users are described in documentation. New functions and updates to existing functions within the past year are shown here.

> [!IMPORTANT]
> Not all functions are supported in all versions of Power BI Desktop, Analysis Services, and Power Pivot in Excel. New and updated functions are typically first introduced in Power BI Desktop, and then later in Analysis Services, Power Pivot in Excel, and tools.
  
## New functions

|Function  |Month  | Description |
|---------|---------|---------|
|[EVALUATEANDLOG](evaluateandlog-function-dax.md)| November, 2022 |  Returns the value of the first argument and logs it in a DAX Evaluation Log profiler event. This function applies to Power BI Desktop only.  |
|[TOCSV](tocsv-function-dax.md) | November, 2022 |  Returns a table as a string in CSV format. This function applies to Power BI Desktop only. |
|[TOJSON](tojson-function-dax.md) | November, 2022 |  Returns a table as a string in JSON format. This function applies to Power BI Desktop only. |
|[NETWORKDAYS](networkdays-dax.md)| July, 2022 |  Returns the number of whole workdays between two dates. |


## Updated functions

|Function  | Month  |Description|
|---------|---------|---------|
|[CALCULATE](calculate-function-dax.md)| September, 2021 |Support for aggregation functions in boolean filter expressions.|
|[CALCULATETABLE](calculatetable-function-dax.md)| September, 2021 |Support for aggregation functions in boolean filter expressions.|
|[FORMAT](format-function-dax.md)| September, 2021 |Additional locale_name parameter that specifies the name of a locale to be used by format_string.|
|[XIRR](xirr-function-dax.md)| September, 2021 |Additional alternateResult parameter that specifies a result to be returned instead of an error if XIRR cannot determine a solution.|
