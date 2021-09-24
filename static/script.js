
var countdownEl= document.getElementById('countdown');
var total_time=25;
var time= total_time * 60;
var minutes; var seconds;
var myvar=-1;

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
    if (myvar==-1)
    {myvar=setInterval(updateCountdown, 1000);}
    else
    {clearInterval(myvar);
        myvar=-1;}
    
    
}

function updateCountdown()
{ 
   minutes= Math.floor(time/60);
   seconds= time % 60;
   if (seconds<10){seconds= "0"+seconds;}
   countdownEl.innerHTML= `${minutes}:${seconds}`;
   time--;
}








