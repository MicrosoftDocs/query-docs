---
description: "Learn more about: Web.BrowserContents"
title: "Web.BrowserContents | Microsoft Docs"
ms.date: 2/13/2020
ms.service: powerquery
ms.reviewer: gepopell
ms.topic: reference
author: dougklopfenstein
ms.author: bezhan

---
# Web.BrowserContents

## Syntax

<pre>
Web.BrowserContents(<b>url</b> as text, optional <b>options</b> as nullable record) as text
</pre>
  
## About  

Returns the HTML for the specified `url`, as viewed by a web browser. An optional record parameter, `options`, may be provided to specify additional properties. The record can contain the following fields:

* `WaitFor`: Specifies a condition to wait for before downloading the HTML, in addition to waiting for the page to load (which is always done). Can be a record containing Timeout and/or Selector fields. If only a Timeout is specified, the function will wait the amount of time specified before downloading the HTML. If both a Selector and Timeout are specified, and the Timeout elapses before the Selector exists on the page, an error will be thrown. If a Selector is specified with no Timeout, a default Timeout of 30 seconds is applied.

## Example 1
Returns the HTML for https://microsoft.com.

```
Web.BrowserContents("https://microsoft.com")
```

```
"<!DOCTYPE html><html xmlns=..."
```

## Example 2
Returns the HTML for https://microsoft.com after waiting for a CSS selector to exist.

```
Web.BrowserContents("https://microsoft.com", [WaitFor = [Selector = "div.ready"]])
```

```
"<!DOCTYPE html><html xmlns=..."
```

## Example 3
Returns the HTML for https://microsoft.com after waiting ten seconds.

```
Web.BrowserContents("https://microsoft.com", [WaitFor = [Timeout = #duration(0,0,0,10)]])
```

```
"<!DOCTYPE html><html xmlns=..."
```

## Example 4
Returns the HTML for https://microsoft.com after waiting up to ten seconds for a CSS selector to exist.

```
Web.BrowserContents("https://microsoft.com", [WaitFor = [Selector = "div.ready", Timeout = #duration(0,0,0,10)]])
```

```
"<!DOCTYPE html><html xmlns=..."
```
