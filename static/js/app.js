// Select The Elements
var toggle_btn;
var big_wrapper;
var hamburger_menu;

function declare() {
  toggle_btn = document.querySelector(".toggle-btn");
  big_wrapper = document.querySelector(".big-wrapper");
  hamburger_menu = document.querySelector(".hamburger-menu");
}

const main = document.querySelector("main");

declare();

let dark = false;

function toggleAnimation() {
  // Clone the wrapper
  dark = !dark;
  let clone = big_wrapper.cloneNode(true);
  if (dark) {
    clone.classList.remove("light");
    clone.classList.add("dark");
  } else {
    clone.classList.remove("dark");
    clone.classList.add("light");
  }
  clone.classList.add("copy");
  main.appendChild(clone);

  document.body.classList.add("stop-scrolling");

  clone.addEventListener("animationend", () => {
     document.body.classList.remove("stop-scrolling");
     big_wrapper.remove();
     clone.classList.remove("copy");
    // Reset Variables   //
     declare();
     events();
     
   });
   //active hover 
   let links = document.querySelectorAll(".links a");
let bodyid = document.querySelector("body").id;
for(let link of links){
  if(link.dataset.active ==bodyid) {
    link.classList.add("active");
  }
}
 
  
  //detels img function
  const imgs =document.querySelectorAll('.img-select  a');
const imgBtns = [...imgs];
let imgId = 1;
imgBtns.forEach((imgItem) => {
  imgItem.addEventListener('click' , (event) =>{
   // event.preventDefault();
    imgId = imgItem.dataset.id;
    slideImage();
  } );
});
function slideImage(){
  const displaywidth =document.querySelector('.img-showcase img:first-child').clientWidth;
  document.querySelector('.img-showcase').style.transform = 
  ` translateX(${- (imgId - 1) * displaywidth}px) `;
  
}
//detels img function
}

function events() {
  toggle_btn.addEventListener("click", toggleAnimation);
  hamburger_menu.addEventListener("click", () => {
    big_wrapper.classList.toggle("active");
  });
}

events();

let links = document.querySelectorAll(".links a");
let bodyid = document.querySelector("body").id;
for(let link of links){
  if(link.dataset.active == bodyid) {
    link.classList.add("active");
  }
}
//  var links = document.querySelectorAll('.links ul li a ');
// links.forEach(function (element) {
//   element.addEventListener('click', function (e) {
//     // PreventDefault to prevent redirect
//     //e.preventDefault();
//     links.forEach(function (element) {
//       element.classList.remove('active');
//     });
//     classList.add('active');
//   });
// });

//detels img function
const imgs =document.querySelectorAll('.img-select  a');
const imgBtns = [...imgs];
let imgId = 1;
imgBtns.forEach((imgItem) => {
  imgItem.addEventListener('click' , (event) =>{
   // event.preventDefault();
    imgId = imgItem.dataset.id;
    slideImage();
  } );
});
function slideImage(){
  const displaywidth =document.querySelector('.img-showcase img:first-child').clientWidth;
  document.querySelector('.img-showcase').style.transform = 
  ` translateX(${- (imgId - 1) * displaywidth}px) `;
  
}
//detels img function

















