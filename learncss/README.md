## [../](../)

#  [CSS (Cascaded Style Sheets)](https://github.com/LafeLabs/pi/blob/main/learncss/README.md)

[raw version of this markdown file](https://raw.githubusercontent.com/LafeLabs/pi/main/learncss/README.md)

[w3schools.com CSS tutorial](https://www.w3schools.com/w3css/)

[codepen.io online html social coding site with amazing CSS examples](https://codepen.io/)

[code server with example CSS code](codeserver/)

[code server code/index.html page](codeserver/code/)


## Goals

1. learn what CSS is, how to put a style into a html file
2. use an external css file, put it into the code server
3. make art with divs
4. make landscape and portrait modes for a page
5. make buttons with hover and active
6. create and share on codepen.io
7. create a custom style sheet to use for yourself, publish
9. define and control classes
10. define and control id's
12. control how tags look

## A sequence of random snippets

[code/index.html](code/index.html)

this is what goes in "head" to add links to the css files.
```
 <link rel="stylesheet" href="box.css"> 
 <link rel="stylesheet" href="body.css"> 
 <link rel="stylesheet" href="scroll.css"> 
 <link rel="stylesheet" href="classes.css"> 
 <link rel="stylesheet" href="aspectratio.css">
```

Formatting a box:

```
#box{
    font-size:8em;
    font-family:courier;
    color:#ff40c0;
    position:absolute;
    top:50%;
    left:50%;
    transform:rotate(110deg);
    border:solid;
    border-color:#00ff00;
    border-width:10px;
}
```

formatting a scroll:

```
#scroll{
    overflow-y:scroll;
    color:#00ff00;
    left:2em;
    top:2em;
    width:200px;
    height:200px;
    background-color:#303030;
}
```

making buttons, using class formatting:

```
.button{
    color:#00ff00;
    font-family:courier;
    font-size:1.5em;
    border:solid;
    border-color:#0000ff80;
    width:10em;
    height:3em;
    background-color:#808080;
    border-width:10px;
    text-align:center;
    cursor:pointer;
}
.data{
    display:none;
}
.button:hover{
    border-width:20px;
    background-color:#8080ff;
}
.button:active{
    background-color:yellow;
}
.textd{
    color:#ffc040;
    background-color:#404040;
    padding-left:3em;
    padding-top:3em;
}
```

using CSS to make the aspect ratio control appearance, using invisible classes

```
@media only screen and (orientation: landscape) {
    .landscape{
        display:block;
    }
    .portrait{
        display:none;
    }

    
}
@media only screen and (orientation: portrait) {
    .landscape{
        display:none;
    }
    .portrait{
        display:block;
    }
}
```