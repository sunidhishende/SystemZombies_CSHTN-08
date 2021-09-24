
var countdownEl= document.getElementById('countdown');
var total_time=25;
var time= total_time * 60;
var minutes; var seconds;
let myvar;
var y=0;

function task(){
    clearInterval(myvar);
     total_time= 25;
     time=total_time * 60;
     myvar=setInterval(updateCountdown, 1000);
}

function breaks(){
    clearInterval(myvar);
     total_time= 5;
     time=total_time * 60;
     myvar=setInterval(updateCountdown, 1000);
}

function pause(){
    clearInterval(myvar);
}

function updateCountdown()
{ 
   minutes= Math.floor(time/60);
   seconds= time % 60;
   countdownEl.innerHTML= `${minutes}:${seconds}`;
   time--;
}








