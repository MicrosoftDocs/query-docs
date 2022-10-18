---
description: "Learn more about: INDEX"
title: "INDEX function (DAX) | Microsoft Docs"
ms.service: powerbi 
ms.subservice: dax
ms.date: 10/17/2022
ms.reviewer: owend
ms.topic: reference
author: minewiskan
ms.author: owend 
recommendations: false

---

# INDEX

Returns a row at an absolute position (specified by the position parameter) within the specified partition sorted by the specified order or on the specified axis.
  
## Syntax  
  
```dax
INDEX(<position>[, < relation>, < orderBy>, < partitionBy>])
```
  
### Parameters  
  
|Term|Definition|  
|--------|--------------|  
|position|The absolute position (1-based) from which to obtain the data.|
|relation|A table expression from which the output will be returned. If omitted, \<orderBy> must be explicitly specified.
|orderBy|(Optional) An ORDERBY() clause containing the columns that define how each partition is sorted. <br>If omitted: <br>- \<relation> must be explicitly specified. <br>- Defaults to ordering by every column in \<relation>.
|partitionBy|(Optional) A PARTITIONBY() clause containing the columns that define how \<relation> is partitioned. <br> If omitted, \<relation> is treated as a single partition. |

## Return value

A row at an absolute position (specified by the position parameter) within the specified partition sorted by the specified order or on the specified axis.
  
## Remarks

This function is similar to OFFSET function.

## Example 1

The following DAX query:
  
```dax
EVALUATE INDEX(1, ALL(DimDate[CalendarYear]))
```

Returns the following table:

|DimDate[CalendarYear]  |
|---------|
|  2005   |

## Example 2

The following DAX query:

```dax
EVALUATE
SUMMARIZECOLUMNS (
    FactInternetSales[ProductKey],
    DimDate[MonthNumberOfYear],
    FILTER (
        VALUES(FactInternetSales[ProductKey]),
        [ProductKey] < 222
    ),
    "CurrentSales", SUM(FactInternetSales[SalesAmount]),
    "LastMonthSales",
    CALCULATE (
        SUM(FactInternetSales[SalesAmount]),
        INDEX(-1, ORDERBY(DimDate[MonthNumberOfYear]))
    )
)
ORDER BY [ProductKey], [MonthNumberOfYear]
```

Returns the following table:

|FactInternetSales[ProductKey]  |DimDate[MonthNumberOfYear]  |[CurrentSales] |[LastMonthSales]  |
|---------|---------|---------|---------|
|214     |    1     |   5423.45     |   8047.7      |
|214     |    2     |   4968.58     |   8047.7      |
|214     |    3     |   5598.4      |   8047.7      |
|214     |    4     |   5073.55     |   8047.7      |
|214     |    5     |   5248.5      |   8047.7      |
|214     |    6     |   7487.86     |   8047.7      |
|214     |    7     |   7382.89     |   8047.7      |
|214     |    8     |   6543.13     |   8047.7      |
|214     |    9     |   6788.06     |   8047.7      |
|214     |   10     |  6858.04      |   8047.7      |
|214     |   11     |  8607.54      |   8047.7      |
|214     |   12     |  8047.7       |   8047.7      |
|217     |   1      |  5353.47      |   7767.78     |
|217     |   2      |  4268.78      |   7767.78     |
|217     |   3      |  5773.35      |   7767.78     |
|217     |   4      |  5738.36      |   7767.78     |
|217     |   5      |  6158.24      |   7767.78     |
|217     |   6      |  6998         |   7767.78     |
|217     |   7      |  5563.41      |   7767.78     |
|217     |   8      |  5913.31      |   7767.78     |
|217     |   9      |  5913.31      |   7767.78     |
|217     |  10      |  6823.05      |   7767.78     |
|217     |  11      |  6683.09      |   7767.78     |
|217     |  12      |  7767.78      |   7767.78     |

## Example 3

The following DAX query:

```dax
DEFINE
MEASURE DimProduct[TotalSales] = SUM(FactInternetSales[SalesAmount])
VAR vRelation = SUMMARIZECOLUMNS (
        DimProduct[Color], 
        DimProduct[ProductKey], 
        FactInternetSales[OrderDate], 
        DimDate[DayNumberOfWeek], 
        FILTER(VALUES(DimProduct[ProductKey]), [ProductKey] < 350), 
        FILTER(VALUES(FactInternetSales[OrderDate]), [OrderDate] < dt"2011-1-15"), 
        "Total Sales", DimProduct[TotalSales]
    ) 
EVALUATE
ADDCOLUMNS (
    vRelation, 
    "Dynamic Position Sales", 
    SELECTCOLUMNS(INDEX([DayNumberOfWeek], vRelation, ORDERBY([ProductKey], ASC, [OrderDate]), PARTITIONBY([Color])), "Dynamic Position Sales", [TotalSales])
)
ORDER BY [Color], [ProductKey] ASC, [OrderDate]
```

Returns the following table:

|DimProduct[Color]|DimProduct[ProductKey]|FactInternetSales[OrderDate]|DimDate[DayNumberOfWeek]|[Total Sales]|[Dynamic Position Sales]|
|---------|---------|---------|---------|---------|---------|
|Black|332|1/4/2011 12:00:00 AM|1|699.0982|699.0982|
|Black|332|1/5/2011 12:00:00 AM|2|699.0982|699.0982|
|Black|332|1/12/2011 12:00:00 AM|2|699.0982|699.0982|
|Black|336|12/29/2010 12:00:00 AM|2|699.0982|699.0982|
|Black|336|1/2/2011 12:00:00 AM|6|699.0982   |        |
|Red|310|12/29/2010 12:00:00 AM|2|3578.27|3578.27|
|Red|310|12/30/2010 12:00:00 AM|3|3578.27|3578.27|
|Red|310|1/2/2011 12:00:00 AM|6|3578.27|3578.27|
|Red|310|1/3/2011 12:00:00 AM|7|3578.27|3578.27|
|Red|310|1/7/2011 12:00:00 AM|4|3578.27|3578.27|
|Red|310|1/8/2011 12:00:00 AM|5|3578.27|3578.27|
|Red|310|1/9/2011 12:00:00 AM|6|3578.27|3578.27|
|Red|310|1/11/2011 12:00:00 AM|1|3578.27|3578.27|
|Red|310|1/13/2011 12:00:00 AM|3|10734.81|3578.27|
|Red|310|1/14/2011 12:00:00 AM|4|3578.27|3578.27|
|Red|311|12/30/2010 12:00:00 AM|3|3578.27|3578.27|
|Red|311|1/1/2011 12:00:00 AM|5|3578.27|3578.27|
|Red|311|1/2/2011 12:00:00 AM|6|7156.54|3578.27|
|Red|311|1/3/2011 12:00:00 AM|7|7156.54|3578.27|
|Red|311|1/4/2011 12:00:00 AM|1|3578.27|3578.27|
|Red|311|1/5/2011 12:00:00 AM|2|7156.54|3578.27|
|Red|311|1/8/2011 12:00:00 AM|5|3578.27|3578.27|
|Red|311|1/10/2011 12:00:00 AM|7|3578.27|3578.27|
|Red|311|1/11/2011 12:00:00 AM|1|7156.54|3578.27|
|Red|311|1/12/2011 12:00:00 AM|2|3578.27|3578.27|
|Red|312|12/31/2010 12:00:00 AM|4|7156.54|3578.27|
|Red|312|1/3/2011 12:00:00 AM|7|3578.27|3578.27|
|Red|312|1/4/2011 12:00:00 AM|1|3578.27|3578.27|
|Red|312|1/6/2011 12:00:00 AM|3|3578.27|3578.27|
|Red|312|1/7/2011 12:00:00 AM|4|3578.27|3578.27|
|Red|312|1/8/2011 12:00:00 AM|5|7156.54|3578.27|
|Red|312|1/10/2011 12:00:00 AM|7|3578.27|3578.27|
|Red|312|1/12/2011 12:00:00 AM|2|3578.27|3578.27|
|Red|313|12/31/2010 12:00:00 AM|4|3578.27|3578.27|
|Red|313|1/6/2011 12:00:00 AM|3|3578.27|3578.27|
|Red|313|1/9/2011 12:00:00 AM|6|3578.27|3578.27|
|Red|313|1/11/2011 12:00:00 AM|1|7156.54|3578.27|
|Red|313|1/14/2011 12:00:00 AM|4|3578.27|3578.27|
|Red|314|12/31/2010 12:00:00 AM|4|3578.27|3578.27|
|Red|314|1/1/2011 12:00:00 AM|5|3578.27|3578.27|
|Red|314|1/2/2011 12:00:00 AM|6|3578.27|3578.27|
|Red|314|1/6/2011 12:00:00 AM|3|3578.27|3578.27|
|Red|314|1/9/2011 12:00:00 AM|6|3578.27|3578.27|
|Red|314|1/11/2011 12:00:00 AM|1|7156.54|3578.27|
|Red|314|1/13/2011 12:00:00 AM|3|3578.27|3578.27|
|Red|314|1/14/2011 12:00:00 AM|4|3578.27|3578.27|
|Red|330|12/31/2010 12:00:00 AM|4|699.0982|3578.27|
|Silver|344|12/30/2010 12:00:00 AM|3|3399.99|6799.98|
|Silver|346|12/29/2010 12:00:00 AM|2|10199.97|10199.97|
|Silver|346|1/6/2011 12:00:00 AM|3|6799.98|6799.98|
|Silver|346|1/7/2011 12:00:00 AM|4|3399.99|3399.99|
|Silver|346|1/14/2011 12:00:00 AM|4|3399.99|3399.99|
|Silver|347|1/9/2011 12:00:00 AM|6|3399.99|3399.99|

## See also

[OFFSET](offset-function-dax.md)  
[ORDERBY](orderby-function-dax.md)  
[PARTITIONBY](partitionby-function-dax.md)  
[WINDOW](window-function-dax.md)
