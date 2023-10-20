---
description: "Learn more about: DATE"
title: "DATE function (DAX) | Microsoft Docs"
---
# DATE

Returns the specified date in **datetime** format.  
  
## Syntax  
  
```dax
DATE(<year>, <month>, <day>)  
```
  
### Parameters  
  
|Term|Definition|  
|--------|--------------|  
|year|A number representing the year.<br /><br />The value of the **year** argument can include one to four digits. The **year** argument is interpreted according to the date system used by your computer.<br /><br />Dates beginning with March 1, 1900 are supported.<br /><br />If you enter a number that has decimal places, the number is rounded.<br /><br />For values greater than 9999 or less than zero (negative values), the function returns a **#VALUE!** error.<br /><br />If the **year** value is between 0 and 1899, the value is added to 1900 to produce the final value. See the examples below. **Note:** You should use four digits for the **year** argument whenever possible to prevent unwanted results. For example, using 07 returns 1907 as the year value.|  
|month|A number representing the month or a calculation according to the following rules:<br /><br />Negative integers are not supported. Valid values are 1-12. <br /><br />If **month** is a number from 1 to 12, then it represents a month of the year. 1 represents January, 2 represents February, and so on until 12 that represents December.<br /><br />If you enter an integer larger than 12, the following computation occurs: the date is calculated by adding the value of **month** to the **year**. For example, if you have DATE( 2008, 18, 1), the function returns a datetime value equivalent to June 1st of 2009, because 18 months are added to the beginning of 2008 yielding a value of June 2009. See examples below.|  
|day|A number representing the day or a calculation according to the following rules:<br /><br />Negative integers are not supported. Valid values are 1-31. <br /><br />If **day** is a number from 1 to the last day of the given month then it represents a day of the month.<br /><br />If you enter an integer larger than last day of the given month, the following computation occurs: the date is calculated by adding the value of **day** to **month**. For example, in the formula `DATE( 2008, 3, 32)`, the DATE function returns a **datetime** value equivalent to April 1st of 2008, because 32 days are added to the beginning of March yielding a value of April 1st.<br /><br />If **day** contains a decimal portion, it is rounded to the nearest integer value.|  
  
## Return value

Returns the specified date (**datetime)**.  
  
## Remarks

- The DATE function takes the integers that are input as arguments, and generates the corresponding date. The DATE function is most useful in situations where the year, month, and day are supplied by formulas. For example, the underlying data might contain dates in a format that is not recognized as a date, such as YYYYMMDD. You can use the DATE function in conjunction with other functions to convert the dates to a number that can be recognized as a date.  
  
- In contrast to Microsoft Excel, which stores dates as a serial number, DAX date functions always return a **datetime** data type. However, you can use formatting to display dates as serial numbers if you want.  

- Date and datetime can also be specified as a literal in the format `dt"YYYY-MM-DD"`, `dt"YYYY-MM-DDThh:mm:ss"`, or `dt"YYYY-MM-DD hh:mm:ss"`. When specified as a literal, using the DATE function in the expression is not necessary. To learn more, see [DAX Syntax | Date and time](dax-syntax-reference.md#date-and-time).
  
- [!INCLUDE [function-not-supported-in-directquery-mode](includes/function-not-supported-in-directquery-mode.md)]
  
## Examples
  
### Simple Date

The following formula returns the date July 8, 2009:  
  
```dax
= DATE(2009,7,8)  
```
  
### Years before 1899  

If the value that you enter for the **year** argument is between 0 (zero) and 1899 (inclusive), that value is added to 1900 to calculate the year. The following formula returns January 2, 1908: (1900+08).  
  
```dax
= DATE(08,1,2)  
```
  
### Years after 1899  

If **year** is between 1900 and 9999 (inclusive), that value is used as the year. The following formula returns January 2, 2008:  
  
```dax
= DATE(2008,1,2)  
```
  
### Months  

If **month** is greater than 12, **month** adds that number of months to the first month in the year specified. The following formula returns the date February 2, 2009:  
  
```dax
= DATE(2008,14,2)  
```
  
### Days  

If **day** is greater than the number of days in the month specified, **day** adds that number of days to the first day in the month. The following formula returns the date February 4, 2008:  

```dax
= DATE(2008,1,35)  
```



## See also

[Date and time functions](date-and-time-functions-dax.md)  
[DAY function](day-function-dax.md)  
[TODAY function](today-function-dax.md)
