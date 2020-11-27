function add(){
    var x = parseInt(document.getElementById('n1').value);
    var y = parseInt(document.getElementById('n2').value);
    document.getElementById('res').innerHTML=x+y;

}

function multiply(){
    var p = parseInt(document.getElementById('n1').value);
    var q = parseInt(document.getElementById('n2').value);
    document.getElementById('res').innerHTML=p*q
}
function divide(){
    var a = parseInt(document.getElementById('n1').value);
    var b = parseInt(document.getElementById('n2').value);
    document.getElementById('res').innerHTML=a/b; //divides andgives the result
}

function substract(){
    var r = parseInt(document.getElementById('n1').value);
    var t = parseInt(document.getElementById('n2').value);
    document.getElementById('res').innerHTML=r-t;
}