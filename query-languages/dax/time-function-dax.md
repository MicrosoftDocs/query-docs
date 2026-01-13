---
description: "Learn more about: TIME"
title: "TIME function (DAX)"
ms.topic: reference
---
# TIME

[!INCLUDE[applies-to-measures-columns-tables-visual-calculations](includes/applies-to-measures-columns-tables-visual-calculations.md)]

Converts hours, minutes, and seconds given as numbers to a time in `datetime` format.

## Syntax

```dax
TIME(hour, minute, second)
```

### Parameters

|Term|Definition|
|--------|--------------|
|`hour`|**Import mode:** A number from 0 to 32767 representing the hour. <br/> Any value greater than 23 will be divided by 24 and the remainder will be treated as the hour value, represented as a fraction of a day. <br /> For example, TIME(27,0,0) = TIME(3,0,0) = 3:00:00 AM <br /><br /> **DirectQuery mode:** A number from 0 to 23 representing the hour.|
|`minute`|**Import mode:** A number from 0 to 32767 representing the minute. <br /> Any value greater than 59 minutes will be converted to hours and minutes. <br /> Any value greater than 1440 (24 hours) does not alter the date portion - instead, it will be divided by 1440 and the remainder will be treated as the minute value, represented as a fraction of a day. <br /> For example, TIME(0,2190,0) = TIME(0,750,0) = TIME(12,30,0) = 12:30:00 PM <br /><br /> **DirectQuery mode:** A number from 0 to 59 representing the minute.|
|`second`|**Import mode:** A number from 0 to 32767 representing the second. <br /> Any value greater than 59 will be converted to hours, minutes, and seconds. <br /> For example, TIME(0,0,2000) = TIME(0,33,20) = 12:33:20 AM <br /><br /> **DirectQuery mode:** A number from 0 to 59 representing the second.| 

## Return value

A time (`datetime`) ranging from 00:00:00 (12:00:00 AM) to 23:59:59 (11:59:59 PM).

## Remarks

- In contrast to Microsoft Excel, which stores dates and times as serial numbers, DAX works with date and time values in a `datetime` format. Numbers in other formats are implicitly converted when you use a date/time value in a DAX function. If you need to use serial numbers, you can use formatting to change the way that the numbers are displayed.

- Time values are a portion of a date value, and in the serial number system are represented by a decimal number. Therefore, the `datetime` value 12:00 PM is equivalent to 0.5, because it is half of a day.

- You can supply the arguments to the TIME function as values that you type directly, as the result of another expression, or by a reference to a column that contains a numeric value. 

- Date and datetime can also be specified as a literal in the format `dt"YYYY-MM-DD"`, `dt"YYYY-MM-DDThh:mm:ss"`, or `dt"YYYY-MM-DD hh:mm:ss"`. When specified as a literal, using the TIME function in the expression is not necessary. To learn more, see [DAX Syntax | Date and time](dax-syntax-reference.md#date-and-time).

- [!INCLUDE [function-not-supported-in-directquery-mode](includes/function-not-supported-in-directquery-mode.md)]

## Example 1

The following examples both return the time, 3:00 AM:

```dax
= TIME(27,0,0)
```

```dax
= TIME(3,0,0)
```

## Example 2

The following examples both return the time, 12:30 PM:

```dax
= TIME(0,750,0)
```

```dax
= TIME(12,30,0)
```

## Example 3

The following example creates a time based on the values in the columns, `intHours`, `intMinutes`, `intSeconds`:

```dax
= TIME([intHours],[intMinutes],[intSeconds])
```

## Related content

[DATE](date-function-dax.md)
[Date and time functions](date-and-time-functions-dax.md)
