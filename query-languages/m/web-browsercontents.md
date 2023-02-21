---
description: "Learn more about: Web.BrowserContents"
title: "Web.BrowserContents"
ms.date: 2/17/2023
---
# Web.BrowserContents

## Syntax

<pre>
Web.BrowserContents(<b>url</b> as text, optional <b>options</b> as nullable record) as text
</pre>

## About

Returns the HTML for the specified `url`, as viewed by a web browser. An optional record parameter, `options`, may be provided to specify additional properties. The record can contain the following fields:

* `ApiKeyName`: If the target site has a notion of an API key, this parameter can be used to specify the name (not the value) of the key parameter that must be used in the URL. The actual key value is provided in the credential.
* `WaitFor`: Specifies a condition to wait for before downloading the HTML, in addition to waiting for the page to load (which is always done). Can be a record containing Timeout and/or Selector fields. If only a Timeout is specified, the function will wait the amount of time specified before downloading the HTML. If both a Selector and Timeout are specified, and the Timeout elapses before the Selector exists on the page, an error will be thrown. If a Selector is specified with no Timeout, a default Timeout of 30 seconds is applied.

## Example 1

Returns the HTML for https://microsoft.com.

**Usage**

```powerquery-m
Web.BrowserContents("https://microsoft.com")
```

**Output**

`"<!DOCTYPE html><html xmlns=..."`

## Example 2

Returns the HTML for https://microsoft.com after waiting for a CSS selector to exist.

**Usage**

```powerquery-m
Web.BrowserContents("https://microsoft.com", [WaitFor = [Selector = "div.ready"]])
```

**Output**

`"<!DOCTYPE html><html xmlns=..."`

## Example 3

Returns the HTML for https://microsoft.com after waiting ten seconds.

**Usage**

```powerquery-m
Web.BrowserContents("https://microsoft.com", [WaitFor = [Timeout = #duration(0,0,0,10)]])
```

**Output**

`"<!DOCTYPE html><html xmlns=..."`

## Example 4

Returns the HTML for https://microsoft.com after waiting up to ten seconds for a CSS selector to exist.

**Usage**

```powerquery-m
Web.BrowserContents("https://microsoft.com", [WaitFor = [Selector = "div.ready", Timeout = #duration(0,0,0,10)]])
```

**Output**

`"<!DOCTYPE html><html xmlns=..."`
