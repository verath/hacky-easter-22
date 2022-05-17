# Fire Alert

> In case of fire, break the glass and press the button.
> 
> http://46.101.107.117:2204

Website has a single button that when clicked redirects to youtube. Looking
through the source we find the script file, and in it we find a `console.log`
command that looks interesting.

index.html:
```
<!DOCTYPE html><html><head><title>Fire Alert</title><script type="text/javascript" src="script.js"></script><link rel="preconnect" href="https://fonts.gstatic.com"><link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Bebas+Neue&amp;display=swap"><link rel="stylesheet" href="styles.css"></head><body><button onclick="firealert()">FIRE ALERT</button></body></html>
```

script.js:
```
function firealert() {
    console.log("%c x", "color:transparent; border-left: 1000px solid lightgreen;");console.log("%c x", "color:transparent; border-left: 1000px solid blue;");
    console.log("%c x", "color:transparent; border-left: 1000px solid red;");console.log("%c x", "color:transparent; border-left: 1000px solid tomato;");
    console.log("%c x", "color:transparent; border-left: 1000px solid darkgray;");console.log("%c x", "color:transparent; border-left: 1000px solid yellow;");
    console.log("%c x", "color:transparent; border-left: 1000px solid black;");console.log(atob("JWMgZmxhZzogaGUyMDIye3RoMXNfZmw0Z18xc19ibDRja19uMHR9"), "color:transparent; border-left: 1000px solid magenta;");
    console.log("%c x", "color:transparent; border-left: 1000px solid purple;");console.log("%c x", "color:transparent; border-left: 1000px solid lightblue;");
    console.log("%c x", "color:transparent; border-left: 1000px solid green;");console.log("%c x", "color:transparent; border-left: 1000px solid gray;");
    window.location.href='https://www.youtube.com/watch?v=0oBx7Jg4m-o';
}
setInterval(function() {
    document.body.style.backgroundColor = "#" + Math.floor(Math.random()*16777215).toString(16);
}, 1000)
```

The `atob("JWMgZmxhZzogaGUyMDIye3RoMXNfZmw0Z18xc19ibDRja19uMHR9")` when
evaluated gives us the flag:

`he2022{th1s_fl4g_1s_bl4ck_n0t}`
