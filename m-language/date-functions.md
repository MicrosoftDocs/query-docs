---
title: "Date functions | Microsoft Docs"
ms.custom: ""
ms.date: "12/28/2017"
ms.prod: "powerbi"
ms.reviewer: ""
ms.suite: ""
ms.technology: 
  - "mlang"
ms.tgt_pltfrm: ""
ms.topic: "index-page "
ms.assetid: 7bd71d76-d113-44da-a464-8c68e7a0cae9
caps.latest.revision: 10
author: "Minewiskan"
ms.author: "owend"
manager: "erikre"
---
# Date functions
The Power Query Formula Language is a mashup language for transforming data. It's a functional, case sensitive language similar to F\#. Power Query Formula Language is used in a number of Microsoft products such as Power BI Desktop, Excel, and Analysis Services. To learn more about the language, see [PowerQueryName reference](https://msdn.microsoft.com/en-us/library/mt211003.aspx).  
  
## <a name="__toc360788935"></a>Date  
  
|Function|Description|  
|------------|---------------|  
|[Date.AddDays](../PowerQuery/date-adddays.md)|Returns a Date/DateTime/DateTimeZone value with the day portion incremented by the number of days provided. It also handles incrementing the month and year potions of the value as appropriate.|  
|[Date.AddMonths](../PowerQuery/date-addmonths.md)|Returns a DateTime value with the month portion incremented by n months.|  
|[Date.AddQuarters](../PowerQuery/date-addquarters.md)|Returns a Date/DateTime/DateTimeZone value incremented by the number of quarters provided. Each quarter is defined as a duration of three months. It also handles incrementing the year potion of the value as appropriate.|  
|[Date.AddWeeks](../PowerQuery/date-addweeks.md)|Returns a Date/DateTime/DateTimeZone value incremented by the number of weeks provided. Each week is defined as a duration of seven days. It also handles incrementing the month and year potions of the value as appropriate.|  
|[Date.AddYears](../PowerQuery/date-addyears.md)|Returns a DateTime value with the year portion incremented by n years.|  
|[Date.Day](../PowerQuery/date-day.md)|Returns the day for a DateTime value.|  
|[Date.DayOfWeek](../PowerQuery/date-dayofweek.md)|Returns a number between 0 and 6 representing the day of the week from a DateTime value.| 
|[Date.DayOfWeekName](../PowerQuery/date-dayofweekname.md)|Returns the day of the week name.|  
|[Date.DayOfYear](../PowerQuery/date-dayofyear.md)|Returns a number that represents the day of the year from a DateTime value.|  
|[Date.DaysInMonth](../PowerQuery/date-daysinmonth.md)|Returns the number of days in the month from a DateTime value.|  
|[Date.EndOfDay](../PowerQuery/date-endofday.md)|Returns a DateTime value for the end of the day.|  
|[Date.EndOfMonth](../PowerQuery/date-endofmonth.md)|Returns a DateTime value for the end of the month.|  
|[Date.EndOfQuarter](../PowerQuery/date-endofquarter.md)|Returns a Date/DateTime/DateTimeZone value representing the end of the quarter. The date and time portions are reset to their terminating values for the quarter. The timezone information is persisted.|  
|[Date.EndOfWeek](../PowerQuery/date-endofweek.md)|Returns a DateTime value for the end of the week.|  
|[Date.EndOfYear](../PowerQuery/date-endofyear.md)|Returns a DateTime value for the end of the year.|  
|[Date.From](../PowerQuery/date-from.md)|Returns a date value from a value.|  
|[Date.FromText](../PowerQuery/date-fromtext.md)|Returns a Date value from a set of date formats and culture value.|  
|[Date.IsInCurrentDay](../PowerQuery/date-isincurrentday.md)|Indicates whether the given datetime value <code>dateTime</code> occurs during the current day, as determined by the current date and time on the system.|
|[Date.IsInCurrentMonth](../PowerQuery/date-isincurrentmonth.md)|Returns a logical value indicating whether the given Date/DateTime/DateTimeZone occurred during the current month, as determined by the current date and time on the system.|  
|[Date.IsInCurrentQuarter](../PowerQuery/date-isincurrentquarter.md)|Returns a logical value indicating whether the given Date/DateTime/DateTimeZone occurred during the current quarter, as determined by the current date and time on the system.|  
|[Date.IsInCurrentWeek](../PowerQuery/date-isincurrentweek.md)|Returns a logical value indicating whether the given Date/DateTime/DateTimeZone occurred during the current week, as determined by the current date and time on the system.|  
|[Date.IsInCurrentYear](../PowerQuery/date-isincurrentyear.md)|Returns a logical value indicating whether the given Date/DateTime/DateTimeZone occurred during the current year, as determined by the current date and time on the system.|
|[Date.IsInNextDay](../PowerQuery/date-isinnextday.md)|Indicates whether the given datetime value dateTime occurs during the next day, as determined by the current date and time on the system.|  
|[Date.IsInNextMonth](../PowerQuery/date-isinnextmonth.md)|Returns a logical value indicating whether the given Date/DateTime/DateTimeZone occurred during the next month, as determined by the current date and time on the system.|
|[Date.IsInNextNDays](../PowerQuery/date-isinnextndays.md)|Indicates whether the given datetime value dateTime occurs during the next number of days, as determined by the current date and time on the system.| 
|[Date.IsInNextNMonths](../PowerQuery/date-isinnextnmonths.md)|Indicates whether the given datetime value dateTime occurs during the next number of months, as determined by the current date and time on the system.|
|[Date.IsInNextNQuarters](../PowerQuery/date-isinnextnquarters.md)|Indicates whether the given datetime value dateTime occurs during the next number of quarters, as determined by the current date and time on the system.|
|[Date.IsInNextNWeeks](../PowerQuery/date-isinnextnweeks.md)|Indicates whether the given datetime value dateTime occurs during the next number of weeks, as determined by the current date and time on the system.|
|[Date.IsInNextNYears](../PowerQuery/date-isinnextnyears.md)|Indicates whether the given datetime value dateTime occurs during the next number of years, as determined by the current date and time on the system.|
|[Date.IsInNextQuarter](../PowerQuery/date-isinnextquarter.md)|Returns a logical value indicating whether the given Date/DateTime/DateTimeZone occurred during the next quarter, as determined by the current date and time on the system.|  
|[Date.IsInNextWeek](../PowerQuery/date-isinnextweek.md)|Returns a logical value indicating whether the given Date/DateTime/DateTimeZone occurred during the next week, as determined by the current date and time on the system.|  
|[Date.IsInNextYear](../PowerQuery/date-isinnextyear.md)|Returns a logical value indicating whether the given Date/DateTime/DateTimeZone occurred during the next year, as determined by the current date and time on the system.|  
|[Date.IsInPreviousDay](../PowerQuery/date-isinpreviousday.md)|Indicates whether the given datetime value dateTime occurs during the previous day, as determined by the current date and time on the system.|
|[Date.IsInPreviousMonth](../PowerQuery/date-isinpreviousmonth.md)|Returns a logical value indicating whether the given Date/DateTime/DateTimeZone occurred during the previous month, as determined by the current date and time on the system.|  
|[Date.IsInPreviousNDays](../PowerQuery/date-isinpreviousndays.md)|Indicates whether the given datetime value dateTime occurs during the previous number of days, as determined by the current date and time on the system.|
|[Date.IsInPreviousNMonths](../PowerQuery/date-isinpreviousnmonths.md)|Indicates whether the given datetime value dateTime occurs during the previous number of months, as determined by the current date and time on the system.|
|[Date.IsInPreviousNQuarters](../PowerQuery/date-isinpreviousnquarters.md)|Indicates whether the given datetime value dateTime occurs during the previous number of quarters, as determined by the current date and time on the system.|
|[Date.IsInPreviousNWeeks](../PowerQuery/date-isinpreviousnweeks.md)|Indicates whether the given datetime value dateTime occurs during the previous number of weeks, as determined by the current date and time on the system.|
|[Date.IsInPreviousNYears](../PowerQuery/date-isinpreviousnyears.md)|Indicates whether the given datetime value dateTime occurs during the previous number of years, as determined by the current date and time on the system.|
|[Date.IsInPreviousQuarter](../PowerQuery/date-isinpreviousquarter.md)|Returns a logical value indicating whether the given Date/DateTime/DateTimeZone occurred during the previous quarter, as determined by the current date and time on the system.|  
|[Date.IsInPreviousWeek](../PowerQuery/date-isinpreviousweek.md)|Returns a logical value indicating whether the given Date/DateTime/DateTimeZone occurred during the previous week, as determined by the current date and time on the system.|  
|[Date.IsInPreviousYear](../PowerQuery/date-isinpreviousyear.md)|Returns a logical value indicating whether the given Date/DateTime/DateTimeZone occurred during the previous year, as determined by the current date and time on the system.|  
|[Date.IsInYearToDate](../PowerQuery/date-isinyeartodate.md)|Returns a logical value indicating whether the given Date/DateTime/DateTimeZone occurred in the period starting January 1st of the current year and ending on the current day, as determined by the current date and time on the system.|  
|[Date.IsLeapYear](../PowerQuery/date-isleapyear.md)|Returns a logical value indicating whether the year portion of a DateTime value is a leap year.|  
|[Date.Month](../PowerQuery/date-month.md)|Returns the month from a DateTime value.| 
|[Date.MonthName](../PowerQuery/date-monthname.md)|Returns the name of the month component.|  
|[Date.QuarterOfYear](../PowerQuery/date-quarterofyear.md)|Returns a number between 1 and 4 for the quarter of the year from a DateTime value.|  
|[Date.StartOfDay](../PowerQuery/date-startofday.md)|Returns a DateTime value for the start of the day.|  
|[Date.StartOfMonth](../PowerQuery/date-startofmonth.md)|Returns a DateTime value representing the start of the month.|  
|[Date.StartOfQuarter](../PowerQuery/date-startofquarter.md)|Returns a DateTime value representing the start of the quarter.|  
|[Date.StartOfWeek](../PowerQuery/date-startofweek.md)|Returns a DateTime value representing the start of the week.|  
|[Date.StartOfYear](../PowerQuery/date-startofyear.md)|Returns a DateTime value representing the start of the year.|  
|[Date.ToRecord](../PowerQuery/date-torecord.md)|Returns a record containing parts of a Date value.|  
|[Date.ToText](../PowerQuery/date-totext.md)|Returns a text value from a Date value.|  
|[Date.WeekOfMonth](../PowerQuery/date-weekofmonth.md)|Returns a number for the count of week in the current month.|  
|[Date.WeekOfYear](../PowerQuery/date-weekofyear.md)|Returns a number for the count of week in the current year.|  
|[Date.Year](../PowerQuery/date-year.md)|Returns the year from a DateTime value.|  
  
Parameter values | Description
---------------- | -----------
[Day.Sunday](../PowerQuery/day-sunday.md) | Represents Sunday.
[Day.Monday](../PowerQuery/day-monday.md) | Represents Monday.
[Day.Tuesday](../PowerQuery/day-tuesday.md) | Represents Tuesday.
[Day.Wednesday](../PowerQuery/day-wednesday.md) | Represents Wednesday.
[Day.Thursday](../PowerQuery/day-thursday.md) | Represents Thursday.
[Day.Friday](../PowerQuery/day-friday.md) | Represents Friday.
[Day.Saturday](../PowerQuery/day-saturday.md) | Represents Saturday.