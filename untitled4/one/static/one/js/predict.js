function goPredict(){
    //alert('goPredict');
    $("#content").load("predictions/ #predict")
}
function goStrategy(){
    //alert('goPredict');
    $("#content").load("strategy/ #strategy")
}
function goAbout(){
    //alert('goPredict');
    $("#content").load("about/ #about")
}
function goAboutFromPredictions(){
    //alert('goPredict');
    $("#content").load("about/ #about")
}

$('#strategy1').on('click',function(){
$("#variants").load("../variants/ #strategy1")
})
$('#strategy2').on('click',function(){
$("#variants").load("../variants/ #strategy2")
})
$('#strategy3').on('click',function(){
$("#variants").load("../variants/ #strategy3")
})


/*document.getElementById("strategy1").onclick=function(){
    alert("Стратегия1")
}
document.getElementById("strategy2").onclick=function(){
    alert("Стратегия2")
}
document.getElementById("strategy3").onclick=function(){
    alert("Стратегия3")
}*/
