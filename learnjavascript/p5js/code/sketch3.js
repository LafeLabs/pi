let x = 100;
let y = 100;
let imgx = 0;
let imgy = 0;
let delta = 10;
let img;
let img2;
function preload() {
  img = loadImage('https://i.imgur.com/Mtgj8R8.png');
  img2 = loadImage('https://i.imgur.com/No1wukK.png');
}

function setup() {
  if(innerWidth > innerHeight){
      createCanvas(innerHeight,innerHeight);
  }
  else{
      createCanvas(innerWidth,innerWidth);
  }
    image(img, 0, 0);

  //fill(255, 0, 0);
}

function draw() {
  if (keyIsDown(LEFT_ARROW)) {
    if(keyIsDown(CONTROL)){
        imgx -= delta;
    }
    else{
        x -= delta;
    }

  }
  if (keyIsDown(RIGHT_ARROW)) {
    if(keyIsDown(CONTROL)){
        imgx += delta;
    }
    else{
      x += delta;
    }
  }

  if (keyIsDown(UP_ARROW)) {
    if(keyIsDown(CONTROL)){
        imgy -= delta;
    }
    else{
        y -= delta;
    }
  }

  if (keyIsDown(DOWN_ARROW)) {
    if(keyIsDown(CONTROL)){
        imgy += delta;
    }
    else{
        y += delta;
    }
  }

  clear();
  //http://vineotron.net/images/uploadimages/image1.PNG
  image(img,imgx,imgy);

//  rect(x, y, 50, 50);
  image(img2, x, y, 50, 50);

}
