---
description: "Learn more about: DateTimeZone.FixedLocalNow"
title: "DateTimeZone.FixedLocalNow"
---
# DateTimeZone.FixedLocalNow

## Syntax

<pre>
DateTimeZone.FixedLocalNow() as datetimezone
</pre>

## About

Returns a `datetime` value set to the current date and time on the system. The returned value contains timezone information representing the local timezone. This value is fixed and will not change with successive calls, unlike [DateTimeZone.LocalNow](datetimezone-localnow.md), which may return different values over the course of execution of an expression.
