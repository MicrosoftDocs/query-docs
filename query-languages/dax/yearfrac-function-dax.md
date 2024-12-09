---
description: "Learn more about: YEARFRAC"
title: "YEARFRAC function (DAX)"
---
# YEARFRAC

[!INCLUDE[applies-to-measures-columns-tables-visual-calculations](includes/applies-to-measures-columns-tables-visual-calculations.md)]

Calculates the fraction of the year represented by the number of whole days between two dates. Use the YEARFRAC worksheet function to identify the proportion of a whole year's benefits or obligations to assign to a specific term.  
  
## Syntax  
  
```dax
YEARFRAC(<start_date>, <end_date>, <basis>)  
```
  
### Parameters  
  
|Term|Definition|  
|--------|--------------|  
|`start_date`|The start date in `datetime` format.|  
|`end_date`|The end date in `datetime` format.|  
|`basis`|(Optional) The type of day count basis to use. All arguments are truncated to integers.<br /><br />Basis - Description<br /><br />0 - US (NASD) 30/360  (Default value)<br /><br />1 -  Actual/actual<br /><br />2 - Actual/360<br /><br />3 -   Actual/365<br /><br />4 - European 30/360|  
  
## Return value

A decimal number. The internal data type is a signed IEEE 64-bit (8-byte) double-precision floating-point number.  
  
## Remarks

- In contrast to Microsoft Excel, which stores dates as serial numbers, DAX uses a `datetime` format to work with dates and times. If you need to view dates as serial numbers, you can use the formatting options in Excel.  
  
- If `start_date` or `end_date` are not valid dates, YEARFRAC returns an error.  
  
- If `basis` &lt; 0 or if `basis` &gt; 4, YEARFRAC returns an error.  
  
## Example 1

The following example returns the fraction of a year represented by the difference between the dates in the two columns, `TransactionDate` and `ShippingDate`:  
  
```dax
= YEARFRAC(Orders[TransactionDate],Orders[ShippingDate])  
```
  
## Example 2

The following example returns the fraction of a year represented by the difference between the dates, January 1 and March 1:  
  
```dax
= YEARFRAC("Jan 1 2007","Mar 1 2007")  
```

Use four-digit years whenever possible, to avoid getting unexpected results. When the year is truncated, the current year is assumed. When the date is or omitted, the first date of the month is assumed.  
  
The second argument, `basis`, has also been omitted. Therefore, the year fraction is calculated according to the US (NASD) 30/360 standard.  
  
## Related content

[Date and time functions](date-and-time-functions-dax.md)  
[WEEKNUM function](weeknum-function-dax.md)  
[YEARFRAC function](yearfrac-function-dax.md)  
[WEEKDAY function](weekday-function-dax.md)  
