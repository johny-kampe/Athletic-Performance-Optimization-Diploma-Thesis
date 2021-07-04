let img;
let poseNet;

function setup(){
  createCanvas(640, 480);
  img = loadImage('data/runner.jpg');
  //poseNet = ml5.poseNet(img, modelLoaded);
}

function modelLoaded() {
  console.log('poseNet is ready !!!');
}

function draw() {
  background(0);
  image(img,0,0,width,height);
  
}