---
title: "DATESBETWEEN function (DAX) | Microsoft Docs"
ms.service: powerbi 
ms.date: 06/24/2020
ms.reviewer: owend
ms.topic: reference
author: minewiskan
ms.author: owend

---
# DATESBETWEEN

Returns a table that contains a column of dates that begins with a specified start date and continues until a specified end date.

This function is suited to pass as a filter to the [CALCULATE](calculate-function-dax.md) function. Use it to filter an expression by a custom date range.

> [!NOTE]
> If you're working with standard date intervals such as days, months, quarters, or years, we recommend you use the better suited [DATESINPERIOD](datesinperiod-function-dax.md) function.

## Syntax

```dax
DATESBETWEEN(<dates>, <start_date>, <end_date>)
```

### Parameters

|Term|Definition|
|--------|--------------|
|dates|A date column from a marked date table.|
|start_date|A date expression.|
|end_date|A date expression.|

## Return value

A table containing a single column of date values.

## Remarks

Ideally, **dates** is a reference to the date column of a marked date table. For more information, see [Creating date tables in Power BI Desktop](/power-bi/guidance/model-date-table).

If **start_date** is BLANK, then **start_date** will be the earliest value in the **dates** column.

If **end_date** is BLANK, then **end_date** will be the latest value in the **dates** column.

Dates used as the **start_date** and **end_date** are inclusive. So, for example, if the **start_date** value is July 1, 2019, then that date will be included in the returned table (providing the date exists in the **dates** column).

The returned table can only contain dates stored in the **dates** column. So, for example, if the **dates** column starts from July 1, 2017, and the **start_date** value is July 1, 2016, the returned table will start from July 1, 2017.

This DAX function isn't supported for use in DirectQuery mode. For more information, see [https://go.microsoft.com/fwlink/?LinkId=219172](https://go.microsoft.com/fwlink/?LinkId=219172).

## Example

The following **Sales** table measure definition uses the DATESBETWEEN function to produce a _life-to-date_ (LTD) calculation. Life-to-date represents the accumulation of a measure over time since the very beginning of time.

Notice that the formula uses the [MAX](max-function-dax.md) function. This function returns the latest date that's in the filter context. So, the DATESBETWEEN function returns a table of dates beginning from the earliest date until the latest date being reported.

_All examples in this article can be added to the sample model. To obtain the model, see [DAX model sample](https://aka.ms/dax-docs-samples)._

```dax
Customers LTD =
CALCULATE(
    DISTINCTCOUNT(Sales[CustomerKey]),
    DATESBETWEEN(
        'Date'[Date],  
        BLANK(),  
        MAX('Date'[Date])  
    )
)
```

Consider that the earliest date stored in the **Date** table is July 1, 2017. So, when a report filters the measure by the month of June 2020, the DATESBETWEEN function returns a date range from July 1, 2017 until June 30, 2020.

## See also

- [Time-intelligence functions (DAX)](time-intelligence-functions-dax.md)
- [Date and time functions (DAX)](date-and-time-functions-dax.md)
- [DATESINPERIOD function (DAX)](datesinperiod-function-dax.md)
