---
description: "Learn more about: SAMPLECARTESIANPOINTSBYCOVER"
title: "SAMPLECARTESIANPOINTSBYCOVER function (DAX) | Microsoft Docs"
ms.topic: reference
author: jajin7
---

# SAMPLECARTESIANPOINTSBYCOVER

[!INCLUDE[applies-to-measures-columns-tables-visual-calculations](includes/applies-to-measures-columns-tables-visual-calculations.md)]

Returns a sample subset from a Table that is obtained by plotting the rows as points in 2D space and removing overlapping points.

## Syntax

```dax
SAMPLECARTESIANPOINTSBYCOVER(<Size>, <Table>, <XAxis>, <YAxis>[, <Radius>] [, <MaxMinRatio>] [, <MaxBlankRatio>] )
```

### Parameters

|Term|Definition|  
|--------|--------------|  
|Size|Number of rows in the sample to return|
|Table|Any DAX expression that returns a table of data from where to return a sample subset from.|
|XAxis|The numerical XAxis column from the Table.|
|YAxis|The numerical YAxis column from the Table.|
|Radius|(Optional) The numerical Radius column from the Table.|
|MaxMinRatio|(Optional) When Radius is specified, MaxMinRatio has to be specified and defines the ratio between the maximum and the minimum radiuses of drawn points. See remarks for more details.|
|MaxBlankRatio|(Optional) When Radius is specified, MaxBlankRatio has to be specified and defines the ratio between the maximum and blank radiuses of the drawn points. See remarks for more details. |

## Return Value

The sample from Table consisting of Size number of rows.

## Remarks
- If Size is less than or equal to 0, SAMPLECARTESIANPOINTSBYCOVER returns an empty table
- If Radius is specified, MaxMinRatio and MaxBlankRatio need to be specified and set to a value larger than 1. If not, SAMPLECARTESIANPOINTSBYCOVER returns an error
- Set MaxMinRatio to the maximum of Radius divided by the minimum of Radius. For example, if the minimum Radius is 20 and the maximum Radius is 60, the MaxMinRatio parameter should be set to 60/20 = 3.
- Set MaxBlankRatio to the maximum of Radius divided by the Radius for blank values. For example, if the maximum Radius is 60 and the Radius for blank values is 6, then MaxBlankRatio should be set to 60/6 = 10.

- [!INCLUDE [function-not-supported-in-directquery-mode](includes/function-not-supported-in-directquery-mode.md)]

## Example

The following DAX query:

```dax
EVALUATE
SAMPLECARTESIANPOINTSBYCOVER (
    1000,
    SELECTCOLUMNS ( Sales, "x", [Unit Price], "y", [Sales Amount] ),
    [x],
    [y]
)
```

Returns a 1000 row sample from unique points from the Sales table in a 2D space defined by Unit Price as the X axis and Sales Amount as the Y axis.