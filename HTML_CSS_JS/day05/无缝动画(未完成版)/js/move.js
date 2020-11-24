window.onload = function(){
    var list = document.getElementById("list");
    var speed = -1;
    list.innerHTML=list.innerHTML+list.innerHTML;
    var olistLeft = 0;
    var btn01 = document.getElementById("btn01");
    var btn02 = document.getElementById("btn02");
    var otimer = null;
    function move(){
      olistLeft += speed;
        if (olistLeft<-1000){
            olistLeft =0;
        }else if(olistLeft>0){
            olistLeft=-1000;
        }
        list.style.left =  olistLeft+"px";
    }
    otimer=setInterval(move,16.666);
    btn02.onclick = function () {
        speed = 1;
    };
    btn01.onclick = function () {
        speed = -1;
    };
    list.onmouseover=function () {
        clearInterval(otimer)
    };
    list.onmouseout = function () {
        otimer=setInterval(move,16.666);
    }
};