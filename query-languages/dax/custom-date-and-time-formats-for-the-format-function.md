---
title: "Custom date and time formats for the FORMAT function | Microsoft Docs"
ms.service: powerbi 
ms.date: 06/30/2020
ms.reviewer: owend
ms.topic: reference
author: minewiskan
ms.author: owend

---
# Custom date and time formats for the FORMAT function

The following tables describe characters used to create user-defined date/time formats.

## User-defined date/time formats

|Character|Description|
|:-----|:-----|
|(**:**)|Time separator. In some locales, other characters may be used to represent the time separator. The time separator separates hours, minutes, and seconds when time values are formatted. The actual character used as the time separator in formatted output is determined by your system settings.|
|(**/**)|Date separator. In some locales, other characters may be used to represent the date separator. The date separator separates the day, month, and year when date values are formatted. The actual character used as the date separator in formatted output is determined by your system settings.|
|(**&#x5c;**)|Backslash. Displays the next character as a literal character. So, it's not interpreted as a formatting character.|
|(**"**)|Double quote. Text enclosed within double quotes is displayed. So, it's not interpreted as formatting characters.|
|c|Display the date as `ddddd` and display the time as `ttttt`, in that order. Display only date information if there is no fractional part to the date serial number; display only time information if there is no integer portion.|
|d|Display the day as a number without a leading zero (1-31).|
|dd|Display the day as a number with a leading zero (01-31).|
|ddd|Display the day as an abbreviation (Sun-Sat). Localized.|
|dddd|Display the day as a full name (Sunday-Saturday). Localized.|
|ddddd|Display the date as a complete date (including day, month, and year), formatted according to your system's short date format setting. The default short date format is  `mm/dd/yyyy`.|
|dddddd|Display a date serial number as a complete date (including day, month, and year) formatted according to the long date setting recognized by your system. The default long date format is  `dddd, mmmm d, yyyy`.|
|w|Display the day of the week as a number (1 for Sunday through 7 for Saturday).|
|ww|Display the week of the year as a number (1-54).|
|m|Display the month as a number without a leading zero (1-12). If `m` immediately follows `h` or `hh`, minute rather than the month is displayed.|
|mm|Display the month as a number with a leading zero (01-12). If `mm` immediately follows `h` or `hh`, minute rather than the month is displayed. |
|mmm|Display the month as an abbreviation (Jan-Dec). Localized.|
|mmmm|Display the month as a full month name (January-December). Localized.|
|q|Display the quarter of the year as a number (1-4).|
|y|Display the day of the year as a number (1-366).|
|yy|Display the year as a 2-digit number (00-99).|
|yyyy|Display the year as a 4-digit number (100-9999).|
|h|Display the hour as a number without a leading zero (0-23).|
|hh|Display the hour as a number with a leading zero (00-23).|
|n|Display the minute as a number without a leading zero (0-59).|
|nn|Display the minute as a number with a leading zero (00-59).|
|s|Display the second as a number without a leading zero (0-59).|
|ss|Display the second as a number with a leading zero (00-59).|
|ttttt|Display a time as a complete time (including hour, minute, and second), formatted using the time separator defined by the time format recognized by your system. A leading zero is displayed if the leading zero option is selected and the time is before 10:00 A.M. or P.M. The default time format is `h:mm:ss`.|
|AM/PM|Use the 12-hour clock and display an uppercase AM with any hour before noon; display an uppercase PM with any hour between noon and 11:59 P.M.|
|am/pm|Use the 12-hour clock and display a lowercase AM with any hour before noon; display a lowercase PM with any hour between noon and 11:59 P.M.|
|A/P|Use the 12-hour clock and display an uppercase A with any hour before noon; display an uppercase P with any hour between noon and 11:59 P.M.|
|a/p|Use the 12-hour clock and display a lowercase A with any hour before noon; display a lowercase P with any hour between noon and 11:59 P.M.|
|AMPM|Use the 12-hour clock and display the AM string literal as defined by your system with any hour before noon; display the PM string literal as defined by your system with any hour between noon and 11:59 P.M. AMPM can be either uppercase or lowercase, but the case of the string displayed matches the string as defined by your system settings. The default format is AM/PM. If your system is set to 24-hour clock, the string is typical set to an empty string.|

## Remarks

Date/time formatting uses the current user locale to format the string. For example, consider the date June 25, 2020. When it's formatted using format string "m/d/yyyy" it will be:

- User locale is United States of America (en-US): "6/25/2020"
- User locale is Germany (de-DE): "6.25.2020"

## Examples

The following examples use the date/time Thursday, June 25, 2020, at 1:23:45 PM.

|Format string|Result (en-US)|Result (de-DE)|
|-------------|--------------|--------------|
|`"c"`|06/25/2020 13:23:45|25.06.2020 13:23:45|
|`"d"`|25|25|
|`"dd"`|25|25|
|`"ddd"`|Thu|Do|
|`"dddd"`|Thursday|Donnerstag|
|`"ddddd"`|06/25/2020|25.06.2020|
|`"dddddd"`|Thursday, June 25, 2020|Donnerstag, 25. Juni 2020|
|`"w"`|5|4|
|`"ww"`|26|26|
|`"m"`|6|6|
|`"mm"`|06|06|
|`"mmm"`|Jun|Jun|
|`"mmmm"`|June|Juni|
|`"q"`|2|2|
|`"y"`|177|177|
|`"yy"`|20|20|
|`"yyyy"`|2020|2020|
|`"""Year"" yyyy"`|Year 2020|Year 2020|
|`"yyyy \Qq"`|2020 Q2|2020 Q2|
|`"dd/mm/yyyy"`|25/06/2020|25.06.2020|
|`"mm/dd/yyyy"`|06/25/2020|06.25.2020|
|`"h:nn:ss"`|13:23:45|13:23:45|
|`"h:nn:ss AMPM"`|1:23:45 PM|1:23:45 <sup>1</sup>|
|`"hh:nn:ss"`|13:23:45|13:23:45|
|`"hh:nn:ss AMPM"`|01:23:45 PM|01:23:45 <sup>1</sup>|
|`"ttttt"`|13:23:45|13:23:45|
|`"ttttt AMPM"`|13:23:45 PM|13:23:45|
|`"mm/dd/yyyy hh:nn:ss AMPM"`|06/25/2020 01:23:45 PM|6.25.2020 01:23:45|

<sup>1</sup> Germany uses a 24-hour system, and there's no equivalent of AM/PM.

## See also

- [FORMAT function (DAX)](format-function-dax.md)
- [Pre-defined date and time formats for the FORMAT function](pre-defined-date-and-time-formats-for-the-format-function.md)
