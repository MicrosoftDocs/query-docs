---
description: "Learn more about: WEEKNUM"
title: "WEEKNUM function (DAX)"
ms.topic: reference
---
# WEEKNUM

[!INCLUDE[applies-to-measures-columns-tables-visual-calculations](includes/applies-to-measures-columns-tables-visual-calculations.md)]

Returns the week number for the given date according to the `return_type` value. The week number indicates where the week falls numerically within a year.

There are two *systems* used for this function:

- **System 1**  -  The week containing January 1 is the first week of the year and is numbered week 1.
- **System 2**  -  The week containing the first Thursday of the year is the first week of the year and is numbered as week 1. This system is the methodology specified in ISO 8601, which is commonly known as the European week numbering system.

## Syntax

```dax
WEEKNUM(<date>[, <return_type>])
```

### Parameters

|Term|Definition|
|--------|--------------|
|`date`|The date in `datetime` format.|
|`return_type`|(Optional)  A number that determines on which day the week begins. Default is 1. See Remarks. |

## Return value

An integer number.

## Remarks

- By default, the WEEKNUM function uses a calendar convention in which the week containing January 1 is considered to be the first week of the year. However, the ISO 8601 calendar standard, widely used in Europe, defines the first week as the one with the majority of days (four or more) falling in the new year. This means that if `return_type` is any valid value other than 21, for any years in which there are three days or less in the first week of January, the WEEKNUM function returns week numbers that are different from the ISO 8601 definition.

- For `return_type`, the following valid values  may not be supported by some DirectQuery data sources:

    |return_type  |Week begins on  |System |
    |---------|---------|---------|
    |1 or omitted     |    Sunday     |     1   |
    |2     |    Monday     |     1    |
    |11    |     Monday    |     1    |
    |12     |     Tuesday    |     1    |
    |13     |     Wednesday    |     1    |
    |14     |     Thursday    |     1    |
    |15     |    Friday     |     1    |
    |16     |    Saturday     |     1    |
    |17     |    Sunday     |     1    |
    |21     |   Monday      |     2    |

## Example 1

The following example returns the week number for February 14, 2010. This calculation assumes weeks begin on Monday.

```dax
= WEEKNUM("Feb 14, 2010", 2) 
```

## Example 2

The following example returns the week number of the date stored in the column, **HireDate**, from the table, **Employees**. This calculation assumes weeks begin on Sunday.

```dax
= WEEKNUM('Employees'[HireDate])
```

## Related content

- [YEARFRAC function](yearfrac-function-dax.md)
- [WEEKDAY function](weekday-function-dax.md)
