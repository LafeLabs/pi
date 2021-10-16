## [../](../)


## [code server](codeserver/)

#  JavaScript: Actions on the Web

JavaScript is the programming language which allows *actions* to happen in a web page.  It can manipulate HTML elements, manipulate CSS styles, do math, and interact with the file system on the server.  Any action, such as the response of a button, is done with JavaScript.  JavaScript is not based on Java, it is named what it is to piggyback on the hype from Java for marketing purposes.  It is loosely "c like" in the sense that much of the syntax is familiar if you've used C, C++, C#, or Java, and will look weird if you've only ever done Python.  

As with all of the web development in this curriculum, the best resources for JavaScript are [w3schools.com](https://www.w3schools.com/) for learning, [Mozilla Development Network](https://developer.mozilla.org/en-US/) for reference, and [codepen.io](https://codepen.io/) for examples.  

A big part of what makes JavaScript powerful is free open source libraries which we can all access via online resources or download and use locally.  There are a *lot* of these!   If you want to do something in a web browser you can often do a web search for "[thing you want to do] open source javascript library" and find fantastic resources.  

The main JavaScript libraries we use in the system presented here are:

 - [ace.js](https://ace.c9.io/) for code editors with syntax hightlighting
 - [showdown.js](http://showdownjs.com/) for conversion between Markdown and HTML
 - [hammer.js](https://hammerjs.github.io/) for touch and mouse movement of graphics
 - [qrcode.js](https://github.com/davidshimjs/qrcodejs) for generating QR codes
 - [mathjax.js](https://www.mathjax.org/) for math typesetting
 - [p5.js](https://p5js.org/), a JavaScript version of the artist-centered programming language [processing](https://processing.org/)
 - mapfactory.js, documented in the [Book of Geometron](https://www.trashrobot.org)
 - geometron.js, documented in the [Book of Geometron](https://www.trashrobot.org)

The main ways to use JavaScript in a web page are to either include reference to an address of a library in the `head` element at the top of an HTML document or to use the script tag with code inside it.  For example:

```
    <script src = "https://cdnjs.cloudflare.com/ajax/libs/
qrcodejs/1.0.0/qrcode.min.js"></script>
```

or for a local library

```
    <script src = "jscode/geometron.js"></script>
```

But if you want to make a program inside the main body of an HTML file, just put code between the script tags as follows:

```
<script>
alert("hello, world");
</script>
```

## goals

 - create a self-replicating calculator
 - create a variant of wall
 - create your own QR code server
 - create a collection of buttons which control things
 - create a feed of text
 - use the showdown js library(markdown)
 - use the qrcode js library
 - use the hammer js library(maps)
 - use ace.js library(understand editor and code server)
 - map factory js library
 - geometron js library
 - make a p5js sketch, learn p5js from the p5js community
 - use mathjax to make a math feed of little equations as social media

## elements

 - functions
 - variables and types
 - boolean and bitwise math
 - for loops, arrays and string loops
 - strings
 - DOM, id, class, etc
 - events: onclick, onchange, onkeydown, onkeyup, onkeypress
 - manipulating inputs
 - connecting with PHP to control file system on server
 - style controls, innerWidth, innerHeight
 - canvas and svg, relation to symbol server
 
[fork.html](fork.html)



