---
title: "DATE Function (DAX) | Microsoft Docs"
ms.service: powerbi 

ms.date: 5/22/2018
ms.reviewer: owend
ms.topic: reference
author: minewiskan
ms.author: owend
manager: kfile
---
# DATE Function (DAX)
Returns the specified date in **datetime** format.  
  
## Syntax  
  
```dax
DATE(<year>, <month>, <day>)  
```
  
#### Parameters  
  
|Term|Definition|  
|--------|--------------|  
|**year**|A number representing the year.<br /><br />The value of the **year** argument can include one to four digits. The **year** argument is interpreted according to the date system used by your computer.<br /><br />Dates beginning with March 1, 1900 are supported.<br /><br />If you enter a number that has decimal places, the number is rounded.<br /><br />For values greater than 9999 or less than zero (negative values), the function returns a **#VALUE!** error.<br /><br />If the **year** value is between 0 and 1899, the value is added to 1900 to produce the final value. See the examples below. **Note:** You should use four digits for the **year** argument whenever possible to prevent unwanted results. For example, using 07 returns 1907 as the year value.|  
|**month**|A number representing the month or a calculation according to the following rules:<br /><br />If **month** is a number from 1 to 12, then it represents a month of the year. 1 represents January, 2 represents February, and so on until 12 that represents December.<br /><br />If you enter an integer larger than 12, the following computation occurs: the date is calculated by adding the value of **month** to the **year**. For example, if you have DATE( 2008, 18, 1), the function returns a datetime value equivalent to June 1st of 2009, because 18 months are added to the beginning of 2008 yielding a value of June 2009. See examples below.<br /><br />If you enter a negative integer, the following computation occurs: the date is calculated subtracting the value of **month** from **year**. For example, if you have DATE( 2008, -6, 15), the function returns a datetime value equivalent to June 15th of 2007, because when 6 months are subtracted from the beginning of 2008 it yields a value of June 2007. See examples below.|  
|**day**|A number representing the day or a calculation according to the following rules:<br /><br />If **day** is a number from 1 to the last day of the given month then it represents a day of the month.<br /><br />If you enter an integer larger than last day of the given month, the following computation occurs: the date is calculated by adding the value of **day** to **month**. For example, in the formula `DATE( 2008, 3, 32)`, the DATE function returns a **datetime** value equivalent to April 1st of 2008, because 32 days are added to the beginning of March yielding a value of April 1st.<br /><br />If you enter a negative integer, the following computation occurs: the date is calculated subtracting the value of **day** from **month**. For example, in the formula `DATE( 2008, 5, -15)`, the DATE function returns a **datetime** value equivalent to April 15th of 2008, because 15 days are subtracted from the beginning of May 2008 yielding a value of April 2008.<br /><br />If **day** contains a decimal portion, it is rounded to the nearest integer value.|  
  
## Return Value  
Returns the specified date (**datetime)**.  
  
## Remarks  
The DATE function takes the integers that are input as arguments, and generates the corresponding date. The DATE function is most useful in situations where the year, month, and day are supplied by formulas. For example, the underlying data might contain dates in a format that is not recognized as a date, such as YYYYMMDD. You can use the DATE function in conjunction with other functions to convert the dates to a number that can be recognized as a date.  
  
In contrast to Microsoft Excel, which stores dates as a serial number, DAX date functions always return a **datetime** data type. However, you can use formatting to display dates as serial numbers if you want.  
  
This DAX function may return different results when used in a model that is deployed and then queried in DirectQuery mode. For more information about semantic differences in DirectQuery mode, see  [https://go.microsoft.com/fwlink/?LinkId=219171](https://go.microsoft.com/fwlink/?LinkId=219171).  
  
## Example: Returning a Simple Date  
  
### Description  
The following formula returns the date July 8, 2009:  
  
### Code  
  
```dax
=DATE(2009,7,8)  
```
  
## Example: Years before 1899  
  
### Description  
If the value that you enter for the **year** argument is between 0 (zero) and 1899 (inclusive), that value is added to 1900 to calculate the year. The following formula returns January 2, 1908: (1900+08).  
  
### Code  
  
```dax
=DATE(08,1,2)  
```
  
## Example: Years before 1899  
  
### Description  
If the value that you enter for the **year** argument is between 0 (zero) and 1899 (inclusive), that value is added to 1900 to calculate the year. The following formula returns January 2, 3700: (1900+1800).  
  
### Code  
  
```dax
=DATE(1800,1,2)  
```
  
## Example: Years after 1899  
  
### Description  
If **year** is between 1900 and 9999 (inclusive), that value is used as the year. The following formula returns January 2, 2008:  
  
### Code  
  
```dax
=DATE(2008,1,2)  
```
  
## Example: Working with Months  
  
### Description  
If **month** is greater than 12, **month** adds that number of months to the first month in the year specified. The following formula returns the date February 2, 2009:  
  
### Code  
  
```dax
=DATE(2008,14,2)  
```
  
### Comment  
If the **month** value is less than 1, the DATE function subtracts the magnitude of that number of months, plus 1, from the first month in the year specified. The following formula returns September 2, 2007:  
  
```dax
=DATE(2008,-3,2)  
```
  
## Example: Working with Days  
  
### Description  
If **day** is greater than the number of days in the month specified, **day** adds that number of days to the first day in the month. The following formula returns the date February 4, 2008:  
  
### Code  
  
```dax
=DATE(2008,1,35)  
```
  
### Comment  
If **day** is less than 1, **day** subtracts the magnitude that number of days, plus one, from the first day of the month specified. The following formula returns December 16, 2007:  
  
```dax
=DATE(2008,1,-15)  
```
  
## See Also  
[Date and Time Functions &#40;DAX&#41;](date-and-time-functions-dax.md)  
[DAY Function &#40;DAX&#41;](day-function-dax.md)  
[TODAY Function &#40;DAX&#41;](today-function-dax.md)  
  
