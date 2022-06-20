---
description: "Learn more about: NETWORKDAYS"
title: "NETWORKDAYS function (DAX) | Microsoft Docs"
ms.service: powerbi
ms.date: 06/20/2022
ms.reviewer: owend
ms.topic: reference
author: minewiskan
ms.author: owend 
recommendations: false

---

# NETWORKDAYS

Returns the number of whole workdays between two dates (inclusive). Parameters specify which and how many days are weekend days. Weekend days and days specified as holidays are not considered as workdays.

## Syntax

```dax
NETWORKDAYS(<start_date>, <end_date>[, <weekend>, <holidays>])
```

### Parameters

|Term|Definition|  
|--------|--------------|  
|start_date|A date that represents the start date. The dates for which the difference is to be computed. The start_date can be earlier than, the same as, or later than the end_date.|
|end_date|A date that represents the end date. The dates for which the difference is to be computed. The start_date can be earlier than, the same as, or later than the end_date.|
|weekend|Indicates the days of the week that are weekend days and are not included in the number of whole working days between start_date and end_date. Weekend is a weekend number that specifies when weekends occur.  </br> Weekend number values indicate the following weekend days: </br>1 or omitted: Saturday, Sunday </br>2: Sunday, Monday </br>3: Monday, Tuesday </br>4: Tuesday, Wednesday </br>5: Wednesday, Thursday </br>6: Thursday, Friday </br>7: Friday, Saturday </br>11: Sunday only </br>12: Monday only </br>13: Tuesday only </br>14: Wednesday only </br>15: Thursday only </br>16: Friday only </br>17: Saturday only|
|holidays|A column table of one or more dates that are to be excluded from the working day calendar.|

## Return Value

An integer number of whole workdays.

## Remarks

- This DAX function is similar to Excel NETWORKDAYS.INTL and NETWORKDAYS functions.

- If start_date and end_date both are BLANK, the output value is also BLANK.

- If either start_date or end_date is BLANK, the BLANK start_date or end_date will be treated as Date(1899, 12, 30).

- Dates must be specified by using [DATE function](date-function-dax.md) or as the result of another expression. For example, `DATE ( 2022, 5, 30 )`, specifies May 30th, 2022. Dates can also be specified as a [literal](dax-syntax-reference.md#date-and-time-literal) in format, `(dt”2022-05-30”)`. Do not specify dates as text.

## Example

The following expression:

```dax
   = NETWORKDAYS (
        DATE ( 2022, 5, 28 ),
        DATE ( 2022, 5, 30 ),
        1,
        {
            DATE ( 2022, 5, 30 )
        }
    )
```

Returns:

| **[Value]** |
| ------------- |
| 0       |

In this example, 0 is returned because the start date is a Saturday and the end date is a Monday. The weekend parameter specifies that the weekend is Saturday and Sunday, so those are not work days. The holiday parameter marks the 30th (the end date) as a holiday, so no working days remain.

