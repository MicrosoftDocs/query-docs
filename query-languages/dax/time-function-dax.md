---
description: "Learn more about: TIME"
title: "TIME function (DAX) | Microsoft Docs"
ms.service: powerbi 
ms.date: 08/06/2021
ms.reviewer: owend
ms.topic: reference
author: minewiskan
ms.author: owend 
recommendations: false

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

- In contrast to Microsoft Excel, which stores dates and times as serial numbers, DAX works with date and time values in a **datetime** format. Numbers in other formats are implicitly converted when you use a date/time value in a DAX function. If you need to use serial numbers, you can use formatting to change the way that the numbers are displayed.  
  
- Time values are a portion of a date value, and in the serial number system are represented by a decimal number. Therefore, the **datetime** value 12:00 PM is equivalent to 0.5, because it is half of a day.  
  
- You can supply the arguments to the TIME function as values that you type directly, as the result of another expression, or by a reference to a column that contains a numeric value. The following restrictions apply:   
  - Any value for **hours** that is greater than 23 will be divided by 24 and the remainder will be treated as the hour value.  
  - Any value for **minutes** that is greater than 59 will be converted to hours and minutes.  
  - Any value for **seconds** that is greater than 59 will be converted to hours, minutes, and seconds.  
  - For minutes or seconds, a value greater than 24 hours will be divided by 24 and the reminder will be treated as the hour value. A value in excess of 24 hours does not alter the date portion.  

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
  
## See also

[DATE](date-function-dax.md)  
[Date and time functions](date-and-time-functions-dax.md)  
