---
description: "Learn more about: MONTH"
title: "MONTH function (DAX)"
ms.topic: reference
---
# MONTH

[!INCLUDE[applies-to-measures-columns-tables-visual-calculations](includes/applies-to-measures-columns-tables-visual-calculations.md)]

Returns the month as a number from 1 (January) to 12 (December).

## Syntax

```dax
MONTH(<datetime>)
```

### Parameters

|Term|Definition|
|--------|--------------|
|`date`|A date in `datetime` or text format.|

## Return value

An integer number from 1 to 12.

## Remarks

- In contrast to Microsoft Excel, which stores dates as serial numbers, DAX uses a `datetime` format when working with dates. You can enter the date used as argument to the MONTH function by typing an accepted `datetime` format, by providing a reference to a column that contains dates, or by using an expression that returns a date.

- Values returned by the YEAR, MONTH and DAY functions will be Gregorian values regardless of the display format for the supplied date value. For example, if the display format of the supplied date is Hijri, the returned values for the YEAR, MONTH and DAY functions will be values associated with the equivalent Gregorian date.

- When the date argument is a text representation of the date, the function uses the locale and date time settings of the client computer to understand the text value in order to perform the conversion. If the current date time settings represent a date in the format of Month/Day/Year, then the following string "1/8/2009" is interpreted as a datetime value equivalent to January 8th of 2009, and the function yields a result of 1. However, if the current date time settings represent a date in the format of Day/Month/Year, then the same string would be interpreted as a datetime value equivalent to August 1st of 2009, and the function yields a result of 8.

- If the text representation of the date cannot be correctly converted to a datetime value, the function returns an error.

## Example 1

The following expression returns 3, which is the integer corresponding to March, the month in the `date` argument.

```dax
= MONTH("March 3, 2008 3:45 PM")
```

## Example 2

The following expression returns the month from the date in the `TransactionDate` column of the `Orders` table.

```dax
= MONTH(Orders[TransactionDate])
```

## Related content

- [Date and time functions](date-and-time-functions-dax.md)
- [HOUR function](hour-function-dax.md)
- [MINUTE function](minute-function-dax.md)
- [YEAR function](year-function-dax.md)
- [SECOND function](second-function-dax.md)
