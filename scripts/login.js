/* ------------------------------------ Click on login and Sign Up to  changue and view the effect
---------------------------------------
*/

function cambiar_login() {
  document.querySelector('.form_open').className = "form_open form_active_tl";
document.querySelector('.form_open_tl').style.display = "block";
document.querySelector('.form_open_sl').style.opacity = "0";

setTimeout(function(){  document.querySelector('.form_open_tl').style.opacity = "1"; },400);

setTimeout(function(){
document.querySelector('.form_open_sl').style.display = "none";
},200);
  }

function cambiar_sign_up() {
  document.querySelector('.form_open').className = "form_open form_active_sl";
  document.querySelector('.form_open_sl').style.display = "block";
document.querySelector('.form_open_tl').style.opacity = "0";

setTimeout(function(){  document.querySelector('.form_open_sl').style.opacity = "1"; },400);

setTimeout(function(){   document.querySelector('.form_open_tl').style.display = "none";
},200);


}



function ocultar_login_sign_up() {

document.querySelector('.form_open').className = "form_open";
document.querySelector('.form_open_sl').style.opacity = "0";
document.querySelector('.form_open_tl').style.opacity = "0";

setTimeout(function(){
document.querySelector('.form_open_sl').style.display = "none";
document.querySelector('.form_open_tl').style.display = "none";
},500);

  }
