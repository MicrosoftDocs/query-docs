---
title: "TIME function (DAX) | Microsoft Docs"
ms.service: powerbi 
ms.date: 12/10/2018
ms.reviewer: owend
ms.topic: reference
author: minewiskan
ms.author: owend

---
# TIME
Converts hours, minutes, and seconds given as numbers to a time in **datetime** format.  
  
## Syntax  
  
```dax
TIME(hour, minute, second)  
```
  
### Parameters  
  
|Term|Definition|  
|--------|--------------|  
|hour|A number from 0 to 23 representing the hour.<br /><br />Any value greater than 23 will be divided by 24 and the remainder will be treated as the hour value.|  
|minute|A number from 0 to 59 representing the minute.<br /><br />Any value greater than 59 will be converted to hours and minutes.|  
|second|A number from 0 to 59 representing the second.<br /><br />Any value greater than 59 will be converted to hours, minutes, and seconds.|  
  
## Return value  
A time (**datetime**).  
  
## Remarks  
In contrast to Microsoft Excel, which stores dates and times as serial numbers, DAX works with date and time values in a **datetime** format. Numbers in other formats are implicitly converted when you use a date/time value in a DAX function. If you need to use serial numbers, you can use formatting to change the way that the numbers are displayed.  
  
Time values are a portion of a date value, and in the serial number system are represented by a decimal number. Therefore, the **datetime** value 12:00 PM is equivalent to 0.5, because it is half of a day.  
  
You can supply the arguments to the TIME function as values that you type directly, as the result of another expression, or by a reference to a column that contains a numeric value. The following restrictions apply:  
  
-   Any value for **hours** that is greater than 23 will be divided by 24 and the remainder will be treated as the hour value.  
  
-   Any value for **minutes** that is greater than 59 will be converted to hours and minutes.  
  
-   Any value for **seconds** that is greater than 59 will be converted to hours, minutes, and seconds.  
  
-   For minutes or seconds, a value greater than 24 hours will be divided by 24 and the reminder will be treated as the hour value. A value in excess of 24 hours does not alter the date portion.  
  
To improve readability of the time values returned by this function, it's recommended that you format the column or PivotTable cell that contains the results of the formula by using one of the time formats provided by Microsoft Excel.  
  
This DAX function may return different results when used in a model that is deployed and then queried in DirectQuery mode. For more information about semantic differences in DirectQuery mode, see  [https://go.microsoft.com/fwlink/?LinkId=219171](https://go.microsoft.com/fwlink/?LinkId=219171).  
  
## Example  
The following examples both return the time, 3:00 AM:  
  
```dax
=TIME(27,0,0)   
=TIME(3,0,0)  
```
  
## Example  
The following examples both return the time, 12:30 PM:  
  
```dax
=TIME(0,750,0)   
=TIME(12,30,0)  
```
  
## Example  
The following example creates a time based on the values in the columns, `intHours`, `intMinutes`, `intSeconds`:  
  
```dax
=TIME([intHours],[intMinutes],[intSeconds])  
```
  
## See also  
[DATE function &#40;DAX&#41;](date-function-dax.md)  
[Date and time functions &#40;DAX&#41;](date-and-time-functions-dax.md)  
  
